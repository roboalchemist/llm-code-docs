:github_url: hide



# SphereMesh

**Inherits:** [PrimitiveMesh<class_PrimitiveMesh>] **<** [Mesh<class_Mesh>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Class representing a spherical [PrimitiveMesh<class_PrimitiveMesh>].


## Description

Class representing a spherical [PrimitiveMesh<class_PrimitiveMesh>].


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+-------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`height<class_SphereMesh_property_height>`                   | ``1.0``   |
> +---------------------------+-------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`   | :ref:`is_hemisphere<class_SphereMesh_property_is_hemisphere>`     | ``false`` |
> +---------------------------+-------------------------------------------------------------------+-----------+
> | :ref:`int<class_int>`     | :ref:`radial_segments<class_SphereMesh_property_radial_segments>` | ``64``    |
> +---------------------------+-------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`radius<class_SphereMesh_property_radius>`                   | ``0.5``   |
> +---------------------------+-------------------------------------------------------------------+-----------+
> | :ref:`int<class_int>`     | :ref:`rings<class_SphereMesh_property_rings>`                     | ``32``    |
> +---------------------------+-------------------------------------------------------------------+-----------+
>

----


## Property Descriptions



[float<class_float>] **height** = `1.0` [🔗<class_SphereMesh_property_height>]


- |void| **set_height**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_height**\ (\ )

Full height of the sphere.


----



[bool<class_bool>] **is_hemisphere** = `false` [🔗<class_SphereMesh_property_is_hemisphere>]


- |void| **set_is_hemisphere**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_is_hemisphere**\ (\ )

If `true`, a hemisphere is created rather than a full sphere.

\ **Note:** To get a regular hemisphere, the height and radius of the sphere must be equal.


----



[int<class_int>] **radial_segments** = `64` [🔗<class_SphereMesh_property_radial_segments>]


- |void| **set_radial_segments**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_radial_segments**\ (\ )

Number of radial segments on the sphere.


----



[float<class_float>] **radius** = `0.5` [🔗<class_SphereMesh_property_radius>]


- |void| **set_radius**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_radius**\ (\ )

Radius of sphere.


----



[int<class_int>] **rings** = `32` [🔗<class_SphereMesh_property_rings>]


- |void| **set_rings**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_rings**\ (\ )

Number of segments along the height of the sphere.

