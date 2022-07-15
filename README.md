# airobo_sample
sample repo during AI robo contest

# Environment
## Environment
### Environment


- Ubuntu 20.04 WSL2
- ROS2 foxy
# Dependencies

```
sudo apt install ros-foxy-turtlesim -y
sudo apt install ros-foxy-robot-state-publisher -y
```

# Build

```
cbp my_first_python_pkg && rosfoxy
```

# Usage

```bash
ros2 run my_first_python_pkg test
```

```python
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
      
```

- [] reference
- [] 연락처