:github_url: hide



# XRHandModifier3D

**Inherits:** [SkeletonModifier3D<class_SkeletonModifier3D>] **<** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A node for driving hand meshes from [XRHandTracker<class_XRHandTracker>] data.


## Description

This node uses hand tracking data from an [XRHandTracker<class_XRHandTracker>] to pose the skeleton of a hand mesh.

Positioning of hands is performed by creating an [XRNode3D<class_XRNode3D>] ancestor of the hand mesh driven by the same [XRHandTracker<class_XRHandTracker>].

The hand tracking position-data is scaled by [Skeleton3D.motion_scale<class_Skeleton3D_property_motion_scale>] when applied to the skeleton, which can be used to adjust the tracked hand to match the scale of the hand model.


## Tutorials

- [../tutorials/xr/index](XR documentation index .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------+-------------------------------------------------------------------+--------------------------------+
> | :ref:`BoneUpdate<enum_XRHandModifier3D_BoneUpdate>` | :ref:`bone_update<class_XRHandModifier3D_property_bone_update>`   | ``0``                          |
> +-----------------------------------------------------+-------------------------------------------------------------------+--------------------------------+
> | :ref:`StringName<class_StringName>`                 | :ref:`hand_tracker<class_XRHandModifier3D_property_hand_tracker>` | ``&"/user/hand_tracker/left"`` |
> +-----------------------------------------------------+-------------------------------------------------------------------+--------------------------------+
>

----


## Enumerations



enum **BoneUpdate**: [🔗<enum_XRHandModifier3D_BoneUpdate>]



[BoneUpdate<enum_XRHandModifier3D_BoneUpdate>] **BONE_UPDATE_FULL** = `0`

The skeleton's bones are fully updated (both position and rotation) to match the tracked bones.



[BoneUpdate<enum_XRHandModifier3D_BoneUpdate>] **BONE_UPDATE_ROTATION_ONLY** = `1`

The skeleton's bones are only rotated to align with the tracked bones, preserving bone length.



[BoneUpdate<enum_XRHandModifier3D_BoneUpdate>] **BONE_UPDATE_MAX** = `2`

Represents the size of the [BoneUpdate<enum_XRHandModifier3D_BoneUpdate>] enum.


----


## Property Descriptions



[BoneUpdate<enum_XRHandModifier3D_BoneUpdate>] **bone_update** = `0` [🔗<class_XRHandModifier3D_property_bone_update>]


- |void| **set_bone_update**\ (\ value\: [BoneUpdate<enum_XRHandModifier3D_BoneUpdate>]\ )
- [BoneUpdate<enum_XRHandModifier3D_BoneUpdate>] **get_bone_update**\ (\ )

Specifies the type of updates to perform on the bones.


----



[StringName<class_StringName>] **hand_tracker** = `&"/user/hand_tracker/left"` [🔗<class_XRHandModifier3D_property_hand_tracker>]


- |void| **set_hand_tracker**\ (\ value\: [StringName<class_StringName>]\ )
- [StringName<class_StringName>] **get_hand_tracker**\ (\ )

The name of the [XRHandTracker<class_XRHandTracker>] registered with [XRServer<class_XRServer>] to obtain the hand tracking data from.

