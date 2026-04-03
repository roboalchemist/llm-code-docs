:github_url: hide



# ChainIK3D

**Inherits:** [IKModifier3D<class_IKModifier3D>] **<** [SkeletonModifier3D<class_SkeletonModifier3D>] **<** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

**Inherited By:** [IterateIK3D<class_IterateIK3D>], [SplineIK3D<class_SplineIK3D>]

A [SkeletonModifier3D<class_SkeletonModifier3D>] to apply inverse kinematics to bone chains containing an arbitrary number of bones.


## Description

Base class of [SkeletonModifier3D<class_SkeletonModifier3D>] that automatically generates a joint list from the bones between the root bone and the end bone.


## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                       | :ref:`get_end_bone<class_ChainIK3D_method_get_end_bone>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                                                           |
> +-------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`BoneDirection<enum_SkeletonModifier3D_BoneDirection>` | :ref:`get_end_bone_direction<class_ChainIK3D_method_get_end_bone_direction>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                                       |
> +-------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                   | :ref:`get_end_bone_length<class_ChainIK3D_method_get_end_bone_length>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                                             |
> +-------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                                 | :ref:`get_end_bone_name<class_ChainIK3D_method_get_end_bone_name>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                                                 |
> +-------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                       | :ref:`get_joint_bone<class_ChainIK3D_method_get_joint_bone>`\ (\ index\: :ref:`int<class_int>`, joint\: :ref:`int<class_int>`\ ) |const|                                                        |
> +-------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                                 | :ref:`get_joint_bone_name<class_ChainIK3D_method_get_joint_bone_name>`\ (\ index\: :ref:`int<class_int>`, joint\: :ref:`int<class_int>`\ ) |const|                                              |
> +-------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                       | :ref:`get_joint_count<class_ChainIK3D_method_get_joint_count>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                                                     |
> +-------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                       | :ref:`get_root_bone<class_ChainIK3D_method_get_root_bone>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                                                         |
> +-------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                                 | :ref:`get_root_bone_name<class_ChainIK3D_method_get_root_bone_name>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                                               |
> +-------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                     | :ref:`is_end_bone_extended<class_ChainIK3D_method_is_end_bone_extended>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                                           |
> +-------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                      | :ref:`set_end_bone<class_ChainIK3D_method_set_end_bone>`\ (\ index\: :ref:`int<class_int>`, bone\: :ref:`int<class_int>`\ )                                                                     |
> +-------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                      | :ref:`set_end_bone_direction<class_ChainIK3D_method_set_end_bone_direction>`\ (\ index\: :ref:`int<class_int>`, bone_direction\: :ref:`BoneDirection<enum_SkeletonModifier3D_BoneDirection>`\ ) |
> +-------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                      | :ref:`set_end_bone_length<class_ChainIK3D_method_set_end_bone_length>`\ (\ index\: :ref:`int<class_int>`, length\: :ref:`float<class_float>`\ )                                                 |
> +-------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                      | :ref:`set_end_bone_name<class_ChainIK3D_method_set_end_bone_name>`\ (\ index\: :ref:`int<class_int>`, bone_name\: :ref:`String<class_String>`\ )                                                |
> +-------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                      | :ref:`set_extend_end_bone<class_ChainIK3D_method_set_extend_end_bone>`\ (\ index\: :ref:`int<class_int>`, enabled\: :ref:`bool<class_bool>`\ )                                                  |
> +-------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                      | :ref:`set_root_bone<class_ChainIK3D_method_set_root_bone>`\ (\ index\: :ref:`int<class_int>`, bone\: :ref:`int<class_int>`\ )                                                                   |
> +-------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                      | :ref:`set_root_bone_name<class_ChainIK3D_method_set_root_bone_name>`\ (\ index\: :ref:`int<class_int>`, bone_name\: :ref:`String<class_String>`\ )                                              |
> +-------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[int<class_int>] **get_end_bone**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_ChainIK3D_method_get_end_bone>]

Returns the end bone index of the bone chain.


----



[BoneDirection<enum_SkeletonModifier3D_BoneDirection>] **get_end_bone_direction**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_ChainIK3D_method_get_end_bone_direction>]

Returns the tail direction of the end bone of the bone chain when [is_end_bone_extended()<class_ChainIK3D_method_is_end_bone_extended>] is `true`.


----



[float<class_float>] **get_end_bone_length**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_ChainIK3D_method_get_end_bone_length>]

Returns the end bone tail length of the bone chain when [is_end_bone_extended()<class_ChainIK3D_method_is_end_bone_extended>] is `true`.


----



[String<class_String>] **get_end_bone_name**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_ChainIK3D_method_get_end_bone_name>]

Returns the end bone name of the bone chain.


----



[int<class_int>] **get_joint_bone**\ (\ index\: [int<class_int>], joint\: [int<class_int>]\ ) |const| [🔗<class_ChainIK3D_method_get_joint_bone>]

Returns the bone index at `joint` in the bone chain's joint list.


----



[String<class_String>] **get_joint_bone_name**\ (\ index\: [int<class_int>], joint\: [int<class_int>]\ ) |const| [🔗<class_ChainIK3D_method_get_joint_bone_name>]

Returns the bone name at `joint` in the bone chain's joint list.


----



[int<class_int>] **get_joint_count**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_ChainIK3D_method_get_joint_count>]

Returns the joint count of the bone chain's joint list.


----



[int<class_int>] **get_root_bone**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_ChainIK3D_method_get_root_bone>]

Returns the root bone index of the bone chain.


----



[String<class_String>] **get_root_bone_name**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_ChainIK3D_method_get_root_bone_name>]

Returns the root bone name of the bone chain.


----



[bool<class_bool>] **is_end_bone_extended**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_ChainIK3D_method_is_end_bone_extended>]

Returns `true` if the end bone is extended to have a tail.


----



|void| **set_end_bone**\ (\ index\: [int<class_int>], bone\: [int<class_int>]\ ) [🔗<class_ChainIK3D_method_set_end_bone>]

Sets the end bone index of the bone chain.


----



|void| **set_end_bone_direction**\ (\ index\: [int<class_int>], bone_direction\: [BoneDirection<enum_SkeletonModifier3D_BoneDirection>]\ ) [🔗<class_ChainIK3D_method_set_end_bone_direction>]

Sets the end bone tail direction of the bone chain when [is_end_bone_extended()<class_ChainIK3D_method_is_end_bone_extended>] is `true`.


----



|void| **set_end_bone_length**\ (\ index\: [int<class_int>], length\: [float<class_float>]\ ) [🔗<class_ChainIK3D_method_set_end_bone_length>]

Sets the end bone tail length of the bone chain when [is_end_bone_extended()<class_ChainIK3D_method_is_end_bone_extended>] is `true`.


----



|void| **set_end_bone_name**\ (\ index\: [int<class_int>], bone_name\: [String<class_String>]\ ) [🔗<class_ChainIK3D_method_set_end_bone_name>]

Sets the end bone name of the bone chain.

\ **Note:** The end bone must be the root bone or a child of the root bone. If they are the same, the tail must be extended by [set_extend_end_bone()<class_ChainIK3D_method_set_extend_end_bone>] to modify the bone.


----



|void| **set_extend_end_bone**\ (\ index\: [int<class_int>], enabled\: [bool<class_bool>]\ ) [🔗<class_ChainIK3D_method_set_extend_end_bone>]

If `enabled` is `true`, the end bone is extended to have a tail.

The extended tail config is allocated to the last element in the joint list. In other words, if you set `enabled` to `false`, the config of the last element in the joint list has no effect in the simulated result.


----



|void| **set_root_bone**\ (\ index\: [int<class_int>], bone\: [int<class_int>]\ ) [🔗<class_ChainIK3D_method_set_root_bone>]

Sets the root bone index of the bone chain.


----



|void| **set_root_bone_name**\ (\ index\: [int<class_int>], bone_name\: [String<class_String>]\ ) [🔗<class_ChainIK3D_method_set_root_bone_name>]

Sets the root bone name of the bone chain.

