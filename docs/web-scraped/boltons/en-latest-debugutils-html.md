# Source: https://boltons.readthedocs.io/en/latest/debugutils.html

Title: Debugging utilities — boltons 25.0.0 documentation

URL Source: https://boltons.readthedocs.io/en/latest/debugutils.html

Markdown Content:
`debugutils` - Debugging utilities[](https://boltons.readthedocs.io/en/latest/debugutils.html#module-boltons.debugutils "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------

A small set of utilities useful for debugging misbehaving applications. Currently this focuses on ways to use [`pdb`](https://docs.python.org/3/library/pdb.html#module-pdb "(in Python v3.14)"), the built-in Python debugger.

boltons.debugutils.pdb_on_exception(_limit=100_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/debugutils.html#pdb_on_exception)[](https://boltons.readthedocs.io/en/latest/debugutils.html#boltons.debugutils.pdb_on_exception "Link to this definition")
Installs a handler which, instead of exiting, attaches a post-mortem pdb console whenever an unhandled exception is encountered.

Parameters:
**limit** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – the max number of stack frames to display when printing the traceback

A similar effect can be achieved from the command-line using the following command:

python -m pdb your_code.py

But `pdb_on_exception` allows you to do this conditionally and within your application. To restore default behavior, just do:

sys.excepthook = sys. __excepthook__ 

boltons.debugutils.pdb_on_signal(_signalnum=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/debugutils.html#pdb_on_signal)[](https://boltons.readthedocs.io/en/latest/debugutils.html#boltons.debugutils.pdb_on_signal "Link to this definition")
Installs a signal handler for _signalnum_, which defaults to `SIGINT`, or keyboard interrupt/ctrl-c. This signal handler launches a [`pdb`](https://docs.python.org/3/library/pdb.html#module-pdb "(in Python v3.14)") breakpoint. Results vary in concurrent systems, but this technique can be useful for debugging infinite loops, or easily getting into deep call stacks.

Parameters:
**signalnum** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – The signal number of the signal to handle with pdb. Defaults to `signal.SIGINT`, see [`signal`](https://docs.python.org/3/library/signal.html#module-signal "(in Python v3.14)") for more information.

boltons.debugutils.wrap_trace(_obj_, _hook=<function trace\_print\_hook>_, _which=None_, _events=None_, _label=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/debugutils.html#wrap_trace)[](https://boltons.readthedocs.io/en/latest/debugutils.html#boltons.debugutils.wrap_trace "Link to this definition")
Monitor an object for interactions. Whenever code calls a method, gets an attribute, or sets an attribute, an event is called. By default the trace output is printed, but a custom tracing _hook_ can be passed.

Parameters:
*   **obj** ([_object_](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")) – New- or old-style object to be traced. Built-in objects like lists and dicts also supported.

*   **hook** (_callable_) – A function called once for every event. See below for details.

*   **which** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – One or more attribute names to trace, or a function accepting attribute name and value, and returning True/False.

*   **events** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – One or more kinds of events to call _hook_ on. Expected values are 
```
['get', 'set', 'del', 'call',
'raise', 'return']
```
. Defaults to all events.

*   **label** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – A name to associate with the traced object Defaults to hexadecimal memory address, similar to repr.

The object returned is not the same object as the one passed in. It will not pass identity checks. However, it will pass [`isinstance()`](https://docs.python.org/3/library/functions.html#isinstance "(in Python v3.14)") checks, as it is a new instance of a new subtype of the object passed.
