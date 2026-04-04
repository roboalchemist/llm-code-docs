:github_url: hide

> **META**
	:keywords: trigger



# Area3D

**Inherits:** [CollisionObject3D<class_CollisionObject3D>] **<** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A region of 3D space that detects other [CollisionObject3D<class_CollisionObject3D>]\ s entering or exiting it.


## Description

**Area3D** is a region of 3D space defined by one or multiple [CollisionShape3D<class_CollisionShape3D>] or [CollisionPolygon3D<class_CollisionPolygon3D>] child nodes. It detects when other [CollisionObject3D<class_CollisionObject3D>]\ s enter or exit it, and it also keeps track of which collision objects haven't exited it yet (i.e. which one are overlapping it).

This node can also locally alter or override physics parameters (gravity, damping) and route audio to custom audio buses.

\ **Note:** Areas and bodies created with [PhysicsServer3D<class_PhysicsServer3D>] might not interact as expected with **Area3D**\ s, and might not emit signals or track objects correctly.

\ **Warning:** Using a [ConcavePolygonShape3D<class_ConcavePolygonShape3D>] inside a [CollisionShape3D<class_CollisionShape3D>] child of this node (created e.g. by using the **Create Trimesh Collision Sibling** option in the **Mesh** menu that appears when selecting a [MeshInstance3D<class_MeshInstance3D>] node) may give unexpected results, since this collision shape is hollow. If this is not desired, it has to be split into multiple [ConvexPolygonShape3D<class_ConvexPolygonShape3D>]\ s or primitive shapes like [BoxShape3D<class_BoxShape3D>], or in some cases it may be replaceable by a [CollisionPolygon3D<class_CollisionPolygon3D>].


## Tutorials

- [../tutorials/physics/using_area_2d](Using Area2D .md)

- [3D Platformer Demo ](https://godotengine.org/asset-library/asset/2748)_

- [GUI in 3D Viewport Demo ](https://godotengine.org/asset-library/asset/2807)_


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`                       | :ref:`angular_damp<class_Area3D_property_angular_damp>`                               | ``0.1``               |
> +-------------------------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`SpaceOverride<enum_Area3D_SpaceOverride>` | :ref:`angular_damp_space_override<class_Area3D_property_angular_damp_space_override>` | ``0``                 |
> +-------------------------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`StringName<class_StringName>`             | :ref:`audio_bus_name<class_Area3D_property_audio_bus_name>`                           | ``&"Master"``         |
> +-------------------------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`                         | :ref:`audio_bus_override<class_Area3D_property_audio_bus_override>`                   | ``false``             |
> +-------------------------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`                       | :ref:`gravity<class_Area3D_property_gravity>`                                         | ``9.8``               |
> +-------------------------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`Vector3<class_Vector3>`                   | :ref:`gravity_direction<class_Area3D_property_gravity_direction>`                     | ``Vector3(0, -1, 0)`` |
> +-------------------------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`                         | :ref:`gravity_point<class_Area3D_property_gravity_point>`                             | ``false``             |
> +-------------------------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`Vector3<class_Vector3>`                   | :ref:`gravity_point_center<class_Area3D_property_gravity_point_center>`               | ``Vector3(0, -1, 0)`` |
> +-------------------------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`                       | :ref:`gravity_point_unit_distance<class_Area3D_property_gravity_point_unit_distance>` | ``0.0``               |
> +-------------------------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`SpaceOverride<enum_Area3D_SpaceOverride>` | :ref:`gravity_space_override<class_Area3D_property_gravity_space_override>`           | ``0``                 |
> +-------------------------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`                       | :ref:`linear_damp<class_Area3D_property_linear_damp>`                                 | ``0.1``               |
> +-------------------------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`SpaceOverride<enum_Area3D_SpaceOverride>` | :ref:`linear_damp_space_override<class_Area3D_property_linear_damp_space_override>`   | ``0``                 |
> +-------------------------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`                         | :ref:`monitorable<class_Area3D_property_monitorable>`                                 | ``true``              |
> +-------------------------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`                         | :ref:`monitoring<class_Area3D_property_monitoring>`                                   | ``true``              |
> +-------------------------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`int<class_int>`                           | :ref:`priority<class_Area3D_property_priority>`                                       | ``0``                 |
> +-------------------------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`                       | :ref:`reverb_bus_amount<class_Area3D_property_reverb_bus_amount>`                     | ``0.0``               |
> +-------------------------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`                         | :ref:`reverb_bus_enabled<class_Area3D_property_reverb_bus_enabled>`                   | ``false``             |
> +-------------------------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`StringName<class_StringName>`             | :ref:`reverb_bus_name<class_Area3D_property_reverb_bus_name>`                         | ``&"Master"``         |
> +-------------------------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`                       | :ref:`reverb_bus_uniformity<class_Area3D_property_reverb_bus_uniformity>`             | ``0.0``               |
> +-------------------------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`                       | :ref:`wind_attenuation_factor<class_Area3D_property_wind_attenuation_factor>`         | ``0.0``               |
> +-------------------------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`                       | :ref:`wind_force_magnitude<class_Area3D_property_wind_force_magnitude>`               | ``0.0``               |
> +-------------------------------------------------+---------------------------------------------------------------------------------------+-----------------------+
> | :ref:`NodePath<class_NodePath>`                 | :ref:`wind_source_path<class_Area3D_property_wind_source_path>`                       | ``NodePath("")``      |
> +-------------------------------------------------+---------------------------------------------------------------------------------------+-----------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +----------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`Area3D<class_Area3D>`\] | :ref:`get_overlapping_areas<class_Area3D_method_get_overlapping_areas>`\ (\ ) |const|                 |
> +----------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`Node3D<class_Node3D>`\] | :ref:`get_overlapping_bodies<class_Area3D_method_get_overlapping_bodies>`\ (\ ) |const|               |
> +----------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                  | :ref:`has_overlapping_areas<class_Area3D_method_has_overlapping_areas>`\ (\ ) |const|                 |
> +----------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                  | :ref:`has_overlapping_bodies<class_Area3D_method_has_overlapping_bodies>`\ (\ ) |const|               |
> +----------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                  | :ref:`overlaps_area<class_Area3D_method_overlaps_area>`\ (\ area\: :ref:`Node<class_Node>`\ ) |const| |
> +----------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                  | :ref:`overlaps_body<class_Area3D_method_overlaps_body>`\ (\ body\: :ref:`Node<class_Node>`\ ) |const| |
> +----------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
>

----


## Signals



**area_entered**\ (\ area\: [Area3D<class_Area3D>]\ ) [🔗<class_Area3D_signal_area_entered>]

Emitted when the received `area` enters this area. Requires [monitoring<class_Area3D_property_monitoring>] to be set to `true`.


----



**area_exited**\ (\ area\: [Area3D<class_Area3D>]\ ) [🔗<class_Area3D_signal_area_exited>]

Emitted when the received `area` exits this area. Requires [monitoring<class_Area3D_property_monitoring>] to be set to `true`.


----



**area_shape_entered**\ (\ area_rid\: [RID<class_RID>], area\: [Area3D<class_Area3D>], area_shape_index\: [int<class_int>], local_shape_index\: [int<class_int>]\ ) [🔗<class_Area3D_signal_area_shape_entered>]

Emitted when a [Shape3D<class_Shape3D>] of the received `area` enters a shape of this area. Requires [monitoring<class_Area3D_property_monitoring>] to be set to `true`.

\ `local_shape_index` and `area_shape_index` contain indices of the interacting shapes from this area and the other area, respectively. `area_rid` contains the [RID<class_RID>] of the other area. These values can be used with the [PhysicsServer3D<class_PhysicsServer3D>].

\ **Example:** Get the [CollisionShape3D<class_CollisionShape3D>] node from the shape index:


> **TABS**
>

    var other_shape_owner = area.shape_find_owner(area_shape_index)
    var other_shape_node = area.shape_owner_get_owner(other_shape_owner)

    var local_shape_owner = shape_find_owner(local_shape_index)
    var local_shape_node = shape_owner_get_owner(local_shape_owner)




----



**area_shape_exited**\ (\ area_rid\: [RID<class_RID>], area\: [Area3D<class_Area3D>], area_shape_index\: [int<class_int>], local_shape_index\: [int<class_int>]\ ) [🔗<class_Area3D_signal_area_shape_exited>]

Emitted when a [Shape3D<class_Shape3D>] of the received `area` exits a shape of this area. Requires [monitoring<class_Area3D_property_monitoring>] to be set to `true`.

See also [area_shape_entered<class_Area3D_signal_area_shape_entered>].


----



**body_entered**\ (\ body\: [Node3D<class_Node3D>]\ ) [🔗<class_Area3D_signal_body_entered>]

Emitted when the received `body` enters this area. `body` can be a [PhysicsBody3D<class_PhysicsBody3D>] or a [GridMap<class_GridMap>]. [GridMap<class_GridMap>]\ s are detected if their [MeshLibrary<class_MeshLibrary>] has collision shapes configured. Requires [monitoring<class_Area3D_property_monitoring>] to be set to `true`.


----



**body_exited**\ (\ body\: [Node3D<class_Node3D>]\ ) [🔗<class_Area3D_signal_body_exited>]

Emitted when the received `body` exits this area. `body` can be a [PhysicsBody3D<class_PhysicsBody3D>] or a [GridMap<class_GridMap>]. [GridMap<class_GridMap>]\ s are detected if their [MeshLibrary<class_MeshLibrary>] has collision shapes configured. Requires [monitoring<class_Area3D_property_monitoring>] to be set to `true`.


----



**body_shape_entered**\ (\ body_rid\: [RID<class_RID>], body\: [Node3D<class_Node3D>], body_shape_index\: [int<class_int>], local_shape_index\: [int<class_int>]\ ) [🔗<class_Area3D_signal_body_shape_entered>]

Emitted when a [Shape3D<class_Shape3D>] of the received `body` enters a shape of this area. `body` can be a [PhysicsBody3D<class_PhysicsBody3D>] or a [GridMap<class_GridMap>]. [GridMap<class_GridMap>]\ s are detected if their [MeshLibrary<class_MeshLibrary>] has collision shapes configured. Requires [monitoring<class_Area3D_property_monitoring>] to be set to `true`.

\ `local_shape_index` and `body_shape_index` contain indices of the interacting shapes from this area and the interacting body, respectively. `body_rid` contains the [RID<class_RID>] of the body. These values can be used with the [PhysicsServer3D<class_PhysicsServer3D>].

\ **Example:** Get the [CollisionShape3D<class_CollisionShape3D>] node from the shape index:


> **TABS**
>

    var body_shape_owner = body.shape_find_owner(body_shape_index)
    var body_shape_node = body.shape_owner_get_owner(body_shape_owner)

    var local_shape_owner = shape_find_owner(local_shape_index)
    var local_shape_node = shape_owner_get_owner(local_shape_owner)




----



**body_shape_exited**\ (\ body_rid\: [RID<class_RID>], body\: [Node3D<class_Node3D>], body_shape_index\: [int<class_int>], local_shape_index\: [int<class_int>]\ ) [🔗<class_Area3D_signal_body_shape_exited>]

Emitted when a [Shape3D<class_Shape3D>] of the received `body` exits a shape of this area. `body` can be a [PhysicsBody3D<class_PhysicsBody3D>] or a [GridMap<class_GridMap>]. [GridMap<class_GridMap>]\ s are detected if their [MeshLibrary<class_MeshLibrary>] has collision shapes configured. Requires [monitoring<class_Area3D_property_monitoring>] to be set to `true`.

See also [body_shape_entered<class_Area3D_signal_body_shape_entered>].


----


## Enumerations



enum **SpaceOverride**: [🔗<enum_Area3D_SpaceOverride>]



[SpaceOverride<enum_Area3D_SpaceOverride>] **SPACE_OVERRIDE_DISABLED** = `0`

This area does not affect gravity/damping.



[SpaceOverride<enum_Area3D_SpaceOverride>] **SPACE_OVERRIDE_COMBINE** = `1`

This area adds its gravity/damping values to whatever has been calculated so far (in [priority<class_Area3D_property_priority>] order).



[SpaceOverride<enum_Area3D_SpaceOverride>] **SPACE_OVERRIDE_COMBINE_REPLACE** = `2`

This area adds its gravity/damping values to whatever has been calculated so far (in [priority<class_Area3D_property_priority>] order), ignoring any lower priority areas.



[SpaceOverride<enum_Area3D_SpaceOverride>] **SPACE_OVERRIDE_REPLACE** = `3`

This area replaces any gravity/damping, even the defaults, ignoring any lower priority areas.



[SpaceOverride<enum_Area3D_SpaceOverride>] **SPACE_OVERRIDE_REPLACE_COMBINE** = `4`

This area replaces any gravity/damping calculated so far (in [priority<class_Area3D_property_priority>] order), but keeps calculating the rest of the areas.


----


## Property Descriptions



[float<class_float>] **angular_damp** = `0.1` [🔗<class_Area3D_property_angular_damp>]


- |void| **set_angular_damp**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_angular_damp**\ (\ )

The rate at which objects stop spinning in this area. Represents the angular velocity lost per second.

See [ProjectSettings.physics/3d/default_angular_damp<class_ProjectSettings_property_physics/3d/default_angular_damp>] for more details about damping.


----



[SpaceOverride<enum_Area3D_SpaceOverride>] **angular_damp_space_override** = `0` [🔗<class_Area3D_property_angular_damp_space_override>]


- |void| **set_angular_damp_space_override_mode**\ (\ value\: [SpaceOverride<enum_Area3D_SpaceOverride>]\ )
- [SpaceOverride<enum_Area3D_SpaceOverride>] **get_angular_damp_space_override_mode**\ (\ )

Override mode for angular damping calculations within this area.


----



[StringName<class_StringName>] **audio_bus_name** = `&"Master"` [🔗<class_Area3D_property_audio_bus_name>]


- |void| **set_audio_bus_name**\ (\ value\: [StringName<class_StringName>]\ )
- [StringName<class_StringName>] **get_audio_bus_name**\ (\ )

The name of the area's audio bus.


----



[bool<class_bool>] **audio_bus_override** = `false` [🔗<class_Area3D_property_audio_bus_override>]


- |void| **set_audio_bus_override**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_overriding_audio_bus**\ (\ )

If `true`, the area's audio bus overrides the default audio bus.


----



[float<class_float>] **gravity** = `9.8` [🔗<class_Area3D_property_gravity>]


- |void| **set_gravity**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_gravity**\ (\ )

The area's gravity intensity (in meters per second squared). This value multiplies the gravity direction. This is useful to alter the force of gravity without altering its direction.


----



[Vector3<class_Vector3>] **gravity_direction** = `Vector3(0, -1, 0)` [🔗<class_Area3D_property_gravity_direction>]


- |void| **set_gravity_direction**\ (\ value\: [Vector3<class_Vector3>]\ )
- [Vector3<class_Vector3>] **get_gravity_direction**\ (\ )

The area's gravity vector (not normalized).


----



[bool<class_bool>] **gravity_point** = `false` [🔗<class_Area3D_property_gravity_point>]


- |void| **set_gravity_is_point**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_gravity_a_point**\ (\ )

If `true`, gravity is calculated from a point (set via [gravity_point_center<class_Area3D_property_gravity_point_center>]). See also [gravity_space_override<class_Area3D_property_gravity_space_override>].


----



[Vector3<class_Vector3>] **gravity_point_center** = `Vector3(0, -1, 0)` [🔗<class_Area3D_property_gravity_point_center>]


- |void| **set_gravity_point_center**\ (\ value\: [Vector3<class_Vector3>]\ )
- [Vector3<class_Vector3>] **get_gravity_point_center**\ (\ )

If gravity is a point (see [gravity_point<class_Area3D_property_gravity_point>]), this will be the point of attraction.


----



[float<class_float>] **gravity_point_unit_distance** = `0.0` [🔗<class_Area3D_property_gravity_point_unit_distance>]


- |void| **set_gravity_point_unit_distance**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_gravity_point_unit_distance**\ (\ )

The distance at which the gravity strength is equal to [gravity<class_Area3D_property_gravity>]. For example, on a planet 100 meters in radius with a surface gravity of 4.0 m/s², set the [gravity<class_Area3D_property_gravity>] to 4.0 and the unit distance to 100.0. The gravity will have falloff according to the inverse square law, so in the example, at 200 meters from the center the gravity will be 1.0 m/s² (twice the distance, 1/4th the gravity), at 50 meters it will be 16.0 m/s² (half the distance, 4x the gravity), and so on.

The above is true only when the unit distance is a positive number. When this is set to 0.0, the gravity will be constant regardless of distance.


----



[SpaceOverride<enum_Area3D_SpaceOverride>] **gravity_space_override** = `0` [🔗<class_Area3D_property_gravity_space_override>]


- |void| **set_gravity_space_override_mode**\ (\ value\: [SpaceOverride<enum_Area3D_SpaceOverride>]\ )
- [SpaceOverride<enum_Area3D_SpaceOverride>] **get_gravity_space_override_mode**\ (\ )

Override mode for gravity calculations within this area.


----



[float<class_float>] **linear_damp** = `0.1` [🔗<class_Area3D_property_linear_damp>]


- |void| **set_linear_damp**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_linear_damp**\ (\ )

The rate at which objects stop moving in this area. Represents the linear velocity lost per second.

See [ProjectSettings.physics/3d/default_linear_damp<class_ProjectSettings_property_physics/3d/default_linear_damp>] for more details about damping.


----



[SpaceOverride<enum_Area3D_SpaceOverride>] **linear_damp_space_override** = `0` [🔗<class_Area3D_property_linear_damp_space_override>]


- |void| **set_linear_damp_space_override_mode**\ (\ value\: [SpaceOverride<enum_Area3D_SpaceOverride>]\ )
- [SpaceOverride<enum_Area3D_SpaceOverride>] **get_linear_damp_space_override_mode**\ (\ )

Override mode for linear damping calculations within this area.


----



[bool<class_bool>] **monitorable** = `true` [🔗<class_Area3D_property_monitorable>]


- |void| **set_monitorable**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_monitorable**\ (\ )

If `true`, other monitoring areas can detect this area.


----



[bool<class_bool>] **monitoring** = `true` [🔗<class_Area3D_property_monitoring>]


- |void| **set_monitoring**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_monitoring**\ (\ )

If `true`, the area detects bodies or areas entering and exiting it.


----



[int<class_int>] **priority** = `0` [🔗<class_Area3D_property_priority>]


- |void| **set_priority**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_priority**\ (\ )

The area's priority. Higher priority areas are processed first. The [World3D<class_World3D>]'s physics is always processed last, after all areas.


----



[float<class_float>] **reverb_bus_amount** = `0.0` [🔗<class_Area3D_property_reverb_bus_amount>]


- |void| **set_reverb_amount**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_reverb_amount**\ (\ )

The degree to which this area applies reverb to its associated audio. Ranges from `0` to `1` with `0.1` precision.


----



[bool<class_bool>] **reverb_bus_enabled** = `false` [🔗<class_Area3D_property_reverb_bus_enabled>]


- |void| **set_use_reverb_bus**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_using_reverb_bus**\ (\ )

If `true`, the area applies reverb to its associated audio.


----



[StringName<class_StringName>] **reverb_bus_name** = `&"Master"` [🔗<class_Area3D_property_reverb_bus_name>]


- |void| **set_reverb_bus_name**\ (\ value\: [StringName<class_StringName>]\ )
- [StringName<class_StringName>] **get_reverb_bus_name**\ (\ )

The name of the reverb bus to use for this area's associated audio.


----



[float<class_float>] **reverb_bus_uniformity** = `0.0` [🔗<class_Area3D_property_reverb_bus_uniformity>]


- |void| **set_reverb_uniformity**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_reverb_uniformity**\ (\ )

The degree to which this area's reverb is a uniform effect. Ranges from `0` to `1` with `0.1` precision.


----



[float<class_float>] **wind_attenuation_factor** = `0.0` [🔗<class_Area3D_property_wind_attenuation_factor>]


- |void| **set_wind_attenuation_factor**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_wind_attenuation_factor**\ (\ )

The exponential rate at which wind force decreases with distance from its origin.

\ **Note:** This wind force only applies to [SoftBody3D<class_SoftBody3D>] nodes. Other physics bodies are currently not affected by wind.


----



[float<class_float>] **wind_force_magnitude** = `0.0` [🔗<class_Area3D_property_wind_force_magnitude>]


- |void| **set_wind_force_magnitude**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_wind_force_magnitude**\ (\ )

The magnitude of area-specific wind force.

\ **Note:** This wind force only applies to [SoftBody3D<class_SoftBody3D>] nodes. Other physics bodies are currently not affected by wind.


----



[NodePath<class_NodePath>] **wind_source_path** = `NodePath("")` [🔗<class_Area3D_property_wind_source_path>]


- |void| **set_wind_source_path**\ (\ value\: [NodePath<class_NodePath>]\ )
- [NodePath<class_NodePath>] **get_wind_source_path**\ (\ )

The [Node3D<class_Node3D>] which is used to specify the direction and origin of an area-specific wind force. The direction is opposite to the z-axis of the [Node3D<class_Node3D>]'s local transform, and its origin is the origin of the [Node3D<class_Node3D>]'s local transform.

\ **Note:** This wind force only applies to [SoftBody3D<class_SoftBody3D>] nodes. Other physics bodies are currently not affected by wind.


----


## Method Descriptions



[Array<class_Array>]\[[Area3D<class_Area3D>]\] **get_overlapping_areas**\ (\ ) |const| [🔗<class_Area3D_method_get_overlapping_areas>]

Returns a list of intersecting **Area3D**\ s. The overlapping area's [CollisionObject3D.collision_layer<class_CollisionObject3D_property_collision_layer>] must be part of this area's [CollisionObject3D.collision_mask<class_CollisionObject3D_property_collision_mask>] in order to be detected.

For performance reasons (collisions are all processed at the same time) this list is modified once during the physics step, not immediately after objects are moved. Consider using signals instead.


----



[Array<class_Array>]\[[Node3D<class_Node3D>]\] **get_overlapping_bodies**\ (\ ) |const| [🔗<class_Area3D_method_get_overlapping_bodies>]

Returns a list of intersecting [PhysicsBody3D<class_PhysicsBody3D>]\ s and [GridMap<class_GridMap>]\ s. The overlapping body's [CollisionObject3D.collision_layer<class_CollisionObject3D_property_collision_layer>] must be part of this area's [CollisionObject3D.collision_mask<class_CollisionObject3D_property_collision_mask>] in order to be detected.

For performance reasons (collisions are all processed at the same time) this list is modified once during the physics step, not immediately after objects are moved. Consider using signals instead.


----



[bool<class_bool>] **has_overlapping_areas**\ (\ ) |const| [🔗<class_Area3D_method_has_overlapping_areas>]

Returns `true` if intersecting any **Area3D**\ s, otherwise returns `false`. The overlapping area's [CollisionObject3D.collision_layer<class_CollisionObject3D_property_collision_layer>] must be part of this area's [CollisionObject3D.collision_mask<class_CollisionObject3D_property_collision_mask>] in order to be detected.

For performance reasons (collisions are all processed at the same time) the list of overlapping areas is modified once during the physics step, not immediately after objects are moved. Consider using signals instead.


----



[bool<class_bool>] **has_overlapping_bodies**\ (\ ) |const| [🔗<class_Area3D_method_has_overlapping_bodies>]

Returns `true` if intersecting any [PhysicsBody3D<class_PhysicsBody3D>]\ s or [GridMap<class_GridMap>]\ s, otherwise returns `false`. The overlapping body's [CollisionObject3D.collision_layer<class_CollisionObject3D_property_collision_layer>] must be part of this area's [CollisionObject3D.collision_mask<class_CollisionObject3D_property_collision_mask>] in order to be detected.

For performance reasons (collisions are all processed at the same time) the list of overlapping bodies is modified once during the physics step, not immediately after objects are moved. Consider using signals instead.


----



[bool<class_bool>] **overlaps_area**\ (\ area\: [Node<class_Node>]\ ) |const| [🔗<class_Area3D_method_overlaps_area>]

Returns `true` if the given **Area3D** intersects or overlaps this **Area3D**, `false` otherwise.

\ **Note:** The result of this test is not immediate after moving objects. For performance, list of overlaps is updated once per frame and before the physics step. Consider using signals instead.


----



[bool<class_bool>] **overlaps_body**\ (\ body\: [Node<class_Node>]\ ) |const| [🔗<class_Area3D_method_overlaps_body>]

Returns `true` if the given physics body intersects or overlaps this **Area3D**, `false` otherwise.

\ **Note:** The result of this test is not immediate after moving objects. For performance, list of overlaps is updated once per frame and before the physics step. Consider using signals instead.

The `body` argument can either be a [PhysicsBody3D<class_PhysicsBody3D>] or a [GridMap<class_GridMap>] instance. While GridMaps are not physics body themselves, they register their tiles with collision shapes as a virtual physics body.

