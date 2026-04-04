# Open Scripting Architecture

TheOpen Scripting Architecture (OSA)provides a standard and extensible mechanism for interapplication communication in OS X. Communication takes place through the exchange of Apple events, a type of message designed to encapsulate commands and data of any complexity.
Apple events provide an event dispatching and data transport mechanism that can be used within a single application, between applications on the same computer, and between applications on different computers. The OSA defines data structures, a set of common terms, and a library of functions, so that applications can more easily create and send Apple events, as well as receive them and extract data from them.
Note:Apple events are not always the most efficient or appropriate mechanism for communicating between processes. OS X offers other mechanisms, including distributed objects, notifications, sockets, ports, streams, shared memory, and Mach messaging. These mechanisms are described in âIPC and Notification Mechanismsâ inKernel and Device Drivers LayerinMac Technology Overview.
The OSA supports several powerful features in OS X:
- the ability to create scriptable applications (described inScriptable Applications)
the ability to create scriptable applications (described inScriptable Applications)
- the ability for users to write scripts that combine operations from multiple scriptable applications
the ability for users to write scripts that combine operations from multiple scriptable applications
- the ability to communicate between applications with Apple events
the ability to communicate between applications with Apple events

## The Parts of the Open Scripting Architecture
Applications that need full access to the Open Scripting Architecture can get it by linking with the Carbon framework. Some applications that work with Apple events (especially those with minimal user interface requirements) may be able to obtain all the services they need by linking to the Core Services framework.
Note:Aframeworkis a type of bundle (or directory in the file system) that packages software with the resources that software requires, including the headers that define its interface. Frameworks are typically located in/System/Library/Frameworks, though they may be nested inside other frameworks.
The Open Scripting Architecture is made up of the following parts:
- TheApple Event Managerprovides an API for sending and receiving Apple events and working with the information they contain. It supplies the underlying support for creating scriptable applications. It is implemented inAE.framework, a subframework ofCoreServices.framework. (Prior to OS X version 10.5, theAE.frameworkwas a subframework ofApplicationServices.framework.)This framework also defines constants that developers can use to support a standard vocabulary for Apple events among different applications.For API documentation, seeApple Event Manager Reference. For conceptual documentation and code samples, seeApple Events Programming Guide.
TheApple Event Managerprovides an API for sending and receiving Apple events and working with the information they contain. It supplies the underlying support for creating scriptable applications. It is implemented inAE.framework, a subframework ofCoreServices.framework. (Prior to OS X version 10.5, theAE.frameworkwas a subframework ofApplicationServices.framework.)
This framework also defines constants that developers can use to support a standard vocabulary for Apple events among different applications.
For API documentation, seeApple Event Manager Reference. For conceptual documentation and code samples, seeApple Events Programming Guide.
- TheCarbon umbrella frameworkincludes the HIToolbox framework, which in turn defines certain functions used in processing and sending Apple events (for example, in the header fileInteraction.h).
TheCarbon umbrella frameworkincludes the HIToolbox framework, which in turn defines certain functions used in processing and sending Apple events (for example, in the header fileInteraction.h).
- TheOpen Scripting frameworkdefines standard data structures, routines, and resources for creating scripting components, which support scripting languages. Because of its standard interface, applications can interact with any scripting component, regardless of its language. This framework provides API for compiling, executing, loading, and storing scripts. It is implemented inOpenScripting.framework, a subframework ofCarbon.framework.For documentation, seeOpen Scripting Architecture Reference.
TheOpen Scripting frameworkdefines standard data structures, routines, and resources for creating scripting components, which support scripting languages. Because of its standard interface, applications can interact with any scripting component, regardless of its language. This framework provides API for compiling, executing, loading, and storing scripts. It is implemented inOpenScripting.framework, a subframework ofCarbon.framework.
For documentation, seeOpen Scripting Architecture Reference.
- The AppleScript component (inSystem/Library/Components) implements the AppleScript language, which provides a way for scripts to control scriptable applications.The AppleScript language is described inAppleScript Language Guide, as well as in a number of third-party books.
The AppleScript component (inSystem/Library/Components) implements the AppleScript language, which provides a way for scripts to control scriptable applications.
The AppleScript language is described inAppleScript Language Guide, as well as in a number of third-party books.

## Apple Events
The Apple event is the basic message for interprocess communication in the Open Scripting Architecture. With Apple events, you can gather all the data necessary to accomplish a high level task into a single package that can be passed across process boundaries, evaluated, and returned with results.
An Apple event consists of a series of nested data structures, each identified by one or more four-character codes (also referred to as Apple event codes). These data structures, as well as the codes and the header files in which they are defined, are described inApple Events Programming Guide. That document also provides conceptual information about Apple events and programming examples that work with them. For a list of four-character codes and their related terminology used by Apple, seeAppleScript Terminology and Apple Event Codes Reference. Your application can reuse these terms and codes whenever it performs an equivalent function.

## Apple Events Sent by the Mac OS
The Mac OS takes advantage of Apple events to communicate with applications, such as to notify an application that it has been launched or should open or print a list of documents. Applications that present a graphical user interface must be able to respond to whichever of these events make sense for the application. For example, all such applications can be launched and quit, but some may not be able to open or print documents.
For detailed information on the events sent by the Mac OS and how to respond to them, see:
- For Carbon applications: âHandling Events Sent by the Mac OSâ inResponding to Apple EventsinApple Events Programming Guide.
For Carbon applications: âHandling Events Sent by the Mac OSâ inResponding to Apple EventsinApple Events Programming Guide.
- For Cocoa applications:How Cocoa Applications Handle Apple EventsinCocoa Scripting Guide.
For Cocoa applications:How Cocoa Applications Handle Apple EventsinCocoa Scripting Guide.

## Script Execution in the Open Scripting Architecture
The Open Scripting Architecture allows users to control multiple applications with scripts written in a variety of scripting languages. Each scripting language has a corresponding scripting component. The AppleScript component supports the AppleScript language. When a scripting component executes a script, statements in the script may result in Apple events being sent to applications.
Although AppleScript is the most widely used language (and the only one provided by Apple), developers are free to use the Open Scripting Architecture to create scripting components for other scripting languages. Depending on the implementation, scripts written in these languages may be able to communicate with scriptable applications.
Figure 1shows what happens when theScript Editorapplication executes an AppleScript script that targets the Mail application. Script Editor calls functions in the Open Scripting framework. The Open Scripting framework communicates through the AppleScript component, which in turn uses the Apple Event Manager to send any required Apple events to the Mail application. If a reply is requested, the Mail application returns information in a reply Apple event.
Applications can also call Apple Event Manager functions directly to send Apple events to other applications and get replies from them (not shown inFigure 1).

## Extending AppleScript with Coercions, Scripting Additions, and Faceless Background Applications
Developers can extend AppleScript by creating bundles that provide command handlers and coercion handlers. The bundles can be applications or scripting additions. However, in many cases the best solution for extending AppleScript is to provide features through a faceless background applicationâthat is, a sort of invisible server application.

### Coercions
Coercionis the process of converting the information in an Apple event from one type to another. Acoercion handleris a function that provides coercion between two (or possibly more) data types. OS X provides default coercion between many standard types. For a complete listing, seeDefault Coercion HandlersinApple Events Programming Guide.
Coercion is available to both scripts and applications. In a script, for example, the following statement coerces the numeric value 1234 to the string value â1234â.

```applescript
set myString to 1234 as text
```

A scriptable application can specify a type when it uses an Apple Event Manager function to extract data from an Apple event. If the data is not already in the specified type, the Apple Event Manager will attempt to coerce it to that type. An application can provide coercion handlers for its own data types, as described inWriting and Installing Coercion HandlersinApple Events Programming Guide.

### Scripting Additions
Ascripting additionis a file or bundle that provides AppleScript commands or coercions. A single scripting addition can contain multiple handlers. For example, the Standard Additions scripting addition in OS X (filenameStandardAdditions.osax), includes commands for using the Clipboard, obtaining the path to a file, speaking text, executing shell scripts, and more. The commands provided by the Standard Additions are available to all scripts. To see what terminology a scripting addition provides, you can examine its dictionary, as described inDisplaying Scripting Dictionaries.
Terms introduced by scripting additions exist in the same name space as AppleScript terms and application-defined terms. While this has the advantage of making a service globally available, it also means that terms from scripting additions can conflict with other terms, polluting the global name space. Debugging scripting additions can also be difficult. Because you can not simply set breakpoints in your own code, you may need to use sampling, profiling, and various other tools to determine where a problem lies. (SeeFaceless Background Applicationsfor an approach that avoids these problems.)
A scripting addition provides its services by installing event handlers (for commands) or coercion handlers (for coercions) in an applicationâs system dispatch tables. The handlers for the Standard Additions (and for any other scripting additions installed by the Mac OS in/System/Library/ScriptingAdditions) get installed if the application calls API in the Open Scripting framework, or if the application specifically loads a scripting addition. An application can also specifically load other scripting additions from other locations.
For information on writing scripting additions, see Technical Note TN1164,Native Scripting Additions. For information on loading scripting additions, see Technical Q&A QA1070,Loading Scripting Additions Without Initializing Apple Script in OS X.

### Faceless Background Applications
A faceless background application (now more commonly referred to as an agent), is one that, as its name implies, runs in the background and has no visible user interface. By creating a scriptable agent, you can provide services without some of the disadvantages of scripting additions. For example, you can develop and debug in a standard application environment, and any terminology you provide does not pollute the global name spaceâit is available only within a scriptâstellstatement that targets the agent.
You can install your agent directly, but if it is intended for use with another application, you can put it in theResourcesfolder of the application it supports. That promotes ease of use by allowing a drag-and-drop installation process, and will minimize users stumbling across the agent and asking âWhat is this for?â The agent will be launched whenever it is referenced in atellstatement. It can be told to quit, and you can also set it up to time out, so it can get unloaded when it is no longer in use.
Apple provides a number of scriptable services through agents, as described inSystem Events and GUI Scripting,Image Events, andDatabase Events. For example, scripts can use the System Events application to perform operations on property list files.
Copyright © 2002, 2007 Apple Inc. All Rights Reserved.Terms of Use|Privacy Policy|  Updated: 2007-10-31