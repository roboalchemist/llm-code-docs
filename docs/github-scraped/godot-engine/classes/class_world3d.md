:github_url: hide



# World3D

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A resource that holds all components of a 3D world, such as a visual scenario and a physics space.


## Description

Class that has everything pertaining to a world: A physics space, a visual scenario, and a sound space. 3D nodes register their resources into the current 3D world.


## Tutorials

- [../tutorials/physics/ray-casting](Ray-casting .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------------------------+--------------------------------------------------------------------------+
> | :ref:`CameraAttributes<class_CameraAttributes>`                   | :ref:`camera_attributes<class_World3D_property_camera_attributes>`       |
> +-------------------------------------------------------------------+--------------------------------------------------------------------------+
> | :ref:`PhysicsDirectSpaceState3D<class_PhysicsDirectSpaceState3D>` | :ref:`direct_space_state<class_World3D_property_direct_space_state>`     |
> +-------------------------------------------------------------------+--------------------------------------------------------------------------+
> | :ref:`Environment<class_Environment>`                             | :ref:`environment<class_World3D_property_environment>`                   |
> +-------------------------------------------------------------------+--------------------------------------------------------------------------+
> | :ref:`Environment<class_Environment>`                             | :ref:`fallback_environment<class_World3D_property_fallback_environment>` |
> +-------------------------------------------------------------------+--------------------------------------------------------------------------+
> | :ref:`RID<class_RID>`                                             | :ref:`navigation_map<class_World3D_property_navigation_map>`             |
> +-------------------------------------------------------------------+--------------------------------------------------------------------------+
> | :ref:`RID<class_RID>`                                             | :ref:`scenario<class_World3D_property_scenario>`                         |
> +-------------------------------------------------------------------+--------------------------------------------------------------------------+
> | :ref:`RID<class_RID>`                                             | :ref:`space<class_World3D_property_space>`                               |
> +-------------------------------------------------------------------+--------------------------------------------------------------------------+
>

----


## Property Descriptions



[CameraAttributes<class_CameraAttributes>] **camera_attributes** [🔗<class_World3D_property_camera_attributes>]


- |void| **set_camera_attributes**\ (\ value\: [CameraAttributes<class_CameraAttributes>]\ )
- [CameraAttributes<class_CameraAttributes>] **get_camera_attributes**\ (\ )

The default [CameraAttributes<class_CameraAttributes>] resource to use if none set on the [Camera3D<class_Camera3D>].


----



[PhysicsDirectSpaceState3D<class_PhysicsDirectSpaceState3D>] **direct_space_state** [🔗<class_World3D_property_direct_space_state>]


- [PhysicsDirectSpaceState3D<class_PhysicsDirectSpaceState3D>] **get_direct_space_state**\ (\ )

Direct access to the world's physics 3D space state. Used for querying current and potential collisions. When using multi-threaded physics, access is limited to [Node._physics_process()<class_Node_private_method__physics_process>] in the main thread.


----



[Environment<class_Environment>] **environment** [🔗<class_World3D_property_environment>]


- |void| **set_environment**\ (\ value\: [Environment<class_Environment>]\ )
- [Environment<class_Environment>] **get_environment**\ (\ )

The World3D's [Environment<class_Environment>].


----



[Environment<class_Environment>] **fallback_environment** [🔗<class_World3D_property_fallback_environment>]


- |void| **set_fallback_environment**\ (\ value\: [Environment<class_Environment>]\ )
- [Environment<class_Environment>] **get_fallback_environment**\ (\ )

The World3D's fallback environment will be used if [environment<class_World3D_property_environment>] fails or is missing.


----



[RID<class_RID>] **navigation_map** [🔗<class_World3D_property_navigation_map>]


- [RID<class_RID>] **get_navigation_map**\ (\ )

The [RID<class_RID>] of this world's navigation map. Used by the [NavigationServer3D<class_NavigationServer3D>].


----



[RID<class_RID>] **scenario** [🔗<class_World3D_property_scenario>]


- [RID<class_RID>] **get_scenario**\ (\ )

The World3D's visual scenario.


----



[RID<class_RID>] **space** [🔗<class_World3D_property_space>]


- [RID<class_RID>] **get_space**\ (\ )

The World3D's physics space.

