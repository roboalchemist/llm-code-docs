:github_url: hide



# EngineDebugger

**Inherits:** [Object<class_Object>]

Exposes the internal debugger.


## Description

**EngineDebugger** handles the communication between the editor and the running game. It is active in the running game. Messages can be sent/received through it. It also manages the profilers.


## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                  | :ref:`clear_breakpoints<class_EngineDebugger_method_clear_breakpoints>`\ (\ )                                                                                                                                                     |
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                  | :ref:`debug<class_EngineDebugger_method_debug>`\ (\ can_continue\: :ref:`bool<class_bool>` = true, is_error_breakpoint\: :ref:`bool<class_bool>` = false\ )                                                                       |
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`   | :ref:`get_depth<class_EngineDebugger_method_get_depth>`\ (\ ) |const|                                                                                                                                                             |
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`   | :ref:`get_lines_left<class_EngineDebugger_method_get_lines_left>`\ (\ ) |const|                                                                                                                                                   |
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`has_capture<class_EngineDebugger_method_has_capture>`\ (\ name\: :ref:`StringName<class_StringName>`\ )                                                                                                                     |
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`has_profiler<class_EngineDebugger_method_has_profiler>`\ (\ name\: :ref:`StringName<class_StringName>`\ )                                                                                                                   |
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                  | :ref:`insert_breakpoint<class_EngineDebugger_method_insert_breakpoint>`\ (\ line\: :ref:`int<class_int>`, source\: :ref:`StringName<class_StringName>`\ )                                                                         |
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`is_active<class_EngineDebugger_method_is_active>`\ (\ )                                                                                                                                                                     |
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`is_breakpoint<class_EngineDebugger_method_is_breakpoint>`\ (\ line\: :ref:`int<class_int>`, source\: :ref:`StringName<class_StringName>`\ ) |const|                                                                         |
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`is_profiling<class_EngineDebugger_method_is_profiling>`\ (\ name\: :ref:`StringName<class_StringName>`\ )                                                                                                                   |
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`is_skipping_breakpoints<class_EngineDebugger_method_is_skipping_breakpoints>`\ (\ ) |const|                                                                                                                                 |
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                  | :ref:`line_poll<class_EngineDebugger_method_line_poll>`\ (\ )                                                                                                                                                                     |
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                  | :ref:`profiler_add_frame_data<class_EngineDebugger_method_profiler_add_frame_data>`\ (\ name\: :ref:`StringName<class_StringName>`, data\: :ref:`Array<class_Array>`\ )                                                           |
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                  | :ref:`profiler_enable<class_EngineDebugger_method_profiler_enable>`\ (\ name\: :ref:`StringName<class_StringName>`, enable\: :ref:`bool<class_bool>`, arguments\: :ref:`Array<class_Array>` = []\ )                               |
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                  | :ref:`register_message_capture<class_EngineDebugger_method_register_message_capture>`\ (\ name\: :ref:`StringName<class_StringName>`, callable\: :ref:`Callable<class_Callable>`\ )                                               |
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                  | :ref:`register_profiler<class_EngineDebugger_method_register_profiler>`\ (\ name\: :ref:`StringName<class_StringName>`, profiler\: :ref:`EngineProfiler<class_EngineProfiler>`\ )                                                 |
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                  | :ref:`remove_breakpoint<class_EngineDebugger_method_remove_breakpoint>`\ (\ line\: :ref:`int<class_int>`, source\: :ref:`StringName<class_StringName>`\ )                                                                         |
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                  | :ref:`script_debug<class_EngineDebugger_method_script_debug>`\ (\ language\: :ref:`ScriptLanguage<class_ScriptLanguage>`, can_continue\: :ref:`bool<class_bool>` = true, is_error_breakpoint\: :ref:`bool<class_bool>` = false\ ) |
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                  | :ref:`send_message<class_EngineDebugger_method_send_message>`\ (\ message\: :ref:`String<class_String>`, data\: :ref:`Array<class_Array>`\ )                                                                                      |
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                  | :ref:`set_depth<class_EngineDebugger_method_set_depth>`\ (\ depth\: :ref:`int<class_int>`\ )                                                                                                                                      |
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                  | :ref:`set_lines_left<class_EngineDebugger_method_set_lines_left>`\ (\ lines\: :ref:`int<class_int>`\ )                                                                                                                            |
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                  | :ref:`unregister_message_capture<class_EngineDebugger_method_unregister_message_capture>`\ (\ name\: :ref:`StringName<class_StringName>`\ )                                                                                       |
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                  | :ref:`unregister_profiler<class_EngineDebugger_method_unregister_profiler>`\ (\ name\: :ref:`StringName<class_StringName>`\ )                                                                                                     |
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



|void| **clear_breakpoints**\ (\ ) [🔗<class_EngineDebugger_method_clear_breakpoints>]

Clears all breakpoints.


----



|void| **debug**\ (\ can_continue\: [bool<class_bool>] = true, is_error_breakpoint\: [bool<class_bool>] = false\ ) [🔗<class_EngineDebugger_method_debug>]

Starts a debug break in script execution, optionally specifying whether the program can continue based on `can_continue` and whether the break was due to a breakpoint.


----



[int<class_int>] **get_depth**\ (\ ) |const| [🔗<class_EngineDebugger_method_get_depth>]

**Experimental:** This method may be changed or removed in future versions.

Returns the current debug depth.


----



[int<class_int>] **get_lines_left**\ (\ ) |const| [🔗<class_EngineDebugger_method_get_lines_left>]

**Experimental:** This method may be changed or removed in future versions.

Returns the number of lines that remain.


----



[bool<class_bool>] **has_capture**\ (\ name\: [StringName<class_StringName>]\ ) [🔗<class_EngineDebugger_method_has_capture>]

Returns `true` if a capture with the given name is present otherwise `false`.


----



[bool<class_bool>] **has_profiler**\ (\ name\: [StringName<class_StringName>]\ ) [🔗<class_EngineDebugger_method_has_profiler>]

Returns `true` if a profiler with the given name is present otherwise `false`.


----



|void| **insert_breakpoint**\ (\ line\: [int<class_int>], source\: [StringName<class_StringName>]\ ) [🔗<class_EngineDebugger_method_insert_breakpoint>]

Inserts a new breakpoint with the given `source` and `line`.


----



[bool<class_bool>] **is_active**\ (\ ) [🔗<class_EngineDebugger_method_is_active>]

Returns `true` if the debugger is active otherwise `false`.


----



[bool<class_bool>] **is_breakpoint**\ (\ line\: [int<class_int>], source\: [StringName<class_StringName>]\ ) |const| [🔗<class_EngineDebugger_method_is_breakpoint>]

Returns `true` if the given `source` and `line` represent an existing breakpoint.


----



[bool<class_bool>] **is_profiling**\ (\ name\: [StringName<class_StringName>]\ ) [🔗<class_EngineDebugger_method_is_profiling>]

Returns `true` if a profiler with the given name is present and active otherwise `false`.


----



[bool<class_bool>] **is_skipping_breakpoints**\ (\ ) |const| [🔗<class_EngineDebugger_method_is_skipping_breakpoints>]

Returns `true` if the debugger is skipping breakpoints otherwise `false`.


----



|void| **line_poll**\ (\ ) [🔗<class_EngineDebugger_method_line_poll>]

Forces a processing loop of debugger events. The purpose of this method is just processing events every now and then when the script might get too busy, so that bugs like infinite loops can be caught.


----



|void| **profiler_add_frame_data**\ (\ name\: [StringName<class_StringName>], data\: [Array<class_Array>]\ ) [🔗<class_EngineDebugger_method_profiler_add_frame_data>]

Calls the `add` callable of the profiler with given `name` and `data`.


----



|void| **profiler_enable**\ (\ name\: [StringName<class_StringName>], enable\: [bool<class_bool>], arguments\: [Array<class_Array>] = []\ ) [🔗<class_EngineDebugger_method_profiler_enable>]

Calls the `toggle` callable of the profiler with given `name` and `arguments`. Enables/Disables the same profiler depending on `enable` argument.


----



|void| **register_message_capture**\ (\ name\: [StringName<class_StringName>], callable\: [Callable<class_Callable>]\ ) [🔗<class_EngineDebugger_method_register_message_capture>]

Registers a message capture with given `name`. If `name` is "my_message" then messages starting with "my_message:" will be called with the given callable.

The callable must accept a message string and a data array as argument. The callable should return `true` if the message is recognized.

\ **Note:** The callable will receive the message with the prefix stripped, unlike [EditorDebuggerPlugin._capture()<class_EditorDebuggerPlugin_private_method__capture>]. See the [EditorDebuggerPlugin<class_EditorDebuggerPlugin>] description for an example.


----



|void| **register_profiler**\ (\ name\: [StringName<class_StringName>], profiler\: [EngineProfiler<class_EngineProfiler>]\ ) [🔗<class_EngineDebugger_method_register_profiler>]

Registers a profiler with the given `name`. See [EngineProfiler<class_EngineProfiler>] for more information.


----



|void| **remove_breakpoint**\ (\ line\: [int<class_int>], source\: [StringName<class_StringName>]\ ) [🔗<class_EngineDebugger_method_remove_breakpoint>]

Removes a breakpoint with the given `source` and `line`.


----



|void| **script_debug**\ (\ language\: [ScriptLanguage<class_ScriptLanguage>], can_continue\: [bool<class_bool>] = true, is_error_breakpoint\: [bool<class_bool>] = false\ ) [🔗<class_EngineDebugger_method_script_debug>]

Starts a debug break in script execution, optionally specifying whether the program can continue based on `can_continue` and whether the break was due to a breakpoint.


----



|void| **send_message**\ (\ message\: [String<class_String>], data\: [Array<class_Array>]\ ) [🔗<class_EngineDebugger_method_send_message>]

Sends a message with given `message` and `data` array.


----



|void| **set_depth**\ (\ depth\: [int<class_int>]\ ) [🔗<class_EngineDebugger_method_set_depth>]

**Experimental:** This method may be changed or removed in future versions.

Sets the current debugging depth.


----



|void| **set_lines_left**\ (\ lines\: [int<class_int>]\ ) [🔗<class_EngineDebugger_method_set_lines_left>]

**Experimental:** This method may be changed or removed in future versions.

Sets the current debugging lines that remain.


----



|void| **unregister_message_capture**\ (\ name\: [StringName<class_StringName>]\ ) [🔗<class_EngineDebugger_method_unregister_message_capture>]

Unregisters the message capture with given `name`.


----



|void| **unregister_profiler**\ (\ name\: [StringName<class_StringName>]\ ) [🔗<class_EngineDebugger_method_unregister_profiler>]

Unregisters a profiler with given `name`.

