# Asking for input (prompts)

This page is about building prompts. Pieces of code that we can embed in a
program for asking the user for input. Even if you want to use prompt_toolkit
for building full screen terminal applications, it is probably still a good
idea to read this first, before heading to the building full screen
applications page.

In this page, we will cover autocompletion, syntax highlighting, key bindings,
and so on.

## Hello world

The following snippet is the most simple example, it uses the
`prompt()` function to ask the user for input
and returns the text. Just like `(raw_)input`.

```
from prompt_toolkit import prompt

text = prompt("Give me some input: ")
print(f"You said: {text}")

```