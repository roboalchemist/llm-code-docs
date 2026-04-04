# Source: https://jackaudio.org/

JACK-AUDIO-CONNECTION-KIT   
---  
  
  * [Main Page](index.html)
  * [Related Pages](pages.html)
  * [Modules](modules.html)
  * [Data Structures](annotated.html)
  * [Files](files.html)
  * ![](search/mag_sel.svg) [![](search/close.svg)](javascript:searchBox.CloseResultsWindow\(\))




JACK Audio Connection Kit 

#  Introduction

JACK is a low-latency audio server, written for any operating system that is reasonably POSIX compliant. It currently exists for Linux, OS X, Solaris, FreeBSD and Windows. It can connect several client applications to an audio device, and allow them to share audio with each other. Clients can run as separate processes like normal applications, or within the JACK server as "plugins".

JACK was designed from the ground up for professional audio work, and its design focuses on two key areas: synchronous execution of all clients, and low latency operation.

See also
    <http://jackaudio.org>

#  JACK Overview

Traditionally it has been hard if not impossible to write audio applications that can share data with each other. In addition, configuring and managing audio interface hardware has often been one of the most complex aspect of writing audio software.

JACK changes all this by providing an API that does several things: 
    
    
    1. provides a high level abstraction for programmers that
       removes the audio interface hardware from the picture and
       allows them to concentrate on the core functionality of
       their software.
    
    2. allows applications to send and receive audio data to/from
       each other as well as the audio interface. There is no
       difference in how an application sends or receives
       data regardless of whether it comes from/goes to another application 
       or an audio interface.
    

For programmers with experience of several other audio APIs such as PortAudio, Apple's CoreAudio, Steinberg's VST and ASIO as well as many others, JACK presents a familiar model: your program provides a "callback" function that will be executed at the right time. Your callback can send and receive data as well as do other signal processing tasks. You are not responsible for managing audio interfaces or threading, and there is no "format negotiation": all audio data within JACK is represented as 32 bit floating point values.

For those with experiences rooted in the Unix world, JACK presents a somewhat unfamiliar API. Most Unix APIs are based on the read/write model spawned by the "everything is a file" abstraction that Unix is rightly famous for. The problem with this design is that it fails to take the realtime nature of audio interfaces into account, or more precisely, it fails to force application developers to pay sufficient attention to this aspect of their task. In addition, it becomes rather difficult to facilitate inter-application audio routing when different programs are not all running synchronously.

Using JACK within your program is very simple, and typically consists of just:

  * calling [jack_client_open()](group__ClientFunctions.html#gabbd2041bca191943b6ef29a991a131c5) to connect to the JACK server.
  * registering "ports" to enable data to be moved to and from your application.
  * registering a "process callback" which will be called at the right time by the JACK server.
  * telling JACK that your application is ready to start processing data.



There is a lot more that you can do with JACK's interfaces, but for many applications, this is all that is needed. The simple_client.c example demonstrates a complete (simple!) JACK application that just copies the signal arriving at its input port to its output port. Similarly, inprocess.c shows how to write an internal client "plugin" that runs within the JACK server process.

#  Reference

The JACK programming interfaces are described in several header files. We present them here broken into useful categories to make the API a little clearer:

  * [Creating & manipulating clients](group__ClientFunctions.html)
  * [Setting Client Callbacks](group__ClientCallbacks.html)
  * [Creating and managing client threads](group__ClientThreads.html)
  * [Controlling & querying JACK server operation](group__ServerControl.html)
  * [Creating & manipulating ports](group__PortFunctions.html)
  * [Looking up ports](group__PortSearching.html)
  * [Managing and determining latency](group__LatencyFunctions.html)
  * [Handling time](group__TimeFunctions.html)
  * [Transport and Timebase control](group__TransportControl.html)
  * [Controlling error/information output](group__ErrorOutput.html)
  * [The non-callback API](group__NonCallbackAPI.html)
  * [Reading and writing MIDI data](group__MIDIAPI.html)
  * [Session API for clients.](group__SessionClientFunctions.html)
  * [managing support for newer/older versions of JACK](group__WeakLinkage.html)
  * [the API for starting and controlling a JACK server](group__ControlAPI.html)
  * [Metadata API.](group__Metadata.html)



The full API is described in:

  * [<jack/jack.h>](jack_8h.html) is the main JACK interface.
  * [<jack/statistics.h>](statistics_8h.html) provides interfaces for monitoring the performance of a running JACK server.
  * [<jack/intclient.h>](intclient_8h.html) allows loading and unloading JACK internal clients.
  * [<jack/ringbuffer.h>](ringbuffer_8h.html) defines a simple API for using lock-free ringbuffers. These are a good way to pass data between threads, when streaming realtime data to slower media, like audio file playback or recording.
  * [<jack/transport.h>](transport_8h.html) defines a simple transport control mechanism for starting, stopping and repositioning clients. This is described in the [JACK Transport Design](transport-design.html) document.
  * [<jack/types.h>](types_8h.html) defines the main JACK data types.
  * [<jack/thread.h>](thread_8h.html) functions standardize thread creation for JACK and its clients.
  * [<jack/midiport.h>](midiport_8h.html) functions to handle reading and writing of MIDI data to a port
  * [<jack/session.h>](session_8h.html) functions that form the JACK session API
  * [<jack/control.h>](control_8h.html) the API for starting and controlling a JACK server
  * [<jack/metadata.h>](metadata_8h.html) the API for managing metadata about objects within JACK (clients and ports)



In addition, the tools directory provides numerous examples of simple JACK clients that nevertheless use the API to do something useful. It includes

  * a metronome.
  * a recording client that can capture any number of channels from any JACK sources and store them as an audio file.
  * command line clients to control the transport mechanism, change the buffer size and more.   

  * commands to load and unload JACK internal clients.
  * tools for checking the status of a running JACK system.



and many more.

#  Porting

JACK is designed to be portable to any system supporting the relevant POSIX and ANSI C standards. It currently runs under GNU/Linux, Mac OS X and Berkeley Unix on several different processor architectures. If you want to port JACK to another platform, please read the [Porting JACK](porting-guide.html) document.

#  License

Copyright (C) 2001-2019 by Paul Davis, Stephane Letz, Jack O'Quinn, Torben Hohn, Filipe Coelho and others.

JACK is free software; you can redistribute it and/or modify it under the terms of the GNU GPL and LGPL licenses as published by the Free Software Foundation, <http://www.gnu.org>. The JACK server uses the GPL, as noted in the source file headers. However, the JACK library is licensed under the LGPL, allowing proprietary programs to link with it and use JACK services. You should have received a copy of these Licenses along with the program; if not, write to the Free Software Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. 

* * *

Generated by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.9.1 
