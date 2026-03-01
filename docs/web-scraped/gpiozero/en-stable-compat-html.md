# Source: https://gpiozero.readthedocs.io/en/stable/compat.html

Title: 10. Backwards Compatibility — gpiozero 2.0.1 Documentation

URL Source: https://gpiozero.readthedocs.io/en/stable/compat.html

Markdown Content:
GPIO Zero 2.x is a new major version and thus backwards incompatible changes can be expected. We have attempted to keep these as minimal as reasonably possible while taking advantage of the opportunity to clean up things. This chapter documents breaking changes from version 1.x of the library to 2.x, and all deprecated functionality which will still work in release 2.0 but is scheduled for removal in a future 2.x release.

10.1. Finding and fixing deprecated usage[](https://gpiozero.readthedocs.io/en/stable/compat.html#finding-and-fixing-deprecated-usage "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------

As of release 2.0, all deprecated functionality will raise [`DeprecationWarning`](https://docs.python.org/3.9/library/exceptions.html#DeprecationWarning "(in Python v3.9)") when used. By default, the Python interpreter suppresses these warnings (as they’re only of interest to developers, not users) but you can easily configure different behaviour.

The following example script uses a number of deprecated functions:

import gpiozero

board = gpiozero.pi_info()
for header in board.headers.values():
    for pin in header.pins.values():
        if pin.pull_up:
            print(pin.function, 'is pulled up')

Despite using deprecated functionality the script runs happily (and silently) with gpiozero 2.0. To discover what deprecated functions are being used, we add a couple of lines to tell the warnings module that we want “default” handling of [`DeprecationWarning`](https://docs.python.org/3.9/library/exceptions.html#DeprecationWarning "(in Python v3.9)"); “default” handling means that the first time an attempt is made to raise this warning at a particular location, the warning’s details will be printed to the console. All future invocations from the same location will be ignored. This saves flooding the console with warning details from tight loops. With this change, the script looks like this:

import gpiozero

import warnings
warnings.filterwarnings('default', category=DeprecationWarning)

board = gpiozero.pi_info()
for header in board.headers.values():
    for pin in header.pins.values():
        if pin.pull_up:
            print(pin.function, 'is pulled up')

And produces the following output on the console when run:

/home/dave/projects/home/gpiozero/gpio-zero/gpiozero/pins/__init__.py:899:
DeprecationWarning: PinInfo.pull_up is deprecated; please use PinInfo.pull
  warnings.warn(
/home/dave/projects/home/gpiozero/gpio-zero/gpiozero/pins/__init__.py:889:
DeprecationWarning: PinInfo.function is deprecated; please use PinInfo.name
  warnings.warn(
GPIO2 is pulled up
GPIO3 is pulled up

This tells us which pieces of deprecated functionality are being used in our script, but it doesn’t tell us where in the script they were used. For this, it is more useful to have warnings converted into full blown exceptions. With this change, each time a [`DeprecationWarning`](https://docs.python.org/3.9/library/exceptions.html#DeprecationWarning "(in Python v3.9)") would have been printed, it will instead cause the script to terminate with an unhandled exception and a full stack trace:

import gpiozero

import warnings
warnings.filterwarnings('error', category=DeprecationWarning)

board = gpiozero.pi_info()
for header in board.headers.values():
    for pin in header.pins.values():
        if pin.pull_up:
            print(pin.function, 'is pulled up')

Now when we run the script it produces the following:

Traceback (most recent call last):
  File "/home/dave/projects/home/gpiozero/gpio-zero/foo.py", line 9, in <module>
 if pin.pull_up:
  File "/home/dave/projects/home/gpiozero/gpio-zero/gpiozero/pins/__init__.py", line 899, in pull_up
 warnings.warn(
DeprecationWarning: PinInfo.pull_up is deprecated; please use PinInfo.pull

This tells us that line 9 of our script is using deprecated functionality, and provides a hint of how to fix it. We change line 9 to use the “pull” attribute instead. Now we run again, and this time get the following:

Traceback (most recent call last):
  File "/home/dave/projects/home/gpiozero/gpio-zero/foo.py", line 10, in <module>
 print(pin.function, 'is pulled up')
  File "/home/dave/projects/home/gpiozero/gpio-zero/gpiozero/pins/__init__.py", line 889, in function
 warnings.warn(
DeprecationWarning: PinInfo.function is deprecated; please use PinInfo.name

Now we can tell line 10 has a problem, and once again the exception tells us how to fix it. We continue in this fashion until the script looks like this:

import gpiozero

import warnings
warnings.filterwarnings('error', category=DeprecationWarning)

board = gpiozero.pi_info()
for header in board.headers.values():
    for pin in header.pins.values():
        if pin.pull == 'up':
            print(pin.name, 'is pulled up')

The script now runs to completion, so we can be confident it’s no longer using any deprecated functionality and will run happily even when this functionality is removed in a future 2.x release. At this point, you may wish to remove the `filterwarnings` line as well (or at least comment it out).

10.2. Python 2.x support dropped[](https://gpiozero.readthedocs.io/en/stable/compat.html#python-2-x-support-dropped "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------

By far the biggest and most important change is that the Python 2.x series is no longer supported (in practice, this means Python 2.7 is no longer supported). If your code is not compatible with Python 3, you should follow the [porting guide](https://docs.python.org/3/howto/pyporting.html) in the [Python documentation](https://docs.python.org/3/).

As of GPIO Zero 2.0, the lowest supported Python version will be 3.5. This base version may advance with minor releases, but we will make a reasonable best effort not to break compatibility with old Python 3.x versions, and to ensure that GPIO Zero can run on the version of Python in Debian oldstable at the time of its release.

10.3. RPIO pin factory removed[](https://gpiozero.readthedocs.io/en/stable/compat.html#rpio-pin-factory-removed "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------

The RPIO pin implementation is unsupported on the Raspberry Pi 2 onwards and hence of little practical use these days. Anybody still relying on RPIO’s stable PWM implementation is advised to try the pigpio pin implementation instead (also supported by GPIO Zero).

10.4. Deprecated pin-factory aliases removed[](https://gpiozero.readthedocs.io/en/stable/compat.html#deprecated-pin-factory-aliases-removed "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

Several deprecated aliases for pin factories, which could be specified by the [`GPIOZERO_PIN_FACTORY`](https://gpiozero.readthedocs.io/en/stable/cli_env.html#envvar-GPIOZERO_PIN_FACTORY) environment variable, have been removed:

*   “PiGPIOPin” is removed in favour of “pigpio”

*   “RPiGPIOPin” is removed in favour of “rpigpio”

*   “NativePin” is removed in favour of “native”

In other words, you can no longer use the following when invoking your script:

$ GPIOZERO_PIN_FACTORY=PiGPIOPin python3 my_script.py

Instead, you should use the following:

$ GPIOZERO_PIN_FACTORY=pigpio python3 my_script.py

10.5. Keyword arguments[](https://gpiozero.readthedocs.io/en/stable/compat.html#keyword-arguments "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------

Many classes in GPIO Zero 1.x were documented as having keyword-only arguments in their constructors and methods. For example, the [`PiLiter`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.PiLiter "gpiozero.PiLiter") was documented as having the constructor: 
```
PiLiter(*, pwm=False,
initial_value=False, pin_factory=None)
```
 implying that all its arguments were keyword only.

However, despite being documented in this manner, this was rarely enforced as it was extremely difficult to do so under Python 2.x without complicating the code-base considerably (Python 2.x lacked the “*” syntax to declare keyword-only arguments; they could only be implemented via “**kwargs” arguments and dictionary manipulation).

In GPIO Zero 2.0, all such arguments are now _actually_ keyword arguments. If your code complied with the 1.x documentation you shouldn’t notice any difference. In other words, the following is still fine:

from gpiozero import PiLiter

l = PiLiter(pwm=True)

However, if you had omitted the keyword you will need to modify your code:

from gpiozero import PiLiter

l = PiLiter(True)  # this will no longer work

10.6. Robots take Motors, and PhaseEnableRobot is deprecated[](https://gpiozero.readthedocs.io/en/stable/compat.html#robots-take-motors-and-phaseenablerobot-is-deprecated "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The GPIO Zero 1.x API specified that a [`Robot`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Robot "gpiozero.Robot") was constructed with two tuples that were in turn used to construct two [`Motor`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Motor "gpiozero.Motor") instances. The 2.x API replaces this with simply passing in the [`Motor`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Motor "gpiozero.Motor"), or [`PhaseEnableMotor()`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.PhaseEnableMotor "gpiozero.PhaseEnableMotor") instances you wish to use as the left and right wheels.

If your current code uses pins 4 and 14 for the left wheel, and 17 and 18 for the right wheel, it may look like this:

from gpiozero import Robot

r = Robot(left=(4, 14), right=(17, 18))

This should be changed to the following:

from gpiozero import Robot, Motor

r = Robot(left=Motor(4, 14), right=Motor(17, 18))

Likewise, if you are currently using [`PhaseEnableRobot()`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.PhaseEnableRobot "gpiozero.PhaseEnableRobot") your code may look like this:

from gpiozero import PhaseEnableRobot

r = PhaseEnableRobot(left=(4, 14), right=(17, 18))

This should be changed to the following:

from gpiozero import Robot, PhaseEnableMotor

r = Robot(left=PhaseEnableMotor(4, 14),
          right=PhaseEnableMotor(17, 18))

This change came about because the [`Motor`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.Motor "gpiozero.Motor") class was also documented as having two mandatory parameters (_forward_ and _backward_) and several keyword-only parameters, including the _enable_ pin. However, _enable_ was treated as a positional argument for the sake of constructing [`Robot`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Robot "gpiozero.Robot") which was inconsistent. Furthermore, [`PhaseEnableRobot()`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.PhaseEnableRobot "gpiozero.PhaseEnableRobot") was more or less a redundant duplicate of [`Robot`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Robot "gpiozero.Robot") but was lacking a couple of features added to [`Robot`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Robot "gpiozero.Robot") later (notable “curved” turning).

Although the new API requires a little more typing, it does mean that phase enable robot boards now inherit all the functionality of [`Robot`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Robot "gpiozero.Robot") because that’s all they use. Theoretically you could also mix and match regular motors and phase-enable motors although there’s little sense in doing so.

The former functionality (passing tuples to the [`Robot`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Robot "gpiozero.Robot") constructor) will remain as deprecated functionality for gpiozero 2.0, but will be removed in a future 2.x release. [`PhaseEnableRobot()`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.PhaseEnableRobot "gpiozero.PhaseEnableRobot") remains as a stub function which simply returns a [`Robot`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Robot "gpiozero.Robot") instance, but this will be removed in a future 2.x release.
