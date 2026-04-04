:github_url: hide



# EditorDebuggerPlugin

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A base class to implement debugger plugins.


## Description

**EditorDebuggerPlugin** provides functions related to the editor side of the debugger.

To interact with the debugger, an instance of this class must be added to the editor via [EditorPlugin.add_debugger_plugin()<class_EditorPlugin_method_add_debugger_plugin>].

Once added, the [_setup_session()<class_EditorDebuggerPlugin_private_method__setup_session>] callback will be called for every [EditorDebuggerSession<class_EditorDebuggerSession>] available to the plugin, and when new ones are created (the sessions may be inactive during this stage).

You can retrieve the available [EditorDebuggerSession<class_EditorDebuggerSession>]\ s via [get_sessions()<class_EditorDebuggerPlugin_method_get_sessions>] or get a specific one via [get_session()<class_EditorDebuggerPlugin_method_get_session>].


> **TABS**
>

    @tool
    extends EditorPlugin

    class ExampleEditorDebugger extends EditorDebuggerPlugin:

        func _has_capture(capture):
            # Return true if you wish to handle messages with the prefix "my_plugin:".
            return capture == "my_plugin"

        func _capture(message, data, session_id):
            if message == "my_plugin:ping":
                get_session(session_id).send_message("my_plugin:echo", data)
                return true
            return false

        func _setup_session(session_id):
            # Add a new tab in the debugger session UI containing a label.
            var label = Label.new()
            label.name = "Example plugin" # Will be used as the tab title.
            label.text = "Example plugin"
            var session = get_session(session_id)
            # Listens to the session started and stopped signals.
            session.started.connect(func (): print("Session started"))
            session.stopped.connect(func (): print("Session stopped"))
            session.add_session_tab(label)

    var debugger = ExampleEditorDebugger.new()

    func _enter_tree():
        add_debugger_plugin(debugger)

    func _exit_tree():
        remove_debugger_plugin(debugger)



To connect on the running game side, use the [EngineDebugger<class_EngineDebugger>] singleton:


> **TABS**
>

    extends Node

    func _ready():
        EngineDebugger.register_message_capture("my_plugin", _capture)
        EngineDebugger.send_message("my_plugin:ping", ["test"])

    func _capture(message, data):
        # Note that the "my_plugin:" prefix is not used here.
        if message == "echo":
            prints("Echo received:", data)
            return true
        return false



\ **Note:** While the game is running, [@GlobalScope.print()<class_@GlobalScope_method_print>] and similar functions *called in the editor* do not print anything, the Output Log prints only game messages.


## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                    | :ref:`_breakpoint_set_in_tree<class_EditorDebuggerPlugin_private_method__breakpoint_set_in_tree>`\ (\ script\: :ref:`Script<class_Script>`, line\: :ref:`int<class_int>`, enabled\: :ref:`bool<class_bool>`\ ) |virtual| |
> +-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                    | :ref:`_breakpoints_cleared_in_tree<class_EditorDebuggerPlugin_private_method__breakpoints_cleared_in_tree>`\ (\ ) |virtual|                                                                                              |
> +-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                   | :ref:`_capture<class_EditorDebuggerPlugin_private_method__capture>`\ (\ message\: :ref:`String<class_String>`, data\: :ref:`Array<class_Array>`, session_id\: :ref:`int<class_int>`\ ) |virtual|                         |
> +-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                    | :ref:`_goto_script_line<class_EditorDebuggerPlugin_private_method__goto_script_line>`\ (\ script\: :ref:`Script<class_Script>`, line\: :ref:`int<class_int>`\ ) |virtual|                                                |
> +-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                   | :ref:`_has_capture<class_EditorDebuggerPlugin_private_method__has_capture>`\ (\ capture\: :ref:`String<class_String>`\ ) |virtual| |const|                                                                               |
> +-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                    | :ref:`_setup_session<class_EditorDebuggerPlugin_private_method__setup_session>`\ (\ session_id\: :ref:`int<class_int>`\ ) |virtual|                                                                                      |
> +-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`EditorDebuggerSession<class_EditorDebuggerSession>` | :ref:`get_session<class_EditorDebuggerPlugin_method_get_session>`\ (\ id\: :ref:`int<class_int>`\ )                                                                                                                      |
> +-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`                                 | :ref:`get_sessions<class_EditorDebuggerPlugin_method_get_sessions>`\ (\ )                                                                                                                                                |
> +-----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



|void| **_breakpoint_set_in_tree**\ (\ script\: [Script<class_Script>], line\: [int<class_int>], enabled\: [bool<class_bool>]\ ) |virtual| [🔗<class_EditorDebuggerPlugin_private_method__breakpoint_set_in_tree>]

Override this method to be notified when a breakpoint is set in the editor.


----



|void| **_breakpoints_cleared_in_tree**\ (\ ) |virtual| [🔗<class_EditorDebuggerPlugin_private_method__breakpoints_cleared_in_tree>]

Override this method to be notified when all breakpoints are cleared in the editor.


----



[bool<class_bool>] **_capture**\ (\ message\: [String<class_String>], data\: [Array<class_Array>], session_id\: [int<class_int>]\ ) |virtual| [🔗<class_EditorDebuggerPlugin_private_method__capture>]

Override this method to process incoming messages. The `session_id` is the ID of the [EditorDebuggerSession<class_EditorDebuggerSession>] that received the `message`. Use [get_session()<class_EditorDebuggerPlugin_method_get_session>] to retrieve the session. This method should return `true` if the message is recognized.


----



|void| **_goto_script_line**\ (\ script\: [Script<class_Script>], line\: [int<class_int>]\ ) |virtual| [🔗<class_EditorDebuggerPlugin_private_method__goto_script_line>]

Override this method to be notified when a breakpoint line has been clicked in the debugger breakpoint panel.


----



[bool<class_bool>] **_has_capture**\ (\ capture\: [String<class_String>]\ ) |virtual| |const| [🔗<class_EditorDebuggerPlugin_private_method__has_capture>]

Override this method to enable receiving messages from the debugger. If `capture` is "my_message" then messages starting with "my_message:" will be passed to the [_capture()<class_EditorDebuggerPlugin_private_method__capture>] method.


----



|void| **_setup_session**\ (\ session_id\: [int<class_int>]\ ) |virtual| [🔗<class_EditorDebuggerPlugin_private_method__setup_session>]

Override this method to be notified whenever a new [EditorDebuggerSession<class_EditorDebuggerSession>] is created. Note that the session may be inactive during this stage.


----



[EditorDebuggerSession<class_EditorDebuggerSession>] **get_session**\ (\ id\: [int<class_int>]\ ) [🔗<class_EditorDebuggerPlugin_method_get_session>]

Returns the [EditorDebuggerSession<class_EditorDebuggerSession>] with the given `id`.


----



[Array<class_Array>] **get_sessions**\ (\ ) [🔗<class_EditorDebuggerPlugin_method_get_sessions>]

Returns an array of [EditorDebuggerSession<class_EditorDebuggerSession>] currently available to this debugger plugin.

\ **Note:** Sessions in the array may be inactive, check their state via [EditorDebuggerSession.is_active()<class_EditorDebuggerSession_method_is_active>].

