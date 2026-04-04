:github_url: hide



# OpenXRHand

**Deprecated:** Use [XRHandModifier3D<class_XRHandModifier3D>] instead.

**Inherits:** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

Node supporting hand and finger tracking in OpenXR.


## Description

This node enables OpenXR's hand tracking functionality. The node should be a child node of an [XROrigin3D<class_XROrigin3D>] node, tracking will update its position to the player's tracked hand Palm joint location (the center of the middle finger's metacarpal bone). This node also updates the skeleton of a properly skinned hand or avatar model.

If the skeleton is a hand (one of the hand bones is the root node of the skeleton), then the skeleton will be placed relative to the hand palm location and the hand mesh and skeleton should be children of the OpenXRHand node.

If the hand bones are part of a full skeleton, then the root of the hand will keep its location with the assumption that IK is used to position the hand and arm.

By default the skeleton hand bones are repositioned to match the size of the tracked hand. To preserve the modeled bone sizes change [bone_update<class_OpenXRHand_property_bone_update>] to apply rotation only.


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------+---------------------------------------------------------------+------------------+
> | :ref:`BoneUpdate<enum_OpenXRHand_BoneUpdate>`   | :ref:`bone_update<class_OpenXRHand_property_bone_update>`     | ``0``            |
> +-------------------------------------------------+---------------------------------------------------------------+------------------+
> | :ref:`Hands<enum_OpenXRHand_Hands>`             | :ref:`hand<class_OpenXRHand_property_hand>`                   | ``0``            |
> +-------------------------------------------------+---------------------------------------------------------------+------------------+
> | :ref:`NodePath<class_NodePath>`                 | :ref:`hand_skeleton<class_OpenXRHand_property_hand_skeleton>` | ``NodePath("")`` |
> +-------------------------------------------------+---------------------------------------------------------------+------------------+
> | :ref:`MotionRange<enum_OpenXRHand_MotionRange>` | :ref:`motion_range<class_OpenXRHand_property_motion_range>`   | ``0``            |
> +-------------------------------------------------+---------------------------------------------------------------+------------------+
> | :ref:`SkeletonRig<enum_OpenXRHand_SkeletonRig>` | :ref:`skeleton_rig<class_OpenXRHand_property_skeleton_rig>`   | ``0``            |
> +-------------------------------------------------+---------------------------------------------------------------+------------------+
>

----


## Enumerations



enum **Hands**: [🔗<enum_OpenXRHand_Hands>]



[Hands<enum_OpenXRHand_Hands>] **HAND_LEFT** = `0`

Tracking the player's left hand.



[Hands<enum_OpenXRHand_Hands>] **HAND_RIGHT** = `1`

Tracking the player's right hand.



[Hands<enum_OpenXRHand_Hands>] **HAND_MAX** = `2`

Maximum supported hands.


----



enum **MotionRange**: [🔗<enum_OpenXRHand_MotionRange>]



[MotionRange<enum_OpenXRHand_MotionRange>] **MOTION_RANGE_UNOBSTRUCTED** = `0`

When player grips, hand skeleton will form a full fist.



[MotionRange<enum_OpenXRHand_MotionRange>] **MOTION_RANGE_CONFORM_TO_CONTROLLER** = `1`

When player grips, hand skeleton conforms to the controller the player is holding.



[MotionRange<enum_OpenXRHand_MotionRange>] **MOTION_RANGE_MAX** = `2`

Maximum supported motion ranges.


----



enum **SkeletonRig**: [🔗<enum_OpenXRHand_SkeletonRig>]



[SkeletonRig<enum_OpenXRHand_SkeletonRig>] **SKELETON_RIG_OPENXR** = `0`

An OpenXR compliant skeleton.



[SkeletonRig<enum_OpenXRHand_SkeletonRig>] **SKELETON_RIG_HUMANOID** = `1`

A [SkeletonProfileHumanoid<class_SkeletonProfileHumanoid>] compliant skeleton.



[SkeletonRig<enum_OpenXRHand_SkeletonRig>] **SKELETON_RIG_MAX** = `2`

Maximum supported hands.


----



enum **BoneUpdate**: [🔗<enum_OpenXRHand_BoneUpdate>]



[BoneUpdate<enum_OpenXRHand_BoneUpdate>] **BONE_UPDATE_FULL** = `0`

The skeletons bones are fully updated (both position and rotation) to match the tracked bones.



[BoneUpdate<enum_OpenXRHand_BoneUpdate>] **BONE_UPDATE_ROTATION_ONLY** = `1`

The skeletons bones are only rotated to align with the tracked bones, preserving bone length.



[BoneUpdate<enum_OpenXRHand_BoneUpdate>] **BONE_UPDATE_MAX** = `2`

Maximum supported bone update mode.


----


## Property Descriptions



[BoneUpdate<enum_OpenXRHand_BoneUpdate>] **bone_update** = `0` [🔗<class_OpenXRHand_property_bone_update>]


- |void| **set_bone_update**\ (\ value\: [BoneUpdate<enum_OpenXRHand_BoneUpdate>]\ )
- [BoneUpdate<enum_OpenXRHand_BoneUpdate>] **get_bone_update**\ (\ )

Specify the type of updates to perform on the bone.


----



[Hands<enum_OpenXRHand_Hands>] **hand** = `0` [🔗<class_OpenXRHand_property_hand>]


- |void| **set_hand**\ (\ value\: [Hands<enum_OpenXRHand_Hands>]\ )
- [Hands<enum_OpenXRHand_Hands>] **get_hand**\ (\ )

Specifies whether this node tracks the left or right hand of the player.


----



[NodePath<class_NodePath>] **hand_skeleton** = `NodePath("")` [🔗<class_OpenXRHand_property_hand_skeleton>]


- |void| **set_hand_skeleton**\ (\ value\: [NodePath<class_NodePath>]\ )
- [NodePath<class_NodePath>] **get_hand_skeleton**\ (\ )

Set a [Skeleton3D<class_Skeleton3D>] node for which the pose positions will be updated.


----



[MotionRange<enum_OpenXRHand_MotionRange>] **motion_range** = `0` [🔗<class_OpenXRHand_property_motion_range>]


- |void| **set_motion_range**\ (\ value\: [MotionRange<enum_OpenXRHand_MotionRange>]\ )
- [MotionRange<enum_OpenXRHand_MotionRange>] **get_motion_range**\ (\ )

Set the motion range (if supported) limiting the hand motion.


----



[SkeletonRig<enum_OpenXRHand_SkeletonRig>] **skeleton_rig** = `0` [🔗<class_OpenXRHand_property_skeleton_rig>]


- |void| **set_skeleton_rig**\ (\ value\: [SkeletonRig<enum_OpenXRHand_SkeletonRig>]\ )
- [SkeletonRig<enum_OpenXRHand_SkeletonRig>] **get_skeleton_rig**\ (\ )

Set the type of skeleton rig the [hand_skeleton<class_OpenXRHand_property_hand_skeleton>] is compliant with.

