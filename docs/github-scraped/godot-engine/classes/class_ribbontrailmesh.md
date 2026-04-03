:github_url: hide



# RibbonTrailMesh

**Inherits:** [PrimitiveMesh<class_PrimitiveMesh>] **<** [Mesh<class_Mesh>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Represents a straight ribbon-shaped [PrimitiveMesh<class_PrimitiveMesh>] with variable width.


## Description

**RibbonTrailMesh** represents a straight ribbon-shaped mesh with variable width. The ribbon is composed of a number of flat or cross-shaped sections, each with the same [section_length<class_RibbonTrailMesh_property_section_length>] and number of [section_segments<class_RibbonTrailMesh_property_section_segments>]. A [curve<class_RibbonTrailMesh_property_curve>] is sampled along the total length of the ribbon, meaning that the curve determines the size of the ribbon along its length.

This primitive mesh is usually used for particle trails.


## Tutorials

- [../tutorials/3d/particles/trails](3D Particle trails .md)

- [../tutorials/3d/particles/index](Particle systems (3D) .md)


## Properties

> **TABLE**
> :widths: auto
>
> +------------------------------------------+--------------------------------------------------------------------------+---------+
> | :ref:`Curve<class_Curve>`                | :ref:`curve<class_RibbonTrailMesh_property_curve>`                       |         |
> +------------------------------------------+--------------------------------------------------------------------------+---------+
> | :ref:`float<class_float>`                | :ref:`section_length<class_RibbonTrailMesh_property_section_length>`     | ``0.2`` |
> +------------------------------------------+--------------------------------------------------------------------------+---------+
> | :ref:`int<class_int>`                    | :ref:`section_segments<class_RibbonTrailMesh_property_section_segments>` | ``3``   |
> +------------------------------------------+--------------------------------------------------------------------------+---------+
> | :ref:`int<class_int>`                    | :ref:`sections<class_RibbonTrailMesh_property_sections>`                 | ``5``   |
> +------------------------------------------+--------------------------------------------------------------------------+---------+
> | :ref:`Shape<enum_RibbonTrailMesh_Shape>` | :ref:`shape<class_RibbonTrailMesh_property_shape>`                       | ``1``   |
> +------------------------------------------+--------------------------------------------------------------------------+---------+
> | :ref:`float<class_float>`                | :ref:`size<class_RibbonTrailMesh_property_size>`                         | ``1.0`` |
> +------------------------------------------+--------------------------------------------------------------------------+---------+
>

----


## Enumerations



enum **Shape**: [🔗<enum_RibbonTrailMesh_Shape>]



[Shape<enum_RibbonTrailMesh_Shape>] **SHAPE_FLAT** = `0`

Gives the mesh a single flat face.



[Shape<enum_RibbonTrailMesh_Shape>] **SHAPE_CROSS** = `1`

Gives the mesh two perpendicular flat faces, making a cross shape.


----


## Property Descriptions



[Curve<class_Curve>] **curve** [🔗<class_RibbonTrailMesh_property_curve>]


- |void| **set_curve**\ (\ value\: [Curve<class_Curve>]\ )
- [Curve<class_Curve>] **get_curve**\ (\ )

Determines the size of the ribbon along its length. The size of a particular section segment is obtained by multiplying the baseline [size<class_RibbonTrailMesh_property_size>] by the value of this curve at the given distance. For values smaller than `0`, the faces will be inverted. Should be a unit [Curve<class_Curve>].


----



[float<class_float>] **section_length** = `0.2` [🔗<class_RibbonTrailMesh_property_section_length>]


- |void| **set_section_length**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_section_length**\ (\ )

The length of a section of the ribbon.


----



[int<class_int>] **section_segments** = `3` [🔗<class_RibbonTrailMesh_property_section_segments>]


- |void| **set_section_segments**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_section_segments**\ (\ )

The number of segments in a section. The [curve<class_RibbonTrailMesh_property_curve>] is sampled on each segment to determine its size. Higher values result in a more detailed ribbon at the cost of performance.


----



[int<class_int>] **sections** = `5` [🔗<class_RibbonTrailMesh_property_sections>]


- |void| **set_sections**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_sections**\ (\ )

The total number of sections on the ribbon.


----



[Shape<enum_RibbonTrailMesh_Shape>] **shape** = `1` [🔗<class_RibbonTrailMesh_property_shape>]


- |void| **set_shape**\ (\ value\: [Shape<enum_RibbonTrailMesh_Shape>]\ )
- [Shape<enum_RibbonTrailMesh_Shape>] **get_shape**\ (\ )

Determines the shape of the ribbon.


----



[float<class_float>] **size** = `1.0` [🔗<class_RibbonTrailMesh_property_size>]


- |void| **set_size**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_size**\ (\ )

The baseline size of the ribbon. The size of a particular section segment is obtained by multiplying this size by the value of the [curve<class_RibbonTrailMesh_property_curve>] at the given distance.

