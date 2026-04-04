:github_url: hide



# AnimationNodeStateMachine

**Inherits:** [AnimationRootNode<class_AnimationRootNode>] **<** [AnimationNode<class_AnimationNode>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A state machine with multiple [AnimationRootNode<class_AnimationRootNode>]\ s, used by [AnimationTree<class_AnimationTree>].


## Description

Contains multiple [AnimationRootNode<class_AnimationRootNode>]\ s representing animation states, connected in a graph. State transitions can be configured to happen automatically or via code, using a shortest-path algorithm. Retrieve the [AnimationNodeStateMachinePlayback<class_AnimationNodeStateMachinePlayback>] object from the [AnimationTree<class_AnimationTree>] node to control it programmatically.


> **TABS**
>

    var state_machine = $AnimationTree.get("parameters/playback")
    state_machine.travel("some_state")


    var stateMachine = GetNode<AnimationTree>("AnimationTree").Get("parameters/playback") as AnimationNodeStateMachinePlayback;
    stateMachine.Travel("some_state");




## Tutorials

- [../tutorials/animation/animation_tree](Using AnimationTree .md)


## Properties

> **TABLE**
> :widths: auto
>
> +--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                                                  | :ref:`allow_transition_to_self<class_AnimationNodeStateMachine_property_allow_transition_to_self>` | ``false`` |
> +--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                                                  | :ref:`reset_ends<class_AnimationNodeStateMachine_property_reset_ends>`                             | ``false`` |
> +--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+-----------+
> | :ref:`StateMachineType<enum_AnimationNodeStateMachine_StateMachineType>` | :ref:`state_machine_type<class_AnimationNodeStateMachine_property_state_machine_type>`             | ``0``     |
> +--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+-----------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                                | :ref:`add_node<class_AnimationNodeStateMachine_method_add_node>`\ (\ name\: :ref:`StringName<class_StringName>`, node\: :ref:`AnimationNode<class_AnimationNode>`, position\: :ref:`Vector2<class_Vector2>` = Vector2(0, 0)\ )                                               |
> +---------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                                | :ref:`add_transition<class_AnimationNodeStateMachine_method_add_transition>`\ (\ from\: :ref:`StringName<class_StringName>`, to\: :ref:`StringName<class_StringName>`, transition\: :ref:`AnimationNodeStateMachineTransition<class_AnimationNodeStateMachineTransition>`\ ) |
> +---------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>`                                                         | :ref:`get_graph_offset<class_AnimationNodeStateMachine_method_get_graph_offset>`\ (\ ) |const|                                                                                                                                                                               |
> +---------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`AnimationNode<class_AnimationNode>`                                             | :ref:`get_node<class_AnimationNodeStateMachine_method_get_node>`\ (\ name\: :ref:`StringName<class_StringName>`\ ) |const|                                                                                                                                                   |
> +---------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`StringName<class_StringName>`\]                      | :ref:`get_node_list<class_AnimationNodeStateMachine_method_get_node_list>`\ (\ ) |const|                                                                                                                                                                                     |
> +---------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`StringName<class_StringName>`                                                   | :ref:`get_node_name<class_AnimationNodeStateMachine_method_get_node_name>`\ (\ node\: :ref:`AnimationNode<class_AnimationNode>`\ ) |const|                                                                                                                                   |
> +---------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>`                                                         | :ref:`get_node_position<class_AnimationNodeStateMachine_method_get_node_position>`\ (\ name\: :ref:`StringName<class_StringName>`\ ) |const|                                                                                                                                 |
> +---------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`AnimationNodeStateMachineTransition<class_AnimationNodeStateMachineTransition>` | :ref:`get_transition<class_AnimationNodeStateMachine_method_get_transition>`\ (\ idx\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                      |
> +---------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                                                 | :ref:`get_transition_count<class_AnimationNodeStateMachine_method_get_transition_count>`\ (\ ) |const|                                                                                                                                                                       |
> +---------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`StringName<class_StringName>`                                                   | :ref:`get_transition_from<class_AnimationNodeStateMachine_method_get_transition_from>`\ (\ idx\: :ref:`int<class_int>`\ ) |const|                                                                                                                                            |
> +---------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`StringName<class_StringName>`                                                   | :ref:`get_transition_to<class_AnimationNodeStateMachine_method_get_transition_to>`\ (\ idx\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                |
> +---------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                                               | :ref:`has_node<class_AnimationNodeStateMachine_method_has_node>`\ (\ name\: :ref:`StringName<class_StringName>`\ ) |const|                                                                                                                                                   |
> +---------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                                               | :ref:`has_transition<class_AnimationNodeStateMachine_method_has_transition>`\ (\ from\: :ref:`StringName<class_StringName>`, to\: :ref:`StringName<class_StringName>`\ ) |const|                                                                                             |
> +---------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                                | :ref:`remove_node<class_AnimationNodeStateMachine_method_remove_node>`\ (\ name\: :ref:`StringName<class_StringName>`\ )                                                                                                                                                     |
> +---------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                                | :ref:`remove_transition<class_AnimationNodeStateMachine_method_remove_transition>`\ (\ from\: :ref:`StringName<class_StringName>`, to\: :ref:`StringName<class_StringName>`\ )                                                                                               |
> +---------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                                | :ref:`remove_transition_by_index<class_AnimationNodeStateMachine_method_remove_transition_by_index>`\ (\ idx\: :ref:`int<class_int>`\ )                                                                                                                                      |
> +---------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                                | :ref:`rename_node<class_AnimationNodeStateMachine_method_rename_node>`\ (\ name\: :ref:`StringName<class_StringName>`, new_name\: :ref:`StringName<class_StringName>`\ )                                                                                                     |
> +---------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                                | :ref:`replace_node<class_AnimationNodeStateMachine_method_replace_node>`\ (\ name\: :ref:`StringName<class_StringName>`, node\: :ref:`AnimationNode<class_AnimationNode>`\ )                                                                                                 |
> +---------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                                | :ref:`set_graph_offset<class_AnimationNodeStateMachine_method_set_graph_offset>`\ (\ offset\: :ref:`Vector2<class_Vector2>`\ )                                                                                                                                               |
> +---------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                                | :ref:`set_node_position<class_AnimationNodeStateMachine_method_set_node_position>`\ (\ name\: :ref:`StringName<class_StringName>`, position\: :ref:`Vector2<class_Vector2>`\ )                                                                                               |
> +---------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **StateMachineType**: [🔗<enum_AnimationNodeStateMachine_StateMachineType>]



[StateMachineType<enum_AnimationNodeStateMachine_StateMachineType>] **STATE_MACHINE_TYPE_ROOT** = `0`

Seeking to the beginning is treated as playing from the start state. Transition to the end state is treated as exiting the state machine.



[StateMachineType<enum_AnimationNodeStateMachine_StateMachineType>] **STATE_MACHINE_TYPE_NESTED** = `1`

Seeking to the beginning is treated as seeking to the beginning of the animation in the current state. Transition to the end state, or the absence of transitions in each state, is treated as exiting the state machine.



[StateMachineType<enum_AnimationNodeStateMachine_StateMachineType>] **STATE_MACHINE_TYPE_GROUPED** = `2`

This is a grouped state machine that can be controlled from a parent state machine. It does not work independently. There must be a state machine with [state_machine_type<class_AnimationNodeStateMachine_property_state_machine_type>] of [STATE_MACHINE_TYPE_ROOT<class_AnimationNodeStateMachine_constant_STATE_MACHINE_TYPE_ROOT>] or [STATE_MACHINE_TYPE_NESTED<class_AnimationNodeStateMachine_constant_STATE_MACHINE_TYPE_NESTED>] in the parent or ancestor.


----


## Property Descriptions



[bool<class_bool>] **allow_transition_to_self** = `false` [🔗<class_AnimationNodeStateMachine_property_allow_transition_to_self>]


- |void| **set_allow_transition_to_self**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_allow_transition_to_self**\ (\ )

If `true`, allows teleport to the self state with [AnimationNodeStateMachinePlayback.travel()<class_AnimationNodeStateMachinePlayback_method_travel>]. When the reset option is enabled in [AnimationNodeStateMachinePlayback.travel()<class_AnimationNodeStateMachinePlayback_method_travel>], the animation is restarted. If `false`, nothing happens on the teleportation to the self state.


----



[bool<class_bool>] **reset_ends** = `false` [🔗<class_AnimationNodeStateMachine_property_reset_ends>]


- |void| **set_reset_ends**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **are_ends_reset**\ (\ )

If `true`, treat the cross-fade to the start and end nodes as a blend with the RESET animation.

In most cases, when additional cross-fades are performed in the parent [AnimationNode<class_AnimationNode>] of the state machine, setting this property to `false` and matching the cross-fade time of the parent [AnimationNode<class_AnimationNode>] and the state machine's start node and end node gives good results.


----



[StateMachineType<enum_AnimationNodeStateMachine_StateMachineType>] **state_machine_type** = `0` [🔗<class_AnimationNodeStateMachine_property_state_machine_type>]


- |void| **set_state_machine_type**\ (\ value\: [StateMachineType<enum_AnimationNodeStateMachine_StateMachineType>]\ )
- [StateMachineType<enum_AnimationNodeStateMachine_StateMachineType>] **get_state_machine_type**\ (\ )

This property can define the process of transitions for different use cases. See also [StateMachineType<enum_AnimationNodeStateMachine_StateMachineType>].


----


## Method Descriptions



|void| **add_node**\ (\ name\: [StringName<class_StringName>], node\: [AnimationNode<class_AnimationNode>], position\: [Vector2<class_Vector2>] = Vector2(0, 0)\ ) [🔗<class_AnimationNodeStateMachine_method_add_node>]

Adds a new animation node to the graph. The `position` is used for display in the editor.


----



|void| **add_transition**\ (\ from\: [StringName<class_StringName>], to\: [StringName<class_StringName>], transition\: [AnimationNodeStateMachineTransition<class_AnimationNodeStateMachineTransition>]\ ) [🔗<class_AnimationNodeStateMachine_method_add_transition>]

Adds a transition between the given animation nodes.


----



[Vector2<class_Vector2>] **get_graph_offset**\ (\ ) |const| [🔗<class_AnimationNodeStateMachine_method_get_graph_offset>]

Returns the draw offset of the graph. Used for display in the editor.


----



[AnimationNode<class_AnimationNode>] **get_node**\ (\ name\: [StringName<class_StringName>]\ ) |const| [🔗<class_AnimationNodeStateMachine_method_get_node>]

Returns the animation node with the given name.


----



[Array<class_Array>]\[[StringName<class_StringName>]\] **get_node_list**\ (\ ) |const| [🔗<class_AnimationNodeStateMachine_method_get_node_list>]

Returns a list containing the names of all animation nodes in this state machine.


----



[StringName<class_StringName>] **get_node_name**\ (\ node\: [AnimationNode<class_AnimationNode>]\ ) |const| [🔗<class_AnimationNodeStateMachine_method_get_node_name>]

Returns the given animation node's name.


----



[Vector2<class_Vector2>] **get_node_position**\ (\ name\: [StringName<class_StringName>]\ ) |const| [🔗<class_AnimationNodeStateMachine_method_get_node_position>]

Returns the given animation node's coordinates. Used for display in the editor.


----



[AnimationNodeStateMachineTransition<class_AnimationNodeStateMachineTransition>] **get_transition**\ (\ idx\: [int<class_int>]\ ) |const| [🔗<class_AnimationNodeStateMachine_method_get_transition>]

Returns the given transition.


----



[int<class_int>] **get_transition_count**\ (\ ) |const| [🔗<class_AnimationNodeStateMachine_method_get_transition_count>]

Returns the number of connections in the graph.


----



[StringName<class_StringName>] **get_transition_from**\ (\ idx\: [int<class_int>]\ ) |const| [🔗<class_AnimationNodeStateMachine_method_get_transition_from>]

Returns the given transition's start node.


----



[StringName<class_StringName>] **get_transition_to**\ (\ idx\: [int<class_int>]\ ) |const| [🔗<class_AnimationNodeStateMachine_method_get_transition_to>]

Returns the given transition's end node.


----



[bool<class_bool>] **has_node**\ (\ name\: [StringName<class_StringName>]\ ) |const| [🔗<class_AnimationNodeStateMachine_method_has_node>]

Returns `true` if the graph contains the given animation node.


----



[bool<class_bool>] **has_transition**\ (\ from\: [StringName<class_StringName>], to\: [StringName<class_StringName>]\ ) |const| [🔗<class_AnimationNodeStateMachine_method_has_transition>]

Returns `true` if there is a transition between the given animation nodes.


----



|void| **remove_node**\ (\ name\: [StringName<class_StringName>]\ ) [🔗<class_AnimationNodeStateMachine_method_remove_node>]

Deletes the given animation node from the graph.


----



|void| **remove_transition**\ (\ from\: [StringName<class_StringName>], to\: [StringName<class_StringName>]\ ) [🔗<class_AnimationNodeStateMachine_method_remove_transition>]

Deletes the transition between the two specified animation nodes.


----



|void| **remove_transition_by_index**\ (\ idx\: [int<class_int>]\ ) [🔗<class_AnimationNodeStateMachine_method_remove_transition_by_index>]

Deletes the given transition by index.


----



|void| **rename_node**\ (\ name\: [StringName<class_StringName>], new_name\: [StringName<class_StringName>]\ ) [🔗<class_AnimationNodeStateMachine_method_rename_node>]

Renames the given animation node.


----



|void| **replace_node**\ (\ name\: [StringName<class_StringName>], node\: [AnimationNode<class_AnimationNode>]\ ) [🔗<class_AnimationNodeStateMachine_method_replace_node>]

Replaces the given animation node with a new animation node.


----



|void| **set_graph_offset**\ (\ offset\: [Vector2<class_Vector2>]\ ) [🔗<class_AnimationNodeStateMachine_method_set_graph_offset>]

Sets the draw offset of the graph. Used for display in the editor.


----



|void| **set_node_position**\ (\ name\: [StringName<class_StringName>], position\: [Vector2<class_Vector2>]\ ) [🔗<class_AnimationNodeStateMachine_method_set_node_position>]

Sets the animation node's coordinates. Used for display in the editor.

