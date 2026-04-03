# XRHandModifier3D

# XRHandModifier3D
Inherits:SkeletonModifier3D<Node3D<Node<Object
A node for driving hand meshes fromXRHandTrackerdata.

## Description
This node uses hand tracking data from anXRHandTrackerto pose the skeleton of a hand mesh.
Positioning of hands is performed by creating anXRNode3Dancestor of the hand mesh driven by the sameXRHandTracker.
The hand tracking position-data is scaled bySkeleton3D.motion_scalewhen applied to the skeleton, which can be used to adjust the tracked hand to match the scale of the hand model.

## Tutorials
- XR documentation index
XR documentation index

## Properties

| BoneUpdate | bone_update | 0 |
|---|---|---|
| StringName | hand_tracker | &"/user/hand_tracker/left" |

BoneUpdate
bone_update
StringName
hand_tracker
&"/user/hand_tracker/left"

## Enumerations
enumBoneUpdate:🔗
BoneUpdateBONE_UPDATE_FULL=0
The skeleton's bones are fully updated (both position and rotation) to match the tracked bones.
BoneUpdateBONE_UPDATE_ROTATION_ONLY=1
The skeleton's bones are only rotated to align with the tracked bones, preserving bone length.
BoneUpdateBONE_UPDATE_MAX=2
Represents the size of theBoneUpdateenum.

## Property Descriptions
BoneUpdatebone_update=0🔗
- voidset_bone_update(value:BoneUpdate)
voidset_bone_update(value:BoneUpdate)
- BoneUpdateget_bone_update()
BoneUpdateget_bone_update()
Specifies the type of updates to perform on the bones.
StringNamehand_tracker=&"/user/hand_tracker/left"🔗
- voidset_hand_tracker(value:StringName)
voidset_hand_tracker(value:StringName)
- StringNameget_hand_tracker()
StringNameget_hand_tracker()
The name of theXRHandTrackerregistered withXRServerto obtain the hand tracking data from.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.