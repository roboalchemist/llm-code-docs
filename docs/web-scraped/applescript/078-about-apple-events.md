# About Apple Events

# Retired Document
Important:This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

# About Apple Events
This chapter provides an overview of when and how applications use Apple events, with links to more detailed information on those topics. It also provides a brief description of the framework and language support available for working with Apple events in Mac OS X.
AnApple eventis a type of interprocess message that can encapsulate commands and data of arbitrary complexity. Apple events provide a data transport and event dispatching mechanism that can be used within a single application, between applications on the same computer, and between applications on different computers connected to a network. The Mac OS uses Apple events to communicate with applications.
Apple events are part of theOpen Scripting Architecture (OSA), which provides a standard and extensible mechanism for interapplication communication in Mac OS X. The OSA is described inAppleScript Overview.
Note:Apple events are not always the most efficient or appropriate method for communicating between processes. Mac OS X offers other mechanisms, including distributed objects, notifications, sockets, ports, streams, shared memory, and Mach messaging. These mechanisms are described in âInterprocess Communicationâ inSystem-Level TechnologiesinMac Technology Overview.

## A Quick Look at Working With Apple Events
Apple events are designed to provide a flexible mechanism for interprocess communication. An Apple event specifies a target application (or other process) and provides a detailed description of an operation to perform. The operating system locates the target, delivers the event and, if necessary, delivers a reply Apple event back to the sender. While simple in concept, this mechanism provides a basis for powerful interaction between processes and for automating tasks that use multiple applications.

### When Applications Use Apple Events
An application is most likely to work with Apple events for the following reasons:
- To respond to Apple events received from the Mac OS.For applications that present a graphical user interface, Mac OS X sends Apple events to initiate certain operations, such as launching or quitting the application.For Cocoa applications, most of the work of responding to these events happens automatically. Carbon applications need to provide more of their own implementationâfor details, seeHandling Apple Events Sent by the Mac OS.
To respond to Apple events received from the Mac OS.
For applications that present a graphical user interface, Mac OS X sends Apple events to initiate certain operations, such as launching or quitting the application.
For Cocoa applications, most of the work of responding to these events happens automatically. Carbon applications need to provide more of their own implementationâfor details, seeHandling Apple Events Sent by the Mac OS.
- To make its services or data available to other processes.Most applications that provide services through Apple events are scriptable applicationsâthey provide a scripting terminology that lets users write AppleScript scripts to access the applicationâs operations and data. When a script is executed, some of its statements result in Apple events being sent to the application. Other applications can also send Apple events directly to scriptable applications.Scriptable applications make it possible for users to automate their work. And starting in Mac OS X version 10.4, your scriptable application can also provide users with Automator actions. (Automator is an application that lets users work in a graphical interface to put together complex, automated workflows, made up of actions that perform discrete operations.)Scriptable Carbon applications can use the techniques for working with Apple events that are described throughout this document. For information on scriptable Cocoa applications, seeFramework and Language Support.For information on designing and creating scriptable applications, and on creating Automator actions, see the learning paths inGetting Started with AppleScript.
To make its services or data available to other processes.
Most applications that provide services through Apple events are scriptable applicationsâthey provide a scripting terminology that lets users write AppleScript scripts to access the applicationâs operations and data. When a script is executed, some of its statements result in Apple events being sent to the application. Other applications can also send Apple events directly to scriptable applications.
Scriptable applications make it possible for users to automate their work. And starting in Mac OS X version 10.4, your scriptable application can also provide users with Automator actions. (Automator is an application that lets users work in a graphical interface to put together complex, automated workflows, made up of actions that perform discrete operations.)
Scriptable Carbon applications can use the techniques for working with Apple events that are described throughout this document. For information on scriptable Cocoa applications, seeFramework and Language Support.
For information on designing and creating scriptable applications, and on creating Automator actions, see the learning paths inGetting Started with AppleScript.
- To communicate directly with other applications.An application can send an Apple event to ask another application to perform an operation or return data. For example, you might create a scriptable server application, running locally or remotely. Your other applications create Apple events and send them to the scriptable server to access its services. This is, in effect, another way to factor your code, with the shared functionality made available through Apple events.
To communicate directly with other applications.
An application can send an Apple event to ask another application to perform an operation or return data. For example, you might create a scriptable server application, running locally or remotely. Your other applications create Apple events and send them to the scriptable server to access its services. This is, in effect, another way to factor your code, with the shared functionality made available through Apple events.
- To support recording in a scriptable application.Recordingrefers to the assemblingof Apple events that represent a userâs actions into a script. Users can turn on recording in the Script Editor application, then perform actions with scriptable applications that support recording. Any Apple events generated by those actions are recorded into an AppleScript script. To support recording as fully as possible, you can take these steps:Factor code that implements the user interface in your application from code that actually performs operationsâthis is a standard approach for applications that follow the model-view-controller design paradigm.Send Apple events within the application to connect these two parts of your application. The Apple Event Manager provides a mechanism for doing this with a minimum of overhead, described inAddressing an Apple Event for Direct Dispatching.Make sure that any significant action within your application generates an Apple event that can be recorded in a script.Recording is beyond the scope of this document, but you can read more about it in the sectionsâRecordable ApplicationsâandâMaking Your Application RecordableâinInside Macintosh: Interapplication Communication.
To support recording in a scriptable application.
Recordingrefers to the assemblingof Apple events that represent a userâs actions into a script. Users can turn on recording in the Script Editor application, then perform actions with scriptable applications that support recording. Any Apple events generated by those actions are recorded into an AppleScript script. To support recording as fully as possible, you can take these steps:
- Factor code that implements the user interface in your application from code that actually performs operationsâthis is a standard approach for applications that follow the model-view-controller design paradigm.
Factor code that implements the user interface in your application from code that actually performs operationsâthis is a standard approach for applications that follow the model-view-controller design paradigm.
- Send Apple events within the application to connect these two parts of your application. The Apple Event Manager provides a mechanism for doing this with a minimum of overhead, described inAddressing an Apple Event for Direct Dispatching.
Send Apple events within the application to connect these two parts of your application. The Apple Event Manager provides a mechanism for doing this with a minimum of overhead, described inAddressing an Apple Event for Direct Dispatching.
- Make sure that any significant action within your application generates an Apple event that can be recorded in a script.
Make sure that any significant action within your application generates an Apple event that can be recorded in a script.
Recording is beyond the scope of this document, but you can read more about it in the sectionsâRecordable ApplicationsâandâMaking Your Application RecordableâinInside Macintosh: Interapplication Communication.

### Apple Event Terminology
A scriptable application specifies the terminology that can be used in scripts that target the application. There are currently three formats for this information:
- aete:This is the original dictionary format and is still used in Carbon applications. The name comes from the Resource Manager resource type in which the information is stored ('aete').
aete:This is the original dictionary format and is still used in Carbon applications. The name comes from the Resource Manager resource type in which the information is stored ('aete').
- script suite:This is the original format used by Cocoa applications. A script suite contains a pair of information property list (plist) files.
script suite:This is the original format used by Cocoa applications. A script suite contains a pair of information property list (plist) files.
- sdef:âsdefâ is short for âscripting definition.â This XML-based format is a superset of the other two formats and supports additional features.
sdef:âsdefâ is short for âscripting definition.â This XML-based format is a superset of the other two formats and supports additional features.
For more information on these formats, including pointers to additional documentation, see "Scriptable Applications" inOpen Scripting ArchitectureinAppleScript Overview.

### Sending and Receiving Apple Events
Applications typically use Apple events to request services and information from other applications or to provide services and information in response to such requests. In client-server terms, theclient applicationsends an Apple event to request a service or information from theserver application. The recipient of an Apple event is also known as thetarget applicationbecause it is the target of the event. A client application must know which kinds of Apple events the server supports.
Figure 1-1shows two applications communicating with Apple events. The client uses Apple Event Manager functions to create and send an Apple event to the server, the FileMaker Pro database application. The event might, for example, request employee information from a payroll database. FileMaker Pro uses other Apple Event Manager functions to extract information from the event and identify the requested operation. Depending on the event, FileMaker Pro may need to add a record, delete a record, or return specified information in a reply Apple event.
The most common Apple event client is a script editor application executing an AppleScript script. Statements in a script that target an application may result in Apple events being sent to the application. Another common client is the Mac OS, which sends Apple events to applications to open documents and perform other operations.
The most common servers are scriptable applications and scriptable parts of the Mac OS, such as the Finder and the System Events application (located in/System/Library/CoreServices). You can read more about script editors and scriptable applications inAppleScript Overview.

### Responding to Apple Events
Your application should be prepared to respond to Apple events sent by the Mac OS, as well as to other Apple events the application supports. An Apple event typically contains information that specifies the target application, the action to perform, and optionally the objects on which to operate. For example,Figure 1-2shows anopen documentsApple event sent by Mac OS X to the AppleWorks application. This type of Apple event provides a list of files for the target application to open.
For an application to handle a specific Apple event such as theopen documentsevent, it must register with the Apple Event Manager a function that handles events of that type. The Apple Event Manager dispatches a received Apple event to the handler registered for it. AnApple event handleris an application-defined function that extracts pertinent data from an Apple event, performs the requested action, and if necessary, returns a result.

## How to Use Apple Events
The steps your application takes in working with Apple events will differ, depending on whether it is responding to Apple events or creating and sending them.

### Steps for Responding to Apple Events
To respond to Apple events in your application, you perform steps like the following:
- Determine which Apple events your application will support.
Determine which Apple events your application will support.
- Make sure your application can receive Apple events and dispatch them to a function that can handle them.Write functions that handle the Apple events you support.Register the functions with the Apple Event Manager so it can dispatch events to them.
Make sure your application can receive Apple events and dispatch them to a function that can handle them.
- Write functions that handle the Apple events you support.
Write functions that handle the Apple events you support.
- Register the functions with the Apple Event Manager so it can dispatch events to them.
Register the functions with the Apple Event Manager so it can dispatch events to them.
- Call Apple Event Manager functions to extract information from received Apple events and locate specified items in your application.Note:Locating objects in your application is not covered in this documentâfor details, seeâResolving and Creating Object Specifier RecordsâinInside Macintosh: Interapplication Communication.
Call Apple Event Manager functions to extract information from received Apple events and locate specified items in your application.
Note:Locating objects in your application is not covered in this documentâfor details, seeâResolving and Creating Object Specifier RecordsâinInside Macintosh: Interapplication Communication.
- Perform the actions specified by received Apple events.
Perform the actions specified by received Apple events.
- If necessary, add information to a reply Apple event (sent to you as part of a received Apple event).If an error occurs, return an error code; you can also add error information to the reply event.
If necessary, add information to a reply Apple event (sent to you as part of a received Apple event).
If an error occurs, return an error code; you can also add error information to the reply event.
For guidelines and sample code for performing these steps, seeApple Event DispatchingandResponding to Apple Events.

### Steps for Creating and Sending Apple Events
To create and send Apple events in your application, you perform steps like the following:
- Create an Apple event.The Apple Event Manager provides functions for building an Apple event in one step and for creating an Apple event and adding information to it as a sequence of steps.
Create an Apple event.
The Apple Event Manager provides functions for building an Apple event in one step and for creating an Apple event and adding information to it as a sequence of steps.
- Send the Apple event.The Apple Event Manager provides functions for sending an event with more options and more overhead, or with less options and less overhead.You will have to specify information such asthe target application to send the Apple event tohow to handle a timeout (in case the target doesnât respond)whether to allow interaction with the user (for example, if the Apple event might result in showing a dialog)
Send the Apple event.
The Apple Event Manager provides functions for sending an event with more options and more overhead, or with less options and less overhead.
You will have to specify information such as
- the target application to send the Apple event to
the target application to send the Apple event to
- how to handle a timeout (in case the target doesnât respond)
how to handle a timeout (in case the target doesnât respond)
- whether to allow interaction with the user (for example, if the Apple event might result in showing a dialog)
whether to allow interaction with the user (for example, if the Apple event might result in showing a dialog)
For guidelines and sample code for performing these steps, seeTwo Approaches to Creating an Apple EventandCreating and Sending Apple Events.

## Framework and Language Support
You work with Apple events primarily through the API defined by the Apple Event Manager, which is documented inApple Event Manager Reference. This API is implemented by the AE framework, a subframework of the Application Services framework, and is made available through headers written in the C programming language.
Note:The Apple Event Manager is part of the Open Scripting Architecture. Some Apple-event related functions and constants are not defined in the AE frameworkâthey are defined in other frameworks, as described inOpen Scripting Architectureâ inAppleScript Overview.
Carbon applications that work with Apple events, whether written in C or C++, typically call Apple Event Manager functions directly. Apple also provides C sample code, such asMoreOSL, to help in the implementation of scriptable Carbon applications.
Cocoa applications are written in Objective-C or Java. The Cocoa application framework provides built-in support for AppleScript scripting that allows many applications to be scriptable without working directly with Apple Event Manager functions. The Cocoa application framework also includes classes such asNSAppleEventDescriptor, for working with underlying Apple event data structures, andNSAppleEventManager, for accessing certain Apple Event Manager functions.
However, because Objective-C is a super set of the C language, Cocoa applications written in Objective-C can call Apple Event Manager functions directly and use any of the mechanisms described in this document. For example, a Cocoa application might use Apple Event Manager functions to perform operations that are not currently supported by the Cocoa framework, such as directly sending an Apple event. For details on writing a scriptable Cocoa application, seeCocoa Scripting Guide.
Copyright © 2005, 2007 Apple Inc. All Rights Reserved.Terms of Use|Privacy Policy|  Updated: 2007-10-31