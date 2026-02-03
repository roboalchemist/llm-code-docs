# Testing and Debugging Apple Event Code

# Retired Document
Important:This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

# Testing and Debugging Apple Event Code
To test and debug your Apple event code you can generally use the same techniques and tools you use with any code. For example, Xcode contains a full-featured source-level debugger that lets you set breakpoints and step through your code line by line. For C, C++, and Objective-C code, Xcode uses GDB, the debugger from theGNU Project. You can use Xcodeâs graphical interface to GDB or you can enter commands directly into the GDB console. For more information, see âDebuggingâ in Xcode Help andDebugging With GDB.
The remainder of this chapter provides tips that are specific to debugging code that works with Apple events.

## Determining If an Application Is Receiving Apple Events
The easiest way to determine if your application is receiving a particular event is to set a breakpoint in the event handler for that event, then send an event of that type to your application. There are several ways to send Apple events to your application:
- You can create and send events that target your application from within the application itself or from a test application. For more information, seeCreating and Sending Apple Events. This approach can be useful if youâre setting up a test suite and want to thoroughly test how your application responds to a variety of events.
You can create and send events that target your application from within the application itself or from a test application. For more information, seeCreating and Sending Apple Events. This approach can be useful if youâre setting up a test suite and want to thoroughly test how your application responds to a variety of events.
- You can use Script Editor to send Apple events to your application.For example, you can execute this one-line script to send your application aquitevent:Listing 8-1A simple script to quit an applicationtell app "MyApplication" to quitIf your application is scriptable, you may prefer to set up a test suite of scripts to thoroughly exercise the events you support, rather than perform the same task in a test application.For additional information on sending Apple events with Script Editor, seeScript Editor is an Apple Event Test Tool.
You can use Script Editor to send Apple events to your application.
For example, you can execute this one-line script to send your application aquitevent:
Listing 8-1A simple script to quit an application
```
    tell app "MyApplication" to quit```
If your application is scriptable, you may prefer to set up a test suite of scripts to thoroughly exercise the events you support, rather than perform the same task in a test application.
For additional information on sending Apple events with Script Editor, seeScript Editor is an Apple Event Test Tool.
- You can use the Mac OS to send Apple events to your application.For example, you can select an application document in the Finder and double-click it to send anopen documentsevent to the application. SeeHandling Apple Events Sent by the Mac OSfor a list of the events the Mac OS sends to applications.
You can use the Mac OS to send Apple events to your application.
For example, you can select an application document in the Finder and double-click it to send anopen documentsevent to the application. SeeHandling Apple Events Sent by the Mac OSfor a list of the events the Mac OS sends to applications.
What if youâre sending events to your application, but the debugger never reaches the breakpoints you set in your Apple event code? One simple approach is to install a single Apple event handler with the event type and event class set totypeWildCard. Any Apple event your application receives will be dispatched to this handler, so a breakpoint in the handler should allow you to verify whether the application is actually receiving events.
Once you know your application is receiving events, you can take a closer look at the events using the information provided inExamining Apple Events. That information is also useful if you never hit the breakpoint in your wildcard handler. For example, you can examine the test events you are sending to see if they correctly target your application.

## Script Editor is an Apple Event Test Tool
The Script Editor application, located in/Applications/AppleScript, is a useful tool for working with Apple events. If your application is scriptable, you can use Script Editor to write and execute scripts that target your application, resulting in Apple events being sent to the application.
Even if your application is not fully scriptable, you can use Script Editor to send it events such as theopen applicationandquitevents that your application usually receives from the Mac OS.Listing 8-1shows an example of this.
In addition, you can use Script Editor to construct and send Apple events using raw format, in which you enclose actual four-character codes in special characters to specify an event. For example,Listing 8-2shows how to use the raw format to send anopen locationcommand to the Safari application and open the specified web page.
Listing 8-2Sending a raw event to open an URL
```
tell application "Safari"```
```
    Â«event GURLGURLÂ» "http://www.apple.com/"```
```
end tell```
When you compile this script, Script Editor examines Safariâs scripting dictionary and converts the second line to this:
```
    open location "http://www.apple.com/"```
However, for an application that doesnât have a scripting dictionary, the raw code is not replaced by an equivalent term, but the Apple event can still be sent and understood (if the application supports it).
You enter the special characters that surround the raw code (called double angle brackets or guillemets) by typing Option-\ and Option-Shift-\. For additional information, seeDouble Angle Brackets in Results and ScriptsinAppleScript Language Guide.
Turning on Apple Event Loggingshows how you can examine the Apple events Script Editor sends and receives.
Note:The following features can also be useful in debugging your Apple event code:
You can execute AppleScript scripts from shell scripts and shell scripts from AppleScript scripts, which may come in handy for automating your testing. For more information, see âUsing AppleScript With Other Scripting Systemsâ inAppleScript Overview.
In addition, Xcode provides a build phase in which you can execute AppleScript scripts, and Xcode itself is scriptable. For additional information, see Xcode Help.

## Examining Apple Events
There are several available mechanisms for examining the contents of Apple events that your application sends and receives.

### Turning on Apple Event Logging
You can set environment variables in a Terminal window so that any Apple events sent or received by an application launched in that window are logged to the window in a human-readable format.Listing 8-4shows how you would do this if youâre working with the C shell.
Listing 8-3Turning on logging for sent and received Apple events in the C shell
```
%setenv AEDebugSends 1; setenv AEDebugReceives 1```
If you are using thebashshell you, you can use the form shown inListing 8-4.
Listing 8-4Turning on Apple event logging in the Bash shell
```
%export AEDebugSends=1; export AEDebugReceives=1```
To see which Apple events an application sends and receives, you set these environment variables, then launch the application in a Terminal window. For example, to see what events the Script Editor application sends, you can execute the line inListing 8-5. Once the Script Editor launches, you can compile and execute scripts and examine, in the Terminal window, the Apple events that are generated.
Listing 8-5Launching Script Editor in Terminal
```
% /Applications/AppleScript/Script\ Editor.app/Contents/MacOS/Script\ Editor```
Important:To launch an application in Terminal, you provide the full path to its executable, which is typically located inside the application bundle, rather than the path to the application itself.
Listing 8-6shows how to perform the same task with the Finder, a scriptable application that may send Apple events to your application.
Listing 8-6Launching Finder in Terminal
```
% /System/Library/CoreServices/Finder.app/Contents/MacOS/Finder```
This technique for examining Apple events works for both Carbon and Cocoa applications. For example,Listing 8-7shows the output for areopenApple event sent to a Carbon application when you click on its icon in the Dock.
Listing 8-7Output of a reopen Apple event in Terminal
```
AE2000 (968): Received an event:```
```
------oo start of event oo------```
```
{ 1 } 'aevt':  aevt/rapp (ppc ){```
```
          return id: 22609967 (0x159002f)```
```
     transaction id: 0 (0x0)```
```
  interaction level: 112 (0x70)```
```
     reply required: 0 (0x0)```
```
             remote: 0 (0x0)```
```
  target:```
```
    { 1 } 'psn ':  8 bytes {```
```
      { 0x0, 0x60001 } (Dock)```
```
    }```
```
  optional attributes:```
```
    { 1 } 'reco':  - 1 items {```
```
      key 'optk' -```
```
        { 1 } 'list':  - 1 elements {```
```
          { 1 } 'keyw':  4 bytes {```
```
            'frnt'```
```
          }```
```
        }```
```
    }```
```
 ```
```
  event data:```
```
    { 1 } 'aevt':  - 1 items {```
```
      key 'frnt' -```
```
        { 1 } 'bool':  1 bytes {```
```
          false```
```
        }```
```
    }```
```
}```
```
------oo  end of event  oo------```
From the formatted output inListing 8-7, you can identify various information in the Apple event. For example,aevt/rappis the event class/event ID pair for the event. You can look up these values in the Apple Event Manager headers and see that'rapp'is the value of the constantkAEReopenApplication, defined inAERegistry.h. For this event, no reply is required (reply required: 0), but if a reply were required, the target would be the Dock (target: { 1 } 'psn ':  8 bytes { { 0x0, 0x60001 } (Dock) }), which sent the Apple event.
Although Apple event log information can be somewhat cryptic, you can see that the event contains an optional attribute containing boolean data with the value false and the key'frnt'. This indicates that the application was not frontmost at the time thereopenevent was sent (when you clicked the application icon in the Dock). If the application is in front, the event data will contain the valuefalse.
Note:For Cocoa applications, you can display additional formatted output for Apple events using the mechanism described in âTurn On Debugging Output for Scriptingâ inKey Steps for Creating Scriptable ApplicationsinCocoa Scripting Guide.

### Observing Apple Events for Multiple Applications
You can open multiple Terminal windows, turn on debugging output in each, and debug your own application and other applications that it sends Apple events to or receives Apple events from at the same time.

### Setting Breakpoints and Printing Apple Events in GDB
The GDB debugger provides acallcommand that you can use to call routines such as Apple Event Manager functions. The sectionâUsing AEPrint* with GDBâin Technical Note TN2106,AEBuild*, AEPrint*, and Friends, shows how you can set breakpoints in GDB and print out the contents of Apple events in a readable format. While this approach is a little more complex, it provides a good example of setting breakpoints on Apple Event Manager routines and examining Apple events.

### Third Party Options
There are a number of third-party tools, some of them quite powerful, for monitoring and debugging Apple events and scriptable applications. You can find some of them listed atAppleScript Resources.
Copyright © 2005, 2007 Apple Inc. All Rights Reserved.Terms of Use|Privacy Policy|  Updated: 2007-10-31