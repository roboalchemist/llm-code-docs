# Scriptable Applications

# Scriptable Applications
Ascriptable applicationis one that goes beyond the basics of responding to Apple events sent by the Mac OS to make its most important data and operations available to AppleScript scripts or to other applications. To do this, the application must provide both a terminology for scripters to use and the underlying Apple event code to support it. Both Carbon and Cocoa applications can be scriptable, and the Cocoa framework contains built-in support that minimizes the amount of code you have to write.

## Specifying Scripting Terminology
Scriptable applications describe the scripting terminology they support by supplying a scripting dictionary. A dictionary specifies the commands and objects an application supports, as well as other information that is used by AppleScript or the application itself, and possibly by other applications or scripts that want to take advantage of the applicationâs scriptability. For information on designing a scripting terminology, see Technical Note TN2106,Scripting Interface Guidelines.
Users typically examine a dictionary for information on how to control an application in their scripts. You can display the dictionary for a scriptable application or scripting addition with Script Editor, as described inDisplaying Scripting Dictionaries.
There are currently three dictionary formats:
- sdef:âsdefâ is short for âscripting definition.â This XML-based format is a superset of the two formats described next and supports new and improved features. Although prior to OS X version 10.4, you could not use an sdef directly in your application, you could convert an sdef into either of the other formats with thesdptool. Starting in OS X v10.4, Cocoa applications can work natively with the sdef format, as described inPreparing a Scripting Definition Fileand other chapters inCocoa Scripting Guide.In OS X v10.5 (Leopard), itâs possible to create applications that provide dictionary information solely in sdef format, both for Carbon and Cocoa applications. You can read about additional refinements to sdef usage in Cocoa applications for Leopard in the Scripting section ofFoundation Release Notes for macOS 10.13 and iOS 11.For documentation on the sdef format, including a change history, see thesdef(5) man page.Scripting Interface Guidelinesalso includes information on working with sdefs. For documentation on thesdptool, see the man page forsdp(1), as well asEvolution of Cocoa Scriptability InformationinCocoa Scripting Guide. For an example of how to use an sdef file, see the Sketch sample application. For other examples, see the sample code projects listed inSupport for Cocoa Applications.
sdef:âsdefâ is short for âscripting definition.â This XML-based format is a superset of the two formats described next and supports new and improved features. Although prior to OS X version 10.4, you could not use an sdef directly in your application, you could convert an sdef into either of the other formats with thesdptool. Starting in OS X v10.4, Cocoa applications can work natively with the sdef format, as described inPreparing a Scripting Definition Fileand other chapters inCocoa Scripting Guide.
In OS X v10.5 (Leopard), itâs possible to create applications that provide dictionary information solely in sdef format, both for Carbon and Cocoa applications. You can read about additional refinements to sdef usage in Cocoa applications for Leopard in the Scripting section ofFoundation Release Notes for macOS 10.13 and iOS 11.
For documentation on the sdef format, including a change history, see thesdef(5) man page.Scripting Interface Guidelinesalso includes information on working with sdefs. For documentation on thesdptool, see the man page forsdp(1), as well asEvolution of Cocoa Scriptability InformationinCocoa Scripting Guide. For an example of how to use an sdef file, see the Sketch sample application. For other examples, see the sample code projects listed inSupport for Cocoa Applications.
- script suite:This is the original format used by Cocoa applications and it is still supported for backward compatibility. A script suite contains a pair of information property list (plist) files that provide both AppleScript information and information used by the application. An application can contain multiple script suites.For documentation, seeScript Suite and Script Terminology FilesinCocoa Scripting Guide.
script suite:This is the original format used by Cocoa applications and it is still supported for backward compatibility. A script suite contains a pair of information property list (plist) files that provide both AppleScript information and information used by the application. An application can contain multiple script suites.
For documentation, seeScript Suite and Script Terminology FilesinCocoa Scripting Guide.
- aete:This is the original dictionary format, and is still used in Carbon applications. The name comes from the Resource Manager resource type in which the information is stored ('aete'). An aete is useful in 10.4 and earlier, in both Carbon and Cocoa applications, to provide a dictionary that scripting languages can use without launching the application.
aete:This is the original dictionary format, and is still used in Carbon applications. The name comes from the Resource Manager resource type in which the information is stored ('aete'). An aete is useful in 10.4 and earlier, in both Carbon and Cocoa applications, to provide a dictionary that scripting languages can use without launching the application.

## Determining What to Make Scriptable
In designing a scriptable application, itâs a good idea to provide access to all of the applicationâs main features, though it may make sense to start with just a key subset. You donât typically make your applicationâs user interface directly scriptable. A good design allows users to script your applicationâs model objects (which represent data and basic behaviors) rather than its user interface (which presents information to the user).
For example, the scripting support for a drawing application might allow a script to rotate an image, but not to perform the user interface operation of clicking a Rotate button. Some applications provide additional capabilities through their scripting interface that arenât otherwise available.
For design information, see âLearning How to Make an Application Scriptableâ inGetting Started with AppleScriptand Technical Note TN2106,Scripting Interface Guidelines.
For information on how to support printing in a scriptable application, seeThe Enhanced Print Apple Event.

## Registering to Receive Apple Events
A scriptable application typically responds to a set of common commands, such asget data,set data,delete, andsave, as well as to other commands that support operations specific to the application. Commands are represented in Apple events by constants defined in framework or application headers. To support a command, an application registers an event handler routine with the Apple Event Manager to handle Apple events it receives that specify that command. The Apple Event Manager dispatches received events to the handlers registered for them.
Note:For Cocoa applications, commands are registered automatically, so that developers rarely need to register apple event handlers directly.
For more information on creating and registering event handlers, seeApple Event DispatchingandResponding to Apple EventsinApple Events Programming Guide.

## Resolving Objects in the Application
Apple events often specify items in the application. For example, aget dataevent might ask for the text of a paragraph in an open document. A distinct item in an application that can be specified in an Apple event is known as anApple event object. (The term object does not imply that the items must be represented internally as objects in an object-oriented programming language.) All such objects are considered to be contained in other objects, with the application itself serving as the ultimate container. For a given application, theAppleScript object model(also called the Apple event object model) specifies the classes of objects a scripter can work with in scripts, the accessible properties of those objects, and the inheritance and containment relationships for those objects.
The structures within an Apple event that identify objects are referred to asobject specifiers. Finding the Apple event objects they specify is known as resolving the object specifiers. To resolve object specifiers, an application must include functions that are able to find objects within their containers. The application registers these functions with the Apple Event Manager, and works with the Apple Event Manager to call them at the appropriate time to obtain the objects they specify.
For Cocoa applications, Cocoa scripting support does much of the work of resolving object specifiers, but a scriptable application must still supply methods that can locate an object within its object model containment hierarchy.
For an example of an AppleScript object model, seeOverview of Cocoa Support for Scriptable Applications; for information on how Cocoa applications resolve objects, seeObject Specifiers; both are inCocoa Scripting Guide.

## Recording
A recordable application is one that sends Apple events to itself when a user performs actions with the application. If the user has turned on recording in the Script Editor application (with Script > Record), actions that generate Apple events are recorded into an AppleScript script.
Applications that support recording typically:
- Factor code that implements the user interface from code that actually performs operations (a standard approach for applications that follow the model-view-controller design paradigm).
Factor code that implements the user interface from code that actually performs operations (a standard approach for applications that follow the model-view-controller design paradigm).
- Send Apple events within the application to connect those two parts of the application. The Apple Event Manager provides a mechanism for doing this with a minimum of overhead, described in âAddressing an Apple Event for Direct Dispatchingâ inCreating and Sending Apple EventsinApple Events Programming Guide.
Send Apple events within the application to connect those two parts of the application. The Apple Event Manager provides a mechanism for doing this with a minimum of overhead, described in âAddressing an Apple Event for Direct Dispatchingâ inCreating and Sending Apple EventsinApple Events Programming Guide.
- Make sure that any significant action or series of related actions within the application generates an Apple event.
Make sure that any significant action or series of related actions within the application generates an Apple event.
The Finder application in OS X is recordable. Starting in OS X version 10.5, theAutomatorapplication has a separate Record mechanism that lets users record actions into an Automator workflow.

## Creating and Sending Apple Events
An application can create and send Apple events directly. This is usually done either to send internal Apple events, as described inRecording, to obtain services from a scriptable application, or to communicate directly with another application. The Open Scripting Architecture provides various mechanisms for creating and sending Apple events.
Starting in OS X version 10.5, applications can useScripting Bridgeto obtain services from scriptable applications. Scripting Bridge lets you work efficiently in a high-level language (Objective-C) without having to handle the details of sending and receiving Apple events. (See alsoSupport for Cocoa Applicationsfor related information.)
When you really do need to send an Apple event directly, seeBuilding an Apple EventandCreating and Sending Apple EventsinApple Events Programming Guide.

## Executing Scripts
To execute scripts, an application establishes a connection with the AppleScript scripting component. It can then:
- Use the standard scripting component routines to manipulate scripts associated with any part of the application or its documents.
Use the standard scripting component routines to manipulate scripts associated with any part of the application or its documents.
- Let users record and edit scripts.
Let users record and edit scripts.
- Compile and execute scripts.
Compile and execute scripts.
Note:Starting in OS X version 10.5, applications can useScripting Bridgeto obtain services from scriptable applications. This can be much more efficient than manipulating scripts.
An application can store and execute scripts regardless of whether it is scriptable or recordable. If an application is scriptable, however, it can execute scripts that control its own behavior, thus acting as both the client application and the server application for the corresponding Apple events. For more information, seeOpen Scripting Architecture Reference.
In Cocoa, theNSAppleScriptclass, described inNSAppleScript Class Reference, provides a high-level wrapper for executing AppleScript scripts from applications. For more information, seeSupport for Cocoa Applications.

## Summary of Operations in a Scriptable Application
The following list summarizes how scriptable applications interact with the Open Scripting Architecture to make their features available to scripters.
- The Apple Event Manager defines data structures that are used to construct Apple events.
The Apple Event Manager defines data structures that are used to construct Apple events.
- The Open Scripting Architecture (OSA) provides a data transport and event dispatching mechanism for Apple events, built on top of lower level protocols.
The Open Scripting Architecture (OSA) provides a data transport and event dispatching mechanism for Apple events, built on top of lower level protocols.
- AppleScript defines a scripting language, described inAppleScript Language Guide(and third-party books) and implemented by the AppleScript component in OS X.
AppleScript defines a scripting language, described inAppleScript Language Guide(and third-party books) and implemented by the AppleScript component in OS X.
- There is a small set of Apple events sent by the Mac OS, such asopen application,quit, andopen documentsthat all applications should be able to respond to. A scriptable application responds to additional common events, such asget dataandset data, as well as to its own specific commands.
There is a small set of Apple events sent by the Mac OS, such asopen application,quit, andopen documentsthat all applications should be able to respond to. A scriptable application responds to additional common events, such asget dataandset data, as well as to its own specific commands.
- A scriptable application provides a scripting terminology (or dictionary) for the operations it supports. The application can reuse some event constants defined by the OSA or use its own for custom events. (Constants defined by Apple, many of which you can reuse in your applications, are described inAppleScript Terminology and Apple Event Codes Reference.)The sdef file format provides a mechanism for creating one terminology definition that can be converted for use in different environments.
A scriptable application provides a scripting terminology (or dictionary) for the operations it supports. The application can reuse some event constants defined by the OSA or use its own for custom events. (Constants defined by Apple, many of which you can reuse in your applications, are described inAppleScript Terminology and Apple Event Codes Reference.)
The sdef file format provides a mechanism for creating one terminology definition that can be converted for use in different environments.
- Developers design their applications so that key operations can be invoked in response to received Apple events.
Developers design their applications so that key operations can be invoked in response to received Apple events.
- A scriptable application works with the Apple Event Manager to:Register handlers for Apple events it can process.Extract information from received Apple events, then perform requested operations or return requested data.Construct Apple events for replies or other purposes.Scriptable Carbon applications work with the Apple Event Manager directly, but for scriptable Cocoa applications, much of this work is handled automatically.
A scriptable application works with the Apple Event Manager to:
- Register handlers for Apple events it can process.
Register handlers for Apple events it can process.
- Extract information from received Apple events, then perform requested operations or return requested data.
Extract information from received Apple events, then perform requested operations or return requested data.
- Construct Apple events for replies or other purposes.
Construct Apple events for replies or other purposes.
Scriptable Carbon applications work with the Apple Event Manager directly, but for scriptable Cocoa applications, much of this work is handled automatically.
- Scripters write AppleScript scripts that specify scriptable applications and the operations to perform.
Scripters write AppleScript scripts that specify scriptable applications and the operations to perform.
- When a script is executed, script statements that target applications are translated by the AppleScript component into Apple events that are sent to those applications.Applications can also send Apple events directly to other applications.
When a script is executed, script statements that target applications are translated by the AppleScript component into Apple events that are sent to those applications.
Applications can also send Apple events directly to other applications.
- An application responds to the Apple events it receives by performing operations, returning data, or both.
An application responds to the Apple events it receives by performing operations, returning data, or both.

## OS X Support for Creating Scriptable Applications
OS X supplies a number of resources that applications can use to work with Apple events and to support scriptability, including the API provided in the following frameworks:
- The underlying support in OS X for creating scriptable applications and working with Apple events is provided by the Open Scripting Architecture, and is described inThe Parts of the Open Scripting Architecture.
The underlying support in OS X for creating scriptable applications and working with Apple events is provided by the Open Scripting Architecture, and is described inThe Parts of the Open Scripting Architecture.
- TheCocoa framework(Cocoa.framework) includes the Application Kit and Foundation frameworks, which together provide the building blocks for sophisticated Mac apps. The Cocoa framework includes a great deal of support for creating scriptable applications.For specific Cocoa scripting documentation, seeCocoa Scripting Guide.
TheCocoa framework(Cocoa.framework) includes the Application Kit and Foundation frameworks, which together provide the building blocks for sophisticated Mac apps. The Cocoa framework includes a great deal of support for creating scriptable applications.
For specific Cocoa scripting documentation, seeCocoa Scripting Guide.
- Java applications are not typically scriptable, though they can be made AppleScript-aware using the mechanisms described inOS X Integration for JavainJava Development Guide for Mac.
Java applications are not typically scriptable, though they can be made AppleScript-aware using the mechanisms described inOS X Integration for JavainJava Development Guide for Mac.

### Support for Carbon Applications
Carbon applications have traditionally worked directly with the Apple Event Manager to create, send, receive, and interpret Apple events. These topics are described in detail inApple Events Programming Guide.
For information on making your Carbon application scriptable, see previous sections in this chapter, as well as the learning paths inGetting Started with AppleScript.
Carbon applications can use functions such asOSACompileandOSAExecutefromOpenScripting.frameworkto compile and execute scripts. Keep in mind, however, that if you are executing a script merely to send a simple command to another application, it is more efficient to create and send an Apple event directly.
If the purpose for executing a script is just to perform ado shell scriptcommand, Carbon applications can do so more efficiently using one of the BSD callssystem(3),popen(3), orexec(3), which you can read about at their respective man pages.

### Support for Cocoa Applications
The Foundation and Application Kit frameworks provide Cocoa applications with automated handling for certain Apple events. This includes events that may be sent by the Mac OS, such as theopen application,open documents,print documents, andquitApple events.
In addition, Cocoa provides substantial support for creating scriptable applications. To take advantage of it, applications provide scriptability information in one of the formats described inSpecifying Scripting Terminology. They also create KVC-compliant accessors for scriptable properties in their scriptable classes. (Key-value coding, or KVC, is described inKey-Value Coding Programming Guide.) Though creating a fully scriptable application is a non-trivial task, an application can support many standard AppleScript commands, such as those for getting and setting properties of application objects, with a relatively small number of additional steps.
Cocoa applications can also use any of the Open Scripting Architecture APIs available to Carbon applications, and in fact, Cocoa links with the Carbon framework. For example, a Cocoa Application might call an Apple Event Manager function to send an Apple event directly (there currently is no Cocoa API to do that).
Starting in OS X version 10.5, theScripting Bridgetechnology provides an efficient way for Cocoa applications to interact with scriptable applications at a high levelâthat is, without having to construct or parse individual Apple events.
Cocoa provides theNSAppleScriptclass for tasks such as compiling and executing scripts. This gives applications another mechanism to control scriptable applications and take advantage of services they provide. However, you should not useNSAppleScriptto execute a script merely to result in sending an Apple event, because it is far more expensive than using Scripting Bridge or creating and sending an Apple event directly. And if the purpose for executing a script is to perform ado shell scriptcommand, Cocoa applications can execute shell commands more efficiently usingNSTask.
The Cocoa framework also includes classes such asNSAppleEventDescriptor, for working with underlying Apple event data structures, andNSAppleEventManager, for accessing certain Apple Event Manager functions.
Cocoa support for handling Apple events and creating scriptable applications is documented inCocoa Scripting Guide. For related information, see âFramework and Language Supportâ inAbout Apple EventsinApple Events Programming Guide. For introductory sample code, seeSimpleScripting,SimpleScriptingProperties,SimpleScriptingObjects, andSimpleScriptingVerbs. For a more complex example, see the Sketch sample application.
Copyright © 2002, 2007 Apple Inc. All Rights Reserved.Terms of Use|Privacy Policy|  Updated: 2007-10-31