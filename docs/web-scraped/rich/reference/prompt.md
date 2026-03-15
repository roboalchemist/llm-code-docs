# Source: https://rich.readthedocs.io/en/latest/reference/prompt.html

[]

# rich.prompt[](#module-rich.prompt "Link to this heading")

*[[class]][ ]*[[rich.prompt.]][[Confirm]][(]*[[prompt]][[=]][[\'\']]*, *[[\*]]*, *[[console]][[=]][[None]]*, *[[password]][[=]][[False]]*, *[[choices]][[=]][[None]]*, *[[case_sensitive]][[=]][[True]]*, *[[show_default]][[=]][[True]]*, *[[show_choices]][[=]][[True]]*[)][[[\[source\]]]](../_modules/rich/prompt.html#Confirm)[](#rich.prompt.Confirm "Link to this definition")

:   A yes / no confirmation prompt.

    Example

    ::: 
    ::: highlight
        >>> if Confirm.ask("Continue"):
                run_job()
    :::
    :::

    Parameters[:]

    :   -   **prompt** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") *\|* [*Text*](text.html#rich.text.Text "rich.text.Text"))

        -   **console** ([*Console*](console.html#rich.console.Console "rich.console.Console") *\|* *None*)

        -   **password** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"))

        -   **choices** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")*\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*\]*)

        -   **case_sensitive** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"))

        -   **show_default** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"))

        -   **show_choices** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"))

    [[process_response]][(]*[[value]]*[)][[[\[source\]]]](../_modules/rich/prompt.html#Confirm.process_response)[](#rich.prompt.Confirm.process_response "Link to this definition")

    :   Convert choices to a bool.

        Parameters[:]

        :   **value** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)"))

        Return type[:]

        :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    [[render_default]][(]*[[default]]*[)][[[\[source\]]]](../_modules/rich/prompt.html#Confirm.render_default)[](#rich.prompt.Confirm.render_default "Link to this definition")

    :   Render the default as (y) or (n) rather than True/False.

        Parameters[:]

        :   **default** (*DefaultType*)

        Return type[:]

        :   [*Text*](text.html#rich.text.Text "rich.text.Text")

    [[response_type]][](#rich.prompt.Confirm.response_type "Link to this definition")

    :   alias of [[`bool`]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

```
<!-- -->
```

*[[class]][ ]*[[rich.prompt.]][[FloatPrompt]][(]*[[prompt]][[=]][[\'\']]*, *[[\*]]*, *[[console]][[=]][[None]]*, *[[password]][[=]][[False]]*, *[[choices]][[=]][[None]]*, *[[case_sensitive]][[=]][[True]]*, *[[show_default]][[=]][[True]]*, *[[show_choices]][[=]][[True]]*[)][[[\[source\]]]](../_modules/rich/prompt.html#FloatPrompt)[](#rich.prompt.FloatPrompt "Link to this definition")

:   A prompt that returns a float.

    Example

    ::: 
    ::: highlight
        >>> temperature = FloatPrompt.ask("Enter desired temperature")
    :::
    :::

    Parameters[:]

    :   -   **prompt** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") *\|* [*Text*](text.html#rich.text.Text "rich.text.Text"))

        -   **console** ([*Console*](console.html#rich.console.Console "rich.console.Console") *\|* *None*)

        -   **password** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"))

        -   **choices** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")*\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*\]* *\|* *None*)

        -   **case_sensitive** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"))

        -   **show_default** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"))

        -   **show_choices** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"))

    [[response_type]][](#rich.prompt.FloatPrompt.response_type "Link to this definition")

    :   alias of [[`float`]](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")

```
<!-- -->
```

*[[class]][ ]*[[rich.prompt.]][[IntPrompt]][(]*[[prompt]][[=]][[\'\']]*, *[[\*]]*, *[[console]][[=]][[None]]*, *[[password]][[=]][[False]]*, *[[choices]][[=]][[None]]*, *[[case_sensitive]][[=]][[True]]*, *[[show_default]][[=]][[True]]*, *[[show_choices]][[=]][[True]]*[)][[[\[source\]]]](../_modules/rich/prompt.html#IntPrompt)[](#rich.prompt.IntPrompt "Link to this definition")

:   A prompt that returns an integer.

    Example

    ::: 
    ::: highlight
        >>> burrito_count = IntPrompt.ask("How many burritos do you want to order")
    :::
    :::

    Parameters[:]

    :   -   **prompt** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") *\|* [*Text*](text.html#rich.text.Text "rich.text.Text"))

        -   **console** ([*Console*](console.html#rich.console.Console "rich.console.Console") *\|* *None*)

        -   **password** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"))

        -   **choices** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")*\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*\]* *\|* *None*)

        -   **case_sensitive** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"))

        -   **show_default** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"))

        -   **show_choices** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"))

    [[response_type]][](#rich.prompt.IntPrompt.response_type "Link to this definition")

    :   alias of [[`int`]](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")

```
<!-- -->
```

*[[exception]][ ]*[[rich.prompt.]][[InvalidResponse]][(]*[[message]]*[)][[[\[source\]]]](../_modules/rich/prompt.html#InvalidResponse)[](#rich.prompt.InvalidResponse "Link to this definition")

:   Exception to indicate a response was invalid. Raise this within process_response() to indicate an error and provide an error message.

    Parameters[:]

    :   **message** (*Union\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*,* [*Text*](text.html#rich.text.Text "rich.text.Text")*\]*) -- Error message.

    Return type[:]

    :   None

```
<!-- -->
```

*[[class]][ ]*[[rich.prompt.]][[Prompt]][(]*[[prompt]][[=]][[\'\']]*, *[[\*]]*, *[[console]][[=]][[None]]*, *[[password]][[=]][[False]]*, *[[choices]][[=]][[None]]*, *[[case_sensitive]][[=]][[True]]*, *[[show_default]][[=]][[True]]*, *[[show_choices]][[=]][[True]]*[)][[[\[source\]]]](../_modules/rich/prompt.html#Prompt)[](#rich.prompt.Prompt "Link to this definition")

:   A prompt that returns a str.

    Example

    ::: 
    ::: highlight
        >>> name = Prompt.ask("Enter your name")
    :::
    :::

    Parameters[:]

    :   -   **prompt** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") *\|* [*Text*](text.html#rich.text.Text "rich.text.Text"))

        -   **console** ([*Console*](console.html#rich.console.Console "rich.console.Console") *\|* *None*)

        -   **password** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"))

        -   **choices** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")*\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*\]* *\|* *None*)

        -   **case_sensitive** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"))

        -   **show_default** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"))

        -   **show_choices** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)"))

    [[response_type]][](#rich.prompt.Prompt.response_type "Link to this definition")

    :   alias of [[`str`]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

```
<!-- -->
```

*[[class]][ ]*[[rich.prompt.]][[PromptBase]][(]*[[prompt]][[=]][[\'\']]*, *[[\*]]*, *[[console]][[=]][[None]]*, *[[password]][[=]][[False]]*, *[[choices]][[=]][[None]]*, *[[case_sensitive]][[=]][[True]]*, *[[show_default]][[=]][[True]]*, *[[show_choices]][[=]][[True]]*[)][[[\[source\]]]](../_modules/rich/prompt.html#PromptBase)[](#rich.prompt.PromptBase "Link to this definition")

:   Ask the user for input until a valid response is received. This is the base class, see one of the concrete classes for examples.

    Parameters[:]

    :   -   **prompt** (*TextType,* *optional*) -- Prompt text. Defaults to "".

        -   **console** ([*Console*](console.html#rich.console.Console "rich.console.Console")*,* *optional*) -- A Console instance or None to use global console. Defaults to None.

        -   **password** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable password input. Defaults to False.

        -   **choices** (*List\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*\],* *optional*) -- A list of valid choices. Defaults to None.

        -   **case_sensitive** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Matching of choices should be case-sensitive. Defaults to True.

        -   **show_default** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Show default in prompt. Defaults to True.

        -   **show_choices** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Show choices in prompt. Defaults to True.

    *[[classmethod]][ ]*[[ask]][(]*[[prompt]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[ ][[\|]][ ][[Text]](text.html#rich.text.Text "rich.text.Text")][ ][[=]][ ][[\'\']]*, *[[\*]]*, *[[console]][[:]][ ][[[Console]](console.html#rich.console.Console "rich.console.Console")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")][ ][[=]][ ][[None]]*, *[[password]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")][ ][[=]][ ][[False]]*, *[[choices]][[:]][ ][[[List]](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")][ ][[=]][ ][[None]]*, *[[case_sensitive]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")][ ][[=]][ ][[True]]*, *[[show_default]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")][ ][[=]][ ][[True]]*, *[[show_choices]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")][ ][[=]][ ][[True]]*, *[[default]][[:]][ ][[DefaultType]]*, *[[stream]][[:]][ ][[[TextIO]](https://docs.python.org/3/library/typing.html#typing.TextIO "(in Python v3.13)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")][ ][[=]][ ][[None]]*[)] [[→] [[DefaultType][ ][[\|]][ ][PromptType]]][[[\[source\]]]](../_modules/rich/prompt.html#PromptBase.ask)[](#rich.prompt.PromptBase.ask "Link to this definition")\
    *[[classmethod]][ ]*[[ask]][(]*[[prompt]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[ ][[\|]][ ][[Text]](text.html#rich.text.Text "rich.text.Text")][ ][[=]][ ][[\'\']]*, *[[\*]]*, *[[console]][[:]][ ][[[Console]](console.html#rich.console.Console "rich.console.Console")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")][ ][[=]][ ][[None]]*, *[[password]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")][ ][[=]][ ][[False]]*, *[[choices]][[:]][ ][[[List]](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")][ ][[=]][ ][[None]]*, *[[case_sensitive]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")][ ][[=]][ ][[True]]*, *[[show_default]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")][ ][[=]][ ][[True]]*, *[[show_choices]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")][ ][[=]][ ][[True]]*, *[[stream]][[:]][ ][[[TextIO]](https://docs.python.org/3/library/typing.html#typing.TextIO "(in Python v3.13)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)")][ ][[=]][ ][[None]]*[)] [[→] [[PromptType]]]

    :   Shortcut to construct and run a prompt loop and return the result.

        Example

        ::: 
        ::: highlight
            >>> filename = Prompt.ask("Enter a filename")
        :::
        :::

        Parameters[:]

        :   -   **prompt** (*TextType,* *optional*) -- Prompt text. Defaults to "".

            -   **console** ([*Console*](console.html#rich.console.Console "rich.console.Console")*,* *optional*) -- A Console instance or None to use global console. Defaults to None.

            -   **password** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Enable password input. Defaults to False.

            -   **choices** (*List\[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*\],* *optional*) -- A list of valid choices. Defaults to None.

            -   **case_sensitive** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Matching of choices should be case-sensitive. Defaults to True.

            -   **show_default** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Show default in prompt. Defaults to True.

            -   **show_choices** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")*,* *optional*) -- Show choices in prompt. Defaults to True.

            -   **stream** (*TextIO,* *optional*) -- Optional text file open for reading to get input. Defaults to None.

    [[check_choice]][(]*[[value]]*[)][[[\[source\]]]](../_modules/rich/prompt.html#PromptBase.check_choice)[](#rich.prompt.PromptBase.check_choice "Link to this definition")

    :   Check value is in the list of valid choices.

        Parameters[:]

        :   **value** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")) -- Value entered by user.

        Returns[:]

        :   True if choice was valid, otherwise False.

        Return type[:]

        :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")

    *[[classmethod]][ ]*[[get_input]][(]*[[console]]*, *[[prompt]]*, *[[password]]*, *[[stream]][[=]][[None]]*[)][[[\[source\]]]](../_modules/rich/prompt.html#PromptBase.get_input)[](#rich.prompt.PromptBase.get_input "Link to this definition")

    :   Get input from user.

        Parameters[:]

        :   -   **console** ([*Console*](console.html#rich.console.Console "rich.console.Console")) -- Console instance.

            -   **prompt** (*TextType*) -- Prompt text.

            -   **password** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")) -- Enable password entry.

            -   **stream** ([*TextIO*](https://docs.python.org/3/library/typing.html#typing.TextIO "(in Python v3.13)") *\|* *None*)

        Returns[:]

        :   String from user.

        Return type[:]

        :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    [[make_prompt]][(]*[[default]]*[)][[[\[source\]]]](../_modules/rich/prompt.html#PromptBase.make_prompt)[](#rich.prompt.PromptBase.make_prompt "Link to this definition")

    :   Make prompt text.

        Parameters[:]

        :   **default** (*DefaultType*) -- Default value.

        Returns[:]

        :   Text to display in prompt.

        Return type[:]

        :   [Text](text.html#rich.text.Text "rich.text.Text")

    [[on_validate_error]][(]*[[value]]*, *[[error]]*[)][[[\[source\]]]](../_modules/rich/prompt.html#PromptBase.on_validate_error)[](#rich.prompt.PromptBase.on_validate_error "Link to this definition")

    :   Called to handle validation error.

        Parameters[:]

        :   -   **value** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")) -- String entered by user.

            -   **error** ([*InvalidResponse*](#rich.prompt.InvalidResponse "rich.prompt.InvalidResponse")) -- Exception instance the initiated the error.

        Return type[:]

        :   None

    [[pre_prompt]][(][)][[[\[source\]]]](../_modules/rich/prompt.html#PromptBase.pre_prompt)[](#rich.prompt.PromptBase.pre_prompt "Link to this definition")

    :   Hook to display something before the prompt.

        Return type[:]

        :   None

    [[process_response]][(]*[[value]]*[)][[[\[source\]]]](../_modules/rich/prompt.html#PromptBase.process_response)[](#rich.prompt.PromptBase.process_response "Link to this definition")

    :   Process response from user, convert to prompt type.

        Parameters[:]

        :   **value** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")) -- String typed by user.

        Raises[:]

        :   [**InvalidResponse**](#rich.prompt.InvalidResponse "rich.prompt.InvalidResponse") -- If [`value`] is invalid.

        Returns[:]

        :   The value to be returned from ask method.

        Return type[:]

        :   PromptType

    [[render_default]][(]*[[default]]*[)][[[\[source\]]]](../_modules/rich/prompt.html#PromptBase.render_default)[](#rich.prompt.PromptBase.render_default "Link to this definition")

    :   Turn the supplied default in to a Text instance.

        Parameters[:]

        :   **default** (*DefaultType*) -- Default value.

        Returns[:]

        :   Text containing rendering of default value.

        Return type[:]

        :   [Text](text.html#rich.text.Text "rich.text.Text")

    [[response_type]][](#rich.prompt.PromptBase.response_type "Link to this definition")

    :   alias of [[`str`]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

```
<!-- -->
```

*[[exception]][ ]*[[rich.prompt.]][[PromptError]][[[\[source\]]]](../_modules/rich/prompt.html#PromptError)[](#rich.prompt.PromptError "Link to this definition")

:   Exception base class for prompt related errors.

------------------------------------------------------------------------

© Copyright Will McGugan.

Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).