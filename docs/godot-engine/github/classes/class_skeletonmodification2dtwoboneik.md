:github_url: hide



# SkeletonModification2DTwoBoneIK

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [SkeletonModification2D<class_SkeletonModification2D>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A modification that rotates two bones using the law of cosines to reach the target.


## Description

This [SkeletonModification2D<class_SkeletonModification2D>] uses an algorithm typically called TwoBoneIK. This algorithm works by leveraging the law of cosines and the lengths of the bones to figure out what rotation the bones currently have, and what rotation they need to make a complete triangle, where the first bone, the second bone, and the target form the three vertices of the triangle. Because the algorithm works by making a triangle, it can only operate on two bones.

TwoBoneIK is great for arms, legs, and really any joints that can be represented by just two bones that bend to reach a target. This solver is more lightweight than [SkeletonModification2DFABRIK<class_SkeletonModification2DFABRIK>], but gives similar, natural looking results.


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------+--------------------------------------------------------------------------------------------------------+------------------+
> | :ref:`bool<class_bool>`         | :ref:`flip_bend_direction<class_SkeletonModification2DTwoBoneIK_property_flip_bend_direction>`         | ``false``        |
> +---------------------------------+--------------------------------------------------------------------------------------------------------+------------------+
> | :ref:`float<class_float>`       | :ref:`target_maximum_distance<class_SkeletonModification2DTwoBoneIK_property_target_maximum_distance>` | ``0.0``          |
> +---------------------------------+--------------------------------------------------------------------------------------------------------+------------------+
> | :ref:`float<class_float>`       | :ref:`target_minimum_distance<class_SkeletonModification2DTwoBoneIK_property_target_minimum_distance>` | ``0.0``          |
> +---------------------------------+--------------------------------------------------------------------------------------------------------+------------------+
> | :ref:`NodePath<class_NodePath>` | :ref:`target_nodepath<class_SkeletonModification2DTwoBoneIK_property_target_nodepath>`                 | ``NodePath("")`` |
> +---------------------------------+--------------------------------------------------------------------------------------------------------+------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`NodePath<class_NodePath>` | :ref:`get_joint_one_bone2d_node<class_SkeletonModification2DTwoBoneIK_method_get_joint_one_bone2d_node>`\ (\ ) |const|                                        |
> +---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`           | :ref:`get_joint_one_bone_idx<class_SkeletonModification2DTwoBoneIK_method_get_joint_one_bone_idx>`\ (\ ) |const|                                              |
> +---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`NodePath<class_NodePath>` | :ref:`get_joint_two_bone2d_node<class_SkeletonModification2DTwoBoneIK_method_get_joint_two_bone2d_node>`\ (\ ) |const|                                        |
> +---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`           | :ref:`get_joint_two_bone_idx<class_SkeletonModification2DTwoBoneIK_method_get_joint_two_bone_idx>`\ (\ ) |const|                                              |
> +---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                          | :ref:`set_joint_one_bone2d_node<class_SkeletonModification2DTwoBoneIK_method_set_joint_one_bone2d_node>`\ (\ bone2d_node\: :ref:`NodePath<class_NodePath>`\ ) |
> +---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                          | :ref:`set_joint_one_bone_idx<class_SkeletonModification2DTwoBoneIK_method_set_joint_one_bone_idx>`\ (\ bone_idx\: :ref:`int<class_int>`\ )                    |
> +---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                          | :ref:`set_joint_two_bone2d_node<class_SkeletonModification2DTwoBoneIK_method_set_joint_two_bone2d_node>`\ (\ bone2d_node\: :ref:`NodePath<class_NodePath>`\ ) |
> +---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                          | :ref:`set_joint_two_bone_idx<class_SkeletonModification2DTwoBoneIK_method_set_joint_two_bone_idx>`\ (\ bone_idx\: :ref:`int<class_int>`\ )                    |
> +---------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[bool<class_bool>] **flip_bend_direction** = `false` [🔗<class_SkeletonModification2DTwoBoneIK_property_flip_bend_direction>]


- |void| **set_flip_bend_direction**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_flip_bend_direction**\ (\ )

If `true`, the bones in the modification will bend outward as opposed to inwards when contracting. If `false`, the bones will bend inwards when contracting.


----



[float<class_float>] **target_maximum_distance** = `0.0` [🔗<class_SkeletonModification2DTwoBoneIK_property_target_maximum_distance>]


- |void| **set_target_maximum_distance**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_target_maximum_distance**\ (\ )

The maximum distance the target can be at. If the target is farther than this distance, the modification will solve as if it's at this maximum distance. When set to `0`, the modification will solve without distance constraints.


----



[float<class_float>] **target_minimum_distance** = `0.0` [🔗<class_SkeletonModification2DTwoBoneIK_property_target_minimum_distance>]


- |void| **set_target_minimum_distance**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_target_minimum_distance**\ (\ )

The minimum distance the target can be at. If the target is closer than this distance, the modification will solve as if it's at this minimum distance. When set to `0`, the modification will solve without distance constraints.


----



[NodePath<class_NodePath>] **target_nodepath** = `NodePath("")` [🔗<class_SkeletonModification2DTwoBoneIK_property_target_nodepath>]


- |void| **set_target_node**\ (\ value\: [NodePath<class_NodePath>]\ )
- [NodePath<class_NodePath>] **get_target_node**\ (\ )

The NodePath to the node that is the target for the TwoBoneIK modification. This node is what the modification will use when bending the [Bone2D<class_Bone2D>] nodes.


----


## Method Descriptions



[NodePath<class_NodePath>] **get_joint_one_bone2d_node**\ (\ ) |const| [🔗<class_SkeletonModification2DTwoBoneIK_method_get_joint_one_bone2d_node>]

Returns the [Bone2D<class_Bone2D>] node that is being used as the first bone in the TwoBoneIK modification.


----



[int<class_int>] **get_joint_one_bone_idx**\ (\ ) |const| [🔗<class_SkeletonModification2DTwoBoneIK_method_get_joint_one_bone_idx>]

Returns the index of the [Bone2D<class_Bone2D>] node that is being used as the first bone in the TwoBoneIK modification.


----



[NodePath<class_NodePath>] **get_joint_two_bone2d_node**\ (\ ) |const| [🔗<class_SkeletonModification2DTwoBoneIK_method_get_joint_two_bone2d_node>]

Returns the [Bone2D<class_Bone2D>] node that is being used as the second bone in the TwoBoneIK modification.


----



[int<class_int>] **get_joint_two_bone_idx**\ (\ ) |const| [🔗<class_SkeletonModification2DTwoBoneIK_method_get_joint_two_bone_idx>]

Returns the index of the [Bone2D<class_Bone2D>] node that is being used as the second bone in the TwoBoneIK modification.


----



|void| **set_joint_one_bone2d_node**\ (\ bone2d_node\: [NodePath<class_NodePath>]\ ) [🔗<class_SkeletonModification2DTwoBoneIK_method_set_joint_one_bone2d_node>]

Sets the [Bone2D<class_Bone2D>] node that is being used as the first bone in the TwoBoneIK modification.


----



|void| **set_joint_one_bone_idx**\ (\ bone_idx\: [int<class_int>]\ ) [🔗<class_SkeletonModification2DTwoBoneIK_method_set_joint_one_bone_idx>]

Sets the index of the [Bone2D<class_Bone2D>] node that is being used as the first bone in the TwoBoneIK modification.


----



|void| **set_joint_two_bone2d_node**\ (\ bone2d_node\: [NodePath<class_NodePath>]\ ) [🔗<class_SkeletonModification2DTwoBoneIK_method_set_joint_two_bone2d_node>]

Sets the [Bone2D<class_Bone2D>] node that is being used as the second bone in the TwoBoneIK modification.


----



|void| **set_joint_two_bone_idx**\ (\ bone_idx\: [int<class_int>]\ ) [🔗<class_SkeletonModification2DTwoBoneIK_method_set_joint_two_bone_idx>]

Sets the index of the [Bone2D<class_Bone2D>] node that is being used as the second bone in the TwoBoneIK modification.

