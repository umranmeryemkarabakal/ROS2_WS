import rclpy
from rclpy.node import Node
from rviz_plugin_tutorial_msg.msg import CustomMessage

class CustomMessagePublisher(Node):
    def __init__(self):
        super().__init__('custom_message_publisher')
        self.publisher_ = self.create_publisher(CustomMessage, 'custom_topic', 10)
        self.timer = self.create_timer(1.0, self.publish_message)

    def publish_message(self):
        msg = CustomMessage()
        msg.x = 1.0
        msg.y = 2.0
        msg.z = 3.0
        msg.label = 'Example Label'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: x={msg.x}, y={msg.y}, z={msg.z}, label={msg.label}')

def main(args=None):
    rclpy.init(args=args)
    node = CustomMessagePublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
