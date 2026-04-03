# XRFaceModifier3D in English

# XRFaceModifier3D
Experimental:This class may be changed or removed in future versions.
Inherits:Node3D<Node<Object
A node for driving standard face meshes fromXRFaceTrackerweights.

## Description
This node applies weights from anXRFaceTrackerto a mesh with supporting face blend shapes.
TheUnified Expressionsblend shapes are supported, as well as ARKit and SRanipal blend shapes.
The node attempts to identify blend shapes based on name matching. Blend shapes should match the names listed in theUnified Expressions Compatibilitychart.

## Tutorials
- XR documentation index
XR documentation index

## Properties

| StringName | face_tracker | &"/user/face_tracker" |
|---|---|---|
| NodePath | target | NodePath("") |

StringName
face_tracker
&"/user/face_tracker"
NodePath
target
NodePath("")

## Property Descriptions
StringNameface_tracker=&"/user/face_tracker"🔗
- voidset_face_tracker(value:StringName)
voidset_face_tracker(value:StringName)
- StringNameget_face_tracker()
StringNameget_face_tracker()
TheXRFaceTrackerpath.
NodePathtarget=NodePath("")🔗
- voidset_target(value:NodePath)
voidset_target(value:NodePath)
- NodePathget_target()
NodePathget_target()
TheNodePathof the faceMeshInstance3D.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.