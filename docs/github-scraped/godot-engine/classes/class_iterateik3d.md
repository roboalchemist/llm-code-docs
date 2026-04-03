:github_url: hide



# IterateIK3D

**Inherits:** [ChainIK3D<class_ChainIK3D>] **<** [IKModifier3D<class_IKModifier3D>] **<** [SkeletonModifier3D<class_SkeletonModifier3D>] **<** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

**Inherited By:** [CCDIK3D<class_CCDIK3D>], [FABRIK3D<class_FABRIK3D>], [JacobianIK3D<class_JacobianIK3D>]

A [SkeletonModifier3D<class_SkeletonModifier3D>] to approach the goal by repeating small rotations.


## Description

Base class of [SkeletonModifier3D<class_SkeletonModifier3D>] to approach the goal by repeating small rotations.

Each bone chain (setting) has one effector, which is processed in order of the setting list. You can set some limitations for each joint.


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+----------------------------------------------------------------------------+-----------------+
> | :ref:`float<class_float>` | :ref:`angular_delta_limit<class_IterateIK3D_property_angular_delta_limit>` | ``0.034906585`` |
> +---------------------------+----------------------------------------------------------------------------+-----------------+
> | :ref:`bool<class_bool>`   | :ref:`deterministic<class_IterateIK3D_property_deterministic>`             | ``false``       |
> +---------------------------+----------------------------------------------------------------------------+-----------------+
> | :ref:`int<class_int>`     | :ref:`max_iterations<class_IterateIK3D_property_max_iterations>`           | ``4``           |
> +---------------------------+----------------------------------------------------------------------------+-----------------+
> | :ref:`float<class_float>` | :ref:`min_distance<class_IterateIK3D_property_min_distance>`               | ``0.001``       |
> +---------------------------+----------------------------------------------------------------------------+-----------------+
> | :ref:`int<class_int>`     | :ref:`setting_count<class_IterateIK3D_property_setting_count>`             | ``0``           |
> +---------------------------+----------------------------------------------------------------------------+-----------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`JointLimitation3D<class_JointLimitation3D>`                     | :ref:`get_joint_limitation<class_IterateIK3D_method_get_joint_limitation>`\ (\ index\: :ref:`int<class_int>`, joint\: :ref:`int<class_int>`\ ) |const|                                                                                                  |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`SecondaryDirection<enum_SkeletonModifier3D_SecondaryDirection>` | :ref:`get_joint_limitation_right_axis<class_IterateIK3D_method_get_joint_limitation_right_axis>`\ (\ index\: :ref:`int<class_int>`, joint\: :ref:`int<class_int>`\ ) |const|                                                                            |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                                         | :ref:`get_joint_limitation_right_axis_vector<class_IterateIK3D_method_get_joint_limitation_right_axis_vector>`\ (\ index\: :ref:`int<class_int>`, joint\: :ref:`int<class_int>`\ ) |const|                                                              |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Quaternion<class_Quaternion>`                                   | :ref:`get_joint_limitation_rotation_offset<class_IterateIK3D_method_get_joint_limitation_rotation_offset>`\ (\ index\: :ref:`int<class_int>`, joint\: :ref:`int<class_int>`\ ) |const|                                                                  |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`RotationAxis<enum_SkeletonModifier3D_RotationAxis>`             | :ref:`get_joint_rotation_axis<class_IterateIK3D_method_get_joint_rotation_axis>`\ (\ index\: :ref:`int<class_int>`, joint\: :ref:`int<class_int>`\ ) |const|                                                                                            |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                                         | :ref:`get_joint_rotation_axis_vector<class_IterateIK3D_method_get_joint_rotation_axis_vector>`\ (\ index\: :ref:`int<class_int>`, joint\: :ref:`int<class_int>`\ ) |const|                                                                              |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`NodePath<class_NodePath>`                                       | :ref:`get_target_node<class_IterateIK3D_method_get_target_node>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                                                                                                           |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                | :ref:`set_joint_limitation<class_IterateIK3D_method_set_joint_limitation>`\ (\ index\: :ref:`int<class_int>`, joint\: :ref:`int<class_int>`, limitation\: :ref:`JointLimitation3D<class_JointLimitation3D>`\ )                                          |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                | :ref:`set_joint_limitation_right_axis<class_IterateIK3D_method_set_joint_limitation_right_axis>`\ (\ index\: :ref:`int<class_int>`, joint\: :ref:`int<class_int>`, direction\: :ref:`SecondaryDirection<enum_SkeletonModifier3D_SecondaryDirection>`\ ) |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                | :ref:`set_joint_limitation_right_axis_vector<class_IterateIK3D_method_set_joint_limitation_right_axis_vector>`\ (\ index\: :ref:`int<class_int>`, joint\: :ref:`int<class_int>`, vector\: :ref:`Vector3<class_Vector3>`\ )                              |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                | :ref:`set_joint_limitation_rotation_offset<class_IterateIK3D_method_set_joint_limitation_rotation_offset>`\ (\ index\: :ref:`int<class_int>`, joint\: :ref:`int<class_int>`, offset\: :ref:`Quaternion<class_Quaternion>`\ )                            |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                | :ref:`set_joint_rotation_axis<class_IterateIK3D_method_set_joint_rotation_axis>`\ (\ index\: :ref:`int<class_int>`, joint\: :ref:`int<class_int>`, axis\: :ref:`RotationAxis<enum_SkeletonModifier3D_RotationAxis>`\ )                                  |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                | :ref:`set_joint_rotation_axis_vector<class_IterateIK3D_method_set_joint_rotation_axis_vector>`\ (\ index\: :ref:`int<class_int>`, joint\: :ref:`int<class_int>`, axis_vector\: :ref:`Vector3<class_Vector3>`\ )                                         |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                | :ref:`set_target_node<class_IterateIK3D_method_set_target_node>`\ (\ index\: :ref:`int<class_int>`, target_node\: :ref:`NodePath<class_NodePath>`\ )                                                                                                    |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[float<class_float>] **angular_delta_limit** = `0.034906585` [🔗<class_IterateIK3D_property_angular_delta_limit>]


- |void| **set_angular_delta_limit**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_angular_delta_limit**\ (\ )

The maximum amount each bone can rotate in a single iteration.

\ **Note:** This limitation is applied during each iteration. For example, if [max_iterations<class_IterateIK3D_property_max_iterations>] is `4` and [angular_delta_limit<class_IterateIK3D_property_angular_delta_limit>] is `5` degrees, the maximum rotation possible in a single frame is `20` degrees.


----



[bool<class_bool>] **deterministic** = `false` [🔗<class_IterateIK3D_property_deterministic>]


- |void| **set_deterministic**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_deterministic**\ (\ )

If `false`, the result is calculated from the previous frame's **IterateIK3D** result as the initial state.

If `true`, the previous frame's **IterateIK3D** result is discarded. At this point, the new result is calculated from the bone pose excluding the **IterateIK3D** as the initial state. This means the result will be always equal as long as the target position and the previous bone pose are the same. However, if [angular_delta_limit<class_IterateIK3D_property_angular_delta_limit>] and [max_iterations<class_IterateIK3D_property_max_iterations>] are set too small, the end bone of the chain will never reach the target.


----



[int<class_int>] **max_iterations** = `4` [🔗<class_IterateIK3D_property_max_iterations>]


- |void| **set_max_iterations**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_max_iterations**\ (\ )

The number of iteration loops used by the IK solver to produce more accurate results.


----



[float<class_float>] **min_distance** = `0.001` [🔗<class_IterateIK3D_property_min_distance>]


- |void| **set_min_distance**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_min_distance**\ (\ )

The minimum distance between the end bone and the target. If the distance is below this value, the IK solver stops any further iterations.


----



[int<class_int>] **setting_count** = `0` [🔗<class_IterateIK3D_property_setting_count>]


- |void| **set_setting_count**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_setting_count**\ (\ )

The number of settings.


----


## Method Descriptions



[JointLimitation3D<class_JointLimitation3D>] **get_joint_limitation**\ (\ index\: [int<class_int>], joint\: [int<class_int>]\ ) |const| [🔗<class_IterateIK3D_method_get_joint_limitation>]

Returns the joint limitation at `joint` in the bone chain's joint list.


----



[SecondaryDirection<enum_SkeletonModifier3D_SecondaryDirection>] **get_joint_limitation_right_axis**\ (\ index\: [int<class_int>], joint\: [int<class_int>]\ ) |const| [🔗<class_IterateIK3D_method_get_joint_limitation_right_axis>]

Returns the joint limitation right axis at `joint` in the bone chain's joint list.


----



[Vector3<class_Vector3>] **get_joint_limitation_right_axis_vector**\ (\ index\: [int<class_int>], joint\: [int<class_int>]\ ) |const| [🔗<class_IterateIK3D_method_get_joint_limitation_right_axis_vector>]

Returns the joint limitation right axis vector at `joint` in the bone chain's joint list.

If [get_joint_limitation_right_axis()<class_IterateIK3D_method_get_joint_limitation_right_axis>] is [SkeletonModifier3D.SECONDARY_DIRECTION_NONE<class_SkeletonModifier3D_constant_SECONDARY_DIRECTION_NONE>], this method returns `Vector3(0, 0, 0)`.


----



[Quaternion<class_Quaternion>] **get_joint_limitation_rotation_offset**\ (\ index\: [int<class_int>], joint\: [int<class_int>]\ ) |const| [🔗<class_IterateIK3D_method_get_joint_limitation_rotation_offset>]

Returns the joint limitation rotation offset at `joint` in the bone chain's joint list.

Rotation is done in the local space which is constructed by the bone direction (in general parent to child) as the +Y axis and [get_joint_limitation_right_axis_vector()<class_IterateIK3D_method_get_joint_limitation_right_axis_vector>] as the +X axis.

If the +X and +Y axes are not orthogonal, the +X axis is implicitly modified to make it orthogonal.

Also, if the length of [get_joint_limitation_right_axis_vector()<class_IterateIK3D_method_get_joint_limitation_right_axis_vector>] is zero, the space is created by rotating the bone rest using the shortest arc that rotates the +Y axis of the bone rest to match the bone direction.


----



[RotationAxis<enum_SkeletonModifier3D_RotationAxis>] **get_joint_rotation_axis**\ (\ index\: [int<class_int>], joint\: [int<class_int>]\ ) |const| [🔗<class_IterateIK3D_method_get_joint_rotation_axis>]

Returns the rotation axis at `joint` in the bone chain's joint list.


----



[Vector3<class_Vector3>] **get_joint_rotation_axis_vector**\ (\ index\: [int<class_int>], joint\: [int<class_int>]\ ) |const| [🔗<class_IterateIK3D_method_get_joint_rotation_axis_vector>]

Returns the rotation axis vector for the specified joint in the bone chain. This vector represents the axis around which the joint can rotate. It is determined based on the rotation axis set for the joint.

If [get_joint_rotation_axis()<class_IterateIK3D_method_get_joint_rotation_axis>] is [SkeletonModifier3D.ROTATION_AXIS_ALL<class_SkeletonModifier3D_constant_ROTATION_AXIS_ALL>], this method returns `Vector3(0, 0, 0)`.


----



[NodePath<class_NodePath>] **get_target_node**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_IterateIK3D_method_get_target_node>]

Returns the target node that the end bone is trying to reach.


----



|void| **set_joint_limitation**\ (\ index\: [int<class_int>], joint\: [int<class_int>], limitation\: [JointLimitation3D<class_JointLimitation3D>]\ ) [🔗<class_IterateIK3D_method_set_joint_limitation>]

Sets the joint limitation at `joint` in the bone chain's joint list.


----



|void| **set_joint_limitation_right_axis**\ (\ index\: [int<class_int>], joint\: [int<class_int>], direction\: [SecondaryDirection<enum_SkeletonModifier3D_SecondaryDirection>]\ ) [🔗<class_IterateIK3D_method_set_joint_limitation_right_axis>]

Sets the joint limitation right axis at `joint` in the bone chain's joint list.


----



|void| **set_joint_limitation_right_axis_vector**\ (\ index\: [int<class_int>], joint\: [int<class_int>], vector\: [Vector3<class_Vector3>]\ ) [🔗<class_IterateIK3D_method_set_joint_limitation_right_axis_vector>]

Sets the optional joint limitation right axis vector at `joint` in the bone chain's joint list.


----



|void| **set_joint_limitation_rotation_offset**\ (\ index\: [int<class_int>], joint\: [int<class_int>], offset\: [Quaternion<class_Quaternion>]\ ) [🔗<class_IterateIK3D_method_set_joint_limitation_rotation_offset>]

Sets the joint limitation rotation offset at `joint` in the bone chain's joint list.

Rotation is done in the local space which is constructed by the bone direction (in general parent to child) as the +Y axis and [get_joint_limitation_right_axis_vector()<class_IterateIK3D_method_get_joint_limitation_right_axis_vector>] as the +X axis.

If the +X and +Y axes are not orthogonal, the +X axis is implicitly modified to make it orthogonal.

Also, if the length of [get_joint_limitation_right_axis_vector()<class_IterateIK3D_method_get_joint_limitation_right_axis_vector>] is zero, the space is created by rotating the bone rest using the shortest arc that rotates the +Y axis of the bone rest to match the bone direction.


----



|void| **set_joint_rotation_axis**\ (\ index\: [int<class_int>], joint\: [int<class_int>], axis\: [RotationAxis<enum_SkeletonModifier3D_RotationAxis>]\ ) [🔗<class_IterateIK3D_method_set_joint_rotation_axis>]

Sets the rotation axis at `joint` in the bone chain's joint list.

The axes are based on the [Skeleton3D.get_bone_rest()<class_Skeleton3D_method_get_bone_rest>]'s space, if `axis` is [SkeletonModifier3D.ROTATION_AXIS_CUSTOM<class_SkeletonModifier3D_constant_ROTATION_AXIS_CUSTOM>], you can specify any axis.

\ **Note:** The rotation axis and the forward vector shouldn't be colinear to avoid unintended rotation since [ChainIK3D<class_ChainIK3D>] does not factor in twisting forces.


----



|void| **set_joint_rotation_axis_vector**\ (\ index\: [int<class_int>], joint\: [int<class_int>], axis_vector\: [Vector3<class_Vector3>]\ ) [🔗<class_IterateIK3D_method_set_joint_rotation_axis_vector>]

Sets the rotation axis vector for the specified joint in the bone chain.

This vector is normalized by an internal process and represents the axis around which the bone chain can rotate.

If the vector length is `0`, it is considered synonymous with [SkeletonModifier3D.ROTATION_AXIS_ALL<class_SkeletonModifier3D_constant_ROTATION_AXIS_ALL>].


----



|void| **set_target_node**\ (\ index\: [int<class_int>], target_node\: [NodePath<class_NodePath>]\ ) [🔗<class_IterateIK3D_method_set_target_node>]

Sets the target node that the end bone is trying to reach.

