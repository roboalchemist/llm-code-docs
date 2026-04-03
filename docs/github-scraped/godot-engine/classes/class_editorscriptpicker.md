:github_url: hide



# EditorScriptPicker

**Inherits:** [EditorResourcePicker<class_EditorResourcePicker>] **<** [HBoxContainer<class_HBoxContainer>] **<** [BoxContainer<class_BoxContainer>] **<** [Container<class_Container>] **<** [Control<class_Control>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

Godot editor's control for selecting the `script` property of a [Node<class_Node>].


## Description

Similar to [EditorResourcePicker<class_EditorResourcePicker>] this [Control<class_Control>] node is used in the editor's Inspector dock, but only to edit the `script` property of a [Node<class_Node>]. Default options for creating new resources of all possible subtypes are replaced with dedicated buttons that open the "Attach Node Script" dialog. Can be used with [EditorInspectorPlugin<class_EditorInspectorPlugin>] to recreate the same behavior.

\ **Note:** You must set the [script_owner<class_EditorScriptPicker_property_script_owner>] for the custom context menu items to work.


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------+---------------------------------------------------------------------+
> | :ref:`Node<class_Node>` | :ref:`script_owner<class_EditorScriptPicker_property_script_owner>` |
> +-------------------------+---------------------------------------------------------------------+
>

----


## Property Descriptions



[Node<class_Node>] **script_owner** [🔗<class_EditorScriptPicker_property_script_owner>]


- |void| **set_script_owner**\ (\ value\: [Node<class_Node>]\ )
- [Node<class_Node>] **get_script_owner**\ (\ )

The owner [Node<class_Node>] of the script property that holds the edited resource.

