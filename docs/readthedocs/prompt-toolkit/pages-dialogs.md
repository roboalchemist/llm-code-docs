# Dialogs

Prompt_toolkit ships with a high level API for displaying dialogs, similar to
the Whiptail program, but in pure Python.

## Message box

Use the `message_dialog()` function to display a
simple message box. For instance:

```
from prompt_toolkit.shortcuts import message_dialog

message_dialog(
    title='Example dialog window',
    text='Do you want to continue?\nPress ENTER to quit.').run()

```