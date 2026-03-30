# Mac Automation Scripting Guide: How Mac Scripting Works

## How Mac Scripting Works

TheOpen Scripting Architecture (OSA)provides a standard and extensible mechanism for interapplication communication in OS X. This communication takes place through the exchange of Apple events. AnApple eventis a type of interprocess message that encapsulates commands and data.
Ascriptable applicationresponds to Apple events by performing operations or supplying data. Every scriptable app implements its own scripting features and exposes its own unique terminology through ascripting dictionary. While not all apps are consideredscriptable, any app with a graphical user interface responds to Apple Events at a minimal level. This is because OSÂ X uses Apple Events to instruct all apps to perform core tasks such as launching, quitting, opening a document, and printing. To learn about scripting terminology and dictionaries, seeAccessing Scripting Terminology.
The OSA provides the following capabilities in OS X:

- The ability for app developers to create scriptable apps and expose scripting terminology
The ability for app developers to create scriptable apps and expose scripting terminology

- The ability for users to write scripts in a variety of scripting languages
The ability for users to write scripts in a variety of scripting languages

- The ability to communicate between apps on the same computer or on different computers using Apple events
The ability to communicate between apps on the same computer or on different computers using Apple events
TheOpen Scripting frameworkdefines standard data structures, routines, and resources for creatingscripting components, which implement support for specific scripting languages. The AppleScript and JavaScript components (inSystem/Library/Components), for example, make it possible to control scriptable apps from AppleScript and JavaScript scripts. Through the frameworkâs standard interface, a scriptable app can interact with any scripting component, regardless of its language. The framework also provides API for compiling, executing, loading, and storing scriptsâfunctions provided by script editing apps.
TheApple Event Managersupplies the underlying support for creating scriptable apps and is implemented in the AE framework within the CoreServices framework. App developers can interact with the Apple Event Manager through the Apple Event APIs in the Foundation framework. SeeNSAppleEventManager Class ReferenceandNSAppleEventDescriptor Class Reference.
Figure 2-1shows how OSA elements work together in OSÂ X.

### Extending the Reach of Scripting

Every scriptable app expands the reach of scripting. Developers can also add new scripting capabilities through scripting additions and scriptable background apps.
Ascripting additionis a bundle that implements new scripting terminology. For example, the Standard Additions scripting addition that comes with OSÂ X (found in/System/Library/ScriptingAdditions/StandardAdditions.osax), includes commands for using the Clipboard, displaying alerts, speaking text, executing shell scripts, and more. Since scripting additions are loaded in a global context, commands provided by Standard Additions are available to all scripts.
Ascriptable background application(sometimes called anagent) runs with no visible user interface and provides scripts with access to useful features. System Events and Image Events are examples of scriptable background apps in OSÂ X. Scripts can target System Events to perform operations on property list files, adjust system preferences, and much more. Scripts can target Image Events to perform basic image manipulations, such as cropping, rotating, and resizing.

### Objective-C Bridging

Several technologies in OSÂ X make it possible for scripts to interact with Objective-C frameworks, and vice-versa.
AppleScriptObjCis a bridge between AppleScript and Objective-C, andJavaScriptObjCis a bridge between JavaScript for automation and Objective-C. These bridges enable you to write scripts that use scripting terminology to interact with Objective-C frameworks, such as Foundation and AppKit. The bridges also enable you to design user interfaces for scripts that have the same look and feel of any other Cocoa app. For information about the AppleScriptObjC bridge, seeObjective-C to AppleScript Quick Translation Guide. For information about JavaScriptObjC, seeObjective-C BridgeinJavaScript for Automation Release Notes.
TheScripting Bridgelets you control scriptable apps using standard Objective-C syntax. Instead of incorporating scripts in your Cocoa app or dealing with the complexities of sending and handling Apple events, you can simply send Objective-C messages to objects representing scriptable apps. Your Cocoa app can do anything a script can, but in Objective-C code thatâs more tightly integrated with the rest of your projectâs code. SeeScripting Bridge Programming GuideandScripting Bridge Framework Reference.
About Mac Scripting
Types of Scripts
Copyright © 2018 Apple Inc. All rights reserved.Terms of Use|Privacy Policy|Updated: 2016-06-13
