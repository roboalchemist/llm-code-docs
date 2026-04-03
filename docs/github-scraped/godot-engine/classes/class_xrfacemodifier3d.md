:github_url: hide



# XRFaceModifier3D

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A node for driving standard face meshes from [XRFaceTracker<class_XRFaceTracker>] weights.


## Description

This node applies weights from an [XRFaceTracker<class_XRFaceTracker>] to a mesh with supporting face blend shapes.

The [Unified Expressions ](https://docs.vrcft.io/docs/tutorial-avatars/tutorial-avatars-extras/unified-blendshapes)_ blend shapes are supported, as well as ARKit and SRanipal blend shapes.

The node attempts to identify blend shapes based on name matching. Blend shapes should match the names listed in the [Unified Expressions Compatibility ](https://docs.vrcft.io/docs/tutorial-avatars/tutorial-avatars-extras/compatibility/overview)_ chart.


## Tutorials

- [../tutorials/xr/index](XR documentation index .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------------+-------------------------------------------------------------------+---------------------------+
> | :ref:`StringName<class_StringName>` | :ref:`face_tracker<class_XRFaceModifier3D_property_face_tracker>` | ``&"/user/face_tracker"`` |
> +-------------------------------------+-------------------------------------------------------------------+---------------------------+
> | :ref:`NodePath<class_NodePath>`     | :ref:`target<class_XRFaceModifier3D_property_target>`             | ``NodePath("")``          |
> +-------------------------------------+-------------------------------------------------------------------+---------------------------+
>

----


## Property Descriptions



[StringName<class_StringName>] **face_tracker** = `&"/user/face_tracker"` [🔗<class_XRFaceModifier3D_property_face_tracker>]


- |void| **set_face_tracker**\ (\ value\: [StringName<class_StringName>]\ )
- [StringName<class_StringName>] **get_face_tracker**\ (\ )

The [XRFaceTracker<class_XRFaceTracker>] path.


----



[NodePath<class_NodePath>] **target** = `NodePath("")` [🔗<class_XRFaceModifier3D_property_target>]


- |void| **set_target**\ (\ value\: [NodePath<class_NodePath>]\ )
- [NodePath<class_NodePath>] **get_target**\ (\ )

The [NodePath<class_NodePath>] of the face [MeshInstance3D<class_MeshInstance3D>].

