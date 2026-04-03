:github_url: hide



# CSGShape3D

**Inherits:** [GeometryInstance3D<class_GeometryInstance3D>] **<** [VisualInstance3D<class_VisualInstance3D>] **<** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

**Inherited By:** [CSGCombiner3D<class_CSGCombiner3D>], [CSGPrimitive3D<class_CSGPrimitive3D>]

The CSG base class.


## Description

This is the CSG base class that provides CSG operation support to the various CSG nodes in Godot.

\ **Performance:** CSG nodes are only intended for prototyping as they have a significant CPU performance cost. Consider baking final CSG operation results into static geometry that replaces the CSG nodes.

Individual CSG root node results can be baked to nodes with static resources with the editor menu that appears when a CSG root node is selected.

Individual CSG root nodes can also be baked to static resources with scripts by calling [bake_static_mesh()<class_CSGShape3D_method_bake_static_mesh>] for the visual mesh or [bake_collision_shape()<class_CSGShape3D_method_bake_collision_shape>] for the physics collision.

Entire scenes of CSG nodes can be baked to static geometry and exported with the editor glTF scene exporter: **Scene > Export As... > glTF 2.0 Scene...**


## Tutorials

- [../tutorials/3d/csg_tools](Prototyping levels with CSG .md)


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------------------+-------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                     | :ref:`calculate_tangents<class_CSGShape3D_property_calculate_tangents>` | ``true``  |
> +---------------------------------------------+-------------------------------------------------------------------------+-----------+
> | :ref:`int<class_int>`                       | :ref:`collision_layer<class_CSGShape3D_property_collision_layer>`       | ``1``     |
> +---------------------------------------------+-------------------------------------------------------------------------+-----------+
> | :ref:`int<class_int>`                       | :ref:`collision_mask<class_CSGShape3D_property_collision_mask>`         | ``1``     |
> +---------------------------------------------+-------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>`                   | :ref:`collision_priority<class_CSGShape3D_property_collision_priority>` | ``1.0``   |
> +---------------------------------------------+-------------------------------------------------------------------------+-----------+
> | :ref:`Operation<enum_CSGShape3D_Operation>` | :ref:`operation<class_CSGShape3D_property_operation>`                   | ``0``     |
> +---------------------------------------------+-------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>`                   | :ref:`snap<class_CSGShape3D_property_snap>`                             |           |
> +---------------------------------------------+-------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                     | :ref:`use_collision<class_CSGShape3D_property_use_collision>`           | ``false`` |
> +---------------------------------------------+-------------------------------------------------------------------------+-----------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`ConcavePolygonShape3D<class_ConcavePolygonShape3D>` | :ref:`bake_collision_shape<class_CSGShape3D_method_bake_collision_shape>`\ (\ )                                                                                  |
> +-----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`ArrayMesh<class_ArrayMesh>`                         | :ref:`bake_static_mesh<class_CSGShape3D_method_bake_static_mesh>`\ (\ )                                                                                          |
> +-----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                   | :ref:`get_collision_layer_value<class_CSGShape3D_method_get_collision_layer_value>`\ (\ layer_number\: :ref:`int<class_int>`\ ) |const|                          |
> +-----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                   | :ref:`get_collision_mask_value<class_CSGShape3D_method_get_collision_mask_value>`\ (\ layer_number\: :ref:`int<class_int>`\ ) |const|                            |
> +-----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`                                 | :ref:`get_meshes<class_CSGShape3D_method_get_meshes>`\ (\ ) |const|                                                                                              |
> +-----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                   | :ref:`is_root_shape<class_CSGShape3D_method_is_root_shape>`\ (\ ) |const|                                                                                        |
> +-----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                    | :ref:`set_collision_layer_value<class_CSGShape3D_method_set_collision_layer_value>`\ (\ layer_number\: :ref:`int<class_int>`, value\: :ref:`bool<class_bool>`\ ) |
> +-----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                    | :ref:`set_collision_mask_value<class_CSGShape3D_method_set_collision_mask_value>`\ (\ layer_number\: :ref:`int<class_int>`, value\: :ref:`bool<class_bool>`\ )   |
> +-----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **Operation**: [🔗<enum_CSGShape3D_Operation>]



[Operation<enum_CSGShape3D_Operation>] **OPERATION_UNION** = `0`

Geometry of both primitives is merged, intersecting geometry is removed.



[Operation<enum_CSGShape3D_Operation>] **OPERATION_INTERSECTION** = `1`

Only intersecting geometry remains, the rest is removed.



[Operation<enum_CSGShape3D_Operation>] **OPERATION_SUBTRACTION** = `2`

The second shape is subtracted from the first, leaving a dent with its shape.


----


## Property Descriptions



[bool<class_bool>] **calculate_tangents** = `true` [🔗<class_CSGShape3D_property_calculate_tangents>]


- |void| **set_calculate_tangents**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_calculating_tangents**\ (\ )

Calculate tangents for the CSG shape which allows the use of normal and height maps. This is only applied on the root shape, this setting is ignored on any child. Setting this to `false` can speed up shape generation slightly.


----



[int<class_int>] **collision_layer** = `1` [🔗<class_CSGShape3D_property_collision_layer>]


- |void| **set_collision_layer**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_collision_layer**\ (\ )

The physics layers this area is in.

Collidable objects can exist in any of 32 different layers. These layers work like a tagging system, and are not visual. A collidable can use these layers to select with which objects it can collide, using the collision_mask property.

A contact is detected if object A is in any of the layers that object B scans, or object B is in any layer scanned by object A. See [Collision layers and masks ](../tutorials/physics/physics_introduction.html#collision-layers-and-masks)_ in the documentation for more information.


----



[int<class_int>] **collision_mask** = `1` [🔗<class_CSGShape3D_property_collision_mask>]


- |void| **set_collision_mask**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_collision_mask**\ (\ )

The physics layers this CSG shape scans for collisions. Only effective if [use_collision<class_CSGShape3D_property_use_collision>] is `true`. See [Collision layers and masks ](../tutorials/physics/physics_introduction.html#collision-layers-and-masks)_ in the documentation for more information.


----



[float<class_float>] **collision_priority** = `1.0` [🔗<class_CSGShape3D_property_collision_priority>]


- |void| **set_collision_priority**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_collision_priority**\ (\ )

The priority used to solve colliding when occurring penetration. Only effective if [use_collision<class_CSGShape3D_property_use_collision>] is `true`. The higher the priority is, the lower the penetration into the object will be. This can for example be used to prevent the player from breaking through the boundaries of a level.


----



[Operation<enum_CSGShape3D_Operation>] **operation** = `0` [🔗<class_CSGShape3D_property_operation>]


- |void| **set_operation**\ (\ value\: [Operation<enum_CSGShape3D_Operation>]\ )
- [Operation<enum_CSGShape3D_Operation>] **get_operation**\ (\ )

The operation that is performed on this shape. This is ignored for the first CSG child node as the operation is between this node and the previous child of this nodes parent.


----



[float<class_float>] **snap** [🔗<class_CSGShape3D_property_snap>]


- |void| **set_snap**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_snap**\ (\ )

**Deprecated:** The CSG library no longer uses snapping.

This property does nothing.


----



[bool<class_bool>] **use_collision** = `false` [🔗<class_CSGShape3D_property_use_collision>]


- |void| **set_use_collision**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_using_collision**\ (\ )

Adds a collision shape to the physics engine for our CSG shape. This will always act like a static body. Note that the collision shape is still active even if the CSG shape itself is hidden. See also [collision_mask<class_CSGShape3D_property_collision_mask>] and [collision_priority<class_CSGShape3D_property_collision_priority>].


----


## Method Descriptions



[ConcavePolygonShape3D<class_ConcavePolygonShape3D>] **bake_collision_shape**\ (\ ) [🔗<class_CSGShape3D_method_bake_collision_shape>]

Returns a baked physics [ConcavePolygonShape3D<class_ConcavePolygonShape3D>] of this node's CSG operation result. Returns an empty shape if the node is not a CSG root node or has no valid geometry.

\ **Performance:** If the CSG operation results in a very detailed geometry with many faces physics performance will be very slow. Concave shapes should in general only be used for static level geometry and not with dynamic objects that are moving.

\ **Note:** CSG mesh data updates are deferred, which means they are updated with a delay of one rendered frame. To avoid getting an empty shape or outdated mesh data, make sure to call `await get_tree().process_frame` before using [bake_collision_shape()<class_CSGShape3D_method_bake_collision_shape>] in [Node._ready()<class_Node_private_method__ready>] or after changing properties on the **CSGShape3D**.


----



[ArrayMesh<class_ArrayMesh>] **bake_static_mesh**\ (\ ) [🔗<class_CSGShape3D_method_bake_static_mesh>]

Returns a baked static [ArrayMesh<class_ArrayMesh>] of this node's CSG operation result. Materials from involved CSG nodes are added as extra mesh surfaces. Returns an empty mesh if the node is not a CSG root node or has no valid geometry.

\ **Note:** CSG mesh data updates are deferred, which means they are updated with a delay of one rendered frame. To avoid getting an empty mesh or outdated mesh data, make sure to call `await get_tree().process_frame` before using [bake_static_mesh()<class_CSGShape3D_method_bake_static_mesh>] in [Node._ready()<class_Node_private_method__ready>] or after changing properties on the **CSGShape3D**.


----



[bool<class_bool>] **get_collision_layer_value**\ (\ layer_number\: [int<class_int>]\ ) |const| [🔗<class_CSGShape3D_method_get_collision_layer_value>]

Returns whether or not the specified layer of the [collision_layer<class_CSGShape3D_property_collision_layer>] is enabled, given a `layer_number` between 1 and 32.


----



[bool<class_bool>] **get_collision_mask_value**\ (\ layer_number\: [int<class_int>]\ ) |const| [🔗<class_CSGShape3D_method_get_collision_mask_value>]

Returns whether or not the specified layer of the [collision_mask<class_CSGShape3D_property_collision_mask>] is enabled, given a `layer_number` between 1 and 32.


----



[Array<class_Array>] **get_meshes**\ (\ ) |const| [🔗<class_CSGShape3D_method_get_meshes>]

Returns an [Array<class_Array>] with two elements, the first is the [Transform3D<class_Transform3D>] of this node and the second is the root [Mesh<class_Mesh>] of this node. Only works when this node is the root shape.

\ **Note:** CSG mesh data updates are deferred, which means they are updated with a delay of one rendered frame. To avoid getting an empty shape or outdated mesh data, make sure to call `await get_tree().process_frame` before using [get_meshes()<class_CSGShape3D_method_get_meshes>] in [Node._ready()<class_Node_private_method__ready>] or after changing properties on the **CSGShape3D**.


----



[bool<class_bool>] **is_root_shape**\ (\ ) |const| [🔗<class_CSGShape3D_method_is_root_shape>]

Returns `true` if this is a root shape and is thus the object that is rendered.


----



|void| **set_collision_layer_value**\ (\ layer_number\: [int<class_int>], value\: [bool<class_bool>]\ ) [🔗<class_CSGShape3D_method_set_collision_layer_value>]

Based on `value`, enables or disables the specified layer in the [collision_layer<class_CSGShape3D_property_collision_layer>], given a `layer_number` between 1 and 32.


----



|void| **set_collision_mask_value**\ (\ layer_number\: [int<class_int>], value\: [bool<class_bool>]\ ) [🔗<class_CSGShape3D_method_set_collision_mask_value>]

Based on `value`, enables or disables the specified layer in the [collision_mask<class_CSGShape3D_property_collision_mask>], given a `layer_number` between 1 and 32.

