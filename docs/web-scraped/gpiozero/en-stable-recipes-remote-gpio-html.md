# Source: https://gpiozero.readthedocs.io/en/stable/recipes_remote_gpio.html

Title: 5. Remote GPIO Recipes — gpiozero 2.0.1 Documentation

URL Source: https://gpiozero.readthedocs.io/en/stable/recipes_remote_gpio.html

Markdown Content:
The following recipes demonstrate some of the capabilities of the remote GPIO feature of the GPIO Zero library. Before you start following these examples, please read up on preparing your Pi and your host PC to work with [Configuring Remote GPIO](https://gpiozero.readthedocs.io/en/stable/remote_gpio.html).

Please note that all recipes are written assuming Python 3. Recipes _may_ work under Python 2, but no guarantees!

5.1. LED + Button[](https://gpiozero.readthedocs.io/en/stable/recipes_remote_gpio.html#led-button "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------

Let a [`Button`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button "gpiozero.Button") on one Raspberry Pi control the [`LED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED "gpiozero.LED") of another:

from gpiozero import Button, LED
from gpiozero.pins.pigpio import PiGPIOFactory
from signal import pause

factory = PiGPIOFactory(host='192.168.1.3')

button = Button(2)
led = LED(17, pin_factory=factory)

led.source = button

pause()

5.2. LED + 2 Buttons[](https://gpiozero.readthedocs.io/en/stable/recipes_remote_gpio.html#led-2-buttons "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------

The [`LED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED "gpiozero.LED") will come on when both buttons are pressed:

from gpiozero import Button, LED
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero.tools import all_values
from signal import pause

factory3 = PiGPIOFactory(host='192.168.1.3')
factory4 = PiGPIOFactory(host='192.168.1.4')

led = LED(17)
button_1 = Button(17, pin_factory=factory3)
button_2 = Button(17, pin_factory=factory4)

led.source = all_values(button_1, button_2)

pause()

5.3. Multi-room motion alert[](https://gpiozero.readthedocs.io/en/stable/recipes_remote_gpio.html#multi-room-motion-alert "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------

Install a Raspberry Pi with a [`MotionSensor`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.MotionSensor "gpiozero.MotionSensor") in each room of your house, and have an class:LED indicator showing when there’s motion in each room:

from gpiozero import LEDBoard, MotionSensor
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero.tools import zip_values
from signal import pause

ips = ['192.168.1.3', '192.168.1.4', '192.168.1.5', '192.168.1.6']
remotes = [PiGPIOFactory(host=ip) for ip in ips]

leds = LEDBoard(2, 3, 4, 5)  # leds on this pi
sensors = [MotionSensor(17, pin_factory=r) for r in remotes]  # remote sensors

leds.source = zip_values(*sensors)

pause()

5.4. Multi-room doorbell[](https://gpiozero.readthedocs.io/en/stable/recipes_remote_gpio.html#multi-room-doorbell "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------

Install a Raspberry Pi with a [`Buzzer`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Buzzer "gpiozero.Buzzer") attached in each room you want to hear the doorbell, and use a push [`Button`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button "gpiozero.Button") as the doorbell:

from gpiozero import LEDBoard, MotionSensor
from gpiozero.pins.pigpio import PiGPIOFactory
from signal import pause

ips = ['192.168.1.3', '192.168.1.4', '192.168.1.5', '192.168.1.6']
remotes = [PiGPIOFactory(host=ip) for ip in ips]

button = Button(17)  # button on this pi
buzzers = [Buzzer(pin, pin_factory=r) for r in remotes]  # buzzers on remote pins

for buzzer in buzzers:
    buzzer.source = button

pause()

This could also be used as an internal doorbell (tell people it’s time for dinner from the kitchen).

5.5. Remote button robot[](https://gpiozero.readthedocs.io/en/stable/recipes_remote_gpio.html#remote-button-robot "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------

Similarly to the simple recipe for the button controlled [`Robot`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Robot "gpiozero.Robot"), this example uses four buttons to control the direction of a robot. However, using remote pins for the robot means the control buttons can be separate from the robot:

from gpiozero import Button, Robot, Motor
from gpiozero.pins.pigpio import PiGPIOFactory
from signal import pause

factory = PiGPIOFactory(host='192.168.1.17')
robot = Robot(left=Motor(4, 14), right=Motor(17, 18),
              pin_factory=factory)  # remote pins

# local buttons
left = Button(26)
right = Button(16)
fw = Button(21)
bw = Button(20)

fw.when_pressed = robot.forward
fw.when_released = robot.stop

left.when_pressed = robot.left
left.when_released = robot.stop

right.when_pressed = robot.right
right.when_released = robot.stop

bw.when_pressed = robot.backward
bw.when_released = robot.stop

pause()

5.6. Light sensor + Sense HAT[](https://gpiozero.readthedocs.io/en/stable/recipes_remote_gpio.html#light-sensor-sense-hat "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------

The [Sense HAT](https://www.raspberrypi.org/products/sense-hat/) (not supported by GPIO Zero) includes temperature, humidity and pressure sensors, but no light sensor. Remote GPIO allows an external [`LightSensor`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.LightSensor "gpiozero.LightSensor") to be used as well. The Sense HAT LED display can be used to show different colours according to the light levels:

from gpiozero import LightSensor
from gpiozero.pins.pigpio import PiGPIOFactory
from sense_hat import SenseHat

remote_factory = PiGPIOFactory(host='192.168.1.4')
light = LightSensor(4, pin_factory=remote_factory)  # remote motion sensor
sense = SenseHat()  # local sense hat

blue = (0, 0, 255)
yellow = (255, 255, 0)

while True:
    if light.value > 0.5:
        sense.clear(yellow)
    else:
        sense.clear(blue)

Note that in this case, the Sense HAT code must be run locally, and the GPIO remotely.
