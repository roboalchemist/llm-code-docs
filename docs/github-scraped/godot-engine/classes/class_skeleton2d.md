:github_url: hide



# Skeleton2D

**Inherits:** [Node2D<class_Node2D>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

The parent of a hierarchy of [Bone2D<class_Bone2D>]\ s, used to create a 2D skeletal animation.


## Description

**Skeleton2D** parents a hierarchy of [Bone2D<class_Bone2D>] nodes. It holds a reference to each [Bone2D<class_Bone2D>]'s rest pose and acts as a single point of access to its bones.

To set up different types of inverse kinematics for the given Skeleton2D, a [SkeletonModificationStack2D<class_SkeletonModificationStack2D>] should be created. The inverse kinematics be applied by increasing [SkeletonModificationStack2D.modification_count<class_SkeletonModificationStack2D_property_modification_count>] and creating the desired number of modifications.


## Tutorials

- [../tutorials/animation/2d_skeletons](2D skeletons .md)


## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                | :ref:`execute_modifications<class_Skeleton2D_method_execute_modifications>`\ (\ delta\: :ref:`float<class_float>`, execution_mode\: :ref:`int<class_int>`\ )                                                                                                         |
> +-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Bone2D<class_Bone2D>`                                           | :ref:`get_bone<class_Skeleton2D_method_get_bone>`\ (\ idx\: :ref:`int<class_int>`\ )                                                                                                                                                                                 |
> +-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                                 | :ref:`get_bone_count<class_Skeleton2D_method_get_bone_count>`\ (\ ) |const|                                                                                                                                                                                          |
> +-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Transform2D<class_Transform2D>`                                 | :ref:`get_bone_local_pose_override<class_Skeleton2D_method_get_bone_local_pose_override>`\ (\ bone_idx\: :ref:`int<class_int>`\ )                                                                                                                                    |
> +-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`SkeletonModificationStack2D<class_SkeletonModificationStack2D>` | :ref:`get_modification_stack<class_Skeleton2D_method_get_modification_stack>`\ (\ ) |const|                                                                                                                                                                          |
> +-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`RID<class_RID>`                                                 | :ref:`get_skeleton<class_Skeleton2D_method_get_skeleton>`\ (\ ) |const|                                                                                                                                                                                              |
> +-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                | :ref:`set_bone_local_pose_override<class_Skeleton2D_method_set_bone_local_pose_override>`\ (\ bone_idx\: :ref:`int<class_int>`, override_pose\: :ref:`Transform2D<class_Transform2D>`, strength\: :ref:`float<class_float>`, persistent\: :ref:`bool<class_bool>`\ ) |
> +-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                | :ref:`set_modification_stack<class_Skeleton2D_method_set_modification_stack>`\ (\ modification_stack\: :ref:`SkeletonModificationStack2D<class_SkeletonModificationStack2D>`\ )                                                                                      |
> +-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**bone_setup_changed**\ (\ ) [🔗<class_Skeleton2D_signal_bone_setup_changed>]

Emitted when the [Bone2D<class_Bone2D>] setup attached to this skeletons changes. This is primarily used internally within the skeleton.


----


## Method Descriptions



|void| **execute_modifications**\ (\ delta\: [float<class_float>], execution_mode\: [int<class_int>]\ ) [🔗<class_Skeleton2D_method_execute_modifications>]

Executes all the modifications on the [SkeletonModificationStack2D<class_SkeletonModificationStack2D>], if the Skeleton2D has one assigned.


----



[Bone2D<class_Bone2D>] **get_bone**\ (\ idx\: [int<class_int>]\ ) [🔗<class_Skeleton2D_method_get_bone>]

Returns a [Bone2D<class_Bone2D>] from the node hierarchy parented by Skeleton2D. The object to return is identified by the parameter `idx`. Bones are indexed by descending the node hierarchy from top to bottom, adding the children of each branch before moving to the next sibling.


----



[int<class_int>] **get_bone_count**\ (\ ) |const| [🔗<class_Skeleton2D_method_get_bone_count>]

Returns the number of [Bone2D<class_Bone2D>] nodes in the node hierarchy parented by Skeleton2D.


----



[Transform2D<class_Transform2D>] **get_bone_local_pose_override**\ (\ bone_idx\: [int<class_int>]\ ) [🔗<class_Skeleton2D_method_get_bone_local_pose_override>]

Returns the local pose override transform for `bone_idx`.


----



[SkeletonModificationStack2D<class_SkeletonModificationStack2D>] **get_modification_stack**\ (\ ) |const| [🔗<class_Skeleton2D_method_get_modification_stack>]

Returns the [SkeletonModificationStack2D<class_SkeletonModificationStack2D>] attached to this skeleton, if one exists.


----



[RID<class_RID>] **get_skeleton**\ (\ ) |const| [🔗<class_Skeleton2D_method_get_skeleton>]

Returns the [RID<class_RID>] of a Skeleton2D instance.


----



|void| **set_bone_local_pose_override**\ (\ bone_idx\: [int<class_int>], override_pose\: [Transform2D<class_Transform2D>], strength\: [float<class_float>], persistent\: [bool<class_bool>]\ ) [🔗<class_Skeleton2D_method_set_bone_local_pose_override>]

Sets the local pose transform, `override_pose`, for the bone at `bone_idx`.

\ `strength` is the interpolation strength that will be used when applying the pose, and `persistent` determines if the applied pose will remain.

\ **Note:** The pose transform needs to be a local transform relative to the [Bone2D<class_Bone2D>] node at `bone_idx`!


----



|void| **set_modification_stack**\ (\ modification_stack\: [SkeletonModificationStack2D<class_SkeletonModificationStack2D>]\ ) [🔗<class_Skeleton2D_method_set_modification_stack>]

Sets the [SkeletonModificationStack2D<class_SkeletonModificationStack2D>] attached to this skeleton.

