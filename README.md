# ROS2_WS

<p>
  <img src="https://img.shields.io/badge/ROS%202-22314E?style=for-the-badge&logo=ros&logoColor=white" alt="ROS 2" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
</p>

## Overview

A ROS 2 workspace of tutorial packages worked through while learning ROS 2: publishers and subscribers, services, actions, custom interfaces, parameters, launch files, tf2, URDF and RViz.

**Quick start:** `colcon build && source install/setup.bash`

## Proje hakkında

ROS 2 öğrenirken resmi eğitimler takip edilerek yazılmış paketlerden oluşan çalışma alanı.

## Paketler

- `py_pubsub`: yayıncı / abone
- `py_srvcli`: servis sunucu / istemci
- `custom_action_interfaces`, `tutorial_interfaces`, `rviz_plugin_tutorial_msg`: özel mesaj, servis ve action tanımları
- `python_parameters`, `python_parameter_event_handler`: parametreler ve parametre olayları
- `launch_tutorial`, `py_launch_example`: launch dosyaları
- `learning_tf2_py`: tf2 yayıncı / dinleyici
- `urdf_tutorial_r2d2`: URDF modeli ve durum yayıncısı
- `send_img`: `cv_bridge` ile görüntü yayını
- `my_package`, `my_test_package`: ilk paket denemeleri

## Kurulum ve çalıştırma

```bash
cd ROS2_WS
rosdep install --from-paths src -y --ignore-src
colcon build
source install/setup.bash

ros2 run py_pubsub talker        # örnek
```

## Dosya yapısı

```text
ROS2_WS/
└── src/
    ├── custom_action_interfaces/  (4 dosya)
    ├── launch_tutorial/  (22 dosya)
    ├── learning_tf2_py/  (17 dosya)
    ├── my_package/  (10 dosya)
    ├── my_test_package/  (8 dosya)
    ├── py_launch_example/  (10 dosya)
    ├── py_pubsub/  (13 dosya)
    ├── py_srvcli/  (13 dosya)
    ├── python_parameter_event_handler/  (10 dosya)
    ├── python_parameters/  (10 dosya)
    ├── rviz_plugin_tutorial_msg/  (11 dosya)
    ├── send_img/  (14 dosya)
    ├── tutorial_interfaces/  (6 dosya)
    ├── urdf_tutorial_r2d2/  (13 dosya)
    ├── ros_tutorials
    └── urdf_tutorial
```
