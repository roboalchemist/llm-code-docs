:github_url: hide



# EditorScript

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Base script that can be used to add extension functions to the editor.


## Description

Scripts extending this class and implementing its [_run()<class_EditorScript_private_method__run>] method can be executed from the Script Editor's **File > Run** menu option (or by pressing :kbd:`Ctrl + Shift + X`) while the editor is running. This is useful for adding custom in-editor functionality to Godot. For more complex additions, consider using [EditorPlugin<class_EditorPlugin>]\ s instead.

If a script extending this class also has a global class name, it will be included in the editor's command palette.

\ **Note:** Extending scripts need to have `tool` mode enabled.

\ **Example:** Running the following script prints "Hello from the Godot Editor!":


> **TABS**
>

    @tool
    extends EditorScript

    func _run():
        print("Hello from the Godot Editor!")


    using Godot;

    [Tool]
    public partial class HelloEditor : EditorScript
    {
        public override void _Run()
        {
            GD.Print("Hello from the Godot Editor!");
## }



\ **Note:** EditorScript is [RefCounted<class_RefCounted>], meaning it is destroyed when nothing references it. This can cause errors during asynchronous operations if there are no references to the script.


## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------+-----------------------------------------------------------------------------------------------------+
> | |void|                                        | :ref:`_run<class_EditorScript_private_method__run>`\ (\ ) |virtual| |required|                      |
> +-----------------------------------------------+-----------------------------------------------------------------------------------------------------+
> | |void|                                        | :ref:`add_root_node<class_EditorScript_method_add_root_node>`\ (\ node\: :ref:`Node<class_Node>`\ ) |
> +-----------------------------------------------+-----------------------------------------------------------------------------------------------------+
> | :ref:`EditorInterface<class_EditorInterface>` | :ref:`get_editor_interface<class_EditorScript_method_get_editor_interface>`\ (\ ) |const|           |
> +-----------------------------------------------+-----------------------------------------------------------------------------------------------------+
> | :ref:`Node<class_Node>`                       | :ref:`get_scene<class_EditorScript_method_get_scene>`\ (\ ) |const|                                 |
> +-----------------------------------------------+-----------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



|void| **_run**\ (\ ) |virtual| |required| [🔗<class_EditorScript_private_method__run>]

This method is executed by the Editor when **File > Run** is used.


----



|void| **add_root_node**\ (\ node\: [Node<class_Node>]\ ) [🔗<class_EditorScript_method_add_root_node>]

**Deprecated:** Use [EditorInterface.add_root_node()<class_EditorInterface_method_add_root_node>] instead.

Makes `node` root of the currently opened scene. Only works if the scene is empty. If the `node` is a scene instance, an inheriting scene will be created.


----



[EditorInterface<class_EditorInterface>] **get_editor_interface**\ (\ ) |const| [🔗<class_EditorScript_method_get_editor_interface>]

**Deprecated:** [EditorInterface<class_EditorInterface>] is a global singleton and can be accessed directly by its name.

Returns the [EditorInterface<class_EditorInterface>] singleton instance.


----



[Node<class_Node>] **get_scene**\ (\ ) |const| [🔗<class_EditorScript_method_get_scene>]

**Deprecated:** Use [EditorInterface.get_edited_scene_root()<class_EditorInterface_method_get_edited_scene_root>] instead.

Returns the edited (current) scene's root [Node<class_Node>]. Equivalent of [EditorInterface.get_edited_scene_root()<class_EditorInterface_method_get_edited_scene_root>].

