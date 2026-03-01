# Source: https://gpiozero.readthedocs.io/en/stable/api_tools.html

Title: Device Source Tools — gpiozero 2.0.1 Documentation

URL Source: https://gpiozero.readthedocs.io/en/stable/api_tools.html

Published Time: Thu, 15 Feb 2024 22:39:20 GMT

Markdown Content:
GPIO Zero includes several utility routines which are intended to be used with the [Source/Values](https://gpiozero.readthedocs.io/en/stable/source_values.html) attributes common to most devices in the library. These utility routines are in the `tools` module of GPIO Zero and are typically imported as follows:

from gpiozero.tools import scaled, negated, all_values

Given that [`source`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.SourceMixin.source "gpiozero.SourceMixin.source") and [`values`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.ValuesMixin.values "gpiozero.ValuesMixin.values") deal with infinite iterators, another excellent source of utilities is the [`itertools`](https://docs.python.org/3.9/library/itertools.html#module-itertools "(in Python v3.9)") module in the standard library.

20.1. Single source conversions[](https://gpiozero.readthedocs.io/en/stable/api_tools.html#single-source-conversions "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------

gpiozero.tools.absoluted(_values_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/tools.html#absoluted)[](https://gpiozero.readthedocs.io/en/stable/api_tools.html#gpiozero.tools.absoluted "Link to this definition")
Returns _values_ with all negative elements negated (so that they’re positive). For example:

from gpiozero import PWMLED, Motor, MCP3008
from gpiozero.tools import absoluted, scaled
from signal import pause

led = PWMLED(4)
motor = Motor(22, 27)
pot = MCP3008(channel=0)

motor.source = scaled(pot, -1, 1)
led.source = absoluted(motor)

pause()

gpiozero.tools.booleanized(_values_, _min\_value_, _max\_value_, _hysteresis=0_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/tools.html#booleanized)[](https://gpiozero.readthedocs.io/en/stable/api_tools.html#gpiozero.tools.booleanized "Link to this definition")
Returns True for each item in _values_ between _min\_value_ and _max\_value_, and False otherwise. _hysteresis_ can optionally be used to add [hysteresis](https://en.wikipedia.org/wiki/Hysteresis) which prevents the output value rapidly flipping when the input value is fluctuating near the _min\_value_ or _max\_value_ thresholds. For example, to light an LED only when a potentiometer is between ¼ and ¾ of its full range:

from gpiozero import LED, MCP3008
from gpiozero.tools import booleanized
from signal import pause

led = LED(4)
pot = MCP3008(channel=0)

led.source = booleanized(pot, 0.25, 0.75)

pause()

gpiozero.tools.clamped(_values_, _output\_min=0_, _output\_max=1_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/tools.html#clamped)[](https://gpiozero.readthedocs.io/en/stable/api_tools.html#gpiozero.tools.clamped "Link to this definition")
Returns _values_ clamped from _output\_min_ to _output\_max_, i.e. any items less than _output\_min_ will be returned as _output\_min_ and any items larger than _output\_max_ will be returned as _output\_max_ (these default to 0 and 1 respectively). For example:

from gpiozero import PWMLED, MCP3008
from gpiozero.tools import clamped
from signal import pause

led = PWMLED(4)
pot = MCP3008(channel=0)

led.source = clamped(pot, 0.5, 1.0)

pause()

gpiozero.tools.inverted(_values_, _input\_min=0_, _input\_max=1_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/tools.html#inverted)[](https://gpiozero.readthedocs.io/en/stable/api_tools.html#gpiozero.tools.inverted "Link to this definition")
Returns the inversion of the supplied values (_input\_min_ becomes _input\_max_, _input\_max_ becomes _input\_min_, input_min + 0.1 becomes input_max - 0.1, etc.). All items in _values_ are assumed to be between _input\_min_ and _input\_max_ (which default to 0 and 1 respectively), and the output will be in the same range. For example:

from gpiozero import MCP3008, PWMLED
from gpiozero.tools import inverted
from signal import pause

led = PWMLED(4)
pot = MCP3008(channel=0)

led.source = inverted(pot)

pause()

gpiozero.tools.negated(_values_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/tools.html#negated)[](https://gpiozero.readthedocs.io/en/stable/api_tools.html#gpiozero.tools.negated "Link to this definition")
Returns the negation of the supplied values ([`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") becomes [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)"), and [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") becomes [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)")). For example:

from gpiozero import Button, LED
from gpiozero.tools import negated
from signal import pause

led = LED(4)
btn = Button(17)

led.source = negated(btn)

pause()

gpiozero.tools.post_delayed(_values_, _delay_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/tools.html#post_delayed)[](https://gpiozero.readthedocs.io/en/stable/api_tools.html#gpiozero.tools.post_delayed "Link to this definition")
Waits for _delay_ seconds after returning each item from _values_.

gpiozero.tools.post_periodic_filtered(_values_, _repeat\_after_, _block_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/tools.html#post_periodic_filtered)[](https://gpiozero.readthedocs.io/en/stable/api_tools.html#gpiozero.tools.post_periodic_filtered "Link to this definition")
After every _repeat\_after_ items, blocks the next _block_ items from _values_. Note that unlike [`pre_periodic_filtered()`](https://gpiozero.readthedocs.io/en/stable/api_tools.html#gpiozero.tools.pre_periodic_filtered "gpiozero.tools.pre_periodic_filtered"), _repeat\_after_ can’t be 0. For example, to block every tenth item read from an ADC:

from gpiozero import MCP3008
from gpiozero.tools import post_periodic_filtered

adc = MCP3008(channel=0)

for value in post_periodic_filtered(adc, 9, 1):
    print(value)

gpiozero.tools.pre_delayed(_values_, _delay_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/tools.html#pre_delayed)[](https://gpiozero.readthedocs.io/en/stable/api_tools.html#gpiozero.tools.pre_delayed "Link to this definition")
Waits for _delay_ seconds before returning each item from _values_.

gpiozero.tools.pre_periodic_filtered(_values_, _block_, _repeat\_after_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/tools.html#pre_periodic_filtered)[](https://gpiozero.readthedocs.io/en/stable/api_tools.html#gpiozero.tools.pre_periodic_filtered "Link to this definition")
Blocks the first _block_ items from _values_, repeating the block after every _repeat\_after_ items, if _repeat\_after_ is non-zero. For example, to discard the first 50 values read from an ADC:

from gpiozero import MCP3008
from gpiozero.tools import pre_periodic_filtered

adc = MCP3008(channel=0)

for value in pre_periodic_filtered(adc, 50, 0):
    print(value)

Or to only display every even item read from an ADC:

from gpiozero import MCP3008
from gpiozero.tools import pre_periodic_filtered

adc = MCP3008(channel=0)

for value in pre_periodic_filtered(adc, 1, 1):
    print(value)

gpiozero.tools.quantized(_values_, _steps_, _input\_min=0_, _input\_max=1_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/tools.html#quantized)[](https://gpiozero.readthedocs.io/en/stable/api_tools.html#gpiozero.tools.quantized "Link to this definition")
Returns _values_ quantized to _steps_ increments. All items in _values_ are assumed to be between _input\_min_ and _input\_max_ (which default to 0 and 1 respectively), and the output will be in the same range.

For example, to quantize values between 0 and 1 to 5 “steps” (0.0, 0.25, 0.5, 0.75, 1.0):

from gpiozero import PWMLED, MCP3008
from gpiozero.tools import quantized
from signal import pause

led = PWMLED(4)
pot = MCP3008(channel=0)

led.source = quantized(pot, 4)

pause()

gpiozero.tools.queued(_values_, _qsize_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/tools.html#queued)[](https://gpiozero.readthedocs.io/en/stable/api_tools.html#gpiozero.tools.queued "Link to this definition")
Queues up readings from _values_ (the number of readings queued is determined by _qsize_) and begins yielding values only when the queue is full. For example, to “cascade” values along a sequence of LEDs:

from gpiozero import LEDBoard, Button
from gpiozero.tools import queued
from signal import pause

leds = LEDBoard(5, 6, 13, 19, 26)
btn = Button(17)

for i in range(4):
    leds[i].source = queued(leds[i + 1], 5)
    leds[i].source_delay = 0.01

leds[4].source = btn

pause()

gpiozero.tools.smoothed(_values_, _qsize_, _average=<function mean>_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/tools.html#smoothed)[](https://gpiozero.readthedocs.io/en/stable/api_tools.html#gpiozero.tools.smoothed "Link to this definition")
Queues up readings from _values_ (the number of readings queued is determined by _qsize_) and begins yielding the _average_ of the last _qsize_ values when the queue is full. The larger the _qsize_, the more the values are smoothed. For example, to smooth the analog values read from an ADC:

from gpiozero import MCP3008
from gpiozero.tools import smoothed

adc = MCP3008(channel=0)

for value in smoothed(adc, 5):
    print(value)

gpiozero.tools.scaled(_values_, _output\_min_, _output\_max_, _input\_min=0_, _input\_max=1_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/tools.html#scaled)[](https://gpiozero.readthedocs.io/en/stable/api_tools.html#gpiozero.tools.scaled "Link to this definition")
Returns _values_ scaled from _output\_min_ to _output\_max_, assuming that all items in _values_ lie between _input\_min_ and _input\_max_ (which default to 0 and 1 respectively). For example, to control the direction of a motor (which is represented as a value between -1 and 1) using a potentiometer (which typically provides values between 0 and 1):

from gpiozero import Motor, MCP3008
from gpiozero.tools import scaled
from signal import pause

motor = Motor(20, 21)
pot = MCP3008(channel=0)

motor.source = scaled(pot, -1, 1)

pause()

Warning

If _values_ contains elements that lie outside _input\_min_ to _input\_max_ (inclusive) then the function will not produce values that lie within _output\_min_ to _output\_max_ (inclusive).

20.2. Combining sources[](https://gpiozero.readthedocs.io/en/stable/api_tools.html#combining-sources "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------

gpiozero.tools.all_values(_*values_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/tools.html#all_values)[](https://gpiozero.readthedocs.io/en/stable/api_tools.html#gpiozero.tools.all_values "Link to this definition")
Returns the [logical conjunction](https://en.wikipedia.org/wiki/Logical_conjunction) of all supplied values (the result is only [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") if and only if all input values are simultaneously [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)")). One or more _values_ can be specified. For example, to light an [`LED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED "gpiozero.LED") only when _both_ buttons are pressed:

from gpiozero import LED, Button
from gpiozero.tools import all_values
from signal import pause

led = LED(4)
btn1 = Button(20)
btn2 = Button(21)

led.source = all_values(btn1, btn2)

pause()

gpiozero.tools.any_values(_*values_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/tools.html#any_values)[](https://gpiozero.readthedocs.io/en/stable/api_tools.html#gpiozero.tools.any_values "Link to this definition")
Returns the [logical disjunction](https://en.wikipedia.org/wiki/Logical_disjunction) of all supplied values (the result is [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") if any of the input values are currently [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)")). One or more _values_ can be specified. For example, to light an [`LED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED "gpiozero.LED") when _any_ button is pressed:

from gpiozero import LED, Button
from gpiozero.tools import any_values
from signal import pause

led = LED(4)
btn1 = Button(20)
btn2 = Button(21)

led.source = any_values(btn1, btn2)

pause()

gpiozero.tools.averaged(_*values_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/tools.html#averaged)[](https://gpiozero.readthedocs.io/en/stable/api_tools.html#gpiozero.tools.averaged "Link to this definition")
Returns the mean of all supplied values. One or more _values_ can be specified. For example, to light a [`PWMLED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED "gpiozero.PWMLED") as the average of several potentiometers connected to an [`MCP3008`](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3008 "gpiozero.MCP3008") ADC:

from gpiozero import MCP3008, PWMLED
from gpiozero.tools import averaged
from signal import pause

pot1 = MCP3008(channel=0)
pot2 = MCP3008(channel=1)
pot3 = MCP3008(channel=2)
led = PWMLED(4)

led.source = averaged(pot1, pot2, pot3)

pause()

gpiozero.tools.multiplied(_*values_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/tools.html#multiplied)[](https://gpiozero.readthedocs.io/en/stable/api_tools.html#gpiozero.tools.multiplied "Link to this definition")
Returns the product of all supplied values. One or more _values_ can be specified. For example, to light a [`PWMLED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED "gpiozero.PWMLED") as the product (i.e. multiplication) of several potentiometers connected to an [`MCP3008`](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3008 "gpiozero.MCP3008") ADC:

from gpiozero import MCP3008, PWMLED
from gpiozero.tools import multiplied
from signal import pause

pot1 = MCP3008(channel=0)
pot2 = MCP3008(channel=1)
pot3 = MCP3008(channel=2)
led = PWMLED(4)

led.source = multiplied(pot1, pot2, pot3)

pause()

gpiozero.tools.summed(_*values_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/tools.html#summed)[](https://gpiozero.readthedocs.io/en/stable/api_tools.html#gpiozero.tools.summed "Link to this definition")
Returns the sum of all supplied values. One or more _values_ can be specified. For example, to light a [`PWMLED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED "gpiozero.PWMLED") as the (scaled) sum of several potentiometers connected to an [`MCP3008`](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.MCP3008 "gpiozero.MCP3008") ADC:

from gpiozero import MCP3008, PWMLED
from gpiozero.tools import summed, scaled
from signal import pause

pot1 = MCP3008(channel=0)
pot2 = MCP3008(channel=1)
pot3 = MCP3008(channel=2)
led = PWMLED(4)

led.source = scaled(summed(pot1, pot2, pot3), 0, 1, 0, 3)

pause()

gpiozero.tools.zip_values(_*devices_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/tools.html#zip_values)[](https://gpiozero.readthedocs.io/en/stable/api_tools.html#gpiozero.tools.zip_values "Link to this definition")
Provides a source constructed from the values of each item, for example:

from gpiozero import MCP3008, Robot
from gpiozero.tools import zip_values
from signal import pause

robot = Robot(left=(4, 14), right=(17, 18))

left = MCP3008(0)
right = MCP3008(1)

robot.source = zip_values(left, right)

pause()

`zip_values(left, right)` is equivalent to 
```
zip(left.values,
right.values)
```
.

20.3. Artificial sources[](https://gpiozero.readthedocs.io/en/stable/api_tools.html#artificial-sources "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------

gpiozero.tools.alternating_values(_initial\_value=False_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/tools.html#alternating_values)[](https://gpiozero.readthedocs.io/en/stable/api_tools.html#gpiozero.tools.alternating_values "Link to this definition")
Provides an infinite source of values alternating between [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") and [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)"), starting wth _initial\_value_ (which defaults to [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)")). For example, to produce a flashing LED:

from gpiozero import LED
from gpiozero.tools import alternating_values
from signal import pause

red = LED(2)

red.source_delay = 0.5
red.source = alternating_values()

pause()

gpiozero.tools.cos_values(_period=360_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/tools.html#cos_values)[](https://gpiozero.readthedocs.io/en/stable/api_tools.html#gpiozero.tools.cos_values "Link to this definition")
Provides an infinite source of values representing a cosine wave (from -1 to +1) which repeats every _period_ values. For example, to produce a “siren” effect with a couple of LEDs that repeats once a second:

from gpiozero import PWMLED
from gpiozero.tools import cos_values, scaled_half, inverted
from signal import pause

red = PWMLED(2)
blue = PWMLED(3)

red.source_delay = 0.01
blue.source_delay = red.source_delay
red.source = scaled_half(cos_values(100))
blue.source = inverted(red)

pause()

If you require a different range than -1 to +1, see [`scaled()`](https://gpiozero.readthedocs.io/en/stable/api_tools.html#gpiozero.tools.scaled "gpiozero.tools.scaled").

gpiozero.tools.ramping_values(_period=360_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/tools.html#ramping_values)[](https://gpiozero.readthedocs.io/en/stable/api_tools.html#gpiozero.tools.ramping_values "Link to this definition")
Provides an infinite source of values representing a triangle wave (from 0 to 1 and back again) which repeats every _period_ values. For example, to pulse an LED once a second:

from gpiozero import PWMLED
from gpiozero.tools import ramping_values
from signal import pause

red = PWMLED(2)

red.source_delay = 0.01
red.source = ramping_values(100)

pause()

If you require a wider range than 0 to 1, see [`scaled()`](https://gpiozero.readthedocs.io/en/stable/api_tools.html#gpiozero.tools.scaled "gpiozero.tools.scaled").

gpiozero.tools.random_values()[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/tools.html#random_values)[](https://gpiozero.readthedocs.io/en/stable/api_tools.html#gpiozero.tools.random_values "Link to this definition")
Provides an infinite source of random values between 0 and 1. For example, to produce a “flickering candle” effect with an LED:

from gpiozero import PWMLED
from gpiozero.tools import random_values
from signal import pause

led = PWMLED(4)

led.source = random_values()

pause()

If you require a wider range than 0 to 1, see [`scaled()`](https://gpiozero.readthedocs.io/en/stable/api_tools.html#gpiozero.tools.scaled "gpiozero.tools.scaled").

gpiozero.tools.sin_values(_period=360_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/tools.html#sin_values)[](https://gpiozero.readthedocs.io/en/stable/api_tools.html#gpiozero.tools.sin_values "Link to this definition")
Provides an infinite source of values representing a sine wave (from -1 to +1) which repeats every _period_ values. For example, to produce a “siren” effect with a couple of LEDs that repeats once a second:

from gpiozero import PWMLED
from gpiozero.tools import sin_values, scaled_half, inverted
from signal import pause

red = PWMLED(2)
blue = PWMLED(3)

red.source_delay = 0.01
blue.source_delay = red.source_delay
red.source = scaled_half(sin_values(100))
blue.source = inverted(red)

pause()

If you require a different range than -1 to +1, see [`scaled()`](https://gpiozero.readthedocs.io/en/stable/api_tools.html#gpiozero.tools.scaled "gpiozero.tools.scaled").
