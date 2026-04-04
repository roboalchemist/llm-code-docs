:github_url: hide



# Skeleton3D

**Inherits:** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A node containing a bone hierarchy, used to create a 3D skeletal animation.


## Description

**Skeleton3D** provides an interface for managing a hierarchy of bones, including pose, rest and animation (see [Animation<class_Animation>]). It can also use ragdoll physics.

The overall transform of a bone with respect to the skeleton is determined by bone pose. Bone rest defines the initial transform of the bone pose.

Note that "global pose" below refers to the overall transform of the bone with respect to skeleton, so it is not the actual global/world transform of the bone.


## Tutorials

- [Third Person Shooter (TPS) Demo ](https://godotengine.org/asset-library/asset/2710)_


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                                                         | :ref:`animate_physical_bones<class_Skeleton3D_property_animate_physical_bones>`                 | ``true``  |
> +---------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+-----------+
> | :ref:`ModifierCallbackModeProcess<enum_Skeleton3D_ModifierCallbackModeProcess>` | :ref:`modifier_callback_mode_process<class_Skeleton3D_property_modifier_callback_mode_process>` | ``1``     |
> +---------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>`                                                       | :ref:`motion_scale<class_Skeleton3D_property_motion_scale>`                                     | ``1.0``   |
> +---------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                                                         | :ref:`show_rest_only<class_Skeleton3D_property_show_rest_only>`                                 | ``false`` |
> +---------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+-----------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                            | :ref:`add_bone<class_Skeleton3D_method_add_bone>`\ (\ name\: :ref:`String<class_String>`\ )                                                                                                                                                                         |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`advance<class_Skeleton3D_method_advance>`\ (\ delta\: :ref:`float<class_float>`\ )                                                                                                                                                                            |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`clear_bones<class_Skeleton3D_method_clear_bones>`\ (\ )                                                                                                                                                                                                       |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`clear_bones_global_pose_override<class_Skeleton3D_method_clear_bones_global_pose_override>`\ (\ )                                                                                                                                                             |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Skin<class_Skin>`                                          | :ref:`create_skin_from_rest_transforms<class_Skeleton3D_method_create_skin_from_rest_transforms>`\ (\ )                                                                                                                                                             |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                            | :ref:`find_bone<class_Skeleton3D_method_find_bone>`\ (\ name\: :ref:`String<class_String>`\ ) |const|                                                                                                                                                               |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`force_update_all_bone_transforms<class_Skeleton3D_method_force_update_all_bone_transforms>`\ (\ )                                                                                                                                                             |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`force_update_bone_child_transform<class_Skeleton3D_method_force_update_bone_child_transform>`\ (\ bone_idx\: :ref:`int<class_int>`\ )                                                                                                                         |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedInt32Array<class_PackedInt32Array>`                  | :ref:`get_bone_children<class_Skeleton3D_method_get_bone_children>`\ (\ bone_idx\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                 |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                            | :ref:`get_bone_count<class_Skeleton3D_method_get_bone_count>`\ (\ ) |const|                                                                                                                                                                                         |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>`                            | :ref:`get_bone_global_pose<class_Skeleton3D_method_get_bone_global_pose>`\ (\ bone_idx\: :ref:`int<class_int>`\ ) |const|                                                                                                                                           |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>`                            | :ref:`get_bone_global_pose_no_override<class_Skeleton3D_method_get_bone_global_pose_no_override>`\ (\ bone_idx\: :ref:`int<class_int>`\ ) |const|                                                                                                                   |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>`                            | :ref:`get_bone_global_pose_override<class_Skeleton3D_method_get_bone_global_pose_override>`\ (\ bone_idx\: :ref:`int<class_int>`\ ) |const|                                                                                                                         |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>`                            | :ref:`get_bone_global_rest<class_Skeleton3D_method_get_bone_global_rest>`\ (\ bone_idx\: :ref:`int<class_int>`\ ) |const|                                                                                                                                           |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>`                                    | :ref:`get_bone_meta<class_Skeleton3D_method_get_bone_meta>`\ (\ bone_idx\: :ref:`int<class_int>`, key\: :ref:`StringName<class_StringName>`\ ) |const|                                                                                                              |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`StringName<class_StringName>`\] | :ref:`get_bone_meta_list<class_Skeleton3D_method_get_bone_meta_list>`\ (\ bone_idx\: :ref:`int<class_int>`\ ) |const|                                                                                                                                               |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                                      | :ref:`get_bone_name<class_Skeleton3D_method_get_bone_name>`\ (\ bone_idx\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                         |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                            | :ref:`get_bone_parent<class_Skeleton3D_method_get_bone_parent>`\ (\ bone_idx\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                     |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>`                            | :ref:`get_bone_pose<class_Skeleton3D_method_get_bone_pose>`\ (\ bone_idx\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                         |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                                    | :ref:`get_bone_pose_position<class_Skeleton3D_method_get_bone_pose_position>`\ (\ bone_idx\: :ref:`int<class_int>`\ ) |const|                                                                                                                                       |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Quaternion<class_Quaternion>`                              | :ref:`get_bone_pose_rotation<class_Skeleton3D_method_get_bone_pose_rotation>`\ (\ bone_idx\: :ref:`int<class_int>`\ ) |const|                                                                                                                                       |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                                    | :ref:`get_bone_pose_scale<class_Skeleton3D_method_get_bone_pose_scale>`\ (\ bone_idx\: :ref:`int<class_int>`\ ) |const|                                                                                                                                             |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>`                            | :ref:`get_bone_rest<class_Skeleton3D_method_get_bone_rest>`\ (\ bone_idx\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                         |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`StringName<class_StringName>`                              | :ref:`get_concatenated_bone_names<class_Skeleton3D_method_get_concatenated_bone_names>`\ (\ ) |const|                                                                                                                                                               |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedInt32Array<class_PackedInt32Array>`                  | :ref:`get_parentless_bones<class_Skeleton3D_method_get_parentless_bones>`\ (\ ) |const|                                                                                                                                                                             |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                            | :ref:`get_version<class_Skeleton3D_method_get_version>`\ (\ ) |const|                                                                                                                                                                                               |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`has_bone_meta<class_Skeleton3D_method_has_bone_meta>`\ (\ bone_idx\: :ref:`int<class_int>`, key\: :ref:`StringName<class_StringName>`\ ) |const|                                                                                                              |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`is_bone_enabled<class_Skeleton3D_method_is_bone_enabled>`\ (\ bone_idx\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                     |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`localize_rests<class_Skeleton3D_method_localize_rests>`\ (\ )                                                                                                                                                                                                 |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`physical_bones_add_collision_exception<class_Skeleton3D_method_physical_bones_add_collision_exception>`\ (\ exception\: :ref:`RID<class_RID>`\ )                                                                                                              |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`physical_bones_remove_collision_exception<class_Skeleton3D_method_physical_bones_remove_collision_exception>`\ (\ exception\: :ref:`RID<class_RID>`\ )                                                                                                        |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`physical_bones_start_simulation<class_Skeleton3D_method_physical_bones_start_simulation>`\ (\ bones\: :ref:`Array<class_Array>`\[:ref:`StringName<class_StringName>`\] = []\ )                                                                                |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`physical_bones_stop_simulation<class_Skeleton3D_method_physical_bones_stop_simulation>`\ (\ )                                                                                                                                                                 |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`SkinReference<class_SkinReference>`                        | :ref:`register_skin<class_Skeleton3D_method_register_skin>`\ (\ skin\: :ref:`Skin<class_Skin>`\ )                                                                                                                                                                   |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`reset_bone_pose<class_Skeleton3D_method_reset_bone_pose>`\ (\ bone_idx\: :ref:`int<class_int>`\ )                                                                                                                                                             |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`reset_bone_poses<class_Skeleton3D_method_reset_bone_poses>`\ (\ )                                                                                                                                                                                             |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`set_bone_enabled<class_Skeleton3D_method_set_bone_enabled>`\ (\ bone_idx\: :ref:`int<class_int>`, enabled\: :ref:`bool<class_bool>` = true\ )                                                                                                                 |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`set_bone_global_pose<class_Skeleton3D_method_set_bone_global_pose>`\ (\ bone_idx\: :ref:`int<class_int>`, pose\: :ref:`Transform3D<class_Transform3D>`\ )                                                                                                     |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`set_bone_global_pose_override<class_Skeleton3D_method_set_bone_global_pose_override>`\ (\ bone_idx\: :ref:`int<class_int>`, pose\: :ref:`Transform3D<class_Transform3D>`, amount\: :ref:`float<class_float>`, persistent\: :ref:`bool<class_bool>` = false\ ) |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`set_bone_meta<class_Skeleton3D_method_set_bone_meta>`\ (\ bone_idx\: :ref:`int<class_int>`, key\: :ref:`StringName<class_StringName>`, value\: :ref:`Variant<class_Variant>`\ )                                                                               |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`set_bone_name<class_Skeleton3D_method_set_bone_name>`\ (\ bone_idx\: :ref:`int<class_int>`, name\: :ref:`String<class_String>`\ )                                                                                                                             |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`set_bone_parent<class_Skeleton3D_method_set_bone_parent>`\ (\ bone_idx\: :ref:`int<class_int>`, parent_idx\: :ref:`int<class_int>`\ )                                                                                                                         |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`set_bone_pose<class_Skeleton3D_method_set_bone_pose>`\ (\ bone_idx\: :ref:`int<class_int>`, pose\: :ref:`Transform3D<class_Transform3D>`\ )                                                                                                                   |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`set_bone_pose_position<class_Skeleton3D_method_set_bone_pose_position>`\ (\ bone_idx\: :ref:`int<class_int>`, position\: :ref:`Vector3<class_Vector3>`\ )                                                                                                     |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`set_bone_pose_rotation<class_Skeleton3D_method_set_bone_pose_rotation>`\ (\ bone_idx\: :ref:`int<class_int>`, rotation\: :ref:`Quaternion<class_Quaternion>`\ )                                                                                               |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`set_bone_pose_scale<class_Skeleton3D_method_set_bone_pose_scale>`\ (\ bone_idx\: :ref:`int<class_int>`, scale\: :ref:`Vector3<class_Vector3>`\ )                                                                                                              |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`set_bone_rest<class_Skeleton3D_method_set_bone_rest>`\ (\ bone_idx\: :ref:`int<class_int>`, rest\: :ref:`Transform3D<class_Transform3D>`\ )                                                                                                                   |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`unparent_bone_and_rest<class_Skeleton3D_method_unparent_bone_and_rest>`\ (\ bone_idx\: :ref:`int<class_int>`\ )                                                                                                                                               |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**bone_enabled_changed**\ (\ bone_idx\: [int<class_int>]\ ) [🔗<class_Skeleton3D_signal_bone_enabled_changed>]

Emitted when the bone at `bone_idx` is toggled with [set_bone_enabled()<class_Skeleton3D_method_set_bone_enabled>]. Use [is_bone_enabled()<class_Skeleton3D_method_is_bone_enabled>] to check the new value.


----



**bone_list_changed**\ (\ ) [🔗<class_Skeleton3D_signal_bone_list_changed>]

Emitted when the list of bones changes, such as when calling [add_bone()<class_Skeleton3D_method_add_bone>], [set_bone_parent()<class_Skeleton3D_method_set_bone_parent>], [unparent_bone_and_rest()<class_Skeleton3D_method_unparent_bone_and_rest>], or [clear_bones()<class_Skeleton3D_method_clear_bones>].


----



**pose_updated**\ (\ ) [🔗<class_Skeleton3D_signal_pose_updated>]

Emitted when the pose is updated.

\ **Note:** During the update process, this signal is not fired, so modification by [SkeletonModifier3D<class_SkeletonModifier3D>] is not detected.


----



**rest_updated**\ (\ ) [🔗<class_Skeleton3D_signal_rest_updated>]

Emitted when the rest is updated.


----



**show_rest_only_changed**\ (\ ) [🔗<class_Skeleton3D_signal_show_rest_only_changed>]

Emitted when the value of [show_rest_only<class_Skeleton3D_property_show_rest_only>] changes.


----



**skeleton_updated**\ (\ ) [🔗<class_Skeleton3D_signal_skeleton_updated>]

Emitted when the final pose has been calculated will be applied to the skin in the update process.

This means that all [SkeletonModifier3D<class_SkeletonModifier3D>] processing is complete. In order to detect the completion of the processing of each [SkeletonModifier3D<class_SkeletonModifier3D>], use [SkeletonModifier3D.modification_processed<class_SkeletonModifier3D_signal_modification_processed>].


----


## Enumerations



enum **ModifierCallbackModeProcess**: [🔗<enum_Skeleton3D_ModifierCallbackModeProcess>]



[ModifierCallbackModeProcess<enum_Skeleton3D_ModifierCallbackModeProcess>] **MODIFIER_CALLBACK_MODE_PROCESS_PHYSICS** = `0`

Set a flag to process modification during physics frames (see [Node.NOTIFICATION_INTERNAL_PHYSICS_PROCESS<class_Node_constant_NOTIFICATION_INTERNAL_PHYSICS_PROCESS>]).



[ModifierCallbackModeProcess<enum_Skeleton3D_ModifierCallbackModeProcess>] **MODIFIER_CALLBACK_MODE_PROCESS_IDLE** = `1`

Set a flag to process modification during process frames (see [Node.NOTIFICATION_INTERNAL_PROCESS<class_Node_constant_NOTIFICATION_INTERNAL_PROCESS>]).



[ModifierCallbackModeProcess<enum_Skeleton3D_ModifierCallbackModeProcess>] **MODIFIER_CALLBACK_MODE_PROCESS_MANUAL** = `2`

Do not process modification. Use [advance()<class_Skeleton3D_method_advance>] to process the modification manually.


----


## Constants



**NOTIFICATION_UPDATE_SKELETON** = `50` [🔗<class_Skeleton3D_constant_NOTIFICATION_UPDATE_SKELETON>]

Notification received when this skeleton's pose needs to be updated. In that case, this is called only once per frame in a deferred process.


----


## Property Descriptions



[bool<class_bool>] **animate_physical_bones** = `true` [🔗<class_Skeleton3D_property_animate_physical_bones>]


- |void| **set_animate_physical_bones**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_animate_physical_bones**\ (\ )

**Deprecated:** This property may be changed or removed in future versions.

If you follow the recommended workflow and explicitly have [PhysicalBoneSimulator3D<class_PhysicalBoneSimulator3D>] as a child of **Skeleton3D**, you can control whether it is affected by raycasting without running [physical_bones_start_simulation()<class_Skeleton3D_method_physical_bones_start_simulation>], by its [SkeletonModifier3D.active<class_SkeletonModifier3D_property_active>].

However, for old (deprecated) configurations, **Skeleton3D** has an internal virtual [PhysicalBoneSimulator3D<class_PhysicalBoneSimulator3D>] for compatibility. This property controls the internal virtual [PhysicalBoneSimulator3D<class_PhysicalBoneSimulator3D>]'s [SkeletonModifier3D.active<class_SkeletonModifier3D_property_active>].


----



[ModifierCallbackModeProcess<enum_Skeleton3D_ModifierCallbackModeProcess>] **modifier_callback_mode_process** = `1` [🔗<class_Skeleton3D_property_modifier_callback_mode_process>]


- |void| **set_modifier_callback_mode_process**\ (\ value\: [ModifierCallbackModeProcess<enum_Skeleton3D_ModifierCallbackModeProcess>]\ )
- [ModifierCallbackModeProcess<enum_Skeleton3D_ModifierCallbackModeProcess>] **get_modifier_callback_mode_process**\ (\ )

Sets the processing timing for the Modifier.


----



[float<class_float>] **motion_scale** = `1.0` [🔗<class_Skeleton3D_property_motion_scale>]


- |void| **set_motion_scale**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_motion_scale**\ (\ )

Multiplies the 3D position track animation.

\ **Note:** Unless this value is `1.0`, the key value in animation will not match the actual position value.


----



[bool<class_bool>] **show_rest_only** = `false` [🔗<class_Skeleton3D_property_show_rest_only>]


- |void| **set_show_rest_only**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_show_rest_only**\ (\ )

If `true`, forces the bones in their default rest pose, regardless of their values. In the editor, this also prevents the bones from being edited.


----


## Method Descriptions



[int<class_int>] **add_bone**\ (\ name\: [String<class_String>]\ ) [🔗<class_Skeleton3D_method_add_bone>]

Adds a new bone with the given name. Returns the new bone's index, or `-1` if this method fails.

\ **Note:** Bone names should be unique, non empty, and cannot include the `:` and `/` characters.


----



|void| **advance**\ (\ delta\: [float<class_float>]\ ) [🔗<class_Skeleton3D_method_advance>]

Manually advance the child [SkeletonModifier3D<class_SkeletonModifier3D>]\ s by the specified time (in seconds).

\ **Note:** The `delta` is temporarily accumulated in the **Skeleton3D**, and the deferred process uses the accumulated value to process the modification.


----



|void| **clear_bones**\ (\ ) [🔗<class_Skeleton3D_method_clear_bones>]

Clear all the bones in this skeleton.


----



|void| **clear_bones_global_pose_override**\ (\ ) [🔗<class_Skeleton3D_method_clear_bones_global_pose_override>]

**Deprecated:** This method may be changed or removed in future versions.

Removes the global pose override on all bones in the skeleton.


----



[Skin<class_Skin>] **create_skin_from_rest_transforms**\ (\ ) [🔗<class_Skeleton3D_method_create_skin_from_rest_transforms>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[int<class_int>] **find_bone**\ (\ name\: [String<class_String>]\ ) |const| [🔗<class_Skeleton3D_method_find_bone>]

Returns the bone index that matches `name` as its name. Returns `-1` if no bone with this name exists.


----



|void| **force_update_all_bone_transforms**\ (\ ) [🔗<class_Skeleton3D_method_force_update_all_bone_transforms>]

**Deprecated:** This method should only be called internally.

Force updates the bone transforms/poses for all bones in the skeleton.


----



|void| **force_update_bone_child_transform**\ (\ bone_idx\: [int<class_int>]\ ) [🔗<class_Skeleton3D_method_force_update_bone_child_transform>]

Force updates the bone transform for the bone at `bone_idx` and all of its children.


----



[PackedInt32Array<class_PackedInt32Array>] **get_bone_children**\ (\ bone_idx\: [int<class_int>]\ ) |const| [🔗<class_Skeleton3D_method_get_bone_children>]

Returns an array containing the bone indexes of all the child node of the passed in bone, `bone_idx`.


----



[int<class_int>] **get_bone_count**\ (\ ) |const| [🔗<class_Skeleton3D_method_get_bone_count>]

Returns the number of bones in the skeleton.


----



[Transform3D<class_Transform3D>] **get_bone_global_pose**\ (\ bone_idx\: [int<class_int>]\ ) |const| [🔗<class_Skeleton3D_method_get_bone_global_pose>]

Returns the overall transform of the specified bone, with respect to the skeleton. Being relative to the skeleton frame, this is not the actual "global" transform of the bone.

\ **Note:** This is the global pose you set to the skeleton in the process, the final global pose can get overridden by modifiers in the deferred process, if you want to access the final global pose, use [SkeletonModifier3D.modification_processed<class_SkeletonModifier3D_signal_modification_processed>].


----



[Transform3D<class_Transform3D>] **get_bone_global_pose_no_override**\ (\ bone_idx\: [int<class_int>]\ ) |const| [🔗<class_Skeleton3D_method_get_bone_global_pose_no_override>]

**Deprecated:** This method may be changed or removed in future versions.

Returns the overall transform of the specified bone, with respect to the skeleton, but without any global pose overrides. Being relative to the skeleton frame, this is not the actual "global" transform of the bone.


----



[Transform3D<class_Transform3D>] **get_bone_global_pose_override**\ (\ bone_idx\: [int<class_int>]\ ) |const| [🔗<class_Skeleton3D_method_get_bone_global_pose_override>]

**Deprecated:** This method may be changed or removed in future versions.

Returns the global pose override transform for `bone_idx`.


----



[Transform3D<class_Transform3D>] **get_bone_global_rest**\ (\ bone_idx\: [int<class_int>]\ ) |const| [🔗<class_Skeleton3D_method_get_bone_global_rest>]

Returns the global rest transform for `bone_idx`.


----



[Variant<class_Variant>] **get_bone_meta**\ (\ bone_idx\: [int<class_int>], key\: [StringName<class_StringName>]\ ) |const| [🔗<class_Skeleton3D_method_get_bone_meta>]

Returns the metadata with the given `key` for the bone at index `bone_idx`.


----



[Array<class_Array>]\[[StringName<class_StringName>]\] **get_bone_meta_list**\ (\ bone_idx\: [int<class_int>]\ ) |const| [🔗<class_Skeleton3D_method_get_bone_meta_list>]

Returns the list of all metadata keys for the bone at index `bone_idx`.


----



[String<class_String>] **get_bone_name**\ (\ bone_idx\: [int<class_int>]\ ) |const| [🔗<class_Skeleton3D_method_get_bone_name>]

Returns the name of the bone at index `bone_idx`.


----



[int<class_int>] **get_bone_parent**\ (\ bone_idx\: [int<class_int>]\ ) |const| [🔗<class_Skeleton3D_method_get_bone_parent>]

Returns the bone index which is the parent of the bone at `bone_idx`. If -1, then bone has no parent.

\ **Note:** The parent bone returned will always be less than `bone_idx`.


----



[Transform3D<class_Transform3D>] **get_bone_pose**\ (\ bone_idx\: [int<class_int>]\ ) |const| [🔗<class_Skeleton3D_method_get_bone_pose>]

Returns the pose transform of the specified bone.

\ **Note:** This is the pose you set to the skeleton in the process, the final pose can get overridden by modifiers in the deferred process, if you want to access the final pose, use [SkeletonModifier3D.modification_processed<class_SkeletonModifier3D_signal_modification_processed>].


----



[Vector3<class_Vector3>] **get_bone_pose_position**\ (\ bone_idx\: [int<class_int>]\ ) |const| [🔗<class_Skeleton3D_method_get_bone_pose_position>]

Returns the pose position of the bone at `bone_idx`. The returned [Vector3<class_Vector3>] is in the local coordinate space of the **Skeleton3D** node.


----



[Quaternion<class_Quaternion>] **get_bone_pose_rotation**\ (\ bone_idx\: [int<class_int>]\ ) |const| [🔗<class_Skeleton3D_method_get_bone_pose_rotation>]

Returns the pose rotation of the bone at `bone_idx`. The returned [Quaternion<class_Quaternion>] is local to the bone with respect to the rotation of any parent bones.


----



[Vector3<class_Vector3>] **get_bone_pose_scale**\ (\ bone_idx\: [int<class_int>]\ ) |const| [🔗<class_Skeleton3D_method_get_bone_pose_scale>]

Returns the pose scale of the bone at `bone_idx`.


----



[Transform3D<class_Transform3D>] **get_bone_rest**\ (\ bone_idx\: [int<class_int>]\ ) |const| [🔗<class_Skeleton3D_method_get_bone_rest>]

Returns the rest transform for a bone `bone_idx`.


----



[StringName<class_StringName>] **get_concatenated_bone_names**\ (\ ) |const| [🔗<class_Skeleton3D_method_get_concatenated_bone_names>]

Returns all bone names concatenated with commas (`,`) as a single [StringName<class_StringName>].

It is useful to set it as a hint for the enum property.


----



[PackedInt32Array<class_PackedInt32Array>] **get_parentless_bones**\ (\ ) |const| [🔗<class_Skeleton3D_method_get_parentless_bones>]

Returns an array with all of the bones that are parentless. Another way to look at this is that it returns the indexes of all the bones that are not dependent or modified by other bones in the Skeleton.


----



[int<class_int>] **get_version**\ (\ ) |const| [🔗<class_Skeleton3D_method_get_version>]

Returns the number of times the bone hierarchy has changed within this skeleton, including renames.

The Skeleton version is not serialized: only use within a single instance of Skeleton3D.

Use for invalidating caches in IK solvers and other nodes which process bones.


----



[bool<class_bool>] **has_bone_meta**\ (\ bone_idx\: [int<class_int>], key\: [StringName<class_StringName>]\ ) |const| [🔗<class_Skeleton3D_method_has_bone_meta>]

Returns `true` if the bone at index `bone_idx` has metadata with the given `key`.


----



[bool<class_bool>] **is_bone_enabled**\ (\ bone_idx\: [int<class_int>]\ ) |const| [🔗<class_Skeleton3D_method_is_bone_enabled>]

Returns whether the bone pose for the bone at `bone_idx` is enabled.


----



|void| **localize_rests**\ (\ ) [🔗<class_Skeleton3D_method_localize_rests>]

Returns all bones in the skeleton to their rest poses.


----



|void| **physical_bones_add_collision_exception**\ (\ exception\: [RID<class_RID>]\ ) [🔗<class_Skeleton3D_method_physical_bones_add_collision_exception>]

**Deprecated:** This method may be changed or removed in future versions.

Adds a collision exception to the physical bone.

Works just like the [RigidBody3D<class_RigidBody3D>] node.


----



|void| **physical_bones_remove_collision_exception**\ (\ exception\: [RID<class_RID>]\ ) [🔗<class_Skeleton3D_method_physical_bones_remove_collision_exception>]

**Deprecated:** This method may be changed or removed in future versions.

Removes a collision exception to the physical bone.

Works just like the [RigidBody3D<class_RigidBody3D>] node.


----



|void| **physical_bones_start_simulation**\ (\ bones\: [Array<class_Array>]\[[StringName<class_StringName>]\] = []\ ) [🔗<class_Skeleton3D_method_physical_bones_start_simulation>]

**Deprecated:** This method may be changed or removed in future versions.

Tells the [PhysicalBone3D<class_PhysicalBone3D>] nodes in the Skeleton to start simulating and reacting to the physics world.

Optionally, a list of bone names can be passed-in, allowing only the passed-in bones to be simulated.


----



|void| **physical_bones_stop_simulation**\ (\ ) [🔗<class_Skeleton3D_method_physical_bones_stop_simulation>]

**Deprecated:** This method may be changed or removed in future versions.

Tells the [PhysicalBone3D<class_PhysicalBone3D>] nodes in the Skeleton to stop simulating.


----



[SkinReference<class_SkinReference>] **register_skin**\ (\ skin\: [Skin<class_Skin>]\ ) [🔗<class_Skeleton3D_method_register_skin>]

Binds the given Skin to the Skeleton.


----



|void| **reset_bone_pose**\ (\ bone_idx\: [int<class_int>]\ ) [🔗<class_Skeleton3D_method_reset_bone_pose>]

Sets the bone pose to rest for `bone_idx`.


----



|void| **reset_bone_poses**\ (\ ) [🔗<class_Skeleton3D_method_reset_bone_poses>]

Sets all bone poses to rests.


----



|void| **set_bone_enabled**\ (\ bone_idx\: [int<class_int>], enabled\: [bool<class_bool>] = true\ ) [🔗<class_Skeleton3D_method_set_bone_enabled>]

Disables the pose for the bone at `bone_idx` if `false`, enables the bone pose if `true`.


----



|void| **set_bone_global_pose**\ (\ bone_idx\: [int<class_int>], pose\: [Transform3D<class_Transform3D>]\ ) [🔗<class_Skeleton3D_method_set_bone_global_pose>]

Sets the global pose transform, `pose`, for the bone at `bone_idx`.

\ **Note:** If other bone poses have been changed, this method executes a dirty poses recalculation and will cause performance to deteriorate. If you know that multiple global poses will be applied, consider using [set_bone_pose()<class_Skeleton3D_method_set_bone_pose>] with precalculation.


----



|void| **set_bone_global_pose_override**\ (\ bone_idx\: [int<class_int>], pose\: [Transform3D<class_Transform3D>], amount\: [float<class_float>], persistent\: [bool<class_bool>] = false\ ) [🔗<class_Skeleton3D_method_set_bone_global_pose_override>]

**Deprecated:** This method may be changed or removed in future versions.

Sets the global pose transform, `pose`, for the bone at `bone_idx`.

\ `amount` is the interpolation strength that will be used when applying the pose, and `persistent` determines if the applied pose will remain.

\ **Note:** The pose transform needs to be a global pose! To convert a world transform from a [Node3D<class_Node3D>] to a global bone pose, multiply the [Transform3D.affine_inverse()<class_Transform3D_method_affine_inverse>] of the node's [Node3D.global_transform<class_Node3D_property_global_transform>] by the desired world transform.


----



|void| **set_bone_meta**\ (\ bone_idx\: [int<class_int>], key\: [StringName<class_StringName>], value\: [Variant<class_Variant>]\ ) [🔗<class_Skeleton3D_method_set_bone_meta>]

Sets the metadata with the given `key` to `value` for the bone at index `bone_idx`.


----



|void| **set_bone_name**\ (\ bone_idx\: [int<class_int>], name\: [String<class_String>]\ ) [🔗<class_Skeleton3D_method_set_bone_name>]

Sets the bone name, `name`, for the bone at `bone_idx`.


----



|void| **set_bone_parent**\ (\ bone_idx\: [int<class_int>], parent_idx\: [int<class_int>]\ ) [🔗<class_Skeleton3D_method_set_bone_parent>]

Sets the bone index `parent_idx` as the parent of the bone at `bone_idx`. If -1, then bone has no parent.

\ **Note:** `parent_idx` must be less than `bone_idx`.


----



|void| **set_bone_pose**\ (\ bone_idx\: [int<class_int>], pose\: [Transform3D<class_Transform3D>]\ ) [🔗<class_Skeleton3D_method_set_bone_pose>]

Sets the pose transform, `pose`, for the bone at `bone_idx`.


----



|void| **set_bone_pose_position**\ (\ bone_idx\: [int<class_int>], position\: [Vector3<class_Vector3>]\ ) [🔗<class_Skeleton3D_method_set_bone_pose_position>]

Sets the pose position of the bone at `bone_idx` to `position`. `position` is a [Vector3<class_Vector3>] describing a position local to the **Skeleton3D** node.


----



|void| **set_bone_pose_rotation**\ (\ bone_idx\: [int<class_int>], rotation\: [Quaternion<class_Quaternion>]\ ) [🔗<class_Skeleton3D_method_set_bone_pose_rotation>]

Sets the pose rotation of the bone at `bone_idx` to `rotation`. `rotation` is a [Quaternion<class_Quaternion>] describing a rotation in the bone's local coordinate space with respect to the rotation of any parent bones.


----



|void| **set_bone_pose_scale**\ (\ bone_idx\: [int<class_int>], scale\: [Vector3<class_Vector3>]\ ) [🔗<class_Skeleton3D_method_set_bone_pose_scale>]

Sets the pose scale of the bone at `bone_idx` to `scale`.


----



|void| **set_bone_rest**\ (\ bone_idx\: [int<class_int>], rest\: [Transform3D<class_Transform3D>]\ ) [🔗<class_Skeleton3D_method_set_bone_rest>]

Sets the rest transform for bone `bone_idx`.


----



|void| **unparent_bone_and_rest**\ (\ bone_idx\: [int<class_int>]\ ) [🔗<class_Skeleton3D_method_unparent_bone_and_rest>]

Unparents the bone at `bone_idx` and sets its rest position to that of its parent prior to being reset.

