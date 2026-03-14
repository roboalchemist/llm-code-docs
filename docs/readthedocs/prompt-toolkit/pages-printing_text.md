# Printing (and using) formatted text

Prompt_toolkit ships with a
`print_formatted_text()` function that’s meant to
be (as much as possible) compatible with the built-in print function, but on
top of that, also supports colors and formatting.

On Linux systems, this will output VT100 escape sequences, while on Windows it
will use Win32 API calls or VT100 sequences, depending on what is available.

Note

This page is also useful if you’d like to learn how to use formatting
in other places, like in a prompt or a toolbar. Just like
`print_formatted_text()` takes any kind
of “formatted text” as input, prompts and toolbars also accept
“formatted text”.