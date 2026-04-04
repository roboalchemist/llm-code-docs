:github_url: hide



# SkeletonModifier3D

**Inherits:** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

**Inherited By:** [BoneConstraint3D<class_BoneConstraint3D>], [BoneTwistDisperser3D<class_BoneTwistDisperser3D>], [IKModifier3D<class_IKModifier3D>], [LimitAngularVelocityModifier3D<class_LimitAngularVelocityModifier3D>], [LookAtModifier3D<class_LookAtModifier3D>], [ModifierBoneTarget3D<class_ModifierBoneTarget3D>], [PhysicalBoneSimulator3D<class_PhysicalBoneSimulator3D>], [RetargetModifier3D<class_RetargetModifier3D>], [SkeletonIK3D<class_SkeletonIK3D>], [SpringBoneSimulator3D<class_SpringBoneSimulator3D>], [XRBodyModifier3D<class_XRBodyModifier3D>], [XRHandModifier3D<class_XRHandModifier3D>]

A node that may modify a Skeleton3D's bones.


## Description

**SkeletonModifier3D** retrieves a target [Skeleton3D<class_Skeleton3D>] by having a [Skeleton3D<class_Skeleton3D>] parent.

If there is an [AnimationMixer<class_AnimationMixer>], a modification always performs after playback process of the [AnimationMixer<class_AnimationMixer>].

This node should be used to implement custom IK solvers, constraints, or skeleton physics.


## Tutorials

- [Design of the Skeleton Modifier 3D ](https://godotengine.org/article/design-of-the-skeleton-modifier-3d/)_


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+---------------------------------------------------------------+----------+
> | :ref:`bool<class_bool>`   | :ref:`active<class_SkeletonModifier3D_property_active>`       | ``true`` |
> +---------------------------+---------------------------------------------------------------+----------+
> | :ref:`float<class_float>` | :ref:`influence<class_SkeletonModifier3D_property_influence>` | ``1.0``  |
> +---------------------------+---------------------------------------------------------------+----------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                              | :ref:`_process_modification<class_SkeletonModifier3D_private_method__process_modification>`\ (\ ) |virtual|                                                                                                 |
> +-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                              | :ref:`_process_modification_with_delta<class_SkeletonModifier3D_private_method__process_modification_with_delta>`\ (\ delta\: :ref:`float<class_float>`\ ) |virtual|                                        |
> +-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                              | :ref:`_skeleton_changed<class_SkeletonModifier3D_private_method__skeleton_changed>`\ (\ old_skeleton\: :ref:`Skeleton3D<class_Skeleton3D>`, new_skeleton\: :ref:`Skeleton3D<class_Skeleton3D>`\ ) |virtual| |
> +-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                              | :ref:`_validate_bone_names<class_SkeletonModifier3D_private_method__validate_bone_names>`\ (\ ) |virtual|                                                                                                   |
> +-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Skeleton3D<class_Skeleton3D>` | :ref:`get_skeleton<class_SkeletonModifier3D_method_get_skeleton>`\ (\ ) |const|                                                                                                                             |
> +-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**modification_processed**\ (\ ) [🔗<class_SkeletonModifier3D_signal_modification_processed>]

Notifies when the modification have been finished.

\ **Note:** If you want to get the modified bone pose by the modifier, you must use [Skeleton3D.get_bone_pose()<class_Skeleton3D_method_get_bone_pose>] or [Skeleton3D.get_bone_global_pose()<class_Skeleton3D_method_get_bone_global_pose>] at the moment this signal is fired.


----


## Enumerations



enum **BoneAxis**: [🔗<enum_SkeletonModifier3D_BoneAxis>]



[BoneAxis<enum_SkeletonModifier3D_BoneAxis>] **BONE_AXIS_PLUS_X** = `0`

Enumerated value for the +X axis.



[BoneAxis<enum_SkeletonModifier3D_BoneAxis>] **BONE_AXIS_MINUS_X** = `1`

Enumerated value for the -X axis.



[BoneAxis<enum_SkeletonModifier3D_BoneAxis>] **BONE_AXIS_PLUS_Y** = `2`

Enumerated value for the +Y axis.



[BoneAxis<enum_SkeletonModifier3D_BoneAxis>] **BONE_AXIS_MINUS_Y** = `3`

Enumerated value for the -Y axis.



[BoneAxis<enum_SkeletonModifier3D_BoneAxis>] **BONE_AXIS_PLUS_Z** = `4`

Enumerated value for the +Z axis.



[BoneAxis<enum_SkeletonModifier3D_BoneAxis>] **BONE_AXIS_MINUS_Z** = `5`

Enumerated value for the -Z axis.


----



enum **BoneDirection**: [🔗<enum_SkeletonModifier3D_BoneDirection>]



[BoneDirection<enum_SkeletonModifier3D_BoneDirection>] **BONE_DIRECTION_PLUS_X** = `0`

Enumerated value for the +X axis.



[BoneDirection<enum_SkeletonModifier3D_BoneDirection>] **BONE_DIRECTION_MINUS_X** = `1`

Enumerated value for the -X axis.



[BoneDirection<enum_SkeletonModifier3D_BoneDirection>] **BONE_DIRECTION_PLUS_Y** = `2`

Enumerated value for the +Y axis.



[BoneDirection<enum_SkeletonModifier3D_BoneDirection>] **BONE_DIRECTION_MINUS_Y** = `3`

Enumerated value for the -Y axis.



[BoneDirection<enum_SkeletonModifier3D_BoneDirection>] **BONE_DIRECTION_PLUS_Z** = `4`

Enumerated value for the +Z axis.



[BoneDirection<enum_SkeletonModifier3D_BoneDirection>] **BONE_DIRECTION_MINUS_Z** = `5`

Enumerated value for the -Z axis.



[BoneDirection<enum_SkeletonModifier3D_BoneDirection>] **BONE_DIRECTION_FROM_PARENT** = `6`

Enumerated value for the axis from a parent bone to the child bone.


----



enum **SecondaryDirection**: [🔗<enum_SkeletonModifier3D_SecondaryDirection>]



[SecondaryDirection<enum_SkeletonModifier3D_SecondaryDirection>] **SECONDARY_DIRECTION_NONE** = `0`

Enumerated value for the case when the axis is undefined.



[SecondaryDirection<enum_SkeletonModifier3D_SecondaryDirection>] **SECONDARY_DIRECTION_PLUS_X** = `1`

Enumerated value for the +X axis.



[SecondaryDirection<enum_SkeletonModifier3D_SecondaryDirection>] **SECONDARY_DIRECTION_MINUS_X** = `2`

Enumerated value for the -X axis.



[SecondaryDirection<enum_SkeletonModifier3D_SecondaryDirection>] **SECONDARY_DIRECTION_PLUS_Y** = `3`

Enumerated value for the +Y axis.



[SecondaryDirection<enum_SkeletonModifier3D_SecondaryDirection>] **SECONDARY_DIRECTION_MINUS_Y** = `4`

Enumerated value for the -Y axis.



[SecondaryDirection<enum_SkeletonModifier3D_SecondaryDirection>] **SECONDARY_DIRECTION_PLUS_Z** = `5`

Enumerated value for the +Z axis.



[SecondaryDirection<enum_SkeletonModifier3D_SecondaryDirection>] **SECONDARY_DIRECTION_MINUS_Z** = `6`

Enumerated value for the -Z axis.



[SecondaryDirection<enum_SkeletonModifier3D_SecondaryDirection>] **SECONDARY_DIRECTION_CUSTOM** = `7`

Enumerated value for an optional axis.


----



enum **RotationAxis**: [🔗<enum_SkeletonModifier3D_RotationAxis>]



[RotationAxis<enum_SkeletonModifier3D_RotationAxis>] **ROTATION_AXIS_X** = `0`

Enumerated value for the rotation of the X axis.



[RotationAxis<enum_SkeletonModifier3D_RotationAxis>] **ROTATION_AXIS_Y** = `1`

Enumerated value for the rotation of the Y axis.



[RotationAxis<enum_SkeletonModifier3D_RotationAxis>] **ROTATION_AXIS_Z** = `2`

Enumerated value for the rotation of the Z axis.



[RotationAxis<enum_SkeletonModifier3D_RotationAxis>] **ROTATION_AXIS_ALL** = `3`

Enumerated value for the unconstrained rotation.



[RotationAxis<enum_SkeletonModifier3D_RotationAxis>] **ROTATION_AXIS_CUSTOM** = `4`

Enumerated value for an optional rotation axis.


----


## Property Descriptions



[bool<class_bool>] **active** = `true` [🔗<class_SkeletonModifier3D_property_active>]


- |void| **set_active**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_active**\ (\ )

If `true`, the **SkeletonModifier3D** will be processing.


----



[float<class_float>] **influence** = `1.0` [🔗<class_SkeletonModifier3D_property_influence>]


- |void| **set_influence**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_influence**\ (\ )

Sets the influence of the modification.

\ **Note:** This value is used by [Skeleton3D<class_Skeleton3D>] to blend, so the **SkeletonModifier3D** should always apply only 100% of the result without interpolation.


----


## Method Descriptions



|void| **_process_modification**\ (\ ) |virtual| [🔗<class_SkeletonModifier3D_private_method__process_modification>]

**Deprecated:** Use [_process_modification_with_delta()<class_SkeletonModifier3D_private_method__process_modification_with_delta>] instead.

Override this virtual method to implement a custom skeleton modifier. You should do things like get the [Skeleton3D<class_Skeleton3D>]'s current pose and apply the pose here.

\ [_process_modification()<class_SkeletonModifier3D_private_method__process_modification>] must not apply [influence<class_SkeletonModifier3D_property_influence>] to bone poses because the [Skeleton3D<class_Skeleton3D>] automatically applies influence to all bone poses set by the modifier.


----



|void| **_process_modification_with_delta**\ (\ delta\: [float<class_float>]\ ) |virtual| [🔗<class_SkeletonModifier3D_private_method__process_modification_with_delta>]

Override this virtual method to implement a custom skeleton modifier. You should do things like get the [Skeleton3D<class_Skeleton3D>]'s current pose and apply the pose here.

\ [_process_modification_with_delta()<class_SkeletonModifier3D_private_method__process_modification_with_delta>] must not apply [influence<class_SkeletonModifier3D_property_influence>] to bone poses because the [Skeleton3D<class_Skeleton3D>] automatically applies influence to all bone poses set by the modifier.

\ `delta` is passed from parent [Skeleton3D<class_Skeleton3D>]. See also [Skeleton3D.advance()<class_Skeleton3D_method_advance>].

\ **Note:** This method may be called outside [Node._process()<class_Node_private_method__process>] and [Node._physics_process()<class_Node_private_method__physics_process>] with `delta` is `0.0`, since the modification should be processed immediately after initialization of the [Skeleton3D<class_Skeleton3D>].


----



|void| **_skeleton_changed**\ (\ old_skeleton\: [Skeleton3D<class_Skeleton3D>], new_skeleton\: [Skeleton3D<class_Skeleton3D>]\ ) |virtual| [🔗<class_SkeletonModifier3D_private_method__skeleton_changed>]

Called when the skeleton is changed.


----



|void| **_validate_bone_names**\ (\ ) |virtual| [🔗<class_SkeletonModifier3D_private_method__validate_bone_names>]

Called when bone names and indices need to be validated, such as when entering the scene tree or changing skeleton.


----



[Skeleton3D<class_Skeleton3D>] **get_skeleton**\ (\ ) |const| [🔗<class_SkeletonModifier3D_method_get_skeleton>]

Returns the parent [Skeleton3D<class_Skeleton3D>] node if it exists. Otherwise, returns `null`.

