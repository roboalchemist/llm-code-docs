# Script Objects

This chapter describes thescriptobject, which is used to implement all AppleScript scripts. Before reading this chapter, you should be familiar with the information inAppleScript and Objects.
Ascript objectis a user-defined object that can combine data (in the form of properties) and actions (in the form of handlers and additionalscriptobjects). Script objects support inheritance, allowing you to define a hierarchy of objects that share properties and handlers. You can also extend or modify the behavior of a handler in onescriptobject when calling it from anotherscriptobject.
The top-levelscriptobject is the one that implements the overall script you are working on. Anyscriptobject can contain nestedscriptobjects, each of which is defined just like a top-levelscriptobject, except that a nestedscriptobject is bracketed with statements that mark its beginning and end.
This chapter describesscriptobjects in the following sections:

- Defining Script Objectsshows the syntax for definingscriptobjects and includes a simple example .
Defining Script Objectsshows the syntax for definingscriptobjects and includes a simple example .

- Initializing Script Objectsdescribes how AppleScript creates ascriptobject with the properties and handlers you have defined.
Initializing Script Objectsdescribes how AppleScript creates ascriptobject with the properties and handlers you have defined.

- Sending Commands to Script Objectsdescribes how you usetellstatements to send commands toscriptobjects.
Sending Commands to Script Objectsdescribes how you usetellstatements to send commands toscriptobjects.

- Script Librariesdescribes script libraries and how to use them from other scripts.
Script Librariesdescribes script libraries and how to use them from other scripts.

- Inheritance in Script Objectsdescribes inheritance works and how you can use it to share functionality in thescriptobjects you define.
Inheritance in Script Objectsdescribes inheritance works and how you can use it to share functionality in thescriptobjects you define.

## Defining Script Objects

Eachscriptobject definition (except for the top-levelscriptobject) begins with the keywordscript, followed by a variable name, and ends with the keywordend(orend script). The statements in between can be any combination of property definitions, handler definitions, nestedscriptobject definitions, and other AppleScript statements.
The syntax of ascriptobject definition is as follows:
scriptvariableName
Â Â Â Â [ (property|prop)parent :parentSpecifier]
Â Â Â Â [ (property|prop)propertyLabel:initialValue]...
Â Â Â Â [handlerDefinition]...
Â Â Â Â [statement]...
end[script]
A variable identifier for the script. You can refer to a script object by this name elsewhere in a script.
Specifies the parent of thescriptobject, typically anotherscriptobject.
For more information, seeInheritance in Script Objects.
An identifier, unique within thescriptobject, that specifies a characteristic of the  object; equivalent to an instance variable.
The value that is assigned to the property each time thescriptobject is initialized.scriptobjects are initialized when compiled.initialValueis required in property definitions.
A handler for a command thescriptobject can respond to; equivalent to a method. For more information, seeAbout HandlersandHandler Reference.
Any AppleScript statement. Statements other than handler and property definitions are treated as if they were part of an implicit handler definition for theruncommand; they are executed when ascriptobject receives theruncommand.
Here is a simplescriptobject definition:

```

script John```

```

    property HowManyTimes : 0```

```

 ```

```

    to sayHello to someone```

```

        set HowManyTimes to HowManyTimes + 1```

```

        return "Hello " & someone```

```

    end sayHello```

```

 ```

```

end script```
It defines ascriptobject that can handle thesayHellocommand. It assigns thescriptobject to the variableJohn. The definition includes a handler for thesayHellocommand. It also includes a property, calledHowManyTimes, that indicates how many times thesayHellocommand has been called.
A handler within ascriptobject definition follows the same syntax rules as any other handler.
You can use atellstatement to send commands to ascriptobject. For example, the following statement sends thesayHellocommand thescriptobject defined above.

```

tell John to sayHello to "Herb" --result: "Hello Herb"```
You can manipulate the properties ofscriptobjects by using thegetcommand to get the value of a property and thesetorcopycommand to change the value. The value of a property is persistentâit gets reset every time you compile the script, but not when you run it.

## Initializing Script Objects

When you define ascriptobject, it can contain properties, handlers, and nestedscriptobject definitions. When you execute the script containing it, AppleScript creates ascriptobject with the defined properties, handlers, and nestedscriptobjects. The process of creating an instance of ascriptobject from its definition is called initialization. Ascriptobject must be initialized before it can respond to commands.
A top-levelscriptobject is initialized each time the scriptâsrunhandler is executed. Similarly, if you define a script within a handler, AppleScript initializes ascriptobject each time the handler is called. The parameter variables in the handler definition become local variables of thescriptobject.
For example, themakePointhandler in the following script contains ascriptobject definition for thescriptobjectthePoint:

```

on makePoint(x, y)```

```

    script thePoint```

```

        property xCoordinate:x```

```

        property yCoordinate:y```

```

    end script```

```

    return thePoint```

```

end makePoint```

```

 ```

```

set myPoint to makePoint(10,20)```

```

get xCoordinate of myPoint  --result: 10```

```

get yCoordinate of myPoint  --result: 20```
AppleScript initializes thescriptobjectthePointwhen it executes themakePointcommand. After the call tomakePoint, the variablemyPointrefers to thisscriptobject. The parameter variables in themakePointhandler, in this case,xandy, become local variables of thescriptobject. The initial value ofxis 10, and the initial value ofyis 20, because those are the parameters passed to themakePointhandler that initialized thescriptobject.
If you added the following line to the end of the previous script and ran it, the variablemyOtherPointwould refer to a second instance of thescriptobjectthePoint, with different property values:

```

set myOtherPoint to makePoint(30,50)```
ThemakePointscript is a kind of constructor function that createsscriptobjects representing points.

## Sending Commands to Script Objects

You can usetellstatements to send commands toscriptobjects. For example, the followingtellstatement sends twosayHellocommands to thescriptobjectJohn(defined below):

```

tell John```

```

    sayHello to "Herb"```

```

    sayHello to "Grace"```

```

end tell```
For ascriptobject to respond to a command within atellstatement, either thescriptobject or its parent object must have a handler for the command. For more information about parent objects, seeInheritance in Script Objects.
Ascriptobject definition may include an implicitrunhandler, consisting of all executable statements that are outside of any handler or nestedscriptobject, or it may include an explicitrunhandler that begins withon run, but it may not contain bothâsuch a script will not compile. If a script has no run handler (for example, a script that serves as a library of handlers, as described inParameter Specifications), executing the script does nothing. However, sending it an explicitruncommand causes an error. For more information, seerun Handlers.
Thedisplay dialogcommand in the followingscriptobject definition is the only executable statement at the top level, so it constitutes thescriptobjectâs implicitrunhandler and is executed when the script sends aruncommand toscriptobjectJohn, with the statementtell John to run.

```

script John```

```

    property HowManyTimes : 0```

```

    to sayHello to someone```

```

        set HowManyTimes to HowManyTimes + 1```

```

        return "Hello " & someone```

```

    end sayHello```

```

    display dialog "John received the run command"```

```

end script```

```

 ```

```

tell John to run```
You can also use the possessive to send a command to ascriptobject. For example, either of the following two forms send thesayHellocommand to scriptJohn(the first version compiles into the second):

```

John's sayHello to "Jake" --result: "Hello Jake"```

```

sayHello of John to "Jake" --result: "Hello Jake"```

## Script Libraries

A top-levelscriptobject saved in a Script Libraries folder becomes ascript libraryusable by other scripts. Libraries let you share and reuse handlers, reorganize large scripts into a set of smaller libraries that are easier to manage, and build richer, higher-level functionality out of simpler libraries.
Note:Libraries are supported in OS X Mavericks v10.9 (AppleScript 2.3) and later. To share properties and handlers between scripts in prior OS versions, use theload scriptcommand as described inLibraries using Load Script.

### Creating a Library

The basic requirement for a script to be a script library is its location: it must be a script document in a âScript Librariesâ folder in one of the following folders. When searching for a library, the locations are searched in the order listed, and the first matching script is used:

- If the script that references the library is a bundle, the scriptâs bundleResourcesdirectory. This means that scripts may be packaged and distributed with the libraries they use.
If the script that references the library is a bundle, the scriptâs bundleResourcesdirectory. This means that scripts may be packaged and distributed with the libraries they use.

- If the application running the script is a bundle, the applicationâs bundleResourcesdirectory. This means that script applications (âappletsâ and âdropletsâ) may be packaged and distributed with the libraries they use. It also enables applications that run scripts to provide libraries for use by those scripts.
If the application running the script is a bundle, the applicationâs bundleResourcesdirectory. This means that script applications (âappletsâ and âdropletsâ) may be packaged and distributed with the libraries they use. It also enables applications that run scripts to provide libraries for use by those scripts.

- Any folders specified in the environment variableOSA_LIBRARY_PATH. This allows using a library without installing it in one of the usual locations. The value of this variable is a colon-separated list of paths, such as/opt/local/Script Libraries:/usr/local/Script Libraries. Unlike the other library locations, paths specified inOSA_LIBRARY_PATHare used exactly as-is, without appending âScript Librariesâ.Supported in OS X v10.11 and later.
Any folders specified in the environment variableOSA_LIBRARY_PATH. This allows using a library without installing it in one of the usual locations. The value of this variable is a colon-separated list of paths, such as/opt/local/Script Libraries:/usr/local/Script Libraries. Unlike the other library locations, paths specified inOSA_LIBRARY_PATHare used exactly as-is, without appending âScript Librariesâ.Supported in OS X v10.11 and later.

- The Library folder in the userâs home directory,~/Library. This is the location to install libraries for use by a single user, and is the recommended location during library development.
The Library folder in the userâs home directory,~/Library. This is the location to install libraries for use by a single user, and is the recommended location during library development.

- The computer Library folder,/Library. Libraries located here are available to all users of the computer.
The computer Library folder,/Library. Libraries located here are available to all users of the computer.

- The network Library folder,/Network/Library. Libraries located here are available to multiple computers on a network.
The network Library folder,/Network/Library. Libraries located here are available to multiple computers on a network.

- The system Library folder,/System/Library. These are libraries provided by macOS.
The system Library folder,/System/Library. These are libraries provided by macOS.

- Any installed application bundle, in the applicationâs bundleLibrarydirectory. This allows distributing libraries that are associated with an application, or creating applications that exist solely to distribute libraries.Supported in OS X v10.11 and later.
Any installed application bundle, in the applicationâs bundleLibrarydirectory. This allows distributing libraries that are associated with an application, or creating applications that exist solely to distribute libraries.Supported in OS X v10.11 and later.
Script libraries also havename,id, andversionproperties. It is recommended that you define all three, especially for libraries you plan to distribute publicly: doing so allows clients to unambiguously identify particular versions of libraries that have the functionality they need. These properties may be defined either aspropertydefinitions within the script itself, or, for script bundles, in the Info.plist file, which can be edited using the Bundle Contents drawer in Script Editor. For details, see thescriptclass reference.
A script library may be a single-file (scpt) or bundle format (scptd). If a library is a bundle, it may define its own terminology.

#### Defining Scripting Terminology

Libraries may define scripting terminology, including commands, properties and enumerated values, by supplying a Scripting Definition (sdef) file in their bundle. Like applications, this terminology is available to client scripts when they target the library withtelloruse, and to the library script itself.
To define terminology, create an sdef file as described in theCocoa Scripting GuideunderPreparing a Scripting Definition File. Then, copy the file to the bundleâs Resources directory and set the Info.plist keyOSAScriptingDefinitionto the base name of the sdef file (that is, the file name without the â.sdefâ extension). Script Editorâs Bundle Contents drawer can do this for you: drag the file into the âResourcesâ list to copy the file into the bundle, and enter the base name of the sdef file in the âScripting Definitionâ field.

### Using a Library

A script library defines a script object, which a client script may then reference and then send commands to, as described inSending Commands to Script Objects. Libraries are identified by name:

```

script "My Library"```
AppleScript will search the various Script Library folders, as described above inCreating a Library, and create an instance of the library script. Unlike the result fromload script, this instance is shared and persists for at least the lifetime of the client script, so you do not have to save it in a variable, and state will be preserved while the client script is running. For example, given this library script:

```

property name : "Counter"```

```

property nextNumberProperty : 0```

```

on nextNumber()```

```

    set my nextNumberProperty to my nextNumberProperty + 1```

```

    return my nextNumberProperty```

```

end nextNumber```
This client script, despite referencing the library in full both times, will log â1â and then â2â:

```

tell script "Counter" to log its nextNumber() -- logs "1"```

```

tell script "Counter" to log its nextNumber() -- logs "2"```
Note:Library script instances are unique to, and persistent for the lifetime of, the AppleScript interpreter that loads them. Script Editor, Script Menu, and Folder Actions all run their scripts using a separate interpreter for each script; applets and AppleScriptObjC applications use a single interpreter for the entire application; and other applications may do either. If you are designing a library, try to not rely on persistent state in the library script itself, since its lifetime will vary depending on how the client script is run.

## Inheritance in Script Objects

You can use the AppleScript inheritance mechanism to define relatedscriptobjects in terms of one another. This allows you to share property and handler definitions among manyscriptobjects without repeating the shared definitions. Inheritance is described in the following sections:

- The AppleScript Inheritance Chain
The AppleScript Inheritance Chain

- Defining Inheritance Through the parent Property
Defining Inheritance Through the parent Property

- Some Examples of Inheritance
Some Examples of Inheritance

- Using the continue Statement in Script Objects
Using the continue Statement in Script Objects

### The AppleScript Inheritance Chain

The top-levelscriptobject is the parent of all otherscriptobjects, although anyscriptobject can specify a different parent object. The top-levelscriptobject also has a parentâAppleScript itself (the AppleScript component). And even AppleScript has a parentâthe current application. The name of that application (which is typically Script Editor) can be obtained through the global constantcurrent application. This hierarchy defines theinheritance chainthat AppleScript searches to find the target for a command or the definition of a term.
Everyscriptobject has access to the properties, handlers, and script objects it defines, as well as to those defined by its parent, and those of any other object in the inheritance chain, including AppleScript. Thatâs why the constants and properties described inGlobal Constants in AppleScriptare available to any script.
Note:There is an exception to the previous claim. An explicitlocalvariable canshadow(or block access to) aglobalvariable or property with the same name, making the global version inaccessible in the scope of the handler orscriptobject. For related information, seeScope of Variables and Properties.

### Defining Inheritance Through the parent Property

When working withscriptobjects,inheritanceis the ability of a childscriptobject to take on the properties and handlers of a parent object. You specify inheritance with theparentproperty.
The object listed in aparentproperty definition is called theparent object, or parent. Ascriptobject that includes aparentproperty is referred to as achild script object, or child. Theparentproperty is not required, though if one is not specified, every script is a child of the top-level script, as described inThe AppleScript Inheritance Chain. Ascriptobject can have many children, but a childscriptobject can have only one parent. The parent object may be any object, such as alistor anapplicationobject, but it is typically anotherscriptobject.
The syntax for defining a parent object is
(property|prop)parent :variable
An identifier for a variable that refers to the parent object.
Ascriptobject must be initialized before it can be assigned as a parent of anotherscriptobject. This means that the definition of a parentscriptobject (or a command that calls a function that creates a parentscriptobject) must come before the definition of the child in the same script.

### Some Examples of Inheritance

The inheritance relationship betweenscriptobjects should be familiar to those who are acquainted with C++ or other object-oriented programming languages. A childscriptobject that inherits the handlers and properties defined in its parent is like a C++ class that inherits methods and instance variables from its parent class. If the child does not have its own definition of a property or handler, it uses the inherited property or handler. If the child has its own definition of a particular property or handler, then it ignores (or overrides) the inherited property or handler.
Listing 4-1shows the definitions of a parentscriptobject calledAlexand a childscriptobject calledAlexJunior.
Listing 4-1A pair of script objects with a simple parent-child relationship

```

script Alex```

```

    on sayHello()```

```

        return "Hello, " & getName()```

```

    end sayHello```

```

    on getName()```

```

        return "Alex"```

```

    end getName```

```

end script```

```

 ```

```

script AlexJunior```

```

    property parent : Alex```

```

    on getName()```

```

        return "Alex Jr"```

```

    end getName```

```

end script```

```

 ```

```

-- Sample calls to handlers in the script objects:```

```

tell Alex to sayHello() --result: "Hello, Alex"```

```

tell AlexJunior to sayHello() --result: "Hello, Alex Jr."```

```

 ```

```

tell Alex to getName() --result: "Alex"```

```

tell AlexJunior to getName() --result: "Alex Jr"```
Eachscriptobject defines agetName()handler to return its name. ThescriptobjectAlexalso defines thesayHello()handler. BecauseAlexJuniordeclares Alex to be its parent object, it inherits thesayHello()handler.
Using atellstatement to invoke thesayHello()handler ofscriptobjectAlexreturns"Hello, Alex". Invoking the same handler ofscriptobjectAlexJuniorreturns"Hello, Alex Jr"âalthough the samesayHello()handler inAlexis executed, when that handler callsgetName(), itâs thegetName()inAlexJuniorthat is executed.
The relationship between a parentscriptobject and its childscriptobjects is dynamic. If the properties of the parent change, so do the inherited properties of the children. For example, thescriptobjectJohnSonin the following script inherits itsvegetableproperty fromscriptobjectJohn.

```

script John```

```

    property vegetable : "Spinach"```

```

end script```

```

script JohnSon```

```

    property parent : John```

```

end script```

```

set vegetable of John to "Swiss chard"```

```

vegetable of JohnSon```

```

--result: "Swiss chard"```
When you change thevegetableproperty ofscriptobjectJohnwith thesetcommand, you also change thevegetableproperty of the childscriptobjectSimple. The result of the last line of the script is"Swiss chard".
Similarly, if a child changes one of its inherited properties, the value in the parent object also changes. For example, thescriptobjectJohnSonin the following script inherits thevegetableproperty fromscriptobjectJohn.

```

script John```

```

    property vegetable : "Spinach"```

```

end script```

```

script JohnSon```

```

    property parent : John```

```

    on changeVegetable()```

```

        set my vegetable to "Zucchini"```

```

    end changeVegetable```

```

end script```

```

tell JohnSon to changeVegetable()```

```

vegetable of John```

```

--result: "Zucchini"```
When you change thevegetableproperty ofscriptobjectJohnSonto"Zucchini"with thechangeVegetablecommand, thevegetableproperty ofscriptobjectJohnalso changes.
The previous example demonstrates an important point about inherited properties: to refer to an inherited property from within a childscriptobject, you must use the reserved wordmyorof meto indicate that the value to which youâre referring is a property of the currentscriptobject. (You can also use the wordsof parentto indicate that the value is a property of the parentscriptobject.) If you donât, AppleScript assumes the value is a local variable.
For example, if you refer tovegetableinstead ofmy vegetablein thechangeVegetablehandler in the previous example, the result is"Spinach". For related information, seeThe it and me Keywords.

### Using the continue Statement in Script Objects

In a childscriptobject, you can define a handler with the same name as a handler defined in its parent object. In implementing the child handler, you have several options:

- The handler in the childscriptobject can be independent of the one in its parent. This allows you to call either handler, as you wish.
The handler in the childscriptobject can be independent of the one in its parent. This allows you to call either handler, as you wish.

- The handler in the child can simply invoke the handler in its parent. This allows the child object to take advantage of the parentâs implementation (as shown in thescriptobjects below that contain aon identifyhandler).
The handler in the child can simply invoke the handler in its parent. This allows the child object to take advantage of the parentâs implementation (as shown in thescriptobjects below that contain aon identifyhandler).

- The handler in the child can invoke the handler in its parent, changing the values passed to it or executing additional statements before or after invoking the parent handler. This allows the child object to modify or add to the behavior of its parent, but still take advantage of the parentâs implementation.
The handler in the child can invoke the handler in its parent, changing the values passed to it or executing additional statements before or after invoking the parent handler. This allows the child object to modify or add to the behavior of its parent, but still take advantage of the parentâs implementation.
Normally, if a childscriptobject and its parent both have handlers for the same command, the child uses its own handler. However, the handler in a childscriptobject can handle a command first, and then use acontinuestatement to call the handler for the same command in the parent.
This handing off of control to another object is calleddelegation. By delegating commands to a parentscriptobject, a child can extend the behavior of a handler contained in the parent without having to repeat the entire handler definition. After the parent handles the command, AppleScript continues at the place in the child where thecontinuestatement was executed.
The syntax for acontinuestatement is shown incontinue.
The following script includes twoscriptobject definitions,ElizabethandChildOfElizabeth.

```

script Elizabeth```

```

    property HowManyTimes : 0```

```

    to sayHello to someone```

```

        set HowManyTimes to HowManyTimes + 1```

```

        return "Hello " & someone```

```

    end sayHello```

```

end script```

```

 ```

```

script ChildOfElizabeth```

```

    property parent : Elizabeth```

```

    on sayHello to someone```

```

        if my HowManyTimes > 3 then```

```

            return "No, I'm tired of saying hello."```

```

        else```

```

            continue sayHello to someone```

```

        end if```

```

    end sayHello```

```

end script```

```

tell Elizabeth to sayHello to "Matt"```

```

--result: "Hello Matt", no matter how often the tell is executed```

```

tell ChildOfElizabeth to sayHello to "Bob"```

```

--result: "Hello Bob", the first four times the tell is executed;```

```

--   after the fourth time: "No, Iâm tired of saying hello."```
In this example, the handler defined byChildOfElizabethfor thesayHellocommand checks the value of theHowManyTimesproperty each time the handler is run. If the value is greater than 3,ChildOfElizabethreturns a message refusing to say hello. Otherwise,ChildOfElizabethcalls thesayHellohandler in the parentscriptobject (Elizabeth), which returns the standard hello message. The wordsomeonein thecontinuestatement is a parameter variable. It indicates that the parameter received with the originalsayHellocommand will be passed to the handler in the parent script.
Note:The reserved wordmyin the statementifmy HowManyTimes > 10in this example is required to indicate thatHowManyTimesis a property of thescriptobject. Without the wordmy, AppleScript assumes thatHowManyTimesis an undefined local variable.
Acontinuestatement can change the parameters of a command before delegating it. For example, suppose the followingscriptobject is defined in the same script as the preceding example. The firstcontinuestatement changes the direct parameter of thesayHellocommand from"Bill"to"William". It does this by specifying the value"William"instead of the parameter variablesomeone.

```

script AnotherChildOfElizabeth```

```

    property parent : Elizabeth```

```

    on sayHello to someone```

```

        if someone = "Bill" then```

```

            continue sayHello to "William"```

```

        else```

```

            continue sayHello to someone```

```

        end if```

```

    end sayHello```

```

end script```

```

 ```

```

tell AnotherChildOfElizabeth to sayHello to "Matt"```

```

--result: "Hello Matt"```

```

 ```

```

tell AnotherChildOfElizabeth to sayHello to "Bill"```

```

--result: "Hello William"```
If you override a parentâs handler in this manner, the reserved wordsmeandmyin the parentâs handler no longer refer to the parent, as demonstrated in the example that follows.

```

script Hugh```

```

    on identify()```

```

        me```

```

    end identify```

```

end script```

```

script Andrea```

```

    property parent : Hugh```

```

    on identify()```

```

        continue identify()```

```

    end identify```

```

end script```

```

 ```

```

tell Hugh to identify()```

```

--result: Â«script HughÂ»```

```

 ```

```

tell Andrea to identify()```

```

--result: Â«script AndreaÂ»```
Copyright © 2016 Apple Inc. All Rights Reserved.Terms of Use|Privacy Policy|  Updated: 2016-01-25