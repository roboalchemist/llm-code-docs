:github_url: hide



# AnimationNode

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [AnimationNodeExtension<class_AnimationNodeExtension>], [AnimationNodeOutput<class_AnimationNodeOutput>], [AnimationNodeSync<class_AnimationNodeSync>], [AnimationNodeTimeScale<class_AnimationNodeTimeScale>], [AnimationNodeTimeSeek<class_AnimationNodeTimeSeek>], [AnimationRootNode<class_AnimationRootNode>]

Base class for [AnimationTree<class_AnimationTree>] nodes. Not related to scene nodes.


## Description

Base resource for [AnimationTree<class_AnimationTree>] nodes. In general, it's not used directly, but you can create custom ones with custom blending formulas.

Inherit this when creating animation nodes mainly for use in [AnimationNodeBlendTree<class_AnimationNodeBlendTree>], otherwise [AnimationRootNode<class_AnimationRootNode>] should be used instead.

You can access the time information as read-only parameter which is processed and stored in the previous frame for all nodes except [AnimationNodeOutput<class_AnimationNodeOutput>].

\ **Note:** If multiple inputs exist in the **AnimationNode**, which time information takes precedence depends on the type of **AnimationNode**.

::

    var current_length = $AnimationTree["parameters/AnimationNodeName/current_length"]
    var current_position = $AnimationTree["parameters/AnimationNodeName/current_position"]
    var current_delta = $AnimationTree["parameters/AnimationNodeName/current_delta"]


## Tutorials

- [../tutorials/animation/animation_tree](Using AnimationTree .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------+--------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`filter_enabled<class_AnimationNode_property_filter_enabled>` |
> +-------------------------+--------------------------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`               | :ref:`_get_caption<class_AnimationNode_private_method__get_caption>`\ (\ ) |virtual| |const|                                                                                                                                                                                                                                                                                                                                                                            |
> +-------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`AnimationNode<class_AnimationNode>` | :ref:`_get_child_by_name<class_AnimationNode_private_method__get_child_by_name>`\ (\ name\: :ref:`StringName<class_StringName>`\ ) |virtual| |const|                                                                                                                                                                                                                                                                                                                    |
> +-------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Dictionary<class_Dictionary>`       | :ref:`_get_child_nodes<class_AnimationNode_private_method__get_child_nodes>`\ (\ ) |virtual| |const|                                                                                                                                                                                                                                                                                                                                                                    |
> +-------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>`             | :ref:`_get_parameter_default_value<class_AnimationNode_private_method__get_parameter_default_value>`\ (\ parameter\: :ref:`StringName<class_StringName>`\ ) |virtual| |const|                                                                                                                                                                                                                                                                                           |
> +-------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`                 | :ref:`_get_parameter_list<class_AnimationNode_private_method__get_parameter_list>`\ (\ ) |virtual| |const|                                                                                                                                                                                                                                                                                                                                                              |
> +-------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                   | :ref:`_has_filter<class_AnimationNode_private_method__has_filter>`\ (\ ) |virtual| |const|                                                                                                                                                                                                                                                                                                                                                                              |
> +-------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                   | :ref:`_is_parameter_read_only<class_AnimationNode_private_method__is_parameter_read_only>`\ (\ parameter\: :ref:`StringName<class_StringName>`\ ) |virtual| |const|                                                                                                                                                                                                                                                                                                     |
> +-------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                 | :ref:`_process<class_AnimationNode_private_method__process>`\ (\ time\: :ref:`float<class_float>`, seek\: :ref:`bool<class_bool>`, is_external_seeking\: :ref:`bool<class_bool>`, test_only\: :ref:`bool<class_bool>`\ ) |virtual|                                                                                                                                                                                                                                      |
> +-------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                   | :ref:`add_input<class_AnimationNode_method_add_input>`\ (\ name\: :ref:`String<class_String>`\ )                                                                                                                                                                                                                                                                                                                                                                        |
> +-------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                    | :ref:`blend_animation<class_AnimationNode_method_blend_animation>`\ (\ animation\: :ref:`StringName<class_StringName>`, time\: :ref:`float<class_float>`, delta\: :ref:`float<class_float>`, seeked\: :ref:`bool<class_bool>`, is_external_seeking\: :ref:`bool<class_bool>`, blend\: :ref:`float<class_float>`, looped_flag\: :ref:`LoopedFlag<enum_Animation_LoopedFlag>` = 0\ )                                                                                      |
> +-------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                 | :ref:`blend_input<class_AnimationNode_method_blend_input>`\ (\ input_index\: :ref:`int<class_int>`, time\: :ref:`float<class_float>`, seek\: :ref:`bool<class_bool>`, is_external_seeking\: :ref:`bool<class_bool>`, blend\: :ref:`float<class_float>`, filter\: :ref:`FilterAction<enum_AnimationNode_FilterAction>` = 0, sync\: :ref:`bool<class_bool>` = true, test_only\: :ref:`bool<class_bool>` = false\ )                                                        |
> +-------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                 | :ref:`blend_node<class_AnimationNode_method_blend_node>`\ (\ name\: :ref:`StringName<class_StringName>`, node\: :ref:`AnimationNode<class_AnimationNode>`, time\: :ref:`float<class_float>`, seek\: :ref:`bool<class_bool>`, is_external_seeking\: :ref:`bool<class_bool>`, blend\: :ref:`float<class_float>`, filter\: :ref:`FilterAction<enum_AnimationNode_FilterAction>` = 0, sync\: :ref:`bool<class_bool>` = true, test_only\: :ref:`bool<class_bool>` = false\ ) |
> +-------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                     | :ref:`find_input<class_AnimationNode_method_find_input>`\ (\ name\: :ref:`String<class_String>`\ ) |const|                                                                                                                                                                                                                                                                                                                                                              |
> +-------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                     | :ref:`get_input_count<class_AnimationNode_method_get_input_count>`\ (\ ) |const|                                                                                                                                                                                                                                                                                                                                                                                        |
> +-------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`               | :ref:`get_input_name<class_AnimationNode_method_get_input_name>`\ (\ input\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                                                                                                                                                                                                                           |
> +-------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>`             | :ref:`get_parameter<class_AnimationNode_method_get_parameter>`\ (\ name\: :ref:`StringName<class_StringName>`\ ) |const|                                                                                                                                                                                                                                                                                                                                                |
> +-------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                     | :ref:`get_processing_animation_tree_instance_id<class_AnimationNode_method_get_processing_animation_tree_instance_id>`\ (\ ) |const|                                                                                                                                                                                                                                                                                                                                    |
> +-------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                   | :ref:`is_path_filtered<class_AnimationNode_method_is_path_filtered>`\ (\ path\: :ref:`NodePath<class_NodePath>`\ ) |const|                                                                                                                                                                                                                                                                                                                                              |
> +-------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                   | :ref:`is_process_testing<class_AnimationNode_method_is_process_testing>`\ (\ ) |const|                                                                                                                                                                                                                                                                                                                                                                                  |
> +-------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                    | :ref:`remove_input<class_AnimationNode_method_remove_input>`\ (\ index\: :ref:`int<class_int>`\ )                                                                                                                                                                                                                                                                                                                                                                       |
> +-------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                    | :ref:`set_filter_path<class_AnimationNode_method_set_filter_path>`\ (\ path\: :ref:`NodePath<class_NodePath>`, enable\: :ref:`bool<class_bool>`\ )                                                                                                                                                                                                                                                                                                                      |
> +-------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                   | :ref:`set_input_name<class_AnimationNode_method_set_input_name>`\ (\ input\: :ref:`int<class_int>`, name\: :ref:`String<class_String>`\ )                                                                                                                                                                                                                                                                                                                               |
> +-------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                    | :ref:`set_parameter<class_AnimationNode_method_set_parameter>`\ (\ name\: :ref:`StringName<class_StringName>`, value\: :ref:`Variant<class_Variant>`\ )                                                                                                                                                                                                                                                                                                                 |
> +-------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**animation_node_removed**\ (\ object_id\: [int<class_int>], name\: [String<class_String>]\ ) [🔗<class_AnimationNode_signal_animation_node_removed>]

Emitted by nodes that inherit from this class and that have an internal tree when one of their animation nodes removes. The animation nodes that emit this signal are [AnimationNodeBlendSpace1D<class_AnimationNodeBlendSpace1D>], [AnimationNodeBlendSpace2D<class_AnimationNodeBlendSpace2D>], [AnimationNodeStateMachine<class_AnimationNodeStateMachine>], and [AnimationNodeBlendTree<class_AnimationNodeBlendTree>].


----



**animation_node_renamed**\ (\ object_id\: [int<class_int>], old_name\: [String<class_String>], new_name\: [String<class_String>]\ ) [🔗<class_AnimationNode_signal_animation_node_renamed>]

Emitted by nodes that inherit from this class and that have an internal tree when one of their animation node names changes. The animation nodes that emit this signal are [AnimationNodeBlendSpace1D<class_AnimationNodeBlendSpace1D>], [AnimationNodeBlendSpace2D<class_AnimationNodeBlendSpace2D>], [AnimationNodeStateMachine<class_AnimationNodeStateMachine>], and [AnimationNodeBlendTree<class_AnimationNodeBlendTree>].


----



**tree_changed**\ (\ ) [🔗<class_AnimationNode_signal_tree_changed>]

Emitted by nodes that inherit from this class and that have an internal tree when one of their animation nodes changes. The animation nodes that emit this signal are [AnimationNodeBlendSpace1D<class_AnimationNodeBlendSpace1D>], [AnimationNodeBlendSpace2D<class_AnimationNodeBlendSpace2D>], [AnimationNodeStateMachine<class_AnimationNodeStateMachine>], [AnimationNodeBlendTree<class_AnimationNodeBlendTree>] and [AnimationNodeTransition<class_AnimationNodeTransition>].


----


## Enumerations



enum **FilterAction**: [🔗<enum_AnimationNode_FilterAction>]



[FilterAction<enum_AnimationNode_FilterAction>] **FILTER_IGNORE** = `0`

Do not use filtering.



[FilterAction<enum_AnimationNode_FilterAction>] **FILTER_PASS** = `1`

Paths matching the filter will be allowed to pass.



[FilterAction<enum_AnimationNode_FilterAction>] **FILTER_STOP** = `2`

Paths matching the filter will be discarded.



[FilterAction<enum_AnimationNode_FilterAction>] **FILTER_BLEND** = `3`

Paths matching the filter will be blended (by the blend value).


----


## Property Descriptions



[bool<class_bool>] **filter_enabled** [🔗<class_AnimationNode_property_filter_enabled>]


- |void| **set_filter_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_filter_enabled**\ (\ )

If `true`, filtering is enabled.


----


## Method Descriptions



[String<class_String>] **_get_caption**\ (\ ) |virtual| |const| [🔗<class_AnimationNode_private_method__get_caption>]

When inheriting from [AnimationRootNode<class_AnimationRootNode>], implement this virtual method to override the text caption for this animation node.


----



[AnimationNode<class_AnimationNode>] **_get_child_by_name**\ (\ name\: [StringName<class_StringName>]\ ) |virtual| |const| [🔗<class_AnimationNode_private_method__get_child_by_name>]

When inheriting from [AnimationRootNode<class_AnimationRootNode>], implement this virtual method to return a child animation node by its `name`.


----



[Dictionary<class_Dictionary>] **_get_child_nodes**\ (\ ) |virtual| |const| [🔗<class_AnimationNode_private_method__get_child_nodes>]

When inheriting from [AnimationRootNode<class_AnimationRootNode>], implement this virtual method to return all child animation nodes in order as a `name: node` dictionary.


----



[Variant<class_Variant>] **_get_parameter_default_value**\ (\ parameter\: [StringName<class_StringName>]\ ) |virtual| |const| [🔗<class_AnimationNode_private_method__get_parameter_default_value>]

When inheriting from [AnimationRootNode<class_AnimationRootNode>], implement this virtual method to return the default value of a `parameter`. Parameters are custom local memory used for your animation nodes, given a resource can be reused in multiple trees.


----



[Array<class_Array>] **_get_parameter_list**\ (\ ) |virtual| |const| [🔗<class_AnimationNode_private_method__get_parameter_list>]

When inheriting from [AnimationRootNode<class_AnimationRootNode>], implement this virtual method to return a list of the properties on this animation node. Parameters are custom local memory used for your animation nodes, given a resource can be reused in multiple trees. Format is similar to [Object.get_property_list()<class_Object_method_get_property_list>].


----



[bool<class_bool>] **_has_filter**\ (\ ) |virtual| |const| [🔗<class_AnimationNode_private_method__has_filter>]

When inheriting from [AnimationRootNode<class_AnimationRootNode>], implement this virtual method to return whether the blend tree editor should display filter editing on this animation node.


----



[bool<class_bool>] **_is_parameter_read_only**\ (\ parameter\: [StringName<class_StringName>]\ ) |virtual| |const| [🔗<class_AnimationNode_private_method__is_parameter_read_only>]

When inheriting from [AnimationRootNode<class_AnimationRootNode>], implement this virtual method to return whether the `parameter` is read-only. Parameters are custom local memory used for your animation nodes, given a resource can be reused in multiple trees.


----



[float<class_float>] **_process**\ (\ time\: [float<class_float>], seek\: [bool<class_bool>], is_external_seeking\: [bool<class_bool>], test_only\: [bool<class_bool>]\ ) |virtual| [🔗<class_AnimationNode_private_method__process>]

**Deprecated:** Currently this is mostly useless as there is a lack of many APIs to extend AnimationNode by GDScript. It is planned that a more flexible API using structures will be provided in the future.

When inheriting from [AnimationRootNode<class_AnimationRootNode>], implement this virtual method to run some code when this animation node is processed. The `time` parameter is a relative delta, unless `seek` is `true`, in which case it is absolute.

Here, call the [blend_input()<class_AnimationNode_method_blend_input>], [blend_node()<class_AnimationNode_method_blend_node>] or [blend_animation()<class_AnimationNode_method_blend_animation>] functions. You can also use [get_parameter()<class_AnimationNode_method_get_parameter>] and [set_parameter()<class_AnimationNode_method_set_parameter>] to modify local memory.

This function should return the delta.


----



[bool<class_bool>] **add_input**\ (\ name\: [String<class_String>]\ ) [🔗<class_AnimationNode_method_add_input>]

Adds an input to the animation node. This is only useful for animation nodes created for use in an [AnimationNodeBlendTree<class_AnimationNodeBlendTree>]. If the addition fails, returns `false`.


----



|void| **blend_animation**\ (\ animation\: [StringName<class_StringName>], time\: [float<class_float>], delta\: [float<class_float>], seeked\: [bool<class_bool>], is_external_seeking\: [bool<class_bool>], blend\: [float<class_float>], looped_flag\: [LoopedFlag<enum_Animation_LoopedFlag>] = 0\ ) [🔗<class_AnimationNode_method_blend_animation>]

Blends an animation by `blend` amount (name must be valid in the linked [AnimationPlayer<class_AnimationPlayer>]). A `time` and `delta` may be passed, as well as whether `seeked` happened.

A `looped_flag` is used by internal processing immediately after the loop.


----



[float<class_float>] **blend_input**\ (\ input_index\: [int<class_int>], time\: [float<class_float>], seek\: [bool<class_bool>], is_external_seeking\: [bool<class_bool>], blend\: [float<class_float>], filter\: [FilterAction<enum_AnimationNode_FilterAction>] = 0, sync\: [bool<class_bool>] = true, test_only\: [bool<class_bool>] = false\ ) [🔗<class_AnimationNode_method_blend_input>]

Blends an input. This is only useful for animation nodes created for an [AnimationNodeBlendTree<class_AnimationNodeBlendTree>]. The `time` parameter is a relative delta, unless `seek` is `true`, in which case it is absolute. A filter mode may be optionally passed.


----



[float<class_float>] **blend_node**\ (\ name\: [StringName<class_StringName>], node\: [AnimationNode<class_AnimationNode>], time\: [float<class_float>], seek\: [bool<class_bool>], is_external_seeking\: [bool<class_bool>], blend\: [float<class_float>], filter\: [FilterAction<enum_AnimationNode_FilterAction>] = 0, sync\: [bool<class_bool>] = true, test_only\: [bool<class_bool>] = false\ ) [🔗<class_AnimationNode_method_blend_node>]

Blend another animation node (in case this animation node contains child animation nodes). This function is only useful if you inherit from [AnimationRootNode<class_AnimationRootNode>] instead, otherwise editors will not display your animation node for addition.


----



[int<class_int>] **find_input**\ (\ name\: [String<class_String>]\ ) |const| [🔗<class_AnimationNode_method_find_input>]

Returns the input index which corresponds to `name`. If not found, returns `-1`.


----



[int<class_int>] **get_input_count**\ (\ ) |const| [🔗<class_AnimationNode_method_get_input_count>]

Amount of inputs in this animation node, only useful for animation nodes that go into [AnimationNodeBlendTree<class_AnimationNodeBlendTree>].


----



[String<class_String>] **get_input_name**\ (\ input\: [int<class_int>]\ ) |const| [🔗<class_AnimationNode_method_get_input_name>]

Gets the name of an input by index.


----



[Variant<class_Variant>] **get_parameter**\ (\ name\: [StringName<class_StringName>]\ ) |const| [🔗<class_AnimationNode_method_get_parameter>]

Gets the value of a parameter. Parameters are custom local memory used for your animation nodes, given a resource can be reused in multiple trees.


----



[int<class_int>] **get_processing_animation_tree_instance_id**\ (\ ) |const| [🔗<class_AnimationNode_method_get_processing_animation_tree_instance_id>]

Returns the object id of the [AnimationTree<class_AnimationTree>] that owns this node.

\ **Note:** This method should only be called from within the [AnimationNodeExtension._process_animation_node()<class_AnimationNodeExtension_private_method__process_animation_node>] method, and will return an invalid id otherwise.


----



[bool<class_bool>] **is_path_filtered**\ (\ path\: [NodePath<class_NodePath>]\ ) |const| [🔗<class_AnimationNode_method_is_path_filtered>]

Returns `true` if the given path is filtered.


----



[bool<class_bool>] **is_process_testing**\ (\ ) |const| [🔗<class_AnimationNode_method_is_process_testing>]

Returns `true` if this animation node is being processed in test-only mode.


----



|void| **remove_input**\ (\ index\: [int<class_int>]\ ) [🔗<class_AnimationNode_method_remove_input>]

Removes an input, call this only when inactive.


----



|void| **set_filter_path**\ (\ path\: [NodePath<class_NodePath>], enable\: [bool<class_bool>]\ ) [🔗<class_AnimationNode_method_set_filter_path>]

Adds or removes a path for the filter.


----



[bool<class_bool>] **set_input_name**\ (\ input\: [int<class_int>], name\: [String<class_String>]\ ) [🔗<class_AnimationNode_method_set_input_name>]

Sets the name of the input at the given `input` index. If the setting fails, returns `false`.


----



|void| **set_parameter**\ (\ name\: [StringName<class_StringName>], value\: [Variant<class_Variant>]\ ) [🔗<class_AnimationNode_method_set_parameter>]

Sets a custom parameter. These are used as local memory, because resources can be reused across the tree or scenes.

