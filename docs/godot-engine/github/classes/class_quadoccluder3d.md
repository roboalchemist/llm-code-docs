:github_url: hide



# QuadOccluder3D

**Inherits:** [Occluder3D<class_Occluder3D>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Flat plane shape for use with occlusion culling in [OccluderInstance3D<class_OccluderInstance3D>].


## Description

**QuadOccluder3D** stores a flat plane shape that can be used by the engine's occlusion culling system. See also [PolygonOccluder3D<class_PolygonOccluder3D>] if you need to customize the quad's shape.

See [OccluderInstance3D<class_OccluderInstance3D>]'s documentation for instructions on setting up occlusion culling.


## Tutorials

- [../tutorials/3d/occlusion_culling](Occlusion culling .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------+-------------------------------------------------+-------------------+
> | :ref:`Vector2<class_Vector2>` | :ref:`size<class_QuadOccluder3D_property_size>` | ``Vector2(1, 1)`` |
> +-------------------------------+-------------------------------------------------+-------------------+
>

----


## Property Descriptions



[Vector2<class_Vector2>] **size** = `Vector2(1, 1)` [🔗<class_QuadOccluder3D_property_size>]


- |void| **set_size**\ (\ value\: [Vector2<class_Vector2>]\ )
- [Vector2<class_Vector2>] **get_size**\ (\ )

The quad's size in 3D units.

