:github_url: hide



# CSGPolygon3D

**Inherits:** [CSGPrimitive3D<class_CSGPrimitive3D>] **<** [CSGShape3D<class_CSGShape3D>] **<** [GeometryInstance3D<class_GeometryInstance3D>] **<** [VisualInstance3D<class_VisualInstance3D>] **<** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

Extrudes a 2D polygon shape to create a 3D mesh.


## Description

An array of 2D points is extruded to quickly and easily create a variety of 3D meshes. See also [CSGMesh3D<class_CSGMesh3D>] for using 3D meshes as CSG nodes.

\ **Note:** CSG nodes are intended to be used for level prototyping. Creating CSG nodes has a significant CPU cost compared to creating a [MeshInstance3D<class_MeshInstance3D>] with a [PrimitiveMesh<class_PrimitiveMesh>]. Moving a CSG node within another CSG node also has a significant CPU cost, so it should be avoided during gameplay.


## Tutorials

- [../tutorials/3d/csg_tools](Prototyping levels with CSG .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------------------+-----------------------------------------------------------------------------------+------------------------------------------------+
> | :ref:`float<class_float>`                                   | :ref:`depth<class_CSGPolygon3D_property_depth>`                                   | ``1.0``                                        |
> +-------------------------------------------------------------+-----------------------------------------------------------------------------------+------------------------------------------------+
> | :ref:`Material<class_Material>`                             | :ref:`material<class_CSGPolygon3D_property_material>`                             |                                                |
> +-------------------------------------------------------------+-----------------------------------------------------------------------------------+------------------------------------------------+
> | :ref:`Mode<enum_CSGPolygon3D_Mode>`                         | :ref:`mode<class_CSGPolygon3D_property_mode>`                                     | ``0``                                          |
> +-------------------------------------------------------------+-----------------------------------------------------------------------------------+------------------------------------------------+
> | :ref:`bool<class_bool>`                                     | :ref:`path_continuous_u<class_CSGPolygon3D_property_path_continuous_u>`           |                                                |
> +-------------------------------------------------------------+-----------------------------------------------------------------------------------+------------------------------------------------+
> | :ref:`float<class_float>`                                   | :ref:`path_interval<class_CSGPolygon3D_property_path_interval>`                   |                                                |
> +-------------------------------------------------------------+-----------------------------------------------------------------------------------+------------------------------------------------+
> | :ref:`PathIntervalType<enum_CSGPolygon3D_PathIntervalType>` | :ref:`path_interval_type<class_CSGPolygon3D_property_path_interval_type>`         |                                                |
> +-------------------------------------------------------------+-----------------------------------------------------------------------------------+------------------------------------------------+
> | :ref:`bool<class_bool>`                                     | :ref:`path_joined<class_CSGPolygon3D_property_path_joined>`                       |                                                |
> +-------------------------------------------------------------+-----------------------------------------------------------------------------------+------------------------------------------------+
> | :ref:`bool<class_bool>`                                     | :ref:`path_local<class_CSGPolygon3D_property_path_local>`                         |                                                |
> +-------------------------------------------------------------+-----------------------------------------------------------------------------------+------------------------------------------------+
> | :ref:`NodePath<class_NodePath>`                             | :ref:`path_node<class_CSGPolygon3D_property_path_node>`                           |                                                |
> +-------------------------------------------------------------+-----------------------------------------------------------------------------------+------------------------------------------------+
> | :ref:`PathRotation<enum_CSGPolygon3D_PathRotation>`         | :ref:`path_rotation<class_CSGPolygon3D_property_path_rotation>`                   |                                                |
> +-------------------------------------------------------------+-----------------------------------------------------------------------------------+------------------------------------------------+
> | :ref:`bool<class_bool>`                                     | :ref:`path_rotation_accurate<class_CSGPolygon3D_property_path_rotation_accurate>` |                                                |
> +-------------------------------------------------------------+-----------------------------------------------------------------------------------+------------------------------------------------+
> | :ref:`float<class_float>`                                   | :ref:`path_simplify_angle<class_CSGPolygon3D_property_path_simplify_angle>`       |                                                |
> +-------------------------------------------------------------+-----------------------------------------------------------------------------------+------------------------------------------------+
> | :ref:`float<class_float>`                                   | :ref:`path_u_distance<class_CSGPolygon3D_property_path_u_distance>`               |                                                |
> +-------------------------------------------------------------+-----------------------------------------------------------------------------------+------------------------------------------------+
> | :ref:`PackedVector2Array<class_PackedVector2Array>`         | :ref:`polygon<class_CSGPolygon3D_property_polygon>`                               | ``PackedVector2Array(0, 0, 0, 1, 1, 1, 1, 0)`` |
> +-------------------------------------------------------------+-----------------------------------------------------------------------------------+------------------------------------------------+
> | :ref:`bool<class_bool>`                                     | :ref:`smooth_faces<class_CSGPolygon3D_property_smooth_faces>`                     | ``false``                                      |
> +-------------------------------------------------------------+-----------------------------------------------------------------------------------+------------------------------------------------+
> | :ref:`float<class_float>`                                   | :ref:`spin_degrees<class_CSGPolygon3D_property_spin_degrees>`                     |                                                |
> +-------------------------------------------------------------+-----------------------------------------------------------------------------------+------------------------------------------------+
> | :ref:`int<class_int>`                                       | :ref:`spin_sides<class_CSGPolygon3D_property_spin_sides>`                         |                                                |
> +-------------------------------------------------------------+-----------------------------------------------------------------------------------+------------------------------------------------+
>

----


## Enumerations



enum **Mode**: [🔗<enum_CSGPolygon3D_Mode>]



[Mode<enum_CSGPolygon3D_Mode>] **MODE_DEPTH** = `0`

The [polygon<class_CSGPolygon3D_property_polygon>] shape is extruded along the negative Z axis.



[Mode<enum_CSGPolygon3D_Mode>] **MODE_SPIN** = `1`

The [polygon<class_CSGPolygon3D_property_polygon>] shape is extruded by rotating it around the Y axis.



[Mode<enum_CSGPolygon3D_Mode>] **MODE_PATH** = `2`

The [polygon<class_CSGPolygon3D_property_polygon>] shape is extruded along the [Path3D<class_Path3D>] specified in [path_node<class_CSGPolygon3D_property_path_node>].


----



enum **PathRotation**: [🔗<enum_CSGPolygon3D_PathRotation>]



[PathRotation<enum_CSGPolygon3D_PathRotation>] **PATH_ROTATION_POLYGON** = `0`

The [polygon<class_CSGPolygon3D_property_polygon>] shape is not rotated.

\ **Note:** Requires the path Z coordinates to continually decrease to ensure viable shapes.



[PathRotation<enum_CSGPolygon3D_PathRotation>] **PATH_ROTATION_PATH** = `1`

The [polygon<class_CSGPolygon3D_property_polygon>] shape is rotated along the path, but it is not rotated around the path axis.

\ **Note:** Requires the path Z coordinates to continually decrease to ensure viable shapes.



[PathRotation<enum_CSGPolygon3D_PathRotation>] **PATH_ROTATION_PATH_FOLLOW** = `2`

The [polygon<class_CSGPolygon3D_property_polygon>] shape follows the path and its rotations around the path axis.


----



enum **PathIntervalType**: [🔗<enum_CSGPolygon3D_PathIntervalType>]



[PathIntervalType<enum_CSGPolygon3D_PathIntervalType>] **PATH_INTERVAL_DISTANCE** = `0`

When [mode<class_CSGPolygon3D_property_mode>] is set to [MODE_PATH<class_CSGPolygon3D_constant_MODE_PATH>], [path_interval<class_CSGPolygon3D_property_path_interval>] will determine the distance, in meters, each interval of the path will extrude.



[PathIntervalType<enum_CSGPolygon3D_PathIntervalType>] **PATH_INTERVAL_SUBDIVIDE** = `1`

When [mode<class_CSGPolygon3D_property_mode>] is set to [MODE_PATH<class_CSGPolygon3D_constant_MODE_PATH>], [path_interval<class_CSGPolygon3D_property_path_interval>] will subdivide the polygons along the path.


----


## Property Descriptions



[float<class_float>] **depth** = `1.0` [🔗<class_CSGPolygon3D_property_depth>]


- |void| **set_depth**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_depth**\ (\ )

When [mode<class_CSGPolygon3D_property_mode>] is [MODE_DEPTH<class_CSGPolygon3D_constant_MODE_DEPTH>], the depth of the extrusion.


----



[Material<class_Material>] **material** [🔗<class_CSGPolygon3D_property_material>]


- |void| **set_material**\ (\ value\: [Material<class_Material>]\ )
- [Material<class_Material>] **get_material**\ (\ )

Material to use for the resulting mesh. The UV maps the top half of the material to the extruded shape (U along the length of the extrusions and V around the outline of the [polygon<class_CSGPolygon3D_property_polygon>]), the bottom-left quarter to the front end face, and the bottom-right quarter to the back end face.


----



[Mode<enum_CSGPolygon3D_Mode>] **mode** = `0` [🔗<class_CSGPolygon3D_property_mode>]


- |void| **set_mode**\ (\ value\: [Mode<enum_CSGPolygon3D_Mode>]\ )
- [Mode<enum_CSGPolygon3D_Mode>] **get_mode**\ (\ )

The [mode<class_CSGPolygon3D_property_mode>] used to extrude the [polygon<class_CSGPolygon3D_property_polygon>].


----



[bool<class_bool>] **path_continuous_u** [🔗<class_CSGPolygon3D_property_path_continuous_u>]


- |void| **set_path_continuous_u**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_path_continuous_u**\ (\ )

When [mode<class_CSGPolygon3D_property_mode>] is [MODE_PATH<class_CSGPolygon3D_constant_MODE_PATH>], by default, the top half of the [material<class_CSGPolygon3D_property_material>] is stretched along the entire length of the extruded shape. If `false` the top half of the material is repeated every step of the extrusion.


----



[float<class_float>] **path_interval** [🔗<class_CSGPolygon3D_property_path_interval>]


- |void| **set_path_interval**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_path_interval**\ (\ )

When [mode<class_CSGPolygon3D_property_mode>] is [MODE_PATH<class_CSGPolygon3D_constant_MODE_PATH>], the path interval or ratio of path points to extrusions.


----



[PathIntervalType<enum_CSGPolygon3D_PathIntervalType>] **path_interval_type** [🔗<class_CSGPolygon3D_property_path_interval_type>]


- |void| **set_path_interval_type**\ (\ value\: [PathIntervalType<enum_CSGPolygon3D_PathIntervalType>]\ )
- [PathIntervalType<enum_CSGPolygon3D_PathIntervalType>] **get_path_interval_type**\ (\ )

When [mode<class_CSGPolygon3D_property_mode>] is [MODE_PATH<class_CSGPolygon3D_constant_MODE_PATH>], this will determine if the interval should be by distance ([PATH_INTERVAL_DISTANCE<class_CSGPolygon3D_constant_PATH_INTERVAL_DISTANCE>]) or subdivision fractions ([PATH_INTERVAL_SUBDIVIDE<class_CSGPolygon3D_constant_PATH_INTERVAL_SUBDIVIDE>]).


----



[bool<class_bool>] **path_joined** [🔗<class_CSGPolygon3D_property_path_joined>]


- |void| **set_path_joined**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_path_joined**\ (\ )

When [mode<class_CSGPolygon3D_property_mode>] is [MODE_PATH<class_CSGPolygon3D_constant_MODE_PATH>], if `true` the ends of the path are joined, by adding an extrusion between the last and first points of the path.


----



[bool<class_bool>] **path_local** [🔗<class_CSGPolygon3D_property_path_local>]


- |void| **set_path_local**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_path_local**\ (\ )

When [mode<class_CSGPolygon3D_property_mode>] is [MODE_PATH<class_CSGPolygon3D_constant_MODE_PATH>], if `true` the [Transform3D<class_Transform3D>] of the **CSGPolygon3D** is used as the starting point for the extrusions, not the [Transform3D<class_Transform3D>] of the [path_node<class_CSGPolygon3D_property_path_node>].


----



[NodePath<class_NodePath>] **path_node** [🔗<class_CSGPolygon3D_property_path_node>]


- |void| **set_path_node**\ (\ value\: [NodePath<class_NodePath>]\ )
- [NodePath<class_NodePath>] **get_path_node**\ (\ )

When [mode<class_CSGPolygon3D_property_mode>] is [MODE_PATH<class_CSGPolygon3D_constant_MODE_PATH>], the location of the [Path3D<class_Path3D>] object used to extrude the [polygon<class_CSGPolygon3D_property_polygon>].


----



[PathRotation<enum_CSGPolygon3D_PathRotation>] **path_rotation** [🔗<class_CSGPolygon3D_property_path_rotation>]


- |void| **set_path_rotation**\ (\ value\: [PathRotation<enum_CSGPolygon3D_PathRotation>]\ )
- [PathRotation<enum_CSGPolygon3D_PathRotation>] **get_path_rotation**\ (\ )

When [mode<class_CSGPolygon3D_property_mode>] is [MODE_PATH<class_CSGPolygon3D_constant_MODE_PATH>], the path rotation method used to rotate the [polygon<class_CSGPolygon3D_property_polygon>] as it is extruded.


----



[bool<class_bool>] **path_rotation_accurate** [🔗<class_CSGPolygon3D_property_path_rotation_accurate>]


- |void| **set_path_rotation_accurate**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_path_rotation_accurate**\ (\ )

When [mode<class_CSGPolygon3D_property_mode>] is [MODE_PATH<class_CSGPolygon3D_constant_MODE_PATH>], if `true` the polygon will be rotated according to the proper tangent of the path at the sampled points. If `false` an approximation is used, which decreases in accuracy as the number of subdivisions decreases.


----



[float<class_float>] **path_simplify_angle** [🔗<class_CSGPolygon3D_property_path_simplify_angle>]


- |void| **set_path_simplify_angle**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_path_simplify_angle**\ (\ )

When [mode<class_CSGPolygon3D_property_mode>] is [MODE_PATH<class_CSGPolygon3D_constant_MODE_PATH>], extrusions that are less than this angle, will be merged together to reduce polygon count.


----



[float<class_float>] **path_u_distance** [🔗<class_CSGPolygon3D_property_path_u_distance>]


- |void| **set_path_u_distance**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_path_u_distance**\ (\ )

When [mode<class_CSGPolygon3D_property_mode>] is [MODE_PATH<class_CSGPolygon3D_constant_MODE_PATH>], this is the distance along the path, in meters, the texture coordinates will tile. When set to 0, texture coordinates will match geometry exactly with no tiling.


----



[PackedVector2Array<class_PackedVector2Array>] **polygon** = `PackedVector2Array(0, 0, 0, 1, 1, 1, 1, 0)` [🔗<class_CSGPolygon3D_property_polygon>]


- |void| **set_polygon**\ (\ value\: [PackedVector2Array<class_PackedVector2Array>]\ )
- [PackedVector2Array<class_PackedVector2Array>] **get_polygon**\ (\ )

The point array that defines the 2D polygon that is extruded. This can be a convex or concave polygon with 3 or more points. The polygon must *not* have any intersecting edges. Otherwise, triangulation will fail and no mesh will be generated.

\ **Note:** If only 1 or 2 points are defined in [polygon<class_CSGPolygon3D_property_polygon>], no mesh will be generated.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedVector2Array<class_PackedVector2Array>] for more details.


----



[bool<class_bool>] **smooth_faces** = `false` [🔗<class_CSGPolygon3D_property_smooth_faces>]


- |void| **set_smooth_faces**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_smooth_faces**\ (\ )

If `true`, applies smooth shading to the extrusions.


----



[float<class_float>] **spin_degrees** [🔗<class_CSGPolygon3D_property_spin_degrees>]


- |void| **set_spin_degrees**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_spin_degrees**\ (\ )

When [mode<class_CSGPolygon3D_property_mode>] is [MODE_SPIN<class_CSGPolygon3D_constant_MODE_SPIN>], the total number of degrees the [polygon<class_CSGPolygon3D_property_polygon>] is rotated when extruding.


----



[int<class_int>] **spin_sides** [🔗<class_CSGPolygon3D_property_spin_sides>]


- |void| **set_spin_sides**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_spin_sides**\ (\ )

When [mode<class_CSGPolygon3D_property_mode>] is [MODE_SPIN<class_CSGPolygon3D_constant_MODE_SPIN>], the number of extrusions made.

