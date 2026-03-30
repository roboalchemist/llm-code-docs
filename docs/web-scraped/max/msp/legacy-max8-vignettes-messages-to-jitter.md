# Source: https://docs.cycling74.com/legacy/max8/vignettes/messages_to_jitter

Title: Controlling Jitter with Messages -  Max 8 Documentation

URL Source: https://docs.cycling74.com/legacy/max8/vignettes/messages_to_jitter

Markdown Content:
Controlling Jitter with Messages
--------------------------------

As is the case with Max, you can control Jitter using the [message box](https://docs.cycling74.com/max8/refpages/message) object. Normally, the [message box](https://docs.cycling74.com/max8/refpages/message) contains an object, and you click on it or replace a variable typed into the [message box](https://docs.cycling74.com/max8/refpages/message) to send a message down a patch cord to another Max object. However, if the message in a message box begins with a semicolon (;) followed by the word jitter, any message which follows will be sent directly to the Max application itself, just as though there were a [receive](https://docs.cycling74.com/max8/refpages/receive) object named "jitter".

Another way this may be accomplished is to send messages via the [forward](https://docs.cycling74.com/max8/refpages/forward) object. The forward object works similar to the send object, but is not restricted to sending to named instances of the [receive](https://docs.cycling74.com/max8/refpages/receive) object.

These messages may be also included in a file named "jitter-config.txt", located anywhere in the search path and they will be executed when Jitter loads. This is particularly useful for the javaload message.

Sending a message to Jitter
---------------------------

*    Add a [message](https://docs.cycling74.com/max8/refpages/message) box to your Patcher, and type in a semicolon and the word jitter (;jitter), followed by the message you want to send. Your message box can contain variables (e.g. ;jitter menubar $1). 

When you click on the [message](https://docs.cycling74.com/max8/refpages/message) box or send it a bang or a value, the message will be sent to the Max application.

Here is listing of the messages you can send using this technique:

cursor
------

(Macintosh only) The word cursor, followed by a zero or one, toggles cursor visibility on/off.

html_ref
--------

The word html_ref, followed by a symbol that specifies the name of a Jitter object, launches the reference file for the object. (must be in Max's search path).

javaload
--------

The word javaload, followed by a zero or one, toggles Jitter Java support on/off.

launch_browser
--------------

The word launch_browser, followed by a URL as a symbol, Launches the specified URL in the default system web browser.

(Macintosh only) The word menubar, followed by a zero or one, toggles menubar visibility on/off. Similar to Max's showmenubar, and hidemenubar messages. When using in conjunction with the [jit.window](https://docs.cycling74.com/max8/refpages/jit.window) object's fullscreen attribute, it is recommended that the [jit.window](https://docs.cycling74.com/max8/refpages/jit.window) object's _fsmenubar_ attribute is used instead of Jitter's menubar message, in order to prevent possible "pixel trash".

parallel
--------

The word parallel, followed by a zero or one, toggles parallel processor support. The default is on if machine has multiple processors (or cores), and otherwise off.

parallelthreads
---------------

The word parallelthreads, followed by an integer, specifies the number of threads used for parallel processor support. Default is the number of processors (or cores).

parallelthresh
--------------

The word parallelthresh, followed by an integer, specifies matrix cellcount above which parallel processors are used. Default is 10000 cells.

pollthrottle
------------

The word pollthrottle, followed by an integer, sets the number of scheduler events to process per scheduler tick. Equivalent to Max's setpollthrottle message.

queuethrottle
-------------

The word queuethrottle, followed by an integer, sets the number of low priority queue events to process per low priority queue service. Equivalent to Max's setqueuethrottle message.
