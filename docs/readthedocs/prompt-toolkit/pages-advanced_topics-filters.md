# Filters

Many places in prompt_toolkit require a boolean value that can change over
time. For instance:

- 

to specify whether a part of the layout needs to be visible or not;

- 

or to decide whether a certain key binding needs to be active or not;

- 

or the `wrap_lines` option of
`BufferControl`;

- 

etcetera.

These booleans are often dynamic and can change at runtime. For instance, the
search toolbar should only be visible when the user is actually searching (when
the search buffer has the focus). The `wrap_lines` option could be changed
with a certain key binding. And that key binding could only work when the
default buffer got the focus.

In prompt_toolkit, we decided to reduce the amount of state in the whole
framework, and apply a simple kind of reactive programming to describe the flow
of these booleans as expressions. (It’s one-way only: if a key binding needs to
know whether it’s active or not, it can follow this flow by evaluating an
expression.)

The (abstract) base class is `Filter`, which
wraps an expression that takes no input and evaluates to a boolean. Getting the
state of a filter is done by simply calling it.

## An example

The most obvious way to create such a `Filter`
instance is by creating a `Condition` instance
from a function. For instance, the following condition will evaluate to
`True` when the user is searching:

```
from prompt_toolkit.application.current import get_app
from prompt_toolkit.filters import Condition

is_searching = Condition(lambda: get_app().is_searching)

```