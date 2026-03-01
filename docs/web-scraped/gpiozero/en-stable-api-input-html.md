# Source: https://gpiozero.readthedocs.io/en/stable/api_input.html

Title: Input Devices — gpiozero 2.0.1 Documentation

URL Source: https://gpiozero.readthedocs.io/en/stable/api_input.html

Markdown Content:
14. API - Input Devices[](https://gpiozero.readthedocs.io/en/stable/api_input.html#module-gpiozero.input_devices "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------

These input device component interfaces have been provided for simple use of everyday components. Components must be wired up correctly before use in code.

Note

All GPIO pin numbers use Broadcom (BCM) numbering by default. See the [Pin Numbering](https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering) section for more information.

14.1. Regular Classes[](https://gpiozero.readthedocs.io/en/stable/api_input.html#regular-classes "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------

The following classes are intended for general use with the devices they represent. All classes in this section are concrete (not abstract).

### 14.1.1. Button[](https://gpiozero.readthedocs.io/en/stable/api_input.html#button "Link to this heading")

_class_ gpiozero.Button(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/input_devices.html#Button)[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button "Link to this definition")
Extends [`DigitalInputDevice`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.DigitalInputDevice "gpiozero.DigitalInputDevice") and represents a simple push button or switch.

Connect one side of the button to a ground pin, and the other to any GPIO pin. Alternatively, connect one side of the button to the 3V3 pin, and the other to any GPIO pin, then set _pull\_up_ to [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") in the [`Button`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button "gpiozero.Button") constructor.

The following example will print a line of text when the button is pushed:

from gpiozero import Button

button = Button(4)
button.wait_for_press()
print("The button was pressed!")

Parameters:
*   **pin** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")_or_[_str_](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)")) – The GPIO pin which the button is connected to. See [Pin Numbering](https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering) for valid pin numbers. If this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") a [`GPIODeviceError`](https://gpiozero.readthedocs.io/en/stable/api_exc.html#gpiozero.GPIODeviceError "gpiozero.GPIODeviceError") will be raised.

*   **pull_up** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")_or_ _None_) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") (the default), the GPIO pin will be pulled high by default. In this case, connect the other side of the button to ground. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)"), the GPIO pin will be pulled low by default. In this case, connect the other side of the button to 3V3. If [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)"), the pin will be floating, so it must be externally pulled up or down and the `active_state` parameter must be set accordingly.

*   **active_state** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")_or_ _None_) – See description under [`InputDevice`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.InputDevice "gpiozero.InputDevice") for more information.

*   **bounce_time** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")_or_ _None_) – If [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default), no software bounce compensation will be performed. Otherwise, this is the length of time (in seconds) that the component will ignore changes in state after an initial change.

*   **hold_time** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – The length of time (in seconds) to wait after the button is pushed, until executing the [`when_held`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button.when_held "gpiozero.Button.when_held") handler. Defaults to `1`.

*   **hold_repeat** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"), the [`when_held`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button.when_held "gpiozero.Button.when_held") handler will be repeatedly executed as long as the device remains active, every _hold\_time_ seconds. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") (the default) the [`when_held`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button.when_held "gpiozero.Button.when_held") handler will be only be executed once per hold.

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

wait_for_press(_timeout=None_)[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button.wait_for_press "Link to this definition")
Pause the script until the device is activated, or the timeout is reached.

Parameters:
**timeout** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")_or_ _None_) – Number of seconds to wait before proceeding. If this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default), then wait indefinitely until the device is active.

wait_for_release(_timeout=None_)[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button.wait_for_release "Link to this definition")
Pause the script until the device is deactivated, or the timeout is reached.

Parameters:
**timeout** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")_or_ _None_) – Number of seconds to wait before proceeding. If this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default), then wait indefinitely until the device is inactive.

_property_ held_time[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button.held_time "Link to this definition")
The length of time (in seconds) that the device has been held for. This is counted from the first execution of the [`when_held`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button.when_held "gpiozero.Button.when_held") event rather than when the device activated, in contrast to [`active_time`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.EventsMixin.active_time "gpiozero.EventsMixin.active_time"). If the device is not currently held, this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)").

_property_ hold_repeat[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button.hold_repeat "Link to this definition")
If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"), [`when_held`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button.when_held "gpiozero.Button.when_held") will be executed repeatedly with [`hold_time`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button.hold_time "gpiozero.Button.hold_time") seconds between each invocation.

_property_ hold_time[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button.hold_time "Link to this definition")
The length of time (in seconds) to wait after the device is activated, until executing the [`when_held`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button.when_held "gpiozero.Button.when_held") handler. If [`hold_repeat`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button.hold_repeat "gpiozero.Button.hold_repeat") is True, this is also the length of time between invocations of [`when_held`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button.when_held "gpiozero.Button.when_held").

_property_ is_held[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button.is_held "Link to this definition")
When [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"), the device has been active for at least [`hold_time`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button.hold_time "gpiozero.Button.hold_time") seconds.

_property_ is_pressed[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button.is_pressed "Link to this definition")
Returns [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") if the device is currently active and [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") otherwise. This property is usually derived from [`value`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button.value "gpiozero.Button.value"). Unlike [`value`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button.value "gpiozero.Button.value"), this is _always_ a boolean.

_property_ pin[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button.pin "Link to this definition")
The [`Pin`](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Pin "gpiozero.Pin") that the device is connected to. This will be [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") if the device has been closed (see the [`close()`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.Device.close "gpiozero.Device.close") method). When dealing with GPIO pins, query `pin.number` to discover the GPIO pin (in BCM numbering) that the device is connected to.

_property_ pull_up[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button.pull_up "Link to this definition")
If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"), the device uses a pull-up resistor to set the GPIO pin “high” by default.

_property_ value[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button.value "Link to this definition")
Returns 1 if the button is currently pressed, and 0 if it is not.

when_held[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button.when_held "Link to this definition")
The function to run when the device has remained active for [`hold_time`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button.hold_time "gpiozero.Button.hold_time") seconds.

This can be set to a function which accepts no (mandatory) parameters, or a Python function which accepts a single mandatory parameter (with as many optional parameters as you like). If the function accepts a single mandatory parameter, the device that activated will be passed as that parameter.

Set this property to [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default) to disable the event.

when_pressed[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button.when_pressed "Link to this definition")
The function to run when the device changes state from inactive to active.

This can be set to a function which accepts no (mandatory) parameters, or a Python function which accepts a single mandatory parameter (with as many optional parameters as you like). If the function accepts a single mandatory parameter, the device that activated it will be passed as that parameter.

Set this property to [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default) to disable the event.

when_released[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button.when_released "Link to this definition")
The function to run when the device changes state from active to inactive.

This can be set to a function which accepts no (mandatory) parameters, or a Python function which accepts a single mandatory parameter (with as many optional parameters as you like). If the function accepts a single mandatory parameter, the device that deactivated it will be passed as that parameter.

Set this property to [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default) to disable the event.

### 14.1.2. LineSensor (TRCT5000)[](https://gpiozero.readthedocs.io/en/stable/api_input.html#linesensor-trct5000 "Link to this heading")

_class_ gpiozero.LineSensor(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/input_devices.html#LineSensor)[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.LineSensor "Link to this definition")
Extends [`SmoothedInputDevice`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.SmoothedInputDevice "gpiozero.SmoothedInputDevice") and represents a single pin line sensor like the TCRT5000 infra-red proximity sensor found in the [CamJam #3 EduKit](http://camjam.me/?page_id=1035).

A typical line sensor has a small circuit board with three pins: VCC, GND, and OUT. VCC should be connected to a 3V3 pin, GND to one of the ground pins, and finally OUT to the GPIO specified as the value of the _pin_ parameter in the constructor.

The following code will print a line of text indicating when the sensor detects a line, or stops detecting a line:

from gpiozero import LineSensor
from signal import pause

sensor = LineSensor(4)
sensor.when_line = lambda: print('Line detected')
sensor.when_no_line = lambda: print('No line detected')
pause()

Parameters:
*   **pin** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")_or_[_str_](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)")) – The GPIO pin which the sensor is connected to. See [Pin Numbering](https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering) for valid pin numbers. If this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") a [`GPIODeviceError`](https://gpiozero.readthedocs.io/en/stable/api_exc.html#gpiozero.GPIODeviceError "gpiozero.GPIODeviceError") will be raised.

*   **pull_up** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")_or_ _None_) – See description under [`InputDevice`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.InputDevice "gpiozero.InputDevice") for more information.

*   **active_state** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")_or_ _None_) – See description under [`InputDevice`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.InputDevice "gpiozero.InputDevice") for more information.

*   **queue_len** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")) – The length of the queue used to store values read from the sensor. This defaults to 5.

*   **sample_rate** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – The number of values to read from the device (and append to the internal queue) per second. Defaults to 100.

*   **threshold** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – Defaults to 0.5. When the average of all values in the internal queue rises above this value, the sensor will be considered “active” by the [`is_active`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.SmoothedInputDevice.is_active "gpiozero.SmoothedInputDevice.is_active") property, and all appropriate events will be fired.

*   **partial** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – When [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") (the default), the object will not return a value for [`is_active`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.SmoothedInputDevice.is_active "gpiozero.SmoothedInputDevice.is_active") until the internal queue has filled with values. Only set this to [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") if you require values immediately after object construction.

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

wait_for_line(_timeout=None_)[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.LineSensor.wait_for_line "Link to this definition")
Pause the script until the device is deactivated, or the timeout is reached.

Parameters:
**timeout** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")_or_ _None_) – Number of seconds to wait before proceeding. If this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default), then wait indefinitely until the device is inactive.

wait_for_no_line(_timeout=None_)[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.LineSensor.wait_for_no_line "Link to this definition")
Pause the script until the device is activated, or the timeout is reached.

Parameters:
**timeout** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")_or_ _None_) – Number of seconds to wait before proceeding. If this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default), then wait indefinitely until the device is active.

_property_ pin[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.LineSensor.pin "Link to this definition")
The [`Pin`](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Pin "gpiozero.Pin") that the device is connected to. This will be [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") if the device has been closed (see the [`close()`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.Device.close "gpiozero.Device.close") method). When dealing with GPIO pins, query `pin.number` to discover the GPIO pin (in BCM numbering) that the device is connected to.

_property_ value[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.LineSensor.value "Link to this definition")
Returns a value representing the average of the queued values. This is nearer 0 for black under the sensor, and nearer 1 for white under the sensor.

when_line[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.LineSensor.when_line "Link to this definition")
The function to run when the device changes state from active to inactive.

This can be set to a function which accepts no (mandatory) parameters, or a Python function which accepts a single mandatory parameter (with as many optional parameters as you like). If the function accepts a single mandatory parameter, the device that deactivated it will be passed as that parameter.

Set this property to [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default) to disable the event.

when_no_line[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.LineSensor.when_no_line "Link to this definition")
The function to run when the device changes state from inactive to active.

This can be set to a function which accepts no (mandatory) parameters, or a Python function which accepts a single mandatory parameter (with as many optional parameters as you like). If the function accepts a single mandatory parameter, the device that activated it will be passed as that parameter.

Set this property to [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default) to disable the event.

### 14.1.3. MotionSensor (D-SUN PIR)[](https://gpiozero.readthedocs.io/en/stable/api_input.html#motionsensor-d-sun-pir "Link to this heading")

_class_ gpiozero.MotionSensor(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/input_devices.html#MotionSensor)[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.MotionSensor "Link to this definition")
Extends [`SmoothedInputDevice`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.SmoothedInputDevice "gpiozero.SmoothedInputDevice") and represents a passive infra-red (PIR) motion sensor like the sort found in the [CamJam #2 EduKit](http://camjam.me/?page_id=623).

A typical PIR device has a small circuit board with three pins: VCC, OUT, and GND. VCC should be connected to a 5V pin, GND to one of the ground pins, and finally OUT to the GPIO specified as the value of the _pin_ parameter in the constructor.

The following code will print a line of text when motion is detected:

from gpiozero import MotionSensor

pir = MotionSensor(4)
pir.wait_for_motion()
print("Motion detected!")

Parameters:
*   **pin** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")_or_[_str_](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)")) – The GPIO pin which the sensor is connected to. See [Pin Numbering](https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering) for valid pin numbers. If this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") a [`GPIODeviceError`](https://gpiozero.readthedocs.io/en/stable/api_exc.html#gpiozero.GPIODeviceError "gpiozero.GPIODeviceError") will be raised.

*   **pull_up** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")_or_ _None_) – See description under [`InputDevice`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.InputDevice "gpiozero.InputDevice") for more information.

*   **active_state** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")_or_ _None_) – See description under [`InputDevice`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.InputDevice "gpiozero.InputDevice") for more information.

*   **queue_len** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")) – The length of the queue used to store values read from the sensor. This defaults to 1 which effectively disables the queue. If your motion sensor is particularly “twitchy” you may wish to increase this value.

*   **sample_rate** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – The number of values to read from the device (and append to the internal queue) per second. Defaults to 10.

*   **threshold** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – Defaults to 0.5. When the average of all values in the internal queue rises above this value, the sensor will be considered “active” by the [`is_active`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.SmoothedInputDevice.is_active "gpiozero.SmoothedInputDevice.is_active") property, and all appropriate events will be fired.

*   **partial** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – When [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") (the default), the object will not return a value for [`is_active`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.SmoothedInputDevice.is_active "gpiozero.SmoothedInputDevice.is_active") until the internal queue has filled with values. Only set this to [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") if you require values immediately after object construction.

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

wait_for_motion(_timeout=None_)[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.MotionSensor.wait_for_motion "Link to this definition")
Pause the script until the device is activated, or the timeout is reached.

Parameters:
**timeout** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")_or_ _None_) – Number of seconds to wait before proceeding. If this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default), then wait indefinitely until the device is active.

wait_for_no_motion(_timeout=None_)[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.MotionSensor.wait_for_no_motion "Link to this definition")
Pause the script until the device is deactivated, or the timeout is reached.

Parameters:
**timeout** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")_or_ _None_) – Number of seconds to wait before proceeding. If this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default), then wait indefinitely until the device is inactive.

_property_ motion_detected[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.MotionSensor.motion_detected "Link to this definition")
Returns [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") if the [`value`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.SmoothedInputDevice.value "gpiozero.SmoothedInputDevice.value") currently exceeds [`threshold`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.SmoothedInputDevice.threshold "gpiozero.SmoothedInputDevice.threshold") and [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") otherwise.

_property_ pin[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.MotionSensor.pin "Link to this definition")
The [`Pin`](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Pin "gpiozero.Pin") that the device is connected to. This will be [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") if the device has been closed (see the [`close()`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.Device.close "gpiozero.Device.close") method). When dealing with GPIO pins, query `pin.number` to discover the GPIO pin (in BCM numbering) that the device is connected to.

_property_ value[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.MotionSensor.value "Link to this definition")
With the default _queue\_len_ of 1, this is effectively boolean where 0 means no motion detected and 1 means motion detected. If you specify a _queue\_len_ greater than 1, this will be an averaged value where values closer to 1 imply motion detection.

when_motion[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.MotionSensor.when_motion "Link to this definition")
The function to run when the device changes state from inactive to active.

This can be set to a function which accepts no (mandatory) parameters, or a Python function which accepts a single mandatory parameter (with as many optional parameters as you like). If the function accepts a single mandatory parameter, the device that activated it will be passed as that parameter.

Set this property to [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default) to disable the event.

when_no_motion[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.MotionSensor.when_no_motion "Link to this definition")
The function to run when the device changes state from active to inactive.

This can be set to a function which accepts no (mandatory) parameters, or a Python function which accepts a single mandatory parameter (with as many optional parameters as you like). If the function accepts a single mandatory parameter, the device that deactivated it will be passed as that parameter.

Set this property to [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default) to disable the event.

### 14.1.4. LightSensor (LDR)[](https://gpiozero.readthedocs.io/en/stable/api_input.html#lightsensor-ldr "Link to this heading")

_class_ gpiozero.LightSensor(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/input_devices.html#LightSensor)[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.LightSensor "Link to this definition")
Extends [`SmoothedInputDevice`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.SmoothedInputDevice "gpiozero.SmoothedInputDevice") and represents a light dependent resistor (LDR).

Connect one leg of the LDR to the 3V3 pin; connect one leg of a 1µF capacitor to a ground pin; connect the other leg of the LDR and the other leg of the capacitor to the same GPIO pin. This class repeatedly discharges the capacitor, then times the duration it takes to charge (which will vary according to the light falling on the LDR).

The following code will print a line of text when light is detected:

from gpiozero import LightSensor

ldr = LightSensor(18)
ldr.wait_for_light()
print("Light detected!")

Parameters:
*   **pin** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")_or_[_str_](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)")) – The GPIO pin which the sensor is attached to. See [Pin Numbering](https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering) for valid pin numbers. If this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") a [`GPIODeviceError`](https://gpiozero.readthedocs.io/en/stable/api_exc.html#gpiozero.GPIODeviceError "gpiozero.GPIODeviceError") will be raised.

*   **queue_len** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")) – The length of the queue used to store values read from the circuit. This defaults to 5.

*   **charge_time_limit** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – If the capacitor in the circuit takes longer than this length of time to charge, it is assumed to be dark. The default (0.01 seconds) is appropriate for a 1µF capacitor coupled with the LDR from the [CamJam #2 EduKit](http://camjam.me/?page_id=623). You may need to adjust this value for different valued capacitors or LDRs.

*   **threshold** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – Defaults to 0.1. When the average of all values in the internal queue rises above this value, the area will be considered “light”, and all appropriate events will be fired.

*   **partial** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – When [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") (the default), the object will not return a value for [`is_active`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.SmoothedInputDevice.is_active "gpiozero.SmoothedInputDevice.is_active") until the internal queue has filled with values. Only set this to [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") if you require values immediately after object construction.

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

wait_for_dark(_timeout=None_)[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.LightSensor.wait_for_dark "Link to this definition")
Pause the script until the device is deactivated, or the timeout is reached.

Parameters:
**timeout** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")_or_ _None_) – Number of seconds to wait before proceeding. If this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default), then wait indefinitely until the device is inactive.

wait_for_light(_timeout=None_)[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.LightSensor.wait_for_light "Link to this definition")
Pause the script until the device is activated, or the timeout is reached.

Parameters:
**timeout** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")_or_ _None_) – Number of seconds to wait before proceeding. If this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default), then wait indefinitely until the device is active.

_property_ light_detected[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.LightSensor.light_detected "Link to this definition")
Returns [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") if the [`value`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.SmoothedInputDevice.value "gpiozero.SmoothedInputDevice.value") currently exceeds [`threshold`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.SmoothedInputDevice.threshold "gpiozero.SmoothedInputDevice.threshold") and [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") otherwise.

_property_ pin[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.LightSensor.pin "Link to this definition")
The [`Pin`](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Pin "gpiozero.Pin") that the device is connected to. This will be [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") if the device has been closed (see the [`close()`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.Device.close "gpiozero.Device.close") method). When dealing with GPIO pins, query `pin.number` to discover the GPIO pin (in BCM numbering) that the device is connected to.

_property_ value[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.LightSensor.value "Link to this definition")
Returns a value between 0 (dark) and 1 (light).

when_dark[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.LightSensor.when_dark "Link to this definition")
The function to run when the device changes state from active to inactive.

This can be set to a function which accepts no (mandatory) parameters, or a Python function which accepts a single mandatory parameter (with as many optional parameters as you like). If the function accepts a single mandatory parameter, the device that deactivated it will be passed as that parameter.

Set this property to [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default) to disable the event.

when_light[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.LightSensor.when_light "Link to this definition")
The function to run when the device changes state from inactive to active.

This can be set to a function which accepts no (mandatory) parameters, or a Python function which accepts a single mandatory parameter (with as many optional parameters as you like). If the function accepts a single mandatory parameter, the device that activated it will be passed as that parameter.

Set this property to [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default) to disable the event.

### 14.1.5. DistanceSensor (HC-SR04)[](https://gpiozero.readthedocs.io/en/stable/api_input.html#distancesensor-hc-sr04 "Link to this heading")

_class_ gpiozero.DistanceSensor(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/input_devices.html#DistanceSensor)[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.DistanceSensor "Link to this definition")
Extends [`SmoothedInputDevice`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.SmoothedInputDevice "gpiozero.SmoothedInputDevice") and represents an HC-SR04 ultrasonic distance sensor, as found in the [CamJam #3 EduKit](http://camjam.me/?page_id=1035).

The distance sensor requires two GPIO pins: one for the _trigger_ (marked TRIG on the sensor) and another for the _echo_ (marked ECHO on the sensor). However, a voltage divider is required to ensure the 5V from the ECHO pin doesn’t damage the Pi. Wire your sensor according to the following instructions:

1.   Connect the GND pin of the sensor to a ground pin on the Pi.

2.   Connect the TRIG pin of the sensor a GPIO pin.

3.   Connect one end of a 330Ω resistor to the ECHO pin of the sensor.

4.   Connect one end of a 470Ω resistor to the GND pin of the sensor.

5.   Connect the free ends of both resistors to another GPIO pin. This forms the required [voltage divider](https://en.wikipedia.org/wiki/Voltage_divider).

6.   Finally, connect the VCC pin of the sensor to a 5V pin on the Pi.

Alternatively, the 3V3 tolerant HC-SR04P sensor (which does not require a voltage divider) will work with this class.

Note

If you do not have the precise values of resistor specified above, don’t worry! What matters is the _ratio_ of the resistors to each other.

You also don’t need to be absolutely precise; the [voltage divider](https://en.wikipedia.org/wiki/Voltage_divider) given above will actually output ~3V (rather than 3.3V). A simple 2:3 ratio will give 3.333V which implies you can take three resistors of equal value, use one of them instead of the 330Ω resistor, and two of them in series instead of the 470Ω resistor.

The following code will periodically report the distance measured by the sensor in cm assuming the TRIG pin is connected to GPIO17, and the ECHO pin to GPIO18:

from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=18, trigger=17)
while True:
    print('Distance: ', sensor.distance * 100)
    sleep(1)

Note

For improved accuracy, use the pigpio pin driver rather than the default RPi.GPIO driver (pigpio uses DMA sampling for much more precise edge timing). This is particularly relevant if you’re using Pi 1 or Pi Zero. See [Changing the pin factory](https://gpiozero.readthedocs.io/en/stable/api_pins.html#changing-pin-factory) for further information.

Parameters:
*   **echo** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")_or_[_str_](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)")) – The GPIO pin which the ECHO pin is connected to. See [Pin Numbering](https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering) for valid pin numbers. If this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") a [`GPIODeviceError`](https://gpiozero.readthedocs.io/en/stable/api_exc.html#gpiozero.GPIODeviceError "gpiozero.GPIODeviceError") will be raised.

*   **trigger** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")_or_[_str_](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)")) – The GPIO pin which the TRIG pin is connected to. See [Pin Numbering](https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering) for valid pin numbers. If this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") a [`GPIODeviceError`](https://gpiozero.readthedocs.io/en/stable/api_exc.html#gpiozero.GPIODeviceError "gpiozero.GPIODeviceError") will be raised.

*   **queue_len** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")) – The length of the queue used to store values read from the sensor. This defaults to 9.

*   **max_distance** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – The [`value`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.DistanceSensor.value "gpiozero.DistanceSensor.value") attribute reports a normalized value between 0 (too close to measure) and 1 (maximum distance). This parameter specifies the maximum distance expected in meters. This defaults to 1.

*   **threshold_distance** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – Defaults to 0.3. This is the distance (in meters) that will trigger the `in_range` and `out_of_range` events when crossed.

*   **partial** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – When [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") (the default), the object will not return a value for [`is_active`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.SmoothedInputDevice.is_active "gpiozero.SmoothedInputDevice.is_active") until the internal queue has filled with values. Only set this to [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") if you require values immediately after object construction.

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

wait_for_in_range(_timeout=None_)[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.DistanceSensor.wait_for_in_range "Link to this definition")
Pause the script until the device is deactivated, or the timeout is reached.

Parameters:
**timeout** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")_or_ _None_) – Number of seconds to wait before proceeding. If this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default), then wait indefinitely until the device is inactive.

wait_for_out_of_range(_timeout=None_)[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.DistanceSensor.wait_for_out_of_range "Link to this definition")
Pause the script until the device is activated, or the timeout is reached.

Parameters:
**timeout** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")_or_ _None_) – Number of seconds to wait before proceeding. If this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default), then wait indefinitely until the device is active.

_property_ distance[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.DistanceSensor.distance "Link to this definition")
Returns the current distance measured by the sensor in meters. Note that this property will have a value between 0 and [`max_distance`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.DistanceSensor.max_distance "gpiozero.DistanceSensor.max_distance").

_property_ echo[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.DistanceSensor.echo "Link to this definition")
Returns the [`Pin`](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Pin "gpiozero.Pin") that the sensor’s echo is connected to. This is simply an alias for the usual [`pin`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.GPIODevice.pin "gpiozero.GPIODevice.pin") attribute.

_property_ max_distance[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.DistanceSensor.max_distance "Link to this definition")
The maximum distance that the sensor will measure in meters. This value is specified in the constructor and is used to provide the scaling for the [`value`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.SmoothedInputDevice.value "gpiozero.SmoothedInputDevice.value") attribute. When [`distance`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.DistanceSensor.distance "gpiozero.DistanceSensor.distance") is equal to [`max_distance`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.DistanceSensor.max_distance "gpiozero.DistanceSensor.max_distance"), [`value`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.SmoothedInputDevice.value "gpiozero.SmoothedInputDevice.value") will be 1.

_property_ threshold_distance[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.DistanceSensor.threshold_distance "Link to this definition")
The distance, measured in meters, that will trigger the [`when_in_range`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.DistanceSensor.when_in_range "gpiozero.DistanceSensor.when_in_range") and [`when_out_of_range`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.DistanceSensor.when_out_of_range "gpiozero.DistanceSensor.when_out_of_range") events when crossed. This is simply a meter-scaled variant of the usual [`threshold`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.SmoothedInputDevice.threshold "gpiozero.SmoothedInputDevice.threshold") attribute.

_property_ trigger[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.DistanceSensor.trigger "Link to this definition")
Returns the [`Pin`](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Pin "gpiozero.Pin") that the sensor’s trigger is connected to.

_property_ value[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.DistanceSensor.value "Link to this definition")
Returns a value between 0, indicating the reflector is either touching the sensor or is sufficiently near that the sensor can’t tell the difference, and 1, indicating the reflector is at or beyond the specified _max\_distance_.

when_in_range[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.DistanceSensor.when_in_range "Link to this definition")
The function to run when the device changes state from active to inactive.

This can be set to a function which accepts no (mandatory) parameters, or a Python function which accepts a single mandatory parameter (with as many optional parameters as you like). If the function accepts a single mandatory parameter, the device that deactivated it will be passed as that parameter.

Set this property to [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default) to disable the event.

when_out_of_range[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.DistanceSensor.when_out_of_range "Link to this definition")
The function to run when the device changes state from inactive to active.

This can be set to a function which accepts no (mandatory) parameters, or a Python function which accepts a single mandatory parameter (with as many optional parameters as you like). If the function accepts a single mandatory parameter, the device that activated it will be passed as that parameter.

Set this property to [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default) to disable the event.

### 14.1.6. RotaryEncoder[](https://gpiozero.readthedocs.io/en/stable/api_input.html#rotaryencoder "Link to this heading")

_class_ gpiozero.RotaryEncoder(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/input_devices.html#RotaryEncoder)[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.RotaryEncoder "Link to this definition")
Represents a simple two-pin incremental [rotary encoder](https://en.wikipedia.org/wiki/Rotary_encoder) device.

These devices typically have three pins labelled “A”, “B”, and “C”. Connect A and B directly to two GPIO pins, and C (“common”) to one of the ground pins on your Pi. Then simply specify the A and B pins as the arguments when constructing this classs.

For example, if your encoder’s A pin is connected to GPIO 21, and the B pin to GPIO 20 (and presumably the C pin to a suitable GND pin), while an LED (with a suitable 300Ω resistor) is connected to GPIO 5, the following session will result in the brightness of the LED being controlled by dialling the rotary encoder back and forth:

>>> from gpiozero import RotaryEncoder
>>> from gpiozero.tools import scaled_half
>>> rotor = RotaryEncoder(21, 20)
>>> led = PWMLED(5)
>>> led.source = scaled_half(rotor.values)

Parameters:
*   **a** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")_or_[_str_](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)")) – The GPIO pin connected to the “A” output of the rotary encoder.

*   **b** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")_or_[_str_](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)")) – The GPIO pin connected to the “B” output of the rotary encoder.

*   **bounce_time** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")_or_ _None_) – If [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default), no software bounce compensation will be performed. Otherwise, this is the length of time (in seconds) that the component will ignore changes in state after an initial change.

*   **max_steps** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")) – The number of steps clockwise the encoder takes to change the [`value`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.RotaryEncoder.value "gpiozero.RotaryEncoder.value") from 0 to 1, or counter-clockwise from 0 to -1. If this is 0, then the encoder’s [`value`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.RotaryEncoder.value "gpiozero.RotaryEncoder.value") never changes, but you can still read [`steps`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.RotaryEncoder.steps "gpiozero.RotaryEncoder.steps") to determine the integer number of steps the encoder has moved clockwise or counter clockwise.

*   **threshold_steps** ([_tuple_](https://docs.python.org/3.9/library/stdtypes.html#tuple "(in Python v3.9)")_of_[_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")) – A (min, max) tuple of steps between which the device will be considered “active”, inclusive. In other words, when [`steps`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.RotaryEncoder.steps "gpiozero.RotaryEncoder.steps") is greater than or equal to the _min_ value, and less than or equal the _max_ value, the `active` property will be [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") and the appropriate events (`when_activated`, `when_deactivated`) will be fired. Defaults to (0, 0).

*   **wrap** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") and _max\_steps_ is non-zero, when the [`steps`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.RotaryEncoder.steps "gpiozero.RotaryEncoder.steps") reaches positive or negative _max\_steps_ it wraps around by negation. Defaults to [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)").

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

wait_for_rotate(_timeout=None_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/input_devices.html#RotaryEncoder.wait_for_rotate)[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.RotaryEncoder.wait_for_rotate "Link to this definition")
Pause the script until the encoder is rotated at least one step in either direction, or the timeout is reached.

Parameters:
**timeout** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")_or_ _None_) – Number of seconds to wait before proceeding. If this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default), then wait indefinitely until the encoder is rotated.

wait_for_rotate_clockwise(_timeout=None_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/input_devices.html#RotaryEncoder.wait_for_rotate_clockwise)[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.RotaryEncoder.wait_for_rotate_clockwise "Link to this definition")
Pause the script until the encoder is rotated at least one step clockwise, or the timeout is reached.

Parameters:
**timeout** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")_or_ _None_) – Number of seconds to wait before proceeding. If this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default), then wait indefinitely until the encoder is rotated clockwise.

wait_for_rotate_counter_clockwise(_timeout=None_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/input_devices.html#RotaryEncoder.wait_for_rotate_counter_clockwise)[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.RotaryEncoder.wait_for_rotate_counter_clockwise "Link to this definition")
Pause the script until the encoder is rotated at least one step counter-clockwise, or the timeout is reached.

Parameters:
**timeout** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")_or_ _None_) – Number of seconds to wait before proceeding. If this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default), then wait indefinitely until the encoder is rotated counter-clockwise.

_property_ max_steps[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.RotaryEncoder.max_steps "Link to this definition")
The number of discrete steps the rotary encoder takes to move [`value`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.RotaryEncoder.value "gpiozero.RotaryEncoder.value") from 0 to 1 clockwise, or 0 to -1 counter-clockwise. In another sense, this is also the total number of discrete states this input can represent.

_property_ steps[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.RotaryEncoder.steps "Link to this definition")
The “steps” value of the encoder starts at 0. It increments by one for every step the encoder is rotated clockwise, and decrements by one for every step it is rotated counter-clockwise. The steps value is limited by [`max_steps`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.RotaryEncoder.max_steps "gpiozero.RotaryEncoder.max_steps"). It will not advance beyond positive or negative [`max_steps`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.RotaryEncoder.max_steps "gpiozero.RotaryEncoder.max_steps"), unless [`wrap`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.RotaryEncoder.wrap "gpiozero.RotaryEncoder.wrap") is [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") in which case it will roll around by negation. If [`max_steps`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.RotaryEncoder.max_steps "gpiozero.RotaryEncoder.max_steps") is zero then steps are not limited at all, and will increase infinitely in either direction, but [`value`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.RotaryEncoder.value "gpiozero.RotaryEncoder.value") will return a constant zero.

Note that, in contrast to most other input devices, because the rotary encoder has no absolute position the [`steps`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.RotaryEncoder.steps "gpiozero.RotaryEncoder.steps") attribute (and [`value`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.RotaryEncoder.value "gpiozero.RotaryEncoder.value") by corollary) is writable.

_property_ threshold_steps[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.RotaryEncoder.threshold_steps "Link to this definition")
The mininum and maximum number of steps between which `is_active` will return [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"). Defaults to (0, 0).

_property_ value[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.RotaryEncoder.value "Link to this definition")
Represents the value of the rotary encoder as a value between -1 and 1. The value is calculated by dividing the value of [`steps`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.RotaryEncoder.steps "gpiozero.RotaryEncoder.steps") into the range from negative [`max_steps`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.RotaryEncoder.max_steps "gpiozero.RotaryEncoder.max_steps") to positive [`max_steps`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.RotaryEncoder.max_steps "gpiozero.RotaryEncoder.max_steps").

Note that, in contrast to most other input devices, because the rotary encoder has no absolute position the [`value`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.RotaryEncoder.value "gpiozero.RotaryEncoder.value") attribute is writable.

when_rotated[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.RotaryEncoder.when_rotated "Link to this definition")
The function to be run when the encoder is rotated in either direction.

This can be set to a function which accepts no (mandatory) parameters, or a Python function which accepts a single mandatory parameter (with as many optional parameters as you like). If the function accepts a single mandatory parameter, the device that activated will be passed as that parameter.

Set this property to [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default) to disable the event.

when_rotated_clockwise[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.RotaryEncoder.when_rotated_clockwise "Link to this definition")
The function to be run when the encoder is rotated clockwise.

This can be set to a function which accepts no (mandatory) parameters, or a Python function which accepts a single mandatory parameter (with as many optional parameters as you like). If the function accepts a single mandatory parameter, the device that activated will be passed as that parameter.

Set this property to [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default) to disable the event.

when_rotated_counter_clockwise[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.RotaryEncoder.when_rotated_counter_clockwise "Link to this definition")
The function to be run when the encoder is rotated counter-clockwise.

This can be set to a function which accepts no (mandatory) parameters, or a Python function which accepts a single mandatory parameter (with as many optional parameters as you like). If the function accepts a single mandatory parameter, the device that activated will be passed as that parameter.

Set this property to [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default) to disable the event.

_property_ wrap[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.RotaryEncoder.wrap "Link to this definition")
If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"), when [`value`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.RotaryEncoder.value "gpiozero.RotaryEncoder.value") reaches its limit (-1 or 1), it “wraps around” to the opposite limit. When [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)"), the value (and the corresponding [`steps`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.RotaryEncoder.steps "gpiozero.RotaryEncoder.steps") attribute) simply don’t advance beyond their limits.

14.2. Base Classes[](https://gpiozero.readthedocs.io/en/stable/api_input.html#base-classes "Link to this heading")
-------------------------------------------------------------------------------------------------------------------

The classes in the sections above are derived from a series of base classes, some of which are effectively abstract. The classes form the (partial) hierarchy displayed in the graph below (abstract classes are shaded lighter than concrete classes):

![Image 1: _images/input_device_hierarchy.svg](https://gpiozero.readthedocs.io/en/stable/_images/input_device_hierarchy.svg)
The following sections document these base classes for advanced users that wish to construct classes for their own devices.

### 14.2.1. DigitalInputDevice[](https://gpiozero.readthedocs.io/en/stable/api_input.html#digitalinputdevice "Link to this heading")

_class_ gpiozero.DigitalInputDevice(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/input_devices.html#DigitalInputDevice)[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.DigitalInputDevice "Link to this definition")
Represents a generic input device with typical on/off behaviour.

This class extends [`InputDevice`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.InputDevice "gpiozero.InputDevice") with machinery to fire the active and inactive events for devices that operate in a typical digital manner: straight forward on / off states with (reasonably) clean transitions between the two.

Parameters:
*   **pin** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")_or_[_str_](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)")) – The GPIO pin that the device is connected to. See [Pin Numbering](https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering) for valid pin numbers. If this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") a [`GPIODeviceError`](https://gpiozero.readthedocs.io/en/stable/api_exc.html#gpiozero.GPIODeviceError "gpiozero.GPIODeviceError") will be raised.

*   **pull_up** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")_or_ _None_) – See description under [`InputDevice`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.InputDevice "gpiozero.InputDevice") for more information.

*   **active_state** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")_or_ _None_) – See description under [`InputDevice`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.InputDevice "gpiozero.InputDevice") for more information.

*   **bounce_time** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")_or_ _None_) – Specifies the length of time (in seconds) that the component will ignore changes in state after an initial change. This defaults to [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") which indicates that no bounce compensation will be performed.

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

wait_for_active(_timeout=None_)[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.DigitalInputDevice.wait_for_active "Link to this definition")
Pause the script until the device is activated, or the timeout is reached.

Parameters:
**timeout** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")_or_ _None_) – Number of seconds to wait before proceeding. If this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default), then wait indefinitely until the device is active.

wait_for_inactive(_timeout=None_)[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.DigitalInputDevice.wait_for_inactive "Link to this definition")
Pause the script until the device is deactivated, or the timeout is reached.

Parameters:
**timeout** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")_or_ _None_) – Number of seconds to wait before proceeding. If this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default), then wait indefinitely until the device is inactive.

_property_ active_time[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.DigitalInputDevice.active_time "Link to this definition")
The length of time (in seconds) that the device has been active for. When the device is inactive, this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)").

_property_ inactive_time[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.DigitalInputDevice.inactive_time "Link to this definition")
The length of time (in seconds) that the device has been inactive for. When the device is active, this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)").

_property_ value[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.DigitalInputDevice.value "Link to this definition")
Returns a value representing the device’s state. Frequently, this is a boolean value, or a number between 0 and 1 but some devices use larger ranges (e.g. -1 to +1) and composite devices usually use tuples to return the states of all their subordinate components.

when_activated[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.DigitalInputDevice.when_activated "Link to this definition")
The function to run when the device changes state from inactive to active.

This can be set to a function which accepts no (mandatory) parameters, or a Python function which accepts a single mandatory parameter (with as many optional parameters as you like). If the function accepts a single mandatory parameter, the device that activated it will be passed as that parameter.

Set this property to [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default) to disable the event.

when_deactivated[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.DigitalInputDevice.when_deactivated "Link to this definition")
The function to run when the device changes state from active to inactive.

This can be set to a function which accepts no (mandatory) parameters, or a Python function which accepts a single mandatory parameter (with as many optional parameters as you like). If the function accepts a single mandatory parameter, the device that deactivated it will be passed as that parameter.

Set this property to [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default) to disable the event.

### 14.2.2. SmoothedInputDevice[](https://gpiozero.readthedocs.io/en/stable/api_input.html#smoothedinputdevice "Link to this heading")

_class_ gpiozero.SmoothedInputDevice(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/input_devices.html#SmoothedInputDevice)[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.SmoothedInputDevice "Link to this definition")
Represents a generic input device which takes its value from the average of a queue of historical values.

This class extends [`InputDevice`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.InputDevice "gpiozero.InputDevice") with a queue which is filled by a background thread which continually polls the state of the underlying device. The average (a configurable function) of the values in the queue is compared to a threshold which is used to determine the state of the [`is_active`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.SmoothedInputDevice.is_active "gpiozero.SmoothedInputDevice.is_active") property.

Note

The background queue is not automatically started upon construction. This is to allow descendents to set up additional components before the queue starts reading values. Effectively this is an abstract base class.

This class is intended for use with devices which either exhibit analog behaviour (such as the charging time of a capacitor with an LDR), or those which exhibit “twitchy” behaviour (such as certain motion sensors).

Parameters:
*   **pin** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")_or_[_str_](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)")) – The GPIO pin that the device is connected to. See [Pin Numbering](https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering) for valid pin numbers. If this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") a [`GPIODeviceError`](https://gpiozero.readthedocs.io/en/stable/api_exc.html#gpiozero.GPIODeviceError "gpiozero.GPIODeviceError") will be raised.

*   **pull_up** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")_or_ _None_) – See description under [`InputDevice`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.InputDevice "gpiozero.InputDevice") for more information.

*   **active_state** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")_or_ _None_) – See description under [`InputDevice`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.InputDevice "gpiozero.InputDevice") for more information.

*   **threshold** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – The value above which the device will be considered “on”.

*   **queue_len** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")) – The length of the internal queue which is filled by the background thread.

*   **sample_wait** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – The length of time to wait between retrieving the state of the underlying device. Defaults to 0.0 indicating that values are retrieved as fast as possible.

*   **partial** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") (the default), attempts to read the state of the device (from the [`is_active`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.SmoothedInputDevice.is_active "gpiozero.SmoothedInputDevice.is_active") property) will block until the queue has filled. If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"), a value will be returned immediately, but be aware that this value is likely to fluctuate excessively.

*   **average** – The function used to average the values in the internal queue. This defaults to [`statistics.median()`](https://docs.python.org/3.9/library/statistics.html#statistics.median "(in Python v3.9)") which is a good selection for discarding outliers from jittery sensors. The function specified must accept a sequence of numbers and return a single number.

*   **ignore** ([_frozenset_](https://docs.python.org/3.9/library/stdtypes.html#frozenset "(in Python v3.9)")_or_ _None_) – The set of values which the queue should ignore, if returned from querying the device’s value.

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

_property_ is_active[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.SmoothedInputDevice.is_active "Link to this definition")
Returns [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") if the [`value`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.SmoothedInputDevice.value "gpiozero.SmoothedInputDevice.value") currently exceeds [`threshold`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.SmoothedInputDevice.threshold "gpiozero.SmoothedInputDevice.threshold") and [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") otherwise.

_property_ partial[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.SmoothedInputDevice.partial "Link to this definition")
If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") (the default), attempts to read the [`value`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.SmoothedInputDevice.value "gpiozero.SmoothedInputDevice.value") or [`is_active`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.SmoothedInputDevice.is_active "gpiozero.SmoothedInputDevice.is_active") properties will block until the queue has filled.

_property_ queue_len[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.SmoothedInputDevice.queue_len "Link to this definition")
The length of the internal queue of values which is averaged to determine the overall state of the device. This defaults to 5.

_property_ threshold[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.SmoothedInputDevice.threshold "Link to this definition")
If [`value`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.SmoothedInputDevice.value "gpiozero.SmoothedInputDevice.value") exceeds this amount, then [`is_active`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.SmoothedInputDevice.is_active "gpiozero.SmoothedInputDevice.is_active") will return [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)").

_property_ value[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.SmoothedInputDevice.value "Link to this definition")
Returns the average of the values in the internal queue. This is compared to [`threshold`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.SmoothedInputDevice.threshold "gpiozero.SmoothedInputDevice.threshold") to determine whether [`is_active`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.SmoothedInputDevice.is_active "gpiozero.SmoothedInputDevice.is_active") is [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)").

### 14.2.3. InputDevice[](https://gpiozero.readthedocs.io/en/stable/api_input.html#inputdevice "Link to this heading")

_class_ gpiozero.InputDevice(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/input_devices.html#InputDevice)[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.InputDevice "Link to this definition")
Represents a generic GPIO input device.

This class extends [`GPIODevice`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.GPIODevice "gpiozero.GPIODevice") to add facilities common to GPIO input devices. The constructor adds the optional _pull\_up_ parameter to specify how the pin should be pulled by the internal resistors. The [`is_active`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.InputDevice.is_active "gpiozero.InputDevice.is_active") property is adjusted accordingly so that [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") still means active regardless of the _pull\_up_ setting.

Parameters:
*   **pin** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")_or_[_str_](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)")) – The GPIO pin that the device is connected to. See [Pin Numbering](https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering) for valid pin numbers. If this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") a [`GPIODeviceError`](https://gpiozero.readthedocs.io/en/stable/api_exc.html#gpiozero.GPIODeviceError "gpiozero.GPIODeviceError") will be raised.

*   **pull_up** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")_or_ _None_) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"), the pin will be pulled high with an internal resistor. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") (the default), the pin will be pulled low. If [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)"), the pin will be floating. As gpiozero cannot automatically guess the active state when not pulling the pin, the _active\_state_ parameter must be passed.

*   **active_state** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")_or_ _None_) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"), when the hardware pin state is `HIGH`, the software pin is `HIGH`. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)"), the input polarity is reversed: when the hardware pin state is `HIGH`, the software pin state is `LOW`. Use this parameter to set the active state of the underlying pin when configuring it as not pulled (when _pull\_up_ is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)")). When _pull\_up_ is [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") or [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)"), the active state is automatically set to the proper value.

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

_property_ is_active[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.InputDevice.is_active "Link to this definition")
Returns [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") if the device is currently active and [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") otherwise. This property is usually derived from [`value`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.InputDevice.value "gpiozero.InputDevice.value"). Unlike [`value`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.InputDevice.value "gpiozero.InputDevice.value"), this is _always_ a boolean.

_property_ pull_up[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.InputDevice.pull_up "Link to this definition")
If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"), the device uses a pull-up resistor to set the GPIO pin “high” by default.

_property_ value[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.InputDevice.value "Link to this definition")
Returns a value representing the device’s state. Frequently, this is a boolean value, or a number between 0 and 1 but some devices use larger ranges (e.g. -1 to +1) and composite devices usually use tuples to return the states of all their subordinate components.

### 14.2.4. GPIODevice[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiodevice "Link to this heading")

_class_ gpiozero.GPIODevice(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/devices.html#GPIODevice)[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.GPIODevice "Link to this definition")
Extends [`Device`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.Device "gpiozero.Device"). Represents a generic GPIO device and provides the services common to all single-pin GPIO devices (like ensuring two GPIO devices do no share a [`pin`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.GPIODevice.pin "gpiozero.GPIODevice.pin")).

Parameters:
**pin** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")_or_[_str_](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)")) – The GPIO pin that the device is connected to. See [Pin Numbering](https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering) for valid pin numbers. If this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") a [`GPIODeviceError`](https://gpiozero.readthedocs.io/en/stable/api_exc.html#gpiozero.GPIODeviceError "gpiozero.GPIODeviceError") will be raised. If the pin is already in use by another device, [`GPIOPinInUse`](https://gpiozero.readthedocs.io/en/stable/api_exc.html#gpiozero.GPIOPinInUse "gpiozero.GPIOPinInUse") will be raised.

close()[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/devices.html#GPIODevice.close)[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.GPIODevice.close "Link to this definition")
Shut down the device and release all associated resources (such as GPIO pins).

This method is idempotent (can be called on an already closed device without any side-effects). It is primarily intended for interactive use at the command line. It disables the device and releases its pin(s) for use by another device.

You can attempt to do this simply by deleting an object, but unless you’ve cleaned up all references to the object this may not work (even if you’ve cleaned up all references, there’s still no guarantee the garbage collector will actually delete the object at that point). By contrast, the close method provides a means of ensuring that the object is shut down.

For example, if you have a breadboard with a buzzer connected to pin 16, but then wish to attach an LED instead:

>>> from gpiozero import *
>>> bz = Buzzer(16)
>>> bz.on()
>>> bz.off()
>>> bz.close()
>>> led = LED(16)
>>> led.blink()

[`Device`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.Device "gpiozero.Device") descendents can also be used as context managers using the [`with`](https://docs.python.org/3.9/reference/compound_stmts.html#with "(in Python v3.9)") statement. For example:

>>> from gpiozero import *
>>> with Buzzer(16) as bz:
...     bz.on()
...
>>> with LED(16) as led:
...     led.on()
...

_property_ closed[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.GPIODevice.closed "Link to this definition")
Returns [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") if the device is closed (see the [`close()`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.GPIODevice.close "gpiozero.GPIODevice.close") method). Once a device is closed you can no longer use any other methods or properties to control or query the device.

_property_ pin[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.GPIODevice.pin "Link to this definition")
The [`Pin`](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Pin "gpiozero.Pin") that the device is connected to. This will be [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") if the device has been closed (see the [`close()`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.Device.close "gpiozero.Device.close") method). When dealing with GPIO pins, query `pin.number` to discover the GPIO pin (in BCM numbering) that the device is connected to.

_property_ value[](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.GPIODevice.value "Link to this definition")
Returns a value representing the device’s state. Frequently, this is a boolean value, or a number between 0 and 1 but some devices use larger ranges (e.g. -1 to +1) and composite devices usually use tuples to return the states of all their subordinate components.
