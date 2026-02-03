# Mac Automation Scripting Guide: Navigating a Scripting Dictionary

## Navigating a Scripting Dictionary

A scripting dictionary window in Script Editor contains three primary areas. SeeFigure 12-1.

- Toolbar.Options for toggling between terminology views, setting the scripting language, entering search terms, and more.
Toolbar.Options for toggling between terminology views, setting the scripting language, entering search terms, and more.

- Navigation pane.Columns of scripting terminology.
Navigation pane.Columns of scripting terminology.

- Detail pane.Definitions for any terminology selected in the navigation pane.
Detail pane.Definitions for any terminology selected in the navigation pane.

### Types of Terminology

The navigation pane of a dictionary includes the types of terms described inTable 12-1.
Type
Icon
Description
Suite
Asuiteis a grouping of related commands and classes. Apps often have a Standard Suite, which includes terminology supported by most scriptable apps, such as anopencommand, aquitcommand, and anapplicationclass.
Command
Acommandis an instruction that can be sent to an app or object in order to initiate some action. For example,delete,make,printare commands that are found in many scriptable apps. Many commands haveparametersthat specify the target object and control the behavior of the command.
Class
Aclassis an object within an app, or an app itself. Mail, for example, has anapplicationclass, amessageclass, and asignatureclass, among others. Objects within an app sometimes contain other objects aselements. For example, in Mail, amailboxobjects can containmessageobjects as elements.
Property
Apropertyis an attribute of a class. For example, themessageclass in Mail has many properties, includingdate received,read status, andsubject. Some properties are read-only, while others are readable and writable.

### Key Concepts

Itâs important to understand the concepts ofinheritanceandcontainmentwhen navigating a scripting dictionary.

### Inheritance

In a scriptable app, different classes often implement the same properties. For example, in Finder, thefileandfolderclasses both havecreation date,modification date, andnameproperties. Rather than defining these same properties multiple times throughout the scripting dictionary, Finder implements a genericitemclass. Since files and folders are considered types of Finder items, these classes inherit the properties of theitemclass. In other words, any properties of theitemclass also apply to thefileandfolderclasses. There are many other items in Finder that also inherit these same properties, including thedisk,package, andalias fileclasses.
A class that inherits the properties of other classes can also implement its own properties. In Finder, thefileclass implements a number of file-specific properties, includingfile typeandversion. Thealias fileclass implements anoriginal itemproperty.
In some cases, a class inherits properties from multiple classes. In Finder, an alias is a type of file, which is a type of item. Therefore, thealias fileclass inherits the properties of both thefileanditemclasses, as shown inFigure 12-2.

### Containment

Classes of a scriptable app reside within a certain containment hierarchy. The application is at the top level, with other classes nested beneath. Finder, for example, contains disks, folders, files, and other objects. While files donât contain elements, folders and disks can contain other folders and files. SeeFigure 12-3. Mail is another exampleâthe application contains accounts, which can contain mailboxes, which can contain other mailboxes and messages.
When referencing a class, you must do so very specifically according to its containment hierarchy in order to provide the scripting system with context. To reference a file in Finder, you would specify where the file resides in the folder hierarchy. SeeListing 12-1andListing 12-2. To reference a message in Mail, you would specify where the message resides in the mailbox and account hierarchy.
APPLESCRIPT
Open in Script Editor

- tell application "Finder"
- modification date of file "My File.txt" of folder "Documents" of folder "YourUserName" of folder "Users" of startup disk
- end tell
- --> Result: date "Monday, September 28, 2015 at 10:10:17 AM"
JAVASCRIPT
Open in Script Editor

- var Finder = Application("Finder")
- Finder.startupDisk.folders["Users"].folders["YourUserName"].folders["Documents"].files["My File.txt"].modificationDate()
- // Result: Mon Sep 28 2015 17:10:17 GMT-0700 (PDT)

### Anatomy of a Command Definition

The definition of a command in a scripting dictionary is a recipe for using the command, as shown inFigure 12-4,Listing 12-3, andListing 12-4.
A command definition includes the following elements:

- Command name.The name of the command.
Command name.The name of the command.

- Direct parameter.An object to be targeted by the command. For themovecommand in Finder, this is the object to be moved. If a command definition doesnât specify a direct parameter, then the target object is the application. A direct parameter immediately follows the command.
Direct parameter.An object to be targeted by the command. For themovecommand in Finder, this is the object to be moved. If a command definition doesnât specify a direct parameter, then the target object is the application. A direct parameter immediately follows the command.

- Labeled parameters.Control some aspect of the commandâs behavior and are required or optional. Optional parameters are surrounded by brackets. Since these parameters are identified by label, they can be placed in any order when you write your script. The command definition denotes the value type for each labeled parameter. For example, the optionalreplacingparameter for themovecommand in Finder takes a boolean value.
Labeled parameters.Control some aspect of the commandâs behavior and are required or optional. Optional parameters are surrounded by brackets. Since these parameters are identified by label, they can be placed in any order when you write your script. The command definition denotes the value type for each labeled parameter. For example, the optionalreplacingparameter for themovecommand in Finder takes a boolean value.

- Result.The result of the command, if any. Often, this is a reference to a newly created or modified object. For themovecommand in Finder, itâs a reference to the moved object.
Result.The result of the command, if any. Often, this is a reference to a newly created or modified object. For themovecommand in Finder, itâs a reference to the moved object.
APPLESCRIPT
Open in Script Editor

- tell application "Finder"
- move folder someFolder to someOtherFolder replacing true
- end tell
JAVASCRIPT
Open in Script Editor

- var Finder = Application("Finder")
- Finder.move(someFolder, {
- to: someOtherFolder,
- replacing: true
- })

### Anatomy of a Class Definition

A class definition describes a class, as shown inFigure 12-5.
A class definition includes the following elements:

- Class name.The name of the class.
Class name.The name of the class.

- Inheritance details.A list of other classes from which properties are inherited, if any. Each class is a hyperlinkâclicking it takes you to the definition for the corresponding class.
Inheritance details.A list of other classes from which properties are inherited, if any. Each class is a hyperlinkâclicking it takes you to the definition for the corresponding class.

- Containment details.A list of contained classes, if any. May also list other classes containing the class, if any.
Containment details.A list of contained classes, if any. May also list other classes containing the class, if any.

- Properties.Any properties for the class, along with their data types. Read-only properties include anr/oindicator.
Properties.Any properties for the class, along with their data types. Read-only properties include anr/oindicator.
To view inherited properties, as well as containing classes in the Script Editor dictionary viewer, select Show inherited items in Preferences > General. SeeFigure 12-6.
Opening a Scripting Dictionary
Using Handlers/Functions
Copyright © 2018 Apple Inc. All rights reserved.Terms of Use|Privacy Policy|Updated: 2016-06-13
