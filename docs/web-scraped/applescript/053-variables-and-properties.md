# Variables and Properties

# Variables and Properties
Variables and properties are introduced in previous chapters in this document. You use them inscriptobjects to store and manipulate values.
Important:In reading this chapter, you should be familiar with the information on implicit and explicitrunhandlers inrun Handlers.
The following sections cover common issues in working with variables and properties, including how to declare them and how AppleScript interprets their scope in a script:
- Defining Properties
Defining Properties
- Declaring Variables
Declaring Variables
- Scope of Variables and Properties
Scope of Variables and Properties

## Defining Properties
Property labels follow the rules described inIdentifiers.
Property definitions use the following syntax:
propertypropertyLabel:expression
An identifier.
An AppleScript expression that sets the initial value for the property. Property definitions are evaluated before variable assignments, so property definitions cannot contain variables.
The following are examples of valid property definitions:
```
property windowCount : 0```
```
property defaultName : "Barry"```
```
property strangeValue : (pi * 7)^2```
After you define a property, you can change its value with thecopyorsetcommand.
The value set by a property definition is not reset each time the script is run; instead, it persists until the script is recompiled.
You cannot declare a property in a handler but a handler can access a property defined in its containingscriptobject.

## Declaring Variables
Variable names follow the rules described inIdentifiers.
To create a variable in AppleScript, you assign it a value using thecopyorsetcommand. For example, the following statements create and initialize two variables, one namedcircumferenceand one namedsavedResult:
```
set circumference to pi * 3.5 --result: 10.995574287564```
```
copy circumference to savedResult --result: 10.995574287564 (copy of 1st variable)```
As shown in this example, a variable assignment can make use of a previously defined variable. It can also make use of properties declared in the samescriptobject.
There are some obvious, and some more subtle, differences in usingcopyandsetto create a variableâseeUsing the copy and set Commandsfor more information.
If you assign a new value to a variable that is already in use, it replaces the old value. You can assign a simple value, an expression, or an object specifierâexpressions are evaluated and object specifiers are resolved to obtain the value to assign. To create a variable whose value is an object specifier itself, rather than the value of the object specified, use thea reference tooperator.
The next two sections describe how you can explicitly define alocalor aglobalvariable. These variable types differ primarily in their scope. Scope, which refers to where a variable is accessible within a script, is described in detail inScope of Variables and Properties.

### Local Variables
You can declare explicitlocalvariables using the following syntax:
localvariableName[,variableName]â¦
An identifier.
The following are examples of validlocalvariable declarations:
```
local windowCount -- defines one variable```
```
local agentName, agentNumber, agentHireDate -- defines three variables```
You cannot assign an initial value to alocalvariable in its declaration, nor can you declare a class for the variable. Instead, you use thecopyorsetcommand to initialize a variable and set its class. For example:
```
set windowCount to 0 -- initialize to zero; an integer```
```
set agentName to "James Smith" -- assign agent name; a text string```
```
set agentNumber to getAgentNumber(agentName) -- call handler; an integer```
```
copy current date to agentHireDate -- call current date command; a date```

### Global Variables
The syntax forglobalvariables is nearly identical to that forlocalvariables:
globalvariableName[,variableName]â¦
An identifier.
The following are examples of validglobalvariable declarations:
```
global gAgentCount```
```
global gStatementDate, gNextAgentNumber```
As withlocalvariables, you use thecopyorsetcommand to initializeglobalvariables and set their class types. For example:
```
set gAgentCount to getCurrentAgentCount() -- call handler to get count```
```
set gStatementDate to current date -- get date from current date command```
```
set gNextAgentNumber to getNextAvailNumber() -- call handler to get number```

### Using the copy and set Commands
As its name implies, when you use thecopycommand to create a variable, it always creates a separate copy (though note that a copy of an object specifier still specifies the same object). However, when you use thesetcommand to create a variable, the new variable always refers to the original object or value. You have essentially created another name for the same object.
When more than one variable refers to a changeable (or mutable) object, a change to the object is observable through any of the variables. The types of AppleScript objects that are mutable aredate,list,record, andscriptobjects.
For objects that cannot be modified (immutable objects), variables created with thesetcommand may seem like copiesâthereâs no way to change the object the variables point to, so they seem independent. This is demonstrated in the example in the next section that creates the variablesmyNameandyourName.

#### Declaring Variables with the set Command
You can use thesetcommand to set a variable to any type of object. If the variable doesnât exist, it is created; if it does exist, its current value is replaced:
```
set numClowns to 5 --result: 5```
```
set myList to { 1, 2, "four" } --result: {1, 2, "four"}```
```
tell application "TextEdit"```
```
    set word1 to word 1 of front document --result: some word```
```
end tell```
The following example uses a mutable object. It creates two variables that refer to the same list, then modifies the list through one of the variables:
```
set myList to { 1, 2, 3 }```
```
set yourList to myList```
```
set item 1 of myList to 4```
After executing these statements, the statementsitem 1 of myListanditem 1 of yourListboth yield4, because both variables refer to the same list.
Now suppose youâre working with an immutable object, such as atextobject:
```
set myName to "Sheila"```
```
set yourName to myName```
Both variables refer to the sametextobject, buttextobjects are not mutable, so there is no way to change the the valuemyNamesuch that it affects the value ofyourName. (If you assign new text to one of the variables, you are just creating a new, separatetextobject.)
Thesetcommand can assign several variables at once using a pattern, which may be a list or record: a list or record of variables on one side, and a list or record of values on the other. Values are matched to variables based on their position for a list, or based on their keys for a record. Not having enough values is an error; if there are too many values, the extra ones are ignored. The order in which the values are evaluated and the variables are assigned is unspecified, but all values are evaluated before any assignments are made.
The Examples section of thesetcommand shows some simple pattern assignments. Here is an example with more complex patterns:
```
set x to {8, 94133, {firstName:"John", lastName:"Chapman"}}```
```
set {p, q, r} to x```
```
(* now p, q, and r have these values:```
```
                p = 8```
```
                q = 94133```
```
                r = {firstName:"John", lastName:"Chapman"}  *)```
```
set {p, q, {lastName:r}} to x```
```
(* now p, q, and r have these values: p = 8```
```
                                      q = 94133```
```
                                      r = "Chapman" *)```
In the final assignment statement above,{lastName:r}is a record that hasnât been used before in the script, and contains an item with labellastNameand valuer(a previously defined variable). The variablexhas previously been set to have a record that has an item with labellastNameand value"Chapman". During the assignment, the value of the item labeledlastNamein the new record is set to the value of the item labeledlastNameinxâhence it now has the value"Chapman".
As this example demonstrates, the properties of a record need not be given in the same order and need not all be used when you set a pattern to a pattern, as long as the patterns match. For details, see thesetcommand.
Note:Using patterns with thesetcommand is similar to using patterned parameters with handlers, which is described inHandlers with Patterned Positional Parameters.

#### Declaring Variables with the copy Command
You can use thecopycommand to set a variable to any type of object. If the variable doesnât exist, it is created; if it does exist, its current value is replaced. Thecopycommand creates a new copy that is independent of the originalâa subsequent change does not change the original value (though note that a copy of an object specifier still specifies the same object).
To copy within an application, you should use the applicationâsduplicatecommand, if it has one. To copy between applications, you can use thegetcommand to obtain information from one application and thesetcommand to set it in another.
Thecopycommand creates a deep copyâthat is, if you copy a nested data structure, such as a list that contains another list, the entire structure is copied, as shown in the following example. This example creates a record (alpha), then a list (beta), then a list that contains the first record and list (gamma), then finally a copy ofgamma(delta). It then changes a property in the original record,alpha. The result shows that the property is changed whereveralphaappears, except in the copy,delta:
```
set alpha to {property1:10, property2:20}```
```
set beta to {1, 2, "Hello"}```
```
set gamma to {alpha, beta, "Goodbye"}```
```
copy gamma to delta```
```
set property1 of alpha to 42```
```
 ```
```
{alpha, beta, gamma, delta}  -- List variables to show contents```
```
(*result: {{property1:42, property2:20}, {1, 2, "Hello"}, {{property1:42, property2:20}, {1, 2, "Hello"}, "Goodbye"}, {{property1:10, property2:20}, {1, 2, "Hello"}, "Goodbye"}} *)```
If you make a copy of areferenceobject, it refers to the same object as the original (because both contain the same object specifier):
```
set windowRef to a reference to window 1 of application "Finder"```
```
name of windowRef --result: "Script testing folder"```
```
copy windowRef to currentWindowRef --result: a new object specifier```
```
name of currentWindowRef --result: "Script testing folder"```

## Scope of Variables and Properties
Thedeclarationof a variable or property identifier is the first valid occurrence of the identifier in ascriptobject. The form and location of the declaration determine how AppleScript treats the identifier in thatscriptobject.
Thescopeis the range over which AppleScript recognizes a declared identifier within ascriptobject. The scope of a variable depends on where you declare it and whether you declare it asglobalorlocal. The scope of a property extends to the entirescriptobject in which it is declared. After declaring a property, you can reuse the same identifier as a separate variable only if you first declare it as alocalvariable.
Lifetimerefers to the period of time over which a variable or property is in existence. Only the values of properties andglobalvariables can persist after a script is run.
In the discussions that follow, declarations and statements in ascriptobject that occur outside of any handlers or nestedscriptobjects are identified asoutside.
The following examples show the four basic forms for declaring variables and properties in AppleScript:
- property x: 3The scope of a property definition is thescriptobject in which it is declared, including any handlers or nestedscriptobjects. A property definition specifies an initial value. You cannot declare a property in a handler.The value set by a property definition is not reset each time the script is run; instead, it persists until the script is recompiled.
property x: 3
The scope of a property definition is thescriptobject in which it is declared, including any handlers or nestedscriptobjects. A property definition specifies an initial value. You cannot declare a property in a handler.
The value set by a property definition is not reset each time the script is run; instead, it persists until the script is recompiled.
- global xThe scope of aglobalvariable can be limited to specific handlers or containedscriptobjects or it can extend throughout a top-levelscriptobject. Aglobaldeclaration doesnât set an initial valueâit must be initialized by acopyorsetcommand before a script can access its value.The value of aglobalvariable is not reset each time a script is run, unless its initialization statement is executed.
global x
The scope of aglobalvariable can be limited to specific handlers or containedscriptobjects or it can extend throughout a top-levelscriptobject. Aglobaldeclaration doesnât set an initial valueâit must be initialized by acopyorsetcommand before a script can access its value.
The value of aglobalvariable is not reset each time a script is run, unless its initialization statement is executed.
- local xThe scope of alocalvariable can be limited to specific handlers or containedscriptobjects or it can extend throughout a top-levelscriptobject. Alocaldeclaration doesnât set an initial valueâit must be initialized by acopyorsetcommand before a script can access its value.The value of alocalvariable is reset each time the handler is run (either therunhandler for the script, or the specific handler in which the variable is declared).
local x
The scope of alocalvariable can be limited to specific handlers or containedscriptobjects or it can extend throughout a top-levelscriptobject. Alocaldeclaration doesnât set an initial valueâit must be initialized by acopyorsetcommand before a script can access its value.
The value of alocalvariable is reset each time the handler is run (either therunhandler for the script, or the specific handler in which the variable is declared).
- set x to 3In the absence of aglobalvariable declaration, the scope of a variable declared with thecopyorsetcommand is normally restricted to therunhandler for the script, making it implicitly local to that run handler. However, a handler or nested script object can declare the same variable with aglobaldeclaration to gain access to it.The value of a variable declared with thecopyorsetcommand is reset each time a script is run.
set x to 3
In the absence of aglobalvariable declaration, the scope of a variable declared with thecopyorsetcommand is normally restricted to therunhandler for the script, making it implicitly local to that run handler. However, a handler or nested script object can declare the same variable with aglobaldeclaration to gain access to it.
The value of a variable declared with thecopyorsetcommand is reset each time a script is run.
If you want to use the same identifier in several different places in a script, you should either declare it as a property or as aglobalvariable.
It is often convenient to limit the scope of a particular identifier to a single handler or nestedscriptobject, which you can do by defining it as alocalvariable in the handler orscriptobject. Outside, the identifier has no value associated with it and can be reused elsewhere in the script. When used this way, alocalvariable is said toshadow(or block access to) aglobalvariable or property with the same name, making the global version inaccessible in the scope of the handler orscriptobject where thelocalvariable is declared.
Note:If you save a script as a script application, then run the application on read-only media, the value of a modified property orglobalvariable is not saved.
The following sections provide additional information about scope:
- Scope of Properties and Variables Declared in a Script Object
Scope of Properties and Variables Declared in a Script Object
- Scope of Variables Declared in a Handler
Scope of Variables Declared in a Handler

### Scope of Properties and Variables Declared in a Script Object
Table 3-1shows the scope and lifetime for variables and properties that are declared at the top level in ascriptobject (outside any handlers or nestedscriptobjects).
Declaration type
Scope (visibility)
Lifetime
property x: 3
Everywhere in script
Reset when script is recompiled
global x
Everywhere in script
Reset when reinitialized in script or when script is recompiled
local x
Withinrunhandler only
Reset when script is run
set x to 3
Withinrunhandler only
Reset when script is run
The scope of a property in ascriptobject extends to any subsequent statements anywhere in the script. Consider the following example:
```
property currentCount : 0```
```
increment()```
```
 ```
```
on increment()```
```
    set currentCount to currentCount + 1```
```
    display dialog "Count is now " & currentCount  & "."```
```
end increment```
When it encounters the identifiercurrentCountanywhere in this script, AppleScript associates it with thecurrentCountproperty.
The value of a property persists after the script in which the property is defined has been run. Thus, the value ofcurrentCountis 0 the first time this script is run, 1 the next time it is run, and so on. The propertyâs current value is saved with thescriptobject and is not reset to 0 until the script is recompiledâthat is, modified and then run again, saved, or checked for syntax.
The value of aglobalvariable also persists after the script in which it is defined has been run. However, depending on how it is initialized, aglobalvariable may be reset each time the script is run again. The next example shows how to initialize aglobalvariable so that it is initialized only the first time a script is run, and thus produces the same result as using a property in the previous example:
```
global currentCount```
```
increment()```
```
 ```
```
on increment()```
```
    try```
```
        set currentCount to currentCount + 1```
```
    on error```
```
        set currentCount to 1```
```
    end try```
```
        display dialog "Count is now " & currentCount  & "."```
```
end increment```
The first time the script is run, the statementset currentCount to currentCount + 1generates an error because theglobalvariablecurrentCounthas not been initialized. When the error occurs, theon errorblock initializescurrentCount. When the script is run again, the variable has already been initialized, so the error branch is not executed, and the variable keeps its previous value. Persistence is accomplished, but not as simply as in the previous example.
If you donât want the value associated with an identifier to persist after a script is run but you want to use the same identifier throughout a script, declare aglobalvariable and use thesetcommand to set its value each time the script is run:
```
global currentCount```
```
set currentCount to 0```
```
on increment()```
```
    set currentCount to currentCount + 1```
```
end increment```
```
 ```
```
increment() --result: 1```
```
increment() --result: 2```
Each time theon incrementhandler is called within the script, theglobalvariablecurrentCountincreases by 1. However, when you run the entire script again,currentCountis reset to 0.
In the absence of aglobalvariable declaration, the scope of a variable declaration using thesetcommand is normally restricted to therunhandler for the script. For example, this script declares two separatecurrentCountvariables:
```
set currentCount to 10```
```
on increment()```
```
    set currentCount to 5```
```
end increment```
```
 ```
```
increment() --result: 5```
```
currentCount --result: 10```
The scope of the firstcurrentCountvariableâs declaration is limited to therunhandler for the script. Because this script has no explicitrunhandler, outside statements are part of its implicitrunhandler, as described inrun Handlers. The scope of the secondcurrentCountdeclaration, within theon incrementhandler, is limited to that handler. AppleScript keeps track of each variable independently.
To associate a variable in a handler with the same variable declared with thesetcommand outside the handler, you can use aglobaldeclaration in the handler, as shown in the next example. (This approach also works to associate a variable in a nestedscriptobject.)
```
set currentCount to 0```
```
on increment()```
```
    global currentCount```
```
    set currentCount to currentCount + 1```
```
end increment```
```
 ```
```
increment() --result: 1```
```
currentCount --result: 1```
To restrict the context of a variable to a scriptâsrunhandler regardless of subsequentglobaldeclarations, you must declare it explicitly as alocalvariable, as shown in this example:
```
local currentCount```
```
set currentCount to 10```
```
on increment()```
```
    global currentCount```
```
    set currentCount to currentCount + 2```
```
end increment```
```
 ```
```
increment() --error: "The variable currentCount is not defined"```
Because thecurrentCountvariable in this example is declared as local to the script, and hence to its implicitrunhandler, any subsequent attempt to declare the same variable asglobalresults in an error.
If you declare an outside variable with thesetcommand and then declare the same identifier as a property, the declaration with thesetcommand overrides the property definition. For example, the following script returns 10, not 5. This occurs because AppleScript evaluates property definitions before it evaluatessetcommand declarations:
```
set numClowns to 10 -- evaluated after property definition```
```
property numClowns: 5 -- evaluated first```
```
numClowns --result: 10```
The next example, shows how to use aglobalvariable declaration in ascriptobject to associate aglobalvariable with an outside property:
```
property currentCount : 0```
```
script Paula```
```
    property currentCount : 20```
```
    script Joe```
```
        global currentCount```
```
        on increment()```
```
            set currentCount to currentCount + 1```
```
            return currentCount```
```
        end increment```
```
    end script```
```
    tell Joe to increment()```
```
end script```
```
run Paula --result: 1```
```
run Paula --result: 2```
```
currentCount --result: 2```
```
currentCount of Paula --result: 20```
This script declares two separatecurrentCountproperties: one outside any handlers (andscriptobjects) in the main script and one in thescriptobjectPaulabut outside of any handlers orscriptobjects withinPaula. Because the scriptJoedeclares theglobalvariablecurrentCount, AppleScript looks forcurrentCountat the top level of the script, thus treating JoeâscurrentCountandcurrentCountat the top level of the script as the same variable.

### Scope of Variables Declared in a Handler
A handler canât declare a property, although it can refer to a property that is declared outside any handler in thescriptobject. (A handler can contain script objects, but it canât contain another handler, except in a contained script object.)
Table 3-2summarizes the scope of variables declared in a handler. Examples of each form of declaration follow.
Declaration type
Scope (visibility)
Lifetime
global x
Within handler only
Reset when script is recompiled; if initialized in handler, then reset when handler is run
local x
Within handler only
Reset when handler is run
set x to 3
Within handler only
Reset when handler is run
The scope of aglobalvariable declared in a handler is limited to that handler, although AppleScript looks beyond the handler when it tries to locate an earlier occurrence of the same variable. Hereâs an example:
```
set currentCount to 10```
```
on increment()```
```
    global currentCount```
```
    set currentCount to currentCount + 2```
```
end increment```
```
 ```
```
increment() --result: 12```
```
currentCount --result: 12```
When AppleScript encounters thecurrentCountvariable within theon incrementhandler, it doesnât restrict its search for a previous occurrence to that handler but keeps looking until it finds the declaration outside any handler. However, the use ofcurrentCountin any subsequent handler in the script is local to that handler unless the handler also explicitly declarescurrentCountas aglobalvariable.
The scope of alocalvariable declaration in a handler is limited to that handler, even if the same identifier has been declared as a property outside the handler:
```
property currentCount : 10```
```
on increment()```
```
    local currentCount```
```
    set currentCount to 5```
```
end increment```
```
 ```
```
increment() --result: 5```
```
currentCount --result: 10```
The scope of a variable declaration using thesetcommand in a handler is limited to that handler:
```
script Henry```
```
    set currentCount to 10 -- implicit local variable in script object```
```
    on increment()```
```
        set currentCount to 5-- implicit local variable in handler```
```
    end increment```
```
    return currentCount```
```
end script```
```
 ```
```
tell Henry to increment() --result: 5```
```
run Henry --result: 10```
The scope of the first declaration of the firstcurrentCountvariable in thescriptobjectHenryis limited to therunhandler for thescriptobject (in this case, an implicitrunhandler, consisting of the last two statements in the script). The scope of the secondcurrentCountdeclaration, within theon incrementhandler, is limited to that handler. The two instances ofcurrentCountare independent variables.
Copyright © 2016 Apple Inc. All Rights Reserved.Terms of Use|Privacy Policy|  Updated: 2016-01-25