:github_url: hide



# NavigationMeshSourceGeometryData2D

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Container for parsed source geometry data used in navigation mesh baking.


## Description

Container for parsed source geometry data used in navigation mesh baking.


## Methods

> **TABLE**
> :widths: auto
>
> +----------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                           | :ref:`add_obstruction_outline<class_NavigationMeshSourceGeometryData2D_method_add_obstruction_outline>`\ (\ shape_outline\: :ref:`PackedVector2Array<class_PackedVector2Array>`\ )                                             |
> +----------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                           | :ref:`add_projected_obstruction<class_NavigationMeshSourceGeometryData2D_method_add_projected_obstruction>`\ (\ vertices\: :ref:`PackedVector2Array<class_PackedVector2Array>`, carve\: :ref:`bool<class_bool>`\ )             |
> +----------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                           | :ref:`add_traversable_outline<class_NavigationMeshSourceGeometryData2D_method_add_traversable_outline>`\ (\ shape_outline\: :ref:`PackedVector2Array<class_PackedVector2Array>`\ )                                             |
> +----------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                           | :ref:`append_obstruction_outlines<class_NavigationMeshSourceGeometryData2D_method_append_obstruction_outlines>`\ (\ obstruction_outlines\: :ref:`Array<class_Array>`\[:ref:`PackedVector2Array<class_PackedVector2Array>`\]\ ) |
> +----------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                           | :ref:`append_traversable_outlines<class_NavigationMeshSourceGeometryData2D_method_append_traversable_outlines>`\ (\ traversable_outlines\: :ref:`Array<class_Array>`\[:ref:`PackedVector2Array<class_PackedVector2Array>`\]\ ) |
> +----------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                           | :ref:`clear<class_NavigationMeshSourceGeometryData2D_method_clear>`\ (\ )                                                                                                                                                      |
> +----------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                           | :ref:`clear_projected_obstructions<class_NavigationMeshSourceGeometryData2D_method_clear_projected_obstructions>`\ (\ )                                                                                                        |
> +----------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Rect2<class_Rect2>`                                                        | :ref:`get_bounds<class_NavigationMeshSourceGeometryData2D_method_get_bounds>`\ (\ )                                                                                                                                            |
> +----------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`PackedVector2Array<class_PackedVector2Array>`\] | :ref:`get_obstruction_outlines<class_NavigationMeshSourceGeometryData2D_method_get_obstruction_outlines>`\ (\ ) |const|                                                                                                        |
> +----------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`                                                        | :ref:`get_projected_obstructions<class_NavigationMeshSourceGeometryData2D_method_get_projected_obstructions>`\ (\ ) |const|                                                                                                    |
> +----------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`PackedVector2Array<class_PackedVector2Array>`\] | :ref:`get_traversable_outlines<class_NavigationMeshSourceGeometryData2D_method_get_traversable_outlines>`\ (\ ) |const|                                                                                                        |
> +----------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                                          | :ref:`has_data<class_NavigationMeshSourceGeometryData2D_method_has_data>`\ (\ )                                                                                                                                                |
> +----------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                           | :ref:`merge<class_NavigationMeshSourceGeometryData2D_method_merge>`\ (\ other_geometry\: :ref:`NavigationMeshSourceGeometryData2D<class_NavigationMeshSourceGeometryData2D>`\ )                                                |
> +----------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                           | :ref:`set_obstruction_outlines<class_NavigationMeshSourceGeometryData2D_method_set_obstruction_outlines>`\ (\ obstruction_outlines\: :ref:`Array<class_Array>`\[:ref:`PackedVector2Array<class_PackedVector2Array>`\]\ )       |
> +----------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                           | :ref:`set_projected_obstructions<class_NavigationMeshSourceGeometryData2D_method_set_projected_obstructions>`\ (\ projected_obstructions\: :ref:`Array<class_Array>`\ )                                                        |
> +----------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                           | :ref:`set_traversable_outlines<class_NavigationMeshSourceGeometryData2D_method_set_traversable_outlines>`\ (\ traversable_outlines\: :ref:`Array<class_Array>`\[:ref:`PackedVector2Array<class_PackedVector2Array>`\]\ )       |
> +----------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



|void| **add_obstruction_outline**\ (\ shape_outline\: [PackedVector2Array<class_PackedVector2Array>]\ ) [🔗<class_NavigationMeshSourceGeometryData2D_method_add_obstruction_outline>]

Adds the outline points of a shape as obstructed area.


----



|void| **add_projected_obstruction**\ (\ vertices\: [PackedVector2Array<class_PackedVector2Array>], carve\: [bool<class_bool>]\ ) [🔗<class_NavigationMeshSourceGeometryData2D_method_add_projected_obstruction>]

Adds a projected obstruction shape to the source geometry. If `carve` is `true` the carved shape will not be affected by additional offsets (e.g. agent radius) of the navigation mesh baking process.


----



|void| **add_traversable_outline**\ (\ shape_outline\: [PackedVector2Array<class_PackedVector2Array>]\ ) [🔗<class_NavigationMeshSourceGeometryData2D_method_add_traversable_outline>]

Adds the outline points of a shape as traversable area.


----



|void| **append_obstruction_outlines**\ (\ obstruction_outlines\: [Array<class_Array>]\[[PackedVector2Array<class_PackedVector2Array>]\]\ ) [🔗<class_NavigationMeshSourceGeometryData2D_method_append_obstruction_outlines>]

Appends another array of `obstruction_outlines` at the end of the existing obstruction outlines array.


----



|void| **append_traversable_outlines**\ (\ traversable_outlines\: [Array<class_Array>]\[[PackedVector2Array<class_PackedVector2Array>]\]\ ) [🔗<class_NavigationMeshSourceGeometryData2D_method_append_traversable_outlines>]

Appends another array of `traversable_outlines` at the end of the existing traversable outlines array.


----



|void| **clear**\ (\ ) [🔗<class_NavigationMeshSourceGeometryData2D_method_clear>]

Clears the internal data.


----



|void| **clear_projected_obstructions**\ (\ ) [🔗<class_NavigationMeshSourceGeometryData2D_method_clear_projected_obstructions>]

Clears all projected obstructions.


----



[Rect2<class_Rect2>] **get_bounds**\ (\ ) [🔗<class_NavigationMeshSourceGeometryData2D_method_get_bounds>]

Returns an axis-aligned bounding box that covers all the stored geometry data. The bounds are calculated when calling this function with the result cached until further geometry changes are made.


----



[Array<class_Array>]\[[PackedVector2Array<class_PackedVector2Array>]\] **get_obstruction_outlines**\ (\ ) |const| [🔗<class_NavigationMeshSourceGeometryData2D_method_get_obstruction_outlines>]

Returns all the obstructed area outlines arrays.


----



[Array<class_Array>] **get_projected_obstructions**\ (\ ) |const| [🔗<class_NavigationMeshSourceGeometryData2D_method_get_projected_obstructions>]

Returns the projected obstructions as an [Array<class_Array>] of dictionaries. Each [Dictionary<class_Dictionary>] contains the following entries:

- `vertices` - A [PackedFloat32Array<class_PackedFloat32Array>] that defines the outline points of the projected shape.

- `carve` - A [bool<class_bool>] that defines how the projected shape affects the navigation mesh baking. If `true` the projected shape will not be affected by addition offsets, e.g. agent radius.


----



[Array<class_Array>]\[[PackedVector2Array<class_PackedVector2Array>]\] **get_traversable_outlines**\ (\ ) |const| [🔗<class_NavigationMeshSourceGeometryData2D_method_get_traversable_outlines>]

Returns all the traversable area outlines arrays.


----



[bool<class_bool>] **has_data**\ (\ ) [🔗<class_NavigationMeshSourceGeometryData2D_method_has_data>]

Returns `true` when parsed source geometry data exists.


----



|void| **merge**\ (\ other_geometry\: [NavigationMeshSourceGeometryData2D<class_NavigationMeshSourceGeometryData2D>]\ ) [🔗<class_NavigationMeshSourceGeometryData2D_method_merge>]

Adds the geometry data of another **NavigationMeshSourceGeometryData2D** to the navigation mesh baking data.


----



|void| **set_obstruction_outlines**\ (\ obstruction_outlines\: [Array<class_Array>]\[[PackedVector2Array<class_PackedVector2Array>]\]\ ) [🔗<class_NavigationMeshSourceGeometryData2D_method_set_obstruction_outlines>]

Sets all the obstructed area outlines arrays.


----



|void| **set_projected_obstructions**\ (\ projected_obstructions\: [Array<class_Array>]\ ) [🔗<class_NavigationMeshSourceGeometryData2D_method_set_projected_obstructions>]

Sets the projected obstructions with an Array of Dictionaries with the following key value pairs:


> **TABS**
>

    "vertices" : PackedFloat32Array
    "carve" : bool




----



|void| **set_traversable_outlines**\ (\ traversable_outlines\: [Array<class_Array>]\[[PackedVector2Array<class_PackedVector2Array>]\]\ ) [🔗<class_NavigationMeshSourceGeometryData2D_method_set_traversable_outlines>]

Sets all the traversable area outlines arrays.

