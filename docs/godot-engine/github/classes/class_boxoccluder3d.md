:github_url: hide



# BoxOccluder3D

**Inherits:** [Occluder3D<class_Occluder3D>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Cuboid shape for use with occlusion culling in [OccluderInstance3D<class_OccluderInstance3D>].


## Description

**BoxOccluder3D** stores a cuboid shape that can be used by the engine's occlusion culling system.

See [OccluderInstance3D<class_OccluderInstance3D>]'s documentation for instructions on setting up occlusion culling.


## Tutorials

- [../tutorials/3d/occlusion_culling](Occlusion culling .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------+------------------------------------------------+----------------------+
> | :ref:`Vector3<class_Vector3>` | :ref:`size<class_BoxOccluder3D_property_size>` | ``Vector3(1, 1, 1)`` |
> +-------------------------------+------------------------------------------------+----------------------+
>

----


## Property Descriptions



[Vector3<class_Vector3>] **size** = `Vector3(1, 1, 1)` [🔗<class_BoxOccluder3D_property_size>]


- |void| **set_size**\ (\ value\: [Vector3<class_Vector3>]\ )
- [Vector3<class_Vector3>] **get_size**\ (\ )

The box's size in 3D units.

