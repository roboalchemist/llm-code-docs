# AppleScript Fundamentals

# AppleScript Fundamentals
This chapter describes basic concepts that underlie the terminology and rules covered in the rest of this guide.
- Script Editor Application
Script Editor Application
- AppleScript and Objects
AppleScript and Objects
- Object Specifiers
Object Specifiers
- Coercion (Object Conversion)
Coercion (Object Conversion)
- Scripting Additions
Scripting Additions
- Commands Overview
Commands Overview
- AppleScript Error Handling
AppleScript Error Handling
- Global Constants in AppleScript
Global Constants in AppleScript
- The it and me Keywords
The it and me Keywords
- Aliases and Files
Aliases and Files
- Remote Applications
Remote Applications
- Debugging AppleScript Scripts
Debugging AppleScript Scripts

## Script Editor Application
The Script Editor application is located in/Applications/Utilities. It provides the ability to edit, compile, and execute scripts, display application scripting terminologies, and save scripts in a variety of formats, such as compiled scripts, applications, and plain text.
Script Editor can display the result of executing an AppleScript script and can display a log of the Apple events that are sent during execution of a script. In the Script Editor Preferences, you can also choose to keep a history of recent results or event logs.
Script Editor has text formatting preferences for various types of script text, such as language keywords, comments, and so on. You can also turn on or off the Script Assistant, a code completion tool that can suggest and fill in scripting terms as you type. In addition, Script Editor provides a contextual menu to insert many types of boilerplate script statements, such as conditionals, comments, and error handlers.
Adictionaryis the part of a scriptable application that specifies the scripting terms it understands. You can choose File > Open Dictionary in Script Editor to display the dictionaryof a scriptable application or scripting addition on your computer. Or you can drag an application icon to the Script Editor icon to display its dictionary (if it has one).
To display a list that includes just the scriptable applications and scripting additions provided by macOS, choose Window > Library. Double-click an item in the list to display its dictionary.Figure 2-1shows the dictionary for the Finder application in OS X v10.5. The dictionary is labeled as âFinder.sdefâ. The sdef format, along with other terminology formats, is described in âSpecifying Scripting Terminologyâ inAppleScript Overview.
There are also third-party editors for AppleScript.

## AppleScript and Objects
AppleScript is an object-oriented language. When you write, compile, and execute scripts, everything you work with is an object. Anobjectis an instantiation of a class definition, which can include properties and actions. AppleScript defines classes for the objects you most commonly work with, starting with the top-levelscriptobject, which is the overall script you are working in.
Within in ascriptobject, you work with other objects, including:
- AppleScript objects:AppleScript defines classes for boolean values, scripts, text, numbers, and other kinds of objects for working in scripts; for a complete list, seeClass Reference.
AppleScript objects:
AppleScript defines classes for boolean values, scripts, text, numbers, and other kinds of objects for working in scripts; for a complete list, seeClass Reference.
- macOS objects:Scriptable parts of macOS and applications distributed with it, such as Finder, System Events, and Database Events (located in/System/Library/CoreServices), define many useful classes.
macOS objects:
Scriptable parts of macOS and applications distributed with it, such as Finder, System Events, and Database Events (located in/System/Library/CoreServices), define many useful classes.
- Application objects:Third-party scriptable applications define classes that support a wide variety of features.
Application objects:
Third-party scriptable applications define classes that support a wide variety of features.
The following sections provide more detail about objects:
- What Is in a Script Object
What Is in a Script Object
- Properties
Properties
- Elements
Elements

### What Is in a Script Object
When you enter AppleScript statements in script window in Script Editor, you are working in a top-levelscriptobject. Allscriptobject definitions follow the same syntax, except that a top-levelscriptobject does not have statements marking its beginning and end.
Ascriptobject can contain the following:
- Property definitions (optional):A property is a labeled container in which to store a value.
Property definitions (optional):
A property is a labeled container in which to store a value.
- An explicitrunhandler (optional):Arunhandler contains statements AppleScript executes when the script is run. (For more information, seerun Handlers.)
An explicitrunhandler (optional):
Arunhandler contains statements AppleScript executes when the script is run. (For more information, seerun Handlers.)
- An implicitrunhandler (optional):An implicitrunhandler consists of any statements outside of any contained handlers orscriptobjects.
An implicitrunhandler (optional):
An implicitrunhandler consists of any statements outside of any contained handlers orscriptobjects.
- Additional handlers (optional):A handler is the equivalent of a subroutine. (For details, seeAbout Handlers.)
Additional handlers (optional):
A handler is the equivalent of a subroutine. (For details, seeAbout Handlers.)
- Additionalscriptobjects (optional):Ascriptobject can contain nestedscriptobjects, each of which is defined just like a top-levelscriptobject, except that a nestedscriptobject is bracketed with statements that mark its beginning and end. (For details, seeScript Objects.)
Additionalscriptobjects (optional):
Ascriptobject can contain nestedscriptobjects, each of which is defined just like a top-levelscriptobject, except that a nestedscriptobject is bracketed with statements that mark its beginning and end. (For details, seeScript Objects.)
Here is an example of a simple script with one property, one handler, one nestedscriptobject, and an implicitrunhandler with two statements:
```
property defaultClientName : "Mary Smith"```
```
 ```
```
on greetClient(nameOfClient)```
```
    display dialog ("Hello " & nameOfClient & "!")```
```
end greetClient```
```
 ```
```
script testGreet```
```
    greetClient(defaultClientName)```
```
end script```
```
 ```
```
run testGreet --result: "Hello Mary Smith!"```
```
greetClient("Joe Jones") --result: "Hello Joe Jones!"```
The first statement in therunhandler isrun testGreet, which runs the nestedscriptobjecttestGreet. Thatscriptobject calls the handlergreetClient(), passing the propertydefaultClientName. The handler displays a dialog, greeting the default client, Mary Smith.
The second statement in therunhandler callsgreetClient()directly, passing the string"Joe Jones".

### Properties
Apropertyof an object is a characteristic that has a single value and a label, such as thenameproperty of a window or themonthproperty of a date. The definition for any AppleScript class includes the name and class for each of its properties. Property names must be unique within a class. Property values can be read/write or read only.
The AppleScriptdateclass, for example, defines both read/write and read only properties. These include theweekdayproperty, which is read only, and themonth,day, andyearproperties, which are read/write. Thatâs because the value of theweekdayproperty depends on the other propertiesâyou canât set an arbitrary weekday for an actual date.
The class of a property can be a simple class such asbooleanorinteger, a composite class such as apointclass (made up of two integers), or a more complex class.
Most classes only support predefined properties. However, for thescriptclass, AppleScript lets you to define additional properties. For information on how to do this, seeDefining Properties. You can also define properties forrecordobjects.

### Elements
Anelementis an object contained within another object. The definition for any AppleScript class includes the element types it can contain. An object can typically contain zero or more of each of its elements.
For a given element type, an object can contain many elements or none, and the number of elements that it contains may change over time. For example, it is possible for alistobject to contain no items (it can be an empty list). At a later time, the same list might contain many items.
Whether you can add elements to or remove elements from an object depends on the class and the element. For example, atextobject is immutableâyou cannot add or remove text once the object is created. For alistobject, you cannot remove items, but you can use thesetcommand to add an item to the beginning or end:
```
set myList to {1, "what", 3} --result: {1, "what", 3}```
```
set beginning of myList to 0```
```
set end of myList to "four"```
```
myList --result: {0, 1, "what", 3, "four"}```

## Object Specifiers
Anobject specifierspecifies the information needed to find another object in terms of the objects in which it is contained. An object specifier can refer to an application object, such as a window or file, or to an AppleScript object, such as an item in a list or a property in a record.
An object specifier is fully evaluated (or resolved) only when a script is run, not when it is compiled. A script can contain a valid object specifier (such asthird document of application "TextEdit"that causes an error when the script is executed (because, for example, there may be less than three documents open).
Applications typically return object specifiers in response to commands. For example, if you ask the Finder for a window, it returns information that specifies the window object your script asked for (if it exists). The top-level container in an object specifier is typically the application itself.
You create an object specifier every time your script uses a phrase that describes the path to an object or property, such asname of window 1 of application "Finder". When you use thea reference tooperator, it creates areferenceobject that wraps an object specifier.
The difference between an object specifier and the object it refers to is like the difference between a building address and the building itself. The address is a series of words and numbers, such as â2121 Oak Street, San Francisco, CAâ that identifies a location (on a street, in a city, in a state). It is distinct from the building itself. If the building at that location is torn down and replaced with a new building, the address remains the same.

### What Is in an Object Specifier
An object specifier describes an object type, a location, and how to distinguish the object from other objects of the same type in that location. These three types of informationâthe type, or class; the location, or container; and the distinguishing information, or reference formâallow you to specify any object.
In the following example, the class of the object isparagraph. The container is the phraseof document 1. Because this phrase is inside atellstatement, thetellstatement provides the top-level container,of application "TextEdit". The distinguishing information (the reference form) is the combination of the class,paragraph, and an index value,1, which together indicate the first paragraph.
```
tell application "TextEdit"```
```
    paragraph 1 of document 1```
```
end tell```
Note:If you examine the dictionary for the TextEdit application, you might think this script should sayparagraph 1 of text of document 1. However, where the meaning is unambiguous, some applications make life easier for scripters by allowing them to omit a container from an object specifier. TextEdit uses this feature in supplying animplicitly specified subcontainerfor the text in a document. That is, if an object specifier identifies an object, such as a word or paragraph, that is contained in a documentâs text, TextEdit automatically supplies theof textpart of the object specifier.
In addition to the index reference form, you can specify objects in a container by name, by range, by ID, and by the other forms described inReference Forms.

### Containers
A container is an object that contains one or more objects or properties. In an object specifier, a container specifies where to find an object or a property. To specify a container, use the wordoforin, as in the following statement (from a Findertellblock):
```
folder "Applications" of startup disk```
A container can be an object or a series of objects, listed from the innermost to the outermost containing object, as in the following:
```
tell application "Finder"```
```
    first item of first folder of first disk```
```
end tell```
You can also use the possessive form ('s) to specify containers. In the following example, the innermost container isfirst windowand the object it contains is anameproperty:
```
tell application "TextEdit"```
```
    first window's name```
```
end tell```
In this example, the target of thetellstatement ("TextEdit") is the outer container for the object specifier.

### Absolute and Relative Object Specifiers
Anabsolute object specifierhas enough information to identify an object or objects uniquely. It can be used unambiguously anywhere in a script. For a reference to an application object to be absolute, its outermost container must be the application itself, as in:
```
version of application "Finder" --result: "10.5.1"```
In contrast,arelative object specifierdoes not specify enough information to identify an object or objects uniquely; for example:
```
name of item 1 of disk 2```
When AppleScript encounters a relative object specifier in atellstatement, it attempts to use the default target specified by the statement to complete the object specifier. Though it isnât generally needed, this implicit target can be specified explicitly using the keywordit, which is described inThe it and me Keywords.
The default target of atellstatement is the object that receives commands if no other object is specified. For example, the followingtellstatement tells the Finder to get a name using the previous relative object specifier.
```
tell application "Finder"```
```
    name of item 1 of disk 2```
```
end tell```
When AppleScript encounters a relative object specifier outside anytellstatement, it tries to complete the object specifier by looking up the inheritance chain described inInheritance in Script Objects.

### Object Specifiers in Reference Objects
When you can create areferenceobject  with thea reference tooperator, it contains an object specifier. For example:
```
tell application "TextEdit"```
```
    set docRef to a reference to the first document```
```
    --result: document 1 of application "TextEdit"```
```
        -- an object specifier```
```
    name of docRef --result: "New Report.rtf"```
```
        -- name of the specified object```
```
end tell```
In this script, the variabledocRefis a reference whose object specifier refers to the first document of the application TextEditâwhich happens to be named âNew Report.rtfâ in this case. However, the object thatdocRefrefers to can change. If you open a second TextEdit document called âSecond Report.rtfâ so that its window is in front of the previous document, then run this script again, it will return the name of the now-frontmost document, âSecond Report.rtfâ.
You could instead create a reference with a more specific object specifier:
```
tell application "TextEdit"```
```
    set docRef to a reference to document "New Report.rtf"```
```
    --result: document "New Report.rtf" of application "TextEdit"```
```
    name of docRef --result: "New Report.rtf"```
```
end tell```
If you run this script after opening a second document, it will still return the name of the original document, âNew Report.rtfâ, if the document exists.
After you create areferenceobject with thea reference tooperator, you can use thecontentsproperty to get the value of the object that it refers to. That is, using thecontentsproperty causes the referenceâs object specifier to be evaluated. In the following script, for example, the content of the variablemyWindowis the window reference itself.
```
set myWindow to a ref to window "Q1.rtf" of application "TextEdit"```
```
myWindow```
```
    -- result: window "Q1.rtf" of application "TextEdit" (object specifier)```
```
contents of myWindow```
```
    --result: window id 283 of application "TextEdit" (an evaluated window)```
```
get myWindow```
```
    -- result: window "Q1.rtf" of application "TextEdit" (object specifier)```
Note that the result of thegetcommand is to return the referenceâs object specifier, not to resolve the specifier to the object it specifies.
When it can, AppleScript will implicitly dereference a reference object (without use of thecontentsproperty), as in the following example:
```
set myWindow to a ref to window 1 of application "TextEdit"```
```
name of myWindow --result: "Q1.rtf" (if that is the first window's name)```
For related information, see the Discussion section for thereferenceclass.

## Coercion (Object Conversion)
Coercion(also known asobject conversion) is the process of converting objects from one class to another. AppleScript converts an object to a different class in either of these circumstances:
- in response to theasoperator
in response to theasoperator
- automatically, when an object is of a different class than was expected for a particular command or operation
automatically, when an object is of a different class than was expected for a particular command or operation
Not all classes can be coerced to all other class types.Table 2-1summarizes the coercions that AppleScript supports for commonly used classes. For more information about each coercion, see the corresponding class definition inClass Reference.
AppleScript provides many coercions, either as a built-in part of the language or through the Standard Additions scripting addition. You can use these coercions outside of atellblock in your script. However, coercion of application class types may be dependent on the application and require atellblock that targets the application.
Theasoperator specifies a specific coercion or set of coercions. For example, the following statement coerces the integer2into the text"2"before storing it in the variablemyText:
```
set myText to 2 as text```
If you provide a command parameter or operand of the wrong class, AppleScript automatically coerces the operand or parameter to the expected class, if possible. If the conversion canât be performed, AppleScript reports an error.
When coercingtextstrings to values of classinteger,number, orreal, or vice versa, AppleScript uses the current Numbers settings in the Formats pane in International preferences to determine what separators to use in the string. When coercing strings to values of classdateor vice versa, AppleScript uses the current Dates settings in the Formats pane.
Convert from class
To class
Notes
alias
list(single-item)
text
application
list(single-item)
This is both an AppleScript class and an application class.
boolean
integer
list(single-item)
text
class
list(single-item)
text
constant
list(single-item)
text
date
list(single-item)
text
file
list(single-item)
text
integer
list(single-item)
real
text
Coercing anintegerto anumberdoes not change its class.
list(single-item)
any class to which the item can be coerced if it is not part of a list
list(multiple-item)
text, if each of the items in the list can be coerced to atextobject
number
integer
list(single-item)
real
text
Values identified as values of classnumberare really values of either classintegeror classreal.
POSIX file
seefile
POSIX fileis a pseudo-class equivalent to thefileclass.
real
integer
list(single-item)
In coercing tointeger, any fractional part is rounded.
Coercing arealto anumberdoes not change its class.
record
list
All labels are lost in the coercion and the resulting list cannot be coerced back to a record.
reference
any class to which the referenced object can be coerced
script
list(single-item)
text
integer
list(single-item)
real
Can coerce tointegerorrealonly if thetextobject represents an appropriate number.
unit types
integer
list(single-item)
real
text
Can coerce between unit types in the same category, such asinchestokilometers(length) orgallonstoliters(liquid volume).

## Scripting Additions
Ascripting additionis a file or bundle that provides handlers you can use in scripts to perform commands and coercions.
Many of the commands described in this guide are defined in the Standard Additions scripting addition in macOS. These commands are stored in the fileStandardAdditions.osaxin/System/Library/ScriptingAdditions, and are available to any script. You can examine the terminology for the Standard Additions by opening this file in Script Editor.
Note:A script can obtain the location of the Standard Additions with this script statement, which uses thepath to (folder)command:
path to scripting additions as text--result: "Hard_Disk:System:Library:ScriptingAdditions:"
```
path to scripting additions as text```
```
    --result: "Hard_Disk:System:Library:ScriptingAdditions:"```
Scripting additions can be embedded within bundled script applets by placing them in a folder namedScripting Additions(note the space between âScriptingâ and âAdditionsâ) inside the bundleâÂsContents/Resources/folder. Note that Script Editor does not look for embedded scripting additions when editing bundled applets. During script development, any required scripting additions must be properly installed in/System/ScriptingAdditions,/Library/ScriptingAdditions, or~/Library/ScriptingAdditionsso that Script Editor can find them.
Developers can create their own scripting additions, as described in Technical Note TN1164,Scripting Additions for Mac OS X. For related conceptual information, seeAppleScript Overview, particularly the section âExtending AppleScript with Coercions, Scripting Additions, and Faceless Background Applicationsâ in the chapterOpen Scripting Architecture.

## Commands Overview
Acommandis a word or a series of words used in AppleScript statements to request an action. Every command is directed at atarget, which is the object that responds to the command. The target is often anapplication object(one that is stored in an application or its documents and managed by the application, such as a window or document) or an object in macOS. However, it can also be ascriptobject or a value in the current script.
Commands often return results. For example, thedisplay dialogcommand returns a record that may contain text, a button name, and other information. Your script can examine this record to determine what to do next. You can assign the result of a command to a variable you define, or access it through the predefined AppleScriptresultvariable.

### Types of Commands
Scripts can make use of the following kinds of commands:
- AnAppleScript commandis one that is built into the AppleScript language. There currently are five such commands:get,set,count,copy, andrun. Except forcopy, each of these commands can also be implemented by applications. That is, there is an AppleScript version of the command that works on AppleScript objects, but an application can define its own version that works on the object types it defines.
AnAppleScript commandis one that is built into the AppleScript language. There currently are five such commands:get,set,count,copy, andrun. Except forcopy, each of these commands can also be implemented by applications. That is, there is an AppleScript version of the command that works on AppleScript objects, but an application can define its own version that works on the object types it defines.
- Ascripting addition commandis one that is implemented through the mechanism described inScripting Additions). Although anyone can create a scripting addition (see Technical Note TN1164,Scripting Additions for Mac OS X), this guide documents only the scripting addition commands from the Standard Additions, supplied by Apple as part of macOS. These commands are available to all scripts.
Ascripting addition commandis one that is implemented through the mechanism described inScripting Additions). Although anyone can create a scripting addition (see Technical Note TN1164,Scripting Additions for Mac OS X), this guide documents only the scripting addition commands from the Standard Additions, supplied by Apple as part of macOS. These commands are available to all scripts.
- Auser-defined commandis one that is implemented by a handler defined in ascriptobject. To invoke a user-defined command outside of atellstatement, simply use its name and supply values for any parameters it requires. The command will use the current script as its target.To invoke a user-defined command inside atellstatement, seeCalling Handlers in a tell Statement.
Auser-defined commandis one that is implemented by a handler defined in ascriptobject. To invoke a user-defined command outside of atellstatement, simply use its name and supply values for any parameters it requires. The command will use the current script as its target.
To invoke a user-defined command inside atellstatement, seeCalling Handlers in a tell Statement.
- Anapplication commandis one that is defined by scriptable application to provide access to a scriptable feature. They are typically enclosed in atellstatement that targets the application. You can determine which commands an application supports by examining its dictionary in Script Editor.Scriptable applications that ship with macOS, such as the Finder and System Events applications (located in/System/Library/CoreServices), provide many useful scripting commands.Third-party scriptable applications also provide commands you can use in scripts. Many support all or a subset of the Standard commands, described in Technical Note TN2106,Scripting Interface Guidelines. These include commands such asdelete,duplicate,exists, andmove, as well as application implementations of AppleScript commands, such asgetandset.
Anapplication commandis one that is defined by scriptable application to provide access to a scriptable feature. They are typically enclosed in atellstatement that targets the application. You can determine which commands an application supports by examining its dictionary in Script Editor.
Scriptable applications that ship with macOS, such as the Finder and System Events applications (located in/System/Library/CoreServices), provide many useful scripting commands.
Third-party scriptable applications also provide commands you can use in scripts. Many support all or a subset of the Standard commands, described in Technical Note TN2106,Scripting Interface Guidelines. These include commands such asdelete,duplicate,exists, andmove, as well as application implementations of AppleScript commands, such asgetandset.

### Target
There are two ways to explicitly specify an object as the target of a command: by supplying it as the direct parameter of the command (described in the next section) or by specifying it as the target of atellstatement that contains the command. If a script doesnât explicitly specify the target with atellstatement, and it isnât handled by a handler in the script or by AppleScript itself, it is sent to the next object in the inheritance chain (seeThe AppleScript Inheritance Chain).
In the following script, the target of thegetcommand is the object specifiername of first window. Because the enclosingtellstatement specifies the Finder application, the full specifier isname of first window of application "Finder", and it is the Finder application which obtains and returns the requested information.
```
tell application "Finder"```
```
    get name of first window```
```
end tell```
When a command targets an application, the result may be an application object. If so, subsequent statements that target the result object are sent to the application.
A script may also implicitly specify a target by using an application command imported using aNotestatement. For example, theextract addresscommand in the following script targets the Mail application because the command was imported from Mail:
```
use application "Mail"```
```
extract address from "John Doe <jdoe@example.com>"```

### Direct Parameter
Thedirect parameteris a value, usually an object specifier, that appears immediately next to a command and specifies the target of the command. Not all commands have a direct parameter. If a command can have a direct parameter, it is noted in the commandâs definition.
In the following statement, the object specifierlast file of window 1 of application "Finder"is the direct parameter of theduplicatecommand:
```
duplicate last file of window 1 of application "Finder"```
The direct parameter usually appears immediately after the command, but may also appear immediately before it. This can be easier to read for some commands, such asexistsin this example:
```
if file "semaphore" of application "Finder" exists then```
```
   -- continue processing...```
```
end if```
Atellstatement specifies a default target for all commands contained within it, so the direct parameter is optional. The following example has the same result as the previous example:
```
tell last file of window 1 of application "Finder"```
```
    duplicate```
```
end tell```

### Parameters That Specify Locations
Many commands have parameters that specify locations. A location can be either an insertion point or another object. Aninsertion pointis a location where an object can be added.
In the following example, thetoparameter specifies the location to which to move the first paragraph. The value of thetoparameter of theduplicatecommand is the relative object specifierbefore paragraph 4, which is an insertion point. AppleScript completes the specifier with the target of thetellstatement,front document of application "TextEdit".
```
tell front document of application "TextEdit"```
```
    duplicate paragraph 1 to before paragraph 4```
```
end tell```
The phrasesparagraph 1andbefore paragraph 4are called index and relative references, respectively. For more information, seeReference Forms.

## AppleScript Error Handling
During script execution, errors may occur due to interaction with macOS, problems encountered in an application script command, or problems caused by statements in the script itself. When an error occurs, AppleScript stops execution at the current location, signals an error, and looks up the calling chain for script statements that can handle the error. That is, it looks for the nearest error-handling code block that surrounds the location where the error occurred.
Scripts can handle errors by enclosing statements that may encounter an error within atrystatement. Thetrystatement includes anon errorsection that is invoked if an error occurs. AppleScript passes information about the error, including an error number and an error message, to theon errorsection. This allows scripts to examine the error number and to display information about it.
If the error occurs within a handler that does not provide atrystatement, AppleScript looks for an enclosingtrystatement where the handler was invoked. If none of the calls in the call chain is contained in atrystatement, AppleScript stops execution of the script and displays an error message (for any error number other than -128, described below).
A script can use anerrorstatement to signal an error directly. Doing so invokes the AppleScript error handling mechanism, which looks for an enclosingtrystatement to handle the error.
Some âerrorsâ are the result of the normal operation of a command. For example, commands such asdisplay dialogandchoose filesignalerror â128(User canceled), if the user clicks the Cancel button. Scripts routinely handle the user canceled error to ensure normal operation. For an example of how to do this, see the Examples section for thedisplay dialogcommand. If notrystatement in a script handles the -128 error, AppleScript halts execution of the script without displaying any error message.
For related information, seeResults,error Statements,try Statements,Error Numbers and Error Messages, andWorking with Errors.

## Global Constants in AppleScript
AppleScript defines a number of global constants that you can use anywhere in a script.

### AppleScript Constant
The global constantAppleScriptprovides access to properties you can use throughout your scripts.
You can use theAppleScriptidentifier itself to distinguish an AppleScript property from a property of the current target with the same name, as shown in the sectionversion.
The following sections describe additional properties ofAppleScript.

#### pi
Thismathematicalvalue represents the ratio of a circle's circumference to its diameter. It is defined as a real number with the value 3.14159265359.
For example, the following statement computes the area of a circle with radius 7:
```
set circleArea to pi * 7 * 7 --result: 153.9380400259```

#### result
When a statement is executed, AppleScript stores the resulting value, if any, in the predefined propertyresult. The value remains there until another statement is executed that generates a value. Until a statement that yields a result is executed, the value ofresultis undefined. You can examine the result in Script Editor by looking in the Result pane of the script window.
Note:When an error occurs during script execution, AppleScript signals an error. It doesnât return error information in theresultproperty. For more information, seeAppleScript Error Handling.

#### Text Constants
AppleScript defines the text propertiesspace,tab,return,linefeed, andquote. You effectively use these properties as text constants to represent white space or a double quote (") character. They are described in the Special String Characters section of thetextclass.

#### text item delimiters
AppleScript provides thetext item delimitersproperty for use in processing text. This property consists of a list of strings used as delimiters by AppleScript when it coerces a list to text or gets text items from text strings. When gettingtext itemsof text, all of the strings are used as separators. When coercing a list to text, the first item is used as a separator.
Note:Prior to OS X Snow Leopard v10.6, AppleScript only used the first delimiter in the list when gettingtext items.
Becausetext item delimitersrespectconsideringandignoringattributes in AppleScript 2.0, delimiters are case-insensitive by default. Formerly, they were always case-sensitive. To enforce the previous behavior, add an explicitconsidering casestatement.
You can get and set the current value of thetext item delimitersproperty. Normally, AppleScript doesnât use any delimiters. For example, if the text delimiters have not been explicitly changed, the statement
```
{"bread", "milk", "butter", 10.45}  as string```
returns the following:
```
"breadmilkbutter10.45"```
For printing or display purposes, it is usually preferable to settext item delimitersto something thatâs easier to read. For example, the script
```
set AppleScript's text item delimiters to {", "}```
```
{"bread", "milk", "butter", 10.45}  as string```
returns this result:
```
"bread, milk, butter, 10.45"```
Thetext item delimitersproperty can be used to extract individual names from a pathname. For example, the script
```
set AppleScript's text item delimiters to {":"}```
```
get last text item of "Hard Disk:CD Contents:Release Notes"```
returns the result"Release Notes".
If you change thetext item delimitersproperty in Script Editor, it remains changed until you restore its previous value or until you quit Script Editor and launch it again. If you changetext item delimitersin a script application, it remains changed in that application until you restore its previous value or until the script application quits; however, the delimiters are not changed in Script Editor or in other script applications you run.
Scripts commonly use an error handler to reset thetext item delimitersproperty to its former value if an error occurs (for more on dealing with errors, seeAppleScript Error Handling):
```
set savedDelimiters to AppleScript's text item delimiters```
```
try```
```
    set AppleScript's text item delimiters to {"**"}```
```
    --other script statements...```
```
    --now reset the text item delimiters:```
```
    set AppleScript's text item delimiters to savedDelimiters```
```
on error m number n```
```
    --also reset text item delimiters in case of an error:```
```
    set AppleScript's text item delimiters to savedDelimiters```
```
    --and resignal the error:```
```
    error m number n```
```
end try```

#### version
This property provides the current version of AppleScript. The following script shows how to check for a version greater than or equal to version 1.9. Theifstatement is wrapped in aconsidering numeric stringsstatement so that an AppleScript version such as1.10.6compares as larger than, say, version1.9.
```
considering numeric strings```
```
    if version of AppleScript as string â¥ "1.9" then```
```
        -- Perform operations that depend on version 1.9 or greater```
```
    else```
```
        -- Handle case where version is not high enough```
```
    end if```
```
end considering```
Applications can have their ownversionproperty, so to access the AppleScript version explicitly, you use the phraseversion of AppleScript. This will work inside atellblock that targets another application, such as the following:
```
tell application "Finder"```
```
    version --result: "10.5.1"```
```
    version of AppleScript --result: "2.0"```
```
end tell```

### current application Constant
Thecurrent applicationconstant refers to the application that is executing the current AppleScript script (for example, Script Editor). Because the current application is the parent of AppleScript(seeThe AppleScript Inheritance Chain), it gets a chance to handle commands that arenât handled by the current script or by AppleScript.
Thecurrent applicationconstant is an object specifierâif you ask AppleScript for its value, the result is the object specifier:
```
get current application --result: current application```
However, if you ask forname of current application, AppleScript resolves the object specifier and returns the current applicationâs name:
```
name of current application --result: "Script Editor"```

### missing value Constant
Themissing valueconstant is a placeholder for missing or uninitialized information.
For example, the following statements use themissing valueconstant to determine if a variable has changed:
```
set myVariable to missing value```
```
    -- perform operations that might change the value of myVariable```
```
if myVariable is equal to missing value then```
```
    -- the value of the variable never changed```
```
else```
```
    -- the value of the variable did change```
```
end if```

### true, false Constants
AppleScript defines theBoolean constantstrueandfalse. These constants are described with thebooleanclass.

## The it and me Keywords
AppleScript defines the keywordmeto refer to the current script and the keyworditto refer to the current target. (Thecurrent scriptis the one that is currently being executed; thecurrent targetis the object that is the current default target for commands.) It also definesmyas a synonym forof meanditsas a synonym forof it.
If a script hasnât targeted anything,itandmerefer to the same thingâthe scriptâas shown in the following example:
```
-- At the top-level of the script:```
```
me --result: Â«scriptÂ» (the top-level script object)```
```
it --result: Â«scriptÂ» (same as it, since no target set yet)```
Atellstatement specifies a default target. In the following example, the default target is the Finder application:
```
-- Within a tell block:```
```
tell application "Finder" -- sets target```
```
    me --result: Â«scriptÂ» (still the top-level script object)```
```
    it --result: application "Finder" (target of the tell statement)```
```
end tell```
You can use the wordsof meormyto indicate that the target of a command is the current script and not the target of thetellstatement. In the following example, the wordmyindicates thatminimumValue()handler is defined by the script, not by Finder:
```
tell application "Finder"```
```
    set fileCount to count files in front window```
```
    set myCount to my minimumValue(fileCount, 100)```
```
    --do something with up to the first 100 filesâ¦```
```
end tell```
You can also useof meormyto distinguish script properties from object properties. Suppose there is a TextEdit document open named âSimple.rtfâ:
```
tell document 1 of application "TextEdit"```
```
    name --result: "Simple.rtf" (implicitly uses target of tell)```
```
    name of it --result: "Simple.rtf" (specifies target of tell)```
```
    me --result: Â«scriptÂ» (top-level script object, not target of tell)```
```
end tell```
The following example shows how to specify differentversionproperties in a Findertellstatement. The Finder is the default target, but usingversion of me,my version, orversion of AppleScriptallows you to specify the version of the top-levelscriptobject. (The top-levelscriptobject returns the AppleScript version, because it inherits from AppleScript, as described inThe AppleScript Inheritance Chain.)
```
tell application "Finder"```
```
    version --result: "10.5.1" (Finder version is the default in tell block)```
```
    its version --result: "10.5.1" (specifically asks for Finder version)```
```
    version of me --result: "2.0" (AppleScript version)```
```
    my version --result: "2.0" (AppleScript version)```
```
    version of AppleScript --result: "2.0" (AppleScript version)```
```
end tell```
For information on usingitin a filter reference, see the Discussion section for theFilterreference form.

## Aliases and Files
To refer to items and locations in the macOS file system, you usealiasobjects andfileobjects.
Analiasobject is a dynamic reference to an existing file system object. Because it is dynamic, it can maintain the link to its designated file system object even if that object is moved or renamed.
Afileobject represents a specific file at a specific location in the file system. It can refer to an item that does not currently exist, such as the name and location for a file that is to be created. Afileobject is not dynamic, and always refers to the same location, even if a different item is moved into that place. ThePOSIX filepseudo-class is roughly synonymous with file:POSIX filespecifiers evaluate to afileobject, but they use different semantics for the name, as described inSpecifying Paths.
The following is the recommended usage for these types:
- Use analiasobject to refer to existing file system objects.
Use analiasobject to refer to existing file system objects.
- Use afileobject to refer to a file that does not yet exist.
Use afileobject to refer to a file that does not yet exist.
- Use aPOSIX filespecifier if you want to specify the file using a POSIX path.
Use aPOSIX filespecifier if you want to specify the file using a POSIX path.
The following sections describe how to specify file system objects by path and how to work with them in your scripts.

### Specifying Paths
You can createaliasobjects andfileobjects by supplying a name specifier, where the name is the path to an item in the file system.
For alias and file specifiers, the path is an HFS path, which takes the form"disk:item:subitem:subsubitem:...:item". For example,"Hard_Disk:Applications:Mail.app"is the HFS path to the Mail application, assuming your boot drive is named"Hard_Disk".
HFS paths with a leading colon, such as":folder:file", are resolved relative to the HFS working directory. However, their use is discouraged, because the location of the HFS working directory is unspecified, and there is no way to control it from AppleScript.
For POSIX file specifiers, the path is a POSIX path, which takes the form"/item/subitem/subsubitem/.../item". The disk name is not required for the boot disk. For example,"/Applications/Mail.app"is the POSIX path to the Mail application. You can see the POSIX path of an item in Finder in the "Where" field of its Get Info window. Despite the name, POSIX file specifiers may refer to folders or disks. Use of"~"to specify a home directory is not supported.
POSIX paths without a leading slash, such as"folder/file", are resolved relative to the POSIX working directory. This is supported, but only is useful for scripts run from the shellâthe working directory is the current directory in the shell. The location of the POSIX working directory for applications is unspecified.

### Working With Aliases
AppleScript defines thealiasclass to represent aliases. An alias can be stored in a variable and used throughout a script.
The following script first creates an alias to an existing file in the variablenotesAlias, then uses the variable in atellstatement that opens the file. It uses atrystatement to check for existence of the alias before creating it, so that the alias is only created once, even if the script is run repeatedly.
```
try```
```
    notesAlias -- see if we've created the alias yet```
```
on error```
```
    -- if not, create it in the error branch```
```
    set notesAlias to alias "Hard_Disk:Users:myUser:Feb_Notes.rtf"```
```
end try```
```
-- now open the file from the alias:```
```
tell application "TextEdit" to open notesAlias```
Finding the object an alias refers to is calledresolvingan alias. AppleScript 2.0 attempts to resolve aliases only when you run a script. However, in earlier versions, AppleScript attempts to resolve aliases at compile time.
Once you run the previous example, creating the alias, the script will be able to find the original file when you run it again, even if the fileâs name or location changes. (However, if you run the script again after recompiling it, it will create a new alias.)
You can get the HFS path from an alias by coercing it to text:
```
notesAlias as text --result: "Hard_Disk:Users:myUser:Feb_Notes.rtf"```
You can use thePOSIX pathproperty to obtain a POSIX-style path to the item referred to by an alias:
```
POSIX path of notesAlias --result: "/Feb_Notes.rtf"```
If an alias doesnât refer to an existing file system object then it is broken. You canât create an alias to an object that doesnât exist, such as a file you plan to create. For that you use afileobject, described in the next section.
For a sample script that shows how a script application can process a list of aliases it receives when a user drops one or more file icons on it, seeopen Handlers.

### Working With Files
AppleScript usesfileobjects to represent files in scripts. Afileobject can be stored in a variable and used throughout a script. The following script first creates afileobject for an existing file in the variablenotesFile, then uses the variable in atellstatement that opens the file:
```
set notesFile to POSIX file "/Users/myUser/Feb_Meeting_Notes.rtf"```
```
tell application "TextEdit" to open notesFile```
You can use afileobject to specify a name and location for a file that may not exist:
```
set newFile to POSIX file "/Users/myUser/BrandNewFile.rtf"```
Similarly, you can let a user specify a new file with thechoose file namecommand, then use the returnedfileobject to create the file. In the following example, if the user cancels thechoose file namedialog, the rest of the script is not executed. If the user does supply a file name, the script opens the file, creating it if necessary, then uses atrystatement to make sure it closes the file when it is finished writing to it.
```
set theFile to choose file name```
```
set referenceNumber to open for access theFile with write permission```
```
try```
```
    -- statements to write to the file```
```
on error```
```
    close access referenceNumber```
```
end try```
```
close access referenceNumber```
Typically, when you pass afileobject to a command that uses it to operate on a new or existing item in the file system, the components of the path must exist for the command to succeed.

## Remote Applications
A script can target an application on a remote computer if remote applications are enabled on that computer, and if the script specifies the computer with an eppc-style specifier.

### Enabling Remote Applications
For a script to send commands to a remote application, the following conditions must be satisfied:
- The computer that contains the application and the computer on which the script is run must be connected to each other through a network.
The computer that contains the application and the computer on which the script is run must be connected to each other through a network.
- Remote Apple Events (set in the Sharing preferences pane) must be enabled on the remote computer and user access must be provided (you can allow access for all users or for specified users only).
Remote Apple Events (set in the Sharing preferences pane) must be enabled on the remote computer and user access must be provided (you can allow access for all users or for specified users only).
- If the specified remote application is not running, you must run it.
If the specified remote application is not running, you must run it.
- You must authenticate as admin when you compile or run the script.
You must authenticate as admin when you compile or run the script.

### eppc-Style Specifiers
An eppc-style specifier takes the following format:
```
eppc://[user[:password]@]IP_address```
Either a numeric IP address in dotted decimal form (four numbers, from 0 to 255, separated by periods; for example,123.23.23.123) or a hostname. A hostname can be a Bonjour name.
The following are examples of valid eppc-style specifiers. If you supply the user name and password, no authentication is required. If you do not supply it, authentication may be required.
```
"eppc://myCoolMac.local" -- hostname, no user or pwd```
```
"eppc://myUserName:pwd@myCoolMac.local" -- user, pwd, and hostname```
```
"eppc://123.23.23.123" -- IP address, no user or pwd```
```
"eppc://myUserName:pwd@123.23.23.123" -- user, pwd, and IP address```
```
"eppc://myUserName@server.company.com" -- server address, user```
Important:If a part of the eppc-style specifier contains non-UTF-8 characters or white space, it must be URL-encoded: for example, here is a user name that contains a space:
Â Â ÂJohn%20Smith.

### Targeting Remote Applications
You can target an application that is running on a remote machine and you can launch applications on remote machines that are not currently running.
The following example uses an eppc-style specifier to target the Finder on a remote computer. It includes a user name and password, so no authentication is required.
```
set remoteMachine to "eppc://userName:pwd@MacName.local"```
```
tell app "Finder" of machine remoteMachine to close front window```
Important:If you compile an erroneous eppc-style address, you will have to quit and relaunch Script Editor for changes to that address to take effect.
In some cases, youâll need to use ausing terms fromstatement to tell AppleScript to compile against the local version of an application. The following example uses that technique in telling the remote Finder application to open the TextEdit application:
```
set remoteFinder to application "Finder" of machine Â¬```
```
    "eppc://myUserName:pwd@123.23.23.123"```
```
 ```
```
using terms from application "Finder"```
```
    tell remoteFinder```
```
        open application file id "com.apple.TextEdit"```
```
    end tell```
```
end using terms from```
If you omit the password (pwd) in the previous script, you will have to authenticate when you run the script.

## Debugging AppleScript Scripts
AppleScript does not include a built-in debugger, but it does provide several simple mechanisms to help you debug your scripts or just observe how they are working.

### Feedback From Your Script
You can insert various statements into a script to indicate the current location and other information. In the simplest case, you can insert a beep command in a location of interest:
```
beep 3 -- three beeps; a very important part of the script!```
Adisplay dialogcommand can display information about whatâs happening in a script and, like a breakpoint, it halts execution until you dismiss it (or until it times out, depending on the parameters you pass). The following example displays the current script location and the value of a variable:
```
display dialog "In factorial routine; x = " & (x as string)```
Thesaycommand can get your attention by speaking the specified text. In the following example,currentClientis atextobject that stores a client name:
```
say "I'm in the clientName handler. The client is " & currentClient```

### Logging
Script Editor can display a log of the Apple events that are sent during execution of a script. In the Script Editor Preferences, you can also choose to keep a history of recent results or event logs.
In addition, you can insertlogstatements into a script. Log output is shown in the Event Log pane of a script window, and also in theEvent Log History window, if it is open.
The following simple example logs the current word in arepeat with loopVariable (in list)statement:
```
set wordList to words in "Where is the hammer?"```
```
repeat with currentWord in wordList```
```
    log currentWord```
```
    if contents of currentWord is equal to "hammer" then```
```
        display dialog "I found the hammer!"```
```
    end if```
```
end repeat```
The following shows how the words appear in the log when the script is run:
```
    (*Where*)```
```
    (*is*)```
```
    (*the*)```
```
    (*hammer*)```

### Third Party Debuggers
If you need full-featured debugging capabilities, there are powerful, third-party AppleScript debuggers available.
Copyright © 2016 Apple Inc. All Rights Reserved.Terms of Use|Privacy Policy|  Updated: 2016-01-25