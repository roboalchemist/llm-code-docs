:github_url: hide



# PhysicsDirectBodyState3DExtension

**Inherits:** [PhysicsDirectBodyState3D<class_PhysicsDirectBodyState3D>] **<** [Object<class_Object>]

Provides virtual methods that can be overridden to create custom [PhysicsDirectBodyState3D<class_PhysicsDirectBodyState3D>] implementations.


## Description

This class extends [PhysicsDirectBodyState3D<class_PhysicsDirectBodyState3D>] by providing additional virtual methods that can be overridden. When these methods are overridden, they will be called instead of the internal methods of the physics server.

Intended for use with GDExtension to create custom implementations of [PhysicsDirectBodyState3D<class_PhysicsDirectBodyState3D>].


## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                            | :ref:`_add_constant_central_force<class_PhysicsDirectBodyState3DExtension_private_method__add_constant_central_force>`\ (\ force\: :ref:`Vector3<class_Vector3>`\ ) |virtual| |required|                                     |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                            | :ref:`_add_constant_force<class_PhysicsDirectBodyState3DExtension_private_method__add_constant_force>`\ (\ force\: :ref:`Vector3<class_Vector3>`, position\: :ref:`Vector3<class_Vector3>`\ ) |virtual| |required|           |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                            | :ref:`_add_constant_torque<class_PhysicsDirectBodyState3DExtension_private_method__add_constant_torque>`\ (\ torque\: :ref:`Vector3<class_Vector3>`\ ) |virtual| |required|                                                  |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                            | :ref:`_apply_central_force<class_PhysicsDirectBodyState3DExtension_private_method__apply_central_force>`\ (\ force\: :ref:`Vector3<class_Vector3>`\ ) |virtual| |required|                                                   |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                            | :ref:`_apply_central_impulse<class_PhysicsDirectBodyState3DExtension_private_method__apply_central_impulse>`\ (\ impulse\: :ref:`Vector3<class_Vector3>`\ ) |virtual| |required|                                             |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                            | :ref:`_apply_force<class_PhysicsDirectBodyState3DExtension_private_method__apply_force>`\ (\ force\: :ref:`Vector3<class_Vector3>`, position\: :ref:`Vector3<class_Vector3>`\ ) |virtual| |required|                         |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                            | :ref:`_apply_impulse<class_PhysicsDirectBodyState3DExtension_private_method__apply_impulse>`\ (\ impulse\: :ref:`Vector3<class_Vector3>`, position\: :ref:`Vector3<class_Vector3>`\ ) |virtual| |required|                   |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                            | :ref:`_apply_torque<class_PhysicsDirectBodyState3DExtension_private_method__apply_torque>`\ (\ torque\: :ref:`Vector3<class_Vector3>`\ ) |virtual| |required|                                                                |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                            | :ref:`_apply_torque_impulse<class_PhysicsDirectBodyState3DExtension_private_method__apply_torque_impulse>`\ (\ impulse\: :ref:`Vector3<class_Vector3>`\ ) |virtual| |required|                                               |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                                     | :ref:`_get_angular_velocity<class_PhysicsDirectBodyState3DExtension_private_method__get_angular_velocity>`\ (\ ) |virtual| |required| |const|                                                                                |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                                     | :ref:`_get_center_of_mass<class_PhysicsDirectBodyState3DExtension_private_method__get_center_of_mass>`\ (\ ) |virtual| |required| |const|                                                                                    |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                                     | :ref:`_get_center_of_mass_local<class_PhysicsDirectBodyState3DExtension_private_method__get_center_of_mass_local>`\ (\ ) |virtual| |required| |const|                                                                        |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                             | :ref:`_get_collision_layer<class_PhysicsDirectBodyState3DExtension_private_method__get_collision_layer>`\ (\ ) |virtual| |required| |const|                                                                                  |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                             | :ref:`_get_collision_mask<class_PhysicsDirectBodyState3DExtension_private_method__get_collision_mask>`\ (\ ) |virtual| |required| |const|                                                                                    |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                                     | :ref:`_get_constant_force<class_PhysicsDirectBodyState3DExtension_private_method__get_constant_force>`\ (\ ) |virtual| |required| |const|                                                                                    |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                                     | :ref:`_get_constant_torque<class_PhysicsDirectBodyState3DExtension_private_method__get_constant_torque>`\ (\ ) |virtual| |required| |const|                                                                                  |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`RID<class_RID>`                                             | :ref:`_get_contact_collider<class_PhysicsDirectBodyState3DExtension_private_method__get_contact_collider>`\ (\ contact_idx\: :ref:`int<class_int>`\ ) |virtual| |required| |const|                                           |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                             | :ref:`_get_contact_collider_id<class_PhysicsDirectBodyState3DExtension_private_method__get_contact_collider_id>`\ (\ contact_idx\: :ref:`int<class_int>`\ ) |virtual| |required| |const|                                     |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Object<class_Object>`                                       | :ref:`_get_contact_collider_object<class_PhysicsDirectBodyState3DExtension_private_method__get_contact_collider_object>`\ (\ contact_idx\: :ref:`int<class_int>`\ ) |virtual| |required| |const|                             |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                                     | :ref:`_get_contact_collider_position<class_PhysicsDirectBodyState3DExtension_private_method__get_contact_collider_position>`\ (\ contact_idx\: :ref:`int<class_int>`\ ) |virtual| |required| |const|                         |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                             | :ref:`_get_contact_collider_shape<class_PhysicsDirectBodyState3DExtension_private_method__get_contact_collider_shape>`\ (\ contact_idx\: :ref:`int<class_int>`\ ) |virtual| |required| |const|                               |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                                     | :ref:`_get_contact_collider_velocity_at_position<class_PhysicsDirectBodyState3DExtension_private_method__get_contact_collider_velocity_at_position>`\ (\ contact_idx\: :ref:`int<class_int>`\ ) |virtual| |required| |const| |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                             | :ref:`_get_contact_count<class_PhysicsDirectBodyState3DExtension_private_method__get_contact_count>`\ (\ ) |virtual| |required| |const|                                                                                      |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                                     | :ref:`_get_contact_impulse<class_PhysicsDirectBodyState3DExtension_private_method__get_contact_impulse>`\ (\ contact_idx\: :ref:`int<class_int>`\ ) |virtual| |required| |const|                                             |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                                     | :ref:`_get_contact_local_normal<class_PhysicsDirectBodyState3DExtension_private_method__get_contact_local_normal>`\ (\ contact_idx\: :ref:`int<class_int>`\ ) |virtual| |required| |const|                                   |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                                     | :ref:`_get_contact_local_position<class_PhysicsDirectBodyState3DExtension_private_method__get_contact_local_position>`\ (\ contact_idx\: :ref:`int<class_int>`\ ) |virtual| |required| |const|                               |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                             | :ref:`_get_contact_local_shape<class_PhysicsDirectBodyState3DExtension_private_method__get_contact_local_shape>`\ (\ contact_idx\: :ref:`int<class_int>`\ ) |virtual| |required| |const|                                     |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                                     | :ref:`_get_contact_local_velocity_at_position<class_PhysicsDirectBodyState3DExtension_private_method__get_contact_local_velocity_at_position>`\ (\ contact_idx\: :ref:`int<class_int>`\ ) |virtual| |required| |const|       |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                                     | :ref:`_get_inverse_inertia<class_PhysicsDirectBodyState3DExtension_private_method__get_inverse_inertia>`\ (\ ) |virtual| |required| |const|                                                                                  |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Basis<class_Basis>`                                         | :ref:`_get_inverse_inertia_tensor<class_PhysicsDirectBodyState3DExtension_private_method__get_inverse_inertia_tensor>`\ (\ ) |virtual| |required| |const|                                                                    |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                         | :ref:`_get_inverse_mass<class_PhysicsDirectBodyState3DExtension_private_method__get_inverse_mass>`\ (\ ) |virtual| |required| |const|                                                                                        |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                                     | :ref:`_get_linear_velocity<class_PhysicsDirectBodyState3DExtension_private_method__get_linear_velocity>`\ (\ ) |virtual| |required| |const|                                                                                  |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Basis<class_Basis>`                                         | :ref:`_get_principal_inertia_axes<class_PhysicsDirectBodyState3DExtension_private_method__get_principal_inertia_axes>`\ (\ ) |virtual| |required| |const|                                                                    |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PhysicsDirectSpaceState3D<class_PhysicsDirectSpaceState3D>` | :ref:`_get_space_state<class_PhysicsDirectBodyState3DExtension_private_method__get_space_state>`\ (\ ) |virtual| |required|                                                                                                  |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                         | :ref:`_get_step<class_PhysicsDirectBodyState3DExtension_private_method__get_step>`\ (\ ) |virtual| |required| |const|                                                                                                        |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                         | :ref:`_get_total_angular_damp<class_PhysicsDirectBodyState3DExtension_private_method__get_total_angular_damp>`\ (\ ) |virtual| |required| |const|                                                                            |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                                     | :ref:`_get_total_gravity<class_PhysicsDirectBodyState3DExtension_private_method__get_total_gravity>`\ (\ ) |virtual| |required| |const|                                                                                      |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                         | :ref:`_get_total_linear_damp<class_PhysicsDirectBodyState3DExtension_private_method__get_total_linear_damp>`\ (\ ) |virtual| |required| |const|                                                                              |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Transform3D<class_Transform3D>`                             | :ref:`_get_transform<class_PhysicsDirectBodyState3DExtension_private_method__get_transform>`\ (\ ) |virtual| |required| |const|                                                                                              |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                                     | :ref:`_get_velocity_at_local_position<class_PhysicsDirectBodyState3DExtension_private_method__get_velocity_at_local_position>`\ (\ local_position\: :ref:`Vector3<class_Vector3>`\ ) |virtual| |required| |const|            |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                            | :ref:`_integrate_forces<class_PhysicsDirectBodyState3DExtension_private_method__integrate_forces>`\ (\ ) |virtual| |required|                                                                                                |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                           | :ref:`_is_sleeping<class_PhysicsDirectBodyState3DExtension_private_method__is_sleeping>`\ (\ ) |virtual| |required| |const|                                                                                                  |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                            | :ref:`_set_angular_velocity<class_PhysicsDirectBodyState3DExtension_private_method__set_angular_velocity>`\ (\ velocity\: :ref:`Vector3<class_Vector3>`\ ) |virtual| |required|                                              |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                            | :ref:`_set_collision_layer<class_PhysicsDirectBodyState3DExtension_private_method__set_collision_layer>`\ (\ layer\: :ref:`int<class_int>`\ ) |virtual| |required|                                                           |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                            | :ref:`_set_collision_mask<class_PhysicsDirectBodyState3DExtension_private_method__set_collision_mask>`\ (\ mask\: :ref:`int<class_int>`\ ) |virtual| |required|                                                              |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                            | :ref:`_set_constant_force<class_PhysicsDirectBodyState3DExtension_private_method__set_constant_force>`\ (\ force\: :ref:`Vector3<class_Vector3>`\ ) |virtual| |required|                                                     |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                            | :ref:`_set_constant_torque<class_PhysicsDirectBodyState3DExtension_private_method__set_constant_torque>`\ (\ torque\: :ref:`Vector3<class_Vector3>`\ ) |virtual| |required|                                                  |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                            | :ref:`_set_linear_velocity<class_PhysicsDirectBodyState3DExtension_private_method__set_linear_velocity>`\ (\ velocity\: :ref:`Vector3<class_Vector3>`\ ) |virtual| |required|                                                |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                            | :ref:`_set_sleep_state<class_PhysicsDirectBodyState3DExtension_private_method__set_sleep_state>`\ (\ enabled\: :ref:`bool<class_bool>`\ ) |virtual| |required|                                                               |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                            | :ref:`_set_transform<class_PhysicsDirectBodyState3DExtension_private_method__set_transform>`\ (\ transform\: :ref:`Transform3D<class_Transform3D>`\ ) |virtual| |required|                                                   |
> +-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



|void| **_add_constant_central_force**\ (\ force\: [Vector3<class_Vector3>]\ ) |virtual| |required| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__add_constant_central_force>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



|void| **_add_constant_force**\ (\ force\: [Vector3<class_Vector3>], position\: [Vector3<class_Vector3>]\ ) |virtual| |required| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__add_constant_force>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



|void| **_add_constant_torque**\ (\ torque\: [Vector3<class_Vector3>]\ ) |virtual| |required| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__add_constant_torque>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



|void| **_apply_central_force**\ (\ force\: [Vector3<class_Vector3>]\ ) |virtual| |required| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__apply_central_force>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



|void| **_apply_central_impulse**\ (\ impulse\: [Vector3<class_Vector3>]\ ) |virtual| |required| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__apply_central_impulse>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



|void| **_apply_force**\ (\ force\: [Vector3<class_Vector3>], position\: [Vector3<class_Vector3>]\ ) |virtual| |required| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__apply_force>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



|void| **_apply_impulse**\ (\ impulse\: [Vector3<class_Vector3>], position\: [Vector3<class_Vector3>]\ ) |virtual| |required| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__apply_impulse>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



|void| **_apply_torque**\ (\ torque\: [Vector3<class_Vector3>]\ ) |virtual| |required| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__apply_torque>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



|void| **_apply_torque_impulse**\ (\ impulse\: [Vector3<class_Vector3>]\ ) |virtual| |required| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__apply_torque_impulse>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Vector3<class_Vector3>] **_get_angular_velocity**\ (\ ) |virtual| |required| |const| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__get_angular_velocity>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Vector3<class_Vector3>] **_get_center_of_mass**\ (\ ) |virtual| |required| |const| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__get_center_of_mass>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Vector3<class_Vector3>] **_get_center_of_mass_local**\ (\ ) |virtual| |required| |const| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__get_center_of_mass_local>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[int<class_int>] **_get_collision_layer**\ (\ ) |virtual| |required| |const| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__get_collision_layer>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[int<class_int>] **_get_collision_mask**\ (\ ) |virtual| |required| |const| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__get_collision_mask>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Vector3<class_Vector3>] **_get_constant_force**\ (\ ) |virtual| |required| |const| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__get_constant_force>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Vector3<class_Vector3>] **_get_constant_torque**\ (\ ) |virtual| |required| |const| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__get_constant_torque>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[RID<class_RID>] **_get_contact_collider**\ (\ contact_idx\: [int<class_int>]\ ) |virtual| |required| |const| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__get_contact_collider>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[int<class_int>] **_get_contact_collider_id**\ (\ contact_idx\: [int<class_int>]\ ) |virtual| |required| |const| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__get_contact_collider_id>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Object<class_Object>] **_get_contact_collider_object**\ (\ contact_idx\: [int<class_int>]\ ) |virtual| |required| |const| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__get_contact_collider_object>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Vector3<class_Vector3>] **_get_contact_collider_position**\ (\ contact_idx\: [int<class_int>]\ ) |virtual| |required| |const| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__get_contact_collider_position>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[int<class_int>] **_get_contact_collider_shape**\ (\ contact_idx\: [int<class_int>]\ ) |virtual| |required| |const| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__get_contact_collider_shape>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Vector3<class_Vector3>] **_get_contact_collider_velocity_at_position**\ (\ contact_idx\: [int<class_int>]\ ) |virtual| |required| |const| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__get_contact_collider_velocity_at_position>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[int<class_int>] **_get_contact_count**\ (\ ) |virtual| |required| |const| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__get_contact_count>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Vector3<class_Vector3>] **_get_contact_impulse**\ (\ contact_idx\: [int<class_int>]\ ) |virtual| |required| |const| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__get_contact_impulse>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Vector3<class_Vector3>] **_get_contact_local_normal**\ (\ contact_idx\: [int<class_int>]\ ) |virtual| |required| |const| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__get_contact_local_normal>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Vector3<class_Vector3>] **_get_contact_local_position**\ (\ contact_idx\: [int<class_int>]\ ) |virtual| |required| |const| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__get_contact_local_position>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[int<class_int>] **_get_contact_local_shape**\ (\ contact_idx\: [int<class_int>]\ ) |virtual| |required| |const| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__get_contact_local_shape>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Vector3<class_Vector3>] **_get_contact_local_velocity_at_position**\ (\ contact_idx\: [int<class_int>]\ ) |virtual| |required| |const| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__get_contact_local_velocity_at_position>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Vector3<class_Vector3>] **_get_inverse_inertia**\ (\ ) |virtual| |required| |const| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__get_inverse_inertia>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Basis<class_Basis>] **_get_inverse_inertia_tensor**\ (\ ) |virtual| |required| |const| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__get_inverse_inertia_tensor>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[float<class_float>] **_get_inverse_mass**\ (\ ) |virtual| |required| |const| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__get_inverse_mass>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Vector3<class_Vector3>] **_get_linear_velocity**\ (\ ) |virtual| |required| |const| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__get_linear_velocity>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Basis<class_Basis>] **_get_principal_inertia_axes**\ (\ ) |virtual| |required| |const| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__get_principal_inertia_axes>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[PhysicsDirectSpaceState3D<class_PhysicsDirectSpaceState3D>] **_get_space_state**\ (\ ) |virtual| |required| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__get_space_state>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[float<class_float>] **_get_step**\ (\ ) |virtual| |required| |const| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__get_step>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[float<class_float>] **_get_total_angular_damp**\ (\ ) |virtual| |required| |const| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__get_total_angular_damp>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Vector3<class_Vector3>] **_get_total_gravity**\ (\ ) |virtual| |required| |const| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__get_total_gravity>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[float<class_float>] **_get_total_linear_damp**\ (\ ) |virtual| |required| |const| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__get_total_linear_damp>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Transform3D<class_Transform3D>] **_get_transform**\ (\ ) |virtual| |required| |const| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__get_transform>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Vector3<class_Vector3>] **_get_velocity_at_local_position**\ (\ local_position\: [Vector3<class_Vector3>]\ ) |virtual| |required| |const| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__get_velocity_at_local_position>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



|void| **_integrate_forces**\ (\ ) |virtual| |required| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__integrate_forces>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[bool<class_bool>] **_is_sleeping**\ (\ ) |virtual| |required| |const| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__is_sleeping>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



|void| **_set_angular_velocity**\ (\ velocity\: [Vector3<class_Vector3>]\ ) |virtual| |required| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__set_angular_velocity>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



|void| **_set_collision_layer**\ (\ layer\: [int<class_int>]\ ) |virtual| |required| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__set_collision_layer>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



|void| **_set_collision_mask**\ (\ mask\: [int<class_int>]\ ) |virtual| |required| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__set_collision_mask>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



|void| **_set_constant_force**\ (\ force\: [Vector3<class_Vector3>]\ ) |virtual| |required| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__set_constant_force>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



|void| **_set_constant_torque**\ (\ torque\: [Vector3<class_Vector3>]\ ) |virtual| |required| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__set_constant_torque>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



|void| **_set_linear_velocity**\ (\ velocity\: [Vector3<class_Vector3>]\ ) |virtual| |required| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__set_linear_velocity>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



|void| **_set_sleep_state**\ (\ enabled\: [bool<class_bool>]\ ) |virtual| |required| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__set_sleep_state>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



|void| **_set_transform**\ (\ transform\: [Transform3D<class_Transform3D>]\ ) |virtual| |required| [🔗<class_PhysicsDirectBodyState3DExtension_private_method__set_transform>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!

