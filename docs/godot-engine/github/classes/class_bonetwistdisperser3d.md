:github_url: hide



# BoneTwistDisperser3D

**Inherits:** [SkeletonModifier3D<class_SkeletonModifier3D>] **<** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A node that propagates and disperses the child bone's twist to the parent bones.


## Description

This **BoneTwistDisperser3D** allows for smooth twist interpolation between multiple bones by dispersing the end bone's twist to the parents. This only changes the twist without changing the global position of each joint.

This is useful for smoothly twisting bones in combination with [CopyTransformModifier3D<class_CopyTransformModifier3D>] and IK.

\ **Note:** If an extracted twist is greater than 180 degrees, flipping occurs. This is similar to [ConvertTransformModifier3D<class_ConvertTransformModifier3D>].


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------+---------------------------------------------------------------------------------+----------+
> | :ref:`bool<class_bool>` | :ref:`mutable_bone_axes<class_BoneTwistDisperser3D_property_mutable_bone_axes>` | ``true`` |
> +-------------------------+---------------------------------------------------------------------------------+----------+
> | :ref:`int<class_int>`   | :ref:`setting_count<class_BoneTwistDisperser3D_property_setting_count>`         | ``0``    |
> +-------------------------+---------------------------------------------------------------------------------+----------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                      | :ref:`clear_settings<class_BoneTwistDisperser3D_method_clear_settings>`\ (\ )                                                                                                                              |
> +-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Curve<class_Curve>`                                   | :ref:`get_damping_curve<class_BoneTwistDisperser3D_method_get_damping_curve>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                                                 |
> +-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`DisperseMode<enum_BoneTwistDisperser3D_DisperseMode>` | :ref:`get_disperse_mode<class_BoneTwistDisperser3D_method_get_disperse_mode>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                                                 |
> +-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                       | :ref:`get_end_bone<class_BoneTwistDisperser3D_method_get_end_bone>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                                                           |
> +-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`BoneDirection<enum_SkeletonModifier3D_BoneDirection>` | :ref:`get_end_bone_direction<class_BoneTwistDisperser3D_method_get_end_bone_direction>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                                       |
> +-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                                 | :ref:`get_end_bone_name<class_BoneTwistDisperser3D_method_get_end_bone_name>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                                                 |
> +-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                       | :ref:`get_joint_bone<class_BoneTwistDisperser3D_method_get_joint_bone>`\ (\ index\: :ref:`int<class_int>`, joint\: :ref:`int<class_int>`\ ) |const|                                                        |
> +-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                                 | :ref:`get_joint_bone_name<class_BoneTwistDisperser3D_method_get_joint_bone_name>`\ (\ index\: :ref:`int<class_int>`, joint\: :ref:`int<class_int>`\ ) |const|                                              |
> +-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                       | :ref:`get_joint_count<class_BoneTwistDisperser3D_method_get_joint_count>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                                                     |
> +-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                   | :ref:`get_joint_twist_amount<class_BoneTwistDisperser3D_method_get_joint_twist_amount>`\ (\ index\: :ref:`int<class_int>`, joint\: :ref:`int<class_int>`\ ) |const|                                        |
> +-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                       | :ref:`get_reference_bone<class_BoneTwistDisperser3D_method_get_reference_bone>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                                               |
> +-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                                 | :ref:`get_reference_bone_name<class_BoneTwistDisperser3D_method_get_reference_bone_name>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                                     |
> +-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                       | :ref:`get_root_bone<class_BoneTwistDisperser3D_method_get_root_bone>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                                                         |
> +-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                                 | :ref:`get_root_bone_name<class_BoneTwistDisperser3D_method_get_root_bone_name>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                                               |
> +-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Quaternion<class_Quaternion>`                         | :ref:`get_twist_from<class_BoneTwistDisperser3D_method_get_twist_from>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                                                       |
> +-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                   | :ref:`get_weight_position<class_BoneTwistDisperser3D_method_get_weight_position>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                                             |
> +-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                     | :ref:`is_end_bone_extended<class_BoneTwistDisperser3D_method_is_end_bone_extended>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                                           |
> +-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                     | :ref:`is_twist_from_rest<class_BoneTwistDisperser3D_method_is_twist_from_rest>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                                               |
> +-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                      | :ref:`set_damping_curve<class_BoneTwistDisperser3D_method_set_damping_curve>`\ (\ index\: :ref:`int<class_int>`, curve\: :ref:`Curve<class_Curve>`\ )                                                      |
> +-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                      | :ref:`set_disperse_mode<class_BoneTwistDisperser3D_method_set_disperse_mode>`\ (\ index\: :ref:`int<class_int>`, disperse_mode\: :ref:`DisperseMode<enum_BoneTwistDisperser3D_DisperseMode>`\ )            |
> +-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                      | :ref:`set_end_bone<class_BoneTwistDisperser3D_method_set_end_bone>`\ (\ index\: :ref:`int<class_int>`, bone\: :ref:`int<class_int>`\ )                                                                     |
> +-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                      | :ref:`set_end_bone_direction<class_BoneTwistDisperser3D_method_set_end_bone_direction>`\ (\ index\: :ref:`int<class_int>`, bone_direction\: :ref:`BoneDirection<enum_SkeletonModifier3D_BoneDirection>`\ ) |
> +-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                      | :ref:`set_end_bone_name<class_BoneTwistDisperser3D_method_set_end_bone_name>`\ (\ index\: :ref:`int<class_int>`, bone_name\: :ref:`String<class_String>`\ )                                                |
> +-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                      | :ref:`set_extend_end_bone<class_BoneTwistDisperser3D_method_set_extend_end_bone>`\ (\ index\: :ref:`int<class_int>`, enabled\: :ref:`bool<class_bool>`\ )                                                  |
> +-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                      | :ref:`set_joint_twist_amount<class_BoneTwistDisperser3D_method_set_joint_twist_amount>`\ (\ index\: :ref:`int<class_int>`, joint\: :ref:`int<class_int>`, twist_amount\: :ref:`float<class_float>`\ )      |
> +-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                      | :ref:`set_root_bone<class_BoneTwistDisperser3D_method_set_root_bone>`\ (\ index\: :ref:`int<class_int>`, bone\: :ref:`int<class_int>`\ )                                                                   |
> +-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                      | :ref:`set_root_bone_name<class_BoneTwistDisperser3D_method_set_root_bone_name>`\ (\ index\: :ref:`int<class_int>`, bone_name\: :ref:`String<class_String>`\ )                                              |
> +-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                      | :ref:`set_twist_from<class_BoneTwistDisperser3D_method_set_twist_from>`\ (\ index\: :ref:`int<class_int>`, from\: :ref:`Quaternion<class_Quaternion>`\ )                                                   |
> +-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                      | :ref:`set_twist_from_rest<class_BoneTwistDisperser3D_method_set_twist_from_rest>`\ (\ index\: :ref:`int<class_int>`, enabled\: :ref:`bool<class_bool>`\ )                                                  |
> +-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                      | :ref:`set_weight_position<class_BoneTwistDisperser3D_method_set_weight_position>`\ (\ index\: :ref:`int<class_int>`, weight_position\: :ref:`float<class_float>`\ )                                        |
> +-------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **DisperseMode**: [🔗<enum_BoneTwistDisperser3D_DisperseMode>]



[DisperseMode<enum_BoneTwistDisperser3D_DisperseMode>] **DISPERSE_MODE_EVEN** = `0`

Assign amounts so that they monotonically increase from `0.0` to `1.0`, ensuring all weights are equal. For example, with five joints, the amounts would be `0.2`, `0.4`, `0.6`, `0.8`, and `1.0` starting from the root bone.



[DisperseMode<enum_BoneTwistDisperser3D_DisperseMode>] **DISPERSE_MODE_WEIGHTED** = `1`

Assign amounts so that they monotonically increase from `0.0` to `1.0`, based on the length of the bones between joint segments. See also [set_weight_position()<class_BoneTwistDisperser3D_method_set_weight_position>].



[DisperseMode<enum_BoneTwistDisperser3D_DisperseMode>] **DISPERSE_MODE_CUSTOM** = `2`

You can assign arbitrary amounts to the joint list. See also [set_joint_twist_amount()<class_BoneTwistDisperser3D_method_set_joint_twist_amount>].

When [is_end_bone_extended()<class_BoneTwistDisperser3D_method_is_end_bone_extended>] is `false`, a child of the reference bone exists solely to determine the twist axis, so its custom amount has absolutely no effect at all.


----


## Property Descriptions



[bool<class_bool>] **mutable_bone_axes** = `true` [🔗<class_BoneTwistDisperser3D_property_mutable_bone_axes>]


- |void| **set_mutable_bone_axes**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **are_bone_axes_mutable**\ (\ )

If `true`, the solver retrieves the bone axis from the bone pose every frame.

If `false`, the solver retrieves the bone axis from the bone rest and caches it.


----



[int<class_int>] **setting_count** = `0` [🔗<class_BoneTwistDisperser3D_property_setting_count>]


- |void| **set_setting_count**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_setting_count**\ (\ )

The number of settings.


----


## Method Descriptions



|void| **clear_settings**\ (\ ) [🔗<class_BoneTwistDisperser3D_method_clear_settings>]

Clears all settings.


----



[Curve<class_Curve>] **get_damping_curve**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_BoneTwistDisperser3D_method_get_damping_curve>]

Returns the damping curve when [get_disperse_mode()<class_BoneTwistDisperser3D_method_get_disperse_mode>] is [DISPERSE_MODE_CUSTOM<class_BoneTwistDisperser3D_constant_DISPERSE_MODE_CUSTOM>].


----



[DisperseMode<enum_BoneTwistDisperser3D_DisperseMode>] **get_disperse_mode**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_BoneTwistDisperser3D_method_get_disperse_mode>]

Returns whether to use automatic amount assignment or to allow manual assignment.


----



[int<class_int>] **get_end_bone**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_BoneTwistDisperser3D_method_get_end_bone>]

Returns the end bone index of the bone chain.


----



[BoneDirection<enum_SkeletonModifier3D_BoneDirection>] **get_end_bone_direction**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_BoneTwistDisperser3D_method_get_end_bone_direction>]

Returns the tail direction of the end bone of the bone chain when [is_end_bone_extended()<class_BoneTwistDisperser3D_method_is_end_bone_extended>] is `true`.


----



[String<class_String>] **get_end_bone_name**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_BoneTwistDisperser3D_method_get_end_bone_name>]

Returns the end bone name of the bone chain.


----



[int<class_int>] **get_joint_bone**\ (\ index\: [int<class_int>], joint\: [int<class_int>]\ ) |const| [🔗<class_BoneTwistDisperser3D_method_get_joint_bone>]

Returns the bone index at `joint` in the bone chain's joint list.


----



[String<class_String>] **get_joint_bone_name**\ (\ index\: [int<class_int>], joint\: [int<class_int>]\ ) |const| [🔗<class_BoneTwistDisperser3D_method_get_joint_bone_name>]

Returns the bone name at `joint` in the bone chain's joint list.


----



[int<class_int>] **get_joint_count**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_BoneTwistDisperser3D_method_get_joint_count>]

Returns the joint count of the bone chain's joint list.


----



[float<class_float>] **get_joint_twist_amount**\ (\ index\: [int<class_int>], joint\: [int<class_int>]\ ) |const| [🔗<class_BoneTwistDisperser3D_method_get_joint_twist_amount>]

Returns the twist amount at `joint` in the bone chain's joint list when [get_disperse_mode()<class_BoneTwistDisperser3D_method_get_disperse_mode>] is [DISPERSE_MODE_CUSTOM<class_BoneTwistDisperser3D_constant_DISPERSE_MODE_CUSTOM>].


----



[int<class_int>] **get_reference_bone**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_BoneTwistDisperser3D_method_get_reference_bone>]

Returns the reference bone to extract twist of the setting at `index`.

This bone is either the end of the chain or its parent, depending on [is_end_bone_extended()<class_BoneTwistDisperser3D_method_is_end_bone_extended>].


----



[String<class_String>] **get_reference_bone_name**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_BoneTwistDisperser3D_method_get_reference_bone_name>]

Returns the reference bone name to extract twist of the setting at `index`.

This bone is either the end of the chain or its parent, depending on [is_end_bone_extended()<class_BoneTwistDisperser3D_method_is_end_bone_extended>].


----



[int<class_int>] **get_root_bone**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_BoneTwistDisperser3D_method_get_root_bone>]

Returns the root bone index of the bone chain.


----



[String<class_String>] **get_root_bone_name**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_BoneTwistDisperser3D_method_get_root_bone_name>]

Returns the root bone name of the bone chain.


----



[Quaternion<class_Quaternion>] **get_twist_from**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_BoneTwistDisperser3D_method_get_twist_from>]

Returns the rotation to an arbitrary state before twisting for the current bone pose to extract the twist when [is_twist_from_rest()<class_BoneTwistDisperser3D_method_is_twist_from_rest>] is `false`.


----



[float<class_float>] **get_weight_position**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_BoneTwistDisperser3D_method_get_weight_position>]

Returns the position at which to divide the segment between joints for weight assignment when [get_disperse_mode()<class_BoneTwistDisperser3D_method_get_disperse_mode>] is [DISPERSE_MODE_WEIGHTED<class_BoneTwistDisperser3D_constant_DISPERSE_MODE_WEIGHTED>].


----



[bool<class_bool>] **is_end_bone_extended**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_BoneTwistDisperser3D_method_is_end_bone_extended>]

Returns `true` if the end bone is extended to have a tail.


----



[bool<class_bool>] **is_twist_from_rest**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_BoneTwistDisperser3D_method_is_twist_from_rest>]

Returns `true` if extracting the twist amount from the difference between the bone rest and the current bone pose.


----



|void| **set_damping_curve**\ (\ index\: [int<class_int>], curve\: [Curve<class_Curve>]\ ) [🔗<class_BoneTwistDisperser3D_method_set_damping_curve>]

Sets the damping curve when [get_disperse_mode()<class_BoneTwistDisperser3D_method_get_disperse_mode>] is [DISPERSE_MODE_CUSTOM<class_BoneTwistDisperser3D_constant_DISPERSE_MODE_CUSTOM>].


----



|void| **set_disperse_mode**\ (\ index\: [int<class_int>], disperse_mode\: [DisperseMode<enum_BoneTwistDisperser3D_DisperseMode>]\ ) [🔗<class_BoneTwistDisperser3D_method_set_disperse_mode>]

Sets whether to use automatic amount assignment or to allow manual assignment.


----



|void| **set_end_bone**\ (\ index\: [int<class_int>], bone\: [int<class_int>]\ ) [🔗<class_BoneTwistDisperser3D_method_set_end_bone>]

Sets the end bone index of the bone chain.


----



|void| **set_end_bone_direction**\ (\ index\: [int<class_int>], bone_direction\: [BoneDirection<enum_SkeletonModifier3D_BoneDirection>]\ ) [🔗<class_BoneTwistDisperser3D_method_set_end_bone_direction>]

Sets the end bone tail direction of the bone chain when [is_end_bone_extended()<class_BoneTwistDisperser3D_method_is_end_bone_extended>] is `true`.


----



|void| **set_end_bone_name**\ (\ index\: [int<class_int>], bone_name\: [String<class_String>]\ ) [🔗<class_BoneTwistDisperser3D_method_set_end_bone_name>]

Sets the end bone name of the bone chain.

\ **Note:** The end bone must be a child of the root bone.


----



|void| **set_extend_end_bone**\ (\ index\: [int<class_int>], enabled\: [bool<class_bool>]\ ) [🔗<class_BoneTwistDisperser3D_method_set_extend_end_bone>]

If `enabled` is `true`, the end bone is extended to have a tail.

If `enabled` is `false`, [get_reference_bone()<class_BoneTwistDisperser3D_method_get_reference_bone>] becomes a parent of the end bone and it uses the vector to the end bone as a twist axis.


----



|void| **set_joint_twist_amount**\ (\ index\: [int<class_int>], joint\: [int<class_int>], twist_amount\: [float<class_float>]\ ) [🔗<class_BoneTwistDisperser3D_method_set_joint_twist_amount>]

Sets the twist amount at `joint` in the bone chain's joint list when [get_disperse_mode()<class_BoneTwistDisperser3D_method_get_disperse_mode>] is [DISPERSE_MODE_CUSTOM<class_BoneTwistDisperser3D_constant_DISPERSE_MODE_CUSTOM>].


----



|void| **set_root_bone**\ (\ index\: [int<class_int>], bone\: [int<class_int>]\ ) [🔗<class_BoneTwistDisperser3D_method_set_root_bone>]

Sets the root bone index of the bone chain.


----



|void| **set_root_bone_name**\ (\ index\: [int<class_int>], bone_name\: [String<class_String>]\ ) [🔗<class_BoneTwistDisperser3D_method_set_root_bone_name>]

Sets the root bone name of the bone chain.


----



|void| **set_twist_from**\ (\ index\: [int<class_int>], from\: [Quaternion<class_Quaternion>]\ ) [🔗<class_BoneTwistDisperser3D_method_set_twist_from>]

Sets the rotation to an arbitrary state before twisting for the current bone pose to extract the twist when [is_twist_from_rest()<class_BoneTwistDisperser3D_method_is_twist_from_rest>] is `false`.

In other words, by calling [set_twist_from()<class_BoneTwistDisperser3D_method_set_twist_from>] by [SkeletonModifier3D.modification_processed<class_SkeletonModifier3D_signal_modification_processed>] of a specific [SkeletonModifier3D<class_SkeletonModifier3D>], you can extract only the twists generated by modifiers processed after that but before this **BoneTwistDisperser3D**.


----



|void| **set_twist_from_rest**\ (\ index\: [int<class_int>], enabled\: [bool<class_bool>]\ ) [🔗<class_BoneTwistDisperser3D_method_set_twist_from_rest>]

If `enabled` is `true`, it extracts the twist amount from the difference between the bone rest and the current bone pose.

If `enabled` is `false`, it extracts the twist amount from the difference between [get_twist_from()<class_BoneTwistDisperser3D_method_get_twist_from>] and the current bone pose. See also [set_twist_from()<class_BoneTwistDisperser3D_method_set_twist_from>].


----



|void| **set_weight_position**\ (\ index\: [int<class_int>], weight_position\: [float<class_float>]\ ) [🔗<class_BoneTwistDisperser3D_method_set_weight_position>]

Sets the position at which to divide the segment between joints for weight assignment when [get_disperse_mode()<class_BoneTwistDisperser3D_method_get_disperse_mode>] is [DISPERSE_MODE_WEIGHTED<class_BoneTwistDisperser3D_constant_DISPERSE_MODE_WEIGHTED>].

For example, when `weight_position` is `0.5`, if two bone segments with a length of `1.0` exist between three joints, weights are assigned to each joint from root to end at ratios of `0.5`, `1.0`, and `0.5`. Then amounts become `0.25`, `0.75`, and `1.0` respectively.

