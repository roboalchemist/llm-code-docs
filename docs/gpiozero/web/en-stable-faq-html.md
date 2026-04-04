# Source: https://gpiozero.readthedocs.io/en/stable/faq.html

Title: 9. Frequently Asked Questions — gpiozero 2.0.1 Documentation

URL Source: https://gpiozero.readthedocs.io/en/stable/faq.html

Markdown Content:
9.1. How do I keep my script running?[](https://gpiozero.readthedocs.io/en/stable/faq.html#how-do-i-keep-my-script-running "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------

The following script looks like it should turn an [`LED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED "gpiozero.LED") on:

from gpiozero import LED

led = LED(17)
led.on()

And it does, if you’re using the Python or IPython shell, or the IDLE, Thonny or Mu editors. However, if you saved this script as a Python file and ran it, it would flash on briefly, then the script would end and it would turn off.

The following file includes an intentional [`pause()`](https://docs.python.org/3.9/library/signal.html#signal.pause "(in Python v3.9)") to keep the script alive:

from gpiozero import LED
from signal import pause

led = LED(17)
led.on()

pause()

Now the script will stay running, leaving the LED on, until it is terminated manually (e.g. by pressing Ctrl+C). Similarly, when setting up callbacks on button presses or other input devices, the script needs to be running for the events to be detected:

from gpiozero import Button
from signal import pause

def hello():
    print("Hello")

button = Button(2)
button.when_pressed = hello

pause()

9.2. What’s the difference between when_pressed, is_pressed and wait_for_press?[](https://gpiozero.readthedocs.io/en/stable/faq.html#what-s-the-difference-between-when-pressed-is-pressed-and-wait-for-press "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

gpiozero provides a range of different approaches to reading input devices. Sometimes you want to ask if a button’s pressed, sometimes you want to do something until it’s pressed, and sometimes you want something to happen _when_ it’s been pressed, regardless of what else is going on.

In a simple example where the button is the only device in play, all of the options would be equally effective. But as soon as you introduce an extra element, like another GPIO device, you might need to choose the right approach depending on your use case.

*   [`is_pressed`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button.is_pressed "gpiozero.Button.is_pressed") is an attribute which reveals whether the button is currently pressed by returning `True` or `False`:

while True:
    if btn.is_pressed:
        print("Pressed")
    else:
        print("Not pressed") 
*   [`wait_for_press()`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button.wait_for_press "gpiozero.Button.wait_for_press") is a method which blocks the code from continuing until the button is pressed. Also see [`wait_for_release()`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button.wait_for_release "gpiozero.Button.wait_for_release"):

while True:
    print("Released. Waiting for press..")
    btn.wait_for_press()
    print("Pressed. Waiting for release...")
    btn.wait_for_release() 
*   [`when_pressed`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button.when_pressed "gpiozero.Button.when_pressed") is an attribute which assigns a callback function to the event of the button being pressed. Every time the button is pressed, the callback function is executed in a separate thread. Also see [`when_released`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button.when_released "gpiozero.Button.when_released"):

def pressed():
    print("Pressed")

def released():
    print("Released")

btn.when_pressed = pressed
btn.when_released = released 

This pattern of options is common among many devices. All [input devices](https://gpiozero.readthedocs.io/en/stable/api_input.html) and [internal devices](https://gpiozero.readthedocs.io/en/stable/api_internal.html) have `is_active`, `when_activated`, `when_deactivated`, `wait_for_active` and `wait_for_inactive`, and many provide aliases (such as “pressed” for “activated”).

Also see a more advanced approach in the [Source/Values](https://gpiozero.readthedocs.io/en/stable/source_values.html) page.

9.3. My event handler isn’t being called[](https://gpiozero.readthedocs.io/en/stable/faq.html#my-event-handler-isn-t-being-called "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------

When assigning event handlers, don’t call the function you’re assigning. For example:

from gpiozero import Button

def pushed():
    print("Don't push the button!")

b = Button(17)
b.when_pressed = pushed()

In the case above, when assigning to [`when_pressed`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button.when_pressed "gpiozero.Button.when_pressed"), the thing that is assigned is the _result of calling_ the `pushed` function. Because `pushed` doesn’t explicitly return anything, the result is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)"). Hence this is equivalent to doing:

b.when_pressed = None

This doesn’t raise an error because it’s perfectly valid: it’s what you assign when you don’t want the event handler to do anything. Instead, you want to do the following:

b.when_pressed = pushed

This will assign the function to the event handler _without calling it_. This is the crucial difference between `my_function` (a reference to a function) and `my_function()` (the result of calling a function).

Note

Note that as of v1.5, setting a callback to [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") when it was previously [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") will raise a [`CallbackSetToNone`](https://gpiozero.readthedocs.io/en/stable/api_exc.html#gpiozero.CallbackSetToNone "gpiozero.CallbackSetToNone") warning, with the intention of alerting users when callbacks are set to [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") accidentally. However, if this is intentional, the warning can be suppressed. See the [`warnings`](https://docs.python.org/3.9/library/warnings.html#module-warnings "(in Python v3.9)") module for reference.

9.4. Why do I get PinFactoryFallback warnings when I import gpiozero?[](https://gpiozero.readthedocs.io/en/stable/faq.html#why-do-i-get-pinfactoryfallback-warnings-when-i-import-gpiozero "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You are most likely working in a virtual Python environment and have forgotten to install a pin driver library like `RPi.GPIO`. GPIO Zero relies upon lower level pin drivers to handle interfacing to the GPIO pins on the Raspberry Pi, so you can eliminate the warning simply by installing GPIO Zero’s first preference:

$ pip install rpi.gpio

When GPIO Zero is imported it attempts to find a pin driver by importing them in a preferred order (detailed in [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html)). If it fails to load its first preference (`RPi.GPIO`) it notifies you with a warning, then falls back to trying its second preference and so on. Eventually it will fall back all the way to the `native` implementation. This is a pure Python implementation built into GPIO Zero itself. While this will work for most things it’s almost certainly not what you want (it doesn’t support PWM, and it’s quite slow at certain things).

If you want to use a pin driver other than the default, and you want to suppress the warnings you’ve got a couple of options:

1.   Explicitly specify what pin driver you want via the [`GPIOZERO_PIN_FACTORY`](https://gpiozero.readthedocs.io/en/stable/cli_env.html#envvar-GPIOZERO_PIN_FACTORY) environment variable. For example:

$ GPIOZERO_PIN_FACTORY=pigpio python3 
In this case no warning is issued because there’s no fallback; either the specified factory loads or it fails in which case an [`ImportError`](https://docs.python.org/3.9/library/exceptions.html#ImportError "(in Python v3.9)") will be raised.

2.   Suppress the warnings and let the fallback mechanism work:

>>> import warnings
>>> warnings.simplefilter('ignore')
>>> import gpiozero 
Refer to the [`warnings`](https://docs.python.org/3.9/library/warnings.html#module-warnings "(in Python v3.9)") module documentation for more refined ways to filter out specific warning classes.

9.5. How can I tell what version of gpiozero I have installed?[](https://gpiozero.readthedocs.io/en/stable/faq.html#how-can-i-tell-what-version-of-gpiozero-i-have-installed "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The gpiozero library relies on the setuptools package for installation services. You can use the setuptools `pkg_resources` API to query which version of gpiozero is available in your Python environment like so:

>>> from pkg_resources import require
>>> require('gpiozero')
[gpiozero 1.6.2 (/usr/lib/python3/dist-packages)]
>>> require('gpiozero')[0].version
'1.6.2'

If you have multiple versions installed (e.g. from **pip** and **apt**) they will not show up in the list returned by the `pkg_resources.require()` method. However, the first entry in the list will be the version that `import gpiozero` will import.

If you receive the error “No module named pkg_resources”, you need to install **pip**. This can be done with the following command in Raspberry Pi OS:

$ sudo apt install python3-pip

Alternatively, install pip with [get-pip](https://pip.pypa.io/en/stable/installing/).

9.6. Why do I get “command not found” when running pinout?[](https://gpiozero.readthedocs.io/en/stable/faq.html#why-do-i-get-command-not-found-when-running-pinout "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The gpiozero library is available as a Debian package for Python 2 and Python 3, but the [pinout](https://gpiozero.readthedocs.io/en/stable/cli_pinout.html) tool cannot be made available by both packages, so it’s only included with the Python 3 version of the package. To make sure the [pinout](https://gpiozero.readthedocs.io/en/stable/cli_pinout.html) tool is available, the “python3-gpiozero” package must be installed:

$ sudo apt install python3-gpiozero

Alternatively, installing gpiozero using **pip** will install the command line tool, regardless of Python version:

$ sudo pip3 install gpiozero

or:

$ sudo pip install gpiozero

9.7. The pinout command line tool incorrectly identifies my Raspberry Pi model[](https://gpiozero.readthedocs.io/en/stable/faq.html#the-pinout-command-line-tool-incorrectly-identifies-my-raspberry-pi-model "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If your Raspberry Pi model is new, it’s possible it wasn’t known about at the time of the gpiozero release you are using. Ensure you have the latest version installed (remember, the [pinout](https://gpiozero.readthedocs.io/en/stable/cli_pinout.html) tool usually comes from the Python 3 version of the package as noted in the previous FAQ).

If the Pi model you are using isn’t known to gpiozero, it may have been added since the last release. You can check the [GitHub issues](https://github.com/gpiozero/gpiozero/issues) to see if it’s been reported before, or check the [commits](https://github.com/gpiozero/gpiozero/commits/master) on GitHub since the last release to see if it’s been added. The model determination can be found in `gpiozero/pins/data.py`.

9.8. What’s the gpiozero equivalent of GPIO.cleanup()?[](https://gpiozero.readthedocs.io/en/stable/faq.html#what-s-the-gpiozero-equivalent-of-gpio-cleanup "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Many people ask how to do the equivalent of the `cleanup` function from `RPi.GPIO`. In gpiozero, at the end of your script, cleanup is run automatically, restoring your GPIO pins to the state they were found.

To explicitly close a connection to a pin, you can manually call the [`close()`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.Device.close "gpiozero.Device.close") method on a device object:

>>> led = LED(2)
>>> led.on()
>>> led
<gpiozero.LED object on pin GPIO2, active_high=True, is_active=True>
>>> led.close()
>>> led
<gpiozero.LED object closed>

This means that you can reuse the pin for another device, and that despite turning the LED on (and hence, the pin high), after calling [`close()`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.Device.close "gpiozero.Device.close") it is restored to its previous state (LED off, pin low).

Read more about [Migrating from RPi.GPIO](https://gpiozero.readthedocs.io/en/stable/migrating_from_rpigpio.html#migrating-from-rpigpio).

9.9. How do I use button.when_pressed and button.when_held together?[](https://gpiozero.readthedocs.io/en/stable/faq.html#how-do-i-use-button-when-pressed-and-button-when-held-together "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The [`Button`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button "gpiozero.Button") class provides a [`when_held`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button.when_held "gpiozero.Button.when_held") property which is used to set a callback for when the button is held down for a set amount of time (as determined by the [`hold_time`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button.hold_time "gpiozero.Button.hold_time") property). If you want to set [`when_held`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button.when_held "gpiozero.Button.when_held") as well as [`when_pressed`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button.when_pressed "gpiozero.Button.when_pressed"), you’ll notice that both callbacks will fire. Sometimes, this is acceptable, but often you’ll want to only fire the [`when_pressed`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button.when_pressed "gpiozero.Button.when_pressed") callback when the button has not been held, only pressed.

The way to achieve this is to _not_ set a callback on [`when_pressed`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button.when_pressed "gpiozero.Button.when_pressed"), and instead use [`when_released`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button.when_released "gpiozero.Button.when_released") to work out whether it had been held or just pressed:

from gpiozero import Button

Button.was_held = False

def held(btn):
    btn.was_held = True
    print("button was held not just pressed")

def released(btn):
    if not btn.was_held:
        pressed()
    btn.was_held = False

def pressed():
    print("button was pressed not held")

btn = Button(2)

btn.when_held = held
btn.when_released = released

9.10. Why do I get “ImportError: cannot import name” when trying to import from gpiozero?[](https://gpiozero.readthedocs.io/en/stable/faq.html#why-do-i-get-importerror-cannot-import-name-when-trying-to-import-from-gpiozero "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

It’s common to see people name their first gpiozero script `gpiozero.py`. Unfortunately, this will cause your script to try to import itself, rather than the gpiozero library from the libraries path. You’ll see an error like this:

Traceback (most recent call last):
  File "gpiozero.py", line 1, in <module>
    from gpiozero import LED
  File "/home/pi/gpiozero.py", line 1, in <module>
    from gpiozero import LED
ImportError: cannot import name 'LED'

Simply rename your script to something else, and run it again. Be sure not to name any of your scripts the same name as a Python module you may be importing, such as `picamera.py`.

9.11. Why do I get an AttributeError trying to set attributes on a device object?[](https://gpiozero.readthedocs.io/en/stable/faq.html#why-do-i-get-an-attributeerror-trying-to-set-attributes-on-a-device-object "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you try to add an attribute to a gpiozero device object after its initialization, you’ll find you can’t:

>>> from gpiozero import Button
>>> btn = Button(2)
>>> btn.label = 'alarm'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python3/dist-packages/gpiozero/devices.py", line 118, in  __setattr__ 
 self. __class__ . __name__ , name))
AttributeError: 'Button' object has no attribute 'label'

This is in order to prevent users accidentally setting new attributes by mistake. Because gpiozero provides functionality through setting attributes via properties, such as callbacks on buttons (and often there is no immediate feedback when setting a property), this could lead to bugs very difficult to find. Consider the following example:

from gpiozero import Button

def hello():
    print("hello")

btn = Button(2)

btn.pressed = hello

This is perfectly valid Python code, and no errors would occur, but the program would not behave as expected: pressing the button would do nothing, because the property for setting a callback is `when_pressed` not `pressed`. But without gpiozero preventing this non-existent attribute from being set, the user would likely struggle to see the mistake.

If you really want to set a new attribute on a device object, you need to create it in the class before initializing your object:

>>> from gpiozero import Button
>>> Button.label = ''
>>> btn = Button(2)
>>> btn.label = 'alarm'
>>> def press(btn):
...: print(btn.label, "was pressed")
>>> btn.when_pressed = press

9.12. Why is it called GPIO Zero? Does it only work on Pi Zero?[](https://gpiozero.readthedocs.io/en/stable/faq.html#why-is-it-called-gpio-zero-does-it-only-work-on-pi-zero "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

gpiozero works on all Raspberry Pi models, not just the Pi Zero.

The “zero” is part of a naming convention for “zero-boilerplate” education friendly libraries, which started with [Pygame Zero](https://pygame-zero.readthedocs.io/en/stable/), and has been followed by [NetworkZero](https://networkzero.readthedocs.io/en/latest/), [guizero](https://lawsie.github.io/guizero/) and more.

These libraries aim to remove barrier to entry and provide a smooth learning curve for beginners by making it easy to get started and easy to build up to more advanced projects.
