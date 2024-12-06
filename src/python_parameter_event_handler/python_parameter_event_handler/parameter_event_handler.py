import rclpy
import rclpy.node
import rclpy.parameter

from rclpy.parameter_event_handler import ParameterEventHandler


class SampleNodeWithParameters(rclpy.node.Node):
    def __init__(self):
        super().__init__('node_with_parameters')

        self.declare_parameter('an_int_param', 0)

        self.handler = ParameterEventHandler(self)

        self.callback_handle = self.handler.add_parameter_callback(
            parameter_name="a_double_param",
            node_name="parameter_blackboard",
            callback=self.callback,
        )

    def callback(self, p: rclpy.parameter.Parameter) -> None:
        self.get_logger().info(f"Received an update to parameter: {p.name}: {rclpy.parameter.parameter_value_to_python(p.value)}")


def main():
    rclpy.init()
    node = SampleNodeWithParameters()
    rclpy.spin(node)
    rclpy.shutdown()