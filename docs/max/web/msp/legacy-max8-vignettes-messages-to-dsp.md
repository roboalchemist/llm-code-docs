# Source: https://docs.cycling74.com/legacy/max8/vignettes/messages_to_dsp

Title: Controlling MSP with Messages -  Max 8 Documentation

URL Source: https://docs.cycling74.com/legacy/max8/vignettes/messages_to_dsp

Markdown Content:
Controlling MSP with Messages
-----------------------------

You can control MSP using the [message](https://docs.cycling74.com/max8/refpages/message) box object. Normally, the [message](https://docs.cycling74.com/max8/refpages/message) box contains an object, and you click on it or replace a variable typed into the [message](https://docs.cycling74.com/max8/refpages/message) box to send a message via a patch cord to another Max object. However, if the message in a [message](https://docs.cycling74.com/max8/refpages/message) box begins with a semicolon (;) followed by the word dsp, any message which follows will be sent directly to the Max application itself, just as though there were a [receive](https://docs.cycling74.com/max8/refpages/receive) object named "dsp".

Sending a message to the Max application
----------------------------------------

*    Add a [message](https://docs.cycling74.com/max8/refpages/message) box to your Patcher, and type in a semicolon and the word dsp (;dsp), followed by the message you want to send. Your message box can contain variables (e.g. ;dsp sigvs $1). 

 You don't ned to connect the message box to anything, although you may want to connect something to the inlet of the message box to supply a message argument or trigger it from a [loadbang](https://docs.cycling74.com/max8/refpages/loadbang) object to configure MSP signal processing parameters when your patcher file is opened. 

When you click on the [message](https://docs.cycling74.com/max8/refpages/message) box or send it a bang or a value, the message will be sent to the Max application.

Here is listing of the messages you can send to the Max application using this technique:

cpulimit
--------

The word cpulimit, followed by a number in the range 0-100, sets a utilization limit for the CPU. Above this limit, MSP will not process audio vectors until the utilization comes back down, causing a click. If the cpu limit is set to either 0 or 100, there will be no limit checking done.

inremap
-------

The word inremap, followed by two numbers that specify a physical device input channel number and a logical input channel number, maps the physical device to the logical input channel.

iovs
----

The word iovs, followed by a number that is a power of 2, sets the I/O vector size.

open
----

The word open opens the Audio Status window.

outremap
--------

The word outremap, followed by two numbers that specify a logical device output channel number and a physical output channel number, maps the logical device to the physical output channel.

set
---

The word set, followed by a zero or one, turns the audio on (1) or off (0). It is equivalent to clicking on a [ezadc~](https://docs.cycling74.com/max8/refpages/ezadc~) or [ezdac~](https://docs.cycling74.com/max8/refpages/ezdac~) object.

setdriver
---------

The word setdriver, followed by a number, sets a new audio driver based on its index into the currently generated menu of drivers created by the [adstatus](https://docs.cycling74.com/max8/refpages/adstatus) driver object. If the word setdriver is followed by a symbol that names a valid driver, the new driver is selected by name. An additional symbol argument may be used to specify a "subdriver" (for example, ASIO drivers use _ASIO_ as the name of the driver and _PCI-324_ as a subdriver name that specifies a specific device).

sigvs
-----

The word sigvs, followed by a number that is a power of 2, sets the I/O signal vector size.

sr
--

The word sr, followed by a number, sets a new sampling rate in Hertz.

start
-----

The word start turns the audio on.

status
------

The word status opens the Audio Status window.

stop
----

The word stop turns the audio off.

takeover
--------

The word takeover, followed by a zero or one, turns Scheduler in Audio Interrupt mode off (0) or on (1). It is equivalent to clicking on the 'Audio Interrupt' checkbox in the Audio Status window. 'Overdrive' must be on in order for this change to be reflected.

timecode
--------

The word timecode followed by a zero or one, starts (1) or stops (0) timecode reading by any audio drivers that support the feature (ASIO 2).

wclose
------

The word wclose closes the Audio Status window.
