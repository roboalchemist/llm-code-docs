# Source: https://gpiozero.readthedocs.io/en/stable/api_generic.html

Title: Generic Classes — gpiozero 2.0.1 Documentation

URL Source: https://gpiozero.readthedocs.io/en/stable/api_generic.html

Markdown Content:
19. API - Generic Classes[](https://gpiozero.readthedocs.io/en/stable/api_generic.html#module-gpiozero.devices "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------

The GPIO Zero class hierarchy is quite extensive. It contains several base classes (most of which are documented in their corresponding chapters):

*   [`Device`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.Device "gpiozero.Device") is the root of the hierarchy, implementing base functionality like [`close()`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.Device.close "gpiozero.Device.close") and context manager handlers.

*   [`GPIODevice`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.GPIODevice "gpiozero.GPIODevice") represents individual devices that attach to a single GPIO pin

*   [`SPIDevice`](https://gpiozero.readthedocs.io/en/stable/api_spi.html#gpiozero.SPIDevice "gpiozero.SPIDevice") represents devices that communicate over an SPI interface (implemented as four GPIO pins)

*   [`InternalDevice`](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.InternalDevice "gpiozero.InternalDevice") represents devices that are entirely internal to the Pi (usually operating system related services)

*   [`CompositeDevice`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.CompositeDevice "gpiozero.CompositeDevice") represents devices composed of multiple other devices like HATs

There are also several [mixin classes](https://en.wikipedia.org/wiki/Mixin) for adding important functionality at numerous points in the hierarchy, which is illustrated below (mixin classes are represented in purple, while abstract classes are shaded lighter):

![Image 1: _images/device_hierarchy.svg](https://gpiozero.readthedocs.io/en/stable/_images/device_hierarchy.svg)
19.1. Device[](https://gpiozero.readthedocs.io/en/stable/api_generic.html#device "Link to this heading")
---------------------------------------------------------------------------------------------------------

_class_ gpiozero.Device(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/devices.html#Device)[](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.Device "Link to this definition")
Represents a single device of any type; GPIO-based, SPI-based, I2C-based, etc. This is the base class of the device hierarchy. It defines the basic services applicable to all devices (specifically the [`is_active`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.Device.is_active "gpiozero.Device.is_active") property, the [`value`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.Device.value "gpiozero.Device.value") property, and the [`close()`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.Device.close "gpiozero.Device.close") method).

pin_factory[](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.Device.pin_factory "Link to this definition")
This attribute exists at both a class level (representing the default pin factory used to construct devices when no _pin\_factory_ parameter is specified), and at an instance level (representing the pin factory that the device was constructed with).

The pin factory provides various facilities to the device including allocating pins, providing low level interfaces (e.g. SPI), and clock facilities (querying and calculating elapsed times).

close()[](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.Device.close "Link to this definition")
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

_property_ closed[](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.Device.closed "Link to this definition")
Returns [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") if the device is closed (see the [`close()`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.Device.close "gpiozero.Device.close") method). Once a device is closed you can no longer use any other methods or properties to control or query the device.

_property_ is_active[](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.Device.is_active "Link to this definition")
Returns [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") if the device is currently active and [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") otherwise. This property is usually derived from [`value`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.Device.value "gpiozero.Device.value"). Unlike [`value`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.Device.value "gpiozero.Device.value"), this is _always_ a boolean.

_property_ value[](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.Device.value "Link to this definition")
Returns a value representing the device’s state. Frequently, this is a boolean value, or a number between 0 and 1 but some devices use larger ranges (e.g. -1 to +1) and composite devices usually use tuples to return the states of all their subordinate components.

19.2. ValuesMixin[](https://gpiozero.readthedocs.io/en/stable/api_generic.html#valuesmixin "Link to this heading")
-------------------------------------------------------------------------------------------------------------------

_class_ gpiozero.ValuesMixin(_..._)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/mixins.html#ValuesMixin)[](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.ValuesMixin "Link to this definition")
Adds a [`values`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.ValuesMixin.values "gpiozero.ValuesMixin.values") property to the class which returns an infinite generator of readings from the [`value`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.Device.value "gpiozero.Device.value") property. There is rarely a need to use this mixin directly as all base classes in GPIO Zero include it.

Note

Use this mixin _first_ in the parent class list.

_property_ values[](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.ValuesMixin.values "Link to this definition")
An infinite iterator of values read from `value`.

19.3. SourceMixin[](https://gpiozero.readthedocs.io/en/stable/api_generic.html#sourcemixin "Link to this heading")
-------------------------------------------------------------------------------------------------------------------

_class_ gpiozero.SourceMixin(_..._)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/mixins.html#SourceMixin)[](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.SourceMixin "Link to this definition")
Adds a [`source`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.SourceMixin.source "gpiozero.SourceMixin.source") property to the class which, given an iterable or a [`ValuesMixin`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.ValuesMixin "gpiozero.ValuesMixin") descendent, sets [`value`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.Device.value "gpiozero.Device.value") to each member of that iterable until it is exhausted. This mixin is generally included in novel output devices to allow their state to be driven from another device.

Note

Use this mixin _first_ in the parent class list.

_property_ source[](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.SourceMixin.source "Link to this definition")
The iterable to use as a source of values for `value`.

_property_ source_delay[](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.SourceMixin.source_delay "Link to this definition")
The delay (measured in seconds) in the loop used to read values from [`source`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.SourceMixin.source "gpiozero.SourceMixin.source"). Defaults to 0.01 seconds which is generally sufficient to keep CPU usage to a minimum while providing adequate responsiveness.

19.4. SharedMixin[](https://gpiozero.readthedocs.io/en/stable/api_generic.html#sharedmixin "Link to this heading")
-------------------------------------------------------------------------------------------------------------------

_class_ gpiozero.SharedMixin(_..._)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/mixins.html#SharedMixin)[](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.SharedMixin "Link to this definition")
This mixin marks a class as “shared”. In this case, the meta-class (GPIOMeta) will use [`_shared_key()`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.SharedMixin._shared_key "gpiozero.SharedMixin._shared_key") to convert the constructor arguments to an immutable key, and will check whether any existing instances match that key. If they do, they will be returned by the constructor instead of a new instance. An internal reference counter is used to determine how many times an instance has been “constructed” in this way.

When [`close()`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.Device.close "gpiozero.Device.close") is called, an internal reference counter will be decremented and the instance will only close when it reaches zero.

_classmethod_ _shared_key(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/mixins.html#SharedMixin._shared_key)[](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.SharedMixin._shared_key "Link to this definition")
This is called with the constructor arguments to generate a unique key (which must be storable in a [`dict`](https://docs.python.org/3.9/library/stdtypes.html#dict "(in Python v3.9)") and, thus, immutable and hashable) representing the instance that can be shared. This must be overridden by descendents.

19.5. EventsMixin[](https://gpiozero.readthedocs.io/en/stable/api_generic.html#eventsmixin "Link to this heading")
-------------------------------------------------------------------------------------------------------------------

_class_ gpiozero.EventsMixin(_..._)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/mixins.html#EventsMixin)[](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.EventsMixin "Link to this definition")
Adds edge-detected [`when_activated()`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.EventsMixin.when_activated "gpiozero.EventsMixin.when_activated") and [`when_deactivated()`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.EventsMixin.when_deactivated "gpiozero.EventsMixin.when_deactivated") events to a device based on changes to the [`is_active`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.Device.is_active "gpiozero.Device.is_active") property common to all devices. Also adds [`wait_for_active()`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.EventsMixin.wait_for_active "gpiozero.EventsMixin.wait_for_active") and [`wait_for_inactive()`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.EventsMixin.wait_for_inactive "gpiozero.EventsMixin.wait_for_inactive") methods for level-waiting.

Note

Note that this mixin provides no means of actually firing its events; call `_fire_events()` in sub-classes when device state changes to trigger the events. This should also be called once at the end of initialization to set initial states.

wait_for_active(_timeout=None_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/mixins.html#EventsMixin.wait_for_active)[](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.EventsMixin.wait_for_active "Link to this definition")
Pause the script until the device is activated, or the timeout is reached.

Parameters:
**timeout** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")_or_ _None_) – Number of seconds to wait before proceeding. If this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default), then wait indefinitely until the device is active.

wait_for_inactive(_timeout=None_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/mixins.html#EventsMixin.wait_for_inactive)[](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.EventsMixin.wait_for_inactive "Link to this definition")
Pause the script until the device is deactivated, or the timeout is reached.

Parameters:
**timeout** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")_or_ _None_) – Number of seconds to wait before proceeding. If this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default), then wait indefinitely until the device is inactive.

_property_ active_time[](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.EventsMixin.active_time "Link to this definition")
The length of time (in seconds) that the device has been active for. When the device is inactive, this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)").

_property_ inactive_time[](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.EventsMixin.inactive_time "Link to this definition")
The length of time (in seconds) that the device has been inactive for. When the device is active, this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)").

when_activated[](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.EventsMixin.when_activated "Link to this definition")
The function to run when the device changes state from inactive to active.

This can be set to a function which accepts no (mandatory) parameters, or a Python function which accepts a single mandatory parameter (with as many optional parameters as you like). If the function accepts a single mandatory parameter, the device that activated it will be passed as that parameter.

Set this property to [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default) to disable the event.

when_deactivated[](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.EventsMixin.when_deactivated "Link to this definition")
The function to run when the device changes state from active to inactive.

This can be set to a function which accepts no (mandatory) parameters, or a Python function which accepts a single mandatory parameter (with as many optional parameters as you like). If the function accepts a single mandatory parameter, the device that deactivated it will be passed as that parameter.

Set this property to [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default) to disable the event.

19.6. HoldMixin[](https://gpiozero.readthedocs.io/en/stable/api_generic.html#holdmixin "Link to this heading")
---------------------------------------------------------------------------------------------------------------

_class_ gpiozero.HoldMixin(_..._)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/mixins.html#HoldMixin)[](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.HoldMixin "Link to this definition")
Extends [`EventsMixin`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.EventsMixin "gpiozero.EventsMixin") to add the [`when_held`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.HoldMixin.when_held "gpiozero.HoldMixin.when_held") event and the machinery to fire that event repeatedly (when [`hold_repeat`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.HoldMixin.hold_repeat "gpiozero.HoldMixin.hold_repeat") is [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)")) at internals defined by [`hold_time`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.HoldMixin.hold_time "gpiozero.HoldMixin.hold_time").

_property_ held_time[](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.HoldMixin.held_time "Link to this definition")
The length of time (in seconds) that the device has been held for. This is counted from the first execution of the [`when_held`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.HoldMixin.when_held "gpiozero.HoldMixin.when_held") event rather than when the device activated, in contrast to [`active_time`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.EventsMixin.active_time "gpiozero.EventsMixin.active_time"). If the device is not currently held, this is [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)").

_property_ hold_repeat[](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.HoldMixin.hold_repeat "Link to this definition")
If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"), [`when_held`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.HoldMixin.when_held "gpiozero.HoldMixin.when_held") will be executed repeatedly with [`hold_time`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.HoldMixin.hold_time "gpiozero.HoldMixin.hold_time") seconds between each invocation.

_property_ hold_time[](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.HoldMixin.hold_time "Link to this definition")
The length of time (in seconds) to wait after the device is activated, until executing the [`when_held`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.HoldMixin.when_held "gpiozero.HoldMixin.when_held") handler. If [`hold_repeat`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.HoldMixin.hold_repeat "gpiozero.HoldMixin.hold_repeat") is True, this is also the length of time between invocations of [`when_held`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.HoldMixin.when_held "gpiozero.HoldMixin.when_held").

_property_ is_held[](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.HoldMixin.is_held "Link to this definition")
When [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"), the device has been active for at least [`hold_time`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.HoldMixin.hold_time "gpiozero.HoldMixin.hold_time") seconds.

when_held[](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.HoldMixin.when_held "Link to this definition")
The function to run when the device has remained active for [`hold_time`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.HoldMixin.hold_time "gpiozero.HoldMixin.hold_time") seconds.

This can be set to a function which accepts no (mandatory) parameters, or a Python function which accepts a single mandatory parameter (with as many optional parameters as you like). If the function accepts a single mandatory parameter, the device that activated will be passed as that parameter.

Set this property to [`None`](https://docs.python.org/3.9/library/constants.html#None "(in Python v3.9)") (the default) to disable the event.
