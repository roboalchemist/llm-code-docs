# Source: https://gpiozero.readthedocs.io/en/stable/api_boards.html

Title: Boards and Accessories — gpiozero 2.0.1 Documentation

URL Source: https://gpiozero.readthedocs.io/en/stable/api_boards.html

Markdown Content:
These additional interfaces are provided to group collections of components together for ease of use, and as examples. They are composites made up of components from the various [API - Input Devices](https://gpiozero.readthedocs.io/en/stable/api_input.html) and [API - Output Devices](https://gpiozero.readthedocs.io/en/stable/api_output.html) provided by GPIO Zero. See those pages for more information on using components individually.

Note

All GPIO pin numbers use Broadcom (BCM) numbering by default. See the [Pin Numbering](https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering) section for more information.

17.1. Regular Classes[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#regular-classes "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------

The following classes are intended for general use with the devices they are named after. All classes in this section are concrete (not abstract).

### 17.1.1. LEDBoard[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#ledboard "Link to this heading")

_class_ gpiozero.LEDBoard(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#LEDBoard)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBoard "Link to this definition")
Extends [`LEDCollection`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDCollection "gpiozero.LEDCollection") and represents a generic LED board or collection of LEDs.

The following example turns on all the LEDs on a board containing 5 LEDs attached to GPIO pins 2 through 6:

from gpiozero import LEDBoard

leds = LEDBoard(2, 3, 4, 5, 6)
leds.on()

Parameters:
*   ***pins** – Specify the GPIO pins that the LEDs of the board are attached to. See [Pin Numbering](https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering) for valid pin numbers. You can designate as many pins as necessary. You can also specify [`LEDBoard`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBoard "gpiozero.LEDBoard") instances to create trees of LEDs.

*   **pwm** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"), construct [`PWMLED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED "gpiozero.PWMLED") instances for each pin. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") (the default), construct regular [`LED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED "gpiozero.LED") instances.

*   **active_high** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") (the default), the [`on()`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBoard.on "gpiozero.LEDBoard.on") method will set all the associated pins to HIGH. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)"), the [`on()`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBoard.on "gpiozero.LEDBoard.on") method will set all pins to LOW (the [`off()`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBoard.off "gpiozero.LEDBoard.off") method always does the opposite).

*   **initial_value** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")_or_ _None_) – If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") (the default), all LEDs will be off initially. If [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)"), each device will be left in whatever state the pin is found in when configured for output (warning: this can be on). If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"), the device will be switched on initially.

*   **_order** ([_list_](https://docs.python.org/3.9/library/stdtypes.html#list "(in Python v3.9)")_or_ _None_) – If specified, this is the order of named items specified by keyword arguments (to ensure that the `value` tuple is constructed with a specific order). All keyword arguments _must_ be included in the collection. If omitted, an alphabetically sorted order will be selected for keyword arguments.

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

*   ****named_pins** – Specify GPIO pins that LEDs of the board are attached to, associating each LED with a property name. You can designate as many pins as necessary and use any names, provided they’re not already in use by something else. You can also specify [`LEDBoard`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBoard "gpiozero.LEDBoard") instances to create trees of LEDs.

blink(_on\_time=1_, _off\_time=1_, _fade\_in\_time=0_, _fade\_out\_time=0_, _n=None_, _background=True_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#LEDBoard.blink)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBoard.blink "Link to this definition")
Make all the LEDs turn on and off repeatedly.

Parameters:
*   **on_time** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – Number of seconds on. Defaults to 1 second.

*   **off_time** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – Number of seconds off. Defaults to 1 second.

*   **fade_in_time** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – Number of seconds to spend fading in. Defaults to 0. Must be 0 if `pwm` was [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") when the class was constructed ([`ValueError`](https://docs.python.org/3.9/library/exceptions.html#ValueError "(in Python v3.9)") will be raised if not).

*   **fade_out_time** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – Number of seconds to spend fading out. Defaults to 0. Must be 0 if `pwm` was [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") when the class was constructed ([`ValueError`](https://docs.python.org/3.9/library/exceptions.html#ValueError "(in Python v3.9)") will be raised if not).

*   **n** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")_or_ _None_) – Number of times to blink; [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default) means forever.

*   **background** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"), start a background thread to continue blinking and return immediately. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)"), only return when the blink is finished (warning: the default value of _n_ will result in this method never returning).

off(_*args_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#LEDBoard.off)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBoard.off "Link to this definition")
If no arguments are specified, turn all the LEDs off. If arguments are specified, they must be the indexes of the LEDs you wish to turn off. For example:

from gpiozero import LEDBoard

leds = LEDBoard(2, 3, 4, 5)
leds.on()      # turn on all LEDs
leds.off(0)    # turn off the first LED (pin 2)
leds.off(-1)   # turn off the last LED (pin 5)
leds.off(1, 2) # turn off the middle LEDs (pins 3 and 4)
leds.on()      # turn on all LEDs

If [`blink()`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBoard.blink "gpiozero.LEDBoard.blink") is currently active, it will be stopped first.

Parameters:
**args** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")) – The index(es) of the LED(s) to turn off. If no indexes are specified turn off all LEDs.

on(_*args_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#LEDBoard.on)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBoard.on "Link to this definition")
If no arguments are specified, turn all the LEDs on. If arguments are specified, they must be the indexes of the LEDs you wish to turn on. For example:

from gpiozero import LEDBoard

leds = LEDBoard(2, 3, 4, 5)
leds.on(0)    # turn on the first LED (pin 2)
leds.on(-1)   # turn on the last LED (pin 5)
leds.on(1, 2) # turn on the middle LEDs (pins 3 and 4)
leds.off()    # turn off all LEDs
leds.on()     # turn on all LEDs

If [`blink()`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBoard.blink "gpiozero.LEDBoard.blink") is currently active, it will be stopped first.

Parameters:
**args** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")) – The index(es) of the LED(s) to turn on. If no indexes are specified turn on all LEDs.

pulse(_fade\_in\_time=1_, _fade\_out\_time=1_, _n=None_, _background=True_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#LEDBoard.pulse)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBoard.pulse "Link to this definition")
Make all LEDs fade in and out repeatedly. Note that this method will only work if the _pwm_ parameter was [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") at construction time.

Parameters:
*   **fade_in_time** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – Number of seconds to spend fading in. Defaults to 1.

*   **fade_out_time** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – Number of seconds to spend fading out. Defaults to 1.

*   **n** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")_or_ _None_) – Number of times to blink; [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default) means forever.

*   **background** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") (the default), start a background thread to continue blinking and return immediately. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)"), only return when the blink is finished (warning: the default value of _n_ will result in this method never returning).

toggle(_*args_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#LEDBoard.toggle)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBoard.toggle "Link to this definition")
If no arguments are specified, toggle the state of all LEDs. If arguments are specified, they must be the indexes of the LEDs you wish to toggle. For example:

from gpiozero import LEDBoard

leds = LEDBoard(2, 3, 4, 5)
leds.toggle(0)   # turn on the first LED (pin 2)
leds.toggle(-1)  # turn on the last LED (pin 5)
leds.toggle()    # turn the first and last LED off, and the
                 # middle pair on

If [`blink()`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBoard.blink "gpiozero.LEDBoard.blink") is currently active, it will be stopped first.

Parameters:
**args** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")) – The index(es) of the LED(s) to toggle. If no indexes are specified toggle the state of all LEDs.

### 17.1.2. LEDBarGraph[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#ledbargraph "Link to this heading")

_class_ gpiozero.LEDBarGraph(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#LEDBarGraph)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBarGraph "Link to this definition")
Extends [`LEDCollection`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDCollection "gpiozero.LEDCollection") to control a line of LEDs representing a bar graph. Positive values (0 to 1) light the LEDs from first to last. Negative values (-1 to 0) light the LEDs from last to first.

The following example demonstrates turning on the first two and last two LEDs in a board containing five LEDs attached to GPIOs 2 through 6:

from gpiozero import LEDBarGraph
from time import sleep

graph = LEDBarGraph(2, 3, 4, 5, 6)
graph.value = 2/5  # Light the first two LEDs only
sleep(1)
graph.value = -2/5 # Light the last two LEDs only
sleep(1)
graph.off()

As with all other output devices, [`source`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBarGraph.source "gpiozero.LEDBarGraph.source") and [`values`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBarGraph.values "gpiozero.LEDBarGraph.values") are supported:

from gpiozero import LEDBarGraph, MCP3008
from signal import pause

graph = LEDBarGraph(2, 3, 4, 5, 6, pwm=True)
pot = MCP3008(channel=0)

graph.source = pot

pause()

Parameters:
*   ***pins** – Specify the GPIO pins that the LEDs of the bar graph are attached to. See [Pin Numbering](https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering) for valid pin numbers. You can designate as many pins as necessary.

*   **pwm** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"), construct [`PWMLED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED "gpiozero.PWMLED") instances for each pin. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") (the default), construct regular [`LED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED "gpiozero.LED") instances. This parameter can only be specified as a keyword parameter.

*   **active_high** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") (the default), the `on()` method will set all the associated pins to HIGH. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)"), the `on()` method will set all pins to LOW (the `off()` method always does the opposite). This parameter can only be specified as a keyword parameter.

*   **initial_value** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – The initial [`value`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBarGraph.value "gpiozero.LEDBarGraph.value") of the graph given as a float between -1 and +1. Defaults to 0.0. This parameter can only be specified as a keyword parameter.

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

_property_ lit_count[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBarGraph.lit_count "Link to this definition")
The number of LEDs on the bar graph actually lit up. Note that just like [`value`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBarGraph.value "gpiozero.LEDBarGraph.value"), this can be negative if the LEDs are lit from last to first.

_property_ source[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBarGraph.source "Link to this definition")
The iterable to use as a source of values for [`value`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBarGraph.value "gpiozero.LEDBarGraph.value").

_property_ value[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBarGraph.value "Link to this definition")
The value of the LED bar graph. When no LEDs are lit, the value is 0. When all LEDs are lit, the value is 1. Values between 0 and 1 light LEDs linearly from first to last. Values between 0 and -1 light LEDs linearly from last to first.

To light a particular number of LEDs, simply divide that number by the number of LEDs. For example, if your graph contains 3 LEDs, the following will light the first:

from gpiozero import LEDBarGraph

graph = LEDBarGraph(12, 16, 19)
graph.value = 1/3

Note

Setting value to -1 will light all LEDs. However, querying it subsequently will return 1 as both representations are the same in hardware. The readable range of [`value`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBarGraph.value "gpiozero.LEDBarGraph.value") is effectively -1 < value <= 1.

_property_ values[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBarGraph.values "Link to this definition")
An infinite iterator of values read from [`value`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBarGraph.value "gpiozero.LEDBarGraph.value").

### 17.1.3. LEDCharDisplay[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#ledchardisplay "Link to this heading")

_class_ gpiozero.LEDCharDisplay(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#LEDCharDisplay)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDCharDisplay "Link to this definition")
Extends [`LEDCollection`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDCollection "gpiozero.LEDCollection") for a multi-segment LED display.

[Multi-segment LED displays](https://en.wikipedia.org/wiki/Seven-segment_display) typically have 7 pins (labelled “a” through “g”) representing 7 LEDs layed out in a figure-of-8 fashion. Frequently, an eigth pin labelled “dp” is included for a trailing decimal-point:

     a
   ━━━━━
f ┃     ┃ b
  ┃  g  ┃
   ━━━━━
e ┃     ┃ c
  ┃     ┃
   ━━━━━ • dp
     d

Other common layouts are 9, 14, and 16 segment displays which include additional segments permitting more accurate renditions of alphanumerics. For example:

     a
   ━━━━━
f ┃╲i┃j╱┃ b
  ┃ ╲┃╱k┃
  g━━ ━━h
e ┃ ╱┃╲n┃ c
  ┃╱l┃m╲┃
   ━━━━━ • dp
     d

Such displays have either a common anode, or common cathode pin. This class defaults to the latter; when using a common anode display _active\_high_ should be set to [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)").

Instances of this class can be used to display characters or control individual LEDs on the display. For example:

from gpiozero import LEDCharDisplay

char = LEDCharDisplay(4, 5, 6, 7, 8, 9, 10, active_high=False)
char.value = 'C'

If the class is constructed with 7 or 14 segments, a default [`font`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDCharDisplay.font "gpiozero.LEDCharDisplay.font") will be loaded, mapping some ASCII characters to typical layouts. In other cases, the default mapping will simply assign “ “ (space) to all LEDs off. You can assign your own mapping at construction time or after instantiation.

While the example above shows the display with a [`str`](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)") value, theoretically the _font_ can map any value that can be the key in a [`dict`](https://docs.python.org/3.9/library/stdtypes.html#dict "(in Python v3.9)"), so the value of the display can be likewise be any valid key value (e.g. you could map integer digits to LED patterns). That said, there is one exception to this: when _dp_ is specified to enable the decimal-point, the [`value`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDCharDisplay.value "gpiozero.LEDCharDisplay.value") must be a [`str`](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)") as the presence or absence of a “.” suffix indicates whether the _dp_ LED is lit.

Parameters:
*   ***pins** – Specify the GPIO pins that the multi-segment display is attached to. Pins should be in the LED segment order A, B, C, D, E, F, G, and will be named automatically by the class. If a decimal-point pin is present, specify it separately as the _dp_ parameter.

*   **dp** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")_or_[_str_](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)")) – If a decimal-point segment is present, specify it as this named parameter.

*   **font** ([_dict_](https://docs.python.org/3.9/library/stdtypes.html#dict "(in Python v3.9)")_or_ _None_) – A mapping of values (typically characters, but may also be numbers) to tuples of LED states. A default mapping for ASCII characters is provided for 7 and 14 segment displays.

*   **pwm** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"), construct [`PWMLED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED "gpiozero.PWMLED") instances for each pin. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") (the default), construct regular [`LED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED "gpiozero.LED") instances.

*   **active_high** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") (the default), the `on()` method will set all the associated pins to HIGH. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)"), the `on()` method will set all pins to LOW (the `off()` method always does the opposite).

*   **initial_value** – The initial value to display. Defaults to space (” “) which typically maps to all LEDs being inactive. If [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)"), each device will be left in whatever state the pin is found in when configured for output (warning: this can be on).

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

_property_ font[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDCharDisplay.font "Link to this definition")
An [`LEDCharFont`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDCharFont "gpiozero.LEDCharFont") mapping characters to tuples of LED states. The font is mutable after construction. You can assign a tuple of LED states to a character to modify the font, delete an existing character in the font, or assign a mapping of characters to tuples to replace the entire font.

Note that modifying the [`font`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDCharDisplay.font "gpiozero.LEDCharDisplay.font") never alters the underlying LED states. Only assignment to [`value`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDCharDisplay.value "gpiozero.LEDCharDisplay.value"), or calling the inherited [`LEDCollection`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDCollection "gpiozero.LEDCollection") methods (`on()`, `off()`, etc.) modifies LED states. However, modifying the font may alter the character returned by querying [`value`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDCharDisplay.value "gpiozero.LEDCharDisplay.value").

_property_ value[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDCharDisplay.value "Link to this definition")
The character the display should show. This is mapped by the current [`font`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDCharDisplay.font "gpiozero.LEDCharDisplay.font") to a tuple of LED states which is applied to the underlying LED objects when this attribute is set.

When queried, the current LED states are looked up in the font to determine the character shown. If the current LED states do not correspond to any character in the [`font`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDCharDisplay.font "gpiozero.LEDCharDisplay.font"), the value is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)").

It is possible for multiple characters in the font to map to the same LED states (e.g. S and 5). In this case, if the font was constructed from an ordered mapping (which is the default), then the first matching mapping will always be returned. This also implies that the value queried need not match the value set.

### 17.1.4. LEDMultiCharDisplay[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#ledmultichardisplay "Link to this heading")

_class_ gpiozero.LEDMultiCharDisplay(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#LEDMultiCharDisplay)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDMultiCharDisplay "Link to this definition")
Wraps [`LEDCharDisplay`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDCharDisplay "gpiozero.LEDCharDisplay") for multi-character [multiplexed](https://en.wikipedia.org/wiki/Multiplexed_display) LED character displays.

The class is constructed with a _char_ which is an instance of the [`LEDCharDisplay`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDCharDisplay "gpiozero.LEDCharDisplay") class, capable of controlling the LEDs in one character of the display, and an additional set of _pins_ that represent the common cathode (or anode) of each character.

Warning

You should not attempt to connect the common cathode (or anode) off each character directly to a GPIO. Rather, use a set of transistors (or some other suitable component capable of handling the current of all the segment LEDs simultaneously) to connect the common cathode to ground (or the common anode to the supply) and control those transistors from the GPIOs specified under _pins_.

The _active\_high_ parameter defaults to [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"). Note that it only applies to the specified _pins_, which are assumed to be controlling a set of transistors (hence the default). The specified _char_ will use its own _active\_high_ parameter. Finally, _initial\_value_ defaults to a tuple of [`value`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDCharDisplay.value "gpiozero.LEDCharDisplay.value") attribute of the specified display multiplied by the number of _pins_ provided.

When the [`value`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDMultiCharDisplay.value "gpiozero.LEDMultiCharDisplay.value") is set such that one or more characters in the display differ in value, a background thread is implicitly started to rotate the active character, relying on [persistence of vision](https://en.wikipedia.org/wiki/Persistence_of_vision) to display the complete value.

_property_ plex_delay[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDMultiCharDisplay.plex_delay "Link to this definition")
The delay (measured in seconds) in the loop used to switch each character in the multiplexed display on. Defaults to 0.005 seconds which is generally sufficient to provide a “stable” (non-flickery) display.

_property_ value[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDMultiCharDisplay.value "Link to this definition")
The sequence of values to display.

This can be any sequence containing keys from the [`font`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDCharDisplay.font "gpiozero.LEDCharDisplay.font") of the associated character display. For example, if the value consists only of single-character strings, it’s valid to assign a string to this property (as a string is simply a sequence of individual character keys):

from gpiozero import LEDCharDisplay, LEDMultiCharDisplay

c = LEDCharDisplay(4, 5, 6, 7, 8, 9, 10)
d = LEDMultiCharDisplay(c, 19, 20, 21, 22)
d.value = 'LEDS'

However, things get more complicated if a decimal point is in use as then this class needs to know explicitly where to break the value for use on each character of the display. This can be handled by simply assigning a sequence of strings thus:

from gpiozero import LEDCharDisplay, LEDMultiCharDisplay

c = LEDCharDisplay(4, 5, 6, 7, 8, 9, 10)
d = LEDMultiCharDisplay(c, 19, 20, 21, 22)
d.value = ('L.', 'E', 'D', 'S')

This is how the value will always be represented when queried (as a tuple of individual values) as it neatly handles dealing with heterogeneous types and the aforementioned decimal point issue.

Note

The value also controls whether a background thread is in use to multiplex the display. When all positions in the value are equal the background thread is disabled and all characters are simultaneously enabled.

### 17.1.5. LEDCharFont[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#ledcharfont "Link to this heading")

_class_ gpiozero.LEDCharFont(_font_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#LEDCharFont)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDCharFont "Link to this definition")
Contains a mapping of values to tuples of LED states.

This effectively acts as a “font” for [`LEDCharDisplay`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDCharDisplay "gpiozero.LEDCharDisplay"), and two default fonts (for 7-segment and 14-segment displays) are shipped with GPIO Zero by default. You can construct your own font instance from a [`dict`](https://docs.python.org/3.9/library/stdtypes.html#dict "(in Python v3.9)") which maps values (usually single-character strings) to a tuple of LED states:

from gpiozero import LEDCharDisplay, LEDCharFont

my_font = LEDCharFont({
    ' ': (0, 0, 0, 0, 0, 0, 0),
    'D': (1, 1, 1, 1, 1, 1, 0),
    'A': (1, 1, 1, 0, 1, 1, 1),
    'd': (0, 1, 1, 1, 1, 0, 1),
    'a': (1, 1, 1, 1, 1, 0, 1),
})
display = LEDCharDisplay(26, 13, 12, 22, 17, 19, 6, dp=5, font=my_font)
display.value = 'D'

Font instances are mutable and can be changed while actively in use by an instance of [`LEDCharDisplay`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDCharDisplay "gpiozero.LEDCharDisplay"). However, changing the font will _not_ change the state of the LEDs in the display (though it may change the [`value`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDCharDisplay.value "gpiozero.LEDCharDisplay.value") of the display when next queried).

Note

Your custom mapping should always include a value (typically space) which represents all the LEDs off. This will usually be the default value for an instance of [`LEDCharDisplay`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDCharDisplay "gpiozero.LEDCharDisplay").

You may also wish to load fonts from a friendly text-based format. A simple parser for such formats (supporting an arbitrary number of segments) is provided by [`gpiozero.fonts.load_segment_font()`](https://gpiozero.readthedocs.io/en/stable/api_fonts.html#gpiozero.fonts.load_segment_font "gpiozero.fonts.load_segment_font").

### 17.1.6. ButtonBoard[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#buttonboard "Link to this heading")

_class_ gpiozero.ButtonBoard(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#ButtonBoard)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.ButtonBoard "Link to this definition")
Extends [`CompositeDevice`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.CompositeDevice "gpiozero.CompositeDevice") and represents a generic button board or collection of buttons. The [`value`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.ButtonBoard.value "gpiozero.ButtonBoard.value") of the button board is a tuple of all the buttons states. This can be used to control all the LEDs in a [`LEDBoard`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBoard "gpiozero.LEDBoard") with a [`ButtonBoard`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.ButtonBoard "gpiozero.ButtonBoard"):

from gpiozero import LEDBoard, ButtonBoard
from signal import pause

leds = LEDBoard(2, 3, 4, 5)
btns = ButtonBoard(6, 7, 8, 9)
leds.source = btns

pause()

Alternatively you could represent the number of pressed buttons with an [`LEDBarGraph`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBarGraph "gpiozero.LEDBarGraph"):

from gpiozero import LEDBarGraph, ButtonBoard
from statistics import mean
from signal import pause

graph = LEDBarGraph(2, 3, 4, 5)
bb = ButtonBoard(6, 7, 8, 9)
graph.source = (mean(values) for values in bb.values)

pause()

Parameters:
*   ***pins** – Specify the GPIO pins that the buttons of the board are attached to. See [Pin Numbering](https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering) for valid pin numbers. You can designate as many pins as necessary.

*   **pull_up** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")_or_ _None_) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") (the default), the GPIO pins will be pulled high by default. In this case, connect the other side of the buttons to ground. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)"), the GPIO pins will be pulled low by default. In this case, connect the other side of the buttons to 3V3. If [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)"), the pin will be floating, so it must be externally pulled up or down and the `active_state` parameter must be set accordingly.

*   **active_state** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")_or_ _None_) – See description under [`InputDevice`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.InputDevice "gpiozero.InputDevice") for more information.

*   **bounce_time** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – If [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default), no software bounce compensation will be performed. Otherwise, this is the length of time (in seconds) that the buttons will ignore changes in state after an initial change.

*   **hold_time** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – The length of time (in seconds) to wait after any button is pushed, until executing the `when_held` handler. Defaults to `1`.

*   **hold_repeat** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"), the `when_held` handler will be repeatedly executed as long as any buttons remain held, every _hold\_time_ seconds. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") (the default) the `when_held` handler will be only be executed once per hold.

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

*   ****named_pins** – Specify GPIO pins that buttons of the board are attached to, associating each button with a property name. You can designate as many pins as necessary and use any names, provided they’re not already in use by something else.

wait_for_press(_timeout=None_)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.ButtonBoard.wait_for_press "Link to this definition")
Pause the script until the device is activated, or the timeout is reached.

Parameters:
**timeout** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")_or_ _None_) – Number of seconds to wait before proceeding. If this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default), then wait indefinitely until the device is active.

wait_for_release(_timeout=None_)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.ButtonBoard.wait_for_release "Link to this definition")
Pause the script until the device is deactivated, or the timeout is reached.

Parameters:
**timeout** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")_or_ _None_) – Number of seconds to wait before proceeding. If this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default), then wait indefinitely until the device is inactive.

_property_ is_pressed[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.ButtonBoard.is_pressed "Link to this definition")
Composite devices are considered “active” if any of their constituent devices have a “truthy” value.

_property_ pressed_time[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.ButtonBoard.pressed_time "Link to this definition")
The length of time (in seconds) that the device has been active for. When the device is inactive, this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)").

_property_ value[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.ButtonBoard.value "Link to this definition")
A [`namedtuple()`](https://docs.python.org/3.9/library/collections.html#collections.namedtuple "(in Python v3.9)") containing a value for each subordinate device. Devices with names will be represented as named elements. Unnamed devices will have a unique name generated for them, and they will appear in the position they appeared in the constructor.

when_pressed[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.ButtonBoard.when_pressed "Link to this definition")
The function to run when the device changes state from inactive to active.

This can be set to a function which accepts no (mandatory) parameters, or a Python function which accepts a single mandatory parameter (with as many optional parameters as you like). If the function accepts a single mandatory parameter, the device that activated it will be passed as that parameter.

Set this property to [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default) to disable the event.

when_released[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.ButtonBoard.when_released "Link to this definition")
The function to run when the device changes state from active to inactive.

This can be set to a function which accepts no (mandatory) parameters, or a Python function which accepts a single mandatory parameter (with as many optional parameters as you like). If the function accepts a single mandatory parameter, the device that deactivated it will be passed as that parameter.

Set this property to [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default) to disable the event.

### 17.1.7. TrafficLights[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#trafficlights "Link to this heading")

_class_ gpiozero.TrafficLights(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#TrafficLights)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.TrafficLights "Link to this definition")
Extends [`LEDBoard`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBoard "gpiozero.LEDBoard") for devices containing red, yellow, and green LEDs.

The following example initializes a device connected to GPIO pins 2, 3, and 4, then lights the amber (yellow) LED attached to GPIO 3:

from gpiozero import TrafficLights

traffic = TrafficLights(2, 3, 4)
traffic.amber.on()

Parameters:
*   **red** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")_or_[_str_](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)")) – The GPIO pin that the red LED is attached to. See [Pin Numbering](https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering) for valid pin numbers.

*   **amber** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")_or_[_str_](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)")_or_ _None_) – The GPIO pin that the amber LED is attached to. See [Pin Numbering](https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering) for valid pin numbers.

*   **yellow** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")_or_[_str_](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)")_or_ _None_) – The GPIO pin that the yellow LED is attached to. This is merely an alias for the `amber` parameter; you can’t specify both `amber` and `yellow`. See [Pin Numbering](https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering) for valid pin numbers.

*   **green** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")_or_[_str_](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)")) – The GPIO pin that the green LED is attached to. See [Pin Numbering](https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-numbering) for valid pin numbers.

*   **pwm** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"), construct [`PWMLED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED "gpiozero.PWMLED") instances to represent each LED. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") (the default), construct regular [`LED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED "gpiozero.LED") instances.

*   **initial_value** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")_or_ _None_) – If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") (the default), all LEDs will be off initially. If [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)"), each device will be left in whatever state the pin is found in when configured for output (warning: this can be on). If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"), the device will be switched on initially.

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

red[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.TrafficLights.red "Link to this definition")
The red [`LED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED "gpiozero.LED") or [`PWMLED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED "gpiozero.PWMLED").

amber[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.TrafficLights.amber "Link to this definition")
The amber [`LED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED "gpiozero.LED") or [`PWMLED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED "gpiozero.PWMLED"). Note that this attribute will not be present when the instance is constructed with the _yellow_ keyword parameter.

yellow[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.TrafficLights.yellow "Link to this definition")
The yellow [`LED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED "gpiozero.LED") or [`PWMLED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED "gpiozero.PWMLED"). Note that this attribute will only be present when the instance is constructed with the _yellow_ keyword parameter.

green[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.TrafficLights.green "Link to this definition")
The green [`LED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED "gpiozero.LED") or [`PWMLED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED "gpiozero.PWMLED").

### 17.1.8. TrafficLightsBuzzer[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#trafficlightsbuzzer "Link to this heading")

_class_ gpiozero.TrafficLightsBuzzer(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#TrafficLightsBuzzer)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.TrafficLightsBuzzer "Link to this definition")
Extends [`CompositeOutputDevice`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.CompositeOutputDevice "gpiozero.CompositeOutputDevice") and is a generic class for HATs with traffic lights, a button and a buzzer.

Parameters:
*   **lights** ([_TrafficLights_](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.TrafficLights "gpiozero.TrafficLights")) – An instance of [`TrafficLights`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.TrafficLights "gpiozero.TrafficLights") representing the traffic lights of the HAT.

*   **buzzer** ([_Buzzer_](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Buzzer "gpiozero.Buzzer")) – An instance of [`Buzzer`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Buzzer "gpiozero.Buzzer") representing the buzzer on the HAT.

*   **button** ([_Button_](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button "gpiozero.Button")) – An instance of [`Button`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button "gpiozero.Button") representing the button on the HAT.

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

lights[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.TrafficLightsBuzzer.lights "Link to this definition")
The [`TrafficLights`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.TrafficLights "gpiozero.TrafficLights") instance passed as the _lights_ parameter.

buzzer[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.TrafficLightsBuzzer.buzzer "Link to this definition")
The [`Buzzer`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Buzzer "gpiozero.Buzzer") instance passed as the _buzzer_ parameter.

button[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.TrafficLightsBuzzer.button "Link to this definition")
The [`Button`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button "gpiozero.Button") instance passed as the _button_ parameter.

### 17.1.9. PiHutXmasTree[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#pihutxmastree "Link to this heading")

_class_ gpiozero.PiHutXmasTree(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#PiHutXmasTree)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.PiHutXmasTree "Link to this definition")
Extends [`LEDBoard`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBoard "gpiozero.LEDBoard") for [The Pi Hut’s Xmas board](https://thepihut.com/xmas): a 3D Christmas tree board with 24 red LEDs and a white LED as a star on top.

The 24 red LEDs can be accessed through the attributes led0, led1, led2, and so on. The white star LED is accessed through the [`star`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.PiHutXmasTree.star "gpiozero.PiHutXmasTree.star") attribute. Alternatively, as with all descendents of [`LEDBoard`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBoard "gpiozero.LEDBoard"), you can treat the instance as a sequence of LEDs (the first element is the [`star`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.PiHutXmasTree.star "gpiozero.PiHutXmasTree.star")).

The Xmas Tree board pins are fixed and therefore there’s no need to specify them when constructing this class. The following example turns all the LEDs on one at a time:

from gpiozero import PiHutXmasTree
from time import sleep

tree = PiHutXmasTree()

for light in tree:
    light.on()
    sleep(1)

The following example turns the star LED on and sets all the red LEDs to flicker randomly:

from gpiozero import PiHutXmasTree
from gpiozero.tools import random_values
from signal import pause

tree = PiHutXmasTree(pwm=True)

tree.star.on()

for led in tree[1:]:
    led.source_delay = 0.1
    led.source = random_values()

pause()

Parameters:
*   **pwm** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"), construct [`PWMLED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED "gpiozero.PWMLED") instances for each pin. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") (the default), construct regular [`LED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED "gpiozero.LED") instances.

*   **initial_value** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")_or_ _None_) – If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") (the default), all LEDs will be off initially. If [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)"), each device will be left in whatever state the pin is found in when configured for output (warning: this can be on). If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"), the device will be switched on initially.

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

star[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.PiHutXmasTree.star "Link to this definition")
Returns the [`LED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED "gpiozero.LED") or [`PWMLED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED "gpiozero.PWMLED") representing the white star on top of the tree.

led0,led1,led2,...
Returns the [`LED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED "gpiozero.LED") or [`PWMLED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED "gpiozero.PWMLED") representing one of the red LEDs. There are actually 24 of these properties named led0, led1, and so on but for the sake of brevity we represent all 24 under this section.

### 17.1.10. LedBorg[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#ledborg "Link to this heading")

_class_ gpiozero.LedBorg(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#LedBorg)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LedBorg "Link to this definition")
Extends [`RGBLED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.RGBLED "gpiozero.RGBLED") for the [PiBorg LedBorg](https://www.piborg.org/ledborg): an add-on board containing a very bright RGB LED.

The LedBorg pins are fixed and therefore there’s no need to specify them when constructing this class. The following example turns the LedBorg purple:

from gpiozero import LedBorg

led = LedBorg()
led.color = (1, 0, 1)

Parameters:
*   **initial_value** ([_Color_](https://colorzero.readthedocs.io/en/latest/api_color.html#colorzero.Color "(in Colorzero v2.0)")_or_[_tuple_](https://docs.python.org/3.9/library/stdtypes.html#tuple "(in Python v3.9)")) – The initial color for the LedBorg. Defaults to black `(0, 0, 0)`.

*   **pwm** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") (the default), construct [`PWMLED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED "gpiozero.PWMLED") instances for each component of the LedBorg. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)"), construct regular [`LED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED "gpiozero.LED") instances, which prevents smooth color graduations.

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

### 17.1.11. PiLiter[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#piliter "Link to this heading")

_class_ gpiozero.PiLiter(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#PiLiter)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.PiLiter "Link to this definition")
Extends [`LEDBoard`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBoard "gpiozero.LEDBoard") for the [Ciseco Pi-LITEr](http://shop.ciseco.co.uk/pi-liter-8-led-strip-for-the-raspberry-pi/): a strip of 8 very bright LEDs.

The Pi-LITEr pins are fixed and therefore there’s no need to specify them when constructing this class. The following example turns on all the LEDs of the Pi-LITEr:

from gpiozero import PiLiter

lite = PiLiter()
lite.on()

Parameters:
*   **pwm** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"), construct [`PWMLED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED "gpiozero.PWMLED") instances for each pin. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") (the default), construct regular [`LED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED "gpiozero.LED") instances.

*   **initial_value** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")_or_ _None_) – If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") (the default), all LEDs will be off initially. If [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)"), each LED will be left in whatever state the pin is found in when configured for output (warning: this can be on). If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"), the each LED will be switched on initially.

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

### 17.1.12. PiLiterBarGraph[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#piliterbargraph "Link to this heading")

_class_ gpiozero.PiLiterBarGraph(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#PiLiterBarGraph)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.PiLiterBarGraph "Link to this definition")
Extends [`LEDBarGraph`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBarGraph "gpiozero.LEDBarGraph") to treat the [Ciseco Pi-LITEr](http://shop.ciseco.co.uk/pi-liter-8-led-strip-for-the-raspberry-pi/) as an 8-segment bar graph.

The Pi-LITEr pins are fixed and therefore there’s no need to specify them when constructing this class. The following example sets the graph value to 0.5:

from gpiozero import PiLiterBarGraph

graph = PiLiterBarGraph()
graph.value = 0.5

Parameters:
*   **pwm** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"), construct [`PWMLED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED "gpiozero.PWMLED") instances for each pin. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") (the default), construct regular [`LED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED "gpiozero.LED") instances.

*   **initial_value** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – The initial `value` of the graph given as a float between -1 and +1. Defaults to `0.0`.

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

### 17.1.13. PiTraffic[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#pitraffic "Link to this heading")

_class_ gpiozero.PiTraffic(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#PiTraffic)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.PiTraffic "Link to this definition")
Extends [`TrafficLights`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.TrafficLights "gpiozero.TrafficLights") for the [Low Voltage Labs PI-TRAFFIC](http://lowvoltagelabs.com/products/pi-traffic/) vertical traffic lights board when attached to GPIO pins 9, 10, and 11.

There’s no need to specify the pins if the PI-TRAFFIC is connected to the default pins (9, 10, 11). The following example turns on the amber LED on the PI-TRAFFIC:

from gpiozero import PiTraffic

traffic = PiTraffic()
traffic.amber.on()

To use the PI-TRAFFIC board when attached to a non-standard set of pins, simply use the parent class, [`TrafficLights`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.TrafficLights "gpiozero.TrafficLights").

Parameters:
*   **pwm** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"), construct [`PWMLED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED "gpiozero.PWMLED") instances to represent each LED. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") (the default), construct regular [`LED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED "gpiozero.LED") instances.

*   **initial_value** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") (the default), all LEDs will be off initially. If [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)"), each device will be left in whatever state the pin is found in when configured for output (warning: this can be on). If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"), the device will be switched on initially.

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

### 17.1.14. PiStop[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#pistop "Link to this heading")

_class_ gpiozero.PiStop(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#PiStop)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.PiStop "Link to this definition")
Extends [`TrafficLights`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.TrafficLights "gpiozero.TrafficLights") for the [PiHardware Pi-Stop](https://pihw.wordpress.com/meltwaters-pi-hardware-kits/pi-stop/): a vertical traffic lights board.

The following example turns on the amber LED on a Pi-Stop connected to location `A+`:

from gpiozero import PiStop

traffic = PiStop('A+')
traffic.amber.on()

Parameters:
*   **location** ([_str_](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)")) – The [location](https://github.com/PiHw/Pi-Stop/blob/master/markdown_source/markdown/Discover-PiStop.md) on the GPIO header to which the Pi-Stop is connected. Must be one of: `A`, `A+`, `B`, `B+`, `C`, `D`.

*   **pwm** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"), construct [`PWMLED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED "gpiozero.PWMLED") instances to represent each LED. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") (the default), construct regular [`LED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED "gpiozero.LED") instances.

*   **initial_value** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") (the default), all LEDs will be off initially. If [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)"), each device will be left in whatever state the pin is found in when configured for output (warning: this can be on). If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"), the device will be switched on initially.

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

### 17.1.15. FishDish[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#fishdish "Link to this heading")

_class_ gpiozero.FishDish(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#FishDish)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.FishDish "Link to this definition")
Extends [`CompositeOutputDevice`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.CompositeOutputDevice "gpiozero.CompositeOutputDevice") for the [Pi Supply FishDish](https://www.pi-supply.com/product/fish-dish-raspberry-pi-led-buzzer-board/): traffic light LEDs, a button and a buzzer.

The FishDish pins are fixed and therefore there’s no need to specify them when constructing this class. The following example waits for the button to be pressed on the FishDish, then turns on all the LEDs:

from gpiozero import FishDish

fish = FishDish()
fish.button.wait_for_press()
fish.lights.on()

Parameters:
*   **pwm** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"), construct [`PWMLED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED "gpiozero.PWMLED") instances to represent each LED. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") (the default), construct regular [`LED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED "gpiozero.LED") instances.

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

### 17.1.16. TrafficHat[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#traffichat "Link to this heading")

_class_ gpiozero.TrafficHat(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#TrafficHat)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.TrafficHat "Link to this definition")
Extends [`CompositeOutputDevice`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.CompositeOutputDevice "gpiozero.CompositeOutputDevice") for the [Pi Supply Traffic HAT](https://uk.pi-supply.com/products/traffic-hat-for-raspberry-pi): a board with traffic light LEDs, a button and a buzzer.

The Traffic HAT pins are fixed and therefore there’s no need to specify them when constructing this class. The following example waits for the button to be pressed on the Traffic HAT, then turns on all the LEDs:

from gpiozero import TrafficHat

hat = TrafficHat()
hat.button.wait_for_press()
hat.lights.on()

Parameters:
*   **pwm** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"), construct [`PWMLED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED "gpiozero.PWMLED") instances to represent each LED. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") (the default), construct regular [`LED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED "gpiozero.LED") instances.

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

### 17.1.17. TrafficpHat[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#trafficphat "Link to this heading")

_class_ gpiozero.TrafficpHat(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#TrafficpHat)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.TrafficpHat "Link to this definition")
Extends [`TrafficLights`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.TrafficLights "gpiozero.TrafficLights") for the [Pi Supply Traffic pHAT](http://pisupp.ly/trafficphat): a small board with traffic light LEDs.

The Traffic pHAT pins are fixed and therefore there’s no need to specify them when constructing this class. The following example then turns on all the LEDs:

from gpiozero import TrafficpHat
phat = TrafficpHat()
phat.red.on()
phat.blink()

Parameters:
*   **pwm** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"), construct [`PWMLED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED "gpiozero.PWMLED") instances to represent each LED. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") (the default), construct regular [`LED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED "gpiozero.LED") instances.

*   **initial_value** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")_or_ _None_) – If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") (the default), all LEDs will be off initially. If [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)"), each device will be left in whatever state the pin is found in when configured for output (warning: this can be on). If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"), the device will be switched on initially.

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

### 17.1.18. JamHat[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#jamhat "Link to this heading")

_class_ gpiozero.JamHat(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#JamHat)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.JamHat "Link to this definition")
Extends [`CompositeOutputDevice`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.CompositeOutputDevice "gpiozero.CompositeOutputDevice") for the [ModMyPi JamHat](https://thepihut.com/products/jam-hat) board.

There are 6 LEDs, two buttons and a tonal buzzer. The pins are fixed. Usage:

from gpiozero import JamHat

hat = JamHat()

hat.button_1.wait_for_press()
hat.lights_1.on()
hat.buzzer.play('C4')
hat.button_2.wait_for_press()
hat.off()

Parameters:
*   **pwm** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"), construct [`PWMLED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED "gpiozero.PWMLED") instances to represent each LED on the board. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") (the default), construct regular [`LED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED "gpiozero.LED") instances.

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

lights_1,lights_2
Two [`LEDBoard`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBoard "gpiozero.LEDBoard") instances representing the top (lights_1) and bottom (lights_2) rows of LEDs on the JamHat.

red,yellow,green
[`LED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED "gpiozero.LED") or [`PWMLED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED "gpiozero.PWMLED") instances representing the red, yellow, and green LEDs along the top row.

button_1,button_2
The left (button_1) and right (button_2) [`Button`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button "gpiozero.Button") objects on the JamHat.

buzzer[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.JamHat.buzzer "Link to this definition")
The [`TonalBuzzer`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.TonalBuzzer "gpiozero.TonalBuzzer") at the bottom right of the JamHat.

off()[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#JamHat.off)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.JamHat.off "Link to this definition")
Turns all the LEDs off and stops the buzzer.

on()[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#JamHat.on)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.JamHat.on "Link to this definition")
Turns all the LEDs on and makes the buzzer play its mid tone.

### 17.1.19. Pibrella[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#pibrella "Link to this heading")

_class_ gpiozero.Pibrella(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#Pibrella)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Pibrella "Link to this definition")
Extends [`CompositeOutputDevice`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.CompositeOutputDevice "gpiozero.CompositeOutputDevice") for the Cyntech/Pimoroni [Pibrella](http://www.pibrella.com/) board.

The Pibrella board comprises 3 LEDs, a button, a tonal buzzer, four general purpose input channels, and four general purpose output channels (with LEDs).

This class exposes the LEDs, button and buzzer.

Usage:

from gpiozero import Pibrella

pb = Pibrella()

pb.button.wait_for_press()
pb.lights.on()
pb.buzzer.play('A4')
pb.off()

The four input and output channels are exposed so you can create GPIO Zero devices using these pins without looking up their respective pin numbers:

from gpiozero import Pibrella, LED, Button

pb = Pibrella()
btn = Button(pb.inputs.a, pull_up=False)
led = LED(pb.outputs.e)

btn.when_pressed = led.on

Parameters:
*   **pwm** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"), construct [`PWMLED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED "gpiozero.PWMLED") instances to represent each LED on the board, otherwise if [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") (the default), construct regular [`LED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED "gpiozero.LED") instances.

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

lights[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Pibrella.lights "Link to this definition")
[`TrafficLights`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.TrafficLights "gpiozero.TrafficLights") instance representing the three LEDs

red,amber,green
[`LED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED "gpiozero.LED") or [`PWMLED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED "gpiozero.PWMLED") instances representing the red, amber, and green LEDs

button[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Pibrella.button "Link to this definition")
The red [`Button`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button "gpiozero.Button") object on the Pibrella

buzzer[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Pibrella.buzzer "Link to this definition")
A [`TonalBuzzer`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.TonalBuzzer "gpiozero.TonalBuzzer") object representing the buzzer

inputs[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Pibrella.inputs "Link to this definition")
A [`namedtuple()`](https://docs.python.org/3.9/library/collections.html#collections.namedtuple "(in Python v3.9)") of the input pin numbers

a,b,c,d outputs[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Pibrella.outputs "Link to this definition")
A [`namedtuple()`](https://docs.python.org/3.9/library/collections.html#collections.namedtuple "(in Python v3.9)") of the output pin numbers

e,f,g,h off()[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#Pibrella.off)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Pibrella.off "Link to this definition")
Turns all the LEDs off and stops the buzzer.

on()[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#Pibrella.on)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Pibrella.on "Link to this definition")
Turns all the LEDs on and makes the buzzer play its mid tone.

### 17.1.20. Robot[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#robot "Link to this heading")

_class_ gpiozero.Robot(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#Robot)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Robot "Link to this definition")
Extends [`CompositeDevice`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.CompositeDevice "gpiozero.CompositeDevice") to represent a generic dual-motor robot.

This class is constructed with two motor instances representing the left and right wheels of the robot respectively. For example, if the left motor’s controller is connected to GPIOs 4 and 14, while the right motor’s controller is connected to GPIOs 17 and 18 then the following example will drive the robot forward:

from gpiozero import Robot

robot = Robot(left=Motor(4, 14), right=Motor(17, 18))
robot.forward()

Parameters:
*   **left** ([_Motor_](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Motor "gpiozero.Motor")_or_[_PhaseEnableMotor_](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PhaseEnableMotor "gpiozero.PhaseEnableMotor")) – A [`Motor`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Motor "gpiozero.Motor") or a [`PhaseEnableMotor`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PhaseEnableMotor "gpiozero.PhaseEnableMotor") for the left wheel of the robot.

*   **right** ([_Motor_](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Motor "gpiozero.Motor")_or_[_PhaseEnableMotor_](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PhaseEnableMotor "gpiozero.PhaseEnableMotor")) – A [`Motor`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Motor "gpiozero.Motor") or a [`PhaseEnableMotor`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PhaseEnableMotor "gpiozero.PhaseEnableMotor") for the right wheel of the robot.

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

left_motor[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Robot.left_motor "Link to this definition")
The [`Motor`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Motor "gpiozero.Motor") on the left of the robot.

right_motor[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Robot.right_motor "Link to this definition")
The [`Motor`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Motor "gpiozero.Motor") on the right of the robot.

backward(_speed=1_, _*_, _curve\_left=0_, _curve\_right=0_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#Robot.backward)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Robot.backward "Link to this definition")
Drive the robot backward by running both motors backward.

Parameters:
*   **speed** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – Speed at which to drive the motors, as a value between 0 (stopped) and 1 (full speed). The default is 1.

*   **curve_left** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – The amount to curve left while moving backwards, by driving the left motor at a slower speed. Maximum _curve\_left_ is 1, the default is 0 (no curve). This parameter can only be specified as a keyword parameter, and is mutually exclusive with _curve\_right_.

*   **curve_right** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – The amount to curve right while moving backwards, by driving the right motor at a slower speed. Maximum _curve\_right_ is 1, the default is 0 (no curve). This parameter can only be specified as a keyword parameter, and is mutually exclusive with _curve\_left_.

forward(_speed=1_, _*_, _curve\_left=0_, _curve\_right=0_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#Robot.forward)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Robot.forward "Link to this definition")
Drive the robot forward by running both motors forward.

Parameters:
*   **speed** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – Speed at which to drive the motors, as a value between 0 (stopped) and 1 (full speed). The default is 1.

*   **curve_left** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – The amount to curve left while moving forwards, by driving the left motor at a slower speed. Maximum _curve\_left_ is 1, the default is 0 (no curve). This parameter can only be specified as a keyword parameter, and is mutually exclusive with _curve\_right_.

*   **curve_right** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – The amount to curve right while moving forwards, by driving the right motor at a slower speed. Maximum _curve\_right_ is 1, the default is 0 (no curve). This parameter can only be specified as a keyword parameter, and is mutually exclusive with _curve\_left_.

left(_speed=1_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#Robot.left)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Robot.left "Link to this definition")
Make the robot turn left by running the right motor forward and left motor backward.

Parameters:
**speed** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – Speed at which to drive the motors, as a value between 0 (stopped) and 1 (full speed). The default is 1.

reverse()[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#Robot.reverse)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Robot.reverse "Link to this definition")
Reverse the robot’s current motor directions. If the robot is currently running full speed forward, it will run full speed backward. If the robot is turning left at half-speed, it will turn right at half-speed. If the robot is currently stopped it will remain stopped.

right(_speed=1_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#Robot.right)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Robot.right "Link to this definition")
Make the robot turn right by running the left motor forward and right motor backward.

Parameters:
**speed** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – Speed at which to drive the motors, as a value between 0 (stopped) and 1 (full speed). The default is 1.

stop()[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#Robot.stop)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Robot.stop "Link to this definition")
Stop the robot.

_property_ value[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Robot.value "Link to this definition")
Represents the motion of the robot as a tuple of (left_motor_speed, right_motor_speed) with `(-1, -1)` representing full speed backwards, `(1, 1)` representing full speed forwards, and `(0, 0)` representing stopped.

### 17.1.21. PhaseEnableRobot[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#phaseenablerobot "Link to this heading")

_class_ gpiozero.PhaseEnableRobot(_left=None_, _right=None_, _pwm=True_, _pin\_factory=None_, _*args_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#PhaseEnableRobot)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.PhaseEnableRobot "Link to this definition")
Deprecated alias of [`Robot`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Robot "gpiozero.Robot"). The [`Robot`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Robot "gpiozero.Robot") class can now be constructed directly with [`Motor`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Motor "gpiozero.Motor") or [`PhaseEnableMotor`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PhaseEnableMotor "gpiozero.PhaseEnableMotor") classes.

### 17.1.22. RyanteckRobot[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#ryanteckrobot "Link to this heading")

_class_ gpiozero.RyanteckRobot(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#RyanteckRobot)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.RyanteckRobot "Link to this definition")
Extends [`Robot`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Robot "gpiozero.Robot") for the [Ryanteck motor controller board](https://uk.pi-supply.com/products/ryanteck-rtk-000-001-motor-controller-board-kit-raspberry-pi).

The Ryanteck MCB pins are fixed and therefore there’s no need to specify them when constructing this class. The following example drives the robot forward:

from gpiozero import RyanteckRobot

robot = RyanteckRobot()
robot.forward()

Parameters:
*   **pwm** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") (the default), construct [`PWMOutputDevice`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMOutputDevice "gpiozero.PWMOutputDevice") instances for the motor controller pins, allowing both direction and variable speed control. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)"), construct [`DigitalOutputDevice`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.DigitalOutputDevice "gpiozero.DigitalOutputDevice") instances, allowing only direction control.

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

### 17.1.23. CamJamKitRobot[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#camjamkitrobot "Link to this heading")

_class_ gpiozero.CamJamKitRobot(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#CamJamKitRobot)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.CamJamKitRobot "Link to this definition")
Extends [`Robot`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Robot "gpiozero.Robot") for the [CamJam #3 EduKit](http://camjam.me/?page_id=1035) motor controller board.

The CamJam robot controller pins are fixed and therefore there’s no need to specify them when constructing this class. The following example drives the robot forward:

from gpiozero import CamJamKitRobot

robot = CamJamKitRobot()
robot.forward()

Parameters:
*   **pwm** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") (the default), construct [`PWMOutputDevice`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMOutputDevice "gpiozero.PWMOutputDevice") instances for the motor controller pins, allowing both direction and variable speed control. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)"), construct [`DigitalOutputDevice`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.DigitalOutputDevice "gpiozero.DigitalOutputDevice") instances, allowing only direction control.

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

### 17.1.24. PololuDRV8835Robot[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#pololudrv8835robot "Link to this heading")

_class_ gpiozero.PololuDRV8835Robot(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#PololuDRV8835Robot)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.PololuDRV8835Robot "Link to this definition")
Extends [`Robot`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Robot "gpiozero.Robot") for the [Pololu DRV8835 Dual Motor Driver Kit](https://www.pololu.com/product/2753).

The Pololu DRV8835 pins are fixed and therefore there’s no need to specify them when constructing this class. The following example drives the robot forward:

from gpiozero import PololuDRV8835Robot

robot = PololuDRV8835Robot()
robot.forward()

Parameters:
*   **pwm** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") (the default), construct [`PWMOutputDevice`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMOutputDevice "gpiozero.PWMOutputDevice") instances for the motor controller’s enable pins, allowing both direction and variable speed control. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)"), construct [`DigitalOutputDevice`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.DigitalOutputDevice "gpiozero.DigitalOutputDevice") instances, allowing only direction control.

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

### 17.1.25. Energenie[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#energenie "Link to this heading")

_class_ gpiozero.Energenie(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#Energenie)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Energenie "Link to this definition")
Extends [`Device`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.Device "gpiozero.Device") to represent an [Energenie socket](https://energenie4u.co.uk/index.php/catalogue/product/ENER002-2PI) controller.

This class is constructed with a socket number and an optional initial state (defaults to [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)"), meaning off). Instances of this class can be used to switch peripherals on and off. For example:

from gpiozero import Energenie

lamp = Energenie(1)
lamp.on()

Parameters:
*   **socket** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")) – Which socket this instance should control. This is an integer number between 1 and 4.

*   **initial_value** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")_or_ _None_) – The initial state of the socket. As Energenie sockets provide no means of reading their state, you may provide an initial state for the socket, which will be set upon construction. This defaults to [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") which will switch the socket off. Specifying [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") will not set any initial state nor transmit any control signal to the device.

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

off()[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#Energenie.off)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Energenie.off "Link to this definition")
Turns the socket off.

on()[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#Energenie.on)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Energenie.on "Link to this definition")
Turns the socket on.

_property_ socket[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Energenie.socket "Link to this definition")
Returns the socket number.

_property_ value[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Energenie.value "Link to this definition")
Returns [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") if the socket is on and [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") if the socket is off. Setting this property changes the state of the socket. Returns [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") only when constructed with `initial_value` set to [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") and neither [`on()`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Energenie.on "gpiozero.Energenie.on") nor [`off()`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Energenie.off "gpiozero.Energenie.off") have been called since construction.

### 17.1.26. StatusZero[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#statuszero "Link to this heading")

_class_ gpiozero.StatusZero(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#StatusZero)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.StatusZero "Link to this definition")
Extends [`LEDBoard`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBoard "gpiozero.LEDBoard") for The Pi Hut’s [STATUS Zero](https://thepihut.com/statuszero): a Pi Zero sized add-on board with three sets of red/green LEDs to provide a status indicator.

The following example designates the first strip the label “wifi” and the second “raining”, and turns them green and red respectfully:

from gpiozero import StatusZero

status = StatusZero('wifi', 'raining')
status.wifi.green.on()
status.raining.red.on()

Each designated label will contain two [`LED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED "gpiozero.LED") objects named “red” and “green”.

Parameters:
*   ***labels** ([_str_](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)")) – Specify the names of the labels you wish to designate the strips to. You can list up to three labels. If no labels are given, three strips will be initialised with names ‘one’, ‘two’, and ‘three’. If some, but not all strips are given labels, any remaining strips will not be initialised.

*   **pwm** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"), construct [`PWMLED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED "gpiozero.PWMLED") instances to represent each LED. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") (the default), construct regular [`LED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED "gpiozero.LED") instances.

*   **initial_value** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") (the default), all LEDs will be off initially. If [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)"), each device will be left in whatever state the pin is found in when configured for output (warning: this can be on). If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"), the device will be switched on initially.

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

your-label-here,your-label-here,...
This entry represents one of the three labelled attributes supported on the STATUS Zero board. It is an [`LEDBoard`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBoard "gpiozero.LEDBoard") which contains:

red[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.StatusZero.red "Link to this definition")
The [`LED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED "gpiozero.LED") or [`PWMLED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED "gpiozero.PWMLED") representing the red LED next to the label.

green[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.StatusZero.green "Link to this definition")
The [`LED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED "gpiozero.LED") or [`PWMLED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED "gpiozero.PWMLED") representing the green LED next to the label.

### 17.1.27. StatusBoard[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#statusboard "Link to this heading")

_class_ gpiozero.StatusBoard(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#StatusBoard)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.StatusBoard "Link to this definition")
Extends [`CompositeOutputDevice`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.CompositeOutputDevice "gpiozero.CompositeOutputDevice") for The Pi Hut’s [STATUS](https://thepihut.com/status) board: a HAT sized add-on board with five sets of red/green LEDs and buttons to provide a status indicator with additional input.

The following example designates the first strip the label “wifi” and the second “raining”, turns the wifi green and then activates the button to toggle its lights when pressed:

from gpiozero import StatusBoard

status = StatusBoard('wifi', 'raining')
status.wifi.lights.green.on()
status.wifi.button.when_pressed = status.wifi.lights.toggle

Each designated label will contain a “lights” [`LEDBoard`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBoard "gpiozero.LEDBoard") containing two [`LED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED "gpiozero.LED") objects named “red” and “green”, and a [`Button`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button "gpiozero.Button") object named “button”.

Parameters:
*   ***labels** ([_str_](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)")) – Specify the names of the labels you wish to designate the strips to. You can list up to five labels. If no labels are given, five strips will be initialised with names ‘one’ to ‘five’. If some, but not all strips are given labels, any remaining strips will not be initialised.

*   **pwm** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"), construct [`PWMLED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED "gpiozero.PWMLED") instances to represent each LED. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") (the default), construct regular [`LED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED "gpiozero.LED") instances.

*   **initial_value** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") (the default), all LEDs will be off initially. If [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)"), each device will be left in whatever state the pin is found in when configured for output (warning: this can be on). If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"), the device will be switched on initially.

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

your-label-here,your-label-here,...
This entry represents one of the five labelled attributes supported on the STATUS board. It is an [`CompositeOutputDevice`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.CompositeOutputDevice "gpiozero.CompositeOutputDevice") which contains:

lights[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.StatusBoard.lights "Link to this definition")
A [`LEDBoard`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBoard "gpiozero.LEDBoard") representing the lights next to the label. It contains:

red[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.StatusBoard.red "Link to this definition")
The [`LED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED "gpiozero.LED") or [`PWMLED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED "gpiozero.PWMLED") representing the red LED next to the label.

green[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.StatusBoard.green "Link to this definition")
The [`LED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED "gpiozero.LED") or [`PWMLED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED "gpiozero.PWMLED") representing the green LED next to the label.

button[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.StatusBoard.button "Link to this definition")
A [`Button`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button "gpiozero.Button") representing the button next to the label.

### 17.1.28. SnowPi[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#snowpi "Link to this heading")

_class_ gpiozero.SnowPi(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#SnowPi)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.SnowPi "Link to this definition")
Extends [`LEDBoard`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBoard "gpiozero.LEDBoard") for the [Ryanteck SnowPi](https://ryanteck.uk/raspberry-pi/114-snowpi-the-gpio-snowman-for-raspberry-pi-0635648608303.html) board.

The SnowPi pins are fixed and therefore there’s no need to specify them when constructing this class. The following example turns on the eyes, sets the nose pulsing, and the arms blinking:

from gpiozero import SnowPi

snowman = SnowPi(pwm=True)
snowman.eyes.on()
snowman.nose.pulse()
snowman.arms.blink()

Parameters:
*   **pwm** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"), construct [`PWMLED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED "gpiozero.PWMLED") instances to represent each LED. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") (the default), construct regular [`LED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED "gpiozero.LED") instances.

*   **initial_value** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") (the default), all LEDs will be off initially. If [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)"), each device will be left in whatever state the pin is found in when configured for output (warning: this can be on). If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"), the device will be switched on initially.

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

arms[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.SnowPi.arms "Link to this definition")
A [`LEDBoard`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBoard "gpiozero.LEDBoard") representing the arms of the snow man. It contains the following attributes:

left,right
Two [`LEDBoard`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBoard "gpiozero.LEDBoard") objects representing the left and right arms of the snow-man. They contain:

top,middle,bottom
The [`LED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED "gpiozero.LED") or [`PWMLED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED "gpiozero.PWMLED") down the snow-man’s arms.

eyes[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.SnowPi.eyes "Link to this definition")
A [`LEDBoard`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBoard "gpiozero.LEDBoard") representing the eyes of the snow-man. It contains:

left,right
The [`LED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED "gpiozero.LED") or [`PWMLED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED "gpiozero.PWMLED") for the snow-man’s eyes.

nose[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.SnowPi.nose "Link to this definition")
The [`LED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED "gpiozero.LED") or [`PWMLED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED "gpiozero.PWMLED") for the snow-man’s nose.

### 17.1.29. PumpkinPi[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#pumpkinpi "Link to this heading")

_class_ gpiozero.PumpkinPi(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#PumpkinPi)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.PumpkinPi "Link to this definition")
Extends [`LEDBoard`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBoard "gpiozero.LEDBoard") for the [ModMyPi PumpkinPi](https://www.modmypi.com/halloween-pumpkin-programmable-kit) board.

There are twelve LEDs connected up to individual pins, so for the PumpkinPi the pins are fixed. For example:

from gpiozero import PumpkinPi

pumpkin = PumpkinPi(pwm=True)
pumpkin.sides.pulse()
pumpkin.off()

Parameters:
*   **pwm** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"), construct [`PWMLED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED "gpiozero.PWMLED") instances to represent each LED. If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") (the default), construct regular [`LED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED "gpiozero.LED") instances

*   **initial_value** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")_or_ _None_) – If [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") (the default), all LEDs will be off initially. If [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)"), each device will be left in whatever state the pin is found in when configured for output (warning: this can be on). If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"), the device will be switched on initially.

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

sides[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.PumpkinPi.sides "Link to this definition")
A [`LEDBoard`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBoard "gpiozero.LEDBoard") representing the LEDs around the edge of the pumpkin. It contains:

left,right
Two [`LEDBoard`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBoard "gpiozero.LEDBoard") instances representing the LEDs on the left and right sides of the pumpkin. They each contain:

top,midtop,middle,midbottom,bottom
Each [`LED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED "gpiozero.LED") or [`PWMLED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED "gpiozero.PWMLED") around the specified side of the pumpkin.

eyes[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.PumpkinPi.eyes "Link to this definition")
A [`LEDBoard`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBoard "gpiozero.LEDBoard") representing the eyes of the pumpkin. It contains:

left,right
The [`LED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED "gpiozero.LED") or [`PWMLED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PWMLED "gpiozero.PWMLED") for each of the pumpkin’s eyes.

17.2. Base Classes[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#base-classes "Link to this heading")
--------------------------------------------------------------------------------------------------------------------

The classes in the sections above are derived from a series of base classes, some of which are effectively abstract. The classes form the (partial) hierarchy displayed in the graph below:

![Image 1: _images/composite_device_hierarchy.svg](https://gpiozero.readthedocs.io/en/stable/_images/composite_device_hierarchy.svg)
For composite devices, the following chart shows which devices are composed of which other devices:

![Image 2: _images/composed_devices.svg](https://gpiozero.readthedocs.io/en/stable/_images/composed_devices.svg)
The following sections document these base classes for advanced users that wish to construct classes for their own devices.

### 17.2.1. LEDCollection[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#ledcollection "Link to this heading")

_class_ gpiozero.LEDCollection(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#LEDCollection)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDCollection "Link to this definition")
Extends [`CompositeOutputDevice`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.CompositeOutputDevice "gpiozero.CompositeOutputDevice"). Abstract base class for [`LEDBoard`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBoard "gpiozero.LEDBoard") and [`LEDBarGraph`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDBarGraph "gpiozero.LEDBarGraph").

_property_ is_lit[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDCollection.is_lit "Link to this definition")
Composite devices are considered “active” if any of their constituent devices have a “truthy” value.

_property_ leds[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.LEDCollection.leds "Link to this definition")
A flat tuple of all LEDs contained in this collection (and all sub-collections).

### 17.2.2. CompositeOutputDevice[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#compositeoutputdevice "Link to this heading")

_class_ gpiozero.CompositeOutputDevice(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#CompositeOutputDevice)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.CompositeOutputDevice "Link to this definition")
Extends [`CompositeDevice`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.CompositeDevice "gpiozero.CompositeDevice") with [`on()`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.CompositeOutputDevice.on "gpiozero.CompositeOutputDevice.on"), [`off()`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.CompositeOutputDevice.off "gpiozero.CompositeOutputDevice.off"), and [`toggle()`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.CompositeOutputDevice.toggle "gpiozero.CompositeOutputDevice.toggle") methods for controlling subordinate output devices. Also extends [`value`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.CompositeOutputDevice.value "gpiozero.CompositeOutputDevice.value") to be writeable.

Parameters:
*   ***args** ([_Device_](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.Device "gpiozero.Device")) – The un-named devices that belong to the composite device. The [`value`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.Device.value "gpiozero.Device.value") attributes of these devices will be represented within the composite device’s tuple [`value`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.CompositeOutputDevice.value "gpiozero.CompositeOutputDevice.value") in the order specified here.

*   **_order** ([_list_](https://docs.python.org/3.9/library/stdtypes.html#list "(in Python v3.9)")_or_ _None_) – If specified, this is the order of named items specified by keyword arguments (to ensure that the [`value`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.CompositeOutputDevice.value "gpiozero.CompositeOutputDevice.value") tuple is constructed with a specific order). All keyword arguments _must_ be included in the collection. If omitted, an alphabetically sorted order will be selected for keyword arguments.

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

*   ****kwargs** ([_Device_](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.Device "gpiozero.Device")) – The named devices that belong to the composite device. These devices will be accessible as named attributes on the resulting device, and their [`value`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.CompositeOutputDevice.value "gpiozero.CompositeOutputDevice.value") attributes will be accessible as named elements of the composite device’s tuple [`value`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.CompositeOutputDevice.value "gpiozero.CompositeOutputDevice.value").

off()[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#CompositeOutputDevice.off)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.CompositeOutputDevice.off "Link to this definition")
Turn all the output devices off.

on()[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#CompositeOutputDevice.on)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.CompositeOutputDevice.on "Link to this definition")
Turn all the output devices on.

toggle()[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/boards.html#CompositeOutputDevice.toggle)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.CompositeOutputDevice.toggle "Link to this definition")
Toggle all the output devices. For each device, if it’s on, turn it off; if it’s off, turn it on.

_property_ value[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.CompositeOutputDevice.value "Link to this definition")
A tuple containing a value for each subordinate device. This property can also be set to update the state of all subordinate output devices.

### 17.2.3. CompositeDevice[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#compositedevice "Link to this heading")

_class_ gpiozero.CompositeDevice(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/devices.html#CompositeDevice)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.CompositeDevice "Link to this definition")
Extends [`Device`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.Device "gpiozero.Device"). Represents a device composed of multiple devices like simple HATs, H-bridge motor controllers, robots composed of multiple motors, etc.

The constructor accepts subordinate devices as positional or keyword arguments. Positional arguments form unnamed devices accessed by treating the composite device as a container, while keyword arguments are added to the device as named (read-only) attributes.

For example:

>>> from gpiozero import *
>>> d = CompositeDevice(LED(2), LED(3), LED(4), btn=Button(17))
>>> d[0]
<gpiozero.LED object on pin GPIO2, active_high=True, is_active=False>
>>> d[1]
<gpiozero.LED object on pin GPIO3, active_high=True, is_active=False>
>>> d[2]
<gpiozero.LED object on pin GPIO4, active_high=True, is_active=False>
>>> d.btn
<gpiozero.Button object on pin GPIO17, pull_up=True, is_active=False>
>>> d.value
CompositeDeviceValue(device_0=False, device_1=False, device_2=False, btn=False)

Parameters:
*   ***args** ([_Device_](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.Device "gpiozero.Device")) – The un-named devices that belong to the composite device. The [`value`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.CompositeDevice.value "gpiozero.CompositeDevice.value") attributes of these devices will be represented within the composite device’s tuple [`value`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.CompositeDevice.value "gpiozero.CompositeDevice.value") in the order specified here.

*   **_order** ([_list_](https://docs.python.org/3.9/library/stdtypes.html#list "(in Python v3.9)")_or_ _None_) – If specified, this is the order of named items specified by keyword arguments (to ensure that the [`value`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.CompositeDevice.value "gpiozero.CompositeDevice.value") tuple is constructed with a specific order). All keyword arguments _must_ be included in the collection. If omitted, an alphabetically sorted order will be selected for keyword arguments.

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

*   ****kwargs** ([_Device_](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.Device "gpiozero.Device")) – The named devices that belong to the composite device. These devices will be accessible as named attributes on the resulting device, and their [`value`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.CompositeDevice.value "gpiozero.CompositeDevice.value") attributes will be accessible as named elements of the composite device’s tuple [`value`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.CompositeDevice.value "gpiozero.CompositeDevice.value").

close()[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/devices.html#CompositeDevice.close)[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.CompositeDevice.close "Link to this definition")
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

_property_ closed[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.CompositeDevice.closed "Link to this definition")
Returns [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") if the device is closed (see the [`close()`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.CompositeDevice.close "gpiozero.CompositeDevice.close") method). Once a device is closed you can no longer use any other methods or properties to control or query the device.

_property_ is_active[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.CompositeDevice.is_active "Link to this definition")
Composite devices are considered “active” if any of their constituent devices have a “truthy” value.

_property_ namedtuple[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.CompositeDevice.namedtuple "Link to this definition")
The [`namedtuple()`](https://docs.python.org/3.9/library/collections.html#collections.namedtuple "(in Python v3.9)") type constructed to represent the value of the composite device. The [`value`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.CompositeDevice.value "gpiozero.CompositeDevice.value") attribute returns values of this type.

_property_ value[](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.CompositeDevice.value "Link to this definition")
A [`namedtuple()`](https://docs.python.org/3.9/library/collections.html#collections.namedtuple "(in Python v3.9)") containing a value for each subordinate device. Devices with names will be represented as named elements. Unnamed devices will have a unique name generated for them, and they will appear in the position they appeared in the constructor.
