:github_url: hide



# Shape3D

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [BoxShape3D<class_BoxShape3D>], [CapsuleShape3D<class_CapsuleShape3D>], [ConcavePolygonShape3D<class_ConcavePolygonShape3D>], [ConvexPolygonShape3D<class_ConvexPolygonShape3D>], [CylinderShape3D<class_CylinderShape3D>], [HeightMapShape3D<class_HeightMapShape3D>], [SeparationRayShape3D<class_SeparationRayShape3D>], [SphereShape3D<class_SphereShape3D>], [WorldBoundaryShape3D<class_WorldBoundaryShape3D>]

Abstract base class for 3D shapes used for physics collision.


## Description

Abstract base class for all 3D shapes, intended for use in physics.

\ **Performance:** Primitive shapes, especially [SphereShape3D<class_SphereShape3D>], are fast to check collisions against. [ConvexPolygonShape3D<class_ConvexPolygonShape3D>] and [HeightMapShape3D<class_HeightMapShape3D>] are slower, and [ConcavePolygonShape3D<class_ConcavePolygonShape3D>] is the slowest.


## Tutorials

- [../tutorials/physics/physics_introduction](Physics introduction .md)


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+----------------------------------------------------------------------+----------+
> | :ref:`float<class_float>` | :ref:`custom_solver_bias<class_Shape3D_property_custom_solver_bias>` | ``0.0``  |
> +---------------------------+----------------------------------------------------------------------+----------+
> | :ref:`float<class_float>` | :ref:`margin<class_Shape3D_property_margin>`                         | ``0.04`` |
> +---------------------------+----------------------------------------------------------------------+----------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------+------------------------------------------------------------------+
> | :ref:`ArrayMesh<class_ArrayMesh>` | :ref:`get_debug_mesh<class_Shape3D_method_get_debug_mesh>`\ (\ ) |
> +-----------------------------------+------------------------------------------------------------------+
>

----


## Property Descriptions



[float<class_float>] **custom_solver_bias** = `0.0` [🔗<class_Shape3D_property_custom_solver_bias>]


- |void| **set_custom_solver_bias**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_custom_solver_bias**\ (\ )

The shape's custom solver bias. Defines how much bodies react to enforce contact separation when this shape is involved.

When set to `0`, the default value from [ProjectSettings.physics/3d/solver/default_contact_bias<class_ProjectSettings_property_physics/3d/solver/default_contact_bias>] is used.


----



[float<class_float>] **margin** = `0.04` [🔗<class_Shape3D_property_margin>]


- |void| **set_margin**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_margin**\ (\ )

The collision margin for the shape. This is not used in Godot Physics.

Collision margins allow collision detection to be more efficient by adding an extra shell around shapes. Collision algorithms are more expensive when objects overlap by more than their margin, so a higher value for margins is better for performance, at the cost of accuracy around edges as it makes them less sharp.


----


## Method Descriptions



[ArrayMesh<class_ArrayMesh>] **get_debug_mesh**\ (\ ) [🔗<class_Shape3D_method_get_debug_mesh>]

Returns the [ArrayMesh<class_ArrayMesh>] used to draw the debug collision for this **Shape3D**.

