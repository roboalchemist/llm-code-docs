:github_url: hide



# ScriptEditor

**Inherits:** [PanelContainer<class_PanelContainer>] **<** [Container<class_Container>] **<** [Control<class_Control>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

Godot editor's script editor.


## Description

Godot editor's script editor.

\ **Note:** This class shouldn't be instantiated directly. Instead, access the singleton using [EditorInterface.get_script_editor()<class_EditorInterface_method_get_script_editor>].


## Methods

> **TABLE**
> :widths: auto
>
> +------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                       | :ref:`clear_docs_from_script<class_ScriptEditor_method_clear_docs_from_script>`\ (\ script\: :ref:`Script<class_Script>`\ )                                                             |
> +------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedStringArray<class_PackedStringArray>`                            | :ref:`get_breakpoints<class_ScriptEditor_method_get_breakpoints>`\ (\ )                                                                                                                 |
> +------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`ScriptEditorBase<class_ScriptEditorBase>`                              | :ref:`get_current_editor<class_ScriptEditor_method_get_current_editor>`\ (\ ) |const|                                                                                                   |
> +------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Script<class_Script>`                                                  | :ref:`get_current_script<class_ScriptEditor_method_get_current_script>`\ (\ )                                                                                                           |
> +------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`ScriptEditorBase<class_ScriptEditorBase>`\] | :ref:`get_open_script_editors<class_ScriptEditor_method_get_open_script_editors>`\ (\ ) |const|                                                                                         |
> +------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`Script<class_Script>`\]                     | :ref:`get_open_scripts<class_ScriptEditor_method_get_open_scripts>`\ (\ ) |const|                                                                                                       |
> +------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                       | :ref:`goto_help<class_ScriptEditor_method_goto_help>`\ (\ topic\: :ref:`String<class_String>`\ )                                                                                        |
> +------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                       | :ref:`goto_line<class_ScriptEditor_method_goto_line>`\ (\ line_number\: :ref:`int<class_int>`\ )                                                                                        |
> +------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                       | :ref:`open_script_create_dialog<class_ScriptEditor_method_open_script_create_dialog>`\ (\ base_name\: :ref:`String<class_String>`, base_path\: :ref:`String<class_String>`\ )           |
> +------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                       | :ref:`register_syntax_highlighter<class_ScriptEditor_method_register_syntax_highlighter>`\ (\ syntax_highlighter\: :ref:`EditorSyntaxHighlighter<class_EditorSyntaxHighlighter>`\ )     |
> +------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                       | :ref:`unregister_syntax_highlighter<class_ScriptEditor_method_unregister_syntax_highlighter>`\ (\ syntax_highlighter\: :ref:`EditorSyntaxHighlighter<class_EditorSyntaxHighlighter>`\ ) |
> +------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                       | :ref:`update_docs_from_script<class_ScriptEditor_method_update_docs_from_script>`\ (\ script\: :ref:`Script<class_Script>`\ )                                                           |
> +------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**editor_script_changed**\ (\ script\: [Script<class_Script>]\ ) [🔗<class_ScriptEditor_signal_editor_script_changed>]

Emitted when user changed active script. Argument is a freshly activated [Script<class_Script>].


----



**script_close**\ (\ script\: [Script<class_Script>]\ ) [🔗<class_ScriptEditor_signal_script_close>]

Emitted when editor is about to close the active script. Argument is a [Script<class_Script>] that is going to be closed.


----


## Method Descriptions



|void| **clear_docs_from_script**\ (\ script\: [Script<class_Script>]\ ) [🔗<class_ScriptEditor_method_clear_docs_from_script>]

Removes the documentation for the given `script`.

\ **Note:** This should be called whenever the script is changed to keep the open documentation state up to date.


----



[PackedStringArray<class_PackedStringArray>] **get_breakpoints**\ (\ ) [🔗<class_ScriptEditor_method_get_breakpoints>]

Returns array of breakpoints.


----



[ScriptEditorBase<class_ScriptEditorBase>] **get_current_editor**\ (\ ) |const| [🔗<class_ScriptEditor_method_get_current_editor>]

Returns the [ScriptEditorBase<class_ScriptEditorBase>] object that the user is currently editing.


----



[Script<class_Script>] **get_current_script**\ (\ ) [🔗<class_ScriptEditor_method_get_current_script>]

Returns a [Script<class_Script>] that is currently active in editor.


----



[Array<class_Array>]\[[ScriptEditorBase<class_ScriptEditorBase>]\] **get_open_script_editors**\ (\ ) |const| [🔗<class_ScriptEditor_method_get_open_script_editors>]

Returns an array with all [ScriptEditorBase<class_ScriptEditorBase>] objects which are currently open in editor.


----



[Array<class_Array>]\[[Script<class_Script>]\] **get_open_scripts**\ (\ ) |const| [🔗<class_ScriptEditor_method_get_open_scripts>]

Returns an array with all [Script<class_Script>] objects which are currently open in editor.


----



|void| **goto_help**\ (\ topic\: [String<class_String>]\ ) [🔗<class_ScriptEditor_method_goto_help>]

Opens help for the given topic. The `topic` is an encoded string that controls which class, method, constant, signal, annotation, property, or theme item should be focused.

The supported `topic` formats include `class_name:class`, `class_method:class:method`, `class_constant:class:constant`, `class_signal:class:signal`, `class_annotation:class:@annotation`, `class_property:class:property`, and `class_theme_item:class:item`, where `class` is the class name, `method` is the method name, `constant` is the constant name, `signal` is the signal name, `annotation` is the annotation name, `property` is the property name, and `item` is the theme item.

::

    # Shows help for the Node class.
    class_name:Node
    # Shows help for the global min function.
    # Global objects are accessible in the `@GlobalScope` namespace, shown here.
    class_method:@GlobalScope:min
    # Shows help for get_viewport in the Node class.
    class_method:Node:get_viewport
    # Shows help for the Input constant MOUSE_BUTTON_MIDDLE.
    class_constant:Input:MOUSE_BUTTON_MIDDLE
    # Shows help for the BaseButton signal pressed.
    class_signal:BaseButton:pressed
    # Shows help for the CanvasItem property visible.
    class_property:CanvasItem:visible
    # Shows help for the GDScript annotation export.
    # Annotations should be prefixed with the `@` symbol in the descriptor, as shown here.
    class_annotation:@GDScript:@export
    # Shows help for the GraphNode theme item named panel_selected.
    class_theme_item:GraphNode:panel_selected


----



|void| **goto_line**\ (\ line_number\: [int<class_int>]\ ) [🔗<class_ScriptEditor_method_goto_line>]

Goes to the specified line in the current script.


----



|void| **open_script_create_dialog**\ (\ base_name\: [String<class_String>], base_path\: [String<class_String>]\ ) [🔗<class_ScriptEditor_method_open_script_create_dialog>]

Opens the script create dialog. The script will extend `base_name`. The file extension can be omitted from `base_path`. It will be added based on the selected scripting language.


----



|void| **register_syntax_highlighter**\ (\ syntax_highlighter\: [EditorSyntaxHighlighter<class_EditorSyntaxHighlighter>]\ ) [🔗<class_ScriptEditor_method_register_syntax_highlighter>]

Registers the [EditorSyntaxHighlighter<class_EditorSyntaxHighlighter>] to the editor, the [EditorSyntaxHighlighter<class_EditorSyntaxHighlighter>] will be available on all open scripts.

\ **Note:** Does not apply to scripts that are already opened.


----



|void| **unregister_syntax_highlighter**\ (\ syntax_highlighter\: [EditorSyntaxHighlighter<class_EditorSyntaxHighlighter>]\ ) [🔗<class_ScriptEditor_method_unregister_syntax_highlighter>]

Unregisters the [EditorSyntaxHighlighter<class_EditorSyntaxHighlighter>] from the editor.

\ **Note:** The [EditorSyntaxHighlighter<class_EditorSyntaxHighlighter>] will still be applied to scripts that are already opened.


----



|void| **update_docs_from_script**\ (\ script\: [Script<class_Script>]\ ) [🔗<class_ScriptEditor_method_update_docs_from_script>]

Updates the documentation for the given `script`.

\ **Note:** This should be called whenever the script is changed to keep the open documentation state up to date.

