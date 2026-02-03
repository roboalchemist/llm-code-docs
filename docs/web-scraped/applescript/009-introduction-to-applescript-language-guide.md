# Introduction to AppleScript Language Guide

This document is a guide to the AppleScript languageâits lexical conventions, syntax, keywords, and other elements. It is intended primarily for use with AppleScript 2.0 or later and macOS version 10.5 or later.
AppleScript 2.0 can use scripts developed for any version of AppleScript from 1.1 through 1.10.7, any scripting addition created for AppleScript 1.5 or later for macOS, and any scriptable application for Mac OS v7.1 or later. A script created with AppleScript 2.0 can be used by any version of AppleScript back to version 1.1, provided it does not use features of AppleScript, scripting additions, or scriptable applications that are unavailable in that version.
Important:Descriptions and examples for the terms in this document have been tested with AppleScript 2.0 in OS X v10.5 (Leopard). Except for terms that are noted as being new in Leopard, most descriptions and examples work with previous system versions, but have not been tested against all of them.
If you need detailed information about prior system and AppleScript versions, seeAppleScript Release Notes (OS X v10.4 and earlier).

## What Is AppleScript?

AppleScript is a scripting language created by Apple. It allows users to directly control scriptable Macintosh applications, as well as parts of macOS itself. You can create scriptsâsets of written instructionsâto automate repetitive tasks, combine features from multiple scriptable applications, and create complex workflows.
Note:Apple also provides the Automator application, which allows users to automate common tasks by hooking together ready-made actions in a graphical environment. For more information, seeAutomator Documentation.
A scriptable application is one that can be controlled by a script. For AppleScript, that means being responsive to interapplication messages, calledApple events, sent when a script command targets the application. (Apple events can also be sent directly from other applications and macOS.)
AppleScript itself provides a very small number of commands, but it provides a framework into which you can plug many task-specific commandsâthose provided by scriptable applications and scriptable parts of macOS.
Most script samples and script fragments in this guide use scriptable features of the Finder application, scriptable parts of macOS, or scriptable applications distributed with macOS, such as TextEdit (located in/Applications).

## Who Should Read This Document?

You should use this document if you write or modify AppleScript scripts, or if you create scriptable applications and need to know how scripts should work.
AppleScript Language Guideassumes you are familiar with the high-level information about AppleScript found inAppleScript Overview.

## Organization of This Document

This guide describes the AppleScript language in a series of chapters and appendixes.
The first five chapters introduce components of the language and basic concepts for using it, then provide additional overview on working with script objects and handler routines:

- AppleScript Lexical Conventionsdescribes the characters, symbols, keywords, and other language elements that make up statements in an AppleScript script.
AppleScript Lexical Conventionsdescribes the characters, symbols, keywords, and other language elements that make up statements in an AppleScript script.

- AppleScript Fundamentalsdescribes basic concepts that underly the terminology and rules covered in the rest of this guide.
AppleScript Fundamentalsdescribes basic concepts that underly the terminology and rules covered in the rest of this guide.

- Variables and Propertiesdescribes common issues in working with variables and properties, including how to declare them and how AppleScript interprets their scope.
Variables and Propertiesdescribes common issues in working with variables and properties, including how to declare them and how AppleScript interprets their scope.

- Script Objectsdescribes how to define, initialize, send commands to, and use inheritance with script objects.
Script Objectsdescribes how to define, initialize, send commands to, and use inheritance with script objects.

- About Handlersprovides information on using handlers (a type of function available in AppleScript) to factor and reuse code.
About Handlersprovides information on using handlers (a type of function available in AppleScript) to factor and reuse code.
The following chapters provide reference for the AppleScript Language:

- Class Referencedescribes the classes AppleScript defines for common objects used in scripts.
Class Referencedescribes the classes AppleScript defines for common objects used in scripts.

- Commands Referencedescribes the commands that are available to any script.
Commands Referencedescribes the commands that are available to any script.

- Reference Formsdescribes the syntax for specifying an object or group of objects in an application or other container.
Reference Formsdescribes the syntax for specifying an object or group of objects in an application or other container.

- Operators Referenceprovides a list of the operators AppleScript supports and the rules for using them, along with sections that provide additional detail for commonly used operators.
Operators Referenceprovides a list of the operators AppleScript supports and the rules for using them, along with sections that provide additional detail for commonly used operators.

- Control Statements Referencedescribes statements that control when and how other statements are executed. It covers standard conditional statements, as well as statements used in error handling and other operations.
Control Statements Referencedescribes statements that control when and how other statements are executed. It covers standard conditional statements, as well as statements used in error handling and other operations.

- Handler Referenceshows the syntax for defining and calling handlers and describes other statements you use with handlers.
Handler Referenceshows the syntax for defining and calling handlers and describes other statements you use with handlers.
The following chapter describes an AppleScript-related feature of macOS:

- Folder Actions Referencedescribes how you can write and attach script handlers to specific folders, such that the handlers are invoked when the folders are modified.
Folder Actions Referencedescribes how you can write and attach script handlers to specific folders, such that the handlers are invoked when the folders are modified.
The following appendixes provide additional information about the AppleScript language and how to work with errors in scripts:

- AppleScript Keywordslists the keywords of the AppleScript language, provides a brief description for each, and points to related information.
AppleScript Keywordslists the keywords of the AppleScript language, provides a brief description for each, and points to related information.

- Error Numbers and Error Messagesdescribes error numbers and error messages you may see in working with AppleScript scripts.
Error Numbers and Error Messagesdescribes error numbers and error messages you may see in working with AppleScript scripts.

- Working with Errorsprovides detailed examples of handling errors withtry Statementsanderror Statements.
Working with Errorsprovides detailed examples of handling errors withtry Statementsanderror Statements.

- Double Angle Bracketsdescribes when you are likely to see double angle brackets (or chevronsâÂ«Â») in scripts and how you can work with them.
Double Angle Bracketsdescribes when you are likely to see double angle brackets (or chevronsâÂ«Â») in scripts and how you can work with them.

- Libraries using Load Scriptdescribes how to save libraries of handlers and access them from other scripts.
Libraries using Load Scriptdescribes how to save libraries of handlers and access them from other scripts.

- Unsupported Termslists terms that are no longer supported in AppleScript.
Unsupported Termslists terms that are no longer supported in AppleScript.

## Conventions Used in This Guide

Glossary terms are shown inboldfacewhere they are defined.
Important:This document sometimes uses the continuation character (Â¬) for sample statements that donât fit on one line on a document page. It also uses the continuation character in some syntax statements to identify an item that, if included, must appear on the same line as the previous item. The continuation character itself is not a required part of the syntaxâit is merely a mechanism for including multiple lines in one statement.
The following conventions are used in syntax descriptions:
language element
Plain computer font indicates an element that you type exactly as shown. If there are special symbols (for example,+or&), you also type them exactly as shown.
placeholder
Italic text indicates a placeholder that you replace with an appropriate value.
[optional]
Brackets indicate that the enclosed language element or elements are optional.
(a group)
Parentheses group elements together.
However, the parentheses shown inHandler Syntax (Positional Parameters)are part of the syntax.
[optional]...
Three ellipsis points (...) after a group defined by brackets indicate that you can repeat the group of elements within brackets 0 or more times.
a | b | c
Vertical bars separate elements in a group from which you must choose a single element. The elements are often grouped within parentheses or brackets.
Filenames shown in scripts
Most filenames shown in examples in this document include extensions, such asrtffor a TextEdit document. Use of extensions in scripts is generally dependent on the âShow all file extensionsâ setting in the Advanced pane of Finder Preferences.
To work with the examples on your computer, you may need to modify either that setting or the filenames.

## See Also

These Apple documents provide additional information for working with AppleScript:

- SeeGetting Started with AppleScriptfor a guided quick start, useful to both scripters and developers.
SeeGetting Started with AppleScriptfor a guided quick start, useful to both scripters and developers.

- SeeAppleScript Overview, including the chapterScripting with AppleScript, for a high-level overview of AppleScript and its related technologies.
SeeAppleScript Overview, including the chapterScripting with AppleScript, for a high-level overview of AppleScript and its related technologies.

- SeeGetting Started With Scripting & Automationfor information on the universe of scripting technologies available in macOS.
SeeGetting Started With Scripting & Automationfor information on the universe of scripting technologies available in macOS.

- SeeAppleScript Terminology and Apple Event Codesfor a list of many of the scripting terms defined by Apple.
SeeAppleScript Terminology and Apple Event Codesfor a list of many of the scripting terms defined by Apple.
For additional information on working with the AppleScript language and creating scripts, see one of the comprehensive third-party documents available in bookstores and online.
Copyright © 2016 Apple Inc. All Rights Reserved.Terms of Use|Privacy Policy|  Updated: 2016-01-25
