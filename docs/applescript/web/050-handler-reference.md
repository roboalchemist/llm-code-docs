# Handler Reference

This chapter provides reference for handlers, which are defined and introduced inAbout Handlers. It describes the types of parameters you can use with handlers and how you invoke them. It also describes thecontinueandreturnstatements, which you use to control the flow of execution in handlers.
Acontinuestatement causes AppleScript to invoke the handler with the same name in the parent of the current handler. If there is no such handler in the parent, AppleScript looks up the parent chain, ending with the current application.
Acontinuestatement is like a handler call, in that after execution completes in the new location, it resumes with the statement after thecontinuestatement.

##### Syntax

```

continue handlerName [ parameterList ]```

##### Placeholders

A required identifier that specifies the name of the current handler (which is also the name of the handler in which to continue execution).
The list of parameters to be passed tohandlerName.
The list must follow the same format as the parameter definitions in the handler definition for the command. For handlers with labeled parameters, this means that the parameter labels must match those in the handler definition. For handlers with positional parameters, the parameters must appear in the correct order.
You can list the parameter variables that were specified in the original command (and thus the original values) or you can list values that may differ from those of the original variables.

##### Examples

You can write a handler that overrides an AppleScript command but uses acontinuestatement to pass control on to the AppleScript command if desired:

```

on beep numTimes```

```

    set x to display dialog "Start beeping?" buttons {"Yes", "No"}```

```

    if button returned of x is "Yes" then Â¬```

```

        continue beep numTimes -- Let AppleScript handle the beep.```

```

        -- In this example, nothing to do after returning from the continue.```

```

end beep```

```

 ```

```

beep 3 --result: local beep handler invoked; shows dialog before beeping```

```

tell my parent to beep 3 -- result: AppleScript beep command invoked```
When AppleScript encounters the statementbeep 3, it invokes the localbeephandler, which displays a dialog. If the user clicks Yes, the handler uses acontinuestatement to pass thebeepcommand to the scriptâs parent (AppleScript), which handles the command by beeping. If the user clicks No, it does not continue thebeepcommand, and no sound is heard.
The final statement,tell my parent to beep 3, shows how to directly invoke the AppleScriptbeepcommand, rather than the local handler.
For an example that uses acontinuestatement to exit a script handler and return control to the applicationâs defaultquithandler, seequit Handlers.
For additional examples, seeUsing the continue Statement in Script Objects.
Areturnstatement exits a handler and optionally returns a specified value. Execution continues at the place in the script where the handler was called.

##### Syntax

```

return [ expression ]```

##### Placeholders

Represents the value to return.

##### Examples

The following statement, inserted in the body of a handler, returns the integer2:

```

return 2 -- returns integer value 2```
If you include areturnstatement without an expression, AppleScript exits the handler immediately and no value is returned:

```

return -- no value returned```
See other sections throughoutHandler Referencefor more examples of scripts that use thereturnstatement.

##### Discussion

If a handler does not include areturnstatement, AppleScript returns the value returned by the last statement. If the last statement doesnât return a value, AppleScript returns nothing.
When AppleScript has finished executing a handler (that is, when it executes areturnstatement or the last statement in the handler), it passes control to the place in the script immediately after the place where the handler was called. If a handler call is part of an expression, AppleScript uses the value returned by the handler to evaluate the expression.
It is often considered good programming practice to have just onereturnstatement and locate it at the end of a handler. Doing so can provide the following benefits:

- The script is easier to understand.
The script is easier to understand.

- The script is easier to debug.
The script is easier to debug.

- You can place cleanup code in one place and make sure it is executed.
You can place cleanup code in one place and make sure it is executed.
In some cases, however, it may make more sense to use multiplereturnstatements. For example, theminimumValuehandler inHandler Syntax (Positional Parameters)is a simple script that uses tworeturnstatements.
For related information, seeAppleScript Error Handling.
A handler is a collection of statements that can be invoked by name. This section describes the syntax for handlers that use labeled parameters.
Labeled parameters are identified by their labels and can be listed in any order.

##### Syntax

```

( on | to ) handlerName Â¬   [ [ of | in ] directParamName ] Â¬   [ ASLabel userParamName ]... Â¬   [ given userLabel:userParamName [, userLabel:userParamName ]...]      [ statement ]...end [ handlerName ]```

##### Placeholders

An identifier that names the handler.
An identifier for the direct parameter variable. If it is included,directParamNamemust be listed immediately after the command name. The wordoforinbeforedirectParamNameis required in user-defined handlers, but is optional in terminology-defined handlers (for example, those defined by applications).
If a user-defined handler includes a direct parameter, the handler must also include at least one variable parameter.
An AppleScript-defined label. The available labels are:about,above,against,apart from,around,aside from,at,below,beneath,beside,between,by,for,from,instead of,into,on,onto,out of,over,since,thru(orthrough),under. These are the only labels that can be used without the special labelgiven.Each label must be unique among the labels for the handler (that is, you cannot use the same label for more than one parameter).
An identifier for a user-defined label, associated with a user-defined parameter. Each label must be unique.
The firstuserLabel-userParamNamepair must follow the wordgiven; any additional pairs are separated by commas.
An identifier for a parameter variable.
Any AppleScript statement. These statements can include definitions ofscriptobjects, each of which, like anyscriptobject, can contain handlers and otherscriptobjects. However, you cannot declare another handler within a handler, except within ascriptobject.
Handlers often contain areturnstatement.

##### Examples

For examples and related conceptual information, seeHandlers with Labeled Parameters.

##### Discussion

A handler written to respond to an application command (like those inHandlers in Script Applications) need not include all of the possible parameters defined for that command. For example, an application might define a command with up to five possible parameters, but you could define a handler for that command with only two of the parameters.
If a script calls a handler with more parameters than are specified in the handler definition, the extra parameters are ignored.
This section describes the syntax for calling a handler with labeled parameters.

##### Syntax

```

handlerName Â¬
 [ [ of | in ] directParam ] Â¬
 [ [ ASLabel paramValue ...] Â¬
  | [ with labelForTrueParam [, labelForTrueParam ]... Â¬
   [ ( and | , ) labelForTrueParam ] ] Â¬
  | [ without labelForFalseParam [, labelForFalseParam ]...] Â¬
   [ ( and | , ) labelForFalseParam ] ] Â¬
  | [ given userLabel:paramValue [, userLabel:paramValue ]...]... ```

##### Placeholders

An identifier that names the handler.
Any valid expression. The expression for the direct parameter must be listed first if it is included at all.
One of the following AppleScript-defined labels used in the definition of the handler:about,above,against,apart from,around,aside from,at,below,beneath,beside,between,by,for,from,instead of,into,on,onto,out of,over,since,thru(orthrough),under.
The value of a parameter, which can be any valid expression.
The label for a Boolean parameter whose value istrue. You use this form inwithclauses. Because the valuetrueis implied by the wordwith, you provide only the label, not the value. For an example, see thefindNumbershandler inHandlers with Labeled Parameters.
The label for a Boolean parameter whose value isfalse. You use this form inwithoutclauses. Because the valuefalseis implied by the wordwithout, you provide only the label, not the value.
Any parameter label used in the definition of the handler that is not among the labels forASLabel. You must use the special labelgivento specify these parameters. For an example, see thefindNumbershandler below.

##### Examples

For examples, seeHandlers with Labeled Parameters.

##### Discussion

When you call a handler with labeled parameters, you supply the following:

- The handler name.
The handler name.

- A value for the direct parameter, if the handler has one. It must directly follow the handler name.
A value for the direct parameter, if the handler has one. It must directly follow the handler name.

- One label-value pair for each AppleScript-defined label and parameter defined for the handler.
One label-value pair for each AppleScript-defined label and parameter defined for the handler.

- One label-value pair for each user-defined label and parameter defined for the handler thatis nota boolean value.The first pair is preceded by the wordgiven; a comma precedes each additional pair. The order of the pairs does not have to match the order in the handler definition.
One label-value pair for each user-defined label and parameter defined for the handler thatis nota boolean value.
The first pair is preceded by the wordgiven; a comma precedes each additional pair. The order of the pairs does not have to match the order in the handler definition.

- For each user-defined label and parameter defined for the handler thatisa boolean value, you can either:Supply the label, followed by a boolean expression (as with non-boolean parameters); for example:given rounding:trueUse a combination ofwithandwithoutclauses, as shown in the following examples:with rounding, smoothing and curlingwith rounding without smoothing, curlingNote:AppleScript automatically converts between some forms when you compile. For example,given rounding:trueis converted towith rounding, andwith rounding, smoothingis converted towith rounding and smoothing.
For each user-defined label and parameter defined for the handler thatisa boolean value, you can either:

- Supply the label, followed by a boolean expression (as with non-boolean parameters); for example:given rounding:true
Supply the label, followed by a boolean expression (as with non-boolean parameters); for example:

```

given rounding:true```

- Use a combination ofwithandwithoutclauses, as shown in the following examples:with rounding, smoothing and curlingwith rounding without smoothing, curlingNote:AppleScript automatically converts between some forms when you compile. For example,given rounding:trueis converted towith rounding, andwith rounding, smoothingis converted towith rounding and smoothing.
Use a combination ofwithandwithoutclauses, as shown in the following examples:

```

with rounding, smoothing and curling```

```

with rounding without smoothing, curling```
Note:AppleScript automatically converts between some forms when you compile. For example,given rounding:trueis converted towith rounding, andwith rounding, smoothingis converted towith rounding and smoothing.
A handler is a collection of statements that can be invoked by name. This section describes the syntax for handlers that use positional parameters.
Important:The parentheses that surround the parameter list in the following definition are part of the syntax.

##### Syntax

```

on | to handlerName ( [ userParamName [, userParamName ]...] )
Â Â Â [ statement ]...
end [ handlerName ] ```

##### Placeholders

An identifier that names the handler.
An identifier for a user-defined parameter variable.
Any AppleScript statement, including global or local variable declarations. For information about the scope of local and global variables, seeScope of Variables and Properties.

##### Examples

For examples and related conceptual information, seeHandlers with Positional Parameters.
A call for a handler with positional parameters must list the parameters in the same order as they are specified in the handler definition.

##### Syntax

```

handlerName( [ paramValue [, paramValue ]...] )```

##### Placeholders

An identifier that names the handler.
The value of a parameter, which can be any valid expression. If there are two or more parameters, they must be listed in the same order in which they were specified in the handler definition.

##### Examples

For examples, seeHandlers with Positional Parameters

##### Discussion

When you call a handler with positional parameters, you supply the following:

- The handler name.
The handler name.

- An opening and closing parenthesis.
An opening and closing parenthesis.

- If the handler has any parameters, then you also list, within the parentheses, the following:One value for each parameter defined for the handler. The value can be any valid expression.
If the handler has any parameters, then you also list, within the parentheses, the following:
One value for each parameter defined for the handler. The value can be any valid expression.
A handler is a collection of statements that can be invoked by name. This section describes the syntax for handlers that use interleaved parameters.

##### Syntax

```

on | tohandlerNamePart:userParamName [namePart:userParamName ]... )Â Â Â [ statement ]...end [ handlerName ] ```

##### Placeholders

An identifier that, combined with the other parts, forms the handler name.
An identifier for a user-defined parameter variable.
Any AppleScript statement, including global or local variable declarations. For information about the scope of local and global variables, seeScope of Variables and Properties.

##### Examples

For examples and related conceptual information, seeHandlers with Interleaved Parameters.
A call for a handler with interleaved parameters must list the parameters in the same order as they are specified in the handler definition.

##### Syntax

```

( tell scriptObject to | scriptObject's | my ) handlerNamePart:paramValue [ namePart:paramValue ]...] ```

##### Placeholders

A script object to direct the handler call to, which can be any valid expression.
An identifier that names the handler.
The value of a parameter, which can be any valid expression. If there are two or more parameters, they must be listed in the same order in which they were specified in the handler definition.

##### Examples

For examples, seeHandlers with Positional Parameters

##### Discussion

When you call a handler with positional parameters, you supply the following:

- A script object to direct the handler call to, either usingtellscriptto,script's, ormy, equivalent totell me to.
A script object to direct the handler call to, either usingtellscriptto,script's, ormy, equivalent totell me to.

- The first handler name part.
The first handler name part.

- A value for the first parameter.
A value for the first parameter.

- For each additional parameter, you also list the following:The next name part, followed by a colon and a value for that parameter. The value can be any valid expression.
For each additional parameter, you also list the following:
The next name part, followed by a colon and a value for that parameter. The value can be any valid expression.
Copyright © 2016 Apple Inc. All Rights Reserved.Terms of Use|Privacy Policy|  Updated: 2016-01-25