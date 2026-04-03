:github_url: hide



# Logger

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Custom logger to receive messages from the internal error/warning stream.


## Description

Custom logger to receive messages from the internal error/warning stream. Loggers are registered via [OS.add_logger()<class_OS_method_add_logger>].


## Methods

> **TABLE**
> :widths: auto
>
> +--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`_log_error<class_Logger_private_method__log_error>`\ (\ function\: :ref:`String<class_String>`, file\: :ref:`String<class_String>`, line\: :ref:`int<class_int>`, code\: :ref:`String<class_String>`, rationale\: :ref:`String<class_String>`, editor_notify\: :ref:`bool<class_bool>`, error_type\: :ref:`int<class_int>`, script_backtraces\: :ref:`Array<class_Array>`\[:ref:`ScriptBacktrace<class_ScriptBacktrace>`\]\ ) |virtual| |
> +--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`_log_message<class_Logger_private_method__log_message>`\ (\ message\: :ref:`String<class_String>`, error\: :ref:`bool<class_bool>`\ ) |virtual|                                                                                                                                                                                                                                                                                         |
> +--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **ErrorType**: [🔗<enum_Logger_ErrorType>]



[ErrorType<enum_Logger_ErrorType>] **ERROR_TYPE_ERROR** = `0`

The message received is an error.



[ErrorType<enum_Logger_ErrorType>] **ERROR_TYPE_WARNING** = `1`

The message received is a warning.



[ErrorType<enum_Logger_ErrorType>] **ERROR_TYPE_SCRIPT** = `2`

The message received is a script error.



[ErrorType<enum_Logger_ErrorType>] **ERROR_TYPE_SHADER** = `3`

The message received is a shader error.


----


## Method Descriptions



|void| **_log_error**\ (\ function\: [String<class_String>], file\: [String<class_String>], line\: [int<class_int>], code\: [String<class_String>], rationale\: [String<class_String>], editor_notify\: [bool<class_bool>], error_type\: [int<class_int>], script_backtraces\: [Array<class_Array>]\[[ScriptBacktrace<class_ScriptBacktrace>]\]\ ) |virtual| [🔗<class_Logger_private_method__log_error>]

Called when an error is logged. The error provides the `function`, `file`, and `line` that it originated from, as well as either the `code` that generated the error or a `rationale`.

The type of error provided by `error_type` is described in the [ErrorType<enum_Logger_ErrorType>] enumeration.

Additionally, `script_backtraces` provides backtraces for each of the script languages. These will only contain stack frames in editor builds and debug builds by default. To enable them for release builds as well, you need to enable [ProjectSettings.debug/settings/gdscript/always_track_call_stacks<class_ProjectSettings_property_debug/settings/gdscript/always_track_call_stacks>].

\ **Warning:** This method will be called from threads other than the main thread, possibly at the same time, so you will need to have some kind of thread-safety in your implementation of it, like a [Mutex<class_Mutex>].

\ **Note:** `script_backtraces` will not contain any captured variables, due to its prohibitively high cost. To get those you will need to capture the backtraces yourself, from within the **Logger** virtual methods, using [Engine.capture_script_backtraces()<class_Engine_method_capture_script_backtraces>].

\ **Note:** Logging errors from this method using functions like [@GlobalScope.push_error()<class_@GlobalScope_method_push_error>] or [@GlobalScope.push_warning()<class_@GlobalScope_method_push_warning>] is not supported, as it could cause infinite recursion. These errors will only show up in the console output.


----



|void| **_log_message**\ (\ message\: [String<class_String>], error\: [bool<class_bool>]\ ) |virtual| [🔗<class_Logger_private_method__log_message>]

Called when a message is logged. If `error` is `true`, then this message was meant to be sent to `stderr`.

\ **Warning:** This method will be called from threads other than the main thread, possibly at the same time, so you will need to have some kind of thread-safety in your implementation of it, like a [Mutex<class_Mutex>].

\ **Note:** Logging another message from this method using functions like [@GlobalScope.print()<class_@GlobalScope_method_print>] is not supported, as it could cause infinite recursion. These messages will only show up in the console output.

