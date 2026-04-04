:github_url: hide



# EditorDebuggerSession

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A class to interact with the editor debugger.


## Description

This class cannot be directly instantiated and must be retrieved via an [EditorDebuggerPlugin<class_EditorDebuggerPlugin>].

You can add tabs to the session UI via [add_session_tab()<class_EditorDebuggerSession_method_add_session_tab>], send messages via [send_message()<class_EditorDebuggerSession_method_send_message>], and toggle [EngineProfiler<class_EngineProfiler>]\ s via [toggle_profiler()<class_EditorDebuggerSession_method_toggle_profiler>].


## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                  | :ref:`add_session_tab<class_EditorDebuggerSession_method_add_session_tab>`\ (\ control\: :ref:`Control<class_Control>`\ )                                                                         |
> +-------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`is_active<class_EditorDebuggerSession_method_is_active>`\ (\ )                                                                                                                              |
> +-------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`is_breaked<class_EditorDebuggerSession_method_is_breaked>`\ (\ )                                                                                                                            |
> +-------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`is_debuggable<class_EditorDebuggerSession_method_is_debuggable>`\ (\ )                                                                                                                      |
> +-------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                  | :ref:`remove_session_tab<class_EditorDebuggerSession_method_remove_session_tab>`\ (\ control\: :ref:`Control<class_Control>`\ )                                                                   |
> +-------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                  | :ref:`send_message<class_EditorDebuggerSession_method_send_message>`\ (\ message\: :ref:`String<class_String>`, data\: :ref:`Array<class_Array>` = []\ )                                          |
> +-------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                  | :ref:`set_breakpoint<class_EditorDebuggerSession_method_set_breakpoint>`\ (\ path\: :ref:`String<class_String>`, line\: :ref:`int<class_int>`, enabled\: :ref:`bool<class_bool>`\ )               |
> +-------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                  | :ref:`toggle_profiler<class_EditorDebuggerSession_method_toggle_profiler>`\ (\ profiler\: :ref:`String<class_String>`, enable\: :ref:`bool<class_bool>`, data\: :ref:`Array<class_Array>` = []\ ) |
> +-------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**breaked**\ (\ can_debug\: [bool<class_bool>]\ ) [🔗<class_EditorDebuggerSession_signal_breaked>]

Emitted when the attached remote instance enters a break state. If `can_debug` is `true`, the remote instance will enter the debug loop.


----



**continued**\ (\ ) [🔗<class_EditorDebuggerSession_signal_continued>]

Emitted when the attached remote instance exits a break state.


----



**started**\ (\ ) [🔗<class_EditorDebuggerSession_signal_started>]

Emitted when a remote instance is attached to this session (i.e. the session becomes active).


----



**stopped**\ (\ ) [🔗<class_EditorDebuggerSession_signal_stopped>]

Emitted when a remote instance is detached from this session (i.e. the session becomes inactive).


----


## Method Descriptions



|void| **add_session_tab**\ (\ control\: [Control<class_Control>]\ ) [🔗<class_EditorDebuggerSession_method_add_session_tab>]

Adds the given `control` to the debug session UI in the debugger bottom panel. The `control`'s node name will be used as the tab title.


----



[bool<class_bool>] **is_active**\ (\ ) [🔗<class_EditorDebuggerSession_method_is_active>]

Returns `true` if the debug session is currently attached to a remote instance.


----



[bool<class_bool>] **is_breaked**\ (\ ) [🔗<class_EditorDebuggerSession_method_is_breaked>]

Returns `true` if the attached remote instance is currently in the debug loop.


----



[bool<class_bool>] **is_debuggable**\ (\ ) [🔗<class_EditorDebuggerSession_method_is_debuggable>]

Returns `true` if the attached remote instance can be debugged.


----



|void| **remove_session_tab**\ (\ control\: [Control<class_Control>]\ ) [🔗<class_EditorDebuggerSession_method_remove_session_tab>]

Removes the given `control` from the debug session UI in the debugger bottom panel.


----



|void| **send_message**\ (\ message\: [String<class_String>], data\: [Array<class_Array>] = []\ ) [🔗<class_EditorDebuggerSession_method_send_message>]

Sends the given `message` to the attached remote instance, optionally passing additionally `data`. See [EngineDebugger<class_EngineDebugger>] for how to retrieve those messages.


----



|void| **set_breakpoint**\ (\ path\: [String<class_String>], line\: [int<class_int>], enabled\: [bool<class_bool>]\ ) [🔗<class_EditorDebuggerSession_method_set_breakpoint>]

Enables or disables a specific breakpoint based on `enabled`, updating the Editor Breakpoint Panel accordingly.


----



|void| **toggle_profiler**\ (\ profiler\: [String<class_String>], enable\: [bool<class_bool>], data\: [Array<class_Array>] = []\ ) [🔗<class_EditorDebuggerSession_method_toggle_profiler>]

Toggle the given `profiler` on the attached remote instance, optionally passing additionally `data`. See [EngineProfiler<class_EngineProfiler>] for more details.

