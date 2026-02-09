# About Handlers

When script developers want to factor and re-use their code, they can turn to handlers. A handler is a collection of statements that can be invoked by name. Handlers are also known as functions, subroutines, or methods.
This chapter describes how to work with handlers, in the following sections:

- Handler Basics
Handler Basics

- Handlers in Script Applications
Handlers in Script Applications
For detailed reference information, seeHandler Reference.

## Handler Basics

Ahandleris a collection of statements that can be invoked by name. Handlers are useful in scripts that perform the same action in more than one place. You can package statements that perform a specific task as a handler, give it a descriptive name, and call it from anywhere in the script. This makes the script shorter and easier to maintain.
A script can contain one or more handlers. However, you can not nest a handler definition within another handler (although a script object defined in a handler can contain other handlers).
The definition for a handler specifies the parameters it uses, if any, and may specify a class or classes for the parameter and a default value.
When you call a handler, you must list its parameters according to how they are specified in its definition. Handlers may have labeled, positional, or interleaved parameters, described in subsequent sections. If a parameter has a specified class, AppleScript will coerce the actual value to that class as if using theasoperator. If a parameter has a default value, that parameter may be omitted.
A handler definition can contain variable declarations and statements. It may use areturnstatement (described in detail inreturn) to return a value and exit the handler.
The sections that follow provide additional information on working with handlers:

- Defining a Simple Handler
Defining a Simple Handler

- Handlers with Labeled Parameters
Handlers with Labeled Parameters

- Handlers with Positional Parameters
Handlers with Positional Parameters

- Handlers with Patterned Positional Parameters
Handlers with Patterned Positional Parameters

- Recursive Handlers
Recursive Handlers

- Errors in Handlers
Errors in Handlers

- Passing by Reference Versus Passing by Value
Passing by Reference Versus Passing by Value

- Calling Handlers in a tell Statement
Calling Handlers in a tell Statement

### Defining a Simple Handler

The following is a definition for a simple handler that takes any parameter value that can be displayed as text (presumably one representing a date) and displays it in a dialog box. The handler name isrock; its parameter isaround the clock, wherearoundis a parameter label andclockis the parameter name (theis an AppleScript filler for readability):

```

on rock around the clock```

```

    display dialog (clock as text)```

```

end rock```
This handler allows an English-like calling statement:

```

rock around the current date -- call handler to display current date```
A handler can have no parameters. To indicate that a handler has no parameters, you include a pair of empty parentheses after the handler name in both the handler definition and the handler call. For example, the followinghelloWorldscript has no parameters.

```

on helloWorld()```

```

    display dialog "Hello World"```

```

end```

```

 ```

```

helloWorld() -- Call the handler```

### Handlers with Labeled Parameters

To define a handler with labeled parameters, you list the labels to use when calling the handler and the statements to be executed when it is called. (The syntax is shown inHandler Syntax (Labeled Parameters).)
Handlers with labeled parameters can also have a direct parameter. With the exception of the direct parameter, which must directly follow the handler name, labeled parameters can appear in any order, with the labels from the handler definition identifying the parameter values. This includes parameters listed ingiven,with, andwithoutclauses (of which there can be any number).
ThefindNumbershandler in the following example uses the special labelgivento define a parameter with the labelgiven rounding.

```

to findNumbers of numberList above minLimit given rounding:roundBoolean```

```

        set resultList to {}```

```

        repeat with i from 1 to (count items of numberList)```

```

            set x to item i of numberList```

```

            if roundBoolean then -- round the number```

```

                -- Use copy so original list isnât modified.```

```

                copy (round x) to x```

```

            end if```

```

            if x > minLimit then```

```

                set end of resultList to x```

```

            end if```

```

        end repeat```

```

        return resultList```

```

end findNumbers```
The next statements show how to callfindNumbersby passing a predefinedlistvariable:

```

set myList to {2, 5, 19.75, 99, 1}```

```

findNumbers of myList above 19 given rounding:true```

```

    --result: {20, 99}```

```

findNumbers of myList above 19 given rounding:false```

```

    --result: {19.75, 99}```
You can also specify the value of theroundingparameter by using awithorwithoutclause to indicatetrueorfalse. (In fact, when you compile the previous examples, AppleScript automatically convertsgiven rounding:truetowith roundingandgiven rounding:falsetowithout rounding.) These examples pass alistobject directly, rather than using alistvariable as in the previous case:

```

findNumbers of {5.1, 20.1, 20.5, 33} above 20 with rounding```

```

    --result: {33}```

```

 ```

```

findNumbers of {5.1, 20.1, 20.5, 33.7} above 20 without rounding```

```

    --result: {20.1, 20.5, 33.7}```
Here is another handler that uses parameter labels:

```

to check for yourNumber from startRange thru endRange```

```

    if startRange â¤ yourNumber and yourNumber â¤ endRange then```

```

        display dialog "Congratulations! Your number is included."```

```

    end if```

```

end check```
The following statement calls the handler, causing it to display the"Congratulations!"message

```

check for 8 from 7 thru 10 -- call the handler```

### Handlers with Positional Parameters

The definition for a handler with positional parameters shows the order in which to list parameters when calling the handler and the statements to be executed when the handler is called. The definition must include parentheses, even if it doesnât include any parameters. The syntax is shown inHandler Syntax (Positional Parameters).
In the following example, theminimumValueroutine returns the smaller of two values:

```

on minimumValue(x, y)```

```

    if x < y then```

```

        return x```

```

    else```

```

        return y```

```

    end if```

```

end minimumValue```

```

 ```

```

-- To call minimumValue:```

```

minimumValue(5, 105) --result: 5```
The first line of theminimumValuehandler specifies the parameters of the handler. To call a handler with positional parameters you list the parameters in the same order as they are specified in the handler definition.
If a handler call is part of an expression, AppleScript uses the value returned by the handler to evaluate the expression. For example, to evaluate the following expression, AppleScript first callsminimumValue, then evaluates the rest of the expression.

```

minimumValue(5, 105) + 50 --result: 55```

### Handlers with Patterned Positional Parameters

You can create a handler whose positional parameters define a pattern to match when calling the handler. For example, the following handler takes a single parameter whose pattern consists of two items in a list:

```

on displayPoint({x, y})```

```

    display dialog ("x = " & x & ", y = " & y)```

```

end displayPoint```

```

 ```

```

-- Calling the handler:```

```

set testPoint to {3, 8}```

```

displayPoint(testPoint)```
A parameter pattern can be much more complex than a single list. The handler in the next example takes two numbers and a record whose properties include a list of bounds. The handler displays a dialog box summarizing some of the passed information.

```

on hello(a, b, {length:l, bounds:{x, y, w, h}, name:n})```

```

    set q to a + b```

```

 ```

```

    set response to "Hello " & n & ", you  are " & l & Â¬```

```

        " inches tall and occupy position (" & x &  ", " & y & ")."```

```

 ```

```

    display dialog response```

```

 ```

```

end hello```

```

 ```

```

set thing to {bounds:{1, 2, 4, 5}, name:"George", length:72}```

```

hello (2, 3, thing)```

```

--result: A dialog displaying âHello George, you are 72 inches  tall```

```

--          and occupy position (1,2).â```
The properties of a record passed to a handler with patterned parameters donât have to be given in the same order in which they are given in the handlerâs definition, as long as all the properties required to fit the pattern are present.
The following call tominimumValueuses the value from a handler call tomaximumValueas its second parameter. ThemaximumValuehandler (not shown) returns the larger of two passed numeric values.

```

minimumValue(20, maximumValue(1, 313)) --result: 20```

### Handlers with Interleaved Parameters

A handler with interleaved parameters is a special case of one with positional parameters. The definition shows the order in which to list parameters when calling the handler and the statements to be executed when the handler is called, but the name of the handler is broken into pieces and interleaved with the parameters, which can make it easier to read.  Handlers with interleaved parameters may be used in any script, but are especially useful with bridged Objective-C methods, since they naturally resemble Objective-C syntax. The syntax is shown inHandler Syntax (Interleaved Parameters).
A handler with interleaved parameters may have only one parameter, as in this example:

```

on areaOfCircleWithRadius:radius```

```

    return radius ^ 2 * pi```

```

end areaOfCircleWithRadius:```
Or more than one, as in this example:

```

on areaOfRectangleWithWidth:w height:h```

```

    return w * h```

```

end areaOfRectangleWithWidth:height:```
To call a handler with interleaved parameters, list the parameters in the same order as they are specified in the handler definition. Despite the resemblance to labeled parameters, the parameters may not be reordered. Also, the call must be explicitly sent to an object, even if the target object is the default,it. For example:

```

its foo:5 bar:105 --this works```

```

tell it to foo:5 bar:105 --as does this```

```

foo:5 bar:105 --syntax error.```
Note:The actual name of an interleaved-parameter handler is all the name parts strung together with underscores, and is equivalent to a handler defined using that name with positional parameters. For example, these two handler declarations are equivalent:
on tableView:t objectValueForTableColumn:c row:ron tableView_objectValueForTableColumn_row_(t, c, r)Given a compiled script, AppleScript will automatically translate between the two forms depending on whether or not the current system version supports interleaved parameters.

```

on tableView:t objectValueForTableColumn:c row:r```

```

on tableView_objectValueForTableColumn_row_(t, c, r)```

### Parameter Specifications

Note:Parameter specifications are supported in OS X Yosemite v10.10 and later.
The parameter ânameâ in a handler definition may be a simple name, as shown above, or it may additionally specify a required class and, for labeled parameters, a default value. To specify a required class, follow the name withasclassoras {class,â¦}. For example, you could declare a parameter to be specifically an integer like this:

```

on factorial(x as integer)```
The effect is as if the handler began withset x to x as integer; if coercing the actual value to an integer fails, AppleScript throws an appropriate error, which may be caught with atryblock. The class may be a list of classes, as described inOperators Reference.
Labeled parameters may be declared with a default value by following the formal parameter name with:literal. Doing so makes the parameter optional when called. For example, this declares amakehandler with a default value for thewith dataparameter:

```

on make new theClass with data theData : missing value```
This handler can now be called without supplying awith dataparameter; the handler would seetheDataset to the specified defaultmissing value, which it could then test for and handle appropriately.
A parameter may use both a type specification and a default value. For example, this declares amakehandler with awith propertiesparameter that must be a record and has a default value of an empty record:

```

on make new theClass with properties theProperties as record : {}```

### Recursive Handlers

Arecursive handleris a handler that calls itself. For example, this recursive handler generates a factorial. (The factorial of a number is the product of all the positive integers from 1 to that number. For example, 4 factorial is equal to 1 * 2 * 3 * 4, or 24. The factorial of 0 is 1.)

```

on factorial(x)```

```

    if x > 0 then```

```

        return x * factorial(x - 1)```

```

    else```

```

        return 1```

```

    end if```

```

end factorial```

```

 ```

```

-- To call factorial:```

```

factorial(10)   --result: 3628800```
In the example above, the handlerfactorialis called once, passing the value10. The handler then calls itself recursively with a value ofx - 1, or9. Each time the handler calls itself, it makes another recursive call, until the value ofxis0. Whenxis equal to0, AppleScript skips to theelseclause and finishes executing all the partially executed handlers, including the originalfactorialcall.
When you call a recursive handler, AppleScript keeps track of the variables and pending statements in the original (partially executed) handler until the recursive handler has completed. Because each call uses some memory, the maximum number of pending handlers is limited by the available memory. As a result, a recursive handler may generate an error before the recursive calls complete.
In addition, a recursive handler may not be the most efficient solution to a problem. For example, the factorial handler shown above can be rewritten to use arepeatstatement instead of a recursive call, as shown in the example inrepeat with loopVariable (from startValue to stopValue).

### Errors in Handlers

As with any AppleScript statements that may encounter an error, you can use atrystatement to deal with possible errors in a handler. Atrystatement includes two collections of statements: one to be executed in the general case, and a second to be executed only if an error occurs.
By using one or moretrystatements with a handler, you can combine the advantages of reuse and error handling in one package. For a detailed example that demonstrates this approach, seeWorking with Errors.

### Passing by Reference Versus Passing by Value

Within a handler, each parameter is like a variable, providing access to passed information. AppleScript passes all parameters by reference, which means that a passed variable is shared between the handler and the caller, as if the handler had created a variable using thesetcommand. However, it is important to remember a point raised inUsing the copy and set Commands: only mutable objects can actually be changed.
As a result, a parameterâs class type determines whether information is effectively passed by value or by reference:

- For mutable objects (those whose class isdate,list,record, orscript), information is passedby reference:If a handler changes the value of a parameter of this type, the original object is changed.
For mutable objects (those whose class isdate,list,record, orscript), information is passedby reference:
If a handler changes the value of a parameter of this type, the original object is changed.

- For all other class types, information is effectively passedby value:Although AppleScript passes a reference to the original object, that object cannot be changed. If the handler assigns a new value to a parameter of this type, the original object is unchanged.
For all other class types, information is effectively passedby value:
Although AppleScript passes a reference to the original object, that object cannot be changed. If the handler assigns a new value to a parameter of this type, the original object is unchanged.
If youwantto pass by reference with a class type other thandate,list,record, orscript, you can pass areferenceobject that refers to the object in question. Although the handler will have access only to a copy of thereferenceobject, the specified object will be the same. Changes to the specified object in the handler will change the original object, although changes to thereferenceobject itself will not.

### Calling Handlers in a tell Statement

To call a handler from within atellstatement, you must use the reserved wordsof meormyto indicate that the handler is part of the script and not a command that should be sent to the target of thetellstatement.
For example, the following script calls theminimumValuehandler defined inHandlers with Positional Parametersfrom within atellstatement. If this call did not include the wordsof me, it would cause an error, because AppleScript would send theminimumValuecommand to TextEdit, which does not understand that message.

```

tell front document of application "TextEdit"```

```

    minimumValue(12, 400) of me```

```

    set paragraph 1 to result as text```

```

end tell```

```

--result: The handler call is successful.```
Instead of using the wordsof me, you could insert the wordmybefore the handler call:

```

my minimumValue(12, 400)```

## Handlers in Script Applications

Ascript applicationis an application whose only function is to run the script associated with it. Script applications contain handlers that allow them to respond to commands. For example, many script applications can respond to theruncommand and theopencommand. A script application receives aruncommand whenever it is launched and anopencommand whenever another icon is dropped on its icon in the Finder. It can also contain other handlers to respond to commands such asquitorprint.
When saving a script in Script Editor, you can create a script application by choosing either Application or Application Bundle from the File Format options. Saving as Application results in a simple format that is compatible with Mac OS 9.Saving as Application Bundle results in an application that uses the modern bundle format, with its specified directory structure, which is supported back to OS X v10.3.
When creating a script application, you can also specify whether astartup screen should appear before the application runs its script. Whatever you write in the Description pane of the script window in Script Editor is displayed in the startup screen.You can also specify in Script Editor whether a script application should stay open after running. The default is for the script to quit immediately after it is run.
You can run a script application from the Finder much like any other application. If it has a startup screen, the user must click the Run button or press the Return key before the script actually runs.
Consider the following simple script

```

tell application "Finder"```

```

    close front window```

```

end tell```
What this script does as a script application depends on what you specify when you save it. If you donât specify a startup screen or tell it to stay open, it will automatically execute once, closing the front Finder window, and then quit.
If a script application modifies the value of a property, the changed value persists across launches of the application. For related information, seeScope of Variables and Properties.
For information about some common script application handlers, see the following sections:

- run Handlers
run Handlers

- open Handlers
open Handlers

- idle and quit Handlers for Stay-Open Applications
idle and quit Handlers for Stay-Open Applications
SeeHandler Referencefor syntax information.

### run Handlers

When you run a script or launch a script application, itsrunhandler is invoked. A scriptâsrunhandler is defined in one of two ways:

- As an implicitrunhandler, which consists of all statements declared outside any handler or nestedscriptobject in a script.Declarations for properties andglobalvariables are not considered statements in this contextâthat is, they are not considered to be part of an implicitrunhandler.
As an implicitrunhandler, which consists of all statements declared outside any handler or nestedscriptobject in a script.
Declarations for properties andglobalvariables are not considered statements in this contextâthat is, they are not considered to be part of an implicitrunhandler.

- As an explicitrunhandler, which is enclosed withinon runandendstatements, similar to other handlers.
As an explicitrunhandler, which is enclosed withinon runandendstatements, similar to other handlers.
Having both an implicit and an explicitrunhandler is not allowed, and causes a syntax error during compilation. If a script has no run handler (for example, a script that serves as a library of handlers, as described inParameter Specifications), executing the script does nothing. However, sending it an explicitruncommand causes an error.
The following script demonstrates an implicitrunhandler. The script consists of a statement that invokes thesayHellohandler, and the definition for the handler itself:

```

sayHello()```

```

 ```

```

on sayHello()```

```

    display dialog "Hello"```

```

end sayHello```
The implicitrunhandler for this script consists of the statementsayHello(), which is the only statement outside the handler. If you save this script as a script application and then run the application, the script receives aruncommand, which causes it to execute the one statement in the implicitrunhandler.
You can rewrite the previous script to provide the exact same behavior with an explicitrunhandler:

```

on run```

```

    sayHello()```

```

end run```

```

 ```

```

on sayHello()```

```

    display dialog "Hello"```

```

end sayHello```
Whether a script is saved as a script application or as a compiled script, itsrunhandler is invoked when the script is run. You can also invoke arunhandler in a script application from another script. For information about how to do this, seeCalling a Script Application From a Script.

### open Handlers

Mac apps, including script applications, receive anopencommand whenever the user drops file, folder, or disk icons on the applicationâs Finder icon, even if the application is already running.
If the script in a script application includes anopenhandler, the handler is executed when the application receives theopencommand. Theopenhandler takes a single parameter which provides a list of all the items to be opened. Each item in the list is analiasobject.
For example, the followingopenhandler makes a list of the pathnames of all items dropped on the script applicationâs icon and saves them in the frontmost TextEdit document:

```

on open names```

```

    set pathNamesString to "" -- Start with empty text string.```

```

    repeat with i in names```

```

        -- In this loop, you can perform operations on each dropped item.```

```

        -- For now, just get the name and append a return character.```

```

        set iPath to (i as text)```

```

        set pathNamesString to pathNamesString & iPath & return```

```

    end repeat```

```

    -- Store list in open document, to verify what was dropped.```

```

    tell application "TextEdit"```

```

        set paragraph 1 of front document to pathNamesString```

```

    end tell```

```

    return```

```

end open```
Files, folders, or disks are not moved, copied, or affected in any way by merely dropping them on a script application. However, the script applicationâs handler can tell Finder to move, copy, or otherwise manipulate the items. For examples that work with Finder items, seeFolder Actions Reference.
You can also run anopenhandler by sending a script application theopencommand. For details, seeCalling a Script Application From a Script.

### idle and quit Handlers for Stay-Open Applications

By default, a script application that receives arunoropencommand handles that single command and then quits. In contrast, a stay-open script application (one saved as Stay Open in Script Editor) stays open after it is launched.
A stay-open script application can be useful for several reasons:

- Stay-open script applications can receive and handle other commands in addition torunandopen. This allows you to use a script application as a script server that, when it is running, provides a collection of handlers that can be invoked by any other script.
Stay-open script applications can receive and handle other commands in addition torunandopen. This allows you to use a script application as a script server that, when it is running, provides a collection of handlers that can be invoked by any other script.

- Stay-open script applications can perform periodic actions, even in the background, as long as the script application is running.
Stay-open script applications can perform periodic actions, even in the background, as long as the script application is running.
Two particular handlers that stay-open script applications often provide are anidlehandler and aquithandler.

#### idle Handlers

If a stay-open script application includes anidlehandler, AppleScript sends the script application periodicidlecommandsâby default, every 30 secondsâallowing it to perform background tasks when it is not performing other actions.
If anidlehandler returns a positive number, that number becomes the rate (in seconds) at which the handler is called. If the handler returns a non-numeric value, the rate is not changed. You can return 0 to maintain the default delay of 30 seconds.
For example, when saved as a stay-open application, the following script beeps every 5 seconds:

```

on idle```

```

    beep```

```

    return 5```

```

end idle```
The result returned from a handler is just the result of the last statement, even if it doesnât include the wordreturnexplicitly. (Seereturnfor more information.) For example, this handler gets called once a minute, because the value of the last statement is 60:

```

on idle```

```

    set x to 10```

```

    beep```

```

    set x to x * 6  -- The handler returns the result (60).```

```

end idle```

#### quit Handlers

AppleScript sends a stay-open script application aquitcommand whenever the user chooses the Quit menu command or presses Command-Q while the application is active. If the script includes aquithandler, the statements in the handler are run before the application quits.
Aquithandler can be used to set script properties, tell another application to do something, display a dialog box, or perform almost any other task. If the handler includes acontinue quitstatement, the script applicationâs default quit behavior is invoked and it quits. If thequithandler returns before it encounters acontinue quitstatement, the application doesnât quit.
Note:Thecontinuestatement passes control back to the applicationâs defaultquithandler. For more information, seecontinue.
For example, this handler checks with the user before allowing the application to quit:

```

on quit```

```

    display dialog "Really quit?" Â¬```

```

        buttons {"No", "Quit"} default button  "Quit"```

```

    if the button returned of the result is "Quit" then```

```

        continue quit```

```

    end if```

```

    -- Without the continue statement, the application doesn't quit.```

```

end quit```
Warning:If AppleScript doesnât encounter acontinue quitstatement while executing anon quithandler, it may seem to be impossible to quit the application. For example, if the handler shown above gets an error before thecontinue quitstatement, the application wonât quit. If necessary, you can use Force Quit (Command-Option-Esc) to halt the application.

## Calling a Script Application From a Script

A script can send commands to a script application just as it can to other applications. To launch a non-stay-open application and run its script, use alaunchcommand followed by aruncommand, like this:

```

launch application "NonStayOpen"```

```

run application "NonStayOpen"```
Thelaunchcommand launches the script application without sending it an implicitruncommand. When theruncommand is sent to the script application, it processes the command, sends back a reply if necessary, and quits.
Similarly, to launch a non-stay-open application and run itsstringTesthandler (which takes atextobject as a parameter), use alaunchcommand followed by astringTestcommand, like this:

```

tell application "NonStayOpen"```

```

    launch```

```

    stringTest("Some example text.")```

```

end tell```
For information on how to create script applications, seeHandlers in Script Applications.
Copyright © 2016 Apple Inc. All Rights Reserved.Terms of Use|Privacy Policy|  Updated: 2016-01-25