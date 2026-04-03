:github_url: hide



# ModifierBoneTarget3D

**Inherits:** [SkeletonModifier3D<class_SkeletonModifier3D>] **<** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

А node that dynamically copies the 3D transform of a bone in its parent [Skeleton3D<class_Skeleton3D>].


## Description

This node selects a bone in a [Skeleton3D<class_Skeleton3D>] and attaches to it. This means that the **ModifierBoneTarget3D** node will dynamically copy the 3D transform of the selected bone.

The functionality is similar to [BoneAttachment3D<class_BoneAttachment3D>], but this node adopts the [SkeletonModifier3D<class_SkeletonModifier3D>] cycle and is intended to be used as another [SkeletonModifier3D<class_SkeletonModifier3D>]'s target.


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------+-----------------------------------------------------------------+--------+
> | :ref:`int<class_int>`       | :ref:`bone<class_ModifierBoneTarget3D_property_bone>`           | ``-1`` |
> +-----------------------------+-----------------------------------------------------------------+--------+
> | :ref:`String<class_String>` | :ref:`bone_name<class_ModifierBoneTarget3D_property_bone_name>` | ``""`` |
> +-----------------------------+-----------------------------------------------------------------+--------+
>

----


## Property Descriptions



[int<class_int>] **bone** = `-1` [🔗<class_ModifierBoneTarget3D_property_bone>]


- |void| **set_bone**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_bone**\ (\ )

The index of the attached bone.


----



[String<class_String>] **bone_name** = `""` [🔗<class_ModifierBoneTarget3D_property_bone_name>]


- |void| **set_bone_name**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_bone_name**\ (\ )

The name of the attached bone.

