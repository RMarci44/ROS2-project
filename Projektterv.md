# ROS2 Projektterv

## Tartalomjegyzék
- [ROS2 Projektterv](#ros2-projektterv)
  - [Tartalomjegyzék](#tartalomjegyzék)
  - [Projekt célja](#projekt-célja)
  - [Ütemterv](#ütemterv)
    - [1. Projektindítás és Tervezés (4. hét)](#1-projektindítás-és-tervezés-4-hét)
    - [2. Fejlesztési Környezet és Alapok (6. hét)](#2-fejlesztési-környezet-és-alapok-6-hét)
    - [3. 3D Modell, URDF és Szenzorok Integrációja (8. hét)](#3-3d-modell-urdf-és-szenzorok-integrációja-8-hét)
    - [4. Gazebo Világ és Navigációs Stack Integrációja (10. hét)](#4-gazebo-világ-és-navigációs-stack-integrációja-10-hét)
    - [5. Egyedi ROS Node és Mozgó Akadályok (12. hét)](#5-egyedi-ros-node-és-mozgó-akadályok-12-hét)
    - [6. Integráció, Tesztelés és Dokumentáció (14. hét)](#6-integráció-tesztelés-és-dokumentáció-14-hét)

## Projekt célja
- A projekt célja, hogy egy komplex, sűrűn berendezett szimulációs környezetben (pl. iroda, labor vagy épített tér) integráljuk és behangoljuk a ROS2 navigációs stack-et. 
- A megoldás során a robot autonóm módon térképezi fel a környezetet, és navigál benne, miközben mozgó akadályok (például ember vagy állat) kerülnek szimulálásra. 
- Emellett készítünk egy saját 3D modellt, Collada meshből generált URDF fájlt, illetve bővítjük a meglévő robotmodellt egyedi komponenssel és szenzorral.

## Ütemterv

### 1. Projektindítás és Tervezés (4. hét)
- **Projektfeladat kiválasztása:** A csapat közösen meghatározza a projekt témáját és céljait.
- **Feladatok felbontása:** Részletes feladatlista és munkamegosztás kialakítása.
- **Konzultációk szervezése:** Rendszeres konzultációs időpontok egyeztetése az oktatóval.
- **GitHub repo létrehozása:** A projekt repository létrehozása.

### 2. Fejlesztési Környezet és Alapok (6. hét)
- **Környezeti beállítások:** Colcon workspace létrehozása, függőségek telepítési útmutatójának kidolgozása.
- **Dokumentációs sablon:** README.md elkészítése tartalomjegyzékkel, hivatkozásokkal a használt ROS csomagokra és egyéb forrásokra.

### 3. 3D Modell, URDF és Szenzorok Integrációja (8. hét)
- **3D Modell elkészítése:** Saját 3D modell kidolgozása (vagy meglévő modell egyedi komponenssel történő kiegészítése).
- **Mesh és URDF generálás:** Collada mesh exportálása és URDF fájl készítése.
- **Szenzor szimuláció:** Legalább egy kamera és egy további szenzor integrálása a modellbe, szükséges konfigurációk elvégzése.

### 4. Gazebo Világ és Navigációs Stack Integrációja (10. hét)
- **Gazebo világ építése:** Részletes, berendezett világ modellezése Gazebo-ban (pl. bútorok, épületelemek).
- **Navigációs stack behangolása:** A ROS2 navigációs stack konfigurálása a szimulációs környezethez; paraméterek finomhangolása, térképezési és lokalizációs feladatok tesztelése.

### 5. Egyedi ROS Node és Mozgó Akadályok (12. hét)
- **Egyedi ROS node fejlesztése:** Pythonban vagy C++-ban történő fejlesztés a projekt specifikus feladatainak ellátására (például dinamikus akadályok kezelése).
- **Mozgó akadályok szimulációja:** Dinamikus akadályok (ember, állat) integrálása a Gazebo szimulációba, interakciók tesztelése a navigációs stack-kel.

### 6. Integráció, Tesztelés és Dokumentáció (14. hét)
- **Teljes rendszer integrációja:** Minden komponens (URDF, szenzorok, Gazebo világ, navigációs stack, egyedi node) összehangolása.
- **Hibakeresés és optimalizáció:** Rendszeres tesztelések végrehajtása egy üres colcon workspace-ben, hibák javítása.
- **Bemutató videó készítése:** Legalább 1,5-2,5 perces demo felvétel rögzítése YouTube-ra.
- **Dokumentáció véglegesítése:** README.md és egyéb dokumentációs anyagok frissítése, tartalomjegyzék, képek és hivatkozások beszúrása.
