:github_url: hide



# Geometry2D

**Inherits:** [Object<class_Object>]

Provides methods for some common 2D geometric operations.


## Description

Provides a set of helper functions to create geometric shapes, compute intersections between shapes, and process various other geometric operations in 2D.


## Methods

> **TABLE**
> :widths: auto
>
> +----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`Vector2i<class_Vector2i>`\]                     | :ref:`bresenham_line<class_Geometry2D_method_bresenham_line>`\ (\ from\: :ref:`Vector2i<class_Vector2i>`, to\: :ref:`Vector2i<class_Vector2i>`\ )                                                                                                                                                           |
> +----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`PackedVector2Array<class_PackedVector2Array>`\] | :ref:`clip_polygons<class_Geometry2D_method_clip_polygons>`\ (\ polygon_a\: :ref:`PackedVector2Array<class_PackedVector2Array>`, polygon_b\: :ref:`PackedVector2Array<class_PackedVector2Array>`\ )                                                                                                         |
> +----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`PackedVector2Array<class_PackedVector2Array>`\] | :ref:`clip_polyline_with_polygon<class_Geometry2D_method_clip_polyline_with_polygon>`\ (\ polyline\: :ref:`PackedVector2Array<class_PackedVector2Array>`, polygon\: :ref:`PackedVector2Array<class_PackedVector2Array>`\ )                                                                                  |
> +----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedVector2Array<class_PackedVector2Array>`                              | :ref:`convex_hull<class_Geometry2D_method_convex_hull>`\ (\ points\: :ref:`PackedVector2Array<class_PackedVector2Array>`\ )                                                                                                                                                                                 |
> +----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`PackedVector2Array<class_PackedVector2Array>`\] | :ref:`decompose_polygon_in_convex<class_Geometry2D_method_decompose_polygon_in_convex>`\ (\ polygon\: :ref:`PackedVector2Array<class_PackedVector2Array>`\ )                                                                                                                                                |
> +----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`PackedVector2Array<class_PackedVector2Array>`\] | :ref:`exclude_polygons<class_Geometry2D_method_exclude_polygons>`\ (\ polygon_a\: :ref:`PackedVector2Array<class_PackedVector2Array>`, polygon_b\: :ref:`PackedVector2Array<class_PackedVector2Array>`\ )                                                                                                   |
> +----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>`                                                    | :ref:`get_closest_point_to_segment<class_Geometry2D_method_get_closest_point_to_segment>`\ (\ point\: :ref:`Vector2<class_Vector2>`, s1\: :ref:`Vector2<class_Vector2>`, s2\: :ref:`Vector2<class_Vector2>`\ )                                                                                              |
> +----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>`                                                    | :ref:`get_closest_point_to_segment_uncapped<class_Geometry2D_method_get_closest_point_to_segment_uncapped>`\ (\ point\: :ref:`Vector2<class_Vector2>`, s1\: :ref:`Vector2<class_Vector2>`, s2\: :ref:`Vector2<class_Vector2>`\ )                                                                            |
> +----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedVector2Array<class_PackedVector2Array>`                              | :ref:`get_closest_points_between_segments<class_Geometry2D_method_get_closest_points_between_segments>`\ (\ p1\: :ref:`Vector2<class_Vector2>`, q1\: :ref:`Vector2<class_Vector2>`, p2\: :ref:`Vector2<class_Vector2>`, q2\: :ref:`Vector2<class_Vector2>`\ )                                               |
> +----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`PackedVector2Array<class_PackedVector2Array>`\] | :ref:`intersect_polygons<class_Geometry2D_method_intersect_polygons>`\ (\ polygon_a\: :ref:`PackedVector2Array<class_PackedVector2Array>`, polygon_b\: :ref:`PackedVector2Array<class_PackedVector2Array>`\ )                                                                                               |
> +----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`PackedVector2Array<class_PackedVector2Array>`\] | :ref:`intersect_polyline_with_polygon<class_Geometry2D_method_intersect_polyline_with_polygon>`\ (\ polyline\: :ref:`PackedVector2Array<class_PackedVector2Array>`, polygon\: :ref:`PackedVector2Array<class_PackedVector2Array>`\ )                                                                        |
> +----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                                          | :ref:`is_point_in_circle<class_Geometry2D_method_is_point_in_circle>`\ (\ point\: :ref:`Vector2<class_Vector2>`, circle_position\: :ref:`Vector2<class_Vector2>`, circle_radius\: :ref:`float<class_float>`\ )                                                                                              |
> +----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                                          | :ref:`is_point_in_polygon<class_Geometry2D_method_is_point_in_polygon>`\ (\ point\: :ref:`Vector2<class_Vector2>`, polygon\: :ref:`PackedVector2Array<class_PackedVector2Array>`\ )                                                                                                                         |
> +----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                                          | :ref:`is_polygon_clockwise<class_Geometry2D_method_is_polygon_clockwise>`\ (\ polygon\: :ref:`PackedVector2Array<class_PackedVector2Array>`\ )                                                                                                                                                              |
> +----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>`                                                    | :ref:`line_intersects_line<class_Geometry2D_method_line_intersects_line>`\ (\ from_a\: :ref:`Vector2<class_Vector2>`, dir_a\: :ref:`Vector2<class_Vector2>`, from_b\: :ref:`Vector2<class_Vector2>`, dir_b\: :ref:`Vector2<class_Vector2>`\ )                                                               |
> +----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Dictionary<class_Dictionary>`                                              | :ref:`make_atlas<class_Geometry2D_method_make_atlas>`\ (\ sizes\: :ref:`PackedVector2Array<class_PackedVector2Array>`\ )                                                                                                                                                                                    |
> +----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`PackedVector2Array<class_PackedVector2Array>`\] | :ref:`merge_polygons<class_Geometry2D_method_merge_polygons>`\ (\ polygon_a\: :ref:`PackedVector2Array<class_PackedVector2Array>`, polygon_b\: :ref:`PackedVector2Array<class_PackedVector2Array>`\ )                                                                                                       |
> +----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`PackedVector2Array<class_PackedVector2Array>`\] | :ref:`offset_polygon<class_Geometry2D_method_offset_polygon>`\ (\ polygon\: :ref:`PackedVector2Array<class_PackedVector2Array>`, delta\: :ref:`float<class_float>`, join_type\: :ref:`PolyJoinType<enum_Geometry2D_PolyJoinType>` = 0\ )                                                                    |
> +----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`PackedVector2Array<class_PackedVector2Array>`\] | :ref:`offset_polyline<class_Geometry2D_method_offset_polyline>`\ (\ polyline\: :ref:`PackedVector2Array<class_PackedVector2Array>`, delta\: :ref:`float<class_float>`, join_type\: :ref:`PolyJoinType<enum_Geometry2D_PolyJoinType>` = 0, end_type\: :ref:`PolyEndType<enum_Geometry2D_PolyEndType>` = 3\ ) |
> +----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                                          | :ref:`point_is_inside_triangle<class_Geometry2D_method_point_is_inside_triangle>`\ (\ point\: :ref:`Vector2<class_Vector2>`, a\: :ref:`Vector2<class_Vector2>`, b\: :ref:`Vector2<class_Vector2>`, c\: :ref:`Vector2<class_Vector2>`\ ) |const|                                                             |
> +----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                                        | :ref:`segment_intersects_circle<class_Geometry2D_method_segment_intersects_circle>`\ (\ segment_from\: :ref:`Vector2<class_Vector2>`, segment_to\: :ref:`Vector2<class_Vector2>`, circle_position\: :ref:`Vector2<class_Vector2>`, circle_radius\: :ref:`float<class_float>`\ )                             |
> +----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>`                                                    | :ref:`segment_intersects_segment<class_Geometry2D_method_segment_intersects_segment>`\ (\ from_a\: :ref:`Vector2<class_Vector2>`, to_a\: :ref:`Vector2<class_Vector2>`, from_b\: :ref:`Vector2<class_Vector2>`, to_b\: :ref:`Vector2<class_Vector2>`\ )                                                     |
> +----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedInt32Array<class_PackedInt32Array>`                                  | :ref:`triangulate_delaunay<class_Geometry2D_method_triangulate_delaunay>`\ (\ points\: :ref:`PackedVector2Array<class_PackedVector2Array>`\ )                                                                                                                                                               |
> +----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedInt32Array<class_PackedInt32Array>`                                  | :ref:`triangulate_polygon<class_Geometry2D_method_triangulate_polygon>`\ (\ polygon\: :ref:`PackedVector2Array<class_PackedVector2Array>`\ )                                                                                                                                                                |
> +----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **PolyBooleanOperation**: [🔗<enum_Geometry2D_PolyBooleanOperation>]



[PolyBooleanOperation<enum_Geometry2D_PolyBooleanOperation>] **OPERATION_UNION** = `0`

Create regions where either subject or clip polygons (or both) are filled.



[PolyBooleanOperation<enum_Geometry2D_PolyBooleanOperation>] **OPERATION_DIFFERENCE** = `1`

Create regions where subject polygons are filled except where clip polygons are filled.



[PolyBooleanOperation<enum_Geometry2D_PolyBooleanOperation>] **OPERATION_INTERSECTION** = `2`

Create regions where both subject and clip polygons are filled.



[PolyBooleanOperation<enum_Geometry2D_PolyBooleanOperation>] **OPERATION_XOR** = `3`

Create regions where either subject or clip polygons are filled but not where both are filled.


----



enum **PolyJoinType**: [🔗<enum_Geometry2D_PolyJoinType>]



[PolyJoinType<enum_Geometry2D_PolyJoinType>] **JOIN_SQUARE** = `0`

Squaring is applied uniformally at all convex edge joins at `1 * delta`.



[PolyJoinType<enum_Geometry2D_PolyJoinType>] **JOIN_ROUND** = `1`

While flattened paths can never perfectly trace an arc, they are approximated by a series of arc chords.



[PolyJoinType<enum_Geometry2D_PolyJoinType>] **JOIN_MITER** = `2`

There's a necessary limit to mitered joins since offsetting edges that join at very acute angles will produce excessively long and narrow "spikes". For any given edge join, when miter offsetting would exceed that maximum distance, "square" joining is applied.


----



enum **PolyEndType**: [🔗<enum_Geometry2D_PolyEndType>]



[PolyEndType<enum_Geometry2D_PolyEndType>] **END_POLYGON** = `0`

Endpoints are joined using the [PolyJoinType<enum_Geometry2D_PolyJoinType>] value and the path filled as a polygon.



[PolyEndType<enum_Geometry2D_PolyEndType>] **END_JOINED** = `1`

Endpoints are joined using the [PolyJoinType<enum_Geometry2D_PolyJoinType>] value and the path filled as a polyline.



[PolyEndType<enum_Geometry2D_PolyEndType>] **END_BUTT** = `2`

Endpoints are squared off with no extension.



[PolyEndType<enum_Geometry2D_PolyEndType>] **END_SQUARE** = `3`

Endpoints are squared off and extended by `delta` units.



[PolyEndType<enum_Geometry2D_PolyEndType>] **END_ROUND** = `4`

Endpoints are rounded off and extended by `delta` units.


----


## Method Descriptions



[Array<class_Array>]\[[Vector2i<class_Vector2i>]\] **bresenham_line**\ (\ from\: [Vector2i<class_Vector2i>], to\: [Vector2i<class_Vector2i>]\ ) [🔗<class_Geometry2D_method_bresenham_line>]

Returns the [Bresenham line ](https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm)_ between the `from` and `to` points. A Bresenham line is a series of pixels that draws a line and is always 1-pixel thick on every row and column of the drawing (never more, never less).

Example code to draw a line between two [Marker2D<class_Marker2D>] nodes using a series of [CanvasItem.draw_rect()<class_CanvasItem_method_draw_rect>] calls:

::

    func _draw():
        for pixel in Geometry2D.bresenham_line($MarkerA.position, $MarkerB.position):
            draw_rect(Rect2(pixel, Vector2.ONE), Color.WHITE)


----



[Array<class_Array>]\[[PackedVector2Array<class_PackedVector2Array>]\] **clip_polygons**\ (\ polygon_a\: [PackedVector2Array<class_PackedVector2Array>], polygon_b\: [PackedVector2Array<class_PackedVector2Array>]\ ) [🔗<class_Geometry2D_method_clip_polygons>]

Clips `polygon_a` against `polygon_b` and returns an array of clipped polygons. This performs [OPERATION_DIFFERENCE<class_Geometry2D_constant_OPERATION_DIFFERENCE>] between polygons. Returns an empty array if `polygon_b` completely overlaps `polygon_a`.

If `polygon_b` is enclosed by `polygon_a`, returns an outer polygon (boundary) and inner polygon (hole) which could be distinguished by calling [is_polygon_clockwise()<class_Geometry2D_method_is_polygon_clockwise>].


----



[Array<class_Array>]\[[PackedVector2Array<class_PackedVector2Array>]\] **clip_polyline_with_polygon**\ (\ polyline\: [PackedVector2Array<class_PackedVector2Array>], polygon\: [PackedVector2Array<class_PackedVector2Array>]\ ) [🔗<class_Geometry2D_method_clip_polyline_with_polygon>]

Clips `polyline` against `polygon` and returns an array of clipped polylines. This performs [OPERATION_DIFFERENCE<class_Geometry2D_constant_OPERATION_DIFFERENCE>] between the polyline and the polygon. This operation can be thought of as cutting a line with a closed shape.


----



[PackedVector2Array<class_PackedVector2Array>] **convex_hull**\ (\ points\: [PackedVector2Array<class_PackedVector2Array>]\ ) [🔗<class_Geometry2D_method_convex_hull>]

Given an array of [Vector2<class_Vector2>]\ s, returns the convex hull as a list of points in counterclockwise order. The last point is the same as the first one.


----



[Array<class_Array>]\[[PackedVector2Array<class_PackedVector2Array>]\] **decompose_polygon_in_convex**\ (\ polygon\: [PackedVector2Array<class_PackedVector2Array>]\ ) [🔗<class_Geometry2D_method_decompose_polygon_in_convex>]

Decomposes the `polygon` into multiple convex hulls and returns an array of [PackedVector2Array<class_PackedVector2Array>].


----



[Array<class_Array>]\[[PackedVector2Array<class_PackedVector2Array>]\] **exclude_polygons**\ (\ polygon_a\: [PackedVector2Array<class_PackedVector2Array>], polygon_b\: [PackedVector2Array<class_PackedVector2Array>]\ ) [🔗<class_Geometry2D_method_exclude_polygons>]

Mutually excludes common area defined by intersection of `polygon_a` and `polygon_b` (see [intersect_polygons()<class_Geometry2D_method_intersect_polygons>]) and returns an array of excluded polygons. This performs [OPERATION_XOR<class_Geometry2D_constant_OPERATION_XOR>] between polygons. In other words, returns all but common area between polygons.

The operation may result in an outer polygon (boundary) and inner polygon (hole) produced which could be distinguished by calling [is_polygon_clockwise()<class_Geometry2D_method_is_polygon_clockwise>].


----



[Vector2<class_Vector2>] **get_closest_point_to_segment**\ (\ point\: [Vector2<class_Vector2>], s1\: [Vector2<class_Vector2>], s2\: [Vector2<class_Vector2>]\ ) [🔗<class_Geometry2D_method_get_closest_point_to_segment>]

Returns the 2D point on the 2D segment (`s1`, `s2`) that is closest to `point`. The returned point will always be inside the specified segment.


----



[Vector2<class_Vector2>] **get_closest_point_to_segment_uncapped**\ (\ point\: [Vector2<class_Vector2>], s1\: [Vector2<class_Vector2>], s2\: [Vector2<class_Vector2>]\ ) [🔗<class_Geometry2D_method_get_closest_point_to_segment_uncapped>]

Returns the 2D point on the 2D line defined by (`s1`, `s2`) that is closest to `point`. The returned point can be inside the segment (`s1`, `s2`) or outside of it, i.e. somewhere on the line extending from the segment.


----



[PackedVector2Array<class_PackedVector2Array>] **get_closest_points_between_segments**\ (\ p1\: [Vector2<class_Vector2>], q1\: [Vector2<class_Vector2>], p2\: [Vector2<class_Vector2>], q2\: [Vector2<class_Vector2>]\ ) [🔗<class_Geometry2D_method_get_closest_points_between_segments>]

Given the two 2D segments (`p1`, `q1`) and (`p2`, `q2`), finds those two points on the two segments that are closest to each other. Returns a [PackedVector2Array<class_PackedVector2Array>] that contains this point on (`p1`, `q1`) as well the accompanying point on (`p2`, `q2`).


----



[Array<class_Array>]\[[PackedVector2Array<class_PackedVector2Array>]\] **intersect_polygons**\ (\ polygon_a\: [PackedVector2Array<class_PackedVector2Array>], polygon_b\: [PackedVector2Array<class_PackedVector2Array>]\ ) [🔗<class_Geometry2D_method_intersect_polygons>]

Intersects `polygon_a` with `polygon_b` and returns an array of intersected polygons. This performs [OPERATION_INTERSECTION<class_Geometry2D_constant_OPERATION_INTERSECTION>] between polygons. In other words, returns common area shared by polygons. Returns an empty array if no intersection occurs.

The operation may result in an outer polygon (boundary) and inner polygon (hole) produced which could be distinguished by calling [is_polygon_clockwise()<class_Geometry2D_method_is_polygon_clockwise>].


----



[Array<class_Array>]\[[PackedVector2Array<class_PackedVector2Array>]\] **intersect_polyline_with_polygon**\ (\ polyline\: [PackedVector2Array<class_PackedVector2Array>], polygon\: [PackedVector2Array<class_PackedVector2Array>]\ ) [🔗<class_Geometry2D_method_intersect_polyline_with_polygon>]

Intersects `polyline` with `polygon` and returns an array of intersected polylines. This performs [OPERATION_INTERSECTION<class_Geometry2D_constant_OPERATION_INTERSECTION>] between the polyline and the polygon. This operation can be thought of as chopping a line with a closed shape.


----



[bool<class_bool>] **is_point_in_circle**\ (\ point\: [Vector2<class_Vector2>], circle_position\: [Vector2<class_Vector2>], circle_radius\: [float<class_float>]\ ) [🔗<class_Geometry2D_method_is_point_in_circle>]

Returns `true` if `point` is inside the circle or if it's located exactly *on* the circle's boundary, otherwise returns `false`.


----



[bool<class_bool>] **is_point_in_polygon**\ (\ point\: [Vector2<class_Vector2>], polygon\: [PackedVector2Array<class_PackedVector2Array>]\ ) [🔗<class_Geometry2D_method_is_point_in_polygon>]

Returns `true` if `point` is inside `polygon` or if it's located exactly *on* polygon's boundary, otherwise returns `false`.


----



[bool<class_bool>] **is_polygon_clockwise**\ (\ polygon\: [PackedVector2Array<class_PackedVector2Array>]\ ) [🔗<class_Geometry2D_method_is_polygon_clockwise>]

Returns `true` if `polygon`'s vertices are ordered in clockwise order, otherwise returns `false`.

\ **Note:** Assumes a Cartesian coordinate system where `+x` is right and `+y` is up. If using screen coordinates (`+y` is down), the result will need to be flipped (i.e. a `true` result will indicate counter-clockwise).


----



[Variant<class_Variant>] **line_intersects_line**\ (\ from_a\: [Vector2<class_Vector2>], dir_a\: [Vector2<class_Vector2>], from_b\: [Vector2<class_Vector2>], dir_b\: [Vector2<class_Vector2>]\ ) [🔗<class_Geometry2D_method_line_intersects_line>]

Returns the point of intersection between the two lines (`from_a`, `dir_a`) and (`from_b`, `dir_b`). Returns a [Vector2<class_Vector2>], or `null` if the lines are parallel.

\ `from` and `dir` are *not* endpoints of a line segment or ray but the slope (`dir`) and a known point (`from`) on that line.


> **TABS**
>

    var from_a = Vector2.ZERO
    var dir_a = Vector2.RIGHT
    var from_b = Vector2.DOWN

    # Returns Vector2(1, 0)
    Geometry2D.line_intersects_line(from_a, dir_a, from_b, Vector2(1, -1))
    # Returns Vector2(-1, 0)
    Geometry2D.line_intersects_line(from_a, dir_a, from_b, Vector2(-1, -1))
    # Returns null
    Geometry2D.line_intersects_line(from_a, dir_a, from_b, Vector2.RIGHT)


    var fromA = Vector2.Zero;
    var dirA = Vector2.Right;
    var fromB = Vector2.Down;

    // Returns new Vector2(1, 0)
    Geometry2D.LineIntersectsLine(fromA, dirA, fromB, new Vector2(1, -1));
    // Returns new Vector2(-1, 0)
    Geometry2D.LineIntersectsLine(fromA, dirA, fromB, new Vector2(-1, -1));
    // Returns null
    Geometry2D.LineIntersectsLine(fromA, dirA, fromB, Vector2.Right);




----



[Dictionary<class_Dictionary>] **make_atlas**\ (\ sizes\: [PackedVector2Array<class_PackedVector2Array>]\ ) [🔗<class_Geometry2D_method_make_atlas>]

Given an array of [Vector2<class_Vector2>]\ s representing tiles, builds an atlas. The returned dictionary has two keys: `points` is a [PackedVector2Array<class_PackedVector2Array>] that specifies the positions of each tile, `size` contains the overall size of the whole atlas as [Vector2i<class_Vector2i>].


----



[Array<class_Array>]\[[PackedVector2Array<class_PackedVector2Array>]\] **merge_polygons**\ (\ polygon_a\: [PackedVector2Array<class_PackedVector2Array>], polygon_b\: [PackedVector2Array<class_PackedVector2Array>]\ ) [🔗<class_Geometry2D_method_merge_polygons>]

Merges (combines) `polygon_a` and `polygon_b` and returns an array of merged polygons. This performs [OPERATION_UNION<class_Geometry2D_constant_OPERATION_UNION>] between polygons.

The operation may result in an outer polygon (boundary) and multiple inner polygons (holes) produced which could be distinguished by calling [is_polygon_clockwise()<class_Geometry2D_method_is_polygon_clockwise>].


----



[Array<class_Array>]\[[PackedVector2Array<class_PackedVector2Array>]\] **offset_polygon**\ (\ polygon\: [PackedVector2Array<class_PackedVector2Array>], delta\: [float<class_float>], join_type\: [PolyJoinType<enum_Geometry2D_PolyJoinType>] = 0\ ) [🔗<class_Geometry2D_method_offset_polygon>]

Inflates or deflates `polygon` by `delta` units (pixels). If `delta` is positive, makes the polygon grow outward. If `delta` is negative, shrinks the polygon inward. Returns an array of polygons because inflating/deflating may result in multiple discrete polygons. Returns an empty array if `delta` is negative and the absolute value of it approximately exceeds the minimum bounding rectangle dimensions of the polygon.

Each polygon's vertices will be rounded as determined by `join_type`.

The operation may result in an outer polygon (boundary) and inner polygon (hole) produced which could be distinguished by calling [is_polygon_clockwise()<class_Geometry2D_method_is_polygon_clockwise>].

\ **Note:** To translate the polygon's vertices specifically, multiply them to a [Transform2D<class_Transform2D>]:


> **TABS**
>

    var polygon = PackedVector2Array([Vector2(0, 0), Vector2(100, 0), Vector2(100, 100), Vector2(0, 100)])
    var offset = Vector2(50, 50)
    polygon = Transform2D(0, offset) * polygon
    print(polygon) # Prints [(50.0, 50.0), (150.0, 50.0), (150.0, 150.0), (50.0, 150.0)]


    Vector2[] polygon = [new Vector2(0, 0), new Vector2(100, 0), new Vector2(100, 100), new Vector2(0, 100)];
    var offset = new Vector2(50, 50);
    polygon = new Transform2D(0, offset) * polygon;
    GD.Print((Variant)polygon); // Prints [(50, 50), (150, 50), (150, 150), (50, 150)]




----



[Array<class_Array>]\[[PackedVector2Array<class_PackedVector2Array>]\] **offset_polyline**\ (\ polyline\: [PackedVector2Array<class_PackedVector2Array>], delta\: [float<class_float>], join_type\: [PolyJoinType<enum_Geometry2D_PolyJoinType>] = 0, end_type\: [PolyEndType<enum_Geometry2D_PolyEndType>] = 3\ ) [🔗<class_Geometry2D_method_offset_polyline>]

Inflates or deflates `polyline` by `delta` units (pixels), producing polygons. If `delta` is positive, makes the polyline grow outward. Returns an array of polygons because inflating/deflating may result in multiple discrete polygons. If `delta` is negative, returns an empty array.

Each polygon's vertices will be rounded as determined by `join_type`.

Each polygon's endpoints will be rounded as determined by `end_type`.

The operation may result in an outer polygon (boundary) and inner polygon (hole) produced which could be distinguished by calling [is_polygon_clockwise()<class_Geometry2D_method_is_polygon_clockwise>].


----



[bool<class_bool>] **point_is_inside_triangle**\ (\ point\: [Vector2<class_Vector2>], a\: [Vector2<class_Vector2>], b\: [Vector2<class_Vector2>], c\: [Vector2<class_Vector2>]\ ) |const| [🔗<class_Geometry2D_method_point_is_inside_triangle>]

Returns if `point` is inside the triangle specified by `a`, `b` and `c`.


----



[float<class_float>] **segment_intersects_circle**\ (\ segment_from\: [Vector2<class_Vector2>], segment_to\: [Vector2<class_Vector2>], circle_position\: [Vector2<class_Vector2>], circle_radius\: [float<class_float>]\ ) [🔗<class_Geometry2D_method_segment_intersects_circle>]

Given the 2D segment (`segment_from`, `segment_to`), returns the position on the segment (as a number between 0 and 1) at which the segment hits the circle that is located at position `circle_position` and has radius `circle_radius`. If the segment does not intersect the circle, -1 is returned (this is also the case if the line extending the segment would intersect the circle, but the segment does not).


----



[Variant<class_Variant>] **segment_intersects_segment**\ (\ from_a\: [Vector2<class_Vector2>], to_a\: [Vector2<class_Vector2>], from_b\: [Vector2<class_Vector2>], to_b\: [Vector2<class_Vector2>]\ ) [🔗<class_Geometry2D_method_segment_intersects_segment>]

Checks if the two segments (`from_a`, `to_a`) and (`from_b`, `to_b`) intersect. If yes, return the point of intersection as [Vector2<class_Vector2>]. If no intersection takes place, returns `null`.


----



[PackedInt32Array<class_PackedInt32Array>] **triangulate_delaunay**\ (\ points\: [PackedVector2Array<class_PackedVector2Array>]\ ) [🔗<class_Geometry2D_method_triangulate_delaunay>]

Triangulates the area specified by discrete set of `points` such that no point is inside the circumcircle of any resulting triangle. Returns a [PackedInt32Array<class_PackedInt32Array>] where each triangle consists of three consecutive point indices into `points` (i.e. the returned array will have `n * 3` elements, with `n` being the number of found triangles). If the triangulation did not succeed, an empty [PackedInt32Array<class_PackedInt32Array>] is returned.


----



[PackedInt32Array<class_PackedInt32Array>] **triangulate_polygon**\ (\ polygon\: [PackedVector2Array<class_PackedVector2Array>]\ ) [🔗<class_Geometry2D_method_triangulate_polygon>]

Triangulates the polygon specified by the points in `polygon`. Returns a [PackedInt32Array<class_PackedInt32Array>] where each triangle consists of three consecutive point indices into `polygon` (i.e. the returned array will have `n * 3` elements, with `n` being the number of found triangles). Output triangles will always be counter clockwise, and the contour will be flipped if it's clockwise. If the triangulation did not succeed, an empty [PackedInt32Array<class_PackedInt32Array>] is returned.

