import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import IncludeLaunchDescription


def generate_launch_description():
    broadcaster_listener_nodes = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('launch_tutorial'), 'launch'),
            '/broadcaster_listener_launch.py']),
        launch_arguments={'target_frame': 'carrot1'}.items(),
    )

    return LaunchDescription([
        broadcaster_listener_nodes
    ])
