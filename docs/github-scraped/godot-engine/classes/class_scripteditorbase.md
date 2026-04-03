:github_url: hide



# ScriptEditorBase

**Inherits:** [VBoxContainer<class_VBoxContainer>] **<** [BoxContainer<class_BoxContainer>] **<** [Container<class_Container>] **<** [Control<class_Control>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

Base editor for editing scripts in the [ScriptEditor<class_ScriptEditor>].


## Description

Base editor for editing scripts in the [ScriptEditor<class_ScriptEditor>]. This does not include documentation items.


## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`add_syntax_highlighter<class_ScriptEditorBase_method_add_syntax_highlighter>`\ (\ highlighter\: :ref:`EditorSyntaxHighlighter<class_EditorSyntaxHighlighter>`\ ) |
> +-------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Control<class_Control>` | :ref:`get_base_editor<class_ScriptEditorBase_method_get_base_editor>`\ (\ ) |const|                                                                                    |
> +-------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**edited_script_changed**\ (\ ) [🔗<class_ScriptEditorBase_signal_edited_script_changed>]

Emitted after script validation.


----



**go_to_help**\ (\ what\: [String<class_String>]\ ) [🔗<class_ScriptEditorBase_signal_go_to_help>]

Emitted when the user requests a specific documentation page.


----



**go_to_method**\ (\ script\: [Object<class_Object>], method\: [String<class_String>]\ ) [🔗<class_ScriptEditorBase_signal_go_to_method>]

Emitted when the user requests to view a specific method of a script, similar to [request_open_script_at_line<class_ScriptEditorBase_signal_request_open_script_at_line>].


----



**name_changed**\ (\ ) [🔗<class_ScriptEditorBase_signal_name_changed>]

Emitted after script validation or when the edited resource has changed.


----



**replace_in_files_requested**\ (\ text\: [String<class_String>]\ ) [🔗<class_ScriptEditorBase_signal_replace_in_files_requested>]

Emitted when the user request to find and replace text in the file system.


----



**request_help**\ (\ topic\: [String<class_String>]\ ) [🔗<class_ScriptEditorBase_signal_request_help>]

Emitted when the user requests contextual help.


----



**request_open_script_at_line**\ (\ script\: [Object<class_Object>], line\: [int<class_int>]\ ) [🔗<class_ScriptEditorBase_signal_request_open_script_at_line>]

Emitted when the user requests to view a specific line of a script, similar to [go_to_method<class_ScriptEditorBase_signal_go_to_method>].


----



**request_save_history**\ (\ ) [🔗<class_ScriptEditorBase_signal_request_save_history>]

Emitted when the user contextual goto and the item is in the same script.


----



**request_save_previous_state**\ (\ state\: [Dictionary<class_Dictionary>]\ ) [🔗<class_ScriptEditorBase_signal_request_save_previous_state>]

Emitted when the user changes current script or moves caret by 10 or more columns within the same script.


----



**search_in_files_requested**\ (\ text\: [String<class_String>]\ ) [🔗<class_ScriptEditorBase_signal_search_in_files_requested>]

Emitted when the user request to search text in the file system.


----


## Method Descriptions



|void| **add_syntax_highlighter**\ (\ highlighter\: [EditorSyntaxHighlighter<class_EditorSyntaxHighlighter>]\ ) [🔗<class_ScriptEditorBase_method_add_syntax_highlighter>]

Adds an [EditorSyntaxHighlighter<class_EditorSyntaxHighlighter>] to the open script.


----



[Control<class_Control>] **get_base_editor**\ (\ ) |const| [🔗<class_ScriptEditorBase_method_get_base_editor>]

Returns the underlying [Control<class_Control>] used for editing scripts. For text scripts, this is a [CodeEdit<class_CodeEdit>].

