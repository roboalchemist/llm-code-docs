:github_url: hide



# NavigationPathQueryParameters3D

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Provides parameters for 3D navigation path queries.


## Description

By changing various properties of this object, such as the start and target position, you can configure path queries to the [NavigationServer3D<class_NavigationServer3D>].


## Tutorials

- [../tutorials/navigation/navigation_using_navigationpathqueryobjects](Using NavigationPathQueryObjects .md)


## Properties

> **TABLE**
> :widths: auto
>
> +------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+----------------------+
> | :ref:`Array<class_Array>`\[:ref:`RID<class_RID>`\]                                             | :ref:`excluded_regions<class_NavigationPathQueryParameters3D_property_excluded_regions>`                 | ``[]``               |
> +------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+----------------------+
> | :ref:`Array<class_Array>`\[:ref:`RID<class_RID>`\]                                             | :ref:`included_regions<class_NavigationPathQueryParameters3D_property_included_regions>`                 | ``[]``               |
> +------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+----------------------+
> | :ref:`RID<class_RID>`                                                                          | :ref:`map<class_NavigationPathQueryParameters3D_property_map>`                                           | ``RID()``            |
> +------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+----------------------+
> | |bitfield|\[:ref:`PathMetadataFlags<enum_NavigationPathQueryParameters3D_PathMetadataFlags>`\] | :ref:`metadata_flags<class_NavigationPathQueryParameters3D_property_metadata_flags>`                     | ``7``                |
> +------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+----------------------+
> | :ref:`int<class_int>`                                                                          | :ref:`navigation_layers<class_NavigationPathQueryParameters3D_property_navigation_layers>`               | ``1``                |
> +------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+----------------------+
> | :ref:`PathPostProcessing<enum_NavigationPathQueryParameters3D_PathPostProcessing>`             | :ref:`path_postprocessing<class_NavigationPathQueryParameters3D_property_path_postprocessing>`           | ``0``                |
> +------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+----------------------+
> | :ref:`float<class_float>`                                                                      | :ref:`path_return_max_length<class_NavigationPathQueryParameters3D_property_path_return_max_length>`     | ``0.0``              |
> +------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+----------------------+
> | :ref:`float<class_float>`                                                                      | :ref:`path_return_max_radius<class_NavigationPathQueryParameters3D_property_path_return_max_radius>`     | ``0.0``              |
> +------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+----------------------+
> | :ref:`float<class_float>`                                                                      | :ref:`path_search_max_distance<class_NavigationPathQueryParameters3D_property_path_search_max_distance>` | ``0.0``              |
> +------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+----------------------+
> | :ref:`int<class_int>`                                                                          | :ref:`path_search_max_polygons<class_NavigationPathQueryParameters3D_property_path_search_max_polygons>` | ``4096``             |
> +------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+----------------------+
> | :ref:`PathfindingAlgorithm<enum_NavigationPathQueryParameters3D_PathfindingAlgorithm>`         | :ref:`pathfinding_algorithm<class_NavigationPathQueryParameters3D_property_pathfinding_algorithm>`       | ``0``                |
> +------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+----------------------+
> | :ref:`float<class_float>`                                                                      | :ref:`simplify_epsilon<class_NavigationPathQueryParameters3D_property_simplify_epsilon>`                 | ``0.0``              |
> +------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+----------------------+
> | :ref:`bool<class_bool>`                                                                        | :ref:`simplify_path<class_NavigationPathQueryParameters3D_property_simplify_path>`                       | ``false``            |
> +------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+----------------------+
> | :ref:`Vector3<class_Vector3>`                                                                  | :ref:`start_position<class_NavigationPathQueryParameters3D_property_start_position>`                     | ``Vector3(0, 0, 0)`` |
> +------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+----------------------+
> | :ref:`Vector3<class_Vector3>`                                                                  | :ref:`target_position<class_NavigationPathQueryParameters3D_property_target_position>`                   | ``Vector3(0, 0, 0)`` |
> +------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+----------------------+
>

----


## Enumerations



enum **PathfindingAlgorithm**: [🔗<enum_NavigationPathQueryParameters3D_PathfindingAlgorithm>]



[PathfindingAlgorithm<enum_NavigationPathQueryParameters3D_PathfindingAlgorithm>] **PATHFINDING_ALGORITHM_ASTAR** = `0`

The path query uses the default A\* pathfinding algorithm.


----



enum **PathPostProcessing**: [🔗<enum_NavigationPathQueryParameters3D_PathPostProcessing>]



[PathPostProcessing<enum_NavigationPathQueryParameters3D_PathPostProcessing>] **PATH_POSTPROCESSING_CORRIDORFUNNEL** = `0`

Applies a funnel algorithm to the raw path corridor found by the pathfinding algorithm. This will result in the shortest path possible inside the path corridor. This postprocessing very much depends on the navigation mesh polygon layout and the created corridor. Especially tile- or gridbased layouts can face artificial corners with diagonal movement due to a jagged path corridor imposed by the cell shapes.



[PathPostProcessing<enum_NavigationPathQueryParameters3D_PathPostProcessing>] **PATH_POSTPROCESSING_EDGECENTERED** = `1`

Centers every path position in the middle of the traveled navigation mesh polygon edge. This creates better paths for tile- or gridbased layouts that restrict the movement to the cells center.



[PathPostProcessing<enum_NavigationPathQueryParameters3D_PathPostProcessing>] **PATH_POSTPROCESSING_NONE** = `2`

Applies no postprocessing and returns the raw path corridor as found by the pathfinding algorithm.


----



flags **PathMetadataFlags**: [🔗<enum_NavigationPathQueryParameters3D_PathMetadataFlags>]



[PathMetadataFlags<enum_NavigationPathQueryParameters3D_PathMetadataFlags>] **PATH_METADATA_INCLUDE_NONE** = `0`

Don't include any additional metadata about the returned path.



[PathMetadataFlags<enum_NavigationPathQueryParameters3D_PathMetadataFlags>] **PATH_METADATA_INCLUDE_TYPES** = `1`

Include the type of navigation primitive (region or link) that each point of the path goes through.



[PathMetadataFlags<enum_NavigationPathQueryParameters3D_PathMetadataFlags>] **PATH_METADATA_INCLUDE_RIDS** = `2`

Include the [RID<class_RID>]\ s of the regions and links that each point of the path goes through.



[PathMetadataFlags<enum_NavigationPathQueryParameters3D_PathMetadataFlags>] **PATH_METADATA_INCLUDE_OWNERS** = `4`

Include the `ObjectID`\ s of the [Object<class_Object>]\ s which manage the regions and links each point of the path goes through.



[PathMetadataFlags<enum_NavigationPathQueryParameters3D_PathMetadataFlags>] **PATH_METADATA_INCLUDE_ALL** = `7`

Include all available metadata about the returned path.


----


## Property Descriptions



[Array<class_Array>]\[[RID<class_RID>]\] **excluded_regions** = `[]` [🔗<class_NavigationPathQueryParameters3D_property_excluded_regions>]


- |void| **set_excluded_regions**\ (\ value\: [Array<class_Array>]\[[RID<class_RID>]\]\ )
- [Array<class_Array>]\[[RID<class_RID>]\] **get_excluded_regions**\ (\ )

The list of region [RID<class_RID>]\ s that will be excluded from the path query. Use [NavigationRegion3D.get_rid()<class_NavigationRegion3D_method_get_rid>] to get the [RID<class_RID>] associated with a [NavigationRegion3D<class_NavigationRegion3D>] node.

\ **Note:** The returned array is copied and any changes to it will not update the original property value. To update the value you need to modify the returned array, and then set it to the property again.


----



[Array<class_Array>]\[[RID<class_RID>]\] **included_regions** = `[]` [🔗<class_NavigationPathQueryParameters3D_property_included_regions>]


- |void| **set_included_regions**\ (\ value\: [Array<class_Array>]\[[RID<class_RID>]\]\ )
- [Array<class_Array>]\[[RID<class_RID>]\] **get_included_regions**\ (\ )

The list of region [RID<class_RID>]\ s that will be included by the path query. Use [NavigationRegion3D.get_rid()<class_NavigationRegion3D_method_get_rid>] to get the [RID<class_RID>] associated with a [NavigationRegion3D<class_NavigationRegion3D>] node. If left empty all regions are included. If a region ends up being both included and excluded at the same time it will be excluded.

\ **Note:** The returned array is copied and any changes to it will not update the original property value. To update the value you need to modify the returned array, and then set it to the property again.


----



[RID<class_RID>] **map** = `RID()` [🔗<class_NavigationPathQueryParameters3D_property_map>]


- |void| **set_map**\ (\ value\: [RID<class_RID>]\ )
- [RID<class_RID>] **get_map**\ (\ )

The navigation map [RID<class_RID>] used in the path query.


----



|bitfield|\[[PathMetadataFlags<enum_NavigationPathQueryParameters3D_PathMetadataFlags>]\] **metadata_flags** = `7` [🔗<class_NavigationPathQueryParameters3D_property_metadata_flags>]


- |void| **set_metadata_flags**\ (\ value\: |bitfield|\[[PathMetadataFlags<enum_NavigationPathQueryParameters3D_PathMetadataFlags>]\]\ )
- |bitfield|\[[PathMetadataFlags<enum_NavigationPathQueryParameters3D_PathMetadataFlags>]\] **get_metadata_flags**\ (\ )

Additional information to include with the navigation path.


----



[int<class_int>] **navigation_layers** = `1` [🔗<class_NavigationPathQueryParameters3D_property_navigation_layers>]


- |void| **set_navigation_layers**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_navigation_layers**\ (\ )

The navigation layers the query will use (as a bitmask).


----



[PathPostProcessing<enum_NavigationPathQueryParameters3D_PathPostProcessing>] **path_postprocessing** = `0` [🔗<class_NavigationPathQueryParameters3D_property_path_postprocessing>]


- |void| **set_path_postprocessing**\ (\ value\: [PathPostProcessing<enum_NavigationPathQueryParameters3D_PathPostProcessing>]\ )
- [PathPostProcessing<enum_NavigationPathQueryParameters3D_PathPostProcessing>] **get_path_postprocessing**\ (\ )

The path postprocessing applied to the raw path corridor found by the [pathfinding_algorithm<class_NavigationPathQueryParameters3D_property_pathfinding_algorithm>].


----



[float<class_float>] **path_return_max_length** = `0.0` [🔗<class_NavigationPathQueryParameters3D_property_path_return_max_length>]


- |void| **set_path_return_max_length**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_path_return_max_length**\ (\ )

The maximum allowed length of the returned path in world units. A path will be clipped when going over this length. A value of `0` or below counts as disabled.


----



[float<class_float>] **path_return_max_radius** = `0.0` [🔗<class_NavigationPathQueryParameters3D_property_path_return_max_radius>]


- |void| **set_path_return_max_radius**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_path_return_max_radius**\ (\ )

The maximum allowed radius in world units that the returned path can be from the path start. The path will be clipped when going over this radius. A value of `0` or below counts as disabled.

\ **Note:** This will perform a sphere shaped clip operation on the path with the first path position being the sphere's center position.


----



[float<class_float>] **path_search_max_distance** = `0.0` [🔗<class_NavigationPathQueryParameters3D_property_path_search_max_distance>]


- |void| **set_path_search_max_distance**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_path_search_max_distance**\ (\ )

The maximum distance a searched polygon can be away from the start polygon before the pathfinding cancels the search for a path to the (possibly unreachable or very far away) target position polygon. In this case the pathfinding resets and builds a path from the start polygon to the polygon that was found closest to the target position so far. A value of `0` or below counts as unlimited. In case of unlimited the pathfinding will search all polygons connected with the start polygon until either the target position polygon is found or all available polygon search options are exhausted.


----



[int<class_int>] **path_search_max_polygons** = `4096` [🔗<class_NavigationPathQueryParameters3D_property_path_search_max_polygons>]


- |void| **set_path_search_max_polygons**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_path_search_max_polygons**\ (\ )

The maximum number of polygons that are searched before the pathfinding cancels the search for a path to the (possibly unreachable or very far away) target position polygon. In this case the pathfinding resets and builds a path from the start polygon to the polygon that was found closest to the target position so far. A value of `0` or below counts as unlimited. In case of unlimited the pathfinding will search all polygons connected with the start polygon until either the target position polygon is found or all available polygon search options are exhausted.


----



[PathfindingAlgorithm<enum_NavigationPathQueryParameters3D_PathfindingAlgorithm>] **pathfinding_algorithm** = `0` [🔗<class_NavigationPathQueryParameters3D_property_pathfinding_algorithm>]


- |void| **set_pathfinding_algorithm**\ (\ value\: [PathfindingAlgorithm<enum_NavigationPathQueryParameters3D_PathfindingAlgorithm>]\ )
- [PathfindingAlgorithm<enum_NavigationPathQueryParameters3D_PathfindingAlgorithm>] **get_pathfinding_algorithm**\ (\ )

The pathfinding algorithm used in the path query.


----



[float<class_float>] **simplify_epsilon** = `0.0` [🔗<class_NavigationPathQueryParameters3D_property_simplify_epsilon>]


- |void| **set_simplify_epsilon**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_simplify_epsilon**\ (\ )

The path simplification amount in worlds units.


----



[bool<class_bool>] **simplify_path** = `false` [🔗<class_NavigationPathQueryParameters3D_property_simplify_path>]


- |void| **set_simplify_path**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_simplify_path**\ (\ )

If `true` a simplified version of the path will be returned with less critical path points removed. The simplification amount is controlled by [simplify_epsilon<class_NavigationPathQueryParameters3D_property_simplify_epsilon>]. The simplification uses a variant of Ramer-Douglas-Peucker algorithm for curve point decimation.

Path simplification can be helpful to mitigate various path following issues that can arise with certain agent types and script behaviors. E.g. "steering" agents or avoidance in "open fields".


----



[Vector3<class_Vector3>] **start_position** = `Vector3(0, 0, 0)` [🔗<class_NavigationPathQueryParameters3D_property_start_position>]


- |void| **set_start_position**\ (\ value\: [Vector3<class_Vector3>]\ )
- [Vector3<class_Vector3>] **get_start_position**\ (\ )

The pathfinding start position in global coordinates.


----



[Vector3<class_Vector3>] **target_position** = `Vector3(0, 0, 0)` [🔗<class_NavigationPathQueryParameters3D_property_target_position>]


- |void| **set_target_position**\ (\ value\: [Vector3<class_Vector3>]\ )
- [Vector3<class_Vector3>] **get_target_position**\ (\ )

The pathfinding target position in global coordinates.

