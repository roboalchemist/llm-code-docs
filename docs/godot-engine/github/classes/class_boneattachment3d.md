:github_url: hide

> **META**
	:keywords: tag



# BoneAttachment3D

**Inherits:** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

А node that dynamically copies or overrides the 3D transform of a bone in its parent [Skeleton3D<class_Skeleton3D>].


## Description

This node selects a bone in a [Skeleton3D<class_Skeleton3D>] and attaches to it. This means that the **BoneAttachment3D** node will either dynamically copy or override the 3D transform of the selected bone.


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------------------------+-------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                               | :ref:`bone_idx<class_BoneAttachment3D_property_bone_idx>`                           | ``-1``                                                                        |
> +---------------------------------------------------------------------+-------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                                         | :ref:`bone_name<class_BoneAttachment3D_property_bone_name>`                         | ``""``                                                                        |
> +---------------------------------------------------------------------+-------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
> | :ref:`NodePath<class_NodePath>`                                     | :ref:`external_skeleton<class_BoneAttachment3D_property_external_skeleton>`         |                                                                               |
> +---------------------------------------------------------------------+-------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                             | :ref:`override_pose<class_BoneAttachment3D_property_override_pose>`                 | ``false``                                                                     |
> +---------------------------------------------------------------------+-------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
> | :ref:`PhysicsInterpolationMode<enum_Node_PhysicsInterpolationMode>` | physics_interpolation_mode                                                          | ``2`` (overrides :ref:`Node<class_Node_property_physics_interpolation_mode>`) |
> +---------------------------------------------------------------------+-------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                             | :ref:`use_external_skeleton<class_BoneAttachment3D_property_use_external_skeleton>` | ``false``                                                                     |
> +---------------------------------------------------------------------+-------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------+-----------------------------------------------------------------------------------+
> | :ref:`Skeleton3D<class_Skeleton3D>` | :ref:`get_skeleton<class_BoneAttachment3D_method_get_skeleton>`\ (\ )             |
> +-------------------------------------+-----------------------------------------------------------------------------------+
> | |void|                              | :ref:`on_skeleton_update<class_BoneAttachment3D_method_on_skeleton_update>`\ (\ ) |
> +-------------------------------------+-----------------------------------------------------------------------------------+
>

----


## Property Descriptions



[int<class_int>] **bone_idx** = `-1` [🔗<class_BoneAttachment3D_property_bone_idx>]


- |void| **set_bone_idx**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_bone_idx**\ (\ )

The index of the attached bone.


----



[String<class_String>] **bone_name** = `""` [🔗<class_BoneAttachment3D_property_bone_name>]


- |void| **set_bone_name**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_bone_name**\ (\ )

The name of the attached bone.


----



[NodePath<class_NodePath>] **external_skeleton** [🔗<class_BoneAttachment3D_property_external_skeleton>]


- |void| **set_external_skeleton**\ (\ value\: [NodePath<class_NodePath>]\ )
- [NodePath<class_NodePath>] **get_external_skeleton**\ (\ )

The [NodePath<class_NodePath>] to the external [Skeleton3D<class_Skeleton3D>] node.


----



[bool<class_bool>] **override_pose** = `false` [🔗<class_BoneAttachment3D_property_override_pose>]


- |void| **set_override_pose**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_override_pose**\ (\ )

Whether the **BoneAttachment3D** node will override the bone pose of the bone it is attached to. When set to `true`, the **BoneAttachment3D** node can change the pose of the bone. When set to `false`, the **BoneAttachment3D** will always be set to the bone's transform.

\ **Note:** This override performs interruptively in the skeleton update process using signals due to the old design. It may cause unintended behavior when used at the same time with [SkeletonModifier3D<class_SkeletonModifier3D>].


----



[bool<class_bool>] **use_external_skeleton** = `false` [🔗<class_BoneAttachment3D_property_use_external_skeleton>]


- |void| **set_use_external_skeleton**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_use_external_skeleton**\ (\ )

Whether the **BoneAttachment3D** node will use an external [Skeleton3D<class_Skeleton3D>] node rather than attempting to use its parent node as the [Skeleton3D<class_Skeleton3D>]. When set to `true`, the **BoneAttachment3D** node will use the external [Skeleton3D<class_Skeleton3D>] node set in [external_skeleton<class_BoneAttachment3D_property_external_skeleton>].


----


## Method Descriptions



[Skeleton3D<class_Skeleton3D>] **get_skeleton**\ (\ ) [🔗<class_BoneAttachment3D_method_get_skeleton>]

Returns the parent or external [Skeleton3D<class_Skeleton3D>] node if it exists, otherwise returns `null`.


----



|void| **on_skeleton_update**\ (\ ) [🔗<class_BoneAttachment3D_method_on_skeleton_update>]

A function that is called automatically when the [Skeleton3D<class_Skeleton3D>] is updated. This function is where the **BoneAttachment3D** node updates its position so it is correctly bound when it is *not* set to override the bone pose.

