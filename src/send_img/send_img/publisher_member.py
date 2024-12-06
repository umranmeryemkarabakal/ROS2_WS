import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class ImagePublisher(Node):
    def __init__(self):
        super().__init__('image_publisher')
        self.publisher = self.create_publisher(Image, 'image_topic', 10)
        self.bridge = CvBridge()
        self.timer = self.create_timer(1.0, self.publish_image)

    def publish_image(self):
        image_path = '/home/umranmeryem/ros2_ws/src/send_img/resource/img.png'
        image = cv2.imread(image_path)
        
        if image is None:
            self.get_logger().error('Görüntü yüklenemedi')
            return
        # ros formatına dönüştür
        ros_image = self.bridge.cv2_to_imgmsg(image, encoding='bgr8')
        # yayınlar
        self.publisher.publish(ros_image)
        self.get_logger().info('Görüntü yayınlandı')

def main(args=None):
    rclpy.init(args=args)
    node = ImagePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
