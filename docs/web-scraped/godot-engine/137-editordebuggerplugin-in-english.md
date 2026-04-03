# EditorDebuggerPlugin in English

# EditorDebuggerPlugin
Inherits:RefCounted<Object
A base class to implement debugger plugins.

## Description
EditorDebuggerPluginprovides functions related to the editor side of the debugger.
To interact with the debugger, an instance of this class must be added to the editor viaEditorPlugin.add_debugger_plugin().
Once added, the_setup_session()callback will be called for everyEditorDebuggerSessionavailable to the plugin, and when new ones are created (the sessions may be inactive during this stage).
You can retrieve the availableEditorDebuggerSessions viaget_sessions()or get a specific one viaget_session().
```
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
```
To connect on the running game side, use theEngineDebuggersingleton:
```
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
```
Note:While the game is running,@GlobalScope.print()and similar functionscalled in the editordo not print anything, the Output Log prints only game messages.

## Methods

| void | _breakpoint_set_in_tree(script:Script, line:int, enabled:bool)virtual |
|---|---|
| void | _breakpoints_cleared_in_tree()virtual |
| bool | _capture(message:String, data:Array, session_id:int)virtual |
| void | _goto_script_line(script:Script, line:int)virtual |
| bool | _has_capture(capture:String)virtualconst |
| void | _setup_session(session_id:int)virtual |
| EditorDebuggerSession | get_session(id:int) |
| Array | get_sessions() |

void
_breakpoint_set_in_tree(script:Script, line:int, enabled:bool)virtual
void
_breakpoints_cleared_in_tree()virtual
bool
_capture(message:String, data:Array, session_id:int)virtual
void
_goto_script_line(script:Script, line:int)virtual
bool
_has_capture(capture:String)virtualconst
void
_setup_session(session_id:int)virtual
EditorDebuggerSession
get_session(id:int)
Array
get_sessions()

## Method Descriptions
void_breakpoint_set_in_tree(script:Script, line:int, enabled:bool)virtual🔗
Override this method to be notified when a breakpoint is set in the editor.
void_breakpoints_cleared_in_tree()virtual🔗
Override this method to be notified when all breakpoints are cleared in the editor.
bool_capture(message:String, data:Array, session_id:int)virtual🔗
Override this method to process incoming messages. Thesession_idis the ID of theEditorDebuggerSessionthat received themessage. Useget_session()to retrieve the session. This method should returntrueif the message is recognized.
void_goto_script_line(script:Script, line:int)virtual🔗
Override this method to be notified when a breakpoint line has been clicked in the debugger breakpoint panel.
bool_has_capture(capture:String)virtualconst🔗
Override this method to enable receiving messages from the debugger. Ifcaptureis "my_message" then messages starting with "my_message:" will be passed to the_capture()method.
void_setup_session(session_id:int)virtual🔗
Override this method to be notified whenever a newEditorDebuggerSessionis created. Note that the session may be inactive during this stage.
EditorDebuggerSessionget_session(id:int)🔗
Returns theEditorDebuggerSessionwith the givenid.
Arrayget_sessions()🔗
Returns an array ofEditorDebuggerSessioncurrently available to this debugger plugin.
Note:Sessions in the array may be inactive, check their state viaEditorDebuggerSession.is_active().

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.