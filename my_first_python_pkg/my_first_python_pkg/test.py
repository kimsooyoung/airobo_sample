

import rclpy
from rclpy.node import Node
# tutlesim/msg/Pose
from turtlesim.msg import Pose


# float32 x
# float32 y
# float32 theta

# float32 linear_velocity
# float32 angular_velocity

class TurtlePoseSubNode(Node):
    """turtlesim/Pose msg Subscriber Node.

    This node will listen pose topic from turtlesim.
    Then just print them on terminal.
    """

    def __init__(self):
        """Node Initialization.

        You must type name of the node in inheritanced initializer.
        """
        super().__init__('turtlepose_sub_node')

        queue_size = 10  # Queue Size
        # You can create subscriber with create_subscription function
        # this function get those params
        #
        # msg type, topic name, callback function, queue_size
        #
        # topic name must exists and coincident with exact topic name
        self.pose_subscriber = self.create_subscription(
            Pose, 'turtle1/pose', self.sub_callback, queue_size
        )

    def sub_callback(self, msg):
        """Timer will run this function periodically."""
        self.get_logger().info(f"""x : {msg.x:.3f} / y : {msg.y:.3f} / z : {msg.theta:.3f}
        linear_velocity : {msg.linear_velocity} / angular_velocity : {msg.angular_velocity }""")


def main(args=None):
    """Do enter into this main function first."""
    rclpy.init(args=args)

    tp_sub_node = TurtlePoseSubNode()

    rclpy.spin(tp_sub_node)
    # rclpy.spin_once(tp_sub_node)

    tp_sub_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    """main function"""
    main()
