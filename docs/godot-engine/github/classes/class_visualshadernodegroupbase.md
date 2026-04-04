:github_url: hide



# VisualShaderNodeGroupBase

**Inherits:** [VisualShaderNodeResizableBase<class_VisualShaderNodeResizableBase>] **<** [VisualShaderNode<class_VisualShaderNode>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [VisualShaderNodeExpression<class_VisualShaderNodeExpression>]

Base class for a family of nodes with variable number of input and output ports within the visual shader graph.


## Description

Currently, has no direct usage, use the derived classes instead.


## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                      | :ref:`add_input_port<class_VisualShaderNodeGroupBase_method_add_input_port>`\ (\ id\: :ref:`int<class_int>`, type\: :ref:`int<class_int>`, name\: :ref:`String<class_String>`\ )   |
> +-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                      | :ref:`add_output_port<class_VisualShaderNodeGroupBase_method_add_output_port>`\ (\ id\: :ref:`int<class_int>`, type\: :ref:`int<class_int>`, name\: :ref:`String<class_String>`\ ) |
> +-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                      | :ref:`clear_input_ports<class_VisualShaderNodeGroupBase_method_clear_input_ports>`\ (\ )                                                                                           |
> +-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                      | :ref:`clear_output_ports<class_VisualShaderNodeGroupBase_method_clear_output_ports>`\ (\ )                                                                                         |
> +-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`       | :ref:`get_free_input_port_id<class_VisualShaderNodeGroupBase_method_get_free_input_port_id>`\ (\ ) |const|                                                                         |
> +-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`       | :ref:`get_free_output_port_id<class_VisualShaderNodeGroupBase_method_get_free_output_port_id>`\ (\ ) |const|                                                                       |
> +-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`       | :ref:`get_input_port_count<class_VisualShaderNodeGroupBase_method_get_input_port_count>`\ (\ ) |const|                                                                             |
> +-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>` | :ref:`get_inputs<class_VisualShaderNodeGroupBase_method_get_inputs>`\ (\ ) |const|                                                                                                 |
> +-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`       | :ref:`get_output_port_count<class_VisualShaderNodeGroupBase_method_get_output_port_count>`\ (\ ) |const|                                                                           |
> +-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>` | :ref:`get_outputs<class_VisualShaderNodeGroupBase_method_get_outputs>`\ (\ ) |const|                                                                                               |
> +-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`     | :ref:`has_input_port<class_VisualShaderNodeGroupBase_method_has_input_port>`\ (\ id\: :ref:`int<class_int>`\ ) |const|                                                             |
> +-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`     | :ref:`has_output_port<class_VisualShaderNodeGroupBase_method_has_output_port>`\ (\ id\: :ref:`int<class_int>`\ ) |const|                                                           |
> +-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`     | :ref:`is_valid_port_name<class_VisualShaderNodeGroupBase_method_is_valid_port_name>`\ (\ name\: :ref:`String<class_String>`\ ) |const|                                             |
> +-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                      | :ref:`remove_input_port<class_VisualShaderNodeGroupBase_method_remove_input_port>`\ (\ id\: :ref:`int<class_int>`\ )                                                               |
> +-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                      | :ref:`remove_output_port<class_VisualShaderNodeGroupBase_method_remove_output_port>`\ (\ id\: :ref:`int<class_int>`\ )                                                             |
> +-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                      | :ref:`set_input_port_name<class_VisualShaderNodeGroupBase_method_set_input_port_name>`\ (\ id\: :ref:`int<class_int>`, name\: :ref:`String<class_String>`\ )                       |
> +-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                      | :ref:`set_input_port_type<class_VisualShaderNodeGroupBase_method_set_input_port_type>`\ (\ id\: :ref:`int<class_int>`, type\: :ref:`int<class_int>`\ )                             |
> +-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                      | :ref:`set_inputs<class_VisualShaderNodeGroupBase_method_set_inputs>`\ (\ inputs\: :ref:`String<class_String>`\ )                                                                   |
> +-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                      | :ref:`set_output_port_name<class_VisualShaderNodeGroupBase_method_set_output_port_name>`\ (\ id\: :ref:`int<class_int>`, name\: :ref:`String<class_String>`\ )                     |
> +-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                      | :ref:`set_output_port_type<class_VisualShaderNodeGroupBase_method_set_output_port_type>`\ (\ id\: :ref:`int<class_int>`, type\: :ref:`int<class_int>`\ )                           |
> +-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                      | :ref:`set_outputs<class_VisualShaderNodeGroupBase_method_set_outputs>`\ (\ outputs\: :ref:`String<class_String>`\ )                                                                |
> +-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



|void| **add_input_port**\ (\ id\: [int<class_int>], type\: [int<class_int>], name\: [String<class_String>]\ ) [🔗<class_VisualShaderNodeGroupBase_method_add_input_port>]

Adds an input port with the specified `type` (see [PortType<enum_VisualShaderNode_PortType>]) and `name`.


----



|void| **add_output_port**\ (\ id\: [int<class_int>], type\: [int<class_int>], name\: [String<class_String>]\ ) [🔗<class_VisualShaderNodeGroupBase_method_add_output_port>]

Adds an output port with the specified `type` (see [PortType<enum_VisualShaderNode_PortType>]) and `name`.


----



|void| **clear_input_ports**\ (\ ) [🔗<class_VisualShaderNodeGroupBase_method_clear_input_ports>]

Removes all previously specified input ports.


----



|void| **clear_output_ports**\ (\ ) [🔗<class_VisualShaderNodeGroupBase_method_clear_output_ports>]

Removes all previously specified output ports.


----



[int<class_int>] **get_free_input_port_id**\ (\ ) |const| [🔗<class_VisualShaderNodeGroupBase_method_get_free_input_port_id>]

Returns a free input port ID which can be used in [add_input_port()<class_VisualShaderNodeGroupBase_method_add_input_port>].


----



[int<class_int>] **get_free_output_port_id**\ (\ ) |const| [🔗<class_VisualShaderNodeGroupBase_method_get_free_output_port_id>]

Returns a free output port ID which can be used in [add_output_port()<class_VisualShaderNodeGroupBase_method_add_output_port>].


----



[int<class_int>] **get_input_port_count**\ (\ ) |const| [🔗<class_VisualShaderNodeGroupBase_method_get_input_port_count>]

Returns the number of input ports in use. Alternative for [get_free_input_port_id()<class_VisualShaderNodeGroupBase_method_get_free_input_port_id>].


----



[String<class_String>] **get_inputs**\ (\ ) |const| [🔗<class_VisualShaderNodeGroupBase_method_get_inputs>]

Returns a [String<class_String>] description of the input ports as a colon-separated list using the format `id,type,name;` (see [add_input_port()<class_VisualShaderNodeGroupBase_method_add_input_port>]).


----



[int<class_int>] **get_output_port_count**\ (\ ) |const| [🔗<class_VisualShaderNodeGroupBase_method_get_output_port_count>]

Returns the number of output ports in use. Alternative for [get_free_output_port_id()<class_VisualShaderNodeGroupBase_method_get_free_output_port_id>].


----



[String<class_String>] **get_outputs**\ (\ ) |const| [🔗<class_VisualShaderNodeGroupBase_method_get_outputs>]

Returns a [String<class_String>] description of the output ports as a colon-separated list using the format `id,type,name;` (see [add_output_port()<class_VisualShaderNodeGroupBase_method_add_output_port>]).


----



[bool<class_bool>] **has_input_port**\ (\ id\: [int<class_int>]\ ) |const| [🔗<class_VisualShaderNodeGroupBase_method_has_input_port>]

Returns `true` if the specified input port exists.


----



[bool<class_bool>] **has_output_port**\ (\ id\: [int<class_int>]\ ) |const| [🔗<class_VisualShaderNodeGroupBase_method_has_output_port>]

Returns `true` if the specified output port exists.


----



[bool<class_bool>] **is_valid_port_name**\ (\ name\: [String<class_String>]\ ) |const| [🔗<class_VisualShaderNodeGroupBase_method_is_valid_port_name>]

Returns `true` if the specified port name does not override an existed port name and is valid within the shader.


----



|void| **remove_input_port**\ (\ id\: [int<class_int>]\ ) [🔗<class_VisualShaderNodeGroupBase_method_remove_input_port>]

Removes the specified input port.


----



|void| **remove_output_port**\ (\ id\: [int<class_int>]\ ) [🔗<class_VisualShaderNodeGroupBase_method_remove_output_port>]

Removes the specified output port.


----



|void| **set_input_port_name**\ (\ id\: [int<class_int>], name\: [String<class_String>]\ ) [🔗<class_VisualShaderNodeGroupBase_method_set_input_port_name>]

Renames the specified input port.


----



|void| **set_input_port_type**\ (\ id\: [int<class_int>], type\: [int<class_int>]\ ) [🔗<class_VisualShaderNodeGroupBase_method_set_input_port_type>]

Sets the specified input port's type (see [PortType<enum_VisualShaderNode_PortType>]).


----



|void| **set_inputs**\ (\ inputs\: [String<class_String>]\ ) [🔗<class_VisualShaderNodeGroupBase_method_set_inputs>]

Defines all input ports using a [String<class_String>] formatted as a colon-separated list: `id,type,name;` (see [add_input_port()<class_VisualShaderNodeGroupBase_method_add_input_port>]).


----



|void| **set_output_port_name**\ (\ id\: [int<class_int>], name\: [String<class_String>]\ ) [🔗<class_VisualShaderNodeGroupBase_method_set_output_port_name>]

Renames the specified output port.


----



|void| **set_output_port_type**\ (\ id\: [int<class_int>], type\: [int<class_int>]\ ) [🔗<class_VisualShaderNodeGroupBase_method_set_output_port_type>]

Sets the specified output port's type (see [PortType<enum_VisualShaderNode_PortType>]).


----



|void| **set_outputs**\ (\ outputs\: [String<class_String>]\ ) [🔗<class_VisualShaderNodeGroupBase_method_set_outputs>]

Defines all output ports using a [String<class_String>] formatted as a colon-separated list: `id,type,name;` (see [add_output_port()<class_VisualShaderNodeGroupBase_method_add_output_port>]).

