:github_url: hide



# EditorScenePostImport

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Post-processes scenes after import.


## Description

Imported scenes can be automatically modified right after import by setting their **Custom Script** Import property to a `tool` script that inherits from this class.

The [_post_import()<class_EditorScenePostImport_private_method__post_import>] callback receives the imported scene's root node and returns the modified version of the scene:


> **TABS**
>

    @tool # Needed so it runs in editor.
    extends EditorScenePostImport

    # This sample changes all node names.
    # Called right after the scene is imported and gets the root node.
    func _post_import(scene):
        # Change all node names to "modified_[oldnodename]"
        iterate(scene)
        return scene # Remember to return the imported scene

    func iterate(node):
        if node != null:
            node.name = "modified_" + node.name
            for child in node.get_children():
                iterate(child)


    using Godot;

    // This sample changes all node names.
    // Called right after the scene is imported and gets the root node.
    [Tool]
    public partial class NodeRenamer : EditorScenePostImport
    {
        public override GodotObject _PostImport(Node scene)
        {
            // Change all node names to "modified_[oldnodename]"
            Iterate(scene);
            return scene; // Remember to return the imported scene
        }

        public void Iterate(Node node)
        {
            if (node != null)
            {
                node.Name = $"modified_{node.Name}";
                foreach (Node child in node.GetChildren())
                {
                    Iterate(child);
## }
## }




## Tutorials

- [Importing 3D scenes: Configuration: Using import scripts for automation ](../tutorials/assets_pipeline/importing_3d_scenes/import_configuration.html#using-import-scripts-for-automation)_


## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------+-------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Object<class_Object>` | :ref:`_post_import<class_EditorScenePostImport_private_method__post_import>`\ (\ scene\: :ref:`Node<class_Node>`\ ) |virtual| |
> +-----------------------------+-------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>` | :ref:`get_source_file<class_EditorScenePostImport_method_get_source_file>`\ (\ ) |const|                                      |
> +-----------------------------+-------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[Object<class_Object>] **_post_import**\ (\ scene\: [Node<class_Node>]\ ) |virtual| [🔗<class_EditorScenePostImport_private_method__post_import>]

Called after the scene was imported. This method must return the modified version of the scene.


----



[String<class_String>] **get_source_file**\ (\ ) |const| [🔗<class_EditorScenePostImport_method_get_source_file>]

Returns the source file path which got imported (e.g. `res://scene.dae`).

