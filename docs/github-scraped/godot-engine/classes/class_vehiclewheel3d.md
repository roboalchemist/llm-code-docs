:github_url: hide



# VehicleWheel3D

**Inherits:** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A 3D physics body for a [VehicleBody3D<class_VehicleBody3D>] that simulates the behavior of a wheel.


## Description

A node used as a child of a [VehicleBody3D<class_VehicleBody3D>] parent to simulate the behavior of one of its wheels. This node also acts as a collider to detect if the wheel is touching a surface.

\ **Note:** This class has known issues and isn't designed to provide realistic 3D vehicle physics. If you want advanced vehicle physics, you may need to write your own physics integration using another [PhysicsBody3D<class_PhysicsBody3D>] class.


## Tutorials

- [3D Truck Town Demo ](https://godotengine.org/asset-library/asset/2752)_


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------------------------+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                           | :ref:`brake<class_VehicleWheel3D_property_brake>`                               | ``0.0``                                                                       |
> +---------------------------------------------------------------------+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                           | :ref:`damping_compression<class_VehicleWheel3D_property_damping_compression>`   | ``0.83``                                                                      |
> +---------------------------------------------------------------------+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                           | :ref:`damping_relaxation<class_VehicleWheel3D_property_damping_relaxation>`     | ``0.88``                                                                      |
> +---------------------------------------------------------------------+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                           | :ref:`engine_force<class_VehicleWheel3D_property_engine_force>`                 | ``0.0``                                                                       |
> +---------------------------------------------------------------------+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
> | :ref:`PhysicsInterpolationMode<enum_Node_PhysicsInterpolationMode>` | physics_interpolation_mode                                                      | ``2`` (overrides :ref:`Node<class_Node_property_physics_interpolation_mode>`) |
> +---------------------------------------------------------------------+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                           | :ref:`steering<class_VehicleWheel3D_property_steering>`                         | ``0.0``                                                                       |
> +---------------------------------------------------------------------+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                           | :ref:`suspension_max_force<class_VehicleWheel3D_property_suspension_max_force>` | ``6000.0``                                                                    |
> +---------------------------------------------------------------------+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                           | :ref:`suspension_stiffness<class_VehicleWheel3D_property_suspension_stiffness>` | ``5.88``                                                                      |
> +---------------------------------------------------------------------+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                           | :ref:`suspension_travel<class_VehicleWheel3D_property_suspension_travel>`       | ``0.2``                                                                       |
> +---------------------------------------------------------------------+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                             | :ref:`use_as_steering<class_VehicleWheel3D_property_use_as_steering>`           | ``false``                                                                     |
> +---------------------------------------------------------------------+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                             | :ref:`use_as_traction<class_VehicleWheel3D_property_use_as_traction>`           | ``false``                                                                     |
> +---------------------------------------------------------------------+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                           | :ref:`wheel_friction_slip<class_VehicleWheel3D_property_wheel_friction_slip>`   | ``10.5``                                                                      |
> +---------------------------------------------------------------------+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                           | :ref:`wheel_radius<class_VehicleWheel3D_property_wheel_radius>`                 | ``0.5``                                                                       |
> +---------------------------------------------------------------------+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                           | :ref:`wheel_rest_length<class_VehicleWheel3D_property_wheel_rest_length>`       | ``0.15``                                                                      |
> +---------------------------------------------------------------------+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                           | :ref:`wheel_roll_influence<class_VehicleWheel3D_property_wheel_roll_influence>` | ``0.1``                                                                       |
> +---------------------------------------------------------------------+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------+-----------------------------------------------------------------------------------------+
> | :ref:`Node3D<class_Node3D>`   | :ref:`get_contact_body<class_VehicleWheel3D_method_get_contact_body>`\ (\ ) |const|     |
> +-------------------------------+-----------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>` | :ref:`get_contact_normal<class_VehicleWheel3D_method_get_contact_normal>`\ (\ ) |const| |
> +-------------------------------+-----------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>` | :ref:`get_contact_point<class_VehicleWheel3D_method_get_contact_point>`\ (\ ) |const|   |
> +-------------------------------+-----------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`     | :ref:`get_rpm<class_VehicleWheel3D_method_get_rpm>`\ (\ ) |const|                       |
> +-------------------------------+-----------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`     | :ref:`get_skidinfo<class_VehicleWheel3D_method_get_skidinfo>`\ (\ ) |const|             |
> +-------------------------------+-----------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`       | :ref:`is_in_contact<class_VehicleWheel3D_method_is_in_contact>`\ (\ ) |const|           |
> +-------------------------------+-----------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[float<class_float>] **brake** = `0.0` [🔗<class_VehicleWheel3D_property_brake>]


- |void| **set_brake**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_brake**\ (\ )

Slows down the wheel by applying a braking force. The wheel is only slowed down if it is in contact with a surface. The force you need to apply to adequately slow down your vehicle depends on the [RigidBody3D.mass<class_RigidBody3D_property_mass>] of the vehicle. For a vehicle with a mass set to 1000, try a value in the 25 - 30 range for hard braking.


----



[float<class_float>] **damping_compression** = `0.83` [🔗<class_VehicleWheel3D_property_damping_compression>]


- |void| **set_damping_compression**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_damping_compression**\ (\ )

The damping applied to the suspension spring when being compressed, meaning when the wheel is moving up relative to the vehicle. It is measured in Newton-seconds per millimeter (N⋅s/mm), or megagrams per second (Mg/s). This value should be between 0.0 (no damping) and 1.0, but may be more. A value of 0.0 means the car will keep bouncing as the spring keeps its energy. A good value for this is around 0.3 for a normal car, 0.5 for a race car.


----



[float<class_float>] **damping_relaxation** = `0.88` [🔗<class_VehicleWheel3D_property_damping_relaxation>]


- |void| **set_damping_relaxation**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_damping_relaxation**\ (\ )

The damping applied to the suspension spring when rebounding or extending, meaning when the wheel is moving down relative to the vehicle. It is measured in Newton-seconds per millimeter (N⋅s/mm), or megagrams per second (Mg/s). This value should be between 0.0 (no damping) and 1.0, but may be more. This value should always be slightly higher than the [damping_compression<class_VehicleWheel3D_property_damping_compression>] property. For a [damping_compression<class_VehicleWheel3D_property_damping_compression>] value of 0.3, try a relaxation value of 0.5.


----



[float<class_float>] **engine_force** = `0.0` [🔗<class_VehicleWheel3D_property_engine_force>]


- |void| **set_engine_force**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_engine_force**\ (\ )

Accelerates the wheel by applying an engine force. The wheel is only sped up if it is in contact with a surface. The [RigidBody3D.mass<class_RigidBody3D_property_mass>] of the vehicle has an effect on the acceleration of the vehicle. For a vehicle with a mass set to 1000, try a value in the 25 - 50 range for acceleration.

\ **Note:** The simulation does not take the effect of gears into account, you will need to add logic for this if you wish to simulate gears.

A negative value will result in the wheel reversing.


----



[float<class_float>] **steering** = `0.0` [🔗<class_VehicleWheel3D_property_steering>]


- |void| **set_steering**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_steering**\ (\ )

The steering angle for the wheel, in radians. Setting this to a non-zero value will result in the vehicle turning when it's moving.


----



[float<class_float>] **suspension_max_force** = `6000.0` [🔗<class_VehicleWheel3D_property_suspension_max_force>]


- |void| **set_suspension_max_force**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_suspension_max_force**\ (\ )

The maximum force the spring can resist. This value should be higher than a quarter of the [RigidBody3D.mass<class_RigidBody3D_property_mass>] of the [VehicleBody3D<class_VehicleBody3D>] or the spring will not carry the weight of the vehicle. Good results are often obtained by a value that is about 3× to 4× this number.


----



[float<class_float>] **suspension_stiffness** = `5.88` [🔗<class_VehicleWheel3D_property_suspension_stiffness>]


- |void| **set_suspension_stiffness**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_suspension_stiffness**\ (\ )

The stiffness of the suspension, measured in Newtons per millimeter (N/mm), or megagrams per second squared (Mg/s²). Use a value lower than 50 for an off-road car, a value between 50 and 100 for a race car and try something around 200 for something like a Formula 1 car.


----



[float<class_float>] **suspension_travel** = `0.2` [🔗<class_VehicleWheel3D_property_suspension_travel>]


- |void| **set_suspension_travel**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_suspension_travel**\ (\ )

This is the distance the suspension can travel. As Godot units are equivalent to meters, keep this setting relatively low. Try a value between 0.1 and 0.3 depending on the type of car.


----



[bool<class_bool>] **use_as_steering** = `false` [🔗<class_VehicleWheel3D_property_use_as_steering>]


- |void| **set_use_as_steering**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_used_as_steering**\ (\ )

If `true`, this wheel will be turned when the car steers. This value is used in conjunction with [VehicleBody3D.steering<class_VehicleBody3D_property_steering>] and ignored if you are using the per-wheel [steering<class_VehicleWheel3D_property_steering>] value instead.


----



[bool<class_bool>] **use_as_traction** = `false` [🔗<class_VehicleWheel3D_property_use_as_traction>]


- |void| **set_use_as_traction**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_used_as_traction**\ (\ )

If `true`, this wheel transfers engine force to the ground to propel the vehicle forward. This value is used in conjunction with [VehicleBody3D.engine_force<class_VehicleBody3D_property_engine_force>] and ignored if you are using the per-wheel [engine_force<class_VehicleWheel3D_property_engine_force>] value instead.


----



[float<class_float>] **wheel_friction_slip** = `10.5` [🔗<class_VehicleWheel3D_property_wheel_friction_slip>]


- |void| **set_friction_slip**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_friction_slip**\ (\ )

This determines how much grip this wheel has. It is combined with the friction setting of the surface the wheel is in contact with. 0.0 means no grip, 1.0 is normal grip. For a drift car setup, try setting the grip of the rear wheels slightly lower than the front wheels, or use a lower value to simulate tire wear.

It's best to set this to 1.0 when starting out.


----



[float<class_float>] **wheel_radius** = `0.5` [🔗<class_VehicleWheel3D_property_wheel_radius>]


- |void| **set_radius**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_radius**\ (\ )

The radius of the wheel in meters.


----



[float<class_float>] **wheel_rest_length** = `0.15` [🔗<class_VehicleWheel3D_property_wheel_rest_length>]


- |void| **set_suspension_rest_length**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_suspension_rest_length**\ (\ )

This is the distance in meters the wheel is lowered from its origin point. Don't set this to 0.0 and move the wheel into position, instead move the origin point of your wheel (the gizmo in Godot) to the position the wheel will take when bottoming out, then use the rest length to move the wheel down to the position it should be in when the car is in rest.


----



[float<class_float>] **wheel_roll_influence** = `0.1` [🔗<class_VehicleWheel3D_property_wheel_roll_influence>]


- |void| **set_roll_influence**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_roll_influence**\ (\ )

This value affects the roll of your vehicle. If set to 1.0 for all wheels, your vehicle will resist body roll, while a value of 0.0 will be prone to rolling over.


----


## Method Descriptions



[Node3D<class_Node3D>] **get_contact_body**\ (\ ) |const| [🔗<class_VehicleWheel3D_method_get_contact_body>]

Returns the contacting body node if valid in the tree, as [Node3D<class_Node3D>]. At the moment, [GridMap<class_GridMap>] is not supported so the node will be always of type [PhysicsBody3D<class_PhysicsBody3D>].

Returns `null` if the wheel is not in contact with a surface, or the contact body is not a [PhysicsBody3D<class_PhysicsBody3D>].


----



[Vector3<class_Vector3>] **get_contact_normal**\ (\ ) |const| [🔗<class_VehicleWheel3D_method_get_contact_normal>]

Returns the normal of the suspension's collision in world space if the wheel is in contact. If the wheel isn't in contact with anything, returns a vector pointing directly along the suspension axis toward the vehicle in world space.


----



[Vector3<class_Vector3>] **get_contact_point**\ (\ ) |const| [🔗<class_VehicleWheel3D_method_get_contact_point>]

Returns the point of the suspension's collision in world space if the wheel is in contact. If the wheel isn't in contact with anything, returns the maximum point of the wheel's ray cast in world space, which is defined by `wheel_rest_length + wheel_radius`.


----



[float<class_float>] **get_rpm**\ (\ ) |const| [🔗<class_VehicleWheel3D_method_get_rpm>]

Returns the rotational speed of the wheel in revolutions per minute.


----



[float<class_float>] **get_skidinfo**\ (\ ) |const| [🔗<class_VehicleWheel3D_method_get_skidinfo>]

Returns a value between 0.0 and 1.0 that indicates whether this wheel is skidding. 0.0 is skidding (the wheel has lost grip, e.g. icy terrain), 1.0 means not skidding (the wheel has full grip, e.g. dry asphalt road).


----



[bool<class_bool>] **is_in_contact**\ (\ ) |const| [🔗<class_VehicleWheel3D_method_is_in_contact>]

Returns `true` if this wheel is in contact with a surface.

