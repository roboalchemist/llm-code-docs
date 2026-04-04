:github_url: hide



# CapsuleMesh

**Inherits:** [PrimitiveMesh<class_PrimitiveMesh>] **<** [Mesh<class_Mesh>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Class representing a capsule-shaped [PrimitiveMesh<class_PrimitiveMesh>].


## Description

Class representing a capsule-shaped [PrimitiveMesh<class_PrimitiveMesh>].


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+--------------------------------------------------------------------+---------+
> | :ref:`float<class_float>` | :ref:`height<class_CapsuleMesh_property_height>`                   | ``2.0`` |
> +---------------------------+--------------------------------------------------------------------+---------+
> | :ref:`int<class_int>`     | :ref:`radial_segments<class_CapsuleMesh_property_radial_segments>` | ``64``  |
> +---------------------------+--------------------------------------------------------------------+---------+
> | :ref:`float<class_float>` | :ref:`radius<class_CapsuleMesh_property_radius>`                   | ``0.5`` |
> +---------------------------+--------------------------------------------------------------------+---------+
> | :ref:`int<class_int>`     | :ref:`rings<class_CapsuleMesh_property_rings>`                     | ``8``   |
> +---------------------------+--------------------------------------------------------------------+---------+
>

----


## Property Descriptions



[float<class_float>] **height** = `2.0` [🔗<class_CapsuleMesh_property_height>]


- |void| **set_height**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_height**\ (\ )

Total height of the capsule mesh (including the hemispherical ends).

\ **Note:** The [height<class_CapsuleMesh_property_height>] of a capsule must be at least twice its [radius<class_CapsuleMesh_property_radius>]. Otherwise, the capsule becomes a circle. If the [height<class_CapsuleMesh_property_height>] is less than twice the [radius<class_CapsuleMesh_property_radius>], the properties adjust to a valid value.


----



[int<class_int>] **radial_segments** = `64` [🔗<class_CapsuleMesh_property_radial_segments>]


- |void| **set_radial_segments**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_radial_segments**\ (\ )

Number of radial segments on the capsule mesh.


----



[float<class_float>] **radius** = `0.5` [🔗<class_CapsuleMesh_property_radius>]


- |void| **set_radius**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_radius**\ (\ )

Radius of the capsule mesh.

\ **Note:** The [radius<class_CapsuleMesh_property_radius>] of a capsule cannot be greater than half of its [height<class_CapsuleMesh_property_height>]. Otherwise, the capsule becomes a circle. If the [radius<class_CapsuleMesh_property_radius>] is greater than half of the [height<class_CapsuleMesh_property_height>], the properties adjust to a valid value.


----



[int<class_int>] **rings** = `8` [🔗<class_CapsuleMesh_property_rings>]


- |void| **set_rings**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_rings**\ (\ )

Number of rings along the height of the capsule.

