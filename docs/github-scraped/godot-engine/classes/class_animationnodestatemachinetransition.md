:github_url: hide



# AnimationNodeStateMachineTransition

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A transition within an [AnimationNodeStateMachine<class_AnimationNodeStateMachine>] connecting two [AnimationRootNode<class_AnimationRootNode>]\ s.


## Description

The path generated when using [AnimationNodeStateMachinePlayback.travel()<class_AnimationNodeStateMachinePlayback_method_travel>] is limited to the nodes connected by **AnimationNodeStateMachineTransition**.

You can set the timing and conditions of the transition in detail.


## Tutorials

- [../tutorials/animation/animation_tree](Using AnimationTree .md)


## Properties

> **TABLE**
> :widths: auto
>
> +--------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+-----------+
> | :ref:`StringName<class_StringName>`                                      | :ref:`advance_condition<class_AnimationNodeStateMachineTransition_property_advance_condition>`   | ``&""``   |
> +--------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+-----------+
> | :ref:`String<class_String>`                                              | :ref:`advance_expression<class_AnimationNodeStateMachineTransition_property_advance_expression>` | ``""``    |
> +--------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+-----------+
> | :ref:`AdvanceMode<enum_AnimationNodeStateMachineTransition_AdvanceMode>` | :ref:`advance_mode<class_AnimationNodeStateMachineTransition_property_advance_mode>`             | ``1``     |
> +--------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                                                  | :ref:`break_loop_at_end<class_AnimationNodeStateMachineTransition_property_break_loop_at_end>`   | ``false`` |
> +--------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+-----------+
> | :ref:`int<class_int>`                                                    | :ref:`priority<class_AnimationNodeStateMachineTransition_property_priority>`                     | ``1``     |
> +--------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                                                  | :ref:`reset<class_AnimationNodeStateMachineTransition_property_reset>`                           | ``true``  |
> +--------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+-----------+
> | :ref:`SwitchMode<enum_AnimationNodeStateMachineTransition_SwitchMode>`   | :ref:`switch_mode<class_AnimationNodeStateMachineTransition_property_switch_mode>`               | ``0``     |
> +--------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+-----------+
> | :ref:`Curve<class_Curve>`                                                | :ref:`xfade_curve<class_AnimationNodeStateMachineTransition_property_xfade_curve>`               |           |
> +--------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>`                                                | :ref:`xfade_time<class_AnimationNodeStateMachineTransition_property_xfade_time>`                 | ``0.0``   |
> +--------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+-----------+
>

----


## Signals



**advance_condition_changed**\ (\ ) [🔗<class_AnimationNodeStateMachineTransition_signal_advance_condition_changed>]

Emitted when [advance_condition<class_AnimationNodeStateMachineTransition_property_advance_condition>] is changed.


----


## Enumerations



enum **SwitchMode**: [🔗<enum_AnimationNodeStateMachineTransition_SwitchMode>]



[SwitchMode<enum_AnimationNodeStateMachineTransition_SwitchMode>] **SWITCH_MODE_IMMEDIATE** = `0`

Switch to the next state immediately. The current state will end and blend into the beginning of the new one.



[SwitchMode<enum_AnimationNodeStateMachineTransition_SwitchMode>] **SWITCH_MODE_SYNC** = `1`

Switch to the next state immediately, but will seek the new state to the playback position of the old state.



[SwitchMode<enum_AnimationNodeStateMachineTransition_SwitchMode>] **SWITCH_MODE_AT_END** = `2`

Wait for the current state playback to end, then switch to the beginning of the next state animation.


----



enum **AdvanceMode**: [🔗<enum_AnimationNodeStateMachineTransition_AdvanceMode>]



[AdvanceMode<enum_AnimationNodeStateMachineTransition_AdvanceMode>] **ADVANCE_MODE_DISABLED** = `0`

Don't use this transition.



[AdvanceMode<enum_AnimationNodeStateMachineTransition_AdvanceMode>] **ADVANCE_MODE_ENABLED** = `1`

Only use this transition during [AnimationNodeStateMachinePlayback.travel()<class_AnimationNodeStateMachinePlayback_method_travel>].



[AdvanceMode<enum_AnimationNodeStateMachineTransition_AdvanceMode>] **ADVANCE_MODE_AUTO** = `2`

Automatically use this transition if the [advance_condition<class_AnimationNodeStateMachineTransition_property_advance_condition>] and [advance_expression<class_AnimationNodeStateMachineTransition_property_advance_expression>] checks are `true` (if assigned).


----


## Property Descriptions



[StringName<class_StringName>] **advance_condition** = `&""` [🔗<class_AnimationNodeStateMachineTransition_property_advance_condition>]


- |void| **set_advance_condition**\ (\ value\: [StringName<class_StringName>]\ )
- [StringName<class_StringName>] **get_advance_condition**\ (\ )

Turn on auto advance when this condition is set. The provided name will become a boolean parameter on the [AnimationTree<class_AnimationTree>] that can be controlled from code (see [Using AnimationTree ](../tutorials/animation/animation_tree.html#controlling-from-code)_). For example, if [AnimationTree.tree_root<class_AnimationTree_property_tree_root>] is an [AnimationNodeStateMachine<class_AnimationNodeStateMachine>] and [advance_condition<class_AnimationNodeStateMachineTransition_property_advance_condition>] is set to `"idle"`:


> **TABS**
>

    $animation_tree.set("parameters/conditions/idle", is_on_floor and (linear_velocity.x == 0))


    GetNode<AnimationTree>("animation_tree").Set("parameters/conditions/idle", IsOnFloor && (LinearVelocity.X == 0));




----



[String<class_String>] **advance_expression** = `""` [🔗<class_AnimationNodeStateMachineTransition_property_advance_expression>]


- |void| **set_advance_expression**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_advance_expression**\ (\ )

Use an expression as a condition for state machine transitions. It is possible to create complex animation advance conditions for switching between states and gives much greater flexibility for creating complex state machines by directly interfacing with the script code.


----



[AdvanceMode<enum_AnimationNodeStateMachineTransition_AdvanceMode>] **advance_mode** = `1` [🔗<class_AnimationNodeStateMachineTransition_property_advance_mode>]


- |void| **set_advance_mode**\ (\ value\: [AdvanceMode<enum_AnimationNodeStateMachineTransition_AdvanceMode>]\ )
- [AdvanceMode<enum_AnimationNodeStateMachineTransition_AdvanceMode>] **get_advance_mode**\ (\ )

Determines whether the transition should be disabled, enabled when using [AnimationNodeStateMachinePlayback.travel()<class_AnimationNodeStateMachinePlayback_method_travel>], or traversed automatically if the [advance_condition<class_AnimationNodeStateMachineTransition_property_advance_condition>] and [advance_expression<class_AnimationNodeStateMachineTransition_property_advance_expression>] checks are `true` (if assigned).


----



[bool<class_bool>] **break_loop_at_end** = `false` [🔗<class_AnimationNodeStateMachineTransition_property_break_loop_at_end>]


- |void| **set_break_loop_at_end**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_loop_broken_at_end**\ (\ )

If `true`, breaks the loop at the end of the loop cycle for transition, even if the animation is looping.


----



[int<class_int>] **priority** = `1` [🔗<class_AnimationNodeStateMachineTransition_property_priority>]


- |void| **set_priority**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_priority**\ (\ )

Lower priority transitions are preferred when travelling through the tree via [AnimationNodeStateMachinePlayback.travel()<class_AnimationNodeStateMachinePlayback_method_travel>] or [advance_mode<class_AnimationNodeStateMachineTransition_property_advance_mode>] is set to [ADVANCE_MODE_AUTO<class_AnimationNodeStateMachineTransition_constant_ADVANCE_MODE_AUTO>].


----



[bool<class_bool>] **reset** = `true` [🔗<class_AnimationNodeStateMachineTransition_property_reset>]


- |void| **set_reset**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_reset**\ (\ )

If `true`, the destination animation is played back from the beginning when switched.


----



[SwitchMode<enum_AnimationNodeStateMachineTransition_SwitchMode>] **switch_mode** = `0` [🔗<class_AnimationNodeStateMachineTransition_property_switch_mode>]


- |void| **set_switch_mode**\ (\ value\: [SwitchMode<enum_AnimationNodeStateMachineTransition_SwitchMode>]\ )
- [SwitchMode<enum_AnimationNodeStateMachineTransition_SwitchMode>] **get_switch_mode**\ (\ )

The transition type.


----



[Curve<class_Curve>] **xfade_curve** [🔗<class_AnimationNodeStateMachineTransition_property_xfade_curve>]


- |void| **set_xfade_curve**\ (\ value\: [Curve<class_Curve>]\ )
- [Curve<class_Curve>] **get_xfade_curve**\ (\ )

Ease curve for better control over cross-fade between this state and the next. Should be a unit [Curve<class_Curve>].


----



[float<class_float>] **xfade_time** = `0.0` [🔗<class_AnimationNodeStateMachineTransition_property_xfade_time>]


- |void| **set_xfade_time**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_xfade_time**\ (\ )

The time to cross-fade between this state and the next.

\ **Note:** [AnimationNodeStateMachine<class_AnimationNodeStateMachine>] transitions the current state immediately after the start of the fading. The precise remaining time can only be inferred from the main animation. When [AnimationNodeOutput<class_AnimationNodeOutput>] is considered as the most upstream, so the [xfade_time<class_AnimationNodeStateMachineTransition_property_xfade_time>] is not scaled depending on the downstream delta. See also [AnimationNodeOneShot.fadeout_time<class_AnimationNodeOneShot_property_fadeout_time>].

