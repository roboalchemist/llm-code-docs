# Source: https://boltons.readthedocs.io/en/latest/tbutils.html

Title: Tracebacks and call stacks — boltons 25.0.0 documentation

URL Source: https://boltons.readthedocs.io/en/latest/tbutils.html

Markdown Content:
One of the oft-cited tenets of Python is that it is better to ask forgiveness than permission. That is, there are many cases where it is more inclusive and correct to handle exceptions than spend extra lines and execution time checking for conditions. This philosophy makes good exception handling features all the more important. Unfortunately Python’s [`traceback`](https://docs.python.org/3/library/traceback.html#module-traceback "(in Python v3.14)") module is woefully behind the times.

The `tbutils` module provides two disparate but complementary featuresets:

> 1.   With [`ExceptionInfo`](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.ExceptionInfo "boltons.tbutils.ExceptionInfo") and [`TracebackInfo`](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.TracebackInfo "boltons.tbutils.TracebackInfo"), the ability to extract, construct, manipulate, format, and serialize exceptions, tracebacks, and callstacks.
> 
> 2.   With [`ParsedException`](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.ParsedException "boltons.tbutils.ParsedException"), the ability to find and parse tracebacks from captured output such as logs and stdout.

There is also the [`ContextualTracebackInfo`](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.ContextualTracebackInfo "boltons.tbutils.ContextualTracebackInfo") variant of [`TracebackInfo`](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.TracebackInfo "boltons.tbutils.TracebackInfo"), which includes much more information from each frame of the callstack, including values of locals and neighboring lines of code.

_class_ boltons.tbutils.Callpoint(_module\_name_, _module\_path_, _func\_name_, _lineno_, _lasti_, _line=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/tbutils.html#Callpoint)[](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.Callpoint "Link to this definition")
The Callpoint is a lightweight object used to represent a single entry in the code of a call stack. It stores the code-related metadata of a given frame. Available attributes are the same as the parameters below.

Parameters:
*   **func_name** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – the function name

*   **lineno** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – the line number

*   **module_name** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – the module name

*   **module_path** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – the filesystem path of the module

*   **lasti** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – the index of bytecode execution

*   **line** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – the single-line code content (if available)

_classmethod_ from_current(_level=1_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/tbutils.html#Callpoint.from_current)[](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.Callpoint.from_current "Link to this definition")
Creates a Callpoint from the location of the calling function.

_classmethod_ from_frame(_frame_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/tbutils.html#Callpoint.from_frame)[](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.Callpoint.from_frame "Link to this definition")
Create a Callpoint object from data extracted from the given frame.

_classmethod_ from_tb(_tb_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/tbutils.html#Callpoint.from_tb)[](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.Callpoint.from_tb "Link to this definition")
Create a Callpoint from the traceback of the current exception. Main difference with [`from_frame()`](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.Callpoint.from_frame "boltons.tbutils.Callpoint.from_frame") is that `lineno` and `lasti` come from the traceback, which is to say the line that failed in the try block, not the line currently being executed (in the except block).

tb_frame_str()[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/tbutils.html#Callpoint.tb_frame_str)[](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.Callpoint.tb_frame_str "Link to this definition")
Render the Callpoint as it would appear in a standard printed Python traceback. Returns a string with filename, line number, function name, and the actual code line of the error on up to two lines.

to_dict()[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/tbutils.html#Callpoint.to_dict)[](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.Callpoint.to_dict "Link to this definition")
Get a [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") copy of the Callpoint. Useful for serialization.

_class_ boltons.tbutils.ContextualCallpoint(_*a_, _**kw_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/tbutils.html#ContextualCallpoint)[](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.ContextualCallpoint "Link to this definition")
The ContextualCallpoint is a [`Callpoint`](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.Callpoint "boltons.tbutils.Callpoint") subtype with the exact same API and storing two additional values:

> 1.   [`repr()`](https://docs.python.org/3/library/functions.html#repr "(in Python v3.14)") outputs for local variables from the Callpoint’s scope
> 
> 2.   A number of lines before and after the Callpoint’s line of code

The ContextualCallpoint is used by the [`ContextualTracebackInfo`](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.ContextualTracebackInfo "boltons.tbutils.ContextualTracebackInfo").

_classmethod_ from_frame(_frame_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/tbutils.html#ContextualCallpoint.from_frame)[](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.ContextualCallpoint.from_frame "Link to this definition")
Identical to [`Callpoint.from_frame()`](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.Callpoint.from_frame "boltons.tbutils.Callpoint.from_frame")

_classmethod_ from_tb(_tb_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/tbutils.html#ContextualCallpoint.from_tb)[](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.ContextualCallpoint.from_tb "Link to this definition")
Identical to [`Callpoint.from_tb()`](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.Callpoint.from_tb "boltons.tbutils.Callpoint.from_tb")

to_dict()[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/tbutils.html#ContextualCallpoint.to_dict)[](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.ContextualCallpoint.to_dict "Link to this definition")
Same principle as [`Callpoint.to_dict()`](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.Callpoint.to_dict "boltons.tbutils.Callpoint.to_dict"), but with the added contextual values. With `ContextualCallpoint.to_dict()`, each frame will now be represented like:

{'func_name': 'print_example',
 'lineno': 0,
 'module_name': 'example_module',
 'module_path': '/home/example/example_module.pyc',
 'lasti': 0,
 'line': 'print "example"',
 'locals': {'variable': '"value"'},
 'pre_lines': ['variable = "value"'],
 'post_lines': []}

The locals dictionary and line lists are copies and can be mutated freely.

_class_ boltons.tbutils.ContextualExceptionInfo(_exc\_type_, _exc\_msg_, _tb\_info_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/tbutils.html#ContextualExceptionInfo)[](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.ContextualExceptionInfo "Link to this definition")
The ContextualTracebackInfo type is a [`TracebackInfo`](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.TracebackInfo "boltons.tbutils.TracebackInfo") subtype that uses the [`ContextualCallpoint`](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.ContextualCallpoint "boltons.tbutils.ContextualCallpoint") as its frame-representing primitive.

It carries with it most of the exception information required to recreate the widely recognizable “500” page for debugging Django applications.

tb_info_type[](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.ContextualExceptionInfo.tb_info_type "Link to this definition")
alias of [`ContextualTracebackInfo`](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.ContextualTracebackInfo "boltons.tbutils.ContextualTracebackInfo")

_class_ boltons.tbutils.ContextualTracebackInfo(_frames_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/tbutils.html#ContextualTracebackInfo)[](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.ContextualTracebackInfo "Link to this definition")
The ContextualTracebackInfo type is a [`TracebackInfo`](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.TracebackInfo "boltons.tbutils.TracebackInfo") subtype that is used by [`ContextualExceptionInfo`](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.ContextualExceptionInfo "boltons.tbutils.ContextualExceptionInfo") and uses the [`ContextualCallpoint`](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.ContextualCallpoint "boltons.tbutils.ContextualCallpoint") as its frame-representing primitive.

callpoint_type[](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.ContextualTracebackInfo.callpoint_type "Link to this definition")
alias of [`ContextualCallpoint`](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.ContextualCallpoint "boltons.tbutils.ContextualCallpoint")

_class_ boltons.tbutils.ExceptionInfo(_exc\_type_, _exc\_msg_, _tb\_info_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/tbutils.html#ExceptionInfo)[](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.ExceptionInfo "Link to this definition")
An ExceptionInfo object ties together three main fields suitable for representing an instance of an exception: The exception type name, a string representation of the exception itself (the exception message), and information about the traceback (stored as a [`TracebackInfo`](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.TracebackInfo "boltons.tbutils.TracebackInfo") object).

These fields line up with [`sys.exc_info()`](https://docs.python.org/3/library/sys.html#sys.exc_info "(in Python v3.14)"), but unlike the values returned by that function, ExceptionInfo does not hold any references to the real exception or traceback. This property makes it suitable for serialization or long-term retention, without worrying about formatting pitfalls, circular references, or leaking memory.

Parameters:
*   **exc_type** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – The exception type name.

*   **exc_msg** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – String representation of the exception value.

*   **tb_info** ([_TracebackInfo_](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.TracebackInfo "boltons.tbutils.TracebackInfo")) – Information about the stack trace of the exception.

Like the [`TracebackInfo`](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.TracebackInfo "boltons.tbutils.TracebackInfo"), ExceptionInfo is most commonly instantiated from one of its classmethods: [`from_exc_info()`](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.ExceptionInfo.from_exc_info "boltons.tbutils.ExceptionInfo.from_exc_info") or [`from_current()`](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.ExceptionInfo.from_current "boltons.tbutils.ExceptionInfo.from_current").

_classmethod_ from_current()[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/tbutils.html#ExceptionInfo.from_current)[](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.ExceptionInfo.from_current "Link to this definition")
Create an [`ExceptionInfo`](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.ExceptionInfo "boltons.tbutils.ExceptionInfo") object from the current exception being handled, by way of [`sys.exc_info()`](https://docs.python.org/3/library/sys.html#sys.exc_info "(in Python v3.14)"). Will raise an exception if no exception is currently being handled.

_classmethod_ from_exc_info(_exc\_type_, _exc\_value_, _traceback_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/tbutils.html#ExceptionInfo.from_exc_info)[](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.ExceptionInfo.from_exc_info "Link to this definition")
Create an [`ExceptionInfo`](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.ExceptionInfo "boltons.tbutils.ExceptionInfo") object from the exception’s type, value, and traceback, as returned by [`sys.exc_info()`](https://docs.python.org/3/library/sys.html#sys.exc_info "(in Python v3.14)"). See also [`from_current()`](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.ExceptionInfo.from_current "boltons.tbutils.ExceptionInfo.from_current").

get_formatted()[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/tbutils.html#ExceptionInfo.get_formatted)[](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.ExceptionInfo.get_formatted "Link to this definition")
Returns a string formatted in the traditional Python built-in style observable when an exception is not caught. In other words, mimics [`traceback.format_exception()`](https://docs.python.org/3/library/traceback.html#traceback.format_exception "(in Python v3.14)").

tb_info_type[](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.ExceptionInfo.tb_info_type "Link to this definition")
Override this in inherited types to control the TracebackInfo type used

alias of [`TracebackInfo`](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.TracebackInfo "boltons.tbutils.TracebackInfo")

to_dict()[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/tbutils.html#ExceptionInfo.to_dict)[](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.ExceptionInfo.to_dict "Link to this definition")
Get a [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") representation of the ExceptionInfo, suitable for JSON serialization.

_class_ boltons.tbutils.ParsedException(_exc\_type\_name_, _exc\_msg_, _frames=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/tbutils.html#ParsedException)[](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.ParsedException "Link to this definition")
Stores a parsed traceback and exception as would be typically output by [`sys.excepthook()`](https://docs.python.org/3/library/sys.html#sys.excepthook "(in Python v3.14)") or [`traceback.print_exception()`](https://docs.python.org/3/library/traceback.html#traceback.print_exception "(in Python v3.14)").

_classmethod_ from_string(_tb\_str_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/tbutils.html#ParsedException.from_string)[](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.ParsedException.from_string "Link to this definition")
Parse a traceback and exception from the text _tb\_str_. This text is expected to have been decoded, otherwise it will be interpreted as UTF-8.

This method does not search a larger body of text for tracebacks. If the first line of the text passed does not match one of the known patterns, a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") will be raised. This method will ignore trailing text after the end of the first traceback.

Parameters:
**tb_str** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – The traceback text (`unicode` or UTF-8 bytes)

_property_ source_file[](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.ParsedException.source_file "Link to this definition")
The file path of module containing the function that raised the exception, or None if not available.

to_dict()[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/tbutils.html#ParsedException.to_dict)[](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.ParsedException.to_dict "Link to this definition")
Get a copy as a JSON-serializable [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)").

to_string()[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/tbutils.html#ParsedException.to_string)[](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.ParsedException.to_string "Link to this definition")
Formats the exception and its traceback into the standard format, as returned by the traceback module.

`ParsedException.from_string(text).to_string()` should yield `text`.

Note

Note that this method does not output “anchors” (e.g., `~~~~~^^`), as were added in Python 3.13. See the built-in `traceback` module if these are necessary.

_class_ boltons.tbutils.TracebackInfo(_frames_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/tbutils.html#TracebackInfo)[](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.TracebackInfo "Link to this definition")
The TracebackInfo class provides a basic representation of a stack trace, be it from an exception being handled or just part of normal execution. It is basically a wrapper around a list of [`Callpoint`](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.Callpoint "boltons.tbutils.Callpoint") objects representing frames.

Parameters:
**frames** ([_list_](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")) – A list of frame objects in the stack.

Note

`TracebackInfo` can represent both exception tracebacks and non-exception tracebacks (aka stack traces). As a result, there is no `TracebackInfo.from_current()`, as that would be ambiguous. Instead, call [`TracebackInfo.from_frame()`](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.TracebackInfo.from_frame "boltons.tbutils.TracebackInfo.from_frame") without the _frame_ argument for a stack trace, or [`TracebackInfo.from_traceback()`](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.TracebackInfo.from_traceback "boltons.tbutils.TracebackInfo.from_traceback") without the _tb_ argument for an exception traceback.

callpoint_type[](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.TracebackInfo.callpoint_type "Link to this definition")
alias of [`Callpoint`](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.Callpoint "boltons.tbutils.Callpoint")

_classmethod_ from_dict(_d_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/tbutils.html#TracebackInfo.from_dict)[](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.TracebackInfo.from_dict "Link to this definition")
Complements [`TracebackInfo.to_dict()`](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.TracebackInfo.to_dict "boltons.tbutils.TracebackInfo.to_dict").

_classmethod_ from_frame(_frame=None_, _level=1_, _limit=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/tbutils.html#TracebackInfo.from_frame)[](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.TracebackInfo.from_frame "Link to this definition")
Create a new TracebackInfo _frame_ by recurring up in the stack a max of _limit_ times. If _frame_ is unset, get the frame from [`sys._getframe()`](https://docs.python.org/3/library/sys.html#sys._getframe "(in Python v3.14)") using _level_.

Parameters:
*   **frame** (_types.FrameType_) – frame object from [`sys._getframe()`](https://docs.python.org/3/library/sys.html#sys._getframe "(in Python v3.14)") or elsewhere. Defaults to result of `sys.get_frame()`.

*   **level** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – If _frame_ is unset, the desired frame is this many levels up the stack from the invocation of this method. Default `1` (i.e., caller of this method).

*   **limit** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – max number of parent frames to extract (defaults to [`sys.tracebacklimit`](https://docs.python.org/3/library/sys.html#sys.tracebacklimit "(in Python v3.14)"))

_classmethod_ from_traceback(_tb=None_, _limit=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/tbutils.html#TracebackInfo.from_traceback)[](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.TracebackInfo.from_traceback "Link to this definition")
Create a new TracebackInfo from the traceback _tb_ by recurring up in the stack a max of _limit_ times. If _tb_ is unset, get the traceback from the currently handled exception. If no exception is being handled, raise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)").

Parameters:
*   **frame** ([_types.TracebackType_](https://docs.python.org/3/library/types.html#types.TracebackType "(in Python v3.14)")) – traceback object from [`sys.exc_info()`](https://docs.python.org/3/library/sys.html#sys.exc_info "(in Python v3.14)") or elsewhere. If absent or set to `None`, defaults to `sys.exc_info()[2]`, and raises a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") if no exception is currently being handled.

*   **limit** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – max number of parent frames to extract (defaults to [`sys.tracebacklimit`](https://docs.python.org/3/library/sys.html#sys.tracebacklimit "(in Python v3.14)"))

get_formatted()[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/tbutils.html#TracebackInfo.get_formatted)[](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.TracebackInfo.get_formatted "Link to this definition")
Returns a string as formatted in the traditional Python built-in style observable when an exception is not caught. In other words, mimics [`traceback.format_tb()`](https://docs.python.org/3/library/traceback.html#traceback.format_tb "(in Python v3.14)") and [`traceback.format_stack()`](https://docs.python.org/3/library/traceback.html#traceback.format_stack "(in Python v3.14)").

to_dict()[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/tbutils.html#TracebackInfo.to_dict)[](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.TracebackInfo.to_dict "Link to this definition")
Returns a dict with a list of [`Callpoint`](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.Callpoint "boltons.tbutils.Callpoint") frames converted to dicts.

boltons.tbutils.print_exception(_etype_, _value_, _tb_, _limit=None_, _file=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/tbutils.html#print_exception)[](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.print_exception "Link to this definition")
Print exception up to ‘limit’ stack trace entries from ‘tb’ to ‘file’.

This differs from print_tb() in the following ways: (1) if traceback is not None, it prints a header “Traceback (most recent call last):”; (2) it prints the exception type and value after the stack trace; (3) if type is SyntaxError and value has the appropriate format, it prints the line where the syntax error occurred with a caret on the next line indicating the approximate position of the error.
