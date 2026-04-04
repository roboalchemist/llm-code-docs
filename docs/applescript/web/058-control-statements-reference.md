# Control Statements Reference

This chapter describes AppleScript control statements. Acontrol statementis a statement that determines when and how other statements are executed or how expressions are evaluated. For example, a control statement may cause AppleScript to skip or repeat certain statements.
Simple statementscan be written on one line, whilecompound statementscan contain other statements, including multiple clauses with nested and multi-line statements. A compound statement is known as astatement block.
Compound statements begin with one or more reserved words, such astell, that identify the type of control statement. The last line of a compound statement always starts withend, and can optionally include the word that begins the control statement (such asend tell).

### considering and ignoring Statements

Theconsideringandignoringstatements cause AppleScript to consider or ignore specific characteristics as it executes groups of statements. There are two kinds ofconsideringandignoringstatements:

- Those that specify attributes to be considered or ignored in performing text comparisons.
Those that specify attributes to be considered or ignored in performing text comparisons.

- Those that specify whether AppleScript should consider or ignore responses from an application.
Those that specify whether AppleScript should consider or ignore responses from an application.
Specify how AppleScript should treats attributes, such as case, in performing text comparisons.

##### Syntax

```

considering attribute [, attribute ... and attribute ] Â¬
Â Â Â [ but ignoring attribute [, attribute ... and attribute ] ]
Â Â Â Â Â Â [ statement ]...
end considering
ignoring attribute [, attribute ... and attribute ] Â¬
Â Â Â [ but considering attribute [, attribute ... and attribute ] ]
Â Â Â Â Â Â [ statement ]...
end ignoring```

##### Placeholders

A characteristic of the text:
If this attribute is ignored, uppercase letters are not distinguished from lowercase letters. See Special Considerations below for related information. See alsogreater than, less thanfor a description of how AppleScript sorts letters, punctuation, and other symbols.
If this attribute is ignored,textobjects are compared as if no diacritical marks (such as Â´, `, Ë, Â¨, and Ë) are present; for example,"rÃ©sumÃ©"is equal to"resume".
If this attribute is ignored,textobjects are compared as if no hyphens are present; for example"anti-war"is equal to"antiwar".
By default, this attribute is ignored, and text strings are compared according to their character values. For example, if this attribute is considered,"1.10.1" > "1.9.4"evaluates astrue; otherwise it evaluates asfalse. This can be useful in comparing version strings.
If this attribute is ignored,textobjects are compared as if no punctuation marks (such as. , ? : ; ! ' ") are present; for example"What? he inquired."is equal to"what he inquired".
If this attribute is ignored, thetextobjects are compared as if spaces, tab characters, and return characters were not present; for example"Brick house"would be considered equal to"Brickhouse".
Any AppleScript statement.

##### Examples

The following examples show howconsideringandignoringstatements for various attributes can change the value of text comparisons.

```

"Hello Bob" = "HelloBob" --result: false```

```

ignoring white space```

```

    "Hello Bob" = "HelloBob" --result: true```

```

end ignoring```

```

 ```

```

"BOB" = "bob" --result: true```

```

considering case```

```

    "BOB" = "bob" --result: false```

```

end considering```

```

 ```

```

"a" = "Ã¡" --result: false```

```

ignoring diacriticals```

```

    "a" = "Ã¡" --result: true```

```

end considering```

```

 ```

```

"Babs" = "bÃ¡bs" --result: false```

```

 ```

```

ignoring case```

```

    "Babs" = "bÃ¡bs" --result: false```

```

end ignoring```

```

 ```

```

ignoring case and diacriticals```

```

    "Babs" = "bÃ¡bs" --result: true```

```

end ignoring```

##### Discussion

You can nestconsideringandignoringstatements. If the same attribute appears in both an outer and inner statement, the attribute specified in the inner statement takes precedence.When attributes in an innerconsideringorignoringstatement are different from those in outer statements, they are added to the attributes to be considered and ignored.

##### Special Considerations

Becausetext item delimiters(described inversion) respectconsideringandignoringattributes in AppleScript 2.0, delimiters are case-insensitive by default. Formerly, they were always case-sensitive. To enforce the previous behavior, add an explicitconsidering casestatement.
consideringandignoringare fully Unicode-aware. For example, withignoring case, âÐÐ¾ÑÐ±Ð°Ñâ is equal to âÐÐÐ ÐÐÐ§â. Also, the characters ignored by diacriticals, hyphens, punctuation, and white space are defined by Unicode character classes:

- ignoring punctuationignores category P*, which includes left- and right-quotation marks such asâ â Â« Â».
ignoring punctuationignores category P*, which includes left- and right-quotation marks such asâ â Â« Â».

- ignoring hyphensignores category Pd, which includes em- and en-dashes.
ignoring hyphensignores category Pd, which includes em- and en-dashes.

- ignoring whitespaceignores category Z*, plus tab (\t), return (\r), and linefeed (\n), which includes em-, en-, and non-breaking spaces.
ignoring whitespaceignores category Z*, plus tab (\t), return (\r), and linefeed (\n), which includes em-, en-, and non-breaking spaces.
Para
Permits a script to continue without waiting for an application to respond to commands that target it.

##### Syntax

```

considering | ignoring  application responsesÂ Â Â [ statement ]...end [ considering | ignoring ]```

##### Placeholders

Any AppleScript statement.

##### Examples

The following example shows how to use an ignoring statement so that a script neednât wait while Finder is performing a potentially lengthy task:

```

tell application "Finder"```

```

    ignoring application responses```

```

        empty the trash```

```

    end ignoring```

```

end tell```
Your script may want to ignore most responses from an application, but wait for a response to a particular statement. You can do so by nestingconsideringandignoringstatements:

```

tell application "Finder"```

```

    ignoring application responses```

```

        empty the trash```

```

        -- other statements that ignore application responses```

```

        considering application responses```

```

            set itemName to name of first item of startup disk```

```

        end considering```

```

        -- other statements that ignore application responses```

```

    end ignoring```

```

end tell```

##### Discussion

A response to an application command indicates whether the command completed successfully, and also returns results and error messages, if there are any. When you use anignoring application responsesblock, you forego this information.
Results and error messages from AppleScript commands, scripting additions, and expressions are not affected by theapplication responsesattribute.

### error Statements

During script execution, errors can occur in the operating system (for example, when a specified file isnât found), in an application (for example, when the script specifies an object that doesnât exist), and in the script itself. Anerror messageis a message that is supplied by an application, AppleScript, or macOS when an error occurs during the handling of a command. An error message can include anerror number, which is an integer that identifies the error; anerror expression, which is an expression, usually atextobject, that describes the error; and other information.
A script can signal an errorâwhich can then be handled by an error handlerâwith theerrorstatement. This allows scripts to supply their own messages for errors that occur within the script. For example, a script can prepare to handle anticipated errors by using atrystatement. In theon errorbranch of atrystatement, a script may be able to recover gracefully from the error. If not, it can use anerrorstatement to resignal the error message it receives, modifying the message as needed to supply information specific to the script.
Signals an error in a script.

##### Syntax

```

error [ errorMessage ] [ number errorNumber ] Â¬Â Â Â [ partial resultresultList ] Â¬Â Â Â [ from offendingObject ] [ to expectedType ]```

##### Placeholders

Atextobject describing the error. Although this parameter is optional, you should provide descriptions for errors wherever possible. If you do not include an error description, an emptytextobject ("") is passed to the error handler.
The error number for the error. This is an optional parameter. If you do not include a number parameter, the value -2700 (unknown error) is passed to the error handler.
If the error you are signaling is a close match for one that already has an AppleScript error constant, you can use that constant. If you need to create a new number for the error, avoid using one that conflicts with error numbers defined by AppleScript, macOS, and the Apple Event Manager. In general, you should use positive numbers from 500 to 10,000. For more information, seeError Numbers and Error Messages.
A list of objects. Applies only to commands that return results for multiple objects. If results for some, but not all, of the objects specified in the command are available, you can include them in the partial result parameter. This is rarely supported by applications.
A reference to the object, if any, that caused the error.
A class. If a parameter specified in the command was not of the expected class, and AppleScript was unable to coerce it to the expected class, then you can include the expected class in thetoparameter.

##### Examples

The following example uses atrystatement to handle a simple error, and demonstrates how you can use anerrorstatement to catch an error, then resignal the error exactly as it was received, causing AppleScript to display an error dialog (and halt execution):

```

try```

```

    word 5 of "one two three"```

```

on error eStr number eNum partial result rList from badObj to expectedType```

```

    -- statements that take action based on the error```

```

    display dialog "Doing some preliminary handling..."```

```

    -- then resignal the error```

```

    error eStr number eNum partial result rList from badObj to expectedType```

```

end try```
In the next example, anerrorstatement resignals an error, but omits any original error information and supplies its own message to appear in the error dialog:

```

try```

```

    word 5 of "one two three"```

```

on error```

```

    -- statements to execute in case of error```

```

    error "There are not enough words."```

```

end try```
For more comprehensive examples, seeWorking with Errors.

### if Statements

Anifstatement allows you to define statements or groups of statements that are executed only in specific circumstances, based on the evaluation of one or more Boolean expressions.
Anifstatement is also called a conditional statement. Boolean expressions inifstatements are also called tests.
Executes a statement if a Boolean expression evaluates totrue.

##### Syntax

```

if boolean then statement ```

##### Placeholders

A Boolean expression.
Any AppleScript statement.

##### Examples

This script displays a dialog if the value of the Boolean expressionageOfCat > 1istrue. (The variableageOfCatis set previously.)

```

if ageOfCat > 1 then display dialog "This is not a kitten."```
Executes a group (or groups) of statements if a Boolean expression (or expressions) evaluates totrue.

##### Syntax

```

if boolean [ then ]   [ statement ]...
[else if boolean [ then ]   [ statement ]...]...
[else   [ statement ]...]
end [ if ]```

##### Placeholders

A Boolean expression.
Any AppleScript statement.

##### Examples

The following example uses a compoundifstatement, with a finalelseclause, to display a statement based on the current temperature (obtained separately):

```

if currentTemp < 60 then```

```

    set response to "It's a little chilly today."```

```

else if currentTemp > 80 then```

```

    set response to "It's getting hotter today."```

```

else```

```

    set response to "It's a nice day today."```

```

end if```

```

display dialog response```

##### Discussion

Anifstatement can contain any number ofelse ifclauses; AppleScript looks for the first Boolean expression contained in aniforelse ifclause that istrue, executes the statements contained in its block (the statements between oneelse ifand the followingelse iforelseclause), and then exits theifstatement.
Anifstatement can also include a finalelseclause. The statements in its block are executed if no other test in theifstatement passes.

### repeat Statements

You use arepeatstatement to create loops or execute groups of repeated statements in scripts.
There are a number of types ofrepeatstatement, each differing in the way it terminates the loop. Each of the options, from repeating a loop a specific number of times, to looping over the items in a list, to looping until a condition is met, and so on, lends itself to particular kinds of tasks.
For information on testing and debuggingrepeatstatements, seeDebugging AppleScript Scripts.
Terminates arepeatloop and resumes execution with the statement that follows therepeatstatement.
You can only use anexitstatement inside arepeatstatement. Though most commonly used with therepeat (forever)form, you can also use anexitstatement with other types ofrepeatstatement.

##### Syntax

```

exit [ repeat ]```

##### Examples

See the example inrepeat (forever).
Repeats a statement (or statements) until anexitstatement is encountered.
Important:Arepeat(forever) statement will never complete unless you cause it to do so.
To terminate arepeat(forever) statement, you can:

- Use anexitstatement and design the logic so that it eventually encounters theexitstatement.
Use anexitstatement and design the logic so that it eventually encounters theexitstatement.

- Use areturnstatement, which exits the handler or script that contains the loop, and therefore the loop as well.
Use areturnstatement, which exits the handler or script that contains the loop, and therefore the loop as well.

- Use atrystatement and rely on an error condition to exit the loop.
Use atrystatement and rely on an error condition to exit the loop.

##### Syntax

```

repeat
Â Â Â [ statement ]...
end [ repeat ]```

##### Placeholders

Any AppleScript statement.

##### Examples

This form of therepeatstatement is similar to therepeat untilform, except that instead of putting a test in therepeatstatement itself, you determine within the loop when it is time to exit. You might use this form, for example, to wait for a lengthy or indeterminate operation to complete:

```

repeat```

```

    -- perform operations```

```

    if someBooleanTest then```

```

        exit repeat```

```

    end if```

```

end repeat```
In a script application that stays open, you can use anidlehandler to perform periodic tasks, such as checking for an operation to complete. Seeidle Handlersfor more information.
Repeats a statement (or statements) a specified number of times.

##### Syntax

```

repeat integer [ times ]
Â Â Â [ statement ]...
end [ repeat ]```

##### Placeholders

Specifies the number of times to repeat the statements in the body of the loop.
Instead of an integer, you can specify any value that can be coerced to an integer.
If the value is less than one, the body of therepeatstatement is not executed.
Any AppleScript statement.

##### Examples

The following handler uses therepeat (number) timesform of therepeatstatement to raise a passed number to the passed power:

```

on raiseToTheNth(x, power)```

```

    set returnVal to x```

```

    repeat power - 1 times```

```

        set returnVal to returnVal * x```

```

    end repeat```

```

    return returnVal```

```

end raiseToTheNth```
Repeats a statement (or statements) until a condition is met. Tests the condition before executing any statements.

##### Syntax

```

repeat until boolean
Â Â Â [ statement ]...
end [ repeat ]```

##### Placeholders

A Boolean expression. If it has the valuetruewhen entering the loop, the statements in the loop are not executed.
Any AppleScript statement.

##### Examples

The following example uses therepeat untilform of therepeatstatement to allow a user to enter database records. The handlerenterDataRecord(), which is not shown, returnstrueif the user is done entering records:

```

set userDone to false```

```

repeat until userDone```

```

    set userDone to enterDataRecord()```

```

end repeat```
Repeats a statement (or statements) as long as a condition is met. Tests the condition before executing any statements. Similar to therepeat untilform, except that it continueswhilea condition istrue, instead ofuntilit istrue.

##### Syntax

```

repeat while boolean
Â Â Â [ statement ]...
end [ repeat ]```

##### Placeholders

A Boolean expression. If it has the valuefalsewhen entering the loop, the statements in the loop are not executed.
Any AppleScript statement.

##### Examples

The following example uses therepeat whileform of therepeatstatement to allow a user to enter database records. In this case, weâve just reversed the logic shown in therepeat untilexample. Here, the handlerenterDataRecord(), which is not shown, returnstrueif the user isnotdone entering records:

```

set userNotDone to true```

```

repeat while userNotDone```

```

    set userNotDone to enterDataRecord()```

```

end repeat```
Repeats a statement (or statements) until the value of the controlling loop variable exceeds the value of the predefined stop value.

##### Syntax

```

repeat with  loopVariable  from  startValue  to  stopValue [ by  stepValue ]
Â Â Â [ statement ]...
end [ repeat ]```

##### Placeholders

Controls the number of iterations. It can be a previously defined variable or a new variable you define in therepeatstatement.
Specifies a value that is assigned toloopVariablewhen the loop is entered.
You can specify an integer or any value that can be coerced to an integer.
Specifies an value. When that value is exceeded by the value ofloopVariable, iteration ends. IfstopValueis less thanstartValue, the body is not executed.
You can specify an integer or any value that can be coerced to an integer.
Specifies a value that is added toloopVariableafter each iteration of the loop. You can assign anintegeror arealvalue; arealvalue is rounded to aninteger.
Any AppleScript statement.

##### Examples

The following handler uses therepeat with loopVariable (from startValue to stopValue)form of therepeatstatement to compute a factorial value (the factorial of a number is the product of all the positive integers from 1 to that number):

```

on factorial(x)```

```

    set returnVal to 1```

```

    repeat with n from 2 to x```

```

        set returnVal to returnVal * n```

```

    end repeat```

```

    return returnVal```

```

end factorial```

##### Discussion

You can use an existing variable as the loop variable in arepeat with loopVariable (from startValue to stopValue)statement or define a new one in the statement. In either case, the loop variable is defined outside the loop. You can change the value of the loop variable inside the loop body but it will get reset to the next loop value the next time through the loop. After the loop completes, the loop variable retains its last value.
AppleScript evaluatesstartValue,stopValue, andstepValuewhen it begins executing the loop and stores the values internally. As a result, if you change the values in the body of the loop, it doesnât change the execution of the loop.
Loops through the items in a specified list.
The number of iterations is equal to the number of items in the list. In the first iteration, the value of the variable is a reference to the first item inlist, in the second iteration, it is a reference to the second item inlist, and so on.

##### Syntax

```

repeat with loopVariable in list
Â Â Â [ statement ]...
end [ repeat ]```

##### Placeholders

Any previously defined variable or a new variable you define in therepeatstatement (see Discussion).
A list or a object specifier (such aswords 1 thru 5) whose value is a list.
listcan also be a record; AppleScript coerces the record to a list (see Discussion).
Any AppleScript statement.

##### Examples

The following script uses therepeat with loopVariable (in list)form of therepeatstatement to loop through a list of first names, displaying a greeting for each.

```

set peopleList to {"Chris", "David", "Sal", "Ben"}```

```

repeat with aPerson in peopleList```

```

    display dialog "Hello " & aPerson & "!"```

```

end repeat```

##### Discussion

You can use an existing variable as the loop variable in arepeat with loopVariable (in list)statement or define a new one in therepeat withâ¦statement. In either case, the loop variable is assigned a new valueâthe current item in the loopâat the start of each loop. After the loop completes, the loop variable retains its last value.
This example uses an existing variable as the loop variable:

```

set currentIncrement to 0```

```

-- The loop variable is an existing variable, defined above```

```

repeat with currentIncrement in {1, 2, 3, 4}```

```

    -- Do something```

```

end repeat```

```

currentIncrement```

```

--result: item 4 of {1, 2, 3, 4} --result: the last value of the loop variable```
This example defines a new variable as the loop variable:

```

-- The loop variable is a new variable, defined in the repeat statement```

```

repeat with currentIncrement in {1, 2, 3, 4}```

```

    -- Do something```

```

end repeat```

```

currentIncrement```

```

--result: item 4 of {1, 2, 3, 4} --result: the last value of the loop variable```
You can change the value of the loop variable inside the loop body, but it gets reset to the next loop value the next time through the loop. Again, after the loop completes, the loop variable retains its last value.

```

repeat with currentIncrement in {1, 2, 3, 4}```

```

    display dialog currentIncrement```

```

    set currentIncrement to 0```

```

end repeat```

```

currentIncrement```

```

--result: 0```
AppleScript evaluatesloopVariableinlistas an object specifierâa reference to the current item in the listâthat takes on the value ofitem 1 of list,item 2 of list,item 3 of list, and so on until it reaches the last item in the list. For example:

```

repeat with i in {1, 2, 3, 4}```

```

    set listItem to i```

```

end repeat```

```

--result: item 4 of {1, 2, 3, 4} --result: an object specifier```
To access the actual value of an item in the list, rather than a reference to the item, use thecontents ofproperty:

```

repeat with i in {1, 2, 3, 4}```

```

    set listItem to contents of i```

```

end repeat```

```

--result: 4```
This technique is especially important when performing a comparison, as you typically want to test whether thevalueof a list item matches another value. The following script examines a list of words, displaying a dialog if it finds the word âhammerâ in the list. To perform a proper comparison, the test statement (if (contents of currentWord) is equal to "hammer" then) compares thecontentsof the current list item, rather than the object specifier itself.

```

set wordList to words in "Where is the hammer?"```

```

repeat with currentWord in wordList```

```

    log currentWord```

```

    if (contents of currentWord) is equal to "hammer" then```

```

        display dialog "I found the hammer!"```

```

    end if```

```

end repeat```
Note:In the previous example, the statementlog currentWordlogs the current list item to Script Editorâs log pane. For more information about logging, seeDebugging AppleScript Scripts.
You can also use list variables directly in expressions, which may result in an implicit coercion from an object reference to a specific data type. In the following example, the loop variableiis implicitly coerced to an integer (equivalent to explicitly retrieving thecontents of i) by using the+operator to add it to a variable containing an integer.

```

set total to 0```

```

repeat with i in {1, 2, 3, 4}```

```

    set total to total + i```

```

end repeat```

```

--result: 10```

### tell Statements

Atellstatement specifies the default targetâthat is, the object to which commands are sent if they do not include a direct parameter. Statements within atellstatement that use terminology from the targeted object are compiled against that objectâs dictionary.
The object of atellstatement is typically a reference to an application object or ascriptobject. For example, the followingtellstatement targets the Finder application:

```

tell application "Finder"```

```

    set frontWindowName to name of front window```

```

    -- any number of additional statements can appear here```

```

end tell```
You can nesttellstatements inside othertellstatements, as long as you follow the syntax and rules described intell (compound).
When you need to call a handler from within atellstatement, there are special terms you use to indicate that the handler is part of the script and not a command that should be sent to the object of thetellstatement. These terms are described inThe it and me Keywordsand inCalling Handlers in a tell Statement.
Atellstatement that targets a local application doesnât cause it to launch, if it is not already running. For example, a script can examine therunningproperty of the targetedapplicationobject to determine if the application is running before attempting to send it any commands. If it is not running it wonât be launched.
If atellstatement targets a local application and executes any statements that require a response from the application, then AppleScript will launch the application if it is not already running. The application is launched as hidden, but the script can send it anactivatecommand to bring it to the front, if needed.
Atellstatement that targets a remote application will not cause it to launchâin fact, it will not compile or run unless the application is already running. Nor is it possible to access therunningproperty of an application on a remote computer.
Specifies a target object and a command to send to it.

##### Syntax

```

tell referenceToObject to statement ```

##### Placeholders

Any object. Typically an object specifier or areferenceobject (which contains an object specifier).
Any AppleScript statement.

##### Examples

This simpletellstatement closes the front Finder window:

```

tell front window of application "Finder" to close```
For more information on how to specify an application object, see theapplicationclass.
Specifies a target object and one or more commands to send to it. A compoundtellstatement is different from a simpletellstatement in that it always includes anendstatement.

##### Syntax

```

tell referenceToObject  Â Â Â [ statement ]... end [ tell ]```

##### Placeholders

Any object. Typically an object specifier or areferenceobject (which contains an object specifier).
Any AppleScript statement, including anothertellstatement.

##### Examples

The following statements show how to close a window using first a compoundtellstatement, then with two variations of a simpletellstatement:

```

tell application "Finder"```

```

    close front window```

```

end tell```

```

 ```

```

tell front window of application "Finder" to close```

```

tell application "Finder" to close front window```
The following example shows a nestedtellstatement:

```

tell application "Finder"```

```

    tell document 1 of application "TextEdit"```

```

        set newName to word 1 -- handled by TextEdit```

```

    end tell```

```

    set len to count characters in newName -- handled by AppleScript```

```

    if (len > 2) and (len < 15) then -- comparisons handled by AppleScript```

```

        set name of first item of disk "HD" to newName -- handled by Finder```

```

    end if```

```

end tell```
This example works because in each case the terminology understood by a particular application is used within atellblock targeting that application. However, it would not compile if you asked the Finder forword 1of a document, or told TextEdit toset nameof the first item on a disk, because those applications do not support those terms.

### try Statements

Atrystatement provides the means for scripts to handle potential errors. It attempts to execute one or more statements and, if an error occurs, executes a separate set of statements to deal with the error condition. If an error occurs and there is notrystatement in the calling chain to handle it, AppleScript displays an error and script execution stops.
For related information, seeerror StatementsandAppleScript Error Handling.
Attempts to execute a list of AppleScript statements, calling an error handler if any of the statements results in an error.
Atrystatement is a two-part compound statement that contains a series of AppleScript statements, followed by an error handler to be invoked if any of those statements causes an error. If the statement that caused the error is included in atrystatement, then AppleScript passes control to the error handler. After the error handler completes, control passes to the statement immediately following the end of thetrystatement.

##### Syntax

```

try
Â Â Â [ statement ]...
[ on error [ errorMessage ] [ number errorNumber ] [ from offendingObject ] Â¬
Â Â Â [ partial result resultList ] [ to expectedType ]
Â Â Â Â Â Â [ statement ]... ]
end [ error | try ]```

##### Placeholders

Any AppleScript statement.
Atextobject, that describes the error.
The error number, an integer. For possible values, seeError Numbers and Error Messages.
A reference to the object, if any, that caused the error.
A list that provides partial results for objects that were handled before the error occurred. The list can contain values of any class. This parameter applies only to commands that return results for multiple objects. This is rarely supported by applications.
The expected class. If the error was caused by a coercion failure, the value of this variable is the class of the coercion that failed. (The second example below shows how this works in a case where AppleScript is unable to coerce atextobject into aninteger.)
Either a global variable or a local variable that can be used in the handler. A variable can contain any class of value. The scope of a local variable is the handler. The scope of a global variable extends to any other part of the script, including other handlers andscriptobjects. For related information about local and global variables, seeversion.

##### Examples

The following example shows how you can use atrystatement to handle the âCancelâ button for adisplay alertcommand. Canceling returns an error number of -128, but is not really an error. This test handler just displays a dialog to indicate when the user cancels or when some other error occurs.

```

try```

```

    display alert "Hello" buttons {"Cancel", "Yes", "No"} cancel button 1```

```

on error errText number errNum```

```

    if (errNum is equal to -128) then```

```

        -- User cancelled.```

```

        display dialog "User cancelled."```

```

    else```

```

        display dialog "Some other error: " & errNum & return & errText```

```

    end if```

```

end try```
You can also use a simplified version of thetrystatement that checks for just a single error number. In the following example, only error -128 is handled. Any other error number is ignored by thistrystatement, but is automatically passed up the calling chain, where it may be handled by othertrystatements.

```

try```

```

    display alert "Hello" buttons {"Cancel", "Yes", "No"} cancel button 1```

```

on error number -128```

```

    -- Either do something special to handle Cancel, or just ignore it.```

```

end try```
The following example demonstrates the use of thetokeyword to capture additional information about an error that occurs during a coercion failure:

```

try```

```

    repeat with i from 1 to "Toronto"```

```

        -- do something that depends on variable "i"```

```

    end repeat```

```

on error from obj to newClass```

```

    log {obj, newClass} -- Display from and to info in log pane.```

```

end try```
Thisrepeatstatement fails because thetextobject"Toronto"cannot be coerced to aninteger. The error handler simply writes the values ofobj(the offending value,"Toronto") andnewClass(the class of the coercion that failed,integer) to Script Editorâs Event Log History window (and to the script windowâs Event Log pane). The result is â(*Toronto, integer*)â, indicating the error occurred while trying to coerce âTorontoâ to an integer.
For additional examples, seeWorking with Errors.

### use Statements

Ausestatement declares a required resource for a scriptâan application, script library, framework, or version of AppleScript itselfâand can optionallyimportterminology from the resource for use elsewhere in the script. The effects and syntax ofusevary slightly depending on the used resource; the different cases are described below.
Note:usestatements are supported in OS X Mavericks v10.9 (AppleScript 2.3) and later.
The basic function ofuseis to require that a resource be present before the script begins executing. If the requirement cannot be met, the script will fail to run. Ausestatement can also specify a minimum version for the required resource, such as a minimum compatible version of an application. In this example, AppleScript will ensure that Safari version 7.0 or later is available:

```

use application "Safari" version "7.0"```
usestatements can also import terminology from the used resource, making the terms available throughout the script without requiring the use oftellorusing terms from. AppleScript tracks where terms were imported from, and sends events that use those terms to that target. Ordinarily, commands are sent to the current target (it) as described inTarget, but imported terminology overrides this. Ifâ¦

- the event identifier is imported
the event identifier is imported

- the direct parameter is an imported class or enumeration identifier
the direct parameter is an imported class or enumeration identifier

- the direct parameter is an object specifier ending with an imported term
the direct parameter is an object specifier ending with an imported term
â¦then the command is sent to the import source instead. This happens even if the command is inside atellblock for a different target. For example, this script uses a command from Safari:

```

use application "Safari"```

```

search the web for "AppleScript"```
Importing happens by default, but can be suppressed using thewithout importingparameter, if applicable. You can use this to add requirements to existing scripts without changing anything else about the script:

```

use application "Safari" version "7.0" without importing```
Because Safari's terms are not imported, the script will still need to usetellto send it events.
Declares a required minimum version of AppleScript, and that the script expects a newer behavior for how scripting additions are handled, described inuse (scripting additions).

##### Syntax

```

use AppleScript [ version versionText ] ```

##### Placeholders

The required minimum version of AppleScript, as a version string such as"2.3.2". If omitted, its default value is 2.3, the version in whichusewas introduced. This value is always text, not a number, and is compared as ifconsidering numeric stringsis in effect. For example,"2.10"is greater than"2.3", because 10 is greater than 3.

##### Examples

In its simplest form,usecan be used to declare that the script uses AppleScript:

```

use AppleScript```
This also implicitly means that the script uses AppleScript version 2.3 or later, whenusewas first introduced, and that the script expects a newer behavior for how scripting additions are handled, described inuse (scripting additions).
Ausecommand can also explicitly specify a minimum required version of AppleScript:

```

use AppleScript version "2.3.2"```
Declares that a script uses scripting additions.

##### Syntax

```

use scripting additions Â¬ Â Â Â [ with importing | without importing | importing boolean ]```

##### Placeholders

A boolean value,trueorfalse. AppleScript will recompile this towith importingorwithout importing. The default iswith importing.

##### Examples

Useuse scripting additionsto explicitly declare that the script uses scripting addition commands:

```

use scripting additions```

##### Discussion

Scripting addition commands are handled differently if a script hasusecommands. If a script has one or moreusecommands of any kind, scripting addition commands arenotavailable by default. You must explicitly indicate that you wish to use scripting additions, either with auseorusing terms fromcommand.

```

use scripting additions```

```

display dialog "hello world"```

```

using terms from scripting additions```

```

   display dialog "hello world"```

```

end using terms from```
If a script usesuse scripting additions, AppleScript may optimize scripting addition commands, sending them to the current application instead of the current target (it) when it does not change the meaning to do so. For example,random numberdoes not need to be sent to another application to work correctly, and will always be sent to the current application when imported withuse. Without ause scripting additionscommand, AppleScript must use a less efficient dispatching scheme, so explicitly declaring them is recommended.
Declares a required application or script library, and may import its terms for use later in the script.

##### Syntax

```

use [ identifier : ] ( script | application ) specifier Â¬Â Â Â [ version versionText ] Â¬Â Â Â [ with importing | without importing | importing boolean ]```

##### Placeholders

The required minimum version of the resource as a version number, such as"2.3.2". This value is always text, not a number, and is compared as ifconsidering numeric stringsis in effect. For example,"2.10"is greater than"2.3", because 10 is greater than 3.
An optional identifier for the resource.
Specifier data for the resource. This is typically a name, as inuse application "Finder"oruse script "My Library", but may be any valid specifier form, such as by ID, as inuse application id "com.apple.mail".
A boolean value,trueorfalse. AppleScript will recompile this towith importingorwithout importing. The default iswith importing.

##### Examples

Ausecommand may refer to an application:

```

use application "Finder"```
â¦or a script library:

```

use script "Happy Fun Ball"```
If an optional identifier is given, it defines a property whose value is the required resource. This can make it more convenient to refer to the resource, as in this example: thegetstatement uses the identifierSafariinstead of the full specifierapplication "Safari".

```

use Safari : application "Safari"```

```

get the name of Safari's front window```
By usingusewith multiple applications, you can combine terms from different sources in ways impossible usingtell, becausetellonly makes one terminology source available at a time. For example, the following script, in one statement, uses Mail and Safari to search the web for the sender of the currently selected mail message. Thegetevent is sent to Mail because it definesmessage viewer, while thesearch the webevent is sent to Safari.

```

use application "Mail"```

```

use application "Safari"```

```

 ```

```

search the web for the sender of the first item of Â¬```

```

 ```

```

   (get selected messages of the front message viewer)```
Declares a required framework for use with the AppleScript/Objective-C bridge.

##### Syntax

```

use  framework  specifier```

##### Placeholders

Specifier data for the resource. This may be a base name ("AppKit"), a full name ("AppKit.framework"), or a POSIX path ("/System/Library/Frameworks/AppKit.framework").

##### Examples

Most scripts that use the AppleScript/Objective-C bridge should have at least one of these twousestatements:

```

use framework "Foundation"```

```

use framework "AppKit"```
You can also use other frameworks, such as WebKit:

```

use framework "WebKit"```

##### Discussion

When you declare a required framework, AppleScript ensures the framework is loaded before running your script. To ensure that your AppleScript/Objective-C script libraries work correctly in any application,  declare all needed frameworks explicitly; otherwise, there is no guarantee that a given framework will be available, and your script may fail.
Theversionparameter is not supported for frameworks; to check whether or not a framework supports a certain feature, useNSClassFromStringor-respondsToSelector:.
Note:OS X Yosemite v10.10 and later allow using Objective-C frameworks from any script. OS X Mavericks v10.9 only allows using Objective-C frameworks from a script library.

### using terms from Statements

Ausing terms fromstatement lets you specify which terminology AppleScript should use in compiling the statements in a script. Whereas atellstatement specifies the default target (often an application) to which commands are sentandthe terminology to use, ausing terms fromstatement specifies only the terminology.
Ausing terms fromstatement can be useful in writing application event handler scripts, such as Mail rules.
Another use for this type of statement is with a script that targets an application on a remote computer that may not be available when you compile the script (or the application may not be running). Or, you might be developing locally and only want to test with the remote application at a later time. In either case, you can use ausing terms fromstatement to specify a local application (presumably with a terminology that matches the one on the remote computer) to compile against.
Even if a statement contained within ausing terms fromstatement compiles, the script may fail when run because the target applicationâs terminology may differ from that used in compiling.
You can nestusing terms fromstatements. When you do so, each script statement is compiled against the terminology of the application named in the innermost enclosingusing terms fromstatement.
Instructs AppleScript to use the terminology from the specified source in compiling the enclosed statements.

##### Syntax

```

using terms from ( application  |  script  | scripting additions) Â Â Â [ statement ]... end [ using terms from ]```

##### Placeholders

A specifier for an application object.
A specifier for a script library.
Any AppleScript statement.

##### Examples

The following example shows how to use ausing terms fromstatement in writing a Mail rule action script. These scripts take the following form:

```

using terms from application "Mail"```

```

  on perform mail action with messages theMessages for rule theRule```

```

    tell application "Mail"```

```

        -- statements to process each message in theMessages```

```

    end tell```

```

  end perform mail action with messages```

```

end using terms from```
To use the script, you open Preferences for the Mail application, create or edit a rule, and assign the script as the action for the rule.
For an example that works with an application on a remote machine, seeTargeting Remote Applications.
As discussed inuse Statements, a script with anyusestatements does not make scripting addition terms visible by default. You can enable scripting addition terms for specific parts of a script withusing terms fromas in this example:

```

use AppleScript```

```

-- scripting addition commands such as "display dialog" will not compile here...```

```

using terms from scripting additions -- ...but will compile within this block.```

```

   display dialog "Hello world!"```

```

end using terms from```

##### Discussion

using terms fromdoes not import terms asusedoes, and is subject to the same limits on terminology use astell.using terms from scripting additionsdoes not enable optimization of scripting addition commands asuse scripting additionsdoes.

### with timeout Statements

You can use awith timeoutstatement to control how long AppleScript waits for a command to execute before timing out. By default,when an application fails to respond to a command, AppleScript waits for two minutes before reporting an error and halting execution.
Specifies how long AppleScript waits for a response to a command that is sent to another application.

##### Syntax

```

with timeout [ of ] integerExpression second[s] Â Â Â [ statement ]... end [ timeout ] ```

##### Placeholders

The amount of time, in seconds, AppleScript should wait before timing out (and interrupting the command).
Any AppleScript statement.

##### Examples

The following script tells TextEdit to close its first document; if the document has been modified, it asks the user if the document should be saved. It includes the statementwith timeout of 20 seconds, so that if the user doesnât complete thecloseoperation within 20 seconds, the operation times out.

```

tell application "TextEdit"```

```

    with timeout of 20 seconds```

```

        close document 1 saving ask```

```

    end timeout```

```

end tell```

##### Discussion

When a command fails to complete in the allotted time (whether the default of two minutes, or a time set by awith timeoutstatement), AppleScript stops running the script and returns the error"event timed out".AppleScript does not cancel the operationâit merely stops execution of the script. If you want the script to continue, you can wrap the statements in atrystatement. However, whether your script can send a command to cancel an offending lengthy operation after a timeout is dependent on the application that is performing the command.
Awith timeoutstatement applies only to commands sent to application objects, not to commands sent to the application that is running the script.
In some situations, you may want to use anignoring application responsesstatement (instead of awith timeoutstatement) so that your script neednât wait for application commands to complete. For more information, seeconsidering and ignoring Statements.

### with transaction Statements

When you execute a script, AppleScript may send one or more Apple events to targeted applications. A transaction is a set of operations that are applied as a single unitâeither all of the changes are applied or none are. This mechanism works only with applications that support it.
Associates a single transaction ID with any events sent to a target application as a result of executing commands in the body of the statement.

##### Syntax

```

with transaction [ session ] 
Â Â Â [ statement ]...
end [ transaction ]```

##### Placeholders

An object that identifies a specific session.
Any AppleScript statement.

##### Examples

This example uses awith transactionstatement to ensure that a record can be modified by one user without being modified by another user at the same time. (In the following examples, âSmall DBâ and âSuper DBâ are representative database applications.)

```

tell application "Small DB"```

```

    with transaction```

```

        set oldName to Field "Name"```

```

        set oldAddress to Field "Address"```

```

        set newName to display dialog Â¬```

```

            "Please type a new name" Â¬```

```

            default answer oldName```

```

        set newAddress to display dialog Â¬```

```

            "Please type the new address" Â¬```

```

            default answer oldAddress```

```

        set Field "Name" to newName```

```

        set Field "Address" to newAddress```

```

    end transaction```

```

end tell```
Thesetstatements obtain the current values of the Name and Address fields and invite the user to change them. Enclosing thesesetstatements in a singlewith transactionstatement informs the application that other users should not be allowed to access the same record at the same time.
Awith transactionstatement works only with applications that explicitly support it. Some applications only supportwith transactionstatements (like the one in the previous example) that do not take a session object as a parameter. Other applications support bothwith transactionstatements that have no parameter andwith transactionstatements that take a session parameter.
The following example demonstrates how to specify a session for awith transactionstatement:

```

tell application "Super DB"```

```

    set mySession to make session with data {user: "Bob", password: "Secret"}```

```

    with transaction mySession```

```

        ...```

```

    end transaction```

```

end tell```
Copyright © 2016 Apple Inc. All Rights Reserved.Terms of Use|Privacy Policy|  Updated: 2016-01-25