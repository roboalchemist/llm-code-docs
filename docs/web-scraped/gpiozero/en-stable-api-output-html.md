# Source: https://gpiozero.readthedocs.io/en/stable/api_output.html

Title: Output Devices — gpiozero 2.0.1 Documentation

URL Source: https://gpiozero.readthedocs.io/en/stable/api_output.html

Markdown Content:
15. API - Output Devices[](https://gpiozero.readthedocs.io/en/stable/api_output.html#module-gpiozero.output_devices "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------

These output device component interfaces have been provided for simple use of everyday components. Components must be wired up correctly before use in code.

Note

All GPIO pin numbers use Broadcom (BCM) numbering by default. See the [Pin Numbering](https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering) section for more information.

15.1. Regular Classes[](https://gpiozero.readthedocs.io/en/stable/api_output.html#regular-classes "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------

The following classes are intended for general use with the devices they represent. All classes in this section are concrete (not abstract).

### 15.1.1. LED[](https://gpiozero.readthedocs.io/en/stable/api_output.html#led "Link to this heading")

_class_ gpiozero.LED(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/output_devices.html#LED)[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED "Link to this definition")
Extends [`DigitalOutputDevice`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.DigitalOutputDevice "gpiozero.DigitalOutputDevice") and represents a light emitting diode (LED).

Connect the cathode (short leg, flat side) of the LED to a ground pin; connect the anode (longer leg) to a limiting resistor; connect the other side of the limiting resistor to a GPIO pin (the limiting resistor can be placed either side of the LED).

The following example will light the LED:

from gpiozero import LED

led = LED(17)
led.on()

Parameters:
*   **pin** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")_or_[_str_](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)")) – The GPIO pin which the LED is connected to. See [Pin Numbering](https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering) for valid pin numbers. If this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") a [`GPIODeviceError`](https://gpiozero.readthedocs.io/en/stable/api_exc.html#gpiozero.GPIODeviceError "gpiozero.GPIODeviceError") will be raised.

*   **active_high** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") (the default), the LED will operate normally with the circuit described above. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") you should wire the cathode to the GPIO pin, and the anode to a 3V3 pin (via a limiting resistor).

*   **initial_value** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")_or_ _None_) – If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") (the default), the LED will be off initially. If [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)"), the LED will be left in whatever state the pin is found in when configured for output (warning: this can be on). If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"), the LED will be switched on initially.

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

blink(_on\_time=1_, _off\_time=1_, _n=None_, _background=True_)[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED.blink "Link to this definition")
Make the device turn on and off repeatedly.

Parameters:
*   **on_time** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – Number of seconds on. Defaults to 1 second.

*   **off_time** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – Number of seconds off. Defaults to 1 second.

*   **n** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")_or_ _None_) – Number of times to blink; [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default) means forever.

*   **background** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") (the default), start a background thread to continue blinking and return immediately. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)"), only return when the blink is finished (warning: the default value of _n_ will result in this method never returning).

off()[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED.off "Link to this definition")
Turns the device off.

on()[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED.on "Link to this definition")
Turns the device on.

toggle()[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED.toggle "Link to this definition")
Reverse the state of the device. If it’s on, turn it off; if it’s off, turn it on.

_property_ is_lit[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED.is_lit "Link to this definition")
Returns [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") if the device is currently active and [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") otherwise. This property is usually derived from [`value`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED.value "gpiozero.LED.value"). Unlike [`value`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED.value "gpiozero.LED.value"), this is _always_ a boolean.

_property_ pin[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED.pin "Link to this definition")
The [`Pin`](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Pin "gpiozero.Pin") that the device is connected to. This will be [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") if the device has been closed (see the [`close()`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.Device.close "gpiozero.Device.close") method). When dealing with GPIO pins, query `pin.number` to discover the GPIO pin (in BCM numbering) that the device is connected to.

_property_ value[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED.value "Link to this definition")
Returns 1 if the device is currently active and 0 otherwise. Setting this property changes the state of the device.

### 15.1.2. PWMLED[](https://gpiozero.readthedocs.io/en/stable/api_output.html#pwmled "Link to this heading")

_class_ gpiozero.PWMLED(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/output_devices.html#PWMLED)[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED "Link to this definition")
Extends [`PWMOutputDevice`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMOutputDevice "gpiozero.PWMOutputDevice") and represents a light emitting diode (LED) with variable brightness.

A typical configuration of such a device is to connect a GPIO pin to the anode (long leg) of the LED, and the cathode (short leg) to ground, with an optional resistor to prevent the LED from burning out.

Parameters:
*   **pin** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")_or_[_str_](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)")) – The GPIO pin which the LED is connected to. See [Pin Numbering](https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering) for valid pin numbers. If this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") a [`GPIODeviceError`](https://gpiozero.readthedocs.io/en/stable/api_exc.html#gpiozero.GPIODeviceError "gpiozero.GPIODeviceError") will be raised.

*   **active_high** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") (the default), the [`on()`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED.on "gpiozero.PWMLED.on") method will set the GPIO to HIGH. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)"), the [`on()`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED.on "gpiozero.PWMLED.on") method will set the GPIO to LOW (the [`off()`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED.off "gpiozero.PWMLED.off") method always does the opposite).

*   **initial_value** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – If `0` (the default), the LED will be off initially. Other values between 0 and 1 can be specified as an initial brightness for the LED. Note that [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") cannot be specified (unlike the parent class) as there is no way to tell PWM not to alter the state of the pin.

*   **frequency** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")) – The frequency (in Hz) of pulses emitted to drive the LED. Defaults to 100Hz.

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

blink(_on\_time=1_, _off\_time=1_, _fade\_in\_time=0_, _fade\_out\_time=0_, _n=None_, _background=True_)[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED.blink "Link to this definition")
Make the device turn on and off repeatedly.

Parameters:
*   **on_time** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – Number of seconds on. Defaults to 1 second.

*   **off_time** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – Number of seconds off. Defaults to 1 second.

*   **fade_in_time** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – Number of seconds to spend fading in. Defaults to 0.

*   **fade_out_time** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – Number of seconds to spend fading out. Defaults to 0.

*   **n** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")_or_ _None_) – Number of times to blink; [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default) means forever.

*   **background** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") (the default), start a background thread to continue blinking and return immediately. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)"), only return when the blink is finished (warning: the default value of _n_ will result in this method never returning).

off()[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED.off "Link to this definition")
Turns the device off.

on()[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED.on "Link to this definition")
Turns the device on.

pulse(_fade\_in\_time=1_, _fade\_out\_time=1_, _n=None_, _background=True_)[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED.pulse "Link to this definition")
Make the device fade in and out repeatedly.

Parameters:
*   **fade_in_time** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – Number of seconds to spend fading in. Defaults to 1.

*   **fade_out_time** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – Number of seconds to spend fading out. Defaults to 1.

*   **n** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")_or_ _None_) – Number of times to pulse; [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default) means forever.

*   **background** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") (the default), start a background thread to continue pulsing and return immediately. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)"), only return when the pulse is finished (warning: the default value of _n_ will result in this method never returning).

toggle()[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED.toggle "Link to this definition")
Toggle the state of the device. If the device is currently off ([`value`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED.value "gpiozero.PWMLED.value") is 0.0), this changes it to “fully” on ([`value`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED.value "gpiozero.PWMLED.value") is 1.0). If the device has a duty cycle ([`value`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED.value "gpiozero.PWMLED.value")) of 0.1, this will toggle it to 0.9, and so on.

_property_ is_lit[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED.is_lit "Link to this definition")
Returns [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") if the device is currently active ([`value`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED.value "gpiozero.PWMLED.value") is non-zero) and [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") otherwise.

_property_ pin[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED.pin "Link to this definition")
The [`Pin`](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Pin "gpiozero.Pin") that the device is connected to. This will be [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") if the device has been closed (see the [`close()`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.Device.close "gpiozero.Device.close") method). When dealing with GPIO pins, query `pin.number` to discover the GPIO pin (in BCM numbering) that the device is connected to.

_property_ value[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED.value "Link to this definition")
The duty cycle of the PWM device. 0.0 is off, 1.0 is fully on. Values in between may be specified for varying levels of power in the device.

### 15.1.3. RGBLED[](https://gpiozero.readthedocs.io/en/stable/api_output.html#rgbled "Link to this heading")

_class_ gpiozero.RGBLED(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/output_devices.html#RGBLED)[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.RGBLED "Link to this definition")
Extends [`Device`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.Device "gpiozero.Device") and represents a full color LED component (composed of red, green, and blue LEDs).

Connect the common cathode (longest leg) to a ground pin; connect each of the other legs (representing the red, green, and blue anodes) to any GPIO pins. You should use three limiting resistors (one per anode).

The following code will make the LED yellow:

from gpiozero import RGBLED

led = RGBLED(2, 3, 4)
led.color = (1, 1, 0)

The [colorzero](https://colorzero.readthedocs.io/) library is also supported:

from gpiozero import RGBLED
from colorzero import Color

led = RGBLED(2, 3, 4)
led.color = Color('yellow')

Parameters:
*   **red** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")_or_[_str_](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)")) – The GPIO pin that controls the red component of the RGB LED. See [Pin Numbering](https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering) for valid pin numbers. If this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") a [`GPIODeviceError`](https://gpiozero.readthedocs.io/en/stable/api_exc.html#gpiozero.GPIODeviceError "gpiozero.GPIODeviceError") will be raised.

*   **green** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")_or_[_str_](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)")) – The GPIO pin that controls the green component of the RGB LED.

*   **blue** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")_or_[_str_](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)")) – The GPIO pin that controls the blue component of the RGB LED.

*   **active_high** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – Set to [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") (the default) for common cathode RGB LEDs. If you are using a common anode RGB LED, set this to [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)").

*   **initial_value** ([_Color_](https://colorzero.readthedocs.io/en/latest/api_color.html#colorzero.Color "(in Colorzero v2.0)")_or_[_tuple_](https://docs.python.org/3.9/library/stdtypes.html#tuple "(in Python v3.9)")) – The initial color for the RGB LED. Defaults to black `(0, 0, 0)`.

*   **pwm** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") (the default), construct [`PWMLED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED "gpiozero.PWMLED") instances for each component of the RGBLED. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)"), construct regular [`LED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED "gpiozero.LED") instances, which prevents smooth color graduations.

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

blink(_on\_time=1_, _off\_time=1_, _fade\_in\_time=0_, _fade\_out\_time=0_, _on\_color=(1,1,1)_, _off\_color=(0,0,0)_, _n=None_, _background=True_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/output_devices.html#RGBLED.blink)[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.RGBLED.blink "Link to this definition")
Make the device turn on and off repeatedly.

Parameters:
*   **on_time** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – Number of seconds on. Defaults to 1 second.

*   **off_time** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – Number of seconds off. Defaults to 1 second.

*   **fade_in_time** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – Number of seconds to spend fading in. Defaults to 0. Must be 0 if _pwm_ was [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") when the class was constructed ([`ValueError`](https://docs.python.org/3.9/library/exceptions.html#ValueError "(in Python v3.9)") will be raised if not).

*   **fade_out_time** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – Number of seconds to spend fading out. Defaults to 0. Must be 0 if _pwm_ was [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") when the class was constructed ([`ValueError`](https://docs.python.org/3.9/library/exceptions.html#ValueError "(in Python v3.9)") will be raised if not).

*   **on_color** ([_Color_](https://colorzero.readthedocs.io/en/latest/api_color.html#colorzero.Color "(in Colorzero v2.0)")_or_[_tuple_](https://docs.python.org/3.9/library/stdtypes.html#tuple "(in Python v3.9)")) – The color to use when the LED is “on”. Defaults to white.

*   **off_color** ([_Color_](https://colorzero.readthedocs.io/en/latest/api_color.html#colorzero.Color "(in Colorzero v2.0)")_or_[_tuple_](https://docs.python.org/3.9/library/stdtypes.html#tuple "(in Python v3.9)")) – The color to use when the LED is “off”. Defaults to black.

*   **n** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")_or_ _None_) – Number of times to blink; [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default) means forever.

*   **background** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") (the default), start a background thread to continue blinking and return immediately. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)"), only return when the blink is finished (warning: the default value of _n_ will result in this method never returning).

off()[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/output_devices.html#RGBLED.off)[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.RGBLED.off "Link to this definition")
Turn the LED off. This is equivalent to setting the LED color to black `(0, 0, 0)`.

on()[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/output_devices.html#RGBLED.on)[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.RGBLED.on "Link to this definition")
Turn the LED on. This equivalent to setting the LED color to white `(1, 1, 1)`.

pulse(_fade\_in\_time=1_, _fade\_out\_time=1_, _on\_color=(1,1,1)_, _off\_color=(0,0,0)_, _n=None_, _background=True_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/output_devices.html#RGBLED.pulse)[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.RGBLED.pulse "Link to this definition")
Make the device fade in and out repeatedly.

Parameters:
*   **fade_in_time** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – Number of seconds to spend fading in. Defaults to 1.

*   **fade_out_time** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – Number of seconds to spend fading out. Defaults to 1.

*   **on_color** ([_Color_](https://colorzero.readthedocs.io/en/latest/api_color.html#colorzero.Color "(in Colorzero v2.0)")_or_[_tuple_](https://docs.python.org/3.9/library/stdtypes.html#tuple "(in Python v3.9)")) – The color to use when the LED is “on”. Defaults to white.

*   **off_color** ([_Color_](https://colorzero.readthedocs.io/en/latest/api_color.html#colorzero.Color "(in Colorzero v2.0)")_or_[_tuple_](https://docs.python.org/3.9/library/stdtypes.html#tuple "(in Python v3.9)")) – The color to use when the LED is “off”. Defaults to black.

*   **n** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")_or_ _None_) – Number of times to pulse; [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default) means forever.

*   **background** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") (the default), start a background thread to continue pulsing and return immediately. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)"), only return when the pulse is finished (warning: the default value of _n_ will result in this method never returning).

toggle()[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/output_devices.html#RGBLED.toggle)[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.RGBLED.toggle "Link to this definition")
Toggle the state of the device. If the device is currently off ([`value`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.RGBLED.value "gpiozero.RGBLED.value") is `(0, 0, 0)`), this changes it to “fully” on ([`value`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.RGBLED.value "gpiozero.RGBLED.value") is `(1, 1, 1)`). If the device has a specific color, this method inverts the color.

_property_ blue[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.RGBLED.blue "Link to this definition")
Represents the blue element of the LED as a [`Blue`](https://colorzero.readthedocs.io/en/latest/api_color.html#colorzero.Blue "(in Colorzero v2.0)") object.

_property_ color[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.RGBLED.color "Link to this definition")
Represents the color of the LED as a [`Color`](https://colorzero.readthedocs.io/en/latest/api_color.html#colorzero.Color "(in Colorzero v2.0)") object.

_property_ green[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.RGBLED.green "Link to this definition")
Represents the green element of the LED as a [`Green`](https://colorzero.readthedocs.io/en/latest/api_color.html#colorzero.Green "(in Colorzero v2.0)") object.

_property_ is_lit[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.RGBLED.is_lit "Link to this definition")
Returns [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") if the LED is currently active (not black) and [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") otherwise.

_property_ red[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.RGBLED.red "Link to this definition")
Represents the red element of the LED as a [`Red`](https://colorzero.readthedocs.io/en/latest/api_color.html#colorzero.Red "(in Colorzero v2.0)") object.

_property_ value[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.RGBLED.value "Link to this definition")
Represents the color of the LED as an RGB 3-tuple of 
```
(red, green,
blue)
```
 where each value is between 0 and 1 if _pwm_ was [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") when the class was constructed (and only 0 or 1 if not).

For example, red would be `(1, 0, 0)` and yellow would be 
```
(1, 1,
0)
```
, while orange would be `(1, 0.5, 0)`.

### 15.1.4. Buzzer[](https://gpiozero.readthedocs.io/en/stable/api_output.html#buzzer "Link to this heading")

_class_ gpiozero.Buzzer(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/output_devices.html#Buzzer)[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Buzzer "Link to this definition")
Extends [`DigitalOutputDevice`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.DigitalOutputDevice "gpiozero.DigitalOutputDevice") and represents a digital buzzer component.

Note

This interface is only capable of simple on/off commands, and is not capable of playing a variety of tones (see [`TonalBuzzer`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.TonalBuzzer "gpiozero.TonalBuzzer")).

Connect the cathode (negative pin) of the buzzer to a ground pin; connect the other side to any GPIO pin.

The following example will sound the buzzer:

from gpiozero import Buzzer

bz = Buzzer(3)
bz.on()

Parameters:
*   **pin** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")_or_[_str_](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)")) – The GPIO pin which the buzzer is connected to. See [Pin Numbering](https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering) for valid pin numbers. If this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") a [`GPIODeviceError`](https://gpiozero.readthedocs.io/en/stable/api_exc.html#gpiozero.GPIODeviceError "gpiozero.GPIODeviceError") will be raised.

*   **active_high** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") (the default), the buzzer will operate normally with the circuit described above. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") you should wire the cathode to the GPIO pin, and the anode to a 3V3 pin.

*   **initial_value** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")_or_ _None_) – If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") (the default), the buzzer will be silent initially. If [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)"), the buzzer will be left in whatever state the pin is found in when configured for output (warning: this can be on). If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"), the buzzer will be switched on initially.

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

beep(_on\_time=1_, _off\_time=1_, _n=None_, _background=True_)[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Buzzer.beep "Link to this definition")
Make the device turn on and off repeatedly.

Parameters:
*   **on_time** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – Number of seconds on. Defaults to 1 second.

*   **off_time** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – Number of seconds off. Defaults to 1 second.

*   **n** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")_or_ _None_) – Number of times to blink; [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default) means forever.

*   **background** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") (the default), start a background thread to continue blinking and return immediately. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)"), only return when the blink is finished (warning: the default value of _n_ will result in this method never returning).

off()[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Buzzer.off "Link to this definition")
Turns the device off.

on()[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Buzzer.on "Link to this definition")
Turns the device on.

toggle()[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Buzzer.toggle "Link to this definition")
Reverse the state of the device. If it’s on, turn it off; if it’s off, turn it on.

_property_ is_active[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Buzzer.is_active "Link to this definition")
Returns [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") if the device is currently active and [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") otherwise. This property is usually derived from [`value`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Buzzer.value "gpiozero.Buzzer.value"). Unlike [`value`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Buzzer.value "gpiozero.Buzzer.value"), this is _always_ a boolean.

_property_ pin[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Buzzer.pin "Link to this definition")
The [`Pin`](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Pin "gpiozero.Pin") that the device is connected to. This will be [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") if the device has been closed (see the [`close()`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.Device.close "gpiozero.Device.close") method). When dealing with GPIO pins, query `pin.number` to discover the GPIO pin (in BCM numbering) that the device is connected to.

_property_ value[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Buzzer.value "Link to this definition")
Returns 1 if the device is currently active and 0 otherwise. Setting this property changes the state of the device.

### 15.1.5. TonalBuzzer[](https://gpiozero.readthedocs.io/en/stable/api_output.html#tonalbuzzer "Link to this heading")

_class_ gpiozero.TonalBuzzer(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/output_devices.html#TonalBuzzer)[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.TonalBuzzer "Link to this definition")
Extends [`CompositeDevice`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.CompositeDevice "gpiozero.CompositeDevice") and represents a tonal buzzer.

Parameters:
*   **pin** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")_or_[_str_](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)")) – The GPIO pin which the buzzer is connected to. See [Pin Numbering](https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering) for valid pin numbers. If this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") a [`GPIODeviceError`](https://gpiozero.readthedocs.io/en/stable/api_exc.html#gpiozero.GPIODeviceError "gpiozero.GPIODeviceError") will be raised.

*   **initial_value** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – If [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default), the buzzer will be off initially. Values between -1 and 1 can be specified as an initial value for the buzzer.

*   **mid_tone** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")_or_[_str_](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)")) – The tone which is represented the device’s middle value (0). The default is “A4” (MIDI note 69).

*   **octaves** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")) – The number of octaves to allow away from the base note. The default is 1, meaning a value of -1 goes one octave below the base note, and one above, i.e. from A3 to A5 with the default base note of A4.

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

Note

Note that this class does not currently work with [`PiGPIOFactory`](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.pins.pigpio.PiGPIOFactory "gpiozero.pins.pigpio.PiGPIOFactory").

play(_tone_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/output_devices.html#TonalBuzzer.play)[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.TonalBuzzer.play "Link to this definition")
Play the given _tone_. This can either be an instance of [`Tone`](https://gpiozero.readthedocs.io/en/stable/api_tones.html#gpiozero.tones.Tone "gpiozero.tones.Tone") or can be anything that could be used to construct an instance of [`Tone`](https://gpiozero.readthedocs.io/en/stable/api_tones.html#gpiozero.tones.Tone "gpiozero.tones.Tone").

For example:

>>> from gpiozero import TonalBuzzer
>>> from gpiozero.tones import Tone
>>> b = TonalBuzzer(17)
>>> b.play(Tone("A4"))
>>> b.play(Tone(220.0)) # Hz
>>> b.play(Tone(60)) # middle C in MIDI notation
>>> b.play("A4")
>>> b.play(220.0)
>>> b.play(60)

stop()[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/output_devices.html#TonalBuzzer.stop)[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.TonalBuzzer.stop "Link to this definition")
Turn the buzzer off. This is equivalent to setting [`value`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.TonalBuzzer.value "gpiozero.TonalBuzzer.value") to [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)").

_property_ is_active[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.TonalBuzzer.is_active "Link to this definition")
Returns [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") if the buzzer is currently playing, otherwise [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)").

_property_ max_tone[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.TonalBuzzer.max_tone "Link to this definition")
The highest tone that the buzzer can play, i.e. the tone played when [`value`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.TonalBuzzer.value "gpiozero.TonalBuzzer.value") is 1.

_property_ mid_tone[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.TonalBuzzer.mid_tone "Link to this definition")
The middle tone available, i.e. the tone played when [`value`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.TonalBuzzer.value "gpiozero.TonalBuzzer.value") is 0.

_property_ min_tone[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.TonalBuzzer.min_tone "Link to this definition")
The lowest tone that the buzzer can play, i.e. the tone played when [`value`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.TonalBuzzer.value "gpiozero.TonalBuzzer.value") is -1.

_property_ octaves[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.TonalBuzzer.octaves "Link to this definition")
The number of octaves available (above and below mid_tone).

_property_ tone[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.TonalBuzzer.tone "Link to this definition")
Returns the [`Tone`](https://gpiozero.readthedocs.io/en/stable/api_tones.html#gpiozero.tones.Tone "gpiozero.tones.Tone") that the buzzer is currently playing, or [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") if the buzzer is silent. This property can also be set to play the specified tone.

_property_ value[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.TonalBuzzer.value "Link to this definition")
Represents the state of the buzzer as a value between -1 (representing the minimum tone) and 1 (representing the maximum tone). This can also be the special value [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") indicating that the buzzer is currently silent.

### 15.1.6. Motor[](https://gpiozero.readthedocs.io/en/stable/api_output.html#motor "Link to this heading")

_class_ gpiozero.Motor(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/output_devices.html#Motor)[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Motor "Link to this definition")
Extends [`CompositeDevice`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.CompositeDevice "gpiozero.CompositeDevice") and represents a generic motor connected to a bi-directional motor driver circuit (i.e. an [H-bridge](https://en.wikipedia.org/wiki/H_bridge)).

Attach an [H-bridge](https://en.wikipedia.org/wiki/H_bridge) motor controller to your Pi; connect a power source (e.g. a battery pack or the 5V pin) to the controller; connect the outputs of the controller board to the two terminals of the motor; connect the inputs of the controller board to two GPIO pins.

The following code will make the motor turn “forwards”:

from gpiozero import Motor

motor = Motor(17, 18)
motor.forward()

Parameters:
*   **forward** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")_or_[_str_](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)")) – The GPIO pin that the forward input of the motor driver chip is connected to. See [Pin Numbering](https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering) for valid pin numbers. If this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") a [`GPIODeviceError`](https://gpiozero.readthedocs.io/en/stable/api_exc.html#gpiozero.GPIODeviceError "gpiozero.GPIODeviceError") will be raised.

*   **backward** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")_or_[_str_](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)")) – The GPIO pin that the backward input of the motor driver chip is connected to. See [Pin Numbering](https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering) for valid pin numbers. If this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") a [`GPIODeviceError`](https://gpiozero.readthedocs.io/en/stable/api_exc.html#gpiozero.GPIODeviceError "gpiozero.GPIODeviceError") will be raised.

*   **enable** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")_or_[_str_](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)")_or_ _None_) – The GPIO pin that enables the motor. Required for _some_ motor controller boards. See [Pin Numbering](https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering) for valid pin numbers.

*   **pwm** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") (the default), construct [`PWMOutputDevice`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMOutputDevice "gpiozero.PWMOutputDevice") instances for the motor controller pins, allowing both direction and variable speed control. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)"), construct [`DigitalOutputDevice`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.DigitalOutputDevice "gpiozero.DigitalOutputDevice") instances, allowing only direction control.

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

backward(_speed=1_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/output_devices.html#Motor.backward)[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Motor.backward "Link to this definition")
Drive the motor backwards.

Parameters:
**speed** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – The speed at which the motor should turn. Can be any value between 0 (stopped) and the default 1 (maximum speed) if _pwm_ was [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") when the class was constructed (and only 0 or 1 if not).

forward(_speed=1_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/output_devices.html#Motor.forward)[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Motor.forward "Link to this definition")
Drive the motor forwards.

Parameters:
**speed** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – The speed at which the motor should turn. Can be any value between 0 (stopped) and the default 1 (maximum speed) if _pwm_ was [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") when the class was constructed (and only 0 or 1 if not).

reverse()[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/output_devices.html#Motor.reverse)[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Motor.reverse "Link to this definition")
Reverse the current direction of the motor. If the motor is currently idle this does nothing. Otherwise, the motor’s direction will be reversed at the current speed.

stop()[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/output_devices.html#Motor.stop)[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Motor.stop "Link to this definition")
Stop the motor.

_property_ is_active[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Motor.is_active "Link to this definition")
Returns [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") if the motor is currently running and [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") otherwise.

_property_ value[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Motor.value "Link to this definition")
Represents the speed of the motor as a floating point value between -1 (full speed backward) and 1 (full speed forward), with 0 representing stopped.

### 15.1.7. PhaseEnableMotor[](https://gpiozero.readthedocs.io/en/stable/api_output.html#phaseenablemotor "Link to this heading")

_class_ gpiozero.PhaseEnableMotor(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/output_devices.html#PhaseEnableMotor)[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PhaseEnableMotor "Link to this definition")
Extends [`CompositeDevice`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.CompositeDevice "gpiozero.CompositeDevice") and represents a generic motor connected to a Phase/Enable motor driver circuit; the phase of the driver controls whether the motor turns forwards or backwards, while enable controls the speed with PWM.

The following code will make the motor turn “forwards”:

from gpiozero import PhaseEnableMotor
motor = PhaseEnableMotor(12, 5)
motor.forward()

Parameters:
*   **phase** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")_or_[_str_](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)")) – The GPIO pin that the phase (direction) input of the motor driver chip is connected to. See [Pin Numbering](https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering) for valid pin numbers. If this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") a [`GPIODeviceError`](https://gpiozero.readthedocs.io/en/stable/api_exc.html#gpiozero.GPIODeviceError "gpiozero.GPIODeviceError") will be raised.

*   **enable** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")_or_[_str_](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)")) – The GPIO pin that the enable (speed) input of the motor driver chip is connected to. See [Pin Numbering](https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering) for valid pin numbers. If this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") a [`GPIODeviceError`](https://gpiozero.readthedocs.io/en/stable/api_exc.html#gpiozero.GPIODeviceError "gpiozero.GPIODeviceError") will be raised.

*   **pwm** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") (the default), construct [`PWMOutputDevice`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMOutputDevice "gpiozero.PWMOutputDevice") instances for the motor controller pins, allowing both direction and variable speed control. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)"), construct [`DigitalOutputDevice`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.DigitalOutputDevice "gpiozero.DigitalOutputDevice") instances, allowing only direction control.

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

backward(_speed=1_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/output_devices.html#PhaseEnableMotor.backward)[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PhaseEnableMotor.backward "Link to this definition")
Drive the motor backwards.

Parameters:
**speed** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – The speed at which the motor should turn. Can be any value between 0 (stopped) and the default 1 (maximum speed).

forward(_speed=1_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/output_devices.html#PhaseEnableMotor.forward)[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PhaseEnableMotor.forward "Link to this definition")
Drive the motor forwards.

Parameters:
**speed** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – The speed at which the motor should turn. Can be any value between 0 (stopped) and the default 1 (maximum speed).

reverse()[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/output_devices.html#PhaseEnableMotor.reverse)[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PhaseEnableMotor.reverse "Link to this definition")
Reverse the current direction of the motor. If the motor is currently idle this does nothing. Otherwise, the motor’s direction will be reversed at the current speed.

stop()[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/output_devices.html#PhaseEnableMotor.stop)[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PhaseEnableMotor.stop "Link to this definition")
Stop the motor.

_property_ is_active[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PhaseEnableMotor.is_active "Link to this definition")
Returns [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") if the motor is currently running and [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") otherwise.

_property_ value[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PhaseEnableMotor.value "Link to this definition")
Represents the speed of the motor as a floating point value between -1 (full speed backward) and 1 (full speed forward).

### 15.1.8. Servo[](https://gpiozero.readthedocs.io/en/stable/api_output.html#servo "Link to this heading")

_class_ gpiozero.Servo(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/output_devices.html#Servo)[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Servo "Link to this definition")
Extends [`CompositeDevice`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.CompositeDevice "gpiozero.CompositeDevice") and represents a PWM-controlled servo motor connected to a GPIO pin.

Connect a power source (e.g. a battery pack or the 5V pin) to the power cable of the servo (this is typically colored red); connect the ground cable of the servo (typically colored black or brown) to the negative of your battery pack, or a GND pin; connect the final cable (typically colored white or orange) to the GPIO pin you wish to use for controlling the servo.

The following code will make the servo move between its minimum, maximum, and mid-point positions with a pause between each:

from gpiozero import Servo
from time import sleep

servo = Servo(17)

while True:
    servo.min()
    sleep(1)
    servo.mid()
    sleep(1)
    servo.max()
    sleep(1)

You can also use the [`value`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Servo.value "gpiozero.Servo.value") property to move the servo to a particular position, on a scale from -1 (min) to 1 (max) where 0 is the mid-point:

from gpiozero import Servo

servo = Servo(17)

servo.value = 0.5

Note

To reduce servo jitter, use the pigpio pin driver rather than the default RPi.GPIO driver (pigpio uses DMA sampling for much more precise edge timing). See [Changing the pin factory](https://gpiozero.readthedocs.io/en/stable/api_pins.html#changing-pin-factory) for further information.

Parameters:
*   **pin** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")_or_[_str_](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)")) – The GPIO pin that the servo is connected to. See [Pin Numbering](https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering) for valid pin numbers. If this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") a [`GPIODeviceError`](https://gpiozero.readthedocs.io/en/stable/api_exc.html#gpiozero.GPIODeviceError "gpiozero.GPIODeviceError") will be raised.

*   **initial_value** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – If `0` (the default), the device’s mid-point will be set initially. Other values between -1 and +1 can be specified as an initial position. [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") means to start the servo un-controlled (see [`value`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Servo.value "gpiozero.Servo.value")).

*   **min_pulse_width** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – The pulse width corresponding to the servo’s minimum position. This defaults to 1ms.

*   **max_pulse_width** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – The pulse width corresponding to the servo’s maximum position. This defaults to 2ms.

*   **frame_width** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – The length of time between servo control pulses measured in seconds. This defaults to 20ms which is a common value for servos.

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

detach()[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/output_devices.html#Servo.detach)[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Servo.detach "Link to this definition")
Temporarily disable control of the servo. This is equivalent to setting [`value`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Servo.value "gpiozero.Servo.value") to [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)").

max()[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/output_devices.html#Servo.max)[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Servo.max "Link to this definition")
Set the servo to its maximum position.

mid()[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/output_devices.html#Servo.mid)[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Servo.mid "Link to this definition")
Set the servo to its mid-point position.

min()[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/output_devices.html#Servo.min)[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Servo.min "Link to this definition")
Set the servo to its minimum position.

_property_ frame_width[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Servo.frame_width "Link to this definition")
The time between control pulses, measured in seconds.

_property_ is_active[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Servo.is_active "Link to this definition")
Composite devices are considered “active” if any of their constituent devices have a “truthy” value.

_property_ max_pulse_width[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Servo.max_pulse_width "Link to this definition")
The control pulse width corresponding to the servo’s maximum position, measured in seconds.

_property_ min_pulse_width[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Servo.min_pulse_width "Link to this definition")
The control pulse width corresponding to the servo’s minimum position, measured in seconds.

_property_ pulse_width[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Servo.pulse_width "Link to this definition")
Returns the current pulse width controlling the servo.

_property_ value[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Servo.value "Link to this definition")
Represents the position of the servo as a value between -1 (the minimum position) and +1 (the maximum position). This can also be the special value [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") indicating that the servo is currently “uncontrolled”, i.e. that no control signal is being sent. Typically this means the servo’s position remains unchanged, but that it can be moved by hand.

### 15.1.9. AngularServo[](https://gpiozero.readthedocs.io/en/stable/api_output.html#angularservo "Link to this heading")

_class_ gpiozero.AngularServo(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/output_devices.html#AngularServo)[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.AngularServo "Link to this definition")
Extends [`Servo`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Servo "gpiozero.Servo") and represents a rotational PWM-controlled servo motor which can be set to particular angles (assuming valid minimum and maximum angles are provided to the constructor).

Connect a power source (e.g. a battery pack or the 5V pin) to the power cable of the servo (this is typically colored red); connect the ground cable of the servo (typically colored black or brown) to the negative of your battery pack, or a GND pin; connect the final cable (typically colored white or orange) to the GPIO pin you wish to use for controlling the servo.

Next, calibrate the angles that the servo can rotate to. In an interactive Python session, construct a [`Servo`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Servo "gpiozero.Servo") instance. The servo should move to its mid-point by default. Set the servo to its minimum value, and measure the angle from the mid-point. Set the servo to its maximum value, and again measure the angle:

>>> from gpiozero import Servo
>>> s = Servo(17)
>>> s.min() # measure the angle
>>> s.max() # measure the angle

You should now be able to construct an [`AngularServo`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.AngularServo "gpiozero.AngularServo") instance with the correct bounds:

>>> from gpiozero import AngularServo
>>> s = AngularServo(17, min_angle=-42, max_angle=44)
>>> s.angle = 0.0
>>> s.angle
0.0
>>> s.angle = 15
>>> s.angle
15.0

Note

You can set _min\_angle_ greater than _max\_angle_ if you wish to reverse the sense of the angles (e.g. `min_angle=45, max_angle=-45`). This can be useful with servos that rotate in the opposite direction to your expectations of minimum and maximum.

Parameters:
*   **pin** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")_or_[_str_](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)")) – The GPIO pin that the servo is connected to. See [Pin Numbering](https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering) for valid pin numbers. If this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") a [`GPIODeviceError`](https://gpiozero.readthedocs.io/en/stable/api_exc.html#gpiozero.GPIODeviceError "gpiozero.GPIODeviceError") will be raised.

*   **initial_angle** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – Sets the servo’s initial angle to the specified value. The default is 0. The value specified must be between _min\_angle_ and _max\_angle_ inclusive. [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") means to start the servo un-controlled (see [`value`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.AngularServo.value "gpiozero.AngularServo.value")).

*   **min_angle** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – Sets the minimum angle that the servo can rotate to. This defaults to -90, but should be set to whatever you measure from your servo during calibration.

*   **max_angle** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – Sets the maximum angle that the servo can rotate to. This defaults to 90, but should be set to whatever you measure from your servo during calibration.

*   **min_pulse_width** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – The pulse width corresponding to the servo’s minimum position. This defaults to 1ms.

*   **max_pulse_width** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – The pulse width corresponding to the servo’s maximum position. This defaults to 2ms.

*   **frame_width** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – The length of time between servo control pulses measured in seconds. This defaults to 20ms which is a common value for servos.

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

max()[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.AngularServo.max "Link to this definition")
Set the servo to its maximum position.

mid()[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.AngularServo.mid "Link to this definition")
Set the servo to its mid-point position.

min()[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.AngularServo.min "Link to this definition")
Set the servo to its minimum position.

_property_ angle[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.AngularServo.angle "Link to this definition")
The position of the servo as an angle measured in degrees. This will only be accurate if [`min_angle`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.AngularServo.min_angle "gpiozero.AngularServo.min_angle") and [`max_angle`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.AngularServo.max_angle "gpiozero.AngularServo.max_angle") have been set appropriately in the constructor.

This can also be the special value [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") indicating that the servo is currently “uncontrolled”, i.e. that no control signal is being sent. Typically this means the servo’s position remains unchanged, but that it can be moved by hand.

_property_ is_active[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.AngularServo.is_active "Link to this definition")
Composite devices are considered “active” if any of their constituent devices have a “truthy” value.

_property_ max_angle[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.AngularServo.max_angle "Link to this definition")
The maximum angle that the servo will rotate to when [`max()`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.AngularServo.max "gpiozero.AngularServo.max") is called.

_property_ min_angle[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.AngularServo.min_angle "Link to this definition")
The minimum angle that the servo will rotate to when [`min()`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.AngularServo.min "gpiozero.AngularServo.min") is called.

_property_ value[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.AngularServo.value "Link to this definition")
Represents the position of the servo as a value between -1 (the minimum position) and +1 (the maximum position). This can also be the special value [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") indicating that the servo is currently “uncontrolled”, i.e. that no control signal is being sent. Typically this means the servo’s position remains unchanged, but that it can be moved by hand.

15.2. Base Classes[](https://gpiozero.readthedocs.io/en/stable/api_output.html#base-classes "Link to this heading")
--------------------------------------------------------------------------------------------------------------------

The classes in the sections above are derived from a series of base classes, some of which are effectively abstract. The classes form the (partial) hierarchy displayed in the graph below (abstract classes are shaded lighter than concrete classes):

![Image 1: _images/output_device_hierarchy.svg](https://gpiozero.readthedocs.io/en/stable/_images/output_device_hierarchy.svg)
The following sections document these base classes for advanced users that wish to construct classes for their own devices.

### 15.2.1. DigitalOutputDevice[](https://gpiozero.readthedocs.io/en/stable/api_output.html#digitaloutputdevice "Link to this heading")

_class_ gpiozero.DigitalOutputDevice(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/output_devices.html#DigitalOutputDevice)[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.DigitalOutputDevice "Link to this definition")
Represents a generic output device with typical on/off behaviour.

This class extends [`OutputDevice`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.OutputDevice "gpiozero.OutputDevice") with a [`blink()`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.DigitalOutputDevice.blink "gpiozero.DigitalOutputDevice.blink") method which uses an optional background thread to handle toggling the device state without further interaction.

Parameters:
*   **pin** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")_or_[_str_](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)")) – The GPIO pin that the device is connected to. See [Pin Numbering](https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering) for valid pin numbers. If this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") a [`GPIODeviceError`](https://gpiozero.readthedocs.io/en/stable/api_exc.html#gpiozero.GPIODeviceError "gpiozero.GPIODeviceError") will be raised.

*   **active_high** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") (the default), the [`on()`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.DigitalOutputDevice.on "gpiozero.DigitalOutputDevice.on") method will set the GPIO to HIGH. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)"), the [`on()`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.DigitalOutputDevice.on "gpiozero.DigitalOutputDevice.on") method will set the GPIO to LOW (the [`off()`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.DigitalOutputDevice.off "gpiozero.DigitalOutputDevice.off") method always does the opposite).

*   **initial_value** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")_or_ _None_) – If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") (the default), the device will be off initially. If [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)"), the device will be left in whatever state the pin is found in when configured for output (warning: this can be on). If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"), the device will be switched on initially.

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

blink(_on\_time=1_, _off\_time=1_, _n=None_, _background=True_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/output_devices.html#DigitalOutputDevice.blink)[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.DigitalOutputDevice.blink "Link to this definition")
Make the device turn on and off repeatedly.

Parameters:
*   **on_time** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – Number of seconds on. Defaults to 1 second.

*   **off_time** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – Number of seconds off. Defaults to 1 second.

*   **n** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")_or_ _None_) – Number of times to blink; [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default) means forever.

*   **background** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") (the default), start a background thread to continue blinking and return immediately. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)"), only return when the blink is finished (warning: the default value of _n_ will result in this method never returning).

off()[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/output_devices.html#DigitalOutputDevice.off)[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.DigitalOutputDevice.off "Link to this definition")
Turns the device off.

on()[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/output_devices.html#DigitalOutputDevice.on)[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.DigitalOutputDevice.on "Link to this definition")
Turns the device on.

_property_ value[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.DigitalOutputDevice.value "Link to this definition")
Returns 1 if the device is currently active and 0 otherwise. Setting this property changes the state of the device.

### 15.2.2. PWMOutputDevice[](https://gpiozero.readthedocs.io/en/stable/api_output.html#pwmoutputdevice "Link to this heading")

_class_ gpiozero.PWMOutputDevice(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/output_devices.html#PWMOutputDevice)[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMOutputDevice "Link to this definition")
Generic output device configured for pulse-width modulation (PWM).

Parameters:
*   **pin** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")_or_[_str_](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)")) – The GPIO pin that the device is connected to. See [Pin Numbering](https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering) for valid pin numbers. If this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") a [`GPIODeviceError`](https://gpiozero.readthedocs.io/en/stable/api_exc.html#gpiozero.GPIODeviceError "gpiozero.GPIODeviceError") will be raised.

*   **active_high** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") (the default), the [`on()`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMOutputDevice.on "gpiozero.PWMOutputDevice.on") method will set the GPIO to HIGH. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)"), the [`on()`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMOutputDevice.on "gpiozero.PWMOutputDevice.on") method will set the GPIO to LOW (the [`off()`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMOutputDevice.off "gpiozero.PWMOutputDevice.off") method always does the opposite).

*   **initial_value** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – If 0 (the default), the device’s duty cycle will be 0 initially. Other values between 0 and 1 can be specified as an initial duty cycle. Note that [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") cannot be specified (unlike the parent class) as there is no way to tell PWM not to alter the state of the pin.

*   **frequency** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")) – The frequency (in Hz) of pulses emitted to drive the device. Defaults to 100Hz.

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

blink(_on\_time=1_, _off\_time=1_, _fade\_in\_time=0_, _fade\_out\_time=0_, _n=None_, _background=True_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/output_devices.html#PWMOutputDevice.blink)[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMOutputDevice.blink "Link to this definition")
Make the device turn on and off repeatedly.

Parameters:
*   **on_time** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – Number of seconds on. Defaults to 1 second.

*   **off_time** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – Number of seconds off. Defaults to 1 second.

*   **fade_in_time** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – Number of seconds to spend fading in. Defaults to 0.

*   **fade_out_time** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – Number of seconds to spend fading out. Defaults to 0.

*   **n** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")_or_ _None_) – Number of times to blink; [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default) means forever.

*   **background** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") (the default), start a background thread to continue blinking and return immediately. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)"), only return when the blink is finished (warning: the default value of _n_ will result in this method never returning).

off()[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/output_devices.html#PWMOutputDevice.off)[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMOutputDevice.off "Link to this definition")
Turns the device off.

on()[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/output_devices.html#PWMOutputDevice.on)[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMOutputDevice.on "Link to this definition")
Turns the device on.

pulse(_fade\_in\_time=1_, _fade\_out\_time=1_, _n=None_, _background=True_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/output_devices.html#PWMOutputDevice.pulse)[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMOutputDevice.pulse "Link to this definition")
Make the device fade in and out repeatedly.

Parameters:
*   **fade_in_time** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – Number of seconds to spend fading in. Defaults to 1.

*   **fade_out_time** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – Number of seconds to spend fading out. Defaults to 1.

*   **n** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")_or_ _None_) – Number of times to pulse; [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default) means forever.

*   **background** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") (the default), start a background thread to continue pulsing and return immediately. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)"), only return when the pulse is finished (warning: the default value of _n_ will result in this method never returning).

toggle()[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/output_devices.html#PWMOutputDevice.toggle)[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMOutputDevice.toggle "Link to this definition")
Toggle the state of the device. If the device is currently off ([`value`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMOutputDevice.value "gpiozero.PWMOutputDevice.value") is 0.0), this changes it to “fully” on ([`value`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMOutputDevice.value "gpiozero.PWMOutputDevice.value") is 1.0). If the device has a duty cycle ([`value`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMOutputDevice.value "gpiozero.PWMOutputDevice.value")) of 0.1, this will toggle it to 0.9, and so on.

_property_ frequency[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMOutputDevice.frequency "Link to this definition")
The frequency of the pulses used with the PWM device, in Hz. The default is 100Hz.

_property_ is_active[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMOutputDevice.is_active "Link to this definition")
Returns [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") if the device is currently active ([`value`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMOutputDevice.value "gpiozero.PWMOutputDevice.value") is non-zero) and [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") otherwise.

_property_ value[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMOutputDevice.value "Link to this definition")
The duty cycle of the PWM device. 0.0 is off, 1.0 is fully on. Values in between may be specified for varying levels of power in the device.

### 15.2.3. OutputDevice[](https://gpiozero.readthedocs.io/en/stable/api_output.html#outputdevice "Link to this heading")

_class_ gpiozero.OutputDevice(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/output_devices.html#OutputDevice)[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.OutputDevice "Link to this definition")
Represents a generic GPIO output device.

This class extends [`GPIODevice`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.GPIODevice "gpiozero.GPIODevice") to add facilities common to GPIO output devices: an [`on()`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.OutputDevice.on "gpiozero.OutputDevice.on") method to switch the device on, a corresponding [`off()`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.OutputDevice.off "gpiozero.OutputDevice.off") method, and a [`toggle()`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.OutputDevice.toggle "gpiozero.OutputDevice.toggle") method.

Parameters:
*   **pin** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")_or_[_str_](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)")) – The GPIO pin that the device is connected to. See [Pin Numbering](https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering) for valid pin numbers. If this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") a [`GPIODeviceError`](https://gpiozero.readthedocs.io/en/stable/api_exc.html#gpiozero.GPIODeviceError "gpiozero.GPIODeviceError") will be raised.

*   **active_high** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") (the default), the [`on()`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.OutputDevice.on "gpiozero.OutputDevice.on") method will set the GPIO to HIGH. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)"), the [`on()`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.OutputDevice.on "gpiozero.OutputDevice.on") method will set the GPIO to LOW (the [`off()`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.OutputDevice.off "gpiozero.OutputDevice.off") method always does the opposite).

*   **initial_value** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")_or_ _None_) – If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") (the default), the device will be off initially. If [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)"), the device will be left in whatever state the pin is found in when configured for output (warning: this can be on). If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"), the device will be switched on initially.

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

off()[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/output_devices.html#OutputDevice.off)[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.OutputDevice.off "Link to this definition")
Turns the device off.

on()[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/output_devices.html#OutputDevice.on)[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.OutputDevice.on "Link to this definition")
Turns the device on.

toggle()[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/output_devices.html#OutputDevice.toggle)[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.OutputDevice.toggle "Link to this definition")
Reverse the state of the device. If it’s on, turn it off; if it’s off, turn it on.

_property_ active_high[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.OutputDevice.active_high "Link to this definition")
When [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"), the [`value`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.OutputDevice.value "gpiozero.OutputDevice.value") property is [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") when the device’s [`pin`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.GPIODevice.pin "gpiozero.GPIODevice.pin") is high. When [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") the [`value`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.OutputDevice.value "gpiozero.OutputDevice.value") property is [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") when the device’s pin is low (i.e. the value is inverted).

This property can be set after construction; be warned that changing it will invert [`value`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.OutputDevice.value "gpiozero.OutputDevice.value") (i.e. changing this property doesn’t change the device’s pin state - it just changes how that state is interpreted).

_property_ value[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.OutputDevice.value "Link to this definition")
Returns 1 if the device is currently active and 0 otherwise. Setting this property changes the state of the device.

### 15.2.4. GPIODevice[](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiodevice "Link to this heading")

_class_ gpiozero.GPIODevice(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/devices.html#GPIODevice)
Extends [`Device`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.Device "gpiozero.Device"). Represents a generic GPIO device and provides the services common to all single-pin GPIO devices (like ensuring two GPIO devices do no share a [`pin`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.GPIODevice.pin "gpiozero.GPIODevice.pin")).

Parameters:
**pin** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")_or_[_str_](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)")) – The GPIO pin that the device is connected to. See [Pin Numbering](https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering) for valid pin numbers. If this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") a [`GPIODeviceError`](https://gpiozero.readthedocs.io/en/stable/api_exc.html#gpiozero.GPIODeviceError "gpiozero.GPIODeviceError") will be raised. If the pin is already in use by another device, [`GPIOPinInUse`](https://gpiozero.readthedocs.io/en/stable/api_exc.html#gpiozero.GPIOPinInUse "gpiozero.GPIOPinInUse") will be raised.

close()[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/devices.html#GPIODevice.close)
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

_property_ closed
Returns [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") if the device is closed (see the [`close()`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.GPIODevice.close "gpiozero.GPIODevice.close") method). Once a device is closed you can no longer use any other methods or properties to control or query the device.

_property_ pin
The [`Pin`](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Pin "gpiozero.Pin") that the device is connected to. This will be [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") if the device has been closed (see the [`close()`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.Device.close "gpiozero.Device.close") method). When dealing with GPIO pins, query `pin.number` to discover the GPIO pin (in BCM numbering) that the device is connected to.

_property_ value
Returns a value representing the device’s state. Frequently, this is a boolean value, or a number between 0 and 1 but some devices use larger ranges (e.g. -1 to +1) and composite devices usually use tuples to return the states of all their subordinate components.
