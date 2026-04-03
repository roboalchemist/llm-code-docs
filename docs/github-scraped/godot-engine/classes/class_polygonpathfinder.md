:github_url: hide



# PolygonPathFinder

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

> **CONTAINER**
>
	There is currently no description for this class. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedVector2Array<class_PackedVector2Array>` | :ref:`find_path<class_PolygonPathFinder_method_find_path>`\ (\ from\: :ref:`Vector2<class_Vector2>`, to\: :ref:`Vector2<class_Vector2>`\ )                                            |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Rect2<class_Rect2>`                           | :ref:`get_bounds<class_PolygonPathFinder_method_get_bounds>`\ (\ ) |const|                                                                                                            |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>`                       | :ref:`get_closest_point<class_PolygonPathFinder_method_get_closest_point>`\ (\ point\: :ref:`Vector2<class_Vector2>`\ ) |const|                                                       |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedVector2Array<class_PackedVector2Array>` | :ref:`get_intersections<class_PolygonPathFinder_method_get_intersections>`\ (\ from\: :ref:`Vector2<class_Vector2>`, to\: :ref:`Vector2<class_Vector2>`\ ) |const|                    |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                           | :ref:`get_point_penalty<class_PolygonPathFinder_method_get_point_penalty>`\ (\ idx\: :ref:`int<class_int>`\ ) |const|                                                                 |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                             | :ref:`is_point_inside<class_PolygonPathFinder_method_is_point_inside>`\ (\ point\: :ref:`Vector2<class_Vector2>`\ ) |const|                                                           |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`set_point_penalty<class_PolygonPathFinder_method_set_point_penalty>`\ (\ idx\: :ref:`int<class_int>`, penalty\: :ref:`float<class_float>`\ )                                    |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`setup<class_PolygonPathFinder_method_setup>`\ (\ points\: :ref:`PackedVector2Array<class_PackedVector2Array>`, connections\: :ref:`PackedInt32Array<class_PackedInt32Array>`\ ) |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[PackedVector2Array<class_PackedVector2Array>] **find_path**\ (\ from\: [Vector2<class_Vector2>], to\: [Vector2<class_Vector2>]\ ) [🔗<class_PolygonPathFinder_method_find_path>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Rect2<class_Rect2>] **get_bounds**\ (\ ) |const| [🔗<class_PolygonPathFinder_method_get_bounds>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Vector2<class_Vector2>] **get_closest_point**\ (\ point\: [Vector2<class_Vector2>]\ ) |const| [🔗<class_PolygonPathFinder_method_get_closest_point>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[PackedVector2Array<class_PackedVector2Array>] **get_intersections**\ (\ from\: [Vector2<class_Vector2>], to\: [Vector2<class_Vector2>]\ ) |const| [🔗<class_PolygonPathFinder_method_get_intersections>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[float<class_float>] **get_point_penalty**\ (\ idx\: [int<class_int>]\ ) |const| [🔗<class_PolygonPathFinder_method_get_point_penalty>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[bool<class_bool>] **is_point_inside**\ (\ point\: [Vector2<class_Vector2>]\ ) |const| [🔗<class_PolygonPathFinder_method_is_point_inside>]

Returns `true` if `point` falls inside the polygon area.


> **TABS**
>

    var polygon_path_finder = PolygonPathFinder.new()
    var points = [Vector2(0.0, 0.0), Vector2(1.0, 0.0), Vector2(0.0, 1.0)]
    var connections = [0, 1, 1, 2, 2, 0]
    polygon_path_finder.setup(points, connections)
    print(polygon_path_finder.is_point_inside(Vector2(0.2, 0.2))) # Prints true
    print(polygon_path_finder.is_point_inside(Vector2(1.0, 1.0))) # Prints false


    var polygonPathFinder = new PolygonPathFinder();
    Vector2[] points =
    [
        new Vector2(0.0f, 0.0f),
        new Vector2(1.0f, 0.0f),
        new Vector2(0.0f, 1.0f)
    ];
    int[] connections = [0, 1, 1, 2, 2, 0];
    polygonPathFinder.Setup(points, connections);
    GD.Print(polygonPathFinder.IsPointInside(new Vector2(0.2f, 0.2f))); // Prints True
    GD.Print(polygonPathFinder.IsPointInside(new Vector2(1.0f, 1.0f))); // Prints False




----



|void| **set_point_penalty**\ (\ idx\: [int<class_int>], penalty\: [float<class_float>]\ ) [🔗<class_PolygonPathFinder_method_set_point_penalty>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



|void| **setup**\ (\ points\: [PackedVector2Array<class_PackedVector2Array>], connections\: [PackedInt32Array<class_PackedInt32Array>]\ ) [🔗<class_PolygonPathFinder_method_setup>]

Sets up **PolygonPathFinder** with an array of points that define the vertices of the polygon, and an array of indices that determine the edges of the polygon.

The length of `connections` must be even, returns an error if odd.


> **TABS**
>

    var polygon_path_finder = PolygonPathFinder.new()
    var points = [Vector2(0.0, 0.0), Vector2(1.0, 0.0), Vector2(0.0, 1.0)]
    var connections = [0, 1, 1, 2, 2, 0]
    polygon_path_finder.setup(points, connections)


    var polygonPathFinder = new PolygonPathFinder();
    Vector2[] points =
    [
        new Vector2(0.0f, 0.0f),
        new Vector2(1.0f, 0.0f),
        new Vector2(0.0f, 1.0f)
    ];
    int[] connections = [0, 1, 1, 2, 2, 0];
    polygonPathFinder.Setup(points, connections);



