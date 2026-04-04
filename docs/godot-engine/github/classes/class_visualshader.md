:github_url: hide



# VisualShader

**Inherits:** [Shader<class_Shader>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A custom shader program with a visual editor.


## Description

This class provides a graph-like visual editor for creating a [Shader<class_Shader>]. Although **VisualShader**\ s do not require coding, they share the same logic with script shaders. They use [VisualShaderNode<class_VisualShaderNode>]\ s that can be connected to each other to control the flow of the shader. The visual shader graph is converted to a script shader behind the scenes.


## Tutorials

- [../tutorials/shaders/visual_shaders](Using VisualShaders .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------+---------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>` | :ref:`graph_offset<class_VisualShader_property_graph_offset>` |
> +-------------------------------+---------------------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`add_node<class_VisualShader_method_add_node>`\ (\ type\: :ref:`Type<enum_VisualShader_Type>`, node\: :ref:`VisualShaderNode<class_VisualShaderNode>`, position\: :ref:`Vector2<class_Vector2>`, id\: :ref:`int<class_int>`\ )                                       |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`add_varying<class_VisualShader_method_add_varying>`\ (\ name\: :ref:`String<class_String>`, mode\: :ref:`VaryingMode<enum_VisualShader_VaryingMode>`, type\: :ref:`VaryingType<enum_VisualShader_VaryingType>`\ )                                                   |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`attach_node_to_frame<class_VisualShader_method_attach_node_to_frame>`\ (\ type\: :ref:`Type<enum_VisualShader_Type>`, id\: :ref:`int<class_int>`, frame\: :ref:`int<class_int>`\ )                                                                                  |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`can_connect_nodes<class_VisualShader_method_can_connect_nodes>`\ (\ type\: :ref:`Type<enum_VisualShader_Type>`, from_node\: :ref:`int<class_int>`, from_port\: :ref:`int<class_int>`, to_node\: :ref:`int<class_int>`, to_port\: :ref:`int<class_int>`\ ) |const|   |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>`                            | :ref:`connect_nodes<class_VisualShader_method_connect_nodes>`\ (\ type\: :ref:`Type<enum_VisualShader_Type>`, from_node\: :ref:`int<class_int>`, from_port\: :ref:`int<class_int>`, to_node\: :ref:`int<class_int>`, to_port\: :ref:`int<class_int>`\ )                   |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`connect_nodes_forced<class_VisualShader_method_connect_nodes_forced>`\ (\ type\: :ref:`Type<enum_VisualShader_Type>`, from_node\: :ref:`int<class_int>`, from_port\: :ref:`int<class_int>`, to_node\: :ref:`int<class_int>`, to_port\: :ref:`int<class_int>`\ )     |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`detach_node_from_frame<class_VisualShader_method_detach_node_from_frame>`\ (\ type\: :ref:`Type<enum_VisualShader_Type>`, id\: :ref:`int<class_int>`\ )                                                                                                             |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`disconnect_nodes<class_VisualShader_method_disconnect_nodes>`\ (\ type\: :ref:`Type<enum_VisualShader_Type>`, from_node\: :ref:`int<class_int>`, from_port\: :ref:`int<class_int>`, to_node\: :ref:`int<class_int>`, to_port\: :ref:`int<class_int>`\ )             |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`VisualShaderNode<class_VisualShaderNode>`                  | :ref:`get_node<class_VisualShader_method_get_node>`\ (\ type\: :ref:`Type<enum_VisualShader_Type>`, id\: :ref:`int<class_int>`\ ) |const|                                                                                                                                 |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`Dictionary<class_Dictionary>`\] | :ref:`get_node_connections<class_VisualShader_method_get_node_connections>`\ (\ type\: :ref:`Type<enum_VisualShader_Type>`\ ) |const|                                                                                                                                     |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedInt32Array<class_PackedInt32Array>`                  | :ref:`get_node_list<class_VisualShader_method_get_node_list>`\ (\ type\: :ref:`Type<enum_VisualShader_Type>`\ ) |const|                                                                                                                                                   |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>`                                    | :ref:`get_node_position<class_VisualShader_method_get_node_position>`\ (\ type\: :ref:`Type<enum_VisualShader_Type>`, id\: :ref:`int<class_int>`\ ) |const|                                                                                                               |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                            | :ref:`get_valid_node_id<class_VisualShader_method_get_valid_node_id>`\ (\ type\: :ref:`Type<enum_VisualShader_Type>`\ ) |const|                                                                                                                                           |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`has_varying<class_VisualShader_method_has_varying>`\ (\ name\: :ref:`String<class_String>`\ ) |const|                                                                                                                                                               |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`is_node_connection<class_VisualShader_method_is_node_connection>`\ (\ type\: :ref:`Type<enum_VisualShader_Type>`, from_node\: :ref:`int<class_int>`, from_port\: :ref:`int<class_int>`, to_node\: :ref:`int<class_int>`, to_port\: :ref:`int<class_int>`\ ) |const| |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`remove_node<class_VisualShader_method_remove_node>`\ (\ type\: :ref:`Type<enum_VisualShader_Type>`, id\: :ref:`int<class_int>`\ )                                                                                                                                   |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`remove_varying<class_VisualShader_method_remove_varying>`\ (\ name\: :ref:`String<class_String>`\ )                                                                                                                                                                 |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`replace_node<class_VisualShader_method_replace_node>`\ (\ type\: :ref:`Type<enum_VisualShader_Type>`, id\: :ref:`int<class_int>`, new_class\: :ref:`StringName<class_StringName>`\ )                                                                                |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`set_mode<class_VisualShader_method_set_mode>`\ (\ mode\: :ref:`Mode<enum_Shader_Mode>`\ )                                                                                                                                                                           |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`set_node_position<class_VisualShader_method_set_node_position>`\ (\ type\: :ref:`Type<enum_VisualShader_Type>`, id\: :ref:`int<class_int>`, position\: :ref:`Vector2<class_Vector2>`\ )                                                                             |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **Type**: [🔗<enum_VisualShader_Type>]



[Type<enum_VisualShader_Type>] **TYPE_VERTEX** = `0`

A vertex shader, operating on vertices.



[Type<enum_VisualShader_Type>] **TYPE_FRAGMENT** = `1`

A fragment shader, operating on fragments (pixels).



[Type<enum_VisualShader_Type>] **TYPE_LIGHT** = `2`

A shader for light calculations.



[Type<enum_VisualShader_Type>] **TYPE_START** = `3`

A function for the "start" stage of particle shader.



[Type<enum_VisualShader_Type>] **TYPE_PROCESS** = `4`

A function for the "process" stage of particle shader.



[Type<enum_VisualShader_Type>] **TYPE_COLLIDE** = `5`

A function for the "collide" stage (particle collision handler) of particle shader.



[Type<enum_VisualShader_Type>] **TYPE_START_CUSTOM** = `6`

A function for the "start" stage of particle shader, with customized output.



[Type<enum_VisualShader_Type>] **TYPE_PROCESS_CUSTOM** = `7`

A function for the "process" stage of particle shader, with customized output.



[Type<enum_VisualShader_Type>] **TYPE_SKY** = `8`

A shader for 3D environment's sky.



[Type<enum_VisualShader_Type>] **TYPE_FOG** = `9`

A compute shader that runs for each froxel of the volumetric fog map.



[Type<enum_VisualShader_Type>] **TYPE_MAX** = `10`

Represents the size of the [Type<enum_VisualShader_Type>] enum.


----



enum **VaryingMode**: [🔗<enum_VisualShader_VaryingMode>]



[VaryingMode<enum_VisualShader_VaryingMode>] **VARYING_MODE_VERTEX_TO_FRAG_LIGHT** = `0`

Varying is passed from `Vertex` function to `Fragment` and `Light` functions.



[VaryingMode<enum_VisualShader_VaryingMode>] **VARYING_MODE_FRAG_TO_LIGHT** = `1`

Varying is passed from `Fragment` function to `Light` function.



[VaryingMode<enum_VisualShader_VaryingMode>] **VARYING_MODE_MAX** = `2`

Represents the size of the [VaryingMode<enum_VisualShader_VaryingMode>] enum.


----



enum **VaryingType**: [🔗<enum_VisualShader_VaryingType>]



[VaryingType<enum_VisualShader_VaryingType>] **VARYING_TYPE_FLOAT** = `0`

Varying is of type [float<class_float>].



[VaryingType<enum_VisualShader_VaryingType>] **VARYING_TYPE_INT** = `1`

Varying is of type [int<class_int>].



[VaryingType<enum_VisualShader_VaryingType>] **VARYING_TYPE_UINT** = `2`

Varying is of type unsigned [int<class_int>].



[VaryingType<enum_VisualShader_VaryingType>] **VARYING_TYPE_VECTOR_2D** = `3`

Varying is of type [Vector2<class_Vector2>].



[VaryingType<enum_VisualShader_VaryingType>] **VARYING_TYPE_VECTOR_3D** = `4`

Varying is of type [Vector3<class_Vector3>].



[VaryingType<enum_VisualShader_VaryingType>] **VARYING_TYPE_VECTOR_4D** = `5`

Varying is of type [Vector4<class_Vector4>].



[VaryingType<enum_VisualShader_VaryingType>] **VARYING_TYPE_BOOLEAN** = `6`

Varying is of type [bool<class_bool>].



[VaryingType<enum_VisualShader_VaryingType>] **VARYING_TYPE_TRANSFORM** = `7`

Varying is of type [Transform3D<class_Transform3D>].



[VaryingType<enum_VisualShader_VaryingType>] **VARYING_TYPE_MAX** = `8`

Represents the size of the [VaryingType<enum_VisualShader_VaryingType>] enum.


----


## Constants



**NODE_ID_INVALID** = `-1` [🔗<class_VisualShader_constant_NODE_ID_INVALID>]

Indicates an invalid **VisualShader** node.



**NODE_ID_OUTPUT** = `0` [🔗<class_VisualShader_constant_NODE_ID_OUTPUT>]

Indicates an output node of **VisualShader**.


----


## Property Descriptions



[Vector2<class_Vector2>] **graph_offset** [🔗<class_VisualShader_property_graph_offset>]


- |void| **set_graph_offset**\ (\ value\: [Vector2<class_Vector2>]\ )
- [Vector2<class_Vector2>] **get_graph_offset**\ (\ )

**Deprecated:** This property does nothing and always equals to zero.

Deprecated.


----


## Method Descriptions



|void| **add_node**\ (\ type\: [Type<enum_VisualShader_Type>], node\: [VisualShaderNode<class_VisualShaderNode>], position\: [Vector2<class_Vector2>], id\: [int<class_int>]\ ) [🔗<class_VisualShader_method_add_node>]

Adds the specified `node` to the shader.


----



|void| **add_varying**\ (\ name\: [String<class_String>], mode\: [VaryingMode<enum_VisualShader_VaryingMode>], type\: [VaryingType<enum_VisualShader_VaryingType>]\ ) [🔗<class_VisualShader_method_add_varying>]

Adds a new varying value node to the shader.


----



|void| **attach_node_to_frame**\ (\ type\: [Type<enum_VisualShader_Type>], id\: [int<class_int>], frame\: [int<class_int>]\ ) [🔗<class_VisualShader_method_attach_node_to_frame>]

Attaches the given node to the given frame.


----



[bool<class_bool>] **can_connect_nodes**\ (\ type\: [Type<enum_VisualShader_Type>], from_node\: [int<class_int>], from_port\: [int<class_int>], to_node\: [int<class_int>], to_port\: [int<class_int>]\ ) |const| [🔗<class_VisualShader_method_can_connect_nodes>]

Returns `true` if the specified nodes and ports can be connected together.


----



[Error<enum_@GlobalScope_Error>] **connect_nodes**\ (\ type\: [Type<enum_VisualShader_Type>], from_node\: [int<class_int>], from_port\: [int<class_int>], to_node\: [int<class_int>], to_port\: [int<class_int>]\ ) [🔗<class_VisualShader_method_connect_nodes>]

Connects the specified nodes and ports.


----



|void| **connect_nodes_forced**\ (\ type\: [Type<enum_VisualShader_Type>], from_node\: [int<class_int>], from_port\: [int<class_int>], to_node\: [int<class_int>], to_port\: [int<class_int>]\ ) [🔗<class_VisualShader_method_connect_nodes_forced>]

Connects the specified nodes and ports, even if they can't be connected. Such connection is invalid and will not function properly.


----



|void| **detach_node_from_frame**\ (\ type\: [Type<enum_VisualShader_Type>], id\: [int<class_int>]\ ) [🔗<class_VisualShader_method_detach_node_from_frame>]

Detaches the given node from the frame it is attached to.


----



|void| **disconnect_nodes**\ (\ type\: [Type<enum_VisualShader_Type>], from_node\: [int<class_int>], from_port\: [int<class_int>], to_node\: [int<class_int>], to_port\: [int<class_int>]\ ) [🔗<class_VisualShader_method_disconnect_nodes>]

Connects the specified nodes and ports.


----



[VisualShaderNode<class_VisualShaderNode>] **get_node**\ (\ type\: [Type<enum_VisualShader_Type>], id\: [int<class_int>]\ ) |const| [🔗<class_VisualShader_method_get_node>]

Returns the shader node instance with specified `type` and `id`.


----



[Array<class_Array>]\[[Dictionary<class_Dictionary>]\] **get_node_connections**\ (\ type\: [Type<enum_VisualShader_Type>]\ ) |const| [🔗<class_VisualShader_method_get_node_connections>]

Returns the list of connected nodes with the specified type.


----



[PackedInt32Array<class_PackedInt32Array>] **get_node_list**\ (\ type\: [Type<enum_VisualShader_Type>]\ ) |const| [🔗<class_VisualShader_method_get_node_list>]

Returns the list of all nodes in the shader with the specified type.


----



[Vector2<class_Vector2>] **get_node_position**\ (\ type\: [Type<enum_VisualShader_Type>], id\: [int<class_int>]\ ) |const| [🔗<class_VisualShader_method_get_node_position>]

Returns the position of the specified node within the shader graph.


----



[int<class_int>] **get_valid_node_id**\ (\ type\: [Type<enum_VisualShader_Type>]\ ) |const| [🔗<class_VisualShader_method_get_valid_node_id>]

Returns next valid node ID that can be added to the shader graph.


----



[bool<class_bool>] **has_varying**\ (\ name\: [String<class_String>]\ ) |const| [🔗<class_VisualShader_method_has_varying>]

Returns `true` if the shader has a varying with the given `name`.


----



[bool<class_bool>] **is_node_connection**\ (\ type\: [Type<enum_VisualShader_Type>], from_node\: [int<class_int>], from_port\: [int<class_int>], to_node\: [int<class_int>], to_port\: [int<class_int>]\ ) |const| [🔗<class_VisualShader_method_is_node_connection>]

Returns `true` if the specified node and port connection exist.


----



|void| **remove_node**\ (\ type\: [Type<enum_VisualShader_Type>], id\: [int<class_int>]\ ) [🔗<class_VisualShader_method_remove_node>]

Removes the specified node from the shader.


----



|void| **remove_varying**\ (\ name\: [String<class_String>]\ ) [🔗<class_VisualShader_method_remove_varying>]

Removes a varying value node with the given `name`. Prints an error if a node with this name is not found.


----



|void| **replace_node**\ (\ type\: [Type<enum_VisualShader_Type>], id\: [int<class_int>], new_class\: [StringName<class_StringName>]\ ) [🔗<class_VisualShader_method_replace_node>]

Replaces the specified node with a node of new class type.


----



|void| **set_mode**\ (\ mode\: [Mode<enum_Shader_Mode>]\ ) [🔗<class_VisualShader_method_set_mode>]

Sets the mode of this shader.


----



|void| **set_node_position**\ (\ type\: [Type<enum_VisualShader_Type>], id\: [int<class_int>], position\: [Vector2<class_Vector2>]\ ) [🔗<class_VisualShader_method_set_node_position>]

Sets the position of the specified node.

