:github_url: hide



# AnimationMixer

**Inherits:** [Node<class_Node>] **<** [Object<class_Object>]

**Inherited By:** [AnimationPlayer<class_AnimationPlayer>], [AnimationTree<class_AnimationTree>]

Base class for [AnimationPlayer<class_AnimationPlayer>] and [AnimationTree<class_AnimationTree>].


## Description

Base class for [AnimationPlayer<class_AnimationPlayer>] and [AnimationTree<class_AnimationTree>] to manage animation lists. It also has general properties and methods for playback and blending.

After instantiating the playback information data within the extended class, the blending is processed by the **AnimationMixer**.


## Tutorials

- [Migrating Animations from Godot 4.0 to 4.3 ](https://godotengine.org/article/migrating-animations-from-godot-4-0-to-4-3/)_


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+--------------------+
> | :ref:`bool<class_bool>`                                                                 | :ref:`active<class_AnimationMixer_property_active>`                                 | ``true``           |
> +-----------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+--------------------+
> | :ref:`int<class_int>`                                                                   | :ref:`audio_max_polyphony<class_AnimationMixer_property_audio_max_polyphony>`       | ``32``             |
> +-----------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+--------------------+
> | :ref:`AnimationCallbackModeDiscrete<enum_AnimationMixer_AnimationCallbackModeDiscrete>` | :ref:`callback_mode_discrete<class_AnimationMixer_property_callback_mode_discrete>` | ``1``              |
> +-----------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+--------------------+
> | :ref:`AnimationCallbackModeMethod<enum_AnimationMixer_AnimationCallbackModeMethod>`     | :ref:`callback_mode_method<class_AnimationMixer_property_callback_mode_method>`     | ``0``              |
> +-----------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+--------------------+
> | :ref:`AnimationCallbackModeProcess<enum_AnimationMixer_AnimationCallbackModeProcess>`   | :ref:`callback_mode_process<class_AnimationMixer_property_callback_mode_process>`   | ``1``              |
> +-----------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+--------------------+
> | :ref:`bool<class_bool>`                                                                 | :ref:`deterministic<class_AnimationMixer_property_deterministic>`                   | ``false``          |
> +-----------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+--------------------+
> | :ref:`bool<class_bool>`                                                                 | :ref:`reset_on_save<class_AnimationMixer_property_reset_on_save>`                   | ``true``           |
> +-----------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+--------------------+
> | :ref:`bool<class_bool>`                                                                 | :ref:`root_motion_local<class_AnimationMixer_property_root_motion_local>`           | ``false``          |
> +-----------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+--------------------+
> | :ref:`NodePath<class_NodePath>`                                                         | :ref:`root_motion_track<class_AnimationMixer_property_root_motion_track>`           | ``NodePath("")``   |
> +-----------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+--------------------+
> | :ref:`NodePath<class_NodePath>`                                                         | :ref:`root_node<class_AnimationMixer_property_root_node>`                           | ``NodePath("..")`` |
> +-----------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+--------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>`                                    | :ref:`_post_process_key_value<class_AnimationMixer_private_method__post_process_key_value>`\ (\ animation\: :ref:`Animation<class_Animation>`, track\: :ref:`int<class_int>`, value\: :ref:`Variant<class_Variant>`, object_id\: :ref:`int<class_int>`, object_sub_idx\: :ref:`int<class_int>`\ ) |virtual| |const| |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>`                            | :ref:`add_animation_library<class_AnimationMixer_method_add_animation_library>`\ (\ name\: :ref:`StringName<class_StringName>`, library\: :ref:`AnimationLibrary<class_AnimationLibrary>`\ )                                                                                                                        |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`advance<class_AnimationMixer_method_advance>`\ (\ delta\: :ref:`float<class_float>`\ )                                                                                                                                                                                                                        |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`capture<class_AnimationMixer_method_capture>`\ (\ name\: :ref:`StringName<class_StringName>`, duration\: :ref:`float<class_float>`, trans_type\: :ref:`TransitionType<enum_Tween_TransitionType>` = 0, ease_type\: :ref:`EaseType<enum_Tween_EaseType>` = 0\ )                                                |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`clear_caches<class_AnimationMixer_method_clear_caches>`\ (\ )                                                                                                                                                                                                                                                 |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`StringName<class_StringName>`                              | :ref:`find_animation<class_AnimationMixer_method_find_animation>`\ (\ animation\: :ref:`Animation<class_Animation>`\ ) |const|                                                                                                                                                                                      |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`StringName<class_StringName>`                              | :ref:`find_animation_library<class_AnimationMixer_method_find_animation_library>`\ (\ animation\: :ref:`Animation<class_Animation>`\ ) |const|                                                                                                                                                                      |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Animation<class_Animation>`                                | :ref:`get_animation<class_AnimationMixer_method_get_animation>`\ (\ name\: :ref:`StringName<class_StringName>`\ ) |const|                                                                                                                                                                                           |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`AnimationLibrary<class_AnimationLibrary>`                  | :ref:`get_animation_library<class_AnimationMixer_method_get_animation_library>`\ (\ name\: :ref:`StringName<class_StringName>`\ ) |const|                                                                                                                                                                           |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`StringName<class_StringName>`\] | :ref:`get_animation_library_list<class_AnimationMixer_method_get_animation_library_list>`\ (\ ) |const|                                                                                                                                                                                                             |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedStringArray<class_PackedStringArray>`                | :ref:`get_animation_list<class_AnimationMixer_method_get_animation_list>`\ (\ ) |const|                                                                                                                                                                                                                             |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                                    | :ref:`get_root_motion_position<class_AnimationMixer_method_get_root_motion_position>`\ (\ ) |const|                                                                                                                                                                                                                 |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                                    | :ref:`get_root_motion_position_accumulator<class_AnimationMixer_method_get_root_motion_position_accumulator>`\ (\ ) |const|                                                                                                                                                                                         |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Quaternion<class_Quaternion>`                              | :ref:`get_root_motion_rotation<class_AnimationMixer_method_get_root_motion_rotation>`\ (\ ) |const|                                                                                                                                                                                                                 |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Quaternion<class_Quaternion>`                              | :ref:`get_root_motion_rotation_accumulator<class_AnimationMixer_method_get_root_motion_rotation_accumulator>`\ (\ ) |const|                                                                                                                                                                                         |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                                    | :ref:`get_root_motion_scale<class_AnimationMixer_method_get_root_motion_scale>`\ (\ ) |const|                                                                                                                                                                                                                       |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                                    | :ref:`get_root_motion_scale_accumulator<class_AnimationMixer_method_get_root_motion_scale_accumulator>`\ (\ ) |const|                                                                                                                                                                                               |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`has_animation<class_AnimationMixer_method_has_animation>`\ (\ name\: :ref:`StringName<class_StringName>`\ ) |const|                                                                                                                                                                                           |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`has_animation_library<class_AnimationMixer_method_has_animation_library>`\ (\ name\: :ref:`StringName<class_StringName>`\ ) |const|                                                                                                                                                                           |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`remove_animation_library<class_AnimationMixer_method_remove_animation_library>`\ (\ name\: :ref:`StringName<class_StringName>`\ )                                                                                                                                                                             |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`rename_animation_library<class_AnimationMixer_method_rename_animation_library>`\ (\ name\: :ref:`StringName<class_StringName>`, newname\: :ref:`StringName<class_StringName>`\ )                                                                                                                              |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**animation_finished**\ (\ anim_name\: [StringName<class_StringName>]\ ) [🔗<class_AnimationMixer_signal_animation_finished>]

Notifies when an animation finished playing.

\ **Note:** This signal is not emitted if an animation is looping.


----



**animation_libraries_updated**\ (\ ) [🔗<class_AnimationMixer_signal_animation_libraries_updated>]

Notifies when the animation libraries have changed.


----



**animation_list_changed**\ (\ ) [🔗<class_AnimationMixer_signal_animation_list_changed>]

Notifies when an animation list is changed.


----



**animation_started**\ (\ anim_name\: [StringName<class_StringName>]\ ) [🔗<class_AnimationMixer_signal_animation_started>]

Notifies when an animation starts playing.

\ **Note:** This signal is not emitted if an animation is looping.


----



**caches_cleared**\ (\ ) [🔗<class_AnimationMixer_signal_caches_cleared>]

Notifies when the caches have been cleared, either automatically, or manually via [clear_caches()<class_AnimationMixer_method_clear_caches>].


----



**mixer_applied**\ (\ ) [🔗<class_AnimationMixer_signal_mixer_applied>]

Notifies when the blending result related have been applied to the target objects.


----



**mixer_updated**\ (\ ) [🔗<class_AnimationMixer_signal_mixer_updated>]

Notifies when the property related process have been updated.


----


## Enumerations



enum **AnimationCallbackModeProcess**: [🔗<enum_AnimationMixer_AnimationCallbackModeProcess>]



[AnimationCallbackModeProcess<enum_AnimationMixer_AnimationCallbackModeProcess>] **ANIMATION_CALLBACK_MODE_PROCESS_PHYSICS** = `0`

Process animation during physics frames (see [Node.NOTIFICATION_INTERNAL_PHYSICS_PROCESS<class_Node_constant_NOTIFICATION_INTERNAL_PHYSICS_PROCESS>]). This is especially useful when animating physics bodies.



[AnimationCallbackModeProcess<enum_AnimationMixer_AnimationCallbackModeProcess>] **ANIMATION_CALLBACK_MODE_PROCESS_IDLE** = `1`

Process animation during process frames (see [Node.NOTIFICATION_INTERNAL_PROCESS<class_Node_constant_NOTIFICATION_INTERNAL_PROCESS>]).



[AnimationCallbackModeProcess<enum_AnimationMixer_AnimationCallbackModeProcess>] **ANIMATION_CALLBACK_MODE_PROCESS_MANUAL** = `2`

Do not process animation. Use [advance()<class_AnimationMixer_method_advance>] to process the animation manually.


----



enum **AnimationCallbackModeMethod**: [🔗<enum_AnimationMixer_AnimationCallbackModeMethod>]



[AnimationCallbackModeMethod<enum_AnimationMixer_AnimationCallbackModeMethod>] **ANIMATION_CALLBACK_MODE_METHOD_DEFERRED** = `0`

Batch method calls during the animation process, then do the calls after events are processed. This avoids bugs involving deleting nodes or modifying the AnimationPlayer while playing.



[AnimationCallbackModeMethod<enum_AnimationMixer_AnimationCallbackModeMethod>] **ANIMATION_CALLBACK_MODE_METHOD_IMMEDIATE** = `1`

Make method calls immediately when reached in the animation.


----



enum **AnimationCallbackModeDiscrete**: [🔗<enum_AnimationMixer_AnimationCallbackModeDiscrete>]



[AnimationCallbackModeDiscrete<enum_AnimationMixer_AnimationCallbackModeDiscrete>] **ANIMATION_CALLBACK_MODE_DISCRETE_DOMINANT** = `0`

An [Animation.UPDATE_DISCRETE<class_Animation_constant_UPDATE_DISCRETE>] track value takes precedence when blending [Animation.UPDATE_CONTINUOUS<class_Animation_constant_UPDATE_CONTINUOUS>] or [Animation.UPDATE_CAPTURE<class_Animation_constant_UPDATE_CAPTURE>] track values and [Animation.UPDATE_DISCRETE<class_Animation_constant_UPDATE_DISCRETE>] track values.



[AnimationCallbackModeDiscrete<enum_AnimationMixer_AnimationCallbackModeDiscrete>] **ANIMATION_CALLBACK_MODE_DISCRETE_RECESSIVE** = `1`

An [Animation.UPDATE_CONTINUOUS<class_Animation_constant_UPDATE_CONTINUOUS>] or [Animation.UPDATE_CAPTURE<class_Animation_constant_UPDATE_CAPTURE>] track value takes precedence when blending the [Animation.UPDATE_CONTINUOUS<class_Animation_constant_UPDATE_CONTINUOUS>] or [Animation.UPDATE_CAPTURE<class_Animation_constant_UPDATE_CAPTURE>] track values and the [Animation.UPDATE_DISCRETE<class_Animation_constant_UPDATE_DISCRETE>] track values. This is the default behavior for [AnimationPlayer<class_AnimationPlayer>].



[AnimationCallbackModeDiscrete<enum_AnimationMixer_AnimationCallbackModeDiscrete>] **ANIMATION_CALLBACK_MODE_DISCRETE_FORCE_CONTINUOUS** = `2`

Always treat the [Animation.UPDATE_DISCRETE<class_Animation_constant_UPDATE_DISCRETE>] track value as [Animation.UPDATE_CONTINUOUS<class_Animation_constant_UPDATE_CONTINUOUS>] with [Animation.INTERPOLATION_NEAREST<class_Animation_constant_INTERPOLATION_NEAREST>]. This is the default behavior for [AnimationTree<class_AnimationTree>].

If a value track has un-interpolatable type key values, it is internally converted to use [ANIMATION_CALLBACK_MODE_DISCRETE_RECESSIVE<class_AnimationMixer_constant_ANIMATION_CALLBACK_MODE_DISCRETE_RECESSIVE>] with [Animation.UPDATE_DISCRETE<class_Animation_constant_UPDATE_DISCRETE>].

Un-interpolatable type list:

- [@GlobalScope.TYPE_NIL<class_@GlobalScope_constant_TYPE_NIL>]\ 

- [@GlobalScope.TYPE_NODE_PATH<class_@GlobalScope_constant_TYPE_NODE_PATH>]\ 

- [@GlobalScope.TYPE_RID<class_@GlobalScope_constant_TYPE_RID>]\ 

- [@GlobalScope.TYPE_OBJECT<class_@GlobalScope_constant_TYPE_OBJECT>]\ 

- [@GlobalScope.TYPE_CALLABLE<class_@GlobalScope_constant_TYPE_CALLABLE>]\ 

- [@GlobalScope.TYPE_SIGNAL<class_@GlobalScope_constant_TYPE_SIGNAL>]\ 

- [@GlobalScope.TYPE_DICTIONARY<class_@GlobalScope_constant_TYPE_DICTIONARY>]\ 

- [@GlobalScope.TYPE_PACKED_BYTE_ARRAY<class_@GlobalScope_constant_TYPE_PACKED_BYTE_ARRAY>]\ 

\ [@GlobalScope.TYPE_BOOL<class_@GlobalScope_constant_TYPE_BOOL>] and [@GlobalScope.TYPE_INT<class_@GlobalScope_constant_TYPE_INT>] are treated as [@GlobalScope.TYPE_FLOAT<class_@GlobalScope_constant_TYPE_FLOAT>] during blending and rounded when the result is retrieved.

It is same for arrays and vectors with them such as [@GlobalScope.TYPE_PACKED_INT32_ARRAY<class_@GlobalScope_constant_TYPE_PACKED_INT32_ARRAY>] or [@GlobalScope.TYPE_VECTOR2I<class_@GlobalScope_constant_TYPE_VECTOR2I>], they are treated as [@GlobalScope.TYPE_PACKED_FLOAT32_ARRAY<class_@GlobalScope_constant_TYPE_PACKED_FLOAT32_ARRAY>] or [@GlobalScope.TYPE_VECTOR2<class_@GlobalScope_constant_TYPE_VECTOR2>]. Also note that for arrays, the size is also interpolated.

\ [@GlobalScope.TYPE_STRING<class_@GlobalScope_constant_TYPE_STRING>] and [@GlobalScope.TYPE_STRING_NAME<class_@GlobalScope_constant_TYPE_STRING_NAME>] are interpolated between character codes and lengths, but note that there is a difference in algorithm between interpolation between keys and interpolation by blending.


----


## Property Descriptions



[bool<class_bool>] **active** = `true` [🔗<class_AnimationMixer_property_active>]


- |void| **set_active**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_active**\ (\ )

If `true`, the **AnimationMixer** will be processing.


----



[int<class_int>] **audio_max_polyphony** = `32` [🔗<class_AnimationMixer_property_audio_max_polyphony>]


- |void| **set_audio_max_polyphony**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_audio_max_polyphony**\ (\ )

The number of possible simultaneous sounds for each of the assigned AudioStreamPlayers.

For example, if this value is `32` and the animation has two audio tracks, the two [AudioStreamPlayer<class_AudioStreamPlayer>]\ s assigned can play simultaneously up to `32` voices each.


----



[AnimationCallbackModeDiscrete<enum_AnimationMixer_AnimationCallbackModeDiscrete>] **callback_mode_discrete** = `1` [🔗<class_AnimationMixer_property_callback_mode_discrete>]


- |void| **set_callback_mode_discrete**\ (\ value\: [AnimationCallbackModeDiscrete<enum_AnimationMixer_AnimationCallbackModeDiscrete>]\ )
- [AnimationCallbackModeDiscrete<enum_AnimationMixer_AnimationCallbackModeDiscrete>] **get_callback_mode_discrete**\ (\ )

Ordinarily, tracks can be set to [Animation.UPDATE_DISCRETE<class_Animation_constant_UPDATE_DISCRETE>] to update infrequently, usually when using nearest interpolation.

However, when blending with [Animation.UPDATE_CONTINUOUS<class_Animation_constant_UPDATE_CONTINUOUS>] several results are considered. The [callback_mode_discrete<class_AnimationMixer_property_callback_mode_discrete>] specify it explicitly. See also [AnimationCallbackModeDiscrete<enum_AnimationMixer_AnimationCallbackModeDiscrete>].

To make the blended results look good, it is recommended to set this to [ANIMATION_CALLBACK_MODE_DISCRETE_FORCE_CONTINUOUS<class_AnimationMixer_constant_ANIMATION_CALLBACK_MODE_DISCRETE_FORCE_CONTINUOUS>] to update every frame during blending. Other values exist for compatibility and they are fine if there is no blending, but not so, may produce artifacts.


----



[AnimationCallbackModeMethod<enum_AnimationMixer_AnimationCallbackModeMethod>] **callback_mode_method** = `0` [🔗<class_AnimationMixer_property_callback_mode_method>]


- |void| **set_callback_mode_method**\ (\ value\: [AnimationCallbackModeMethod<enum_AnimationMixer_AnimationCallbackModeMethod>]\ )
- [AnimationCallbackModeMethod<enum_AnimationMixer_AnimationCallbackModeMethod>] **get_callback_mode_method**\ (\ )

The call mode used for "Call Method" tracks.


----



[AnimationCallbackModeProcess<enum_AnimationMixer_AnimationCallbackModeProcess>] **callback_mode_process** = `1` [🔗<class_AnimationMixer_property_callback_mode_process>]


- |void| **set_callback_mode_process**\ (\ value\: [AnimationCallbackModeProcess<enum_AnimationMixer_AnimationCallbackModeProcess>]\ )
- [AnimationCallbackModeProcess<enum_AnimationMixer_AnimationCallbackModeProcess>] **get_callback_mode_process**\ (\ )

The process notification in which to update animations.


----



[bool<class_bool>] **deterministic** = `false` [🔗<class_AnimationMixer_property_deterministic>]


- |void| **set_deterministic**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_deterministic**\ (\ )

If `true`, the blending uses the deterministic algorithm. The total weight is not normalized and the result is accumulated with an initial value (`0` or a `"RESET"` animation if present).

This means that if the total amount of blending is `0.0`, the result is equal to the `"RESET"` animation.

If the number of tracks between the blended animations is different, the animation with the missing track is treated as if it had the initial value.

If `false`, The blend does not use the deterministic algorithm. The total weight is normalized and always `1.0`. If the number of tracks between the blended animations is different, nothing is done about the animation that is missing a track.

\ **Note:** In [AnimationTree<class_AnimationTree>], the blending with [AnimationNodeAdd2<class_AnimationNodeAdd2>], [AnimationNodeAdd3<class_AnimationNodeAdd3>], [AnimationNodeSub2<class_AnimationNodeSub2>] or the weight greater than `1.0` may produce unexpected results.

For example, if [AnimationNodeAdd2<class_AnimationNodeAdd2>] blends two nodes with the amount `1.0`, then total weight is `2.0` but it will be normalized to make the total amount `1.0` and the result will be equal to [AnimationNodeBlend2<class_AnimationNodeBlend2>] with the amount `0.5`.


----



[bool<class_bool>] **reset_on_save** = `true` [🔗<class_AnimationMixer_property_reset_on_save>]


- |void| **set_reset_on_save_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_reset_on_save_enabled**\ (\ )

This is used by the editor. If set to `true`, the scene will be saved with the effects of the reset animation (the animation with the key `"RESET"`) applied as if it had been seeked to time 0, with the editor keeping the values that the scene had before saving.

This makes it more convenient to preview and edit animations in the editor, as changes to the scene will not be saved as long as they are set in the reset animation.


----



[bool<class_bool>] **root_motion_local** = `false` [🔗<class_AnimationMixer_property_root_motion_local>]


- |void| **set_root_motion_local**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_root_motion_local**\ (\ )

If `true`, [get_root_motion_position()<class_AnimationMixer_method_get_root_motion_position>] value is extracted as a local translation value before blending. In other words, it is treated like the translation is done after the rotation.


----



[NodePath<class_NodePath>] **root_motion_track** = `NodePath("")` [🔗<class_AnimationMixer_property_root_motion_track>]


- |void| **set_root_motion_track**\ (\ value\: [NodePath<class_NodePath>]\ )
- [NodePath<class_NodePath>] **get_root_motion_track**\ (\ )

The path to the Animation track used for root motion. Paths must be valid scene-tree paths to a node, and must be specified starting from the parent node of the node that will reproduce the animation. The [root_motion_track<class_AnimationMixer_property_root_motion_track>] uses the same format as [Animation.track_set_path()<class_Animation_method_track_set_path>], but note that a bone must be specified.

If the track has type [Animation.TYPE_POSITION_3D<class_Animation_constant_TYPE_POSITION_3D>], [Animation.TYPE_ROTATION_3D<class_Animation_constant_TYPE_ROTATION_3D>], or [Animation.TYPE_SCALE_3D<class_Animation_constant_TYPE_SCALE_3D>] the transformation will be canceled visually, and the animation will appear to stay in place. See also [get_root_motion_position()<class_AnimationMixer_method_get_root_motion_position>], [get_root_motion_rotation()<class_AnimationMixer_method_get_root_motion_rotation>], [get_root_motion_scale()<class_AnimationMixer_method_get_root_motion_scale>], and [RootMotionView<class_RootMotionView>].


----



[NodePath<class_NodePath>] **root_node** = `NodePath("..")` [🔗<class_AnimationMixer_property_root_node>]


- |void| **set_root_node**\ (\ value\: [NodePath<class_NodePath>]\ )
- [NodePath<class_NodePath>] **get_root_node**\ (\ )

The node which node path references will travel from.


----


## Method Descriptions



[Variant<class_Variant>] **_post_process_key_value**\ (\ animation\: [Animation<class_Animation>], track\: [int<class_int>], value\: [Variant<class_Variant>], object_id\: [int<class_int>], object_sub_idx\: [int<class_int>]\ ) |virtual| |const| [🔗<class_AnimationMixer_private_method__post_process_key_value>]

A virtual function for processing after getting a key during playback.


----



[Error<enum_@GlobalScope_Error>] **add_animation_library**\ (\ name\: [StringName<class_StringName>], library\: [AnimationLibrary<class_AnimationLibrary>]\ ) [🔗<class_AnimationMixer_method_add_animation_library>]

Adds `library` to the animation player, under the key `name`.

AnimationMixer has a global library by default with an empty string as key. For adding an animation to the global library:


> **TABS**
>

    var global_library = mixer.get_animation_library("")
    global_library.add_animation("animation_name", animation_resource)




----



|void| **advance**\ (\ delta\: [float<class_float>]\ ) [🔗<class_AnimationMixer_method_advance>]

Manually advance the animations by the specified time (in seconds).


----



|void| **capture**\ (\ name\: [StringName<class_StringName>], duration\: [float<class_float>], trans_type\: [TransitionType<enum_Tween_TransitionType>] = 0, ease_type\: [EaseType<enum_Tween_EaseType>] = 0\ ) [🔗<class_AnimationMixer_method_capture>]

If the animation track specified by `name` has an option [Animation.UPDATE_CAPTURE<class_Animation_constant_UPDATE_CAPTURE>], stores current values of the objects indicated by the track path as a cache. If there is already a captured cache, the old cache is discarded.

After this it will interpolate with current animation blending result during the playback process for the time specified by `duration`, working like a crossfade.

You can specify `trans_type` as the curve for the interpolation. For better results, it may be appropriate to specify [Tween.TRANS_LINEAR<class_Tween_constant_TRANS_LINEAR>] for cases where the first key of the track begins with a non-zero value or where the key value does not change, and [Tween.TRANS_QUAD<class_Tween_constant_TRANS_QUAD>] for cases where the key value changes linearly.


----



|void| **clear_caches**\ (\ ) [🔗<class_AnimationMixer_method_clear_caches>]

**AnimationMixer** caches animated nodes. It may not notice if a node disappears; [clear_caches()<class_AnimationMixer_method_clear_caches>] forces it to update the cache again.


----



[StringName<class_StringName>] **find_animation**\ (\ animation\: [Animation<class_Animation>]\ ) |const| [🔗<class_AnimationMixer_method_find_animation>]

Returns the key of `animation` or an empty [StringName<class_StringName>] if not found.


----



[StringName<class_StringName>] **find_animation_library**\ (\ animation\: [Animation<class_Animation>]\ ) |const| [🔗<class_AnimationMixer_method_find_animation_library>]

Returns the key for the [AnimationLibrary<class_AnimationLibrary>] that contains `animation` or an empty [StringName<class_StringName>] if not found.


----



[Animation<class_Animation>] **get_animation**\ (\ name\: [StringName<class_StringName>]\ ) |const| [🔗<class_AnimationMixer_method_get_animation>]

Returns the [Animation<class_Animation>] with the key `name`. If the animation does not exist, `null` is returned and an error is logged.


----



[AnimationLibrary<class_AnimationLibrary>] **get_animation_library**\ (\ name\: [StringName<class_StringName>]\ ) |const| [🔗<class_AnimationMixer_method_get_animation_library>]

Returns the first [AnimationLibrary<class_AnimationLibrary>] with key `name` or `null` if not found.

To get the **AnimationMixer**'s global animation library, use `get_animation_library("")`.


----



[Array<class_Array>]\[[StringName<class_StringName>]\] **get_animation_library_list**\ (\ ) |const| [🔗<class_AnimationMixer_method_get_animation_library_list>]

Returns the list of stored library keys.


----



[PackedStringArray<class_PackedStringArray>] **get_animation_list**\ (\ ) |const| [🔗<class_AnimationMixer_method_get_animation_list>]

Returns the list of stored animation keys.


----



[Vector3<class_Vector3>] **get_root_motion_position**\ (\ ) |const| [🔗<class_AnimationMixer_method_get_root_motion_position>]

Retrieve the motion delta of position with the [root_motion_track<class_AnimationMixer_property_root_motion_track>] as a [Vector3<class_Vector3>] that can be used elsewhere.

If [root_motion_track<class_AnimationMixer_property_root_motion_track>] is not a path to a track of type [Animation.TYPE_POSITION_3D<class_Animation_constant_TYPE_POSITION_3D>], returns `Vector3(0, 0, 0)`.

See also [root_motion_track<class_AnimationMixer_property_root_motion_track>] and [RootMotionView<class_RootMotionView>].

The most basic example is applying position to [CharacterBody3D<class_CharacterBody3D>]:


> **TABS**
>

    var current_rotation

    func _process(delta):
        if Input.is_action_just_pressed("animate"):
            current_rotation = get_quaternion()
            state_machine.travel("Animate")
        var velocity = current_rotation * animation_tree.get_root_motion_position() / delta
        set_velocity(velocity)
        move_and_slide()



By using this in combination with [get_root_motion_rotation_accumulator()<class_AnimationMixer_method_get_root_motion_rotation_accumulator>], you can apply the root motion position more correctly to account for the rotation of the node.


> **TABS**
>

    func _process(delta):
        if Input.is_action_just_pressed("animate"):
            state_machine.travel("Animate")
        set_quaternion(get_quaternion() * animation_tree.get_root_motion_rotation())
        var velocity = (animation_tree.get_root_motion_rotation_accumulator().inverse() * get_quaternion()) * animation_tree.get_root_motion_position() / delta
        set_velocity(velocity)
        move_and_slide()



If [root_motion_local<class_AnimationMixer_property_root_motion_local>] is `true`, returns the pre-multiplied translation value with the inverted rotation.

In this case, the code can be written as follows:


> **TABS**
>

    func _process(delta):
        if Input.is_action_just_pressed("animate"):
            state_machine.travel("Animate")
        set_quaternion(get_quaternion() * animation_tree.get_root_motion_rotation())
        var velocity = get_quaternion() * animation_tree.get_root_motion_position() / delta
        set_velocity(velocity)
        move_and_slide()




----



[Vector3<class_Vector3>] **get_root_motion_position_accumulator**\ (\ ) |const| [🔗<class_AnimationMixer_method_get_root_motion_position_accumulator>]

Retrieve the blended value of the position tracks with the [root_motion_track<class_AnimationMixer_property_root_motion_track>] as a [Vector3<class_Vector3>] that can be used elsewhere.

This is useful in cases where you want to respect the initial key values of the animation.

For example, if an animation with only one key `Vector3(0, 0, 0)` is played in the previous frame and then an animation with only one key `Vector3(1, 0, 1)` is played in the next frame, the difference can be calculated as follows:


> **TABS**
>

    var prev_root_motion_position_accumulator

    func _process(delta):
        if Input.is_action_just_pressed("animate"):
            state_machine.travel("Animate")
        var current_root_motion_position_accumulator = animation_tree.get_root_motion_position_accumulator()
        var difference = current_root_motion_position_accumulator - prev_root_motion_position_accumulator
        prev_root_motion_position_accumulator = current_root_motion_position_accumulator
        transform.origin += difference



However, if the animation loops, an unintended discrete change may occur, so this is only useful for some simple use cases.


----



[Quaternion<class_Quaternion>] **get_root_motion_rotation**\ (\ ) |const| [🔗<class_AnimationMixer_method_get_root_motion_rotation>]

Retrieve the motion delta of rotation with the [root_motion_track<class_AnimationMixer_property_root_motion_track>] as a [Quaternion<class_Quaternion>] that can be used elsewhere.

If [root_motion_track<class_AnimationMixer_property_root_motion_track>] is not a path to a track of type [Animation.TYPE_ROTATION_3D<class_Animation_constant_TYPE_ROTATION_3D>], returns `Quaternion(0, 0, 0, 1)`.

See also [root_motion_track<class_AnimationMixer_property_root_motion_track>] and [RootMotionView<class_RootMotionView>].

The most basic example is applying rotation to [CharacterBody3D<class_CharacterBody3D>]:


> **TABS**
>

    func _process(delta):
        if Input.is_action_just_pressed("animate"):
            state_machine.travel("Animate")
        set_quaternion(get_quaternion() * animation_tree.get_root_motion_rotation())




----



[Quaternion<class_Quaternion>] **get_root_motion_rotation_accumulator**\ (\ ) |const| [🔗<class_AnimationMixer_method_get_root_motion_rotation_accumulator>]

Retrieve the blended value of the rotation tracks with the [root_motion_track<class_AnimationMixer_property_root_motion_track>] as a [Quaternion<class_Quaternion>] that can be used elsewhere.

This is necessary to apply the root motion position correctly, taking rotation into account. See also [get_root_motion_position()<class_AnimationMixer_method_get_root_motion_position>].

Also, this is useful in cases where you want to respect the initial key values of the animation.

For example, if an animation with only one key `Quaternion(0, 0, 0, 1)` is played in the previous frame and then an animation with only one key `Quaternion(0, 0.707, 0, 0.707)` is played in the next frame, the difference can be calculated as follows:


> **TABS**
>

    var prev_root_motion_rotation_accumulator

    func _process(delta):
        if Input.is_action_just_pressed("animate"):
            state_machine.travel("Animate")
        var current_root_motion_rotation_accumulator = animation_tree.get_root_motion_rotation_accumulator()
        var difference = prev_root_motion_rotation_accumulator.inverse() * current_root_motion_rotation_accumulator
        prev_root_motion_rotation_accumulator = current_root_motion_rotation_accumulator
        transform.basis *=  Basis(difference)



However, if the animation loops, an unintended discrete change may occur, so this is only useful for some simple use cases.


----



[Vector3<class_Vector3>] **get_root_motion_scale**\ (\ ) |const| [🔗<class_AnimationMixer_method_get_root_motion_scale>]

Retrieve the motion delta of scale with the [root_motion_track<class_AnimationMixer_property_root_motion_track>] as a [Vector3<class_Vector3>] that can be used elsewhere.

If [root_motion_track<class_AnimationMixer_property_root_motion_track>] is not a path to a track of type [Animation.TYPE_SCALE_3D<class_Animation_constant_TYPE_SCALE_3D>], returns `Vector3(0, 0, 0)`.

See also [root_motion_track<class_AnimationMixer_property_root_motion_track>] and [RootMotionView<class_RootMotionView>].

The most basic example is applying scale to [CharacterBody3D<class_CharacterBody3D>]:


> **TABS**
>

    var current_scale = Vector3(1, 1, 1)
    var scale_accum = Vector3(1, 1, 1)

    func _process(delta):
        if Input.is_action_just_pressed("animate"):
            current_scale = get_scale()
            scale_accum = Vector3(1, 1, 1)
            state_machine.travel("Animate")
        scale_accum += animation_tree.get_root_motion_scale()
        set_scale(current_scale * scale_accum)




----



[Vector3<class_Vector3>] **get_root_motion_scale_accumulator**\ (\ ) |const| [🔗<class_AnimationMixer_method_get_root_motion_scale_accumulator>]

Retrieve the blended value of the scale tracks with the [root_motion_track<class_AnimationMixer_property_root_motion_track>] as a [Vector3<class_Vector3>] that can be used elsewhere.

For example, if an animation with only one key `Vector3(1, 1, 1)` is played in the previous frame and then an animation with only one key `Vector3(2, 2, 2)` is played in the next frame, the difference can be calculated as follows:


> **TABS**
>

    var prev_root_motion_scale_accumulator

    func _process(delta):
        if Input.is_action_just_pressed("animate"):
            state_machine.travel("Animate")
        var current_root_motion_scale_accumulator = animation_tree.get_root_motion_scale_accumulator()
        var difference = current_root_motion_scale_accumulator - prev_root_motion_scale_accumulator
        prev_root_motion_scale_accumulator = current_root_motion_scale_accumulator
        transform.basis = transform.basis.scaled(difference)



However, if the animation loops, an unintended discrete change may occur, so this is only useful for some simple use cases.


----



[bool<class_bool>] **has_animation**\ (\ name\: [StringName<class_StringName>]\ ) |const| [🔗<class_AnimationMixer_method_has_animation>]

Returns `true` if the **AnimationMixer** stores an [Animation<class_Animation>] with key `name`.


----



[bool<class_bool>] **has_animation_library**\ (\ name\: [StringName<class_StringName>]\ ) |const| [🔗<class_AnimationMixer_method_has_animation_library>]

Returns `true` if the **AnimationMixer** stores an [AnimationLibrary<class_AnimationLibrary>] with key `name`.


----



|void| **remove_animation_library**\ (\ name\: [StringName<class_StringName>]\ ) [🔗<class_AnimationMixer_method_remove_animation_library>]

Removes the [AnimationLibrary<class_AnimationLibrary>] associated with the key `name`.


----



|void| **rename_animation_library**\ (\ name\: [StringName<class_StringName>], newname\: [StringName<class_StringName>]\ ) [🔗<class_AnimationMixer_method_rename_animation_library>]

Moves the [AnimationLibrary<class_AnimationLibrary>] associated with the key `name` to the key `newname`.

