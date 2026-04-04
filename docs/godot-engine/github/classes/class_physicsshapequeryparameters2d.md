:github_url: hide



# PhysicsShapeQueryParameters2D

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Provides parameters for [PhysicsDirectSpaceState2D<class_PhysicsDirectSpaceState2D>]'s methods.


## Description

By changing various properties of this object, such as the shape, you can configure the parameters for [PhysicsDirectSpaceState2D<class_PhysicsDirectSpaceState2D>]'s methods.


## Properties

> **TABLE**
> :widths: auto
>
> +----------------------------------------------------+----------------------------------------------------------------------------------------------+-----------------------------------+
> | :ref:`bool<class_bool>`                            | :ref:`collide_with_areas<class_PhysicsShapeQueryParameters2D_property_collide_with_areas>`   | ``false``                         |
> +----------------------------------------------------+----------------------------------------------------------------------------------------------+-----------------------------------+
> | :ref:`bool<class_bool>`                            | :ref:`collide_with_bodies<class_PhysicsShapeQueryParameters2D_property_collide_with_bodies>` | ``true``                          |
> +----------------------------------------------------+----------------------------------------------------------------------------------------------+-----------------------------------+
> | :ref:`int<class_int>`                              | :ref:`collision_mask<class_PhysicsShapeQueryParameters2D_property_collision_mask>`           | ``4294967295``                    |
> +----------------------------------------------------+----------------------------------------------------------------------------------------------+-----------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`RID<class_RID>`\] | :ref:`exclude<class_PhysicsShapeQueryParameters2D_property_exclude>`                         | ``[]``                            |
> +----------------------------------------------------+----------------------------------------------------------------------------------------------+-----------------------------------+
> | :ref:`float<class_float>`                          | :ref:`margin<class_PhysicsShapeQueryParameters2D_property_margin>`                           | ``0.0``                           |
> +----------------------------------------------------+----------------------------------------------------------------------------------------------+-----------------------------------+
> | :ref:`Vector2<class_Vector2>`                      | :ref:`motion<class_PhysicsShapeQueryParameters2D_property_motion>`                           | ``Vector2(0, 0)``                 |
> +----------------------------------------------------+----------------------------------------------------------------------------------------------+-----------------------------------+
> | :ref:`Resource<class_Resource>`                    | :ref:`shape<class_PhysicsShapeQueryParameters2D_property_shape>`                             |                                   |
> +----------------------------------------------------+----------------------------------------------------------------------------------------------+-----------------------------------+
> | :ref:`RID<class_RID>`                              | :ref:`shape_rid<class_PhysicsShapeQueryParameters2D_property_shape_rid>`                     | ``RID()``                         |
> +----------------------------------------------------+----------------------------------------------------------------------------------------------+-----------------------------------+
> | :ref:`Transform2D<class_Transform2D>`              | :ref:`transform<class_PhysicsShapeQueryParameters2D_property_transform>`                     | ``Transform2D(1, 0, 0, 1, 0, 0)`` |
> +----------------------------------------------------+----------------------------------------------------------------------------------------------+-----------------------------------+
>

----


## Property Descriptions



[bool<class_bool>] **collide_with_areas** = `false` [🔗<class_PhysicsShapeQueryParameters2D_property_collide_with_areas>]


- |void| **set_collide_with_areas**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_collide_with_areas_enabled**\ (\ )

If `true`, the query will take [Area2D<class_Area2D>]\ s into account.


----



[bool<class_bool>] **collide_with_bodies** = `true` [🔗<class_PhysicsShapeQueryParameters2D_property_collide_with_bodies>]


- |void| **set_collide_with_bodies**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_collide_with_bodies_enabled**\ (\ )

If `true`, the query will take [PhysicsBody2D<class_PhysicsBody2D>]\ s into account.


----



[int<class_int>] **collision_mask** = `4294967295` [🔗<class_PhysicsShapeQueryParameters2D_property_collision_mask>]


- |void| **set_collision_mask**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_collision_mask**\ (\ )

The physics layers the query will detect (as a bitmask). By default, all collision layers are detected. See [Collision layers and masks ](../tutorials/physics/physics_introduction.html#collision-layers-and-masks)_ in the documentation for more information.


----



[Array<class_Array>]\[[RID<class_RID>]\] **exclude** = `[]` [🔗<class_PhysicsShapeQueryParameters2D_property_exclude>]


- |void| **set_exclude**\ (\ value\: [Array<class_Array>]\[[RID<class_RID>]\]\ )
- [Array<class_Array>]\[[RID<class_RID>]\] **get_exclude**\ (\ )

The list of object [RID<class_RID>]\ s that will be excluded from collisions. Use [CollisionObject2D.get_rid()<class_CollisionObject2D_method_get_rid>] to get the [RID<class_RID>] associated with a [CollisionObject2D<class_CollisionObject2D>]-derived node.

\ **Note:** The returned array is copied and any changes to it will not update the original property value. To update the value you need to modify the returned array, and then assign it to the property again.


----



[float<class_float>] **margin** = `0.0` [🔗<class_PhysicsShapeQueryParameters2D_property_margin>]


- |void| **set_margin**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_margin**\ (\ )

The collision margin for the shape.


----



[Vector2<class_Vector2>] **motion** = `Vector2(0, 0)` [🔗<class_PhysicsShapeQueryParameters2D_property_motion>]


- |void| **set_motion**\ (\ value\: [Vector2<class_Vector2>]\ )
- [Vector2<class_Vector2>] **get_motion**\ (\ )

The motion of the shape being queried for.


----



[Resource<class_Resource>] **shape** [🔗<class_PhysicsShapeQueryParameters2D_property_shape>]


- |void| **set_shape**\ (\ value\: [Resource<class_Resource>]\ )
- [Resource<class_Resource>] **get_shape**\ (\ )

The [Shape2D<class_Shape2D>] that will be used for collision/intersection queries. This stores the actual reference which avoids the shape to be released while being used for queries, so always prefer using this over [shape_rid<class_PhysicsShapeQueryParameters2D_property_shape_rid>].


----



[RID<class_RID>] **shape_rid** = `RID()` [🔗<class_PhysicsShapeQueryParameters2D_property_shape_rid>]


- |void| **set_shape_rid**\ (\ value\: [RID<class_RID>]\ )
- [RID<class_RID>] **get_shape_rid**\ (\ )

The queried shape's [RID<class_RID>] that will be used for collision/intersection queries. Use this over [shape<class_PhysicsShapeQueryParameters2D_property_shape>] if you want to optimize for performance using the Servers API:


> **TABS**
>

    var shape_rid = PhysicsServer2D.circle_shape_create()
    var radius = 64
    PhysicsServer2D.shape_set_data(shape_rid, radius)

    var params = PhysicsShapeQueryParameters2D.new()
    params.shape_rid = shape_rid

    # Execute physics queries here...

    # Release the shape when done with physics queries.
    PhysicsServer2D.free_rid(shape_rid)


    RID shapeRid = PhysicsServer2D.CircleShapeCreate();
    int radius = 64;
    PhysicsServer2D.ShapeSetData(shapeRid, radius);

    var params = new PhysicsShapeQueryParameters2D();
    params.ShapeRid = shapeRid;

    // Execute physics queries here...

    // Release the shape when done with physics queries.
    PhysicsServer2D.FreeRid(shapeRid);




----



[Transform2D<class_Transform2D>] **transform** = `Transform2D(1, 0, 0, 1, 0, 0)` [🔗<class_PhysicsShapeQueryParameters2D_property_transform>]


- |void| **set_transform**\ (\ value\: [Transform2D<class_Transform2D>]\ )
- [Transform2D<class_Transform2D>] **get_transform**\ (\ )

The queried shape's transform matrix.

