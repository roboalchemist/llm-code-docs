# Source: https://docs.edgeimpulse.com/projects/expert-network/ros2-part1-pubsub-node.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# ROS2 + Edge Impulse, Part 1: Pub/Sub Node in Python

Created By: Avi Brown

Public Project Link: [https://studio.edgeimpulse.com/public/108508/latest](https://studio.edgeimpulse.com/public/108508/latest)

GitHub Repository: [https://github.com/avielbr/edge-impulse/tree/main/ros2/ei\_ros2](https://github.com/avielbr/edge-impulse/tree/main/ros2/ei_ros2)

<iframe src="https://www.youtube.com/embed/0SabLvJqSaM" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

### Background

ROS2 is the world’s most popular robotics development framework. It enables developers to build organized, modular, and scalable robotics platforms with the full force of the open source community behind it. When developing a new robot, it’s common to recycle existing ROS2 packages instead of writing new ones, saving precious time in development.

In this tutorial we will build a recyclable ROS2 node based around an Edge Impulse machine learning model. This node will **draw** sensor data from a sensor topic, run the data through an Edge Impulse model, and then **publish** the results of the machine learning to another topic, to which other nodes in the system can subscribe.

*For the sake of demonstration, we’ll be using an accelerometer-based machine learning model trained to recognize “circle”, “up\_down”, and “side\_side” movements.*

In this project we’ll learn how to:

* Build a pub/sub Edge Impulse node
* Fill a sensor data buffer using a subscriber
* Import and use a machine learning model from within a ROS2 node
* Publish the inferences made by the machine learning node to a topic

***

## Equipment & software

* Raspberry Pi 4
* Adafruit MPU6050 accelerometer + gyroscope module (\*)
* Ubuntu 20.04 server
* ROS2 Foxy Fitzroy
* Edge Impulse Linux CLI
* VSCode Remote Development extension

**(\*) BYO sensor** For this tutorial we’ll be using a 3-axis accelerometer, but it is general enough to be adapted for just about any type of sensor.

***

### Getting started

This tutorial is meant to be as general as possible, and as such will not go in depth on building an Edge Impulse project / model. If you need help getting started you can find many high quality examples spanning a variety of sensors, boards, and use cases [here](/).

You should also have the Edge Impulse Linux CLI up and running on your Linux board (RPi, Jetson Nano, etc.). Read about installing the CLI [here](/tools/clis/edge-impulse-linux-cli). Test that it is indeed installed by running:

```jsx  theme={"system"}
edge-impulse-linux
```

You should see the CLI initialize.

***

### Creating a ROS2 package

Navigate to your workspace, and from within `ros2_ws/src` run:

```bash  theme={"system"}
ros2 pkg create ei_ros2 --build-type ament_python --dependencies rclpy std_msgs board os adafruit_mpu6050
```

This will create a package called “ei\_ros2”. Adjust the dependencies to suit whatever libraries your package requires (or edit them using the `package.xml` file).

***

### Building a node for the accelerometer (or other sensor)

Now we need to build the node that will publish sensor data that in turn will be fed to the machine learning model. Navigate to the “Impulse design” section of your Edge Impulse project, and take a loot at the first block:

<Frame caption="Untitled">
  <img src="https://i.imgur.com/oRlOJLt.png" />
</Frame>

This block contains a lot of important information. Let’s break it down:

* First, we see that the block expects to receive three input axes (since it is a 3-axis accelerometer).
* Next, we see that the model expects 2000ms (2 seconds) worth of data each time it is called.
* And finally, the frequency tells us *how many times per second* the sensor is sampled. In this case, 98 times / second (Hz).

We’ll return to these numbers a couple of times, but for now let’s start building our sensor node!

**Make a file called `mpu6050_node.py` (or whatever your sensor is called) under `/ros2_ws/src/ei_ros2/ei_ros2`.**

### 1: Imports

Here are the libraries we need for this node. Depending on which sensor you’ll need your imports may look different.

I’m using the `Float32MultiArray` as the message type, because we want to send an array with three readings (accelerometer X, Y, Z) which are float values.

```python  theme={"system"}
import board # Sensor specific
import rclpy # Always
from rclpy.node import Node # Always
from std_msgs.msg import Float32MultiArray # Sensor specific
import adafruit_mpu6050 # Sensor specific
```

### 2: Node class

Now we need a class with a **publisher** to handle our sensor. A lot of this code will be familiar to you if you have experience with ROS2.

* Notice the **frequency**: This should be the same frequency as the one in the “Impulse design” section of your EI project. This will make it so that sensor data is published at the required rate (1 / frequency).
* 98 times per second the `read_mpu6050()` method is called. Each time the 3 accelerometer axes are read, and sent together in an array to the `mpu6050_stream` topic. Once it arrives to the topic it becomes available for our machine learning node to subscribe to.

```python  theme={"system"}
class MPU6050Node(Node):
    def __init__(self):
        super().__init__("mpu6050")
        self.i2c = board.I2C()
        self.mpu = adafruit_mpu6050.MPU6050(self.i2c)
        self.publisher_ = self.create_publisher(Float32MultiArray, "mpu6050_stream", 15)
        self.frequency = 98 # See "Impulse design" block in EI project
        self.timer_ = self.create_timer((1 / self.frequency), self.read_mpu6050)
        self.get_logger().info("MP6050 stream opened.")

    def read_mpu6050(self):
        msg = Float32MultiArray()
        msg.data = [round(self.mpu.acceleration[0], 2), # accX
                    round(self.mpu.acceleration[1], 2), # accY
                    round(self.mpu.acceleration[2], 2)] # accZ
        self.publisher_.publish(msg)
```

Adding the `main()` function, the **full publisher node for the MPU6050 accelerometer** is:

```python  theme={"system"}
import board
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
import adafruit_mpu6050

class MPU6050Node(Node):
    def __init__(self):
        super().__init__("mpu6050")
        self.i2c = board.I2C()
        self.mpu = adafruit_mpu6050.MPU6050(self.i2c)
        self.publisher_ = self.create_publisher(Float32MultiArray, "mpu6050_stream", 15)
        self.frequency = 98
        self.timer_ = self.create_timer((1 / self.frequency), self.read_mpu6050)
        self.get_logger().info("MP6050 stream opened.")

    def read_mpu6050(self):
        msg = Float32MultiArray()
        msg.data = [round(self.mpu.acceleration[0], 2),
                    round(self.mpu.acceleration[1], 2),
                    round(self.mpu.acceleration[2], 2)]
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = MPU6050Node()
    rclpy.spin(node)
    rclpy.shutdown()
```

Now just run `chmod +x mpu6050_node.py` to make your node file executable, since we're using `--symlink-install`

***

### Building an AI powered Edge Impulse pub/sub node

We’ve arrived to the fun part! Effort was made to make this next chunk of code as reusable as possible. Let’s go through it piece by piece.

**First let’s download our model from Edge Impulse**.

* From the terminal, run:

```python  theme={"system"}
edge-impulse-linux-runner --clean
```

* After entering your credentials you should see:

<Frame caption="Untitled">
  <img src="https://user-images.githubusercontent.com/63222803/171701181-6d6f44b6-0eb1-48e9-b46f-b6fcad986839.png" />
</Frame>

* Select the project you want, and hit Enter. Now you should see this message:

<Frame caption="Untitled">
  <img src="https://user-images.githubusercontent.com/63222803/171701086-e13396ac-3f1a-4df6-b11c-786f70b6f09c.png" />
</Frame>

Take note of the file location and name. You should now **copy and paste** this file to the same directory where the sensor / Edge Impulse nodes are located (**`/ros2_ws/src/ei_ros2/ei_ros2`**).

**Now let’s build the node!**

Make a file called `ei_node.py` (or something) under `/ros2_ws/src/ei_ros2/ei_ros2`.

### 1: Imports:

Note that in this case we need both `String` and `Float32MultiArray`:

* `Float32MultiArray` for subscribing to the sensor node we just created
* And `String`, for publishing the machine learning results to an inference stream

```python  theme={"system"}
import os
import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Float32MultiArray
from edge_impulse_linux.runner import ImpulseRunner
```

### 2: Edge Impulse node class

There’s a lot going on here, but the important parts have numbered comments beside them, so let’s take them one by one:

1. “Change subscription” - Make sure you are subscribed to the correct topic (the same one that the sensor node is publishing to)
2. “Adjust timing” - This timer calls the function that runs the machine learning model. Basically, the function will only run the model **once the buffer** (which we’ll discuss in a moment) **is full** of data, so this timer essentially means: **How often do you want to check if the buffer is full**. If time isn’t an issue, you can set it to check every couple of seconds. Here I want to run the model as soon as I have a full buffer, so I set it to check every 0.01 seconds.
3. “Check file name” - The name of the .eim file here should match the name of the file downloaded via the CLI.
4. “Set max length” - The model expects to receive a specific amount of data, so we need to set the buffer (the array of sensor data that is passed to the model) to a specific length. How do we find the length? If we return to the “Impulse design” section of our Edge Impulse project, we’ll see that the window length is **2 seconds**, where the sensor is sampled **98 times per second**, each time giving **3 values**. So: 2 \* 98 \* 3 = **588**.

> Don’t stress too much about this part — if you put the wrong number in, you’ll get an error telling you what the correct number is 🙂

```python  theme={"system"}
class EdgeImpulseNode(Node):
    def __init__(self):
        super().__init__("edge_impulse_classifier")

        # Sensor data subscriber
        self.subscriber_ = self.create_subscription(Float32MultiArray, "mpu6050_stream", self.callback_fill_buffer, 10) # 1: Change subscription
        # Inference publisher
        self.publisher_ = self.create_publisher(String, "inference_stream", 10)
        self.timer_ = self.create_timer(0.01, self.classify) # 2: Adjust timing if desired

        # Create Classifier object based on Edge Impulse model file
        self.classifier = Classifier('model.eim') # 3: Check file name

        self.buffer = []
        self.buffer_full_len = 588 #4: Set max length of buffer array

        self.get_logger().info("Edge Impulse node opened.")

    # If buffer is full, classify and publish result!
    def classify(self):
        # String since we're publishing the class name
        msg = String()

        if len(self.buffer) == self.buffer_full_len:
            # Pass buffer to classifier
            msg.data = self.classifier.classify(self.buffer)
            self.publisher_.publish(msg)

            # Reset buffer
            self.buffer = []

    # Adds to buffer whenever new sensor data is published
    def callback_fill_buffer(self, msg):
        if len(self.buffer) < self.buffer_full_len:
            for val in msg.data:
                self.buffer.append(val)
```

### 3: Classifier class

This class handles passing the sensor data to the Edge Impulse model file we downloaded.

**Note:** The `classify()` method returns a string with the name of the *most likely* result. Machine learning inferences look like: `{'dog': 0.8, 'cat': 0.2, 'fish': 0.1}`. This function returns **only the string with the highest probability**.

```python  theme={"system"}
class Classifier:
    def __init__(self, model_path):
        self.runner = None
        self.model_path = model_path

    def classify(self, features):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        modelfile = os.path.join(dir_path, self.model_path)
        self.runner = ImpulseRunner(modelfile)

        try:
            self.runner.init()
            res = self.runner.classify(features)

            # Return classification with highest probability
            return max(res["result"]["classification"], key=res["result"]["classification"].get)

        finally:
            if (self.runner):
                self.runner.stop()
```

Now we can add the `main()` function and we’re ready to go!

**Full Edge Impulse Pub/Sub code:**

```python  theme={"system"}
# Imports
import os
import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Float32MultiArray
from edge_impulse_linux.runner import ImpulseRunner

# Classificiation node that subs to sensor stream and publishes to inference topic
class EdgeImpulseNode(Node):
    def __init__(self):
        super().__init__("edge_impulse_classifier")

        # Sensor data subscriber
        self.subscriber_ = self.create_subscription(Float32MultiArray, "mpu6050_stream", self.callback_fill_buffer, 10) # 1: Change subscription
        # Inference publisher
        self.publisher_ = self.create_publisher(String, "inference_stream", 10)
        self.timer_ = self.create_timer(0.01, self.classify) # 2: Adjust timing

        # Create Classifier object based on Edge Impulse model file
        self.classifier = Classifier('model.eim') # 3: Check file name

        self.buffer = []
        self.buffer_full_len = 588 #4: Set max length of buffer array

        self.get_logger().info("Edge Impulse node opened.")

    # If buffer is full, classify and publish result!
    def classify(self):
        # String since we're publishing the class name
        msg = String()

        if len(self.buffer) == self.buffer_full_len:
            # Pass buffer to classifier
            msg.data = self.classifier.classify(self.buffer)
            self.publisher_.publish(msg)

            # Reset buffer
            self.buffer = []

    # Adds to buffer whenever new sensor data is published
    def callback_fill_buffer(self, msg):
        if len(self.buffer) < self.buffer_full_len:
            for val in msg.data:
                self.buffer.append(val)

# Edge Impulse classification class
class Classifier:
    def __init__(self, model_path):
        self.runner = None
        self.model_path = model_path

    def classify(self, features):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        modelfile = os.path.join(dir_path, self.model_path)
        self.runner = ImpulseRunner(modelfile)

        try:
            self.runner.init()
            res = self.runner.classify(features)

            # Return classification with highest probability
            return max(res["result"]["classification"], key=res["result"]["classification"].get)

        finally:
            if (self.runner):
                self.runner.stop()

def main(args=None):
    rclpy.init(args=args)
    node = EdgeImpulseNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
```

Once again run `chmod +x ei_node.py` to make your node file executable.

***

### Adding entry points

In your `[setup.py](http://setup.py)` file add entry points for your nodes:

```python  theme={"system"}
.
.
.

entry_points={
        'console_scripts': [
            "mpu6050 = ei_ros2.mpu6050_node:main",
            "ei = ei_ros2.ei_node:main"
        ],
    }
```

***

### We’re ready to build!

Navigate to `ros2_ws` (or your main ROS2 workspace directory) and build the package using:

```python  theme={"system"}
colcon build --packages-select ei_ros2 --symlink-install
```

Once that finishes, we’re ready to for tests!

***

### Testing our Edge Impulse node

Let’s run both the sensor node and the Edge Impulse machine learning node. From two separate terminals run:

```python  theme={"system"}
ros2 run ei_ros2 mpu6050
```

```python  theme={"system"}
ros2 run ei_ros2 ei
```

And now in a third terminal let’s listen on the `inference_stream` topic using:

```python  theme={"system"}
ros2 topic echo /inference_stream
```

Now let’s move our accelerometer around and see what appears on the `inference_stream` topic:

<Frame caption="nodes.gif">
  <img src="https://user-images.githubusercontent.com/63222803/171701011-776ceff4-257f-4b56-8290-9aa81b515fe6.gif" />
</Frame>

Looking good!

***

### To summarize

In this tutorial we looked at how to make a AI-powered pub/sub node in ROS2. This tutorial is part of an Edge Impulse + ROS2 series, and in Part 2 we’ll look at how to use a service / client architecture. The contents of this tutorial can be generalized to suit just about any sensor and use case, so please don’t hesitate to try it out yourself! Feel free to ask questions at forum.edgeimpulse.com, or on the YouTube video version of this tutorial here:

[https://youtu.be/0SabLvJqSaM](https://youtu.be/0SabLvJqSaM)


Built with [Mintlify](https://mintlify.com).