:github_url: hide



# NavigationPolygon

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A 2D navigation mesh that describes a traversable surface for pathfinding.


## Description

A navigation mesh can be created either by baking it with the help of the [NavigationServer2D<class_NavigationServer2D>], or by adding vertices and convex polygon indices arrays manually.

To bake a navigation mesh at least one outline needs to be added that defines the outer bounds of the baked area.


> **TABS**
>

    var new_navigation_mesh = NavigationPolygon.new()
    var bounding_outline = PackedVector2Array([Vector2(0, 0), Vector2(0, 50), Vector2(50, 50), Vector2(50, 0)])
    new_navigation_mesh.add_outline(bounding_outline)
    NavigationServer2D.bake_from_source_geometry_data(new_navigation_mesh, NavigationMeshSourceGeometryData2D.new());
    $NavigationRegion2D.navigation_polygon = new_navigation_mesh


    var newNavigationMesh = new NavigationPolygon();
    Vector2[] boundingOutline = [new Vector2(0, 0), new Vector2(0, 50), new Vector2(50, 50), new Vector2(50, 0)];
    newNavigationMesh.AddOutline(boundingOutline);
    NavigationServer2D.BakeFromSourceGeometryData(newNavigationMesh, new NavigationMeshSourceGeometryData2D());
    GetNode<NavigationRegion2D>("NavigationRegion2D").NavigationPolygon = newNavigationMesh;



Adding vertices and polygon indices manually.


> **TABS**
>

    var new_navigation_mesh = NavigationPolygon.new()
    var new_vertices = PackedVector2Array([Vector2(0, 0), Vector2(0, 50), Vector2(50, 50), Vector2(50, 0)])
    new_navigation_mesh.vertices = new_vertices
    var new_polygon_indices = PackedInt32Array([0, 1, 2, 3])
    new_navigation_mesh.add_polygon(new_polygon_indices)
    $NavigationRegion2D.navigation_polygon = new_navigation_mesh


    var newNavigationMesh = new NavigationPolygon();
    Vector2[] newVertices = [new Vector2(0, 0), new Vector2(0, 50), new Vector2(50, 50), new Vector2(50, 0)];
    newNavigationMesh.Vertices = newVertices;
    int[] newPolygonIndices = [0, 1, 2, 3];
    newNavigationMesh.AddPolygon(newPolygonIndices);
    GetNode<NavigationRegion2D>("NavigationRegion2D").NavigationPolygon = newNavigationMesh;




## Tutorials

- [../tutorials/navigation/navigation_using_navigationmeshes](Using NavigationMeshes .md)

- [Navigation Polygon 2D Demo ](https://godotengine.org/asset-library/asset/2722)_


## Properties

> **TABLE**
> :widths: auto
>
> +------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+-------------------------------------------------+
> | :ref:`float<class_float>`                                              | :ref:`agent_radius<class_NavigationPolygon_property_agent_radius>`                             | ``10.0``                                        |
> +------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+-------------------------------------------------+
> | :ref:`Rect2<class_Rect2>`                                              | :ref:`baking_rect<class_NavigationPolygon_property_baking_rect>`                               | ``Rect2(0, 0, 0, 0)``                           |
> +------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+-------------------------------------------------+
> | :ref:`Vector2<class_Vector2>`                                          | :ref:`baking_rect_offset<class_NavigationPolygon_property_baking_rect_offset>`                 | ``Vector2(0, 0)``                               |
> +------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+-------------------------------------------------+
> | :ref:`float<class_float>`                                              | :ref:`border_size<class_NavigationPolygon_property_border_size>`                               | ``0.0``                                         |
> +------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+-------------------------------------------------+
> | :ref:`float<class_float>`                                              | :ref:`cell_size<class_NavigationPolygon_property_cell_size>`                                   | ``1.0``                                         |
> +------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+-------------------------------------------------+
> | :ref:`int<class_int>`                                                  | :ref:`parsed_collision_mask<class_NavigationPolygon_property_parsed_collision_mask>`           | ``4294967295``                                  |
> +------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+-------------------------------------------------+
> | :ref:`ParsedGeometryType<enum_NavigationPolygon_ParsedGeometryType>`   | :ref:`parsed_geometry_type<class_NavigationPolygon_property_parsed_geometry_type>`             | ``2``                                           |
> +------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+-------------------------------------------------+
> | :ref:`SamplePartitionType<enum_NavigationPolygon_SamplePartitionType>` | :ref:`sample_partition_type<class_NavigationPolygon_property_sample_partition_type>`           | ``0``                                           |
> +------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+-------------------------------------------------+
> | :ref:`StringName<class_StringName>`                                    | :ref:`source_geometry_group_name<class_NavigationPolygon_property_source_geometry_group_name>` | ``&"navigation_polygon_source_geometry_group"`` |
> +------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+-------------------------------------------------+
> | :ref:`SourceGeometryMode<enum_NavigationPolygon_SourceGeometryMode>`   | :ref:`source_geometry_mode<class_NavigationPolygon_property_source_geometry_mode>`             | ``0``                                           |
> +------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+-------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`add_outline<class_NavigationPolygon_method_add_outline>`\ (\ outline\: :ref:`PackedVector2Array<class_PackedVector2Array>`\ )                                                  |
> +-----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`add_outline_at_index<class_NavigationPolygon_method_add_outline_at_index>`\ (\ outline\: :ref:`PackedVector2Array<class_PackedVector2Array>`, index\: :ref:`int<class_int>`\ ) |
> +-----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`add_polygon<class_NavigationPolygon_method_add_polygon>`\ (\ polygon\: :ref:`PackedInt32Array<class_PackedInt32Array>`\ )                                                      |
> +-----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`clear<class_NavigationPolygon_method_clear>`\ (\ )                                                                                                                             |
> +-----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`clear_outlines<class_NavigationPolygon_method_clear_outlines>`\ (\ )                                                                                                           |
> +-----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`clear_polygons<class_NavigationPolygon_method_clear_polygons>`\ (\ )                                                                                                           |
> +-----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`NavigationMesh<class_NavigationMesh>`         | :ref:`get_navigation_mesh<class_NavigationPolygon_method_get_navigation_mesh>`\ (\ )                                                                                                 |
> +-----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedVector2Array<class_PackedVector2Array>` | :ref:`get_outline<class_NavigationPolygon_method_get_outline>`\ (\ idx\: :ref:`int<class_int>`\ ) |const|                                                                            |
> +-----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                               | :ref:`get_outline_count<class_NavigationPolygon_method_get_outline_count>`\ (\ ) |const|                                                                                             |
> +-----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                             | :ref:`get_parsed_collision_mask_value<class_NavigationPolygon_method_get_parsed_collision_mask_value>`\ (\ layer_number\: :ref:`int<class_int>`\ ) |const|                           |
> +-----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedInt32Array<class_PackedInt32Array>`     | :ref:`get_polygon<class_NavigationPolygon_method_get_polygon>`\ (\ idx\: :ref:`int<class_int>`\ )                                                                                    |
> +-----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                               | :ref:`get_polygon_count<class_NavigationPolygon_method_get_polygon_count>`\ (\ ) |const|                                                                                             |
> +-----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedVector2Array<class_PackedVector2Array>` | :ref:`get_vertices<class_NavigationPolygon_method_get_vertices>`\ (\ ) |const|                                                                                                       |
> +-----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`make_polygons_from_outlines<class_NavigationPolygon_method_make_polygons_from_outlines>`\ (\ )                                                                                 |
> +-----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`remove_outline<class_NavigationPolygon_method_remove_outline>`\ (\ idx\: :ref:`int<class_int>`\ )                                                                              |
> +-----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`set_outline<class_NavigationPolygon_method_set_outline>`\ (\ idx\: :ref:`int<class_int>`, outline\: :ref:`PackedVector2Array<class_PackedVector2Array>`\ )                     |
> +-----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`set_parsed_collision_mask_value<class_NavigationPolygon_method_set_parsed_collision_mask_value>`\ (\ layer_number\: :ref:`int<class_int>`, value\: :ref:`bool<class_bool>`\ )  |
> +-----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`set_vertices<class_NavigationPolygon_method_set_vertices>`\ (\ vertices\: :ref:`PackedVector2Array<class_PackedVector2Array>`\ )                                               |
> +-----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **SamplePartitionType**: [🔗<enum_NavigationPolygon_SamplePartitionType>]



[SamplePartitionType<enum_NavigationPolygon_SamplePartitionType>] **SAMPLE_PARTITION_CONVEX_PARTITION** = `0`

Convex partitioning that results in a navigation mesh with convex polygons.



[SamplePartitionType<enum_NavigationPolygon_SamplePartitionType>] **SAMPLE_PARTITION_TRIANGULATE** = `1`

Triangulation partitioning that results in a navigation mesh with triangle polygons.



[SamplePartitionType<enum_NavigationPolygon_SamplePartitionType>] **SAMPLE_PARTITION_MAX** = `2`

Represents the size of the [SamplePartitionType<enum_NavigationPolygon_SamplePartitionType>] enum.


----



enum **ParsedGeometryType**: [🔗<enum_NavigationPolygon_ParsedGeometryType>]



[ParsedGeometryType<enum_NavigationPolygon_ParsedGeometryType>] **PARSED_GEOMETRY_MESH_INSTANCES** = `0`

Parses mesh instances as obstruction geometry. This includes [Polygon2D<class_Polygon2D>], [MeshInstance2D<class_MeshInstance2D>], [MultiMeshInstance2D<class_MultiMeshInstance2D>], and [TileMap<class_TileMap>] nodes.

Meshes are only parsed when they use a 2D vertices surface format.



[ParsedGeometryType<enum_NavigationPolygon_ParsedGeometryType>] **PARSED_GEOMETRY_STATIC_COLLIDERS** = `1`

Parses [StaticBody2D<class_StaticBody2D>] and [TileMap<class_TileMap>] colliders as obstruction geometry. The collider should be in any of the layers specified by [parsed_collision_mask<class_NavigationPolygon_property_parsed_collision_mask>].



[ParsedGeometryType<enum_NavigationPolygon_ParsedGeometryType>] **PARSED_GEOMETRY_BOTH** = `2`

Both [PARSED_GEOMETRY_MESH_INSTANCES<class_NavigationPolygon_constant_PARSED_GEOMETRY_MESH_INSTANCES>] and [PARSED_GEOMETRY_STATIC_COLLIDERS<class_NavigationPolygon_constant_PARSED_GEOMETRY_STATIC_COLLIDERS>].



[ParsedGeometryType<enum_NavigationPolygon_ParsedGeometryType>] **PARSED_GEOMETRY_MAX** = `3`

Represents the size of the [ParsedGeometryType<enum_NavigationPolygon_ParsedGeometryType>] enum.


----



enum **SourceGeometryMode**: [🔗<enum_NavigationPolygon_SourceGeometryMode>]



[SourceGeometryMode<enum_NavigationPolygon_SourceGeometryMode>] **SOURCE_GEOMETRY_ROOT_NODE_CHILDREN** = `0`

Scans the child nodes of the root node recursively for geometry.



[SourceGeometryMode<enum_NavigationPolygon_SourceGeometryMode>] **SOURCE_GEOMETRY_GROUPS_WITH_CHILDREN** = `1`

Scans nodes in a group and their child nodes recursively for geometry. The group is specified by [source_geometry_group_name<class_NavigationPolygon_property_source_geometry_group_name>].



[SourceGeometryMode<enum_NavigationPolygon_SourceGeometryMode>] **SOURCE_GEOMETRY_GROUPS_EXPLICIT** = `2`

Uses nodes in a group for geometry. The group is specified by [source_geometry_group_name<class_NavigationPolygon_property_source_geometry_group_name>].



[SourceGeometryMode<enum_NavigationPolygon_SourceGeometryMode>] **SOURCE_GEOMETRY_MAX** = `3`

Represents the size of the [SourceGeometryMode<enum_NavigationPolygon_SourceGeometryMode>] enum.


----


## Property Descriptions



[float<class_float>] **agent_radius** = `10.0` [🔗<class_NavigationPolygon_property_agent_radius>]


- |void| **set_agent_radius**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_agent_radius**\ (\ )

The distance to erode/shrink the walkable surface when baking the navigation mesh.

\ **Note:** The radius must be equal or higher than `0.0`. If the radius is `0.0`, it won't be possible to fix invalid outline overlaps and other precision errors during the baking process. As a result, some obstacles may be excluded incorrectly from the final navigation mesh, or may delete the navigation mesh's polygons.


----



[Rect2<class_Rect2>] **baking_rect** = `Rect2(0, 0, 0, 0)` [🔗<class_NavigationPolygon_property_baking_rect>]


- |void| **set_baking_rect**\ (\ value\: [Rect2<class_Rect2>]\ )
- [Rect2<class_Rect2>] **get_baking_rect**\ (\ )

If the baking [Rect2<class_Rect2>] has an area the navigation mesh baking will be restricted to its enclosing area.


----



[Vector2<class_Vector2>] **baking_rect_offset** = `Vector2(0, 0)` [🔗<class_NavigationPolygon_property_baking_rect_offset>]


- |void| **set_baking_rect_offset**\ (\ value\: [Vector2<class_Vector2>]\ )
- [Vector2<class_Vector2>] **get_baking_rect_offset**\ (\ )

The position offset applied to the [baking_rect<class_NavigationPolygon_property_baking_rect>] [Rect2<class_Rect2>].


----



[float<class_float>] **border_size** = `0.0` [🔗<class_NavigationPolygon_property_border_size>]


- |void| **set_border_size**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_border_size**\ (\ )

The size of the non-navigable border around the bake bounding area defined by the [baking_rect<class_NavigationPolygon_property_baking_rect>] [Rect2<class_Rect2>].

In conjunction with the [baking_rect<class_NavigationPolygon_property_baking_rect>] the border size can be used to bake tile aligned navigation meshes without the tile edges being shrunk by [agent_radius<class_NavigationPolygon_property_agent_radius>].


----



[float<class_float>] **cell_size** = `1.0` [🔗<class_NavigationPolygon_property_cell_size>]


- |void| **set_cell_size**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_cell_size**\ (\ )

The cell size used to rasterize the navigation mesh vertices. Must match with the cell size on the navigation map.


----



[int<class_int>] **parsed_collision_mask** = `4294967295` [🔗<class_NavigationPolygon_property_parsed_collision_mask>]


- |void| **set_parsed_collision_mask**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_parsed_collision_mask**\ (\ )

The physics layers to scan for static colliders.

Only used when [parsed_geometry_type<class_NavigationPolygon_property_parsed_geometry_type>] is [PARSED_GEOMETRY_STATIC_COLLIDERS<class_NavigationPolygon_constant_PARSED_GEOMETRY_STATIC_COLLIDERS>] or [PARSED_GEOMETRY_BOTH<class_NavigationPolygon_constant_PARSED_GEOMETRY_BOTH>].


----



[ParsedGeometryType<enum_NavigationPolygon_ParsedGeometryType>] **parsed_geometry_type** = `2` [🔗<class_NavigationPolygon_property_parsed_geometry_type>]


- |void| **set_parsed_geometry_type**\ (\ value\: [ParsedGeometryType<enum_NavigationPolygon_ParsedGeometryType>]\ )
- [ParsedGeometryType<enum_NavigationPolygon_ParsedGeometryType>] **get_parsed_geometry_type**\ (\ )

Determines which type of nodes will be parsed as geometry.


----



[SamplePartitionType<enum_NavigationPolygon_SamplePartitionType>] **sample_partition_type** = `0` [🔗<class_NavigationPolygon_property_sample_partition_type>]


- |void| **set_sample_partition_type**\ (\ value\: [SamplePartitionType<enum_NavigationPolygon_SamplePartitionType>]\ )
- [SamplePartitionType<enum_NavigationPolygon_SamplePartitionType>] **get_sample_partition_type**\ (\ )

Partitioning algorithm for creating the navigation mesh polys.


----



[StringName<class_StringName>] **source_geometry_group_name** = `&"navigation_polygon_source_geometry_group"` [🔗<class_NavigationPolygon_property_source_geometry_group_name>]


- |void| **set_source_geometry_group_name**\ (\ value\: [StringName<class_StringName>]\ )
- [StringName<class_StringName>] **get_source_geometry_group_name**\ (\ )

The group name of nodes that should be parsed for baking source geometry.

Only used when [source_geometry_mode<class_NavigationPolygon_property_source_geometry_mode>] is [SOURCE_GEOMETRY_GROUPS_WITH_CHILDREN<class_NavigationPolygon_constant_SOURCE_GEOMETRY_GROUPS_WITH_CHILDREN>] or [SOURCE_GEOMETRY_GROUPS_EXPLICIT<class_NavigationPolygon_constant_SOURCE_GEOMETRY_GROUPS_EXPLICIT>].


----



[SourceGeometryMode<enum_NavigationPolygon_SourceGeometryMode>] **source_geometry_mode** = `0` [🔗<class_NavigationPolygon_property_source_geometry_mode>]


- |void| **set_source_geometry_mode**\ (\ value\: [SourceGeometryMode<enum_NavigationPolygon_SourceGeometryMode>]\ )
- [SourceGeometryMode<enum_NavigationPolygon_SourceGeometryMode>] **get_source_geometry_mode**\ (\ )

The source of the geometry used when baking.


----


## Method Descriptions



|void| **add_outline**\ (\ outline\: [PackedVector2Array<class_PackedVector2Array>]\ ) [🔗<class_NavigationPolygon_method_add_outline>]

Appends a [PackedVector2Array<class_PackedVector2Array>] that contains the vertices of an outline to the internal array that contains all the outlines.


----



|void| **add_outline_at_index**\ (\ outline\: [PackedVector2Array<class_PackedVector2Array>], index\: [int<class_int>]\ ) [🔗<class_NavigationPolygon_method_add_outline_at_index>]

Adds a [PackedVector2Array<class_PackedVector2Array>] that contains the vertices of an outline to the internal array that contains all the outlines at a fixed position.


----



|void| **add_polygon**\ (\ polygon\: [PackedInt32Array<class_PackedInt32Array>]\ ) [🔗<class_NavigationPolygon_method_add_polygon>]

Adds a polygon using the indices of the vertices you get when calling [get_vertices()<class_NavigationPolygon_method_get_vertices>].


----



|void| **clear**\ (\ ) [🔗<class_NavigationPolygon_method_clear>]

Clears the internal arrays for vertices and polygon indices.


----



|void| **clear_outlines**\ (\ ) [🔗<class_NavigationPolygon_method_clear_outlines>]

Clears the array of the outlines, but it doesn't clear the vertices and the polygons that were created by them.


----



|void| **clear_polygons**\ (\ ) [🔗<class_NavigationPolygon_method_clear_polygons>]

Clears the array of polygons, but it doesn't clear the array of outlines and vertices.


----



[NavigationMesh<class_NavigationMesh>] **get_navigation_mesh**\ (\ ) [🔗<class_NavigationPolygon_method_get_navigation_mesh>]

Returns the [NavigationMesh<class_NavigationMesh>] resulting from this navigation polygon. This navigation mesh can be used to update the navigation mesh of a region with the [NavigationServer3D.region_set_navigation_mesh()<class_NavigationServer3D_method_region_set_navigation_mesh>] API directly.


----



[PackedVector2Array<class_PackedVector2Array>] **get_outline**\ (\ idx\: [int<class_int>]\ ) |const| [🔗<class_NavigationPolygon_method_get_outline>]

Returns a [PackedVector2Array<class_PackedVector2Array>] containing the vertices of an outline that was created in the editor or by script.


----



[int<class_int>] **get_outline_count**\ (\ ) |const| [🔗<class_NavigationPolygon_method_get_outline_count>]

Returns the number of outlines that were created in the editor or by script.


----



[bool<class_bool>] **get_parsed_collision_mask_value**\ (\ layer_number\: [int<class_int>]\ ) |const| [🔗<class_NavigationPolygon_method_get_parsed_collision_mask_value>]

Returns whether or not the specified layer of the [parsed_collision_mask<class_NavigationPolygon_property_parsed_collision_mask>] is enabled, given a `layer_number` between 1 and 32.


----



[PackedInt32Array<class_PackedInt32Array>] **get_polygon**\ (\ idx\: [int<class_int>]\ ) [🔗<class_NavigationPolygon_method_get_polygon>]

Returns a [PackedInt32Array<class_PackedInt32Array>] containing the indices of the vertices of a created polygon.


----



[int<class_int>] **get_polygon_count**\ (\ ) |const| [🔗<class_NavigationPolygon_method_get_polygon_count>]

Returns the count of all polygons.


----



[PackedVector2Array<class_PackedVector2Array>] **get_vertices**\ (\ ) |const| [🔗<class_NavigationPolygon_method_get_vertices>]

Returns a [PackedVector2Array<class_PackedVector2Array>] containing all the vertices being used to create the polygons.


----



|void| **make_polygons_from_outlines**\ (\ ) [🔗<class_NavigationPolygon_method_make_polygons_from_outlines>]

**Deprecated:** Use [NavigationServer2D.parse_source_geometry_data()<class_NavigationServer2D_method_parse_source_geometry_data>] and [NavigationServer2D.bake_from_source_geometry_data()<class_NavigationServer2D_method_bake_from_source_geometry_data>] instead.

Creates polygons from the outlines added in the editor or by script.


----



|void| **remove_outline**\ (\ idx\: [int<class_int>]\ ) [🔗<class_NavigationPolygon_method_remove_outline>]

Removes an outline created in the editor or by script. You have to call [make_polygons_from_outlines()<class_NavigationPolygon_method_make_polygons_from_outlines>] for the polygons to update.


----



|void| **set_outline**\ (\ idx\: [int<class_int>], outline\: [PackedVector2Array<class_PackedVector2Array>]\ ) [🔗<class_NavigationPolygon_method_set_outline>]

Changes an outline created in the editor or by script. You have to call [make_polygons_from_outlines()<class_NavigationPolygon_method_make_polygons_from_outlines>] for the polygons to update.


----



|void| **set_parsed_collision_mask_value**\ (\ layer_number\: [int<class_int>], value\: [bool<class_bool>]\ ) [🔗<class_NavigationPolygon_method_set_parsed_collision_mask_value>]

Based on `value`, enables or disables the specified layer in the [parsed_collision_mask<class_NavigationPolygon_property_parsed_collision_mask>], given a `layer_number` between 1 and 32.


----



|void| **set_vertices**\ (\ vertices\: [PackedVector2Array<class_PackedVector2Array>]\ ) [🔗<class_NavigationPolygon_method_set_vertices>]

Sets the vertices that can be then indexed to create polygons with the [add_polygon()<class_NavigationPolygon_method_add_polygon>] method.

