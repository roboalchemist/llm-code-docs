:github_url: hide



# WorldBoundaryShape3D

**Inherits:** [Shape3D<class_Shape3D>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A 3D world boundary (half-space) shape used for physics collision.


## Description

A 3D world boundary shape, intended for use in physics. **WorldBoundaryShape3D** works like an infinite plane that forces all physics bodies to stay above it. The [plane<class_WorldBoundaryShape3D_property_plane>]'s normal determines which direction is considered as "above" and in the editor, the line over the plane represents this direction. It can for example be used for endless flat floors.

\ **Note:** When the physics engine is set to **Jolt Physics** in the project settings ([ProjectSettings.physics/3d/physics_engine<class_ProjectSettings_property_physics/3d/physics_engine>]), **WorldBoundaryShape3D** has a finite size (centered at the shape's origin). It can be adjusted by changing [ProjectSettings.physics/jolt_physics_3d/limits/world_boundary_shape_size<class_ProjectSettings_property_physics/jolt_physics_3d/limits/world_boundary_shape_size>].


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+---------------------------------------------------------+-----------------------+
> | :ref:`Plane<class_Plane>` | :ref:`plane<class_WorldBoundaryShape3D_property_plane>` | ``Plane(0, 1, 0, 0)`` |
> +---------------------------+---------------------------------------------------------+-----------------------+
>

----


## Property Descriptions



[Plane<class_Plane>] **plane** = `Plane(0, 1, 0, 0)` [🔗<class_WorldBoundaryShape3D_property_plane>]


- |void| **set_plane**\ (\ value\: [Plane<class_Plane>]\ )
- [Plane<class_Plane>] **get_plane**\ (\ )

The [Plane<class_Plane>] used by the **WorldBoundaryShape3D** for collision.

