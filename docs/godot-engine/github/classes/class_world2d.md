:github_url: hide



# World2D

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A resource that holds all components of a 2D world, such as a canvas and a physics space.


## Description

Class that has everything pertaining to a 2D world: A physics space, a canvas, and a sound space. 2D nodes register their resources into the current 2D world.


## Tutorials

- [../tutorials/physics/ray-casting](Ray-casting .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------------------------+----------------------------------------------------------------------+
> | :ref:`RID<class_RID>`                                             | :ref:`canvas<class_World2D_property_canvas>`                         |
> +-------------------------------------------------------------------+----------------------------------------------------------------------+
> | :ref:`PhysicsDirectSpaceState2D<class_PhysicsDirectSpaceState2D>` | :ref:`direct_space_state<class_World2D_property_direct_space_state>` |
> +-------------------------------------------------------------------+----------------------------------------------------------------------+
> | :ref:`RID<class_RID>`                                             | :ref:`navigation_map<class_World2D_property_navigation_map>`         |
> +-------------------------------------------------------------------+----------------------------------------------------------------------+
> | :ref:`RID<class_RID>`                                             | :ref:`space<class_World2D_property_space>`                           |
> +-------------------------------------------------------------------+----------------------------------------------------------------------+
>

----


## Property Descriptions



[RID<class_RID>] **canvas** [🔗<class_World2D_property_canvas>]


- [RID<class_RID>] **get_canvas**\ (\ )

The [RID<class_RID>] of this world's canvas resource. Used by the [RenderingServer<class_RenderingServer>] for 2D drawing.


----



[PhysicsDirectSpaceState2D<class_PhysicsDirectSpaceState2D>] **direct_space_state** [🔗<class_World2D_property_direct_space_state>]


- [PhysicsDirectSpaceState2D<class_PhysicsDirectSpaceState2D>] **get_direct_space_state**\ (\ )

Direct access to the world's physics 2D space state. Used for querying current and potential collisions. When using multi-threaded physics, access is limited to [Node._physics_process()<class_Node_private_method__physics_process>] in the main thread.


----



[RID<class_RID>] **navigation_map** [🔗<class_World2D_property_navigation_map>]


- [RID<class_RID>] **get_navigation_map**\ (\ )

The [RID<class_RID>] of this world's navigation map. Used by the [NavigationServer2D<class_NavigationServer2D>].


----



[RID<class_RID>] **space** [🔗<class_World2D_property_space>]


- [RID<class_RID>] **get_space**\ (\ )

The [RID<class_RID>] of this world's physics space resource. Used by the [PhysicsServer2D<class_PhysicsServer2D>] for 2D physics, treating it as both a space and an area.

