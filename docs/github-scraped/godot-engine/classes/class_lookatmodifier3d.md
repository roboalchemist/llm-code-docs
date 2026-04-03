:github_url: hide



# LookAtModifier3D

**Inherits:** [SkeletonModifier3D<class_SkeletonModifier3D>] **<** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

The **LookAtModifier3D** rotates a bone to look at a target.


## Description

This [SkeletonModifier3D<class_SkeletonModifier3D>] rotates a bone to look at a target. This is helpful for moving a character's head to look at the player, rotating a turret to look at a target, or any other case where you want to make a bone rotate towards something quickly and easily.

When applying multiple **LookAtModifier3D**\ s, the **LookAtModifier3D** assigned to the parent bone must be put above the **LookAtModifier3D** assigned to the child bone in the list in order for the child bone results to be correct.


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------+----------------------+
> | :ref:`int<class_int>`                               | :ref:`bone<class_LookAtModifier3D_property_bone>`                                                           | ``-1``               |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------+----------------------+
> | :ref:`String<class_String>`                         | :ref:`bone_name<class_LookAtModifier3D_property_bone_name>`                                                 | ``""``               |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------+----------------------+
> | :ref:`float<class_float>`                           | :ref:`duration<class_LookAtModifier3D_property_duration>`                                                   | ``0.0``              |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------+----------------------+
> | :ref:`EaseType<enum_Tween_EaseType>`                | :ref:`ease_type<class_LookAtModifier3D_property_ease_type>`                                                 | ``0``                |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------+----------------------+
> | :ref:`BoneAxis<enum_SkeletonModifier3D_BoneAxis>`   | :ref:`forward_axis<class_LookAtModifier3D_property_forward_axis>`                                           | ``4``                |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------+----------------------+
> | :ref:`int<class_int>`                               | :ref:`origin_bone<class_LookAtModifier3D_property_origin_bone>`                                             |                      |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------+----------------------+
> | :ref:`String<class_String>`                         | :ref:`origin_bone_name<class_LookAtModifier3D_property_origin_bone_name>`                                   |                      |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------+----------------------+
> | :ref:`NodePath<class_NodePath>`                     | :ref:`origin_external_node<class_LookAtModifier3D_property_origin_external_node>`                           |                      |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------+----------------------+
> | :ref:`OriginFrom<enum_LookAtModifier3D_OriginFrom>` | :ref:`origin_from<class_LookAtModifier3D_property_origin_from>`                                             | ``0``                |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------+----------------------+
> | :ref:`Vector3<class_Vector3>`                       | :ref:`origin_offset<class_LookAtModifier3D_property_origin_offset>`                                         | ``Vector3(0, 0, 0)`` |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------+----------------------+
> | :ref:`float<class_float>`                           | :ref:`origin_safe_margin<class_LookAtModifier3D_property_origin_safe_margin>`                               | ``0.1``              |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------+----------------------+
> | :ref:`float<class_float>`                           | :ref:`primary_damp_threshold<class_LookAtModifier3D_property_primary_damp_threshold>`                       |                      |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------+----------------------+
> | :ref:`float<class_float>`                           | :ref:`primary_limit_angle<class_LookAtModifier3D_property_primary_limit_angle>`                             |                      |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------+----------------------+
> | :ref:`float<class_float>`                           | :ref:`primary_negative_damp_threshold<class_LookAtModifier3D_property_primary_negative_damp_threshold>`     |                      |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------+----------------------+
> | :ref:`float<class_float>`                           | :ref:`primary_negative_limit_angle<class_LookAtModifier3D_property_primary_negative_limit_angle>`           |                      |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------+----------------------+
> | :ref:`float<class_float>`                           | :ref:`primary_positive_damp_threshold<class_LookAtModifier3D_property_primary_positive_damp_threshold>`     |                      |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------+----------------------+
> | :ref:`float<class_float>`                           | :ref:`primary_positive_limit_angle<class_LookAtModifier3D_property_primary_positive_limit_angle>`           |                      |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------+----------------------+
> | :ref:`Axis<enum_Vector3_Axis>`                      | :ref:`primary_rotation_axis<class_LookAtModifier3D_property_primary_rotation_axis>`                         | ``1``                |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------+----------------------+
> | :ref:`bool<class_bool>`                             | :ref:`relative<class_LookAtModifier3D_property_relative>`                                                   | ``true``             |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------+----------------------+
> | :ref:`float<class_float>`                           | :ref:`secondary_damp_threshold<class_LookAtModifier3D_property_secondary_damp_threshold>`                   |                      |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------+----------------------+
> | :ref:`float<class_float>`                           | :ref:`secondary_limit_angle<class_LookAtModifier3D_property_secondary_limit_angle>`                         |                      |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------+----------------------+
> | :ref:`float<class_float>`                           | :ref:`secondary_negative_damp_threshold<class_LookAtModifier3D_property_secondary_negative_damp_threshold>` |                      |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------+----------------------+
> | :ref:`float<class_float>`                           | :ref:`secondary_negative_limit_angle<class_LookAtModifier3D_property_secondary_negative_limit_angle>`       |                      |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------+----------------------+
> | :ref:`float<class_float>`                           | :ref:`secondary_positive_damp_threshold<class_LookAtModifier3D_property_secondary_positive_damp_threshold>` |                      |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------+----------------------+
> | :ref:`float<class_float>`                           | :ref:`secondary_positive_limit_angle<class_LookAtModifier3D_property_secondary_positive_limit_angle>`       |                      |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------+----------------------+
> | :ref:`bool<class_bool>`                             | :ref:`symmetry_limitation<class_LookAtModifier3D_property_symmetry_limitation>`                             |                      |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------+----------------------+
> | :ref:`NodePath<class_NodePath>`                     | :ref:`target_node<class_LookAtModifier3D_property_target_node>`                                             | ``NodePath("")``     |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------+----------------------+
> | :ref:`TransitionType<enum_Tween_TransitionType>`    | :ref:`transition_type<class_LookAtModifier3D_property_transition_type>`                                     | ``0``                |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------+----------------------+
> | :ref:`bool<class_bool>`                             | :ref:`use_angle_limitation<class_LookAtModifier3D_property_use_angle_limitation>`                           | ``false``            |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------+----------------------+
> | :ref:`bool<class_bool>`                             | :ref:`use_secondary_rotation<class_LookAtModifier3D_property_use_secondary_rotation>`                       | ``true``             |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------+----------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------+-------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>` | :ref:`get_interpolation_remaining<class_LookAtModifier3D_method_get_interpolation_remaining>`\ (\ ) |const| |
> +---------------------------+-------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`   | :ref:`is_interpolating<class_LookAtModifier3D_method_is_interpolating>`\ (\ ) |const|                       |
> +---------------------------+-------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`   | :ref:`is_target_within_limitation<class_LookAtModifier3D_method_is_target_within_limitation>`\ (\ ) |const| |
> +---------------------------+-------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **OriginFrom**: [🔗<enum_LookAtModifier3D_OriginFrom>]



[OriginFrom<enum_LookAtModifier3D_OriginFrom>] **ORIGIN_FROM_SELF** = `0`

The bone rest position of the bone specified in [bone<class_LookAtModifier3D_property_bone>] is used as origin.



[OriginFrom<enum_LookAtModifier3D_OriginFrom>] **ORIGIN_FROM_SPECIFIC_BONE** = `1`

The bone global pose position of the bone specified in [origin_bone<class_LookAtModifier3D_property_origin_bone>] is used as origin.

\ **Note:** It is recommended that you select only the parent bone unless you are familiar with the bone processing process. The specified bone pose at the time the **LookAtModifier3D** is processed is used as a reference. In other words, if you specify a child bone and the **LookAtModifier3D** causes the child bone to move, the rendered result and direction will not match.



[OriginFrom<enum_LookAtModifier3D_OriginFrom>] **ORIGIN_FROM_EXTERNAL_NODE** = `2`

The global position of the [Node3D<class_Node3D>] specified in [origin_external_node<class_LookAtModifier3D_property_origin_external_node>] is used as origin.

\ **Note:** Same as [ORIGIN_FROM_SPECIFIC_BONE<class_LookAtModifier3D_constant_ORIGIN_FROM_SPECIFIC_BONE>], when specifying a [BoneAttachment3D<class_BoneAttachment3D>] with a child bone assigned, the rendered result and direction will not match.


----


## Property Descriptions



[int<class_int>] **bone** = `-1` [🔗<class_LookAtModifier3D_property_bone>]


- |void| **set_bone**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_bone**\ (\ )

Index of the [bone_name<class_LookAtModifier3D_property_bone_name>] in the parent [Skeleton3D<class_Skeleton3D>].


----



[String<class_String>] **bone_name** = `""` [🔗<class_LookAtModifier3D_property_bone_name>]


- |void| **set_bone_name**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_bone_name**\ (\ )

The bone name of the [Skeleton3D<class_Skeleton3D>] that the modification will operate on.


----



[float<class_float>] **duration** = `0.0` [🔗<class_LookAtModifier3D_property_duration>]


- |void| **set_duration**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_duration**\ (\ )

The duration of the time-based interpolation. Interpolation is triggered at the following cases:

- When the target node is changed

- When an axis is flipped due to angle limitation

\ **Note:** The flipping occurs when the target is outside the angle limitation and the internally computed secondary rotation axis of the forward vector is flipped. Visually, it occurs when the target is outside the angle limitation and crosses the plane of the [forward_axis<class_LookAtModifier3D_property_forward_axis>] and [primary_rotation_axis<class_LookAtModifier3D_property_primary_rotation_axis>].


----



[EaseType<enum_Tween_EaseType>] **ease_type** = `0` [🔗<class_LookAtModifier3D_property_ease_type>]


- |void| **set_ease_type**\ (\ value\: [EaseType<enum_Tween_EaseType>]\ )
- [EaseType<enum_Tween_EaseType>] **get_ease_type**\ (\ )

The ease type of the time-based interpolation. See also [EaseType<enum_Tween_EaseType>].


----



[BoneAxis<enum_SkeletonModifier3D_BoneAxis>] **forward_axis** = `4` [🔗<class_LookAtModifier3D_property_forward_axis>]


- |void| **set_forward_axis**\ (\ value\: [BoneAxis<enum_SkeletonModifier3D_BoneAxis>]\ )
- [BoneAxis<enum_SkeletonModifier3D_BoneAxis>] **get_forward_axis**\ (\ )

The forward axis of the bone. This [SkeletonModifier3D<class_SkeletonModifier3D>] modifies the bone so that this axis points toward the [target_node<class_LookAtModifier3D_property_target_node>].


----



[int<class_int>] **origin_bone** [🔗<class_LookAtModifier3D_property_origin_bone>]


- |void| **set_origin_bone**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_origin_bone**\ (\ )

Index of the [origin_bone_name<class_LookAtModifier3D_property_origin_bone_name>] in the parent [Skeleton3D<class_Skeleton3D>].


----



[String<class_String>] **origin_bone_name** [🔗<class_LookAtModifier3D_property_origin_bone_name>]


- |void| **set_origin_bone_name**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_origin_bone_name**\ (\ )

If [origin_from<class_LookAtModifier3D_property_origin_from>] is [ORIGIN_FROM_SPECIFIC_BONE<class_LookAtModifier3D_constant_ORIGIN_FROM_SPECIFIC_BONE>], the bone global pose position specified for this is used as origin.


----



[NodePath<class_NodePath>] **origin_external_node** [🔗<class_LookAtModifier3D_property_origin_external_node>]


- |void| **set_origin_external_node**\ (\ value\: [NodePath<class_NodePath>]\ )
- [NodePath<class_NodePath>] **get_origin_external_node**\ (\ )

If [origin_from<class_LookAtModifier3D_property_origin_from>] is [ORIGIN_FROM_EXTERNAL_NODE<class_LookAtModifier3D_constant_ORIGIN_FROM_EXTERNAL_NODE>], the global position of the [Node3D<class_Node3D>] specified for this is used as origin.


----



[OriginFrom<enum_LookAtModifier3D_OriginFrom>] **origin_from** = `0` [🔗<class_LookAtModifier3D_property_origin_from>]


- |void| **set_origin_from**\ (\ value\: [OriginFrom<enum_LookAtModifier3D_OriginFrom>]\ )
- [OriginFrom<enum_LookAtModifier3D_OriginFrom>] **get_origin_from**\ (\ )

This value determines from what origin is retrieved for use in the calculation of the forward vector.


----



[Vector3<class_Vector3>] **origin_offset** = `Vector3(0, 0, 0)` [🔗<class_LookAtModifier3D_property_origin_offset>]


- |void| **set_origin_offset**\ (\ value\: [Vector3<class_Vector3>]\ )
- [Vector3<class_Vector3>] **get_origin_offset**\ (\ )

The offset of the bone pose origin. Matching the origins by offset is useful for cases where multiple bones must always face the same direction, such as the eyes.

\ **Note:** This value indicates the local position of the object set in [origin_from<class_LookAtModifier3D_property_origin_from>].


----



[float<class_float>] **origin_safe_margin** = `0.1` [🔗<class_LookAtModifier3D_property_origin_safe_margin>]


- |void| **set_origin_safe_margin**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_origin_safe_margin**\ (\ )

If the target passes through too close to the origin than this value, time-based interpolation is used even if the target is within the angular limitations, to prevent the angular velocity from becoming too high.


----



[float<class_float>] **primary_damp_threshold** [🔗<class_LookAtModifier3D_property_primary_damp_threshold>]


- |void| **set_primary_damp_threshold**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_primary_damp_threshold**\ (\ )

The threshold to start damping for [primary_limit_angle<class_LookAtModifier3D_property_primary_limit_angle>]. It provides non-linear (b-spline) interpolation, let it feel more resistance the more it rotate to the edge limit. This is useful for simulating the limits of human motion.

If `1.0`, no damping is performed. If `0.0`, damping is always performed.


----



[float<class_float>] **primary_limit_angle** [🔗<class_LookAtModifier3D_property_primary_limit_angle>]


- |void| **set_primary_limit_angle**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_primary_limit_angle**\ (\ )

The limit angle of the primary rotation when [symmetry_limitation<class_LookAtModifier3D_property_symmetry_limitation>] is `true`, in radians.


----



[float<class_float>] **primary_negative_damp_threshold** [🔗<class_LookAtModifier3D_property_primary_negative_damp_threshold>]


- |void| **set_primary_negative_damp_threshold**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_primary_negative_damp_threshold**\ (\ )

The threshold to start damping for [primary_negative_limit_angle<class_LookAtModifier3D_property_primary_negative_limit_angle>].


----



[float<class_float>] **primary_negative_limit_angle** [🔗<class_LookAtModifier3D_property_primary_negative_limit_angle>]


- |void| **set_primary_negative_limit_angle**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_primary_negative_limit_angle**\ (\ )

The limit angle of negative side of the primary rotation when [symmetry_limitation<class_LookAtModifier3D_property_symmetry_limitation>] is `false`, in radians.


----



[float<class_float>] **primary_positive_damp_threshold** [🔗<class_LookAtModifier3D_property_primary_positive_damp_threshold>]


- |void| **set_primary_positive_damp_threshold**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_primary_positive_damp_threshold**\ (\ )

The threshold to start damping for [primary_positive_limit_angle<class_LookAtModifier3D_property_primary_positive_limit_angle>].


----



[float<class_float>] **primary_positive_limit_angle** [🔗<class_LookAtModifier3D_property_primary_positive_limit_angle>]


- |void| **set_primary_positive_limit_angle**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_primary_positive_limit_angle**\ (\ )

The limit angle of positive side of the primary rotation when [symmetry_limitation<class_LookAtModifier3D_property_symmetry_limitation>] is `false`, in radians.


----



[Axis<enum_Vector3_Axis>] **primary_rotation_axis** = `1` [🔗<class_LookAtModifier3D_property_primary_rotation_axis>]


- |void| **set_primary_rotation_axis**\ (\ value\: [Axis<enum_Vector3_Axis>]\ )
- [Axis<enum_Vector3_Axis>] **get_primary_rotation_axis**\ (\ )

The axis of the first rotation. This [SkeletonModifier3D<class_SkeletonModifier3D>] works by compositing the rotation by Euler angles to prevent to rotate the [forward_axis<class_LookAtModifier3D_property_forward_axis>].


----



[bool<class_bool>] **relative** = `true` [🔗<class_LookAtModifier3D_property_relative>]


- |void| **set_relative**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_relative**\ (\ )

The relative option. If `true`, the rotation is applied relative to the pose. If `false`, the rotation is applied relative to the rest. It means to replace the current pose with the **LookAtModifier3D**'s result.


----



[float<class_float>] **secondary_damp_threshold** [🔗<class_LookAtModifier3D_property_secondary_damp_threshold>]


- |void| **set_secondary_damp_threshold**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_secondary_damp_threshold**\ (\ )

The threshold to start damping for [secondary_limit_angle<class_LookAtModifier3D_property_secondary_limit_angle>].


----



[float<class_float>] **secondary_limit_angle** [🔗<class_LookAtModifier3D_property_secondary_limit_angle>]


- |void| **set_secondary_limit_angle**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_secondary_limit_angle**\ (\ )

The limit angle of the secondary rotation when [symmetry_limitation<class_LookAtModifier3D_property_symmetry_limitation>] is `true`, in radians.


----



[float<class_float>] **secondary_negative_damp_threshold** [🔗<class_LookAtModifier3D_property_secondary_negative_damp_threshold>]


- |void| **set_secondary_negative_damp_threshold**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_secondary_negative_damp_threshold**\ (\ )

The threshold to start damping for [secondary_negative_limit_angle<class_LookAtModifier3D_property_secondary_negative_limit_angle>].


----



[float<class_float>] **secondary_negative_limit_angle** [🔗<class_LookAtModifier3D_property_secondary_negative_limit_angle>]


- |void| **set_secondary_negative_limit_angle**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_secondary_negative_limit_angle**\ (\ )

The limit angle of negative side of the secondary rotation when [symmetry_limitation<class_LookAtModifier3D_property_symmetry_limitation>] is `false`, in radians.


----



[float<class_float>] **secondary_positive_damp_threshold** [🔗<class_LookAtModifier3D_property_secondary_positive_damp_threshold>]


- |void| **set_secondary_positive_damp_threshold**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_secondary_positive_damp_threshold**\ (\ )

The threshold to start damping for [secondary_positive_limit_angle<class_LookAtModifier3D_property_secondary_positive_limit_angle>].


----



[float<class_float>] **secondary_positive_limit_angle** [🔗<class_LookAtModifier3D_property_secondary_positive_limit_angle>]


- |void| **set_secondary_positive_limit_angle**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_secondary_positive_limit_angle**\ (\ )

The limit angle of positive side of the secondary rotation when [symmetry_limitation<class_LookAtModifier3D_property_symmetry_limitation>] is `false`, in radians.


----



[bool<class_bool>] **symmetry_limitation** [🔗<class_LookAtModifier3D_property_symmetry_limitation>]


- |void| **set_symmetry_limitation**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_limitation_symmetry**\ (\ )

If `true`, the limitations are spread from the bone symmetrically.

If `false`, the limitation can be specified separately for each side of the bone rest.


----



[NodePath<class_NodePath>] **target_node** = `NodePath("")` [🔗<class_LookAtModifier3D_property_target_node>]


- |void| **set_target_node**\ (\ value\: [NodePath<class_NodePath>]\ )
- [NodePath<class_NodePath>] **get_target_node**\ (\ )

The [NodePath<class_NodePath>] to the node that is the target for the look at modification. This node is what the modification will rotate the bone to.


----



[TransitionType<enum_Tween_TransitionType>] **transition_type** = `0` [🔗<class_LookAtModifier3D_property_transition_type>]


- |void| **set_transition_type**\ (\ value\: [TransitionType<enum_Tween_TransitionType>]\ )
- [TransitionType<enum_Tween_TransitionType>] **get_transition_type**\ (\ )

The transition type of the time-based interpolation. See also [TransitionType<enum_Tween_TransitionType>].


----



[bool<class_bool>] **use_angle_limitation** = `false` [🔗<class_LookAtModifier3D_property_use_angle_limitation>]


- |void| **set_use_angle_limitation**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_using_angle_limitation**\ (\ )

If `true`, limits the amount of rotation. For example, this helps to prevent a character's neck from rotating 360 degrees.

\ **Note:** As with [AnimationTree<class_AnimationTree>] blending, interpolation is provided that favors [Skeleton3D.get_bone_rest()<class_Skeleton3D_method_get_bone_rest>]. This means that interpolation does not select the shortest path in some cases.

\ **Note:** Some values for [transition_type<class_LookAtModifier3D_property_transition_type>] (such as [Tween.TRANS_BACK<class_Tween_constant_TRANS_BACK>], [Tween.TRANS_ELASTIC<class_Tween_constant_TRANS_ELASTIC>], and [Tween.TRANS_SPRING<class_Tween_constant_TRANS_SPRING>]) may exceed the limitations. If interpolation occurs while overshooting the limitations, the result might not respect the bone rest.


----



[bool<class_bool>] **use_secondary_rotation** = `true` [🔗<class_LookAtModifier3D_property_use_secondary_rotation>]


- |void| **set_use_secondary_rotation**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_using_secondary_rotation**\ (\ )

If `true`, provides rotation by two axes.


----


## Method Descriptions



[float<class_float>] **get_interpolation_remaining**\ (\ ) |const| [🔗<class_LookAtModifier3D_method_get_interpolation_remaining>]

Returns the remaining seconds of the time-based interpolation.


----



[bool<class_bool>] **is_interpolating**\ (\ ) |const| [🔗<class_LookAtModifier3D_method_is_interpolating>]

Returns `true` if time-based interpolation is running. If `true`, it is equivalent to [get_interpolation_remaining()<class_LookAtModifier3D_method_get_interpolation_remaining>] returning `0.0`.

This is useful to determine whether a **LookAtModifier3D** can be removed safely.


----



[bool<class_bool>] **is_target_within_limitation**\ (\ ) |const| [🔗<class_LookAtModifier3D_method_is_target_within_limitation>]

Returns whether the target is within the angle limitations. It is useful for unsetting the [target_node<class_LookAtModifier3D_property_target_node>] when the target is outside of the angle limitations.

\ **Note:** The value is updated after [SkeletonModifier3D._process_modification()<class_SkeletonModifier3D_private_method__process_modification>]. To retrieve this value correctly, we recommend using the signal [SkeletonModifier3D.modification_processed<class_SkeletonModifier3D_signal_modification_processed>].

