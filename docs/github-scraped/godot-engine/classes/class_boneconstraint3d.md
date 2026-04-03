:github_url: hide



# BoneConstraint3D

**Inherits:** [SkeletonModifier3D<class_SkeletonModifier3D>] **<** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

**Inherited By:** [AimModifier3D<class_AimModifier3D>], [ConvertTransformModifier3D<class_ConvertTransformModifier3D>], [CopyTransformModifier3D<class_CopyTransformModifier3D>]

A node that may modify Skeleton3D's bone with associating the two bones.


## Description

Base class of [SkeletonModifier3D<class_SkeletonModifier3D>] that modifies the bone set in [set_apply_bone()<class_BoneConstraint3D_method_set_apply_bone>] based on the transform of the bone retrieved by [get_reference_bone()<class_BoneConstraint3D_method_get_reference_bone>].


## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                    | :ref:`clear_setting<class_BoneConstraint3D_method_clear_setting>`\ (\ )                                                                                                            |
> +-----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                 | :ref:`get_amount<class_BoneConstraint3D_method_get_amount>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                                           |
> +-----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                     | :ref:`get_apply_bone<class_BoneConstraint3D_method_get_apply_bone>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                                   |
> +-----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                               | :ref:`get_apply_bone_name<class_BoneConstraint3D_method_get_apply_bone_name>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                         |
> +-----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                     | :ref:`get_reference_bone<class_BoneConstraint3D_method_get_reference_bone>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                           |
> +-----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                               | :ref:`get_reference_bone_name<class_BoneConstraint3D_method_get_reference_bone_name>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                 |
> +-----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`NodePath<class_NodePath>`                           | :ref:`get_reference_node<class_BoneConstraint3D_method_get_reference_node>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                           |
> +-----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`ReferenceType<enum_BoneConstraint3D_ReferenceType>` | :ref:`get_reference_type<class_BoneConstraint3D_method_get_reference_type>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                           |
> +-----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                     | :ref:`get_setting_count<class_BoneConstraint3D_method_get_setting_count>`\ (\ ) |const|                                                                                            |
> +-----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                    | :ref:`set_amount<class_BoneConstraint3D_method_set_amount>`\ (\ index\: :ref:`int<class_int>`, amount\: :ref:`float<class_float>`\ )                                               |
> +-----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                    | :ref:`set_apply_bone<class_BoneConstraint3D_method_set_apply_bone>`\ (\ index\: :ref:`int<class_int>`, bone\: :ref:`int<class_int>`\ )                                             |
> +-----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                    | :ref:`set_apply_bone_name<class_BoneConstraint3D_method_set_apply_bone_name>`\ (\ index\: :ref:`int<class_int>`, bone_name\: :ref:`String<class_String>`\ )                        |
> +-----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                    | :ref:`set_reference_bone<class_BoneConstraint3D_method_set_reference_bone>`\ (\ index\: :ref:`int<class_int>`, bone\: :ref:`int<class_int>`\ )                                     |
> +-----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                    | :ref:`set_reference_bone_name<class_BoneConstraint3D_method_set_reference_bone_name>`\ (\ index\: :ref:`int<class_int>`, bone_name\: :ref:`String<class_String>`\ )                |
> +-----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                    | :ref:`set_reference_node<class_BoneConstraint3D_method_set_reference_node>`\ (\ index\: :ref:`int<class_int>`, node\: :ref:`NodePath<class_NodePath>`\ )                           |
> +-----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                    | :ref:`set_reference_type<class_BoneConstraint3D_method_set_reference_type>`\ (\ index\: :ref:`int<class_int>`, type\: :ref:`ReferenceType<enum_BoneConstraint3D_ReferenceType>`\ ) |
> +-----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                    | :ref:`set_setting_count<class_BoneConstraint3D_method_set_setting_count>`\ (\ count\: :ref:`int<class_int>`\ )                                                                     |
> +-----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **ReferenceType**: [🔗<enum_BoneConstraint3D_ReferenceType>]



[ReferenceType<enum_BoneConstraint3D_ReferenceType>] **REFERENCE_TYPE_BONE** = `0`

The reference target is a bone. In this case, the reference target spaces is local space.



[ReferenceType<enum_BoneConstraint3D_ReferenceType>] **REFERENCE_TYPE_NODE** = `1`

The reference target is a [Node3D<class_Node3D>]. In this case, the reference target spaces is model space.

In other words, the reference target's coordinates are treated as if it were placed directly under [Skeleton3D<class_Skeleton3D>] which parent of the **BoneConstraint3D**.


----


## Method Descriptions



|void| **clear_setting**\ (\ ) [🔗<class_BoneConstraint3D_method_clear_setting>]

Clear all settings.


----



[float<class_float>] **get_amount**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_BoneConstraint3D_method_get_amount>]

Returns the apply amount of the setting at `index`.


----



[int<class_int>] **get_apply_bone**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_BoneConstraint3D_method_get_apply_bone>]

Returns the apply bone of the setting at `index`. This bone will be modified.


----



[String<class_String>] **get_apply_bone_name**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_BoneConstraint3D_method_get_apply_bone_name>]

Returns the apply bone name of the setting at `index`. This bone will be modified.


----



[int<class_int>] **get_reference_bone**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_BoneConstraint3D_method_get_reference_bone>]

Returns the reference bone of the setting at `index`.

This bone will be only referenced and not modified by this modifier.


----



[String<class_String>] **get_reference_bone_name**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_BoneConstraint3D_method_get_reference_bone_name>]

Returns the reference bone name of the setting at `index`.

This bone will be only referenced and not modified by this modifier.


----



[NodePath<class_NodePath>] **get_reference_node**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_BoneConstraint3D_method_get_reference_node>]

Returns the reference node path of the setting at `index`.

This node will be only referenced and not modified by this modifier.


----



[ReferenceType<enum_BoneConstraint3D_ReferenceType>] **get_reference_type**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_BoneConstraint3D_method_get_reference_type>]

Returns the reference target type of the setting at `index`. See also [ReferenceType<enum_BoneConstraint3D_ReferenceType>].


----



[int<class_int>] **get_setting_count**\ (\ ) |const| [🔗<class_BoneConstraint3D_method_get_setting_count>]

Returns the number of settings in the modifier.


----



|void| **set_amount**\ (\ index\: [int<class_int>], amount\: [float<class_float>]\ ) [🔗<class_BoneConstraint3D_method_set_amount>]

Sets the apply amount of the setting at `index` to `amount`.


----



|void| **set_apply_bone**\ (\ index\: [int<class_int>], bone\: [int<class_int>]\ ) [🔗<class_BoneConstraint3D_method_set_apply_bone>]

Sets the apply bone of the setting at `index` to `bone`. This bone will be modified.


----



|void| **set_apply_bone_name**\ (\ index\: [int<class_int>], bone_name\: [String<class_String>]\ ) [🔗<class_BoneConstraint3D_method_set_apply_bone_name>]

Sets the apply bone of the setting at `index` to `bone_name`. This bone will be modified.


----



|void| **set_reference_bone**\ (\ index\: [int<class_int>], bone\: [int<class_int>]\ ) [🔗<class_BoneConstraint3D_method_set_reference_bone>]

Sets the reference bone of the setting at `index` to `bone`.

This bone will be only referenced and not modified by this modifier.


----



|void| **set_reference_bone_name**\ (\ index\: [int<class_int>], bone_name\: [String<class_String>]\ ) [🔗<class_BoneConstraint3D_method_set_reference_bone_name>]

Sets the reference bone of the setting at `index` to `bone_name`.

This bone will be only referenced and not modified by this modifier.


----



|void| **set_reference_node**\ (\ index\: [int<class_int>], node\: [NodePath<class_NodePath>]\ ) [🔗<class_BoneConstraint3D_method_set_reference_node>]

Sets the reference node path of the setting at `index` to `node`.

This node will be only referenced and not modified by this modifier.


----



|void| **set_reference_type**\ (\ index\: [int<class_int>], type\: [ReferenceType<enum_BoneConstraint3D_ReferenceType>]\ ) [🔗<class_BoneConstraint3D_method_set_reference_type>]

Sets the reference target type of the setting at `index` to `type`. See also [ReferenceType<enum_BoneConstraint3D_ReferenceType>].


----



|void| **set_setting_count**\ (\ count\: [int<class_int>]\ ) [🔗<class_BoneConstraint3D_method_set_setting_count>]

Sets the number of settings in the modifier.

