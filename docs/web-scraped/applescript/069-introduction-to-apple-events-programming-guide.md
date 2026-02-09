# Introduction to Apple Events Programming Guide

# Retired Document
Important:This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

Important:This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.
Apple Events Programming Guideprovides conceptual information and programming examples for working with Apple events.
AnApple eventis a type of interprocess message that can specify complex operations and data. Apple events allow you to gather all the data necessary to accomplish a high level task into a single package that can be passed across process boundaries, evaluated, and returned with results. The Mac OS uses Apple events to communicate with applications. Apple events are also an essential part of the AppleScript scripting system, which allows users to automate actions usingscriptable applicationsâapplications that can respond to a variety of Apple events by performing operations or supplying data.
Note:Mac OS X offers other mechanisms for communicating between processes. These mechanisms are described in âIPC and Notification Mechanismsâ in "Darwin and Core Technologiesâ inMac Technology Overview.
Apple Events Programming Guideassumes that you are familiar with the information inAppleScript Overview.
The information in this document applies primarily to Carbon applications. While Cocoa applications can take advantage of most of the described features, in many cases they wonât need to. For more information, seeFramework and Language Support.

## Who Should Read This Document
You should read this document if you want to:
- Make your Carbon application respond to the Apple events sent by the Mac OS (for launching and quitting applications, opening documents, and so on).
Make your Carbon application respond to the Apple events sent by the Mac OS (for launching and quitting applications, opening documents, and so on).
- Work with Apple events as part of writing a scriptable Carbon application.
Work with Apple events as part of writing a scriptable Carbon application.
- Use Apple events to communicate with other applications.
Use Apple events to communicate with other applications.
- Gain background information about Apple events for your work with scriptable Cocoa applications, AppleScript Studio applications, Automator workflows, or AppleScript scripts.
Gain background information about Apple events for your work with scriptable Cocoa applications, AppleScript Studio applications, Automator workflows, or AppleScript scripts.
Important:An Apple event can contain object specifiers that identify objects within the application that receives the event. Object specifiers are mentioned only briefly in this document. For information on how to work with object specifiers, seeâResolving and Creating Object Specifier RecordsâinInside Macintosh: Interapplication Communication.
Do not rely on the API descriptions inInterapplication CommunicationâOpen Scripting Architecture ReferenceandApple Event Manager Referenceprovide the current API documentation.

## Organization of This Document
This document is organized into the following chapters:
- About Apple Eventsdefines Apple events, explains when theyâre useful, and provides a quick overview of common tasks for working with them. It also provides a brief description of the framework and language support available in Mac OS X and provides links to additional information inApple Events Programming Guideand in other documents.
About Apple Eventsdefines Apple events, explains when theyâre useful, and provides a quick overview of common tasks for working with them. It also provides a brief description of the framework and language support available in Mac OS X and provides links to additional information inApple Events Programming Guideand in other documents.
- Building an Apple Eventprovides an overview of Apple event data structures and describes how to build an Apple event.
Building an Apple Eventprovides an overview of Apple event data structures and describes how to build an Apple event.
- Apple Event Dispatchingshows how your application works with the Apple Event Manager to register the Apple events it can handle and dispatch those events to the code that should handle them.
Apple Event Dispatchingshows how your application works with the Apple Event Manager to register the Apple events it can handle and dispatch those events to the code that should handle them.
- Working With the Data in an Apple Eventdescribes how to extract data from Apple events and the data structures that comprise them.
Working With the Data in an Apple Eventdescribes how to extract data from Apple events and the data structures that comprise them.
- Responding to Apple Eventsdescribes how to respond to an Apple event by examining the event, performing the requested action, interacting with the user (if necessary), and returning a reply event. It also provides an overview of how to respond to Apple events sent by the Mac OS.
Responding to Apple Eventsdescribes how to respond to an Apple event by examining the event, performing the requested action, interacting with the user (if necessary), and returning a reply event. It also provides an overview of how to respond to Apple events sent by the Mac OS.
- Creating and Sending Apple Eventsprovides information and sample code that will help you create and send Apple events and respond to reply Apple events.
Creating and Sending Apple Eventsprovides information and sample code that will help you create and send Apple events and respond to reply Apple events.
- Writing and Installing Coercion Handlersdescribes how to write coercion handlers that convert between various types of data and how to install them so that they are available to your application.
Writing and Installing Coercion Handlersdescribes how to write coercion handlers that convert between various types of data and how to install them so that they are available to your application.
- Testing and Debugging Apple Event Codeprovides tips for displaying and debugging Apple events in your application.
Testing and Debugging Apple Event Codeprovides tips for displaying and debugging Apple events in your application.
- Selected Apple Event Manager Functionsprovides information about some commonly used functions.
Selected Apple Event Manager Functionsprovides information about some commonly used functions.
- Selected Apple Event Constantsprovides information about some commonly used constants.
Selected Apple Event Constantsprovides information about some commonly used constants.
- Default Coercion Handlerslists the type conversions performed by the default coercion handlers provided by the Mac OS.
Default Coercion Handlerslists the type conversions performed by the default coercion handlers provided by the Mac OS.

## See Also
The following documents provide related information.
- AppleScript Overviewprovides information that is useful for working with AppleScript and Apple events, including a description of the Open Scripting Architecture, on which both rely.
AppleScript Overviewprovides information that is useful for working with AppleScript and Apple events, including a description of the Open Scripting Architecture, on which both rely.
- Apple Event Manager Referencedescribes the API for sending and receiving Apple events and working with the information they contain.
Apple Event Manager Referencedescribes the API for sending and receiving Apple events and working with the information they contain.
- Technical Note TN2106,Scripting Interface Guidelines, describes how to design the scripting interface for a scriptable application.
Technical Note TN2106,Scripting Interface Guidelines, describes how to design the scripting interface for a scriptable application.
- AppleScript Language Guidedescribes the features and terminology of the AppleScript scripting language.
AppleScript Language Guidedescribes the features and terminology of the AppleScript scripting language.
- For information on sending Apple events to web services, seeXML-RPC and SOAP Programming Guide.
For information on sending Apple events to web services, seeXML-RPC and SOAP Programming Guide.
Copyright © 2005, 2007 Apple Inc. All Rights Reserved.Terms of Use|Privacy Policy|  Updated: 2007-10-31