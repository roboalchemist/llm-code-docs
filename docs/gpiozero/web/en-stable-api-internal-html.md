# Source: https://gpiozero.readthedocs.io/en/stable/api_internal.html

Title: Internal Devices — gpiozero 2.0.1 Documentation

URL Source: https://gpiozero.readthedocs.io/en/stable/api_internal.html

Markdown Content:
18. API - Internal Devices[](https://gpiozero.readthedocs.io/en/stable/api_internal.html#module-gpiozero.internal_devices "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------

GPIO Zero also provides several “internal” devices which represent facilities provided by the operating system itself. These can be used to react to things like the time of day, or whether a server is available on the network.

These devices provide an API similar to and compatible with GPIO devices so that internal device events can trigger changes to GPIO output devices the way input devices can. In the same way a [`Button`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button "gpiozero.Button") object is _active_ when it’s pressed, and can be used to trigger other devices when its state changes, a [`TimeOfDay`](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.TimeOfDay "gpiozero.TimeOfDay") object is _active_ during a particular time period.

Consider the following code in which a [`Button`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button "gpiozero.Button") object is used to control an [`LED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED "gpiozero.LED") object:

from gpiozero import LED, Button
from signal import pause

led = LED(2)
btn = Button(3)

btn.when_pressed = led.on
btn.when_released = led.off

pause()

Now consider the following example in which a [`TimeOfDay`](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.TimeOfDay "gpiozero.TimeOfDay") object is used to control an [`LED`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.LED "gpiozero.LED") using the same method:

from gpiozero import LED, TimeOfDay
from datetime import time
from signal import pause

led = LED(2)
tod = TimeOfDay(time(9), time(10))

tod.when_activated = led.on
tod.when_deactivated = led.off

pause()

Here, rather than the LED being controlled by the press of a button, it’s controlled by the time. When the time reaches 09:00AM, the LED comes on, and at 10:00AM it goes off.

Like the [`Button`](https://gpiozero.readthedocs.io/en/stable/api_input.html#gpiozero.Button "gpiozero.Button") object, internal devices like the [`TimeOfDay`](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.TimeOfDay "gpiozero.TimeOfDay") object has [`value`](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.TimeOfDay.value "gpiozero.TimeOfDay.value"), `values`, [`is_active`](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.TimeOfDay.is_active "gpiozero.TimeOfDay.is_active"), [`when_activated`](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.TimeOfDay.when_activated "gpiozero.TimeOfDay.when_activated") and [`when_deactivated`](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.TimeOfDay.when_deactivated "gpiozero.TimeOfDay.when_deactivated") attributes, so alternative methods using the other paradigms would also work.

Note

Note that although the constructor parameter `pin_factory` is available for internal devices, and is required to be valid, the pin factory chosen will not make any practical difference. Reading a remote Pi’s CPU temperature, for example, is not currently possible.

18.1. Regular Classes[](https://gpiozero.readthedocs.io/en/stable/api_internal.html#regular-classes "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------

The following classes are intended for general use with the devices they are named after. All classes in this section are concrete (not abstract).

### 18.1.1. TimeOfDay[](https://gpiozero.readthedocs.io/en/stable/api_internal.html#timeofday "Link to this heading")

_class_ gpiozero.TimeOfDay(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/internal_devices.html#TimeOfDay)[](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.TimeOfDay "Link to this definition")
Extends [`PolledInternalDevice`](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.PolledInternalDevice "gpiozero.PolledInternalDevice") to provide a device which is active when the computer’s clock indicates that the current time is between _start\_time_ and _end\_time_ (inclusive) which are [`time`](https://docs.python.org/3.9/library/datetime.html#datetime.time "(in Python v3.9)") instances.

The following example turns on a lamp attached to an [`Energenie`](https://gpiozero.readthedocs.io/en/stable/api_boards.html#gpiozero.Energenie "gpiozero.Energenie") plug between 07:00AM and 08:00AM:

from gpiozero import TimeOfDay, Energenie
from datetime import time
from signal import pause

lamp = Energenie(1)
morning = TimeOfDay(time(7), time(8))

morning.when_activated = lamp.on
morning.when_deactivated = lamp.off

pause()

Note that _start\_time_ may be greater than _end\_time_, indicating a time period which crosses midnight.

Parameters:
*   **start_time** ([_time_](https://docs.python.org/3.9/library/datetime.html#datetime.time "(in Python v3.9)")) – The time from which the device will be considered active.

*   **end_time** ([_time_](https://docs.python.org/3.9/library/datetime.html#datetime.time "(in Python v3.9)")) – The time after which the device will be considered inactive.

*   **utc** ([_bool_](https://docs.python.org/3.9/library/functions.html#bool "(in Python v3.9)")) – If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") (the default), a naive UTC time will be used for the comparison rather than a local time-zone reading.

*   **event_delay** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – The number of seconds between file reads (defaults to 10 seconds).

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

_property_ end_time[](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.TimeOfDay.end_time "Link to this definition")
The time of day after which the device will be considered inactive.

_property_ is_active[](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.TimeOfDay.is_active "Link to this definition")
Returns [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") if the device is currently active and [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") otherwise. This property is usually derived from [`value`](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.TimeOfDay.value "gpiozero.TimeOfDay.value"). Unlike [`value`](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.TimeOfDay.value "gpiozero.TimeOfDay.value"), this is _always_ a boolean.

_property_ start_time[](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.TimeOfDay.start_time "Link to this definition")
The time of day after which the device will be considered active.

_property_ utc[](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.TimeOfDay.utc "Link to this definition")
If [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)"), use a naive UTC time reading for comparison instead of a local timezone reading.

_property_ value[](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.TimeOfDay.value "Link to this definition")
Returns `1` when the system clock reads between [`start_time`](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.TimeOfDay.start_time "gpiozero.TimeOfDay.start_time") and [`end_time`](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.TimeOfDay.end_time "gpiozero.TimeOfDay.end_time"), and `0` otherwise. If [`start_time`](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.TimeOfDay.start_time "gpiozero.TimeOfDay.start_time") is greater than [`end_time`](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.TimeOfDay.end_time "gpiozero.TimeOfDay.end_time") (indicating a period that crosses midnight), then this returns `1` when the current time is greater than [`start_time`](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.TimeOfDay.start_time "gpiozero.TimeOfDay.start_time") or less than [`end_time`](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.TimeOfDay.end_time "gpiozero.TimeOfDay.end_time").

when_activated[](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.TimeOfDay.when_activated "Link to this definition")
The function to run when the device changes state from inactive to active (time reaches _start\_time_).

This can be set to a function which accepts no (mandatory) parameters, or a Python function which accepts a single mandatory parameter (with as many optional parameters as you like). If the function accepts a single mandatory parameter, the device that activated it will be passed as that parameter.

Set this property to `None` (the default) to disable the event.

when_deactivated[](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.TimeOfDay.when_deactivated "Link to this definition")
The function to run when the device changes state from active to inactive (time reaches _end\_time_).

This can be set to a function which accepts no (mandatory) parameters, or a Python function which accepts a single mandatory parameter (with as many optional parameters as you like). If the function accepts a single mandatory parameter, the device that activated it will be passed as that parameter.

Set this property to `None` (the default) to disable the event.

### 18.1.2. PingServer[](https://gpiozero.readthedocs.io/en/stable/api_internal.html#pingserver "Link to this heading")

_class_ gpiozero.PingServer(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/internal_devices.html#PingServer)[](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.PingServer "Link to this definition")
Extends [`PolledInternalDevice`](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.PolledInternalDevice "gpiozero.PolledInternalDevice") to provide a device which is active when a _host_ (domain name or IP address) can be pinged.

The following example lights an LED while `google.com` is reachable:

from gpiozero import PingServer, LED
from signal import pause

google = PingServer('google.com')
led = LED(4)

google.when_activated = led.on
google.when_deactivated = led.off

pause()

Parameters:
*   **host** ([_str_](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)")) – The hostname or IP address to attempt to ping.

*   **event_delay** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – The number of seconds between pings (defaults to 10 seconds).

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

_property_ host[](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.PingServer.host "Link to this definition")
The hostname or IP address to test whenever [`value`](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.PingServer.value "gpiozero.PingServer.value") is queried.

_property_ is_active[](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.PingServer.is_active "Link to this definition")
Returns [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") if the device is currently active and [`False`](https://docs.python.org/3.9/library/constants.html#False "(in Python v3.9)") otherwise. This property is usually derived from [`value`](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.PingServer.value "gpiozero.PingServer.value"). Unlike [`value`](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.PingServer.value "gpiozero.PingServer.value"), this is _always_ a boolean.

_property_ value[](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.PingServer.value "Link to this definition")
Returns `1` if the host returned a single ping, and `0` otherwise.

when_activated[](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.PingServer.when_activated "Link to this definition")
The function to run when the device changes state from inactive (host unresponsive) to active (host responsive).

This can be set to a function which accepts no (mandatory) parameters, or a Python function which accepts a single mandatory parameter (with as many optional parameters as you like). If the function accepts a single mandatory parameter, the device that activated it will be passed as that parameter.

Set this property to `None` (the default) to disable the event.

when_deactivated[](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.PingServer.when_deactivated "Link to this definition")
The function to run when the device changes state from inactive (host responsive) to active (host unresponsive).

This can be set to a function which accepts no (mandatory) parameters, or a Python function which accepts a single mandatory parameter (with as many optional parameters as you like). If the function accepts a single mandatory parameter, the device that activated it will be passed as that parameter.

Set this property to `None` (the default) to disable the event.

### 18.1.3. CPUTemperature[](https://gpiozero.readthedocs.io/en/stable/api_internal.html#cputemperature "Link to this heading")

_class_ gpiozero.CPUTemperature(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/internal_devices.html#CPUTemperature)[](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.CPUTemperature "Link to this definition")
Extends [`PolledInternalDevice`](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.PolledInternalDevice "gpiozero.PolledInternalDevice") to provide a device which is active when the CPU temperature exceeds the _threshold_ value.

The following example plots the CPU’s temperature on an LED bar graph:

from gpiozero import LEDBarGraph, CPUTemperature
from signal import pause

# Use minimums and maximums that are closer to "normal" usage so the
# bar graph is a bit more "lively"
cpu = CPUTemperature(min_temp=50, max_temp=90)

print(f'Initial temperature: {cpu.temperature}C')

graph = LEDBarGraph(5, 6, 13, 19, 25, pwm=True)
graph.source = cpu

pause()

Parameters:
*   **sensor_file** ([_str_](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)")) – The file from which to read the temperature. This defaults to the sysfs file `/sys/class/thermal/thermal_zone0/temp`. Whatever file is specified is expected to contain a single line containing the temperature in milli-degrees celsius.

*   **min_temp** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – The temperature at which [`value`](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.CPUTemperature.value "gpiozero.CPUTemperature.value") will read 0.0. This defaults to 0.0.

*   **max_temp** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – The temperature at which [`value`](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.CPUTemperature.value "gpiozero.CPUTemperature.value") will read 1.0. This defaults to 100.0.

*   **threshold** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – The temperature above which the device will be considered “active”. (see [`is_active`](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.CPUTemperature.is_active "gpiozero.CPUTemperature.is_active")). This defaults to 80.0.

*   **event_delay** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – The number of seconds between file reads (defaults to 5 seconds).

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

_property_ is_active[](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.CPUTemperature.is_active "Link to this definition")
Returns [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") when the CPU [`temperature`](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.CPUTemperature.temperature "gpiozero.CPUTemperature.temperature") exceeds the _threshold_.

_property_ temperature[](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.CPUTemperature.temperature "Link to this definition")
Returns the current CPU temperature in degrees celsius.

_property_ value[](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.CPUTemperature.value "Link to this definition")
Returns the current CPU temperature as a value between 0.0 (representing the _min\_temp_ value) and 1.0 (representing the _max\_temp_ value). These default to 0.0 and 100.0 respectively, hence [`value`](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.CPUTemperature.value "gpiozero.CPUTemperature.value") is [`temperature`](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.CPUTemperature.temperature "gpiozero.CPUTemperature.temperature") divided by 100 by default.

when_activated[](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.CPUTemperature.when_activated "Link to this definition")
The function to run when the device changes state from inactive to active (temperature reaches _threshold_).

This can be set to a function which accepts no (mandatory) parameters, or a Python function which accepts a single mandatory parameter (with as many optional parameters as you like). If the function accepts a single mandatory parameter, the device that activated it will be passed as that parameter.

Set this property to `None` (the default) to disable the event.

when_deactivated[](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.CPUTemperature.when_deactivated "Link to this definition")
The function to run when the device changes state from active to inactive (temperature drops below _threshold_).

This can be set to a function which accepts no (mandatory) parameters, or a Python function which accepts a single mandatory parameter (with as many optional parameters as you like). If the function accepts a single mandatory parameter, the device that activated it will be passed as that parameter.

Set this property to `None` (the default) to disable the event.

### 18.1.4. LoadAverage[](https://gpiozero.readthedocs.io/en/stable/api_internal.html#loadaverage "Link to this heading")

_class_ gpiozero.LoadAverage(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/internal_devices.html#LoadAverage)[](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.LoadAverage "Link to this definition")
Extends [`PolledInternalDevice`](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.PolledInternalDevice "gpiozero.PolledInternalDevice") to provide a device which is active when the CPU load average exceeds the _threshold_ value.

The following example plots the load average on an LED bar graph:

from gpiozero import LEDBarGraph, LoadAverage
from signal import pause

la = LoadAverage(min_load_average=0, max_load_average=2)
graph = LEDBarGraph(5, 6, 13, 19, 25, pwm=True)

graph.source = la

pause()

Parameters:
*   **load_average_file** ([_str_](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)")) – The file from which to read the load average. This defaults to the proc file `/proc/loadavg`. Whatever file is specified is expected to contain three space-separated load averages at the beginning of the file, representing 1 minute, 5 minute and 15 minute averages respectively.

*   **min_load_average** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – The load average at which [`value`](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.LoadAverage.value "gpiozero.LoadAverage.value") will read 0.0. This defaults to 0.0.

*   **max_load_average** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – The load average at which [`value`](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.LoadAverage.value "gpiozero.LoadAverage.value") will read 1.0. This defaults to 1.0.

*   **threshold** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – The load average above which the device will be considered “active”. (see [`is_active`](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.LoadAverage.is_active "gpiozero.LoadAverage.is_active")). This defaults to 0.8.

*   **minutes** ([_int_](https://docs.python.org/3.9/library/functions.html#int "(in Python v3.9)")) – The number of minutes over which to average the load. Must be 1, 5 or 15. This defaults to 5.

*   **event_delay** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – The number of seconds between file reads (defaults to 10 seconds).

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

_property_ is_active[](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.LoadAverage.is_active "Link to this definition")
Returns [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") when the [`load_average`](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.LoadAverage.load_average "gpiozero.LoadAverage.load_average") exceeds the _threshold_.

_property_ load_average[](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.LoadAverage.load_average "Link to this definition")
Returns the current load average.

_property_ value[](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.LoadAverage.value "Link to this definition")
Returns the current load average as a value between 0.0 (representing the _min\_load\_average_ value) and 1.0 (representing the _max\_load\_average_ value). These default to 0.0 and 1.0 respectively.

when_activated[](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.LoadAverage.when_activated "Link to this definition")
The function to run when the device changes state from inactive to active (load average reaches _threshold_).

This can be set to a function which accepts no (mandatory) parameters, or a Python function which accepts a single mandatory parameter (with as many optional parameters as you like). If the function accepts a single mandatory parameter, the device that activated it will be passed as that parameter.

Set this property to `None` (the default) to disable the event.

when_deactivated[](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.LoadAverage.when_deactivated "Link to this definition")
The function to run when the device changes state from active to inactive (load average drops below _threshold_).

This can be set to a function which accepts no (mandatory) parameters, or a Python function which accepts a single mandatory parameter (with as many optional parameters as you like). If the function accepts a single mandatory parameter, the device that activated it will be passed as that parameter.

Set this property to `None` (the default) to disable the event.

### 18.1.5. DiskUsage[](https://gpiozero.readthedocs.io/en/stable/api_internal.html#diskusage "Link to this heading")

_class_ gpiozero.DiskUsage(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/internal_devices.html#DiskUsage)[](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.DiskUsage "Link to this definition")
Extends [`PolledInternalDevice`](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.PolledInternalDevice "gpiozero.PolledInternalDevice") to provide a device which is active when the disk space used exceeds the _threshold_ value.

The following example plots the disk usage on an LED bar graph:

from gpiozero import LEDBarGraph, DiskUsage
from signal import pause

disk = DiskUsage()

print(f'Current disk usage: {disk.usage}%')

graph = LEDBarGraph(5, 6, 13, 19, 25, pwm=True)
graph.source = disk

pause()

Parameters:
*   **filesystem** ([_str_](https://docs.python.org/3.9/library/stdtypes.html#str "(in Python v3.9)")) – A path within the filesystem for which the disk usage needs to be computed. This defaults to `/`, which is the root filesystem.

*   **threshold** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – The disk usage percentage above which the device will be considered “active” (see [`is_active`](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.DiskUsage.is_active "gpiozero.DiskUsage.is_active")). This defaults to 90.0.

*   **event_delay** ([_float_](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)")) – The number of seconds between file reads (defaults to 30 seconds).

*   **pin_factory** ([_Factory_](https://gpiozero.readthedocs.io/en/stable/api_pins.html#gpiozero.Factory "gpiozero.Factory")_or_ _None_) – See [API - Pins](https://gpiozero.readthedocs.io/en/stable/api_pins.html) for more information (this is an advanced feature which most users can ignore).

_property_ is_active[](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.DiskUsage.is_active "Link to this definition")
Returns [`True`](https://docs.python.org/3.9/library/constants.html#True "(in Python v3.9)") when the disk [`usage`](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.DiskUsage.usage "gpiozero.DiskUsage.usage") exceeds the _threshold_.

_property_ usage[](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.DiskUsage.usage "Link to this definition")
Returns the current disk usage in percentage.

_property_ value[](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.DiskUsage.value "Link to this definition")
Returns the current disk usage as a value between 0.0 and 1.0 by dividing [`usage`](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.DiskUsage.usage "gpiozero.DiskUsage.usage") by 100.

when_activated[](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.DiskUsage.when_activated "Link to this definition")
The function to run when the device changes state from inactive to active (disk usage reaches _threshold_).

This can be set to a function which accepts no (mandatory) parameters, or a Python function which accepts a single mandatory parameter (with as many optional parameters as you like). If the function accepts a single mandatory parameter, the device that activated it will be passed as that parameter.

Set this property to `None` (the default) to disable the event.

when_deactivated[](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.DiskUsage.when_deactivated "Link to this definition")
The function to run when the device changes state from active to inactive (disk usage drops below _threshold_).

This can be set to a function which accepts no (mandatory) parameters, or a Python function which accepts a single mandatory parameter (with as many optional parameters as you like). If the function accepts a single mandatory parameter, the device that activated it will be passed as that parameter.

Set this property to `None` (the default) to disable the event.

18.2. Base Classes[](https://gpiozero.readthedocs.io/en/stable/api_internal.html#base-classes "Link to this heading")
----------------------------------------------------------------------------------------------------------------------

The classes in the sections above are derived from a series of base classes, some of which are effectively abstract. The classes form the (partial) hierarchy displayed in the graph below (abstract classes are shaded lighter than concrete classes):

![Image 1: _images/internal_device_hierarchy.svg](https://gpiozero.readthedocs.io/en/stable/_images/internal_device_hierarchy.svg)
The following sections document these base classes for advanced users that wish to construct classes for their own devices.

### 18.2.1. PolledInternalDevice[](https://gpiozero.readthedocs.io/en/stable/api_internal.html#polledinternaldevice "Link to this heading")

_class_ gpiozero.PolledInternalDevice(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/internal_devices.html#PolledInternalDevice)[](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.PolledInternalDevice "Link to this definition")
Extends [`InternalDevice`](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.InternalDevice "gpiozero.InternalDevice") to provide a background thread to poll internal devices that lack any other mechanism to inform the instance of changes.

### 18.2.2. InternalDevice[](https://gpiozero.readthedocs.io/en/stable/api_internal.html#internaldevice "Link to this heading")

_class_ gpiozero.InternalDevice(_*args_, _**kwargs_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/internal_devices.html#InternalDevice)[](https://gpiozero.readthedocs.io/en/stable/api_internal.html#gpiozero.InternalDevice "Link to this definition")
Extends [`Device`](https://gpiozero.readthedocs.io/en/stable/api_generic.html#gpiozero.Device "gpiozero.Device") to provide a basis for devices which have no specific hardware representation. These are effectively pseudo-devices and usually represent operating system services like the internal clock, file systems or network facilities.
