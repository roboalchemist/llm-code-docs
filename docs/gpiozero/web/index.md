# Source: https://gpiozero.readthedocs.io/

Title: gpiozero — gpiozero 2.0.1 Documentation

URL Source: https://gpiozero.readthedocs.io/

Markdown Content:
A simple interface to GPIO devices with [Raspberry Pi](https://www.raspberrypi.org/), developed and maintained by [Ben Nuttall](https://github.com/bennuttall) and [Dave Jones](https://github.com/waveform80).

About[](https://gpiozero.readthedocs.io/#about "Link to this heading")
-----------------------------------------------------------------------

Component interfaces are provided to allow a frictionless way to get started with physical computing:

from gpiozero import LED
from time import sleep

led = LED(17)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)

With very little code, you can quickly get going connecting your components together:

from gpiozero import LED, Button
from signal import pause

led = LED(17)
button = Button(3)

button.when_pressed = led.on
button.when_released = led.off

pause()

You can advance to using the declarative paradigm along with provided to describe the behaviour of devices and their interactions:

from gpiozero import OutputDevice, MotionSensor, LightSensor
from gpiozero.tools import booleanized, all_values
from signal import pause

garden = OutputDevice(17)
motion = MotionSensor(4)
light = LightSensor(5)

garden.source = all_values(booleanized(light, 0, 0.1), motion)

pause()

See the chapter on [Source/Values](https://gpiozero.readthedocs.io/en/stable/source_values.html) for more information.

The library includes interfaces to many simple everyday components, as well as some more complex things like sensors, analogue-to-digital converters, full colour LEDs, robotics kits and more. See the [Recipes](https://gpiozero.readthedocs.io/en/stable/recipes.html) chapter of the documentation for ideas on how to get started.

Pin factories[](https://gpiozero.readthedocs.io/#pin-factories "Link to this heading")
---------------------------------------------------------------------------------------

GPIO Zero builds on a number of underlying pin libraries, including [RPi.GPIO](https://pypi.org/project/RPi.GPIO) and [pigpio](https://pypi.org/project/pigpio), each with their own benefits. You can select a particular pin library to be used, either for the whole script or per-device, according to your needs. See the section on [changing the pin factory](https://gpiozero.readthedocs.io/en/stable/api_pins.html#changing-the-pin-factory).

A “mock pin” interface is also provided for testing purposes. Read more about this in the section on [mock pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html#mock-pins).

Installation[](https://gpiozero.readthedocs.io/#installation "Link to this heading")
-------------------------------------------------------------------------------------

GPIO Zero is installed by default in the Raspberry Pi OS desktop image, available from [raspberrypi.org](https://www.raspberrypi.org/software/). To install on Raspberry Pi OS Lite or other operating systems, including for PCs using remote GPIO, see the [Installing](https://gpiozero.readthedocs.io/en/stable/installing.html) chapter.

Documentation[](https://gpiozero.readthedocs.io/#documentation "Link to this heading")
---------------------------------------------------------------------------------------

Comprehensive documentation is available at [https://gpiozero.readthedocs.io/](https://gpiozero.readthedocs.io/). Please refer to the [Contributing](https://gpiozero.readthedocs.io/en/stable/contributing.html) and [Development](https://gpiozero.readthedocs.io/en/stable/development.html) chapters in the documentation for information on contributing to the project.

Issues and questions[](https://gpiozero.readthedocs.io/#issues-and-questions "Link to this heading")
-----------------------------------------------------------------------------------------------------

If you have a feature request or bug report, please open an [issue on GitHub](https://github.com/gpiozero/gpiozero/issues/new). If you have a question or need help, this may be better suited to our [GitHub discussion board](https://github.com/gpiozero/gpiozero/discussions), the [Raspberry Pi Stack Exchange](https://raspberrypi.stackexchange.com/) or the [Raspberry Pi Forums](https://www.raspberrypi.org/forums/).

Contributors[](https://gpiozero.readthedocs.io/#contributors "Link to this heading")
-------------------------------------------------------------------------------------

*   [Alex Chan](https://github.com/gpiozero/gpiozero/commits?author=alexwlchan)

*   [Alex Eames](https://github.com/gpiozero/gpiozero/commits?author=raspitv)

*   [Andrew Scheller](https://github.com/gpiozero/gpiozero/commits?author=lurch)

*   [Barry Byford](https://github.com/gpiozero/gpiozero/commits?author=ukBaz)

*   [Cameron Davidson-Pilon](https://github.com/gpiozero/gpiozero/commits?author=CamDavidsonPilon)

*   [Carl Monk](https://github.com/gpiozero/gpiozero/commits?author=ForToffee)

*   [Claire Pollard](https://github.com/gpiozero/gpiozero/commits?author=tuftii)

*   [Clare Macrae](https://github.com/gpiozero/gpiozero/commits?author=claremacrae)

*   [Dan Jackson](https://github.com/gpiozero/gpiozero/commits?author=e28eta)

*   [Daniele Procida](https://github.com/evildmp)

*   [damosurfer](https://github.com/gpiozero/gpiozero/commits?author=damosurfer)

*   [David Glaude](https://github.com/gpiozero/gpiozero/commits?author=dglaude)

*   [Delcio Torres](https://github.com/gpiozero/gpiozero/commits?author=delciotorres)

*   [Edward Betts](https://github.com/gpiozero/gpiozero/commits?author=edwardbetts)

*   [Fatih Sarhan](https://github.com/gpiozero/gpiozero/commits?author=f9n)

*   [Fangchen Li](https://github.com/gpiozero/gpiozero/commits?author=fangchenli)

*   [G.S.](https://github.com/gpiozero/gpiozero/commits?author=gszy)

*   [gnicki](https://github.com/gpiozero/gpiozero/commits?author=gnicki2000)

*   [Ian Harcombe](https://github.com/gpiozero/gpiozero/commits?author=MrHarcombe)

*   [Jack Wearden](https://github.com/gpiozero/gpiozero/commits?author=NotBobTheBuilder)

*   [Jeevan M R](https://github.com/gpiozero/gpiozero/commits?author=jee1mr)

*   [Josh Thorpe](https://github.com/gpiozero/gpiozero/commits?author=ThorpeJosh)

*   [Kyle Morgan](https://github.com/gpiozero/gpiozero/commits?author=knmorgan)

*   [Linus Groh](https://github.com/gpiozero/gpiozero/commits?author=linusg)

*   [Mahallon](https://github.com/gpiozero/gpiozero/commits?author=Mahallon)

*   [Maksim Levental](https://github.com/gpiozero/gpiozero/commits?author=makslevental)

*   [Martchus](https://github.com/gpiozero/gpiozero/commits?author=Martchus)

*   [Martin O’Hanlon](https://github.com/martinohanlon/commits?author=martinohanlon)

*   [Mike Kazantsev](https://github.com/gpiozero/gpiozero/commits?author=mk-fg)

*   [Paulo Mateus](https://github.com/gpiozero/gpiozero/commits?author=SrMouraSilva)

*   [Phil Howard](https://github.com/gpiozero/gpiozero/commits?author=Gadgetoid)

*   [Philippe Muller](https://github.com/gpiozero/gpiozero/commits?author=pmuller)

*   [Rick Ansell](https://github.com/gpiozero/gpiozero/commits?author=ricksbt)

*   [Rimas Misevičius](https://github.com/gpiozero/gpiozero/commits?author=rmisev)

*   [Robert Erdin](https://github.com/gpiozero/gpiozero/commits?author=roberterdin)

*   [Russel Winder](https://github.com/russel)

*   [Ryan Walmsley](https://github.com/gpiozero/gpiozero/commits?author=ryanteck)

*   [Schelto van Doorn](https://github.com/gpiozero/gpiozero/commits?author=goloplo)

*   [Sofiia Kosovan](https://github.com/gpiozero/gpiozero/commits?author=SofiiaKosovan)

*   [Steve Amor](https://github.com/gpiozero/gpiozero/commits?author=SteveAmor)

*   [Stewart Adcock](https://github.com/gpiozero/gpiozero/commits?author=stewartadcock)

*   [Thijs Triemstra](https://github.com/gpiozero/gpiozero/commits?author=thijstriemstra)

*   [Tim Golden](https://github.com/gpiozero/gpiozero/commits?author=tjguk)

*   [Yisrael Dov Lebow](https://github.com/gpiozero/gpiozero/commits?author=yisraeldov)

See the [contributors page](https://github.com/gpiozero/gpiozero/graphs/contributors) on GitHub for more info.

Table of Contents[](https://gpiozero.readthedocs.io/#table-of-contents "Link to this heading")
-----------------------------------------------------------------------------------------------

*   [1. Installing GPIO Zero](https://gpiozero.readthedocs.io/en/stable/installing.html)
*   [2. Basic Recipes](https://gpiozero.readthedocs.io/en/stable/recipes.html)
*   [3. Advanced Recipes](https://gpiozero.readthedocs.io/en/stable/recipes_advanced.html)
*   [4. Configuring Remote GPIO](https://gpiozero.readthedocs.io/en/stable/remote_gpio.html)
*   [5. Remote GPIO Recipes](https://gpiozero.readthedocs.io/en/stable/recipes_remote_gpio.html)
*   [6. Pi Zero USB OTG](https://gpiozero.readthedocs.io/en/stable/pi_zero_otg.html)
*   [7. Source/Values](https://gpiozero.readthedocs.io/en/stable/source_values.html)
*   [8. Command-line Tools](https://gpiozero.readthedocs.io/en/stable/cli_tools.html)
*   [9. Frequently Asked Questions](https://gpiozero.readthedocs.io/en/stable/faq.html)
*   [10. Backwards Compatibility](https://gpiozero.readthedocs.io/en/stable/compat.html)
*   [11. Migrating from RPi.GPIO](https://gpiozero.readthedocs.io/en/stable/migrating_from_rpigpio.html)
*   [12. Contributing](https://gpiozero.readthedocs.io/en/stable/contributing.html)
*   [13. Development](https://gpiozero.readthedocs.io/en/stable/development.html)
*   [14. API - Input Devices](https://gpiozero.readthedocs.io/en/stable/api_input.html)
*   [15. API - Output Devices](https://gpiozero.readthedocs.io/en/stable/api_output.html)
*   [16. API - SPI Devices](https://gpiozero.readthedocs.io/en/stable/api_spi.html)
*   [17. API - Boards and Accessories](https://gpiozero.readthedocs.io/en/stable/api_boards.html)
*   [18. API - Internal Devices](https://gpiozero.readthedocs.io/en/stable/api_internal.html)
*   [19. API - Generic Classes](https://gpiozero.readthedocs.io/en/stable/api_generic.html)
*   [20. API - Device Source Tools](https://gpiozero.readthedocs.io/en/stable/api_tools.html)
*   [21. API - Fonts](https://gpiozero.readthedocs.io/en/stable/api_fonts.html)
*   [22. API - Tones](https://gpiozero.readthedocs.io/en/stable/api_tones.html)
*   [23. API - Pi Information](https://gpiozero.readthedocs.io/en/stable/api_info.html)
*   [24. API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html)
*   [25. API - Exceptions](https://gpiozero.readthedocs.io/en/stable/api_exc.html)
*   [26. Changelog](https://gpiozero.readthedocs.io/en/stable/changelog.html)
*   [27. License](https://gpiozero.readthedocs.io/en/stable/license.html)

Indices and tables[](https://gpiozero.readthedocs.io/#indices-and-tables "Link to this heading")
-------------------------------------------------------------------------------------------------

*   [Index](https://gpiozero.readthedocs.io/en/stable/genindex.html)

*   [Module Index](https://gpiozero.readthedocs.io/en/stable/py-modindex.html)

*   [Search Page](https://gpiozero.readthedocs.io/en/stable/search.html)
