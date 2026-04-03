:github_url: hide



# AnimationNodeStateMachinePlayback

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Provides playback control for an [AnimationNodeStateMachine<class_AnimationNodeStateMachine>].


## Description

Allows control of [AnimationTree<class_AnimationTree>] state machines created with [AnimationNodeStateMachine<class_AnimationNodeStateMachine>]. Retrieve with `$AnimationTree.get("parameters/playback")`.


> **TABS**
>

    var state_machine = $AnimationTree.get("parameters/playback")
    state_machine.travel("some_state")


    var stateMachine = GetNode<AnimationTree>("AnimationTree").Get("parameters/playback").As<AnimationNodeStateMachinePlayback>();
    stateMachine.Travel("some_state");




## Tutorials

- [../tutorials/animation/animation_tree](Using AnimationTree .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------+-------------------------+---------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | resource_local_to_scene | ``true`` (overrides :ref:`Resource<class_Resource_property_resource_local_to_scene>`) |
> +-------------------------+-------------------------+---------------------------------------------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                        | :ref:`get_current_length<class_AnimationNodeStateMachinePlayback_method_get_current_length>`\ (\ ) |const|                                                                    |
> +------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`StringName<class_StringName>`                              | :ref:`get_current_node<class_AnimationNodeStateMachinePlayback_method_get_current_node>`\ (\ ) |const|                                                                        |
> +------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                        | :ref:`get_current_play_position<class_AnimationNodeStateMachinePlayback_method_get_current_play_position>`\ (\ ) |const|                                                      |
> +------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                        | :ref:`get_fading_from_length<class_AnimationNodeStateMachinePlayback_method_get_fading_from_length>`\ (\ ) |const|                                                            |
> +------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`StringName<class_StringName>`                              | :ref:`get_fading_from_node<class_AnimationNodeStateMachinePlayback_method_get_fading_from_node>`\ (\ ) |const|                                                                |
> +------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                        | :ref:`get_fading_from_play_position<class_AnimationNodeStateMachinePlayback_method_get_fading_from_play_position>`\ (\ ) |const|                                              |
> +------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                        | :ref:`get_fading_length<class_AnimationNodeStateMachinePlayback_method_get_fading_length>`\ (\ ) |const|                                                                      |
> +------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                        | :ref:`get_fading_position<class_AnimationNodeStateMachinePlayback_method_get_fading_position>`\ (\ ) |const|                                                                  |
> +------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`StringName<class_StringName>`\] | :ref:`get_travel_path<class_AnimationNodeStateMachinePlayback_method_get_travel_path>`\ (\ ) |const|                                                                          |
> +------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`is_playing<class_AnimationNodeStateMachinePlayback_method_is_playing>`\ (\ ) |const|                                                                                    |
> +------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`next<class_AnimationNodeStateMachinePlayback_method_next>`\ (\ )                                                                                                        |
> +------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`start<class_AnimationNodeStateMachinePlayback_method_start>`\ (\ node\: :ref:`StringName<class_StringName>`, reset\: :ref:`bool<class_bool>` = true\ )                  |
> +------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`stop<class_AnimationNodeStateMachinePlayback_method_stop>`\ (\ )                                                                                                        |
> +------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`travel<class_AnimationNodeStateMachinePlayback_method_travel>`\ (\ to_node\: :ref:`StringName<class_StringName>`, reset_on_teleport\: :ref:`bool<class_bool>` = true\ ) |
> +------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**state_finished**\ (\ state\: [StringName<class_StringName>]\ ) [🔗<class_AnimationNodeStateMachinePlayback_signal_state_finished>]

Emitted when the `state` finishes playback. If `state` is a state machine set to grouped mode, its signals are passed through with its name prefixed.

If there is a crossfade, this will be fired when the influence of the [get_fading_from_node()<class_AnimationNodeStateMachinePlayback_method_get_fading_from_node>] animation is no longer present.


----



**state_started**\ (\ state\: [StringName<class_StringName>]\ ) [🔗<class_AnimationNodeStateMachinePlayback_signal_state_started>]

Emitted when the `state` starts playback. If `state` is a state machine set to grouped mode, its signals are passed through with its name prefixed.


----


## Method Descriptions



[float<class_float>] **get_current_length**\ (\ ) |const| [🔗<class_AnimationNodeStateMachinePlayback_method_get_current_length>]

Returns the current state length.

\ **Note:** It is possible that any [AnimationRootNode<class_AnimationRootNode>] can be nodes as well as animations. This means that there can be multiple animations within a single state. Which animation length has priority depends on the nodes connected inside it. Also, if a transition does not reset, the remaining length at that point will be returned.


----



[StringName<class_StringName>] **get_current_node**\ (\ ) |const| [🔗<class_AnimationNodeStateMachinePlayback_method_get_current_node>]

Returns the currently playing animation state.

\ **Note:** When using a cross-fade, the current state changes to the next state immediately after the cross-fade begins.


----



[float<class_float>] **get_current_play_position**\ (\ ) |const| [🔗<class_AnimationNodeStateMachinePlayback_method_get_current_play_position>]

Returns the playback position within the current animation state.


----



[float<class_float>] **get_fading_from_length**\ (\ ) |const| [🔗<class_AnimationNodeStateMachinePlayback_method_get_fading_from_length>]

Returns the playback state length of the node from [get_fading_from_node()<class_AnimationNodeStateMachinePlayback_method_get_fading_from_node>]. Returns `0` if no animation fade is occurring.


----



[StringName<class_StringName>] **get_fading_from_node**\ (\ ) |const| [🔗<class_AnimationNodeStateMachinePlayback_method_get_fading_from_node>]

Returns the starting state of currently fading animation.


----



[float<class_float>] **get_fading_from_play_position**\ (\ ) |const| [🔗<class_AnimationNodeStateMachinePlayback_method_get_fading_from_play_position>]

Returns the playback position of the node from [get_fading_from_node()<class_AnimationNodeStateMachinePlayback_method_get_fading_from_node>]. Returns `0` if no animation fade is occurring.


----



[float<class_float>] **get_fading_length**\ (\ ) |const| [🔗<class_AnimationNodeStateMachinePlayback_method_get_fading_length>]

Returns the length of the current fade animation. Returns `0` if no animation fade is occurring.


----



[float<class_float>] **get_fading_position**\ (\ ) |const| [🔗<class_AnimationNodeStateMachinePlayback_method_get_fading_position>]

Returns the playback position of the current fade animation. Returns `0` if no animation fade is occurring.


----



[Array<class_Array>]\[[StringName<class_StringName>]\] **get_travel_path**\ (\ ) |const| [🔗<class_AnimationNodeStateMachinePlayback_method_get_travel_path>]

Returns the current travel path as computed internally by the A\* algorithm.


----



[bool<class_bool>] **is_playing**\ (\ ) |const| [🔗<class_AnimationNodeStateMachinePlayback_method_is_playing>]

Returns `true` if an animation is playing.


----



|void| **next**\ (\ ) [🔗<class_AnimationNodeStateMachinePlayback_method_next>]

If there is a next path by travel or auto advance, immediately transitions from the current state to the next state.


----



|void| **start**\ (\ node\: [StringName<class_StringName>], reset\: [bool<class_bool>] = true\ ) [🔗<class_AnimationNodeStateMachinePlayback_method_start>]

Starts playing the given animation.

If `reset` is `true`, the animation is played from the beginning.


----



|void| **stop**\ (\ ) [🔗<class_AnimationNodeStateMachinePlayback_method_stop>]

Stops the currently playing animation.


----



|void| **travel**\ (\ to_node\: [StringName<class_StringName>], reset_on_teleport\: [bool<class_bool>] = true\ ) [🔗<class_AnimationNodeStateMachinePlayback_method_travel>]

Transitions from the current state to another one, following the shortest path.

If the path does not connect from the current state, the animation will play after the state teleports.

If `reset_on_teleport` is `true`, the animation is played from the beginning when the travel cause a teleportation.

