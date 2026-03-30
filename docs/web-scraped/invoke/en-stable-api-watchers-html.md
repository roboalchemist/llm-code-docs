# Source: https://docs.pyinvoke.org/en/stable/api/watchers.html

Title: watchers — Invoke documentation

URL Source: https://docs.pyinvoke.org/en/stable/api/watchers.html

Markdown Content:
_class_ invoke.watchers.FailingResponder(_pattern:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_, _response:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_, _sentinel:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_)[¶](https://docs.pyinvoke.org/en/stable/api/watchers.html#invoke.watchers.FailingResponder "Permalink to this definition")
Variant of [`Responder`](https://docs.pyinvoke.org/en/stable/api/watchers.html#invoke.watchers.Responder "invoke.watchers.Responder") which is capable of detecting incorrect responses.

This class adds a `sentinel` parameter to `__init__`, and its `submit` will raise [`ResponseNotAccepted`](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.ResponseNotAccepted "invoke.exceptions.ResponseNotAccepted") if it detects that sentinel value in the stream.

New in version 1.0.

 __init__ (_pattern:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_, _response:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_, _sentinel:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/watchers.html#invoke.watchers.FailingResponder.__init__ "Permalink to this definition")
Imprint this [`Responder`](https://docs.pyinvoke.org/en/stable/api/watchers.html#invoke.watchers.Responder "invoke.watchers.Responder") with necessary parameters.

Parameters
*   **pattern** – A raw string (e.g. `r"\[sudo\] password for .*:"`) which will be turned into a regular expression.

*   **response** – The string to submit to the subprocess’ stdin when `pattern` is detected.

submit(_stream:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_)→Generator[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)"),[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")][¶](https://docs.pyinvoke.org/en/stable/api/watchers.html#invoke.watchers.FailingResponder.submit "Permalink to this definition")
Act on `stream` data, potentially returning responses.

Parameters
**stream** ([_str_](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")) – All data read on this stream since the beginning of the session.

Returns
An iterable of `str` (which may be empty).

New in version 1.0.

_class_ invoke.watchers.Responder(_pattern:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_, _response:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_)[¶](https://docs.pyinvoke.org/en/stable/api/watchers.html#invoke.watchers.Responder "Permalink to this definition")
A parameterizable object that submits responses to specific patterns.

Commonly used to implement password auto-responds for things like `sudo`.

New in version 1.0.

 __init__ (_pattern:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_, _response:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/watchers.html#invoke.watchers.Responder.__init__ "Permalink to this definition")
Imprint this [`Responder`](https://docs.pyinvoke.org/en/stable/api/watchers.html#invoke.watchers.Responder "invoke.watchers.Responder") with necessary parameters.

Parameters
*   **pattern** – A raw string (e.g. `r"\[sudo\] password for .*:"`) which will be turned into a regular expression.

*   **response** – The string to submit to the subprocess’ stdin when `pattern` is detected.

pattern_matches(_stream:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_, _pattern:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_, _index\_attr:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_)→Iterable[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")][¶](https://docs.pyinvoke.org/en/stable/api/watchers.html#invoke.watchers.Responder.pattern_matches "Permalink to this definition")
Generic “search for pattern in stream, using index” behavior.

Used here and in some subclasses that want to track multiple patterns concurrently.

Parameters
*   **stream** ([_str_](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")) – The same data passed to `submit`.

*   **pattern** ([_str_](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")) – The pattern to search for.

*   **index_attr** ([_str_](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")) – The name of the index attribute to use.

Returns
An iterable of string matches.

New in version 1.0.

submit(_stream:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_)→Generator[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)"),[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)"),[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")][¶](https://docs.pyinvoke.org/en/stable/api/watchers.html#invoke.watchers.Responder.submit "Permalink to this definition")
Act on `stream` data, potentially returning responses.

Parameters
**stream** ([_str_](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")) – All data read on this stream since the beginning of the session.

Returns
An iterable of `str` (which may be empty).

New in version 1.0.

_class_ invoke.watchers.StreamWatcher[¶](https://docs.pyinvoke.org/en/stable/api/watchers.html#invoke.watchers.StreamWatcher "Permalink to this definition")
A class whose subclasses may act on seen stream data from subprocesses.

Subclasses must exhibit the following API; see [`Responder`](https://docs.pyinvoke.org/en/stable/api/watchers.html#invoke.watchers.Responder "invoke.watchers.Responder") for a concrete example.

*   `__init__` is completely up to each subclass, though as usual, subclasses _of_ subclasses should be careful to make use of [`super`](https://docs.python.org/2.7/library/functions.html#super "(in Python v2.7)") where appropriate.

*   [`submit`](https://docs.pyinvoke.org/en/stable/api/watchers.html#invoke.watchers.StreamWatcher.submit "invoke.watchers.StreamWatcher.submit") must accept the entire current contents of the stream being watched, as a string, and may optionally return an iterable of strings (or act as a generator iterator, i.e. multiple calls to 
```
yield
<string>
```
), which will each be written to the subprocess’ standard input.

Note

[`StreamWatcher`](https://docs.pyinvoke.org/en/stable/api/watchers.html#invoke.watchers.StreamWatcher "invoke.watchers.StreamWatcher") subclasses exist in part to enable state tracking, such as detecting when a submitted password didn’t work & erroring (or prompting a user, or etc). Such bookkeeping isn’t easily achievable with simple callback functions.

Note

[`StreamWatcher`](https://docs.pyinvoke.org/en/stable/api/watchers.html#invoke.watchers.StreamWatcher "invoke.watchers.StreamWatcher") subclasses [`threading.local`](https://docs.python.org/2.7/library/threading.html#threading.local "(in Python v2.7)") so that its instances can be used to ‘watch’ both subprocess stdout and stderr in separate threads.

New in version 1.0.

submit(_stream:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_)→Iterable[[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")][¶](https://docs.pyinvoke.org/en/stable/api/watchers.html#invoke.watchers.StreamWatcher.submit "Permalink to this definition")
Act on `stream` data, potentially returning responses.

Parameters
**stream** ([_str_](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")) – All data read on this stream since the beginning of the session.

Returns
An iterable of `str` (which may be empty).

New in version 1.0.
