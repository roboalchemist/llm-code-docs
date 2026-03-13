# More about key bindings

This page contains a few additional notes about key bindings.

Key bindings can be defined as follows by creating a
`KeyBindings` instance:

```
from prompt_toolkit.key_binding import KeyBindings

bindings = KeyBindings()

@bindings.add('a')
def _(event):
    " Do something if 'a' has been pressed. "
    ...

@bindings.add('c-t')
def _(event):
    " Do something if Control-T has been pressed. "
    ...

```