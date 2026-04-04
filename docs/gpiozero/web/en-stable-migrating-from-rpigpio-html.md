# Source: https://gpiozero.readthedocs.io/en/stable/migrating_from_rpigpio.html

Title: 11. Migrating from RPi.GPIO — gpiozero 2.0.1 Documentation

URL Source: https://gpiozero.readthedocs.io/en/stable/migrating_from_rpigpio.html

Markdown Content:
If you are familiar with the [RPi.GPIO](https://pypi.org/project/RPi.GPIO/) library, you will be used to writing code which deals with _pins_ and the _state of pins_. You will see from the examples in this documentation that we generally refer to things like LEDs and Buttons rather than input pins and output pins.

GPIO Zero provides classes which represent _devices_, so instead of having a pin number and telling it to go high, you have an LED and you tell it to turn on, and instead of having a pin number and asking if it’s high or low, you have a button and ask if it’s pressed. There is also no boilerplate code to get started — you just import the parts you need.

GPIO Zero provides many device classes, each with specific methods and properties bespoke to that device. For example, the functionality for an HC-SR04 Distance Sensor can be found in the [`DistanceSensor`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.DistanceSensor "gpiozero.DistanceSensor") class.

As well as specific device classes, we provide base classes [`InputDevice`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.InputDevice "gpiozero.InputDevice") and [`OutputDevice`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.OutputDevice "gpiozero.OutputDevice"). One main difference between these and the equivalents in RPi.GPIO is that they are classes, not functions, which means that you initialize one to begin, and provide its pin number, but then you never need to use the pin number again, as it’s stored by the object.

GPIO Zero was originally just a layer on top of RPi.GPIO, but we later added support for various other underlying pin libraries. RPi.GPIO is currently the default pin library used. Read more about this in [Changing the pin factory](https://gpiozero.readthedocs.io/en/stable/api_pins.html#changing-pin-factory).

11.1. Output devices[](https://gpiozero.readthedocs.io/en/stable/migrating_from_rpigpio.html#output-devices "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------

Turning an LED on in [RPi.GPIO](https://pypi.org/project/RPi.GPIO/):

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(2, GPIO.OUT)

GPIO.output(2, GPIO.HIGH)

Turning an LED on in GPIO Zero:

from gpiozero import LED

led = LED(2)

led.on()

The [`LED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED "gpiozero.LED") class also supports threaded blinking through the [`blink()`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED.blink "gpiozero.LED.blink") method.

[`OutputDevice`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.OutputDevice "gpiozero.OutputDevice") is the base class for output devices, and can be used in a similar way to output devices in RPi.GPIO.

See a full list of supported [output devices](https://gpiozero.readthedocs.io/en/stable/api_output.html). Other output devices have similar property and method names. There is commonality in naming at base level, such as `OutputDevice.is_active`, which is aliased in a device class, such as [`LED.is_lit`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED.is_lit "gpiozero.LED.is_lit").

11.2. Input devices[](https://gpiozero.readthedocs.io/en/stable/migrating_from_rpigpio.html#input-devices "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------

Reading a button press in [RPi.GPIO](https://pypi.org/project/RPi.GPIO/):

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(4, GPIO.IN, GPIO.PUD_UP)

if not GPIO.input(4):
    print("button is pressed")

Reading a button press in GPIO Zero:

from gpiozero import Button

btn = Button(4)

if btn.is_pressed:
    print("button is pressed")

Note that in the RPi.GPIO example, the button is set up with the option `GPIO.PUD_UP` which means “pull-up”, and therefore when the button is not pressed, the pin is high. When the button is pressed, the pin goes low, so the condition requires negation (`if not`). If the button was configured as pull-down, the logic is reversed and the condition would become 
```
if
GPIO.input(4)
```
:

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(4, GPIO.IN, GPIO.PUD_DOWN)

if GPIO.input(4):
    print("button is pressed")

In GPIO Zero, the default configuration for a button is pull-up, but this can be configured at initialization, and the rest of the code stays the same:

from gpiozero import Button

btn = Button(4, pull_up=False)

if btn.is_pressed:
    print("button is pressed")

RPi.GPIO also supports blocking edge detection.

Wait for a pull-up button to be pressed in RPi.GPIO:

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(4, GPIO.IN, GPIO.PUD_UP)

GPIO.wait_for_edge(4, GPIO.FALLING):
print("button was pressed")

The equivalent in GPIO Zero:

from gpiozero import Button

btn = Button(4)

btn.wait_for_press()
print("button was pressed")

Again, if the button is pulled down, the logic is reversed. Instead of waiting for a falling edge, we’re waiting for a rising edge:

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(4, GPIO.IN, GPIO.PUD_UP)

GPIO.wait_for_edge(4, GPIO.FALLING):
print("button was pressed")

Again, in GPIO Zero, the only difference is in the initialization:

from gpiozero import Button

btn = Button(4, pull_up=False)

btn.wait_for_press()
print("button was pressed")

RPi.GPIO has threaded callbacks. You create a function (which must take one argument), and pass it in to `add_event_detect`, along with the pin number and the edge direction:

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def pressed(pin):
    print("button was pressed")

def released(pin):
    print("button was released")

GPIO.setup(4, GPIO.IN, GPIO.PUD_UP)

GPIO.add_event_detect(4, GPIO.FALLING, pressed)
GPIO.add_event_detect(4, GPIO.RISING, released)

In GPIO Zero, you assign the [`when_pressed`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button.when_pressed "gpiozero.Button.when_pressed") and [`when_released`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button.when_released "gpiozero.Button.when_released") properties to set up callbacks on those actions:

from gpiozero import Button

def pressed():
    print("button was pressed")

def released():
    print("button was released")

btn = Button(4)

btn.when_pressed = pressed
btn.when_released = released

[`when_held`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button.when_held "gpiozero.Button.when_held") is also provided, where the length of time considered a “hold” is configurable.

The callback functions don’t have to take any arguments, but if they take one, the button object is passed in, allowing you to determine which button called the function.

[`InputDevice`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.InputDevice "gpiozero.InputDevice") is the base class for input devices, and can be used in a similar way to input devices in RPi.GPIO.

See a full list of [input devices](https://gpiozero.readthedocs.io/en/stable/api_input.html). Other input devices have similar property and method names. There is commonality in naming at base level, such as [`InputDevice.is_active`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.InputDevice.is_active "gpiozero.InputDevice.is_active"), which is aliased in a device class, such as [`Button.is_pressed`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button.is_pressed "gpiozero.Button.is_pressed") and [`LightSensor.light_detected`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.LightSensor.light_detected "gpiozero.LightSensor.light_detected").

11.3. Composite devices, boards and accessories[](https://gpiozero.readthedocs.io/en/stable/migrating_from_rpigpio.html#composite-devices-boards-and-accessories "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Some devices require connections to multiple pins, for example a distance sensor, a combination of LEDs or a HAT. Some GPIO Zero devices comprise multiple device connections within one object, such as [`RGBLED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.RGBLED "gpiozero.RGBLED"), [`LEDBoard`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBoard "gpiozero.LEDBoard"), [`DistanceSensor`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.DistanceSensor "gpiozero.DistanceSensor"), [`Motor`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Motor "gpiozero.Motor") and [`Robot`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Robot "gpiozero.Robot").

With RPi.GPIO, you would have one output pin for the trigger, and one input pin for the echo. You would time the echo and calculate the distance. With GPIO Zero, you create a single [`DistanceSensor`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.DistanceSensor "gpiozero.DistanceSensor") object, specifying the trigger and echo pins, and you would read the [`DistanceSensor.distance`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.DistanceSensor.distance "gpiozero.DistanceSensor.distance") property which automatically calculates the distance within the implementation of the class.

The [`Motor`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Motor "gpiozero.Motor") class controls two output pins to drive the motor forwards or backwards. The [`Robot`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Robot "gpiozero.Robot") class controls four output pins (two motors) in the right combination to drive a robot forwards or backwards, and turn left and right.

The [`LEDBoard`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBoard "gpiozero.LEDBoard") class takes an arbitrary number of pins, each controlling a single LED. The resulting [`LEDBoard`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBoard "gpiozero.LEDBoard") object can be used to control all LEDs together (all on / all off), or individually by index. Also the object can be iterated over to turn LEDs on in order. See examples of this (including slicing) in the [advanced recipes](https://gpiozero.readthedocs.io/en/stable/recipes_advanced.html#ledboard-advanced).

11.4. PWM (Pulse-width modulation)[](https://gpiozero.readthedocs.io/en/stable/migrating_from_rpigpio.html#pwm-pulse-width-modulation "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------

Both libraries support software PWM control on any pin. Depending on the pin library used, GPIO Zero can also support hardware PWM (using `RPIOPin` or `PiGPIOPin`).

A simple example of using PWM is to control the brightness of an LED.

In [RPi.GPIO](https://pypi.org/project/RPi.GPIO/):

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(2, GPIO.OUT)
pwm = GPIO.PWM(2, 100)
pwm.start(0)

for dc in range(101):
    pwm.changeDutyCycle(dc)
    sleep(0.01)

In GPIO Zero:

from gpiozero import PWMLED
from time import sleep

led = PWMLED(2)

for b in range(101):
    led.value = b / 100.0
    sleep(0.01)

[`PWMLED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED "gpiozero.PWMLED") has a [`blink()`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED.blink "gpiozero.PWMLED.blink") method which can be used the same was as [`LED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED "gpiozero.LED")’s [`blink()`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED.blink "gpiozero.LED.blink") method, but its PWM capabilities allow for `fade_in` and `fade_out` options to be provided. There is also the [`pulse()`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED.pulse "gpiozero.PWMLED.pulse") method which provides a neat way to have an LED fade in and out repeatedly.

Other devices can make use of PWM, such as motors (for variable speed) and servos. See the [`Motor`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Motor "gpiozero.Motor"), [`Servo`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Servo "gpiozero.Servo") and [`AngularServo`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.AngularServo "gpiozero.AngularServo") classes for information on those. [`Motor`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Motor "gpiozero.Motor") and [`Robot`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Robot "gpiozero.Robot") default to using PWM, but it can be disabled with `pwm=False` at initialization. Servos cannot be used without PWM. Devices containing LEDs default to not using PWM, but `pwm=True` can be specified and any LED objects within the device will be initialized as [`PWMLED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED "gpiozero.PWMLED") objects.

11.5. Cleanup[](https://gpiozero.readthedocs.io/en/stable/migrating_from_rpigpio.html#cleanup "Link to this heading")
----------------------------------------------------------------------------------------------------------------------

Pin state cleanup is explicit in RPi.GPIO, and is done manually with `GPIO.cleanup()` but in GPIO Zero, cleanup is automatically performed on every pin used, at the end of the script. Manual cleanup is possible by use of the [`close()`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.Device.close "gpiozero.Device.close") method on the device.

Note that cleanup only occurs at the point of normal termination of the script. If the script exits due to a program error, cleanup will not be performed. To ensure that cleanup is performed after an exception is raised, the exception must be handled, for example:

from gpiozero import Button

btn = Button(4)

while True:
    try:
        if btn.is_pressed:
            print("Pressed")
    except KeyboardInterrupt:
        print("Ending program")

Read more in the relevant FAQ: [What’s the gpiozero equivalent of GPIO.cleanup()?](https://gpiozero.readthedocs.io/en/stable/faq.html#gpio-cleanup)

11.6. Pi Information[](https://gpiozero.readthedocs.io/en/stable/migrating_from_rpigpio.html#pi-information "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------

RPi.GPIO provides information about the Pi you’re using. The equivalent in GPIO Zero is the function [`pi_info()`](https://gpiozero.readthedocs.io/en/stable/api_info.html#gpiozero.pi_info "gpiozero.pi_info"):

>>> from gpiozero import pi_info
>>> pi = pi_info()
>>> pi
PiBoardInfo(revision='a02082', model='3B', pcb_revision='1.2', released='2016Q1', soc='BCM2837', manufacturer='Sony', memory=1024, storage='MicroSD', usb=4, ethernet=1, wifi=True, bluetooth=True, csi=1, dsi=1, headers=..., board=...)
>>> pi.soc
'BCM2837'
>>> pi.wifi
True

Read more about what [`PiBoardInfo`](https://gpiozero.readthedocs.io/en/stable/api_info.html#gpiozero.PiBoardInfo "gpiozero.PiBoardInfo") provides.

11.7. More[](https://gpiozero.readthedocs.io/en/stable/migrating_from_rpigpio.html#more "Link to this heading")
----------------------------------------------------------------------------------------------------------------

GPIO Zero provides more than just GPIO device support, it includes some support for [SPI devices](https://gpiozero.readthedocs.io/en/stable/api_spi.html) including a range of analog to digital converters.

Device classes which are compatible with other GPIO devices, but have no relation to GPIO pins, such as [`CPUTemperature`](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.CPUTemperature "gpiozero.CPUTemperature"), [`TimeOfDay`](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.TimeOfDay "gpiozero.TimeOfDay"), [`PingServer`](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.PingServer "gpiozero.PingServer") and [`LoadAverage`](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.LoadAverage "gpiozero.LoadAverage") are also provided.

GPIO Zero features support for multiple pin libraries. The default is to use `RPi.GPIO` to control the pins, but you can choose to use another library, such as `pigpio`, which supports network controlled GPIO. See [Changing the pin factory](https://gpiozero.readthedocs.io/en/stable/api_pins.html#changing-pin-factory) and [Configuring Remote GPIO](https://gpiozero.readthedocs.io/en/stable/remote_gpio.html) for more information.

It is possible to run GPIO Zero on your PC, both for remote GPIO and for testing purposes, using [Mock pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html#mock-pins).

Another feature of this library is configuring devices to be connected together in a logical way, for example in one line you can say that an LED and button are “paired”, i.e. the button being pressed turns the LED on. Read about this in [Source/Values](https://gpiozero.readthedocs.io/en/stable/source_values.html).

11.8. FAQs[](https://gpiozero.readthedocs.io/en/stable/migrating_from_rpigpio.html#faqs "Link to this heading")
----------------------------------------------------------------------------------------------------------------

Note the following FAQs which may catch out users too familiar with RPi.GPIO:

*   [How do I keep my script running?](https://gpiozero.readthedocs.io/en/stable/faq.html#keep-your-script-running)

*   [Why do I get PinFactoryFallback warnings when I import gpiozero?](https://gpiozero.readthedocs.io/en/stable/faq.html#pinfactoryfallback-warnings)

*   [What’s the gpiozero equivalent of GPIO.cleanup()?](https://gpiozero.readthedocs.io/en/stable/faq.html#gpio-cleanup)
