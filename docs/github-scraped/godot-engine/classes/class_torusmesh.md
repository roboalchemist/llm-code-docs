:github_url: hide



# TorusMesh

**Inherits:** [PrimitiveMesh<class_PrimitiveMesh>] **<** [Mesh<class_Mesh>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Class representing a torus [PrimitiveMesh<class_PrimitiveMesh>].


## Description

Class representing a torus [PrimitiveMesh<class_PrimitiveMesh>].


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+--------------------------------------------------------------+---------+
> | :ref:`float<class_float>` | :ref:`inner_radius<class_TorusMesh_property_inner_radius>`   | ``0.5`` |
> +---------------------------+--------------------------------------------------------------+---------+
> | :ref:`float<class_float>` | :ref:`outer_radius<class_TorusMesh_property_outer_radius>`   | ``1.0`` |
> +---------------------------+--------------------------------------------------------------+---------+
> | :ref:`int<class_int>`     | :ref:`ring_segments<class_TorusMesh_property_ring_segments>` | ``32``  |
> +---------------------------+--------------------------------------------------------------+---------+
> | :ref:`int<class_int>`     | :ref:`rings<class_TorusMesh_property_rings>`                 | ``64``  |
> +---------------------------+--------------------------------------------------------------+---------+
>

----


## Property Descriptions



[float<class_float>] **inner_radius** = `0.5` [🔗<class_TorusMesh_property_inner_radius>]


- |void| **set_inner_radius**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_inner_radius**\ (\ )

The inner radius of the torus.


----



[float<class_float>] **outer_radius** = `1.0` [🔗<class_TorusMesh_property_outer_radius>]


- |void| **set_outer_radius**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_outer_radius**\ (\ )

The outer radius of the torus.


----



[int<class_int>] **ring_segments** = `32` [🔗<class_TorusMesh_property_ring_segments>]


- |void| **set_ring_segments**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_ring_segments**\ (\ )

The number of edges each ring of the torus is constructed of.


----



[int<class_int>] **rings** = `64` [🔗<class_TorusMesh_property_rings>]


- |void| **set_rings**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_rings**\ (\ )

The number of slices the torus is constructed of.

