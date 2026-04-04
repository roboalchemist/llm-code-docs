:github_url: hide



# AnimationNodeBlendTree

**Inherits:** [AnimationRootNode<class_AnimationRootNode>] **<** [AnimationNode<class_AnimationNode>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A sub-tree of many type [AnimationNode<class_AnimationNode>]\ s used for complex animations. Used by [AnimationTree<class_AnimationTree>].


## Description

This animation node may contain a sub-tree of any other type animation nodes, such as [AnimationNodeTransition<class_AnimationNodeTransition>], [AnimationNodeBlend2<class_AnimationNodeBlend2>], [AnimationNodeBlend3<class_AnimationNodeBlend3>], [AnimationNodeOneShot<class_AnimationNodeOneShot>], etc. This is one of the most commonly used animation node roots.

An [AnimationNodeOutput<class_AnimationNodeOutput>] node named `output` is created by default.


## Tutorials

- [../tutorials/animation/animation_tree](Using AnimationTree .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------+-------------------------------------------------------------------------+-------------------+
> | :ref:`Vector2<class_Vector2>` | :ref:`graph_offset<class_AnimationNodeBlendTree_property_graph_offset>` | ``Vector2(0, 0)`` |
> +-------------------------------+-------------------------------------------------------------------------+-------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`add_node<class_AnimationNodeBlendTree_method_add_node>`\ (\ name\: :ref:`StringName<class_StringName>`, node\: :ref:`AnimationNode<class_AnimationNode>`, position\: :ref:`Vector2<class_Vector2>` = Vector2(0, 0)\ ) |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`connect_node<class_AnimationNodeBlendTree_method_connect_node>`\ (\ input_node\: :ref:`StringName<class_StringName>`, input_index\: :ref:`int<class_int>`, output_node\: :ref:`StringName<class_StringName>`\ )       |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`disconnect_node<class_AnimationNodeBlendTree_method_disconnect_node>`\ (\ input_node\: :ref:`StringName<class_StringName>`, input_index\: :ref:`int<class_int>`\ )                                                    |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`AnimationNode<class_AnimationNode>`                        | :ref:`get_node<class_AnimationNodeBlendTree_method_get_node>`\ (\ name\: :ref:`StringName<class_StringName>`\ ) |const|                                                                                                     |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`StringName<class_StringName>`\] | :ref:`get_node_list<class_AnimationNodeBlendTree_method_get_node_list>`\ (\ ) |const|                                                                                                                                       |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>`                                    | :ref:`get_node_position<class_AnimationNodeBlendTree_method_get_node_position>`\ (\ name\: :ref:`StringName<class_StringName>`\ ) |const|                                                                                   |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`has_node<class_AnimationNodeBlendTree_method_has_node>`\ (\ name\: :ref:`StringName<class_StringName>`\ ) |const|                                                                                                     |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`remove_node<class_AnimationNodeBlendTree_method_remove_node>`\ (\ name\: :ref:`StringName<class_StringName>`\ )                                                                                                       |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`rename_node<class_AnimationNodeBlendTree_method_rename_node>`\ (\ name\: :ref:`StringName<class_StringName>`, new_name\: :ref:`StringName<class_StringName>`\ )                                                       |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`set_node_position<class_AnimationNodeBlendTree_method_set_node_position>`\ (\ name\: :ref:`StringName<class_StringName>`, position\: :ref:`Vector2<class_Vector2>`\ )                                                 |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**node_changed**\ (\ node_name\: [StringName<class_StringName>]\ ) [🔗<class_AnimationNodeBlendTree_signal_node_changed>]

Emitted when the input port information is changed.


----


## Constants



**CONNECTION_OK** = `0` [🔗<class_AnimationNodeBlendTree_constant_CONNECTION_OK>]

The connection was successful.



**CONNECTION_ERROR_NO_INPUT** = `1` [🔗<class_AnimationNodeBlendTree_constant_CONNECTION_ERROR_NO_INPUT>]

The input node is `null`.



**CONNECTION_ERROR_NO_INPUT_INDEX** = `2` [🔗<class_AnimationNodeBlendTree_constant_CONNECTION_ERROR_NO_INPUT_INDEX>]

The specified input port is out of range.



**CONNECTION_ERROR_NO_OUTPUT** = `3` [🔗<class_AnimationNodeBlendTree_constant_CONNECTION_ERROR_NO_OUTPUT>]

The output node is `null`.



**CONNECTION_ERROR_SAME_NODE** = `4` [🔗<class_AnimationNodeBlendTree_constant_CONNECTION_ERROR_SAME_NODE>]

Input and output nodes are the same.



**CONNECTION_ERROR_CONNECTION_EXISTS** = `5` [🔗<class_AnimationNodeBlendTree_constant_CONNECTION_ERROR_CONNECTION_EXISTS>]

The specified connection already exists.


----


## Property Descriptions



[Vector2<class_Vector2>] **graph_offset** = `Vector2(0, 0)` [🔗<class_AnimationNodeBlendTree_property_graph_offset>]


- |void| **set_graph_offset**\ (\ value\: [Vector2<class_Vector2>]\ )
- [Vector2<class_Vector2>] **get_graph_offset**\ (\ )

The global offset of all sub animation nodes.


----


## Method Descriptions



|void| **add_node**\ (\ name\: [StringName<class_StringName>], node\: [AnimationNode<class_AnimationNode>], position\: [Vector2<class_Vector2>] = Vector2(0, 0)\ ) [🔗<class_AnimationNodeBlendTree_method_add_node>]

Adds an [AnimationNode<class_AnimationNode>] at the given `position`. The `name` is used to identify the created sub animation node later.


----



|void| **connect_node**\ (\ input_node\: [StringName<class_StringName>], input_index\: [int<class_int>], output_node\: [StringName<class_StringName>]\ ) [🔗<class_AnimationNodeBlendTree_method_connect_node>]

Connects the output of an [AnimationNode<class_AnimationNode>] as input for another [AnimationNode<class_AnimationNode>], at the input port specified by `input_index`.


----



|void| **disconnect_node**\ (\ input_node\: [StringName<class_StringName>], input_index\: [int<class_int>]\ ) [🔗<class_AnimationNodeBlendTree_method_disconnect_node>]

Disconnects the animation node connected to the specified input.


----



[AnimationNode<class_AnimationNode>] **get_node**\ (\ name\: [StringName<class_StringName>]\ ) |const| [🔗<class_AnimationNodeBlendTree_method_get_node>]

Returns the sub animation node with the specified `name`.


----



[Array<class_Array>]\[[StringName<class_StringName>]\] **get_node_list**\ (\ ) |const| [🔗<class_AnimationNodeBlendTree_method_get_node_list>]

Returns a list containing the names of all sub animation nodes in this blend tree.


----



[Vector2<class_Vector2>] **get_node_position**\ (\ name\: [StringName<class_StringName>]\ ) |const| [🔗<class_AnimationNodeBlendTree_method_get_node_position>]

Returns the position of the sub animation node with the specified `name`.


----



[bool<class_bool>] **has_node**\ (\ name\: [StringName<class_StringName>]\ ) |const| [🔗<class_AnimationNodeBlendTree_method_has_node>]

Returns `true` if a sub animation node with specified `name` exists.


----



|void| **remove_node**\ (\ name\: [StringName<class_StringName>]\ ) [🔗<class_AnimationNodeBlendTree_method_remove_node>]

Removes a sub animation node.


----



|void| **rename_node**\ (\ name\: [StringName<class_StringName>], new_name\: [StringName<class_StringName>]\ ) [🔗<class_AnimationNodeBlendTree_method_rename_node>]

Changes the name of a sub animation node.


----



|void| **set_node_position**\ (\ name\: [StringName<class_StringName>], position\: [Vector2<class_Vector2>]\ ) [🔗<class_AnimationNodeBlendTree_method_set_node_position>]

Modifies the position of a sub animation node.

