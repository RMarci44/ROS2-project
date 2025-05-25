import rclpy
from rclpy.node import Node
from std_srvs.srv import Trigger
from geometry_msgs.msg import PoseStamped
from rclpy.action import ActionClient
from nav2_msgs.action import NavigateToPose
from std_msgs.msg import Bool
from tf_transformations import quaternion_from_euler
import math

class DockingNode(Node):
    def __init__(self):
        super().__init__('docking_node')

        # Declare parameters
        self.declare_parameter('dock_pose.x', 1.0)
        self.declare_parameter('dock_pose.y', 1.0)
        self.declare_parameter('dock_pose.theta_degrees', 0.0)
        self.declare_parameter('dock_pose.frame_id', 'map')

        # Initialize dock pose
        self.dock_pose = PoseStamped()
        self.dock_pose.header.frame_id = self.get_parameter('dock_pose.frame_id').get_parameter_value().string_value
        self.dock_pose.pose.position.x = self.get_parameter('dock_pose.x').get_parameter_value().double_value
        self.dock_pose.pose.position.y = self.get_parameter('dock_pose.y').get_parameter_value().double_value
        theta = math.radians(self.get_parameter('dock_pose.theta_degrees').get_parameter_value().double_value)
        q = quaternion_from_euler(0, 0, theta)
        self.dock_pose.pose.orientation.x = q[0]
        self.dock_pose.pose.orientation.y = q[1]
        self.dock_pose.pose.orientation.z = q[2]
        self.dock_pose.pose.orientation.w = q[3]

        # Services
        self.srv = self.create_service(Trigger, 'dock', self.dock_callback)
        self.undock_srv = self.create_service(Trigger, 'undock', self.undock_callback)

        # Action client
        self._action_client = ActionClient(self, NavigateToPose, 'navigate_to_pose')

        # Publisher for explore/resume topic
        self.explore_resume_pub = self.create_publisher(Bool, 'explore/resume', 10)

    def dock_callback(self, request, response):
        # Stop m-explore
        stop_msg = Bool()
        stop_msg.data = False
        self.explore_resume_pub.publish(stop_msg)
        self.get_logger().info('Dock parancs érkezett, indulás a töltőállomásra!')

        # Send navigation goal
        goal_msg = NavigateToPose.Goal()
        goal_msg.pose = self.dock_pose
        self._action_client.wait_for_server()
        send_goal_future = self._action_client.send_goal_async(goal_msg)

        # Handle goal result asynchronously
        def goal_response_callback(future):
            goal_handle = future.result()
            if not goal_handle.accepted:
                self.get_logger().error('Navigációs cél elutasítva!')
                response.success = False
                response.message = 'Navigációs cél elutasítva!'
                return
            self.get_logger().info('Navigációs cél elfogadva, várakozás az eredményre...')
            get_result_future = goal_handle.get_result_async()
            get_result_future.add_done_callback(result_callback)

        def result_callback(future):
            result = future.result().result
            if result:
                self.get_logger().info('Sikeres dokkolás!')
                response.success = True
                response.message = 'Sikeres dokkolás!'
            else:
                self.get_logger().error('Dokkolás sikertelen!')
                response.success = False
                response.message = 'Dokkolás sikertelen!'

        send_goal_future.add_done_callback(goal_response_callback)
        return response

    def undock_callback(self, request, response):
        # Resume m-explore
        resume_msg = Bool()
        resume_msg.data = True
        self.explore_resume_pub.publish(resume_msg)
        self.get_logger().info('Undock parancs érkezett, m-explore folytatódik!')
        response.success = True
        response.message = 'Sikeres undock, m-explore folytatódik!'
        return response

def main(args=None):
    rclpy.init(args=args)
    node = DockingNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()