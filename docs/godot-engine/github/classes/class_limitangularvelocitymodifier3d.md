:github_url: hide



# LimitAngularVelocityModifier3D

**Inherits:** [SkeletonModifier3D<class_SkeletonModifier3D>] **<** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

Limit bone rotation angular velocity.


## Description

This modifier limits bone rotation angular velocity by comparing poses between previous and current frame.

You can add bone chains by specifying their root and end bones, then add the bones between them to a list. Modifier processes either that list or the bones excluding those in the list depending on the option [exclude<class_LimitAngularVelocityModifier3D_property_exclude>].


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+-------------------------------------------------------------------------------------------------+---------------+
> | :ref:`int<class_int>`     | :ref:`chain_count<class_LimitAngularVelocityModifier3D_property_chain_count>`                   | ``0``         |
> +---------------------------+-------------------------------------------------------------------------------------------------+---------------+
> | :ref:`bool<class_bool>`   | :ref:`exclude<class_LimitAngularVelocityModifier3D_property_exclude>`                           | ``false``     |
> +---------------------------+-------------------------------------------------------------------------------------------------+---------------+
> | :ref:`int<class_int>`     | :ref:`joint_count<class_LimitAngularVelocityModifier3D_property_joint_count>`                   | ``0``         |
> +---------------------------+-------------------------------------------------------------------------------------------------+---------------+
> | :ref:`float<class_float>` | :ref:`max_angular_velocity<class_LimitAngularVelocityModifier3D_property_max_angular_velocity>` | ``6.2831855`` |
> +---------------------------+-------------------------------------------------------------------------------------------------+---------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                      | :ref:`clear_chains<class_LimitAngularVelocityModifier3D_method_clear_chains>`\ (\ )                                                                                     |
> +-----------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`       | :ref:`get_end_bone<class_LimitAngularVelocityModifier3D_method_get_end_bone>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                              |
> +-----------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>` | :ref:`get_end_bone_name<class_LimitAngularVelocityModifier3D_method_get_end_bone_name>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                    |
> +-----------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`       | :ref:`get_root_bone<class_LimitAngularVelocityModifier3D_method_get_root_bone>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                            |
> +-----------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>` | :ref:`get_root_bone_name<class_LimitAngularVelocityModifier3D_method_get_root_bone_name>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                  |
> +-----------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                      | :ref:`reset<class_LimitAngularVelocityModifier3D_method_reset>`\ (\ )                                                                                                   |
> +-----------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                      | :ref:`set_end_bone<class_LimitAngularVelocityModifier3D_method_set_end_bone>`\ (\ index\: :ref:`int<class_int>`, bone\: :ref:`int<class_int>`\ )                        |
> +-----------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                      | :ref:`set_end_bone_name<class_LimitAngularVelocityModifier3D_method_set_end_bone_name>`\ (\ index\: :ref:`int<class_int>`, bone_name\: :ref:`String<class_String>`\ )   |
> +-----------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                      | :ref:`set_root_bone<class_LimitAngularVelocityModifier3D_method_set_root_bone>`\ (\ index\: :ref:`int<class_int>`, bone\: :ref:`int<class_int>`\ )                      |
> +-----------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                      | :ref:`set_root_bone_name<class_LimitAngularVelocityModifier3D_method_set_root_bone_name>`\ (\ index\: :ref:`int<class_int>`, bone_name\: :ref:`String<class_String>`\ ) |
> +-----------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[int<class_int>] **chain_count** = `0` [🔗<class_LimitAngularVelocityModifier3D_property_chain_count>]


- |void| **set_chain_count**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_chain_count**\ (\ )

The number of chains.


----



[bool<class_bool>] **exclude** = `false` [🔗<class_LimitAngularVelocityModifier3D_property_exclude>]


- |void| **set_exclude**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_exclude**\ (\ )

If `true`, the modifier processes bones not included in the bone list.

If `false`, the bones processed by the modifier are equal to the bone list.


----



[int<class_int>] **joint_count** = `0` [🔗<class_LimitAngularVelocityModifier3D_property_joint_count>]

The number of joints in the list which created by chains dynamically.


----



[float<class_float>] **max_angular_velocity** = `6.2831855` [🔗<class_LimitAngularVelocityModifier3D_property_max_angular_velocity>]


- |void| **set_max_angular_velocity**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_max_angular_velocity**\ (\ )

The maximum angular velocity per second.


----


## Method Descriptions



|void| **clear_chains**\ (\ ) [🔗<class_LimitAngularVelocityModifier3D_method_clear_chains>]

Clear all chains.


----



[int<class_int>] **get_end_bone**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_LimitAngularVelocityModifier3D_method_get_end_bone>]

Returns the end bone index of the bone chain.


----



[String<class_String>] **get_end_bone_name**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_LimitAngularVelocityModifier3D_method_get_end_bone_name>]

Returns the end bone name of the bone chain.


----



[int<class_int>] **get_root_bone**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_LimitAngularVelocityModifier3D_method_get_root_bone>]

Returns the root bone index of the bone chain.


----



[String<class_String>] **get_root_bone_name**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_LimitAngularVelocityModifier3D_method_get_root_bone_name>]

Returns the root bone name of the bone chain.


----



|void| **reset**\ (\ ) [🔗<class_LimitAngularVelocityModifier3D_method_reset>]

Sets the reference pose for angle comparison to the current pose with the influence of constraints removed. This function is automatically triggered when joints change or upon activation.


----



|void| **set_end_bone**\ (\ index\: [int<class_int>], bone\: [int<class_int>]\ ) [🔗<class_LimitAngularVelocityModifier3D_method_set_end_bone>]

Sets the end bone index of the bone chain.


----



|void| **set_end_bone_name**\ (\ index\: [int<class_int>], bone_name\: [String<class_String>]\ ) [🔗<class_LimitAngularVelocityModifier3D_method_set_end_bone_name>]

Sets the end bone name of the bone chain.

\ **Note:** End bone must be the root bone or a child of the root bone.


----



|void| **set_root_bone**\ (\ index\: [int<class_int>], bone\: [int<class_int>]\ ) [🔗<class_LimitAngularVelocityModifier3D_method_set_root_bone>]

Sets the root bone index of the bone chain.


----



|void| **set_root_bone_name**\ (\ index\: [int<class_int>], bone_name\: [String<class_String>]\ ) [🔗<class_LimitAngularVelocityModifier3D_method_set_root_bone_name>]

Sets the root bone name of the bone chain.

