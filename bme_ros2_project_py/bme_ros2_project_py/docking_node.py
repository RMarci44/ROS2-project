import rclpy
from rclpy.node import Node
from std_srvs.srv import Trigger
from geometry_msgs.msg import PoseStamped
from rclpy.action import ActionClient
from nav2_msgs.action import NavigateToPose

class DockingNode(Node):
    def __init__(self):
        super().__init__('docking_node')
        self.srv = self.create_service(Trigger, 'dock', self.dock_callback)
        self._action_client = ActionClient(self, NavigateToPose, 'navigate_to_pose')
        # Állomás pozíciója (példaérték, ezt testre kell szabni)
        self.dock_pose = PoseStamped()
        self.dock_pose.header.frame_id = 'map'
        self.dock_pose.pose.position.x = 1.0
        self.dock_pose.pose.position.y = 2.0
        self.dock_pose.pose.orientation.w = 1.0

    def dock_callback(self, request, response):
        self.get_logger().info('Dock parancs érkezett, indulás a töltőállomásra!')
        goal_msg = NavigateToPose.Goal()
        goal_msg.pose = self.dock_pose
        self._action_client.wait_for_server()
        send_goal_future = self._action_client.send_goal_async(goal_msg)
        rclpy.spin_until_future_complete(self, send_goal_future)
        goal_handle = send_goal_future.result()
        if not goal_handle.accepted:
            response.success = False
            response.message = 'Navigációs cél elutasítva!'
            return response
        get_result_future = goal_handle.get_result_async()
        rclpy.spin_until_future_complete(self, get_result_future)
        result = get_result_future.result().result
        response.success = True
        response.message = 'Sikeres dokkolás!'
        return response

def main(args=None):
    rclpy.init(args=args)
    node = DockingNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
