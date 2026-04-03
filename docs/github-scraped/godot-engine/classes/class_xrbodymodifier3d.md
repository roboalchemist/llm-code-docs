:github_url: hide



# XRBodyModifier3D

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [SkeletonModifier3D<class_SkeletonModifier3D>] **<** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A node for driving body meshes from [XRBodyTracker<class_XRBodyTracker>] data.


## Description

This node uses body tracking data from an [XRBodyTracker<class_XRBodyTracker>] to pose the skeleton of a body mesh.

Positioning of the body is performed by creating an [XRNode3D<class_XRNode3D>] ancestor of the body mesh driven by the same [XRBodyTracker<class_XRBodyTracker>].

The body tracking position-data is scaled by [Skeleton3D.motion_scale<class_Skeleton3D_property_motion_scale>] when applied to the skeleton, which can be used to adjust the tracked body to match the scale of the body model.


## Tutorials

- [../tutorials/xr/index](XR documentation index .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------------------------+-------------------------------------------------------------------+---------------------------+
> | :ref:`StringName<class_StringName>`                               | :ref:`body_tracker<class_XRBodyModifier3D_property_body_tracker>` | ``&"/user/body_tracker"`` |
> +-------------------------------------------------------------------+-------------------------------------------------------------------+---------------------------+
> | |bitfield|\[:ref:`BodyUpdate<enum_XRBodyModifier3D_BodyUpdate>`\] | :ref:`body_update<class_XRBodyModifier3D_property_body_update>`   | ``7``                     |
> +-------------------------------------------------------------------+-------------------------------------------------------------------+---------------------------+
> | :ref:`BoneUpdate<enum_XRBodyModifier3D_BoneUpdate>`               | :ref:`bone_update<class_XRBodyModifier3D_property_bone_update>`   | ``0``                     |
> +-------------------------------------------------------------------+-------------------------------------------------------------------+---------------------------+
>

----


## Enumerations



flags **BodyUpdate**: [🔗<enum_XRBodyModifier3D_BodyUpdate>]



[BodyUpdate<enum_XRBodyModifier3D_BodyUpdate>] **BODY_UPDATE_UPPER_BODY** = `1`

The skeleton's upper body joints are updated.



[BodyUpdate<enum_XRBodyModifier3D_BodyUpdate>] **BODY_UPDATE_LOWER_BODY** = `2`

The skeleton's lower body joints are updated.



[BodyUpdate<enum_XRBodyModifier3D_BodyUpdate>] **BODY_UPDATE_HANDS** = `4`

The skeleton's hand joints are updated.


----



enum **BoneUpdate**: [🔗<enum_XRBodyModifier3D_BoneUpdate>]



[BoneUpdate<enum_XRBodyModifier3D_BoneUpdate>] **BONE_UPDATE_FULL** = `0`

The skeleton's bones are fully updated (both position and rotation) to match the tracked bones.



[BoneUpdate<enum_XRBodyModifier3D_BoneUpdate>] **BONE_UPDATE_ROTATION_ONLY** = `1`

The skeleton's bones are only rotated to align with the tracked bones, preserving bone length.



[BoneUpdate<enum_XRBodyModifier3D_BoneUpdate>] **BONE_UPDATE_MAX** = `2`

Represents the size of the [BoneUpdate<enum_XRBodyModifier3D_BoneUpdate>] enum.


----


## Property Descriptions



[StringName<class_StringName>] **body_tracker** = `&"/user/body_tracker"` [🔗<class_XRBodyModifier3D_property_body_tracker>]


- |void| **set_body_tracker**\ (\ value\: [StringName<class_StringName>]\ )
- [StringName<class_StringName>] **get_body_tracker**\ (\ )

The name of the [XRBodyTracker<class_XRBodyTracker>] registered with [XRServer<class_XRServer>] to obtain the body tracking data from.


----



|bitfield|\[[BodyUpdate<enum_XRBodyModifier3D_BodyUpdate>]\] **body_update** = `7` [🔗<class_XRBodyModifier3D_property_body_update>]


- |void| **set_body_update**\ (\ value\: |bitfield|\[[BodyUpdate<enum_XRBodyModifier3D_BodyUpdate>]\]\ )
- |bitfield|\[[BodyUpdate<enum_XRBodyModifier3D_BodyUpdate>]\] **get_body_update**\ (\ )

Specifies the body parts to update.


----



[BoneUpdate<enum_XRBodyModifier3D_BoneUpdate>] **bone_update** = `0` [🔗<class_XRBodyModifier3D_property_bone_update>]


- |void| **set_bone_update**\ (\ value\: [BoneUpdate<enum_XRBodyModifier3D_BoneUpdate>]\ )
- [BoneUpdate<enum_XRBodyModifier3D_BoneUpdate>] **get_bone_update**\ (\ )

Specifies the type of updates to perform on the bones.

