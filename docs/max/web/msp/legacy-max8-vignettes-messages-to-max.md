# Source: https://docs.cycling74.com/legacy/max8/vignettes/messages_to_max

Title: Controlling Max with Messages -  Max 8 Documentation

URL Source: https://docs.cycling74.com/legacy/max8/vignettes/messages_to_max

Markdown Content:
Controlling Max with Messages
-----------------------------

You can control Max, MSP, and Jitter using the [message](https://docs.cycling74.com/max8/refpages/message) box object. Normally, the [message](https://docs.cycling74.com/max8/refpages/message) box contains an object, and you click on it or replace a variable typed into the [message](https://docs.cycling74.com/max8/refpages/message) box to send a message down a patch cord to another Max object. However, if the message in a message box begins with a semicolon (;) followed by the word max, any message which follows will be sent directly to the Max application itself, just as though there were a [receive](https://docs.cycling74.com/max8/refpages/receive) object named "max".

Sending a message to the Max application
----------------------------------------

*    Add a [message](https://docs.cycling74.com/max8/refpages/message) box to your Patcher, and type in a semicolon and the word max (;max), followed by the message you want to send to Max. Your message box can contain variables (e.g. ;max pupdate $1 $2). 

When you click on the [message](https://docs.cycling74.com/max8/refpages/message) box or send it a bang or a value, the message will be sent to the Max application.

Here is listing of the messages you can send to the Max application using this technique:

buildcollective
---------------

The word buildcollective, followed by a reference name symbol and an output filename, builds a collective using the patcher associated with the symbol. The collective is named with the output filename.

checkpreempt
------------

The word checkpreempt, followed by a symbol, sends the current Overdrive mode to the [receive](https://docs.cycling74.com/max8/refpages/receive) object named by the symbol.

clean
-----

Causes Max not to show a Save Changes dialog when you close a window or quit, even if there are windows that have been modified. This is useful in conjunction with the quit message below.

clearmaxwindow
--------------

Clear the Max Console.

closefile
---------

The word closefile, followed by a symbol, closes the patcher file previously opened with the openfile message to Max associated with the symbol.

crash
-----

The word crash causes the Max application to terminate and generate a standard crashlog. When relaunched, The Max application will perform standard crash recovery (if crash recovery is enabled in the Max preferences).

Causes Max to write the metadata information currently stored in the database to a file. An optional argument can be used to specify a filename. If no filename is specified, the metadata is backed up to a file in your preferences folder.

Causes Max to load metadata information from a previously stored file into the Max database. An optional argument can be used to specify a filename - when no argument is specified, Max will look for a backup file from a previous call to db.exportmeta in your preferences folder.

db.reset
--------

Causes Max to recreate the database Max uses when operating (e.g. the [File Browser](https://docs.cycling74.com/max8/vignettes/file_browser)).

debug
-----

The word debug, followed by a zero or one, toggles the sending of Max's internal debugging output to the Max Console. Debug information may be of limited use for anyone who isn't debugging Max itself.

disablevirtualmididestinations
------------------------------

The word disablevirtualmididestinations, followed by a one, causes the Core MIDI driver to not create virtual destinations. If an argument of zero is given, the virtual destinations are created again.

disablevirtualmidisources
-------------------------

The word disablevirtualmidisources, followed by a one, causes the Core MIDI driver to not create virtual sources. If an argument of zero is given, the virtual sources are created again.

enablepathcache
---------------

The word enablepathcache, followed by a zero or one, turns on (or off) Max's search path cache. This should only be done if you noticed unusual behavior when opening files.

externaleditor
--------------

The word externaleditor followed by a symbol sets the text editor used for editing text file content - such as saved coll files, text files and Javascript code.

externs
-------

List all of the external objects currently loaded in the Max Console.

fileformat
----------

The word fileformat, followed by two symbols that specify a file extension and a four-character file type, tells Max to associate a filename extension with a particular filetype. The message max fileformat .tx TEXT associates the extension _.tx_ with TEXT (text) files. This allows a user to send a message read george and locate a file with the name _george.tx_. It also ensures that files with the extension _.tx_ will appear in a standard open file dialog where text files can be chosen.

fixwidthratio
-------------

The word fixwidthratio, followed by a floating-point number, sets the ratio of the box to the width of the text when the user chooses **Fix Width** from the Object menu. The default value is 1.0. A value of 1.1 would make boxes wider than they needed to be, and a value of 0.9 would make boxes narrower than they need to be.

getarch
-------

The word getarch, followed by a symbol used as the name of a [receive](https://docs.cycling74.com/max8/refpages/receive) object, sends the currently running Max architecture (always 'x64') to the named [receive](https://docs.cycling74.com/max8/refpages/receive) object.

getdefaultpatcherheight
-----------------------

The word getdefaultpatcherheight followed by a symbol used as the name of a [receive](https://docs.cycling74.com/max8/refpages/receive) object, causes Max to report the current default patcher height in pixels to the named [receive](https://docs.cycling74.com/max8/refpages/receive) object (See also the setdefaultpatcherheight message to Max.)

getdefaultpatcherwidth
----------------------

The word getdefaultpatcherwidth, followed by a symbol used as the name of a [receive](https://docs.cycling74.com/max8/refpages/receive) object, causes Max to report the current default patcher width in pixels to the named [receive](https://docs.cycling74.com/max8/refpages/receive) object (See also the setdefaultpatcherwidth message to Max.)

getenablepathcache
------------------

The word getenablepathcache, followed by a symbol used as the name of a [receive](https://docs.cycling74.com/max8/refpages/receive) object, will report whether the path cache is enabled to the named [receive](https://docs.cycling74.com/max8/refpages/receive) object. (See also the enablepathcache message to Max.)

geteventinterval
----------------

The word geteventinterval, followed by a symbol used as the name of a [receive](https://docs.cycling74.com/max8/refpages/receive) object, will report the event interval to the named [receive](https://docs.cycling74.com/max8/refpages/receive) object. (See also the seteventinterval message to Max.)

getfixwidthratio
----------------

The word getfixwidthratio, followed by a symbol used as the name of a [receive](https://docs.cycling74.com/max8/refpages/receive) object, reports the current fix with ratio value to the named [receive](https://docs.cycling74.com/max8/refpages/receive) object. (See also the fixwidthratio message to Max.)

getpollthrottle
---------------

The word getpollthrottle, followed by a symbol used as the name of a [receive](https://docs.cycling74.com/max8/refpages/receive) object, reports the current poll throttle value to the named [receive](https://docs.cycling74.com/max8/refpages/receive) object. (See also the setpollthrottle message to Max.)

getqueuethrottle
----------------

The word getqueuethrottle, followed by a symbol used as the name of a [receive](https://docs.cycling74.com/max8/refpages/receive) object, causes Max to report the current queue throttle value to the named [receive](https://docs.cycling74.com/max8/refpages/receive) object. (See also the setqueuethrottle message to Max.)

getrefreshrate
--------------

The word getrefreshrate, followed by a symbol used as the name of a [receive](https://docs.cycling74.com/max8/refpages/receive) object, causes Max to report the current refresh rate in frames per second (fps) to the named [receive](https://docs.cycling74.com/max8/refpages/receive) object. (See also the refreshrate message to Max.)

getruntime
----------

The word getruntime, followed by a symbol used as the name of a [receive](https://docs.cycling74.com/max8/refpages/receive) object,sends a 1 to the named [receive](https://docs.cycling74.com/max8/refpages/receive) object if the current version of Max is a runtime version, and a 0 if not.

getslop
-------

The word getslop, followed by a symbol used as the name of a [receive](https://docs.cycling74.com/max8/refpages/receive) object, reports the scheduler slop value to the named [receive](https://docs.cycling74.com/max8/refpages/receive) object. (See also the setslop message to Max.)

getsysqelemthrottle
-------------------

The word getsysqelemthrottle, followed by a symbol used as the name of a [receive](https://docs.cycling74.com/max8/refpages/receive) object, reports the maximum number of patcher UI update events processed at a time to the named [receive](https://docs.cycling74.com/max8/refpages/receive) object. (See also the setsysqelemthrottle message to Max.)

getsystem
---------

The word getsystem, followed by a symbol used as the name of a [receive](https://docs.cycling74.com/max8/refpages/receive) object, will report the name of the system (macintosh or windows) to the named [receive](https://docs.cycling74.com/max8/refpages/receive) object.

getversion
----------

The word getversion, followed by a symbol used as the name of a [receive](https://docs.cycling74.com/max8/refpages/receive) object, will report the Max version number as a decimal value, which needs to be converted to a hexidecimal value (e.g. Max version 7.3.4 is reported as '1844'), and output from the named [receive](https://docs.cycling74.com/max8/refpages/receive) object.

hidecursor
----------

Hides the cursor if it is visible.

Hides the menu bar. Although the pull-down menus are not available when the menu bar is hidden, menu shortcut (accelerator) keys continue to work.

htmlref
-------

The word htmlref, followed by an object name as a symbol, looks for a file called _<object-name>_.html in the search path. If found, a web browser is opened to view the page.

interval
--------

The word interval, followed by a number from 1 to 20, sets the timing interval of Max's internal scheduler in milliseconds. The default value is 1. This message only affects the scheduler when Overdrive is on and scheduler in audio interrupt (available with MSP) is off. (When using scheduler in audio interrupt mode the signal vector size determines the scheduler interval.) Larger scheduler intervals can improve CPU efficiency on slower computer models at the expense of timing accuracy.

launchbrowser
-------------

The word launchbrowser, followed by a URL as a symbol, opens a web browser to view the URL. For example:

_; max launchbrowser http://www.cycling74.com_

maxcharheightforsubpixelantialiasing
------------------------------------

The word maxcharheightforsubpixelantialiasing, followed by a number, sets a threshold font size (in points) for native subpixel aliasing. Since the look of subpixel antialiasing may be undesirable when working with large fonts as compared to regular antialiasing, this attribute lets you specify a threshold font size; if a font is larger than the specified size, it will be rendered using regular rather than subpixel antialiasing. 

 Note that Max honors your computer's system preferences - Max won't use subpixel aliasing if you've disabled it for your system. Setting this attribute value to zero value is 0 will always use regular antialiasing, and setting a very high value will always use subpixel antialiasing (unless it is disabled in system preferences).

When using the runtime version of Max *and* an active custom [menubar](https://docs.cycling74.com/max8/refpages/menubar) object, maxinwmenu, followed by the number 1, will place an item called Status in the Windows menu, allowing users to see the Max Console (labeled Status in the runtime version). When maxinwmenu is followed by 0 the menu item is not present. The default is for the Status item to be present in the Windows menu.

maxwindow
---------

Displays the Max Console. If the Max Console if not currently open, the window will be displayed. If the window is currently open, it will bring it to the front.

midilist
--------

Prints the names of all current MIDI devices in the Max Console. (See also MIDI Messages to Max, below.)

nativetextrendering
-------------------

The word nativetextrendering, followed by a zero or one, toggles between using JUCE font rendering (0) and the platform-native font rendering for your computer (1) when displaying text in Max.

notypeinfo
----------

(Macintosh) The word notypeinfo, followed by zero or one, sets whether Max saves files with traditional Mac OS four-character type information. By default, Max does save this information in files.

objectfile
----------

The word objectfile, followed by two symbols that specify an object name and a file name, creates a mapping between the external object and its filename. For example, the [*~](https://docs.cycling74.com/max8/refpages/times~) object is in a file called _times~_ so at startup Max executes the command max objectfile *~ times~.

openfile
--------

The word openfile, followed by two symbols that specify an reference name and a file name or path name, attempts to open the patcher with the specified name. If successful, the patcher is associated with the reference symbol, which can be passed as argument to the buildcollective, buildplugin, and closefile messages to Max. The openfile message is intended for batch collective building.

paths
-----

List the current search paths in the Max Console. There is a button in the File Preferences window that does this.

preempt
-------

The word preempt, followed by a one (on) or zero (off), toggles Overdrive mode.

pupdate
-------

The word pupdate, followed by two integer values that specify horizontal and vertical position, moves the mouse cursor to that global location.

purgemididevices
----------------

Purge the missing MIDI device cache; Max maintains a cache of the [MIDI Setup](https://docs.cycling74.com/max8/vignettes/midi_setup_window) settings for known, but detached MIDI devices. Sending the message purgemididevices to Max will 'forget' any missing devices.

quit
----

Quits the Max application; equivalent to choosing Quit from the File menu. If there are unsaved changes to open files, and you haven't sent Max the clean message, Max will ask whether to save changes.

refresh
-------

Causes all Max Consoles to be updated.

refreshrate
-----------

The word refreshrate, followed by a number, sets the rate limit, in frames per second, at which the UI for user interface objects is updated. Better visual performance can be achieved - at the cost of a slight performance decrease in Jitter, and little or no performance decrease for audio processing - by specifying a higher frame rate.

relaunchmax
-----------

The word relaunchmax causes the Max application to close and relaunch.

runtime
-------

The word runtime, followed by a zero or one and a message, executes the message if the current version of Max is a runtime version (1) or non-runtime (0).

sendinterval
------------

The word sendinterval, followed by a symbol, sends the current scheduler interval to the [receive](https://docs.cycling74.com/max8/refpages/receive) object named by the symbol.

sendapppath
-----------

The word sendapppath, followed by a symbol, sends a symbol with the path of the Max application to the [receive](https://docs.cycling74.com/max8/refpages/receive) object named by the symbol.

setdefaultpatcherheight
-----------------------

The word setdefaultpatcherheight, followed by an integer value greater than 100, sets the default patcher height in pixels.

setdefaultpatcherwidth
----------------------

The word setdefaultpatcherwidth, followed by an integer value greater than 100, sets the default patcher width in pixels.

seteventinterval
----------------

The word seteventinterval, followed by an integer value, sets the time between invocations of the event-level timer (The default value is 2 milliseconds). The event-level timer handles low priority tasks like drawing user interface updates and playing movies.

setmixergbitmode
----------------

The word setmixergbitmode, followed by a 0, 1 or 2, sets the state of the Enable Mixer Crossfade preference for top-level patcher mixers. A value of 0 sets the preference to `Off`, 1 to `On`, and 2 to `Auto`.

setmixerlatency
---------------

The word setmixerlatency, followed by a number, sets the Mixer Crossfade Latency preference for top-level patcher mixers to the specified number of milliseconds.

setmixerparallel
----------------

The word setmixerparallel, followed by a 0 or 1, disables or enables the Enable Mixer Parallel Processing preference for top-level patcher mixers.

setmixerramptime
----------------

The word setmixerramptime, followed by a number, sets the Mixer Crossfade Ramp Time preference for top-level patcher mixers to the specified number of milliseconds.

setmirrortoconsole
------------------

The word setmirrortoconsole, followed by a 1 or 0, turns on or off (default is 0, off) mirroring of Max Console posts to the system console. The system console is available on the Mac using Console.app, or on Windows using the DbgView program (free download from Microsoft).

setsleep
--------

The word setsleep, followed by a number, sets the time between calls to get the next system event, in 60ths of a second. The default value is 2.

setpollthrottle
---------------

The word setpollthrottle, followed by an integer, sets the maximum number of events the scheduler executes each time it is called (The default value is 20). Setting this value lower may decrease accuracy of timing at the expense of efficiency.

setqueuethrottle
----------------

The word setqueuethrottle, followed by an integer value, sets the maximum number of events handled at low-priority each time the low-priority queue handler is called (The default value is 2). Changing this value may affect the responsiveness of the user interface.

setslop
-------

The word setslop, followed by a floating-point value, sets the scheduler slop value - the amount of time a scheduled event can be earlier than the current time before the time of the event is adjusted to match the current time. The default value is 25 milliseconds.

setsysqelemthrottle
-------------------

The word setsysqelemthrottle, followed by a number, sets the maximum number of patcher UI update events to process at a time. Lower values can lead to more processing power available to other low-priority Max processes, and higher values make the user interface more responsive (especially when using many bpatchers).

showcursor
----------

Shows the cursor if it is hidden.

Shows the menu bar after it has been hidden with hidemenubar.

size
----

Prints the number of symbols in the symbol table in the Max Console.

system
------

The word system, followed by the name of an Operating System (windows or macintosh) and a message, will execute the message if Max is running on the named OS.

useexternaleditor
-----------------

The word useexternaleditor followed by a one (on) or zero (off) toggles using an external editor for text. If enabled, any situation where an external editor can be used will launch the editor. If disabled, an external editor will only be used when selected from the menu.

useslowbutcompletesearching
---------------------------

The word useslowbutcompletesearching, followed by a one (on) or zero (off), toggles complete file searching. When enabled, it causes files not found in Max's cache of the search path to be searched in the file system. This is necessary only in extremely rare cases where the file cache does not update properly. One such case is copying a file into the search path using a version of the Mac OS prior to 10.5.5 over a network. This option may cause patcher files to be loaded more slowly. The setting defaults to off with each launch of the application, and is not stored in the user's preferences. useslowbutcompletesearching 0 turns the setting off.

MIDI Configuration Messages
---------------------------

Messages for creating new MIDI ports:

;#SM createoutport
------------------

_<portname>_ _<drivername>_

Creates a new port for the specified driver. This is only possible on Mac machines. Windows is unsupported. On Mac, specifying the coremidi driver name creates a virtual output port you can use to communicate with other MIDI applications, while specifying the augraph driver name creates another port exclusively assigned to the [DLS synthesizer](https://docs.cycling74.com/max8/vignettes/built_in_midi_synth).

;#SM deleteoutport
------------------

_<portname>_ _<drivername>_

On Mac, deletes a port created with the createoutport message. _drivername_ and _portname_ should be the same as the arguments originally passed to createoutport.

;#SM driver loadbank
--------------------

_<filename>_ _<portname>_

On Mac, loads a type 1 or 2 DLS Bank, where _filename_ is the name of an existing DLS bank file, and _portname_ is the name of the port that will use this bank. If _portname_ is omitted, all DLS ports will use the bank. The folder _/Library/Audio/Sounds/Banks_ is added to the search path when looking for a DLS bank file.

;#SM driver loadbank 0
----------------------

_<portname>_

On Mac, loads the DLS default GM Bank.

;#SM driver reverb
------------------

_<1/0><portname>_

On Mac, turns reverb on or off. By default reverb is off in augraph.

;#SM driver latency
-------------------

_<time>_ _<portname>_

(midi_mme only) Sets the MIDI Output Latency where _time_ is a value in milliseconds and _portname_ is the port that is set to this value.

;#SM inportinfo
---------------

_<portname>_ _<receive name>_

;#SM outportinfo
----------------

_<portname>_ _<receive name>_

The inportinfo and outportinfo messages send information about MIDI ports to named [receive](https://docs.cycling74.com/max8/refpages/receive) objects. The information is contained in an infolist message with the following arguments:

the port's name (symbol)

the port's driver name (symbol)

the port's unique ID (int)

the port's abbreviation (int)

the port's channel offset (int)

whether the port is enabled or disabled (one if enabled, zero if disabled)

whether the port was created dynamically (one if yes, zero if no)

;#SM createinport
-----------------

_<portname>_ _<drivername>_

(Mac only) Adds a virtual MIDI input port, where _portname_ is the name you assign to the port, and _drivername_ should be set to coremidi. Other MIDI applications can send messages to Max using this port.

;#SM deleteinport
-----------------

_<portname>_ _<drivername>_

Deletes a port created with the createinport message. _drivername_ and _portname_ should be the same as the arguments originally passed to createinport.

Ports created with the createoutport and createinport messages are not saved as a part of your MIDI setup preferences.

MIDI Messages
-------------

The word midi, followed by a variable-length message, allows messages to be sent to configure the system MIDI object. These messages need to be prepended with ";max". The following is a list of the available options:

midi portabbrev
---------------

_<innum / outnum>_ _<portname>_ _<abbrev>_

_innum_ specifies an input port, _outnum_ specifies an output port, _portname_ is the name of the port as a single symbol (i.e. It is necessary to use double quotes). An _abbrev_ value is 0 for no abbrev (- in menu), 1 for 'a' and 26 for 'z'.

midi portenable
---------------

_<portname>_ _<0/1>_ _<0/1>_

The first required argument enables (1) or disables (0) the port specified by _portname_. The second argument specifies if the target port is an input port (0, default) or output port (1). All ports are enabled by default.

midi portoffset
---------------

_<innum / outnum>_ _<portname>_ _<offset>_

Similar to portabbrev, but offset is the channel offset added to identify input or output ports when a MIDI object can send to or receive from multiple ports by channel number. Must be a multiple of 16 (e.g. max midi portoffset innum PortA 16 sets the channel offset for PortA device to 16).
