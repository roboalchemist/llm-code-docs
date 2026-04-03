:github_url: hide



# NavigationPathQueryResult3D

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Represents the result of a 3D pathfinding query.


## Description

This class stores the result of a 3D navigation path query from the [NavigationServer3D<class_NavigationServer3D>].


## Tutorials

- [../tutorials/navigation/navigation_using_navigationpathqueryobjects](Using NavigationPathQueryObjects .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------+----------------------------------------------------------------------------------+--------------------------+
> | :ref:`PackedVector3Array<class_PackedVector3Array>` | :ref:`path<class_NavigationPathQueryResult3D_property_path>`                     | ``PackedVector3Array()`` |
> +-----------------------------------------------------+----------------------------------------------------------------------------------+--------------------------+
> | :ref:`float<class_float>`                           | :ref:`path_length<class_NavigationPathQueryResult3D_property_path_length>`       | ``0.0``                  |
> +-----------------------------------------------------+----------------------------------------------------------------------------------+--------------------------+
> | :ref:`PackedInt64Array<class_PackedInt64Array>`     | :ref:`path_owner_ids<class_NavigationPathQueryResult3D_property_path_owner_ids>` | ``PackedInt64Array()``   |
> +-----------------------------------------------------+----------------------------------------------------------------------------------+--------------------------+
> | :ref:`Array<class_Array>`\[:ref:`RID<class_RID>`\]  | :ref:`path_rids<class_NavigationPathQueryResult3D_property_path_rids>`           | ``[]``                   |
> +-----------------------------------------------------+----------------------------------------------------------------------------------+--------------------------+
> | :ref:`PackedInt32Array<class_PackedInt32Array>`     | :ref:`path_types<class_NavigationPathQueryResult3D_property_path_types>`         | ``PackedInt32Array()``   |
> +-----------------------------------------------------+----------------------------------------------------------------------------------+--------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +--------+--------------------------------------------------------------------+
> | |void| | :ref:`reset<class_NavigationPathQueryResult3D_method_reset>`\ (\ ) |
> +--------+--------------------------------------------------------------------+
>

----


## Enumerations



enum **PathSegmentType**: [🔗<enum_NavigationPathQueryResult3D_PathSegmentType>]



[PathSegmentType<enum_NavigationPathQueryResult3D_PathSegmentType>] **PATH_SEGMENT_TYPE_REGION** = `0`

This segment of the path goes through a region.



[PathSegmentType<enum_NavigationPathQueryResult3D_PathSegmentType>] **PATH_SEGMENT_TYPE_LINK** = `1`

This segment of the path goes through a link.


----


## Property Descriptions



[PackedVector3Array<class_PackedVector3Array>] **path** = `PackedVector3Array()` [🔗<class_NavigationPathQueryResult3D_property_path>]


- |void| **set_path**\ (\ value\: [PackedVector3Array<class_PackedVector3Array>]\ )
- [PackedVector3Array<class_PackedVector3Array>] **get_path**\ (\ )

The resulting path array from the navigation query. All path array positions are in global coordinates. Without customized query parameters this is the same path as returned by [NavigationServer3D.map_get_path()<class_NavigationServer3D_method_map_get_path>].

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedVector3Array<class_PackedVector3Array>] for more details.


----



[float<class_float>] **path_length** = `0.0` [🔗<class_NavigationPathQueryResult3D_property_path_length>]


- |void| **set_path_length**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_path_length**\ (\ )

Returns the length of the path.


----



[PackedInt64Array<class_PackedInt64Array>] **path_owner_ids** = `PackedInt64Array()` [🔗<class_NavigationPathQueryResult3D_property_path_owner_ids>]


- |void| **set_path_owner_ids**\ (\ value\: [PackedInt64Array<class_PackedInt64Array>]\ )
- [PackedInt64Array<class_PackedInt64Array>] **get_path_owner_ids**\ (\ )

The `ObjectID`\ s of the [Object<class_Object>]\ s which manage the regions and links each point of the path goes through.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt64Array<class_PackedInt64Array>] for more details.


----



[Array<class_Array>]\[[RID<class_RID>]\] **path_rids** = `[]` [🔗<class_NavigationPathQueryResult3D_property_path_rids>]


- |void| **set_path_rids**\ (\ value\: [Array<class_Array>]\[[RID<class_RID>]\]\ )
- [Array<class_Array>]\[[RID<class_RID>]\] **get_path_rids**\ (\ )

The [RID<class_RID>]\ s of the regions and links that each point of the path goes through.


----



[PackedInt32Array<class_PackedInt32Array>] **path_types** = `PackedInt32Array()` [🔗<class_NavigationPathQueryResult3D_property_path_types>]


- |void| **set_path_types**\ (\ value\: [PackedInt32Array<class_PackedInt32Array>]\ )
- [PackedInt32Array<class_PackedInt32Array>] **get_path_types**\ (\ )

The type of navigation primitive (region or link) that each point of the path goes through.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array<class_PackedInt32Array>] for more details.


----


## Method Descriptions



|void| **reset**\ (\ ) [🔗<class_NavigationPathQueryResult3D_method_reset>]

Reset the result object to its initial state. This is useful to reuse the object across multiple queries.

