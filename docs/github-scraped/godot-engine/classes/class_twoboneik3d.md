:github_url: hide



# TwoBoneIK3D

**Inherits:** [IKModifier3D<class_IKModifier3D>] **<** [SkeletonModifier3D<class_SkeletonModifier3D>] **<** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

Rotation based intersection of two circles inverse kinematics solver.


## Description

This [IKModifier3D<class_IKModifier3D>] requires a pole target. It provides deterministic results by constructing a plane from each joint and pole target and finding the intersection of two circles (disks in 3D).

This IK can handle twist by setting the pole direction. If there are more than one bone between each set bone, their rotations are ignored, and the straight line connecting the root-middle and middle-end joints are treated as virtual bones.


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------+----------------------------------------------------------------+-------+
> | :ref:`int<class_int>` | :ref:`setting_count<class_TwoBoneIK3D_property_setting_count>` | ``0`` |
> +-----------------------+----------------------------------------------------------------+-------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                                 | :ref:`get_end_bone<class_TwoBoneIK3D_method_get_end_bone>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                                                           |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`BoneDirection<enum_SkeletonModifier3D_BoneDirection>`           | :ref:`get_end_bone_direction<class_TwoBoneIK3D_method_get_end_bone_direction>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                                       |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                             | :ref:`get_end_bone_length<class_TwoBoneIK3D_method_get_end_bone_length>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                                             |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                                           | :ref:`get_end_bone_name<class_TwoBoneIK3D_method_get_end_bone_name>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                                                 |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                                 | :ref:`get_middle_bone<class_TwoBoneIK3D_method_get_middle_bone>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                                                     |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                                           | :ref:`get_middle_bone_name<class_TwoBoneIK3D_method_get_middle_bone_name>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                                           |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`SecondaryDirection<enum_SkeletonModifier3D_SecondaryDirection>` | :ref:`get_pole_direction<class_TwoBoneIK3D_method_get_pole_direction>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                                               |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                                         | :ref:`get_pole_direction_vector<class_TwoBoneIK3D_method_get_pole_direction_vector>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                                 |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`NodePath<class_NodePath>`                                       | :ref:`get_pole_node<class_TwoBoneIK3D_method_get_pole_node>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                                                         |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                                 | :ref:`get_root_bone<class_TwoBoneIK3D_method_get_root_bone>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                                                         |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                                           | :ref:`get_root_bone_name<class_TwoBoneIK3D_method_get_root_bone_name>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                                               |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`NodePath<class_NodePath>`                                       | :ref:`get_target_node<class_TwoBoneIK3D_method_get_target_node>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                                                     |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                               | :ref:`is_end_bone_extended<class_TwoBoneIK3D_method_is_end_bone_extended>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                                           |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                               | :ref:`is_using_virtual_end<class_TwoBoneIK3D_method_is_using_virtual_end>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                                           |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                | :ref:`set_end_bone<class_TwoBoneIK3D_method_set_end_bone>`\ (\ index\: :ref:`int<class_int>`, bone\: :ref:`int<class_int>`\ )                                                                     |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                | :ref:`set_end_bone_direction<class_TwoBoneIK3D_method_set_end_bone_direction>`\ (\ index\: :ref:`int<class_int>`, bone_direction\: :ref:`BoneDirection<enum_SkeletonModifier3D_BoneDirection>`\ ) |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                | :ref:`set_end_bone_length<class_TwoBoneIK3D_method_set_end_bone_length>`\ (\ index\: :ref:`int<class_int>`, length\: :ref:`float<class_float>`\ )                                                 |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                | :ref:`set_end_bone_name<class_TwoBoneIK3D_method_set_end_bone_name>`\ (\ index\: :ref:`int<class_int>`, bone_name\: :ref:`String<class_String>`\ )                                                |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                | :ref:`set_extend_end_bone<class_TwoBoneIK3D_method_set_extend_end_bone>`\ (\ index\: :ref:`int<class_int>`, enabled\: :ref:`bool<class_bool>`\ )                                                  |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                | :ref:`set_middle_bone<class_TwoBoneIK3D_method_set_middle_bone>`\ (\ index\: :ref:`int<class_int>`, bone\: :ref:`int<class_int>`\ )                                                               |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                | :ref:`set_middle_bone_name<class_TwoBoneIK3D_method_set_middle_bone_name>`\ (\ index\: :ref:`int<class_int>`, bone_name\: :ref:`String<class_String>`\ )                                          |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                | :ref:`set_pole_direction<class_TwoBoneIK3D_method_set_pole_direction>`\ (\ index\: :ref:`int<class_int>`, direction\: :ref:`SecondaryDirection<enum_SkeletonModifier3D_SecondaryDirection>`\ )    |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                | :ref:`set_pole_direction_vector<class_TwoBoneIK3D_method_set_pole_direction_vector>`\ (\ index\: :ref:`int<class_int>`, vector\: :ref:`Vector3<class_Vector3>`\ )                                 |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                | :ref:`set_pole_node<class_TwoBoneIK3D_method_set_pole_node>`\ (\ index\: :ref:`int<class_int>`, pole_node\: :ref:`NodePath<class_NodePath>`\ )                                                    |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                | :ref:`set_root_bone<class_TwoBoneIK3D_method_set_root_bone>`\ (\ index\: :ref:`int<class_int>`, bone\: :ref:`int<class_int>`\ )                                                                   |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                | :ref:`set_root_bone_name<class_TwoBoneIK3D_method_set_root_bone_name>`\ (\ index\: :ref:`int<class_int>`, bone_name\: :ref:`String<class_String>`\ )                                              |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                | :ref:`set_target_node<class_TwoBoneIK3D_method_set_target_node>`\ (\ index\: :ref:`int<class_int>`, target_node\: :ref:`NodePath<class_NodePath>`\ )                                              |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                | :ref:`set_use_virtual_end<class_TwoBoneIK3D_method_set_use_virtual_end>`\ (\ index\: :ref:`int<class_int>`, enabled\: :ref:`bool<class_bool>`\ )                                                  |
> +-----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[int<class_int>] **setting_count** = `0` [🔗<class_TwoBoneIK3D_property_setting_count>]


- |void| **set_setting_count**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_setting_count**\ (\ )

The number of settings.


----


## Method Descriptions



[int<class_int>] **get_end_bone**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_TwoBoneIK3D_method_get_end_bone>]

Returns the end bone index.


----



[BoneDirection<enum_SkeletonModifier3D_BoneDirection>] **get_end_bone_direction**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_TwoBoneIK3D_method_get_end_bone_direction>]

Returns the end bone's tail direction when [is_end_bone_extended()<class_TwoBoneIK3D_method_is_end_bone_extended>] is `true`.


----



[float<class_float>] **get_end_bone_length**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_TwoBoneIK3D_method_get_end_bone_length>]

Returns the end bone tail length of the bone chain when [is_end_bone_extended()<class_TwoBoneIK3D_method_is_end_bone_extended>] is `true`.


----



[String<class_String>] **get_end_bone_name**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_TwoBoneIK3D_method_get_end_bone_name>]

Returns the end bone name.


----



[int<class_int>] **get_middle_bone**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_TwoBoneIK3D_method_get_middle_bone>]

Returns the middle bone index.


----



[String<class_String>] **get_middle_bone_name**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_TwoBoneIK3D_method_get_middle_bone_name>]

Returns the middle bone name.


----



[SecondaryDirection<enum_SkeletonModifier3D_SecondaryDirection>] **get_pole_direction**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_TwoBoneIK3D_method_get_pole_direction>]

Returns the pole direction.


----



[Vector3<class_Vector3>] **get_pole_direction_vector**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_TwoBoneIK3D_method_get_pole_direction_vector>]

Returns the pole direction vector.

If [get_pole_direction()<class_TwoBoneIK3D_method_get_pole_direction>] is [SkeletonModifier3D.SECONDARY_DIRECTION_NONE<class_SkeletonModifier3D_constant_SECONDARY_DIRECTION_NONE>], this method returns `Vector3(0, 0, 0)`.


----



[NodePath<class_NodePath>] **get_pole_node**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_TwoBoneIK3D_method_get_pole_node>]

Returns the pole target node that constructs a plane which the joints are all on and the pole is trying to direct.


----



[int<class_int>] **get_root_bone**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_TwoBoneIK3D_method_get_root_bone>]

Returns the root bone index.


----



[String<class_String>] **get_root_bone_name**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_TwoBoneIK3D_method_get_root_bone_name>]

Returns the root bone name.


----



[NodePath<class_NodePath>] **get_target_node**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_TwoBoneIK3D_method_get_target_node>]

Returns the target node that the end bone is trying to reach.


----



[bool<class_bool>] **is_end_bone_extended**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_TwoBoneIK3D_method_is_end_bone_extended>]

Returns `true` if the end bone is extended to have a tail.


----



[bool<class_bool>] **is_using_virtual_end**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_TwoBoneIK3D_method_is_using_virtual_end>]

Returns `true` if the end bone is extended from the middle bone as a virtual bone.


----



|void| **set_end_bone**\ (\ index\: [int<class_int>], bone\: [int<class_int>]\ ) [🔗<class_TwoBoneIK3D_method_set_end_bone>]

Sets the end bone index.


----



|void| **set_end_bone_direction**\ (\ index\: [int<class_int>], bone_direction\: [BoneDirection<enum_SkeletonModifier3D_BoneDirection>]\ ) [🔗<class_TwoBoneIK3D_method_set_end_bone_direction>]

Sets the end bone tail direction when [is_end_bone_extended()<class_TwoBoneIK3D_method_is_end_bone_extended>] is `true`.


----



|void| **set_end_bone_length**\ (\ index\: [int<class_int>], length\: [float<class_float>]\ ) [🔗<class_TwoBoneIK3D_method_set_end_bone_length>]

Sets the end bone tail length when [is_end_bone_extended()<class_TwoBoneIK3D_method_is_end_bone_extended>] is `true`.


----



|void| **set_end_bone_name**\ (\ index\: [int<class_int>], bone_name\: [String<class_String>]\ ) [🔗<class_TwoBoneIK3D_method_set_end_bone_name>]

Sets the end bone name.

\ **Note:** The end bone must be a child of the middle bone.


----



|void| **set_extend_end_bone**\ (\ index\: [int<class_int>], enabled\: [bool<class_bool>]\ ) [🔗<class_TwoBoneIK3D_method_set_extend_end_bone>]

If `enabled` is `true`, the end bone is extended to have a tail.


----



|void| **set_middle_bone**\ (\ index\: [int<class_int>], bone\: [int<class_int>]\ ) [🔗<class_TwoBoneIK3D_method_set_middle_bone>]

Sets the middle bone index.


----



|void| **set_middle_bone_name**\ (\ index\: [int<class_int>], bone_name\: [String<class_String>]\ ) [🔗<class_TwoBoneIK3D_method_set_middle_bone_name>]

Sets the middle bone name.

\ **Note:** The middle bone must be a child of the root bone.


----



|void| **set_pole_direction**\ (\ index\: [int<class_int>], direction\: [SecondaryDirection<enum_SkeletonModifier3D_SecondaryDirection>]\ ) [🔗<class_TwoBoneIK3D_method_set_pole_direction>]

Sets the pole direction.

The pole is on the middle bone and will direct to the pole target.

The rotation axis is a vector that is orthogonal to this and the forward vector.

\ **Note:** The pole direction and the forward vector shouldn't be colinear to avoid unintended rotation.


----



|void| **set_pole_direction_vector**\ (\ index\: [int<class_int>], vector\: [Vector3<class_Vector3>]\ ) [🔗<class_TwoBoneIK3D_method_set_pole_direction_vector>]

Sets the pole direction vector.

This vector is normalized by an internal process.

If the vector length is `0`, it is considered synonymous with [SkeletonModifier3D.SECONDARY_DIRECTION_NONE<class_SkeletonModifier3D_constant_SECONDARY_DIRECTION_NONE>].


----



|void| **set_pole_node**\ (\ index\: [int<class_int>], pole_node\: [NodePath<class_NodePath>]\ ) [🔗<class_TwoBoneIK3D_method_set_pole_node>]

Sets the pole target node that constructs a plane which the joints are all on and the pole is trying to direct.


----



|void| **set_root_bone**\ (\ index\: [int<class_int>], bone\: [int<class_int>]\ ) [🔗<class_TwoBoneIK3D_method_set_root_bone>]

Sets the root bone index.


----



|void| **set_root_bone_name**\ (\ index\: [int<class_int>], bone_name\: [String<class_String>]\ ) [🔗<class_TwoBoneIK3D_method_set_root_bone_name>]

Sets the root bone name.


----



|void| **set_target_node**\ (\ index\: [int<class_int>], target_node\: [NodePath<class_NodePath>]\ ) [🔗<class_TwoBoneIK3D_method_set_target_node>]

Sets the target node that the end bone is trying to reach.


----



|void| **set_use_virtual_end**\ (\ index\: [int<class_int>], enabled\: [bool<class_bool>]\ ) [🔗<class_TwoBoneIK3D_method_set_use_virtual_end>]

If `enabled` is `true`, the end bone is extended from the middle bone as a virtual bone.

