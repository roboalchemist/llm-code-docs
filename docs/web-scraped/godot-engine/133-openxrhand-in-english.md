# OpenXRHand in English

# OpenXRHand

Deprecated:UseXRHandModifier3Dinstead.
Inherits:Node3D<Node<Object
Node supporting hand and finger tracking in OpenXR.

## Description

This node enables OpenXR's hand tracking functionality. The node should be a child node of anXROrigin3Dnode, tracking will update its position to the player's tracked hand Palm joint location (the center of the middle finger's metacarpal bone). This node also updates the skeleton of a properly skinned hand or avatar model.
If the skeleton is a hand (one of the hand bones is the root node of the skeleton), then the skeleton will be placed relative to the hand palm location and the hand mesh and skeleton should be children of the OpenXRHand node.
If the hand bones are part of a full skeleton, then the root of the hand will keep its location with the assumption that IK is used to position the hand and arm.
By default the skeleton hand bones are repositioned to match the size of the tracked hand. To preserve the modeled bone sizes changebone_updateto apply rotation only.

## Properties

| BoneUpdate | bone_update | 0 |
|---|---|---|
| Hands | hand | 0 |
| NodePath | hand_skeleton | NodePath("") |
| MotionRange | motion_range | 0 |
| SkeletonRig | skeleton_rig | 0 |

BoneUpdate
bone_update
Hands
hand
NodePath
hand_skeleton
NodePath("")
MotionRange
motion_range
SkeletonRig
skeleton_rig

## Enumerations

enumHands:🔗
HandsHAND_LEFT=0
Tracking the player's left hand.
HandsHAND_RIGHT=1
Tracking the player's right hand.
HandsHAND_MAX=2
Maximum supported hands.
enumMotionRange:🔗
MotionRangeMOTION_RANGE_UNOBSTRUCTED=0
When player grips, hand skeleton will form a full fist.
MotionRangeMOTION_RANGE_CONFORM_TO_CONTROLLER=1
When player grips, hand skeleton conforms to the controller the player is holding.
MotionRangeMOTION_RANGE_MAX=2
Maximum supported motion ranges.
enumSkeletonRig:🔗
SkeletonRigSKELETON_RIG_OPENXR=0
An OpenXR compliant skeleton.
SkeletonRigSKELETON_RIG_HUMANOID=1
ASkeletonProfileHumanoidcompliant skeleton.
SkeletonRigSKELETON_RIG_MAX=2
Maximum supported hands.
enumBoneUpdate:🔗
BoneUpdateBONE_UPDATE_FULL=0
The skeletons bones are fully updated (both position and rotation) to match the tracked bones.
BoneUpdateBONE_UPDATE_ROTATION_ONLY=1
The skeletons bones are only rotated to align with the tracked bones, preserving bone length.
BoneUpdateBONE_UPDATE_MAX=2
Maximum supported bone update mode.

## Property Descriptions

BoneUpdatebone_update=0🔗

- voidset_bone_update(value:BoneUpdate)
voidset_bone_update(value:BoneUpdate)
- BoneUpdateget_bone_update()
BoneUpdateget_bone_update()
Specify the type of updates to perform on the bone.
Handshand=0🔗
- voidset_hand(value:Hands)
voidset_hand(value:Hands)
- Handsget_hand()
Handsget_hand()
Specifies whether this node tracks the left or right hand of the player.
NodePathhand_skeleton=NodePath("")🔗
- voidset_hand_skeleton(value:NodePath)
voidset_hand_skeleton(value:NodePath)
- NodePathget_hand_skeleton()
NodePathget_hand_skeleton()
Set aSkeleton3Dnode for which the pose positions will be updated.
MotionRangemotion_range=0🔗
- voidset_motion_range(value:MotionRange)
voidset_motion_range(value:MotionRange)
- MotionRangeget_motion_range()
MotionRangeget_motion_range()
Set the motion range (if supported) limiting the hand motion.
SkeletonRigskeleton_rig=0🔗
- voidset_skeleton_rig(value:SkeletonRig)
voidset_skeleton_rig(value:SkeletonRig)
- SkeletonRigget_skeleton_rig()
SkeletonRigget_skeleton_rig()
Set the type of skeleton rig thehand_skeletonis compliant with.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
