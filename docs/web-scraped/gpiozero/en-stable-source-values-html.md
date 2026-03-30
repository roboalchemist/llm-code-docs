# Source: https://gpiozero.readthedocs.io/en/stable/source_values.html

Title: 7. Source/Values — gpiozero 2.0.1 Documentation

URL Source: https://gpiozero.readthedocs.io/en/stable/source_values.html

Markdown Content:
GPIO Zero provides a method of using the declarative programming paradigm to connect devices together: feeding the values of one device into another, for example the values of a button into an LED:

![Image 1: _images/led_button.svg](https://gpiozero.readthedocs.io/en/stable/_images/led_button.svg)

from gpiozero import LED, Button
from signal import pause

led = LED(17)
button = Button(2)

led.source = button

pause()

which is equivalent to:

from gpiozero import LED, Button
from time import sleep

led = LED(17)
button = Button(2)

while True:
    led.value = button.value
    sleep(0.01)

except that the former is updated in a background thread, which enables you to do other things at the same time.

Every device has a [`value`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.Device.value "gpiozero.Device.value") property (the device’s current value). Input devices (like buttons) can only have their values read, but output devices (like LEDs) can also have their value set to alter the state of the device:

>>> led = PWMLED(17)
>>> led.value  # LED is initially off
0.0
>>> led.on()  # LED is now on
>>> led.value
1.0
>>> led.value = 0  # LED is now off

Every device also has a [`values`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.ValuesMixin.values "gpiozero.ValuesMixin.values") property (a [generator](https://wiki.python.org/moin/Generators) continuously yielding the device’s current value). All output devices have a [`source`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.SourceMixin.source "gpiozero.SourceMixin.source") property which can be set to any [iterator](https://wiki.python.org/moin/Iterator). The device will iterate over the values of the device provided, setting the device’s value to each element at a rate specified in the [`source_delay`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.SourceMixin.source_delay "gpiozero.SourceMixin.source_delay") property (the default is 0.01 seconds).

![Image 2: _images/source_values.svg](https://gpiozero.readthedocs.io/en/stable/_images/source_values.svg)
The most common use case for this is to set the source of an output device to match the values of an input device, like the example above. A more interesting example would be a potentiometer controlling the brightness of an LED:

![Image 3: _images/pwmled_pot.svg](https://gpiozero.readthedocs.io/en/stable/_images/pwmled_pot.svg)

from gpiozero import PWMLED, MCP3008
from signal import pause

led = PWMLED(17)
pot = MCP3008()

led.source = pot

pause()

The way this works is that the input device’s [`values`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.ValuesMixin.values "gpiozero.ValuesMixin.values") property is used to feed values into the output device. Prior to v1.5, the [`source`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.SourceMixin.source "gpiozero.SourceMixin.source") had to be set directly to a device’s [`values`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.ValuesMixin.values "gpiozero.ValuesMixin.values") property:

from gpiozero import PWMLED, MCP3008
from signal import pause

led = PWMLED(17)
pot = MCP3008()

led.source = pot.values

pause()

Note

Although this method is still supported, the recommended way is now to set the [`source`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.SourceMixin.source "gpiozero.SourceMixin.source") to a device object.

It is also possible to set an output device’s [`source`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.SourceMixin.source "gpiozero.SourceMixin.source") to another output device, to keep them matching. In this example, the red LED is set to match the button, and the green LED is set to match the red LED, so both LEDs will be on when the button is pressed:

![Image 4: _images/matching_leds.svg](https://gpiozero.readthedocs.io/en/stable/_images/matching_leds.svg)

from gpiozero import LED, Button
from signal import pause

red = LED(14)
green = LED(15)
button = Button(17)

red.source = button
green.source = red

pause()

7.1. Processing values[](https://gpiozero.readthedocs.io/en/stable/source_values.html#processing-values "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------

The device’s values can also be processed before they are passed to the [`source`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.SourceMixin.source "gpiozero.SourceMixin.source"):

![Image 5: _images/value_processing.svg](https://gpiozero.readthedocs.io/en/stable/_images/value_processing.svg)
For example, writing a generator function to pass the opposite of the Button value into the LED:

![Image 6: _images/led_button_opposite.svg](https://gpiozero.readthedocs.io/en/stable/_images/led_button_opposite.svg)

from gpiozero import Button, LED
from signal import pause

def opposite(device):
    for value in device.values:
        yield not value

led = LED(4)
btn = Button(17)

led.source = opposite(btn)

pause()

Alternatively, a custom generator can be used to provide values from an artificial source:

![Image 7: _images/custom_generator.svg](https://gpiozero.readthedocs.io/en/stable/_images/custom_generator.svg)
For example, writing a generator function to randomly yield 0 or 1:

![Image 8: _images/random_led.svg](https://gpiozero.readthedocs.io/en/stable/_images/random_led.svg)

from gpiozero import LED
from random import randint
from signal import pause

def rand():
    while True:
        yield randint(0, 1)

led = LED(17)
led.source = rand()

pause()

If the iterator is infinite (i.e. an infinite generator), the elements will be processed until the [`source`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.SourceMixin.source "gpiozero.SourceMixin.source") is changed or set to [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)").

If the iterator is finite (e.g. a list), this will terminate once all elements are processed (leaving the device’s value at the final element):

from gpiozero import LED
from signal import pause

led = LED(17)
led.source_delay = 1
led.source = [1, 0, 1, 1, 1, 0, 0, 1, 0, 1]

pause()

7.2. Source Tools[](https://gpiozero.readthedocs.io/en/stable/source_values.html#source-tools "Link to this heading")
----------------------------------------------------------------------------------------------------------------------

GPIO Zero provides a set of ready-made functions for dealing with source/values, called source tools. These are available by importing from [`gpiozero.tools`](https://gpiozero.readthedocs.io/en/stable/api_tools.html#module-gpiozero.tools "gpiozero.tools").

Some of these source tools are artificial sources which require no input:

![Image 9: _images/source_tool.svg](https://gpiozero.readthedocs.io/en/stable/_images/source_tool.svg)
In this example, random values between 0 and 1 are passed to the LED, giving it a flickering candle effect:

![Image 10: _images/source_tool_candle.svg](https://gpiozero.readthedocs.io/en/stable/_images/source_tool_candle.svg)

from gpiozero import PWMLED
from gpiozero.tools import random_values
from signal import pause

led = PWMLED(4)
led.source = random_values()
led.source_delay = 0.1

pause()

Note that in the above example, [`source_delay`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.SourceMixin.source_delay "gpiozero.SourceMixin.source_delay") is used to make the LED iterate over the random values slightly slower. [`source_delay`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.SourceMixin.source_delay "gpiozero.SourceMixin.source_delay") can be set to a larger number (e.g. 1 for a one second delay) or set to 0 to disable any delay.

Some tools take a single source and process its values:

![Image 11: _images/source_tool_value_processor.svg](https://gpiozero.readthedocs.io/en/stable/_images/source_tool_value_processor.svg)
In this example, the LED is lit only when the button is not pressed:

![Image 12: _images/led_button_negated.svg](https://gpiozero.readthedocs.io/en/stable/_images/led_button_negated.svg)

from gpiozero import Button, LED
from gpiozero.tools import negated
from signal import pause

led = LED(4)
btn = Button(17)

led.source = negated(btn)

pause()

Note

Note that source tools which take one or more `value` parameters support passing either [`ValuesMixin`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.ValuesMixin "gpiozero.ValuesMixin") derivatives, or iterators, including a device’s [`values`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.ValuesMixin.values "gpiozero.ValuesMixin.values") property.

Some tools combine the values of multiple sources:

![Image 13: _images/combining_sources.svg](https://gpiozero.readthedocs.io/en/stable/_images/combining_sources.svg)
In this example, the LED is lit only if both buttons are pressed (like an [AND](https://en.wikipedia.org/wiki/AND_gate) gate):

![Image 14: _images/combining_sources_led_buttons.svg](https://gpiozero.readthedocs.io/en/stable/_images/combining_sources_led_buttons.svg)

from gpiozero import Button, LED
from gpiozero.tools import all_values
from signal import pause

button_a = Button(2)
button_b = Button(3)
led = LED(17)

led.source = all_values(button_a, button_b)

pause()

Similarly, [`any_values()`](https://gpiozero.readthedocs.io/en/stable/api_tools.html#gpiozero.tools.any_values "gpiozero.tools.any_values") with two buttons would simulate an [OR](https://en.wikipedia.org/wiki/OR_gate) gate.

While most devices have a [`value`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.Device.value "gpiozero.Device.value") range between 0 and 1, some have a range between -1 and 1 (e.g. [`Motor`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Motor "gpiozero.Motor"), [`Servo`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Servo "gpiozero.Servo") and [`TonalBuzzer`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.TonalBuzzer "gpiozero.TonalBuzzer")). Some source tools output values between -1 and 1, which are ideal for these devices, for example passing [`sin_values()`](https://gpiozero.readthedocs.io/en/stable/api_tools.html#gpiozero.tools.sin_values "gpiozero.tools.sin_values") in:

![Image 15: _images/sin_values.svg](https://gpiozero.readthedocs.io/en/stable/_images/sin_values.svg)

from gpiozero import Motor, Servo, TonalBuzzer
from gpiozero.tools import sin_values
from signal import pause

motor = Motor(2, 3)
servo = Servo(4)
buzzer = TonalBuzzer(5)

motor.source = sin_values()
servo.source = motor
buzzer.source = motor

pause()

In this example, all three devices are following the [sine wave](https://en.wikipedia.org/wiki/Sine_wave). The motor value ramps up from 0 (stopped) to 1 (full speed forwards), then back down to 0 and on to -1 (full speed backwards) in a cycle. Similarly, the servo moves from its mid point to the right, then towards the left; and the buzzer starts with its mid tone, gradually raises its frequency, to its highest tone, then down towards its lowest tone. Note that setting [`source_delay`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.SourceMixin.source_delay "gpiozero.SourceMixin.source_delay") will alter the speed at which the device iterates through the values. Alternatively, the tool [`cos_values()`](https://gpiozero.readthedocs.io/en/stable/api_tools.html#gpiozero.tools.cos_values "gpiozero.tools.cos_values") could be used to start from -1 and go up to 1, and so on.

7.3. Internal devices[](https://gpiozero.readthedocs.io/en/stable/source_values.html#internal-devices "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------

GPIO Zero also provides several [internal devices](https://gpiozero.readthedocs.io/en/stable/api_internal.html) which represent facilities provided by the operating system itself. These can be used to react to things like the time of day, or whether a server is available on the network. These classes include a [`values`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.ValuesMixin.values "gpiozero.ValuesMixin.values") property which can be used to feed values into a device’s [`source`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.SourceMixin.source "gpiozero.SourceMixin.source"). For example, a lamp connected to an [`Energenie`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Energenie "gpiozero.Energenie") socket can be controlled by a [`TimeOfDay`](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.TimeOfDay "gpiozero.TimeOfDay") object so that it is on between the hours of 8am and 8pm:

![Image 16: _images/timed_heat_lamp.svg](https://gpiozero.readthedocs.io/en/stable/_images/timed_heat_lamp.svg)

from gpiozero import Energenie, TimeOfDay
from datetime import time
from signal import pause

lamp = Energenie(1)
daytime = TimeOfDay(time(8), time(20))

daytime.when_activated = lamp.on
daytime.when_deactivated = lamp.off

pause()

Using the [`DiskUsage`](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.DiskUsage "gpiozero.DiskUsage") class with [`LEDBarGraph`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBarGraph "gpiozero.LEDBarGraph") can show your Pi’s disk usage percentage on a bar graph:

![Image 17: _images/disk_usage_bar_graph.svg](https://gpiozero.readthedocs.io/en/stable/_images/disk_usage_bar_graph.svg)

from gpiozero import DiskUsage, LEDBarGraph
from signal import pause

disk = DiskUsage()
graph = LEDBarGraph(2, 3, 4, 5, 6, 7, 8)

graph.source = disk

pause()

Demonstrating a garden light system whereby the light comes on if it’s dark and there’s motion is simple enough, but it requires using the [`booleanized()`](https://gpiozero.readthedocs.io/en/stable/api_tools.html#gpiozero.tools.booleanized "gpiozero.tools.booleanized") source tool to convert the light sensor from a float value into a boolean:

![Image 18: _images/garden_light.svg](https://gpiozero.readthedocs.io/en/stable/_images/garden_light.svg)

from gpiozero import LED, MotionSensor, LightSensor
from gpiozero.tools import booleanized, all_values
from signal import pause

garden = LED(2)
motion = MotionSensor(4)
light = LightSensor(5)

garden.source = all_values(booleanized(light, 0, 0.1), motion)

pause()

7.4. Composite devices[](https://gpiozero.readthedocs.io/en/stable/source_values.html#composite-devices "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------

The [`value`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.Device.value "gpiozero.Device.value") of a composite device made up of the nested values of its devices. For example, the value of a [`Robot`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Robot "gpiozero.Robot") object is a 2-tuple containing its left and right motor values:

>>> from gpiozero import Robot
>>> robot = Robot(left=(14, 15), right=(17, 18))
>>> robot.value
RobotValue(left_motor=0.0, right_motor=0.0)
>>> tuple(robot.value)
(0.0, 0.0)
>>> robot.forward()
>>> tuple(robot.value)
(1.0, 1.0)
>>> robot.backward()
>>> tuple(robot.value)
(-1.0, -1.0)
>>> robot.value = (1, 1)  # robot is now driven forwards

Use two potentiometers to control the left and right motor speed of a robot:

![Image 19: _images/robot_pots_1.svg](https://gpiozero.readthedocs.io/en/stable/_images/robot_pots_1.svg)

from gpiozero import Robot, Motor, MCP3008
from gpiozero.tools import zip_values
from signal import pause

robot = Robot(left=Motor(4, 14), right=Motor(17, 18))

left_pot = MCP3008(0)
right_pot = MCP3008(1)

robot.source = zip_values(left_pot, right_pot)

pause()

To include reverse direction, scale the potentiometer values from 0->1 to -1->1:

![Image 20: _images/robot_pots_2.svg](https://gpiozero.readthedocs.io/en/stable/_images/robot_pots_2.svg)

from gpiozero import Robot, Motor, MCP3008
from gpiozero.tools import scaled
from signal import pause

robot = Robot(left=Motor(4, 14), right=Motor(17, 18))

left_pot = MCP3008(0)
right_pot = MCP3008(1)

robot.source = zip(scaled(left_pot, -1, 1), scaled(right_pot, -1, 1))

pause()

Note that this example uses the built-in [`zip()`](https://docs.python.org/3.9/library/functions.html#zip "(in Python v3.9)") rather than the tool [`zip_values()`](https://gpiozero.readthedocs.io/en/stable/api_tools.html#gpiozero.tools.zip_values "gpiozero.tools.zip_values") as the [`scaled()`](https://gpiozero.readthedocs.io/en/stable/api_tools.html#gpiozero.tools.scaled "gpiozero.tools.scaled") tool yields values which do not need converting, just zipping. Also note that this use of [`zip()`](https://docs.python.org/3.9/library/functions.html#zip "(in Python v3.9)") will not work in Python 2, instead use [izip](https://docs.python.org/2/library/itertools.html#itertools.izip).
