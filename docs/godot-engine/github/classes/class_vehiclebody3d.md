:github_url: hide



# VehicleBody3D

**Inherits:** [RigidBody3D<class_RigidBody3D>] **<** [PhysicsBody3D<class_PhysicsBody3D>] **<** [CollisionObject3D<class_CollisionObject3D>] **<** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A 3D physics body that simulates the behavior of a car.


## Description

This physics body implements all the physics logic needed to simulate a car. It is based on the raycast vehicle system commonly found in physics engines. Aside from a [CollisionShape3D<class_CollisionShape3D>] for the main body of the vehicle, you must also add a [VehicleWheel3D<class_VehicleWheel3D>] node for each wheel. You should also add a [MeshInstance3D<class_MeshInstance3D>] to this node for the 3D model of the vehicle, but this model should generally not include meshes for the wheels. You can control the vehicle by using the [brake<class_VehicleBody3D_property_brake>], [engine_force<class_VehicleBody3D_property_engine_force>], and [steering<class_VehicleBody3D_property_steering>] properties. The position or orientation of this node shouldn't be changed directly.

\ **Note:** The local forward for this node is [Vector3.MODEL_FRONT<class_Vector3_constant_MODEL_FRONT>].

\ **Note:** The origin point of your VehicleBody3D will determine the center of gravity of your vehicle. To make the vehicle more grounded, the origin point is usually kept low, moving the [CollisionShape3D<class_CollisionShape3D>] and [MeshInstance3D<class_MeshInstance3D>] upwards.

\ **Note:** This class has known issues and isn't designed to provide realistic 3D vehicle physics. If you want advanced vehicle physics, you may have to write your own physics integration using [CharacterBody3D<class_CharacterBody3D>] or [RigidBody3D<class_RigidBody3D>].


## Tutorials

- [../tutorials/physics/physics_introduction](Physics introduction .md)

- [../tutorials/physics/troubleshooting_physics_issues](Troubleshooting physics issues .md)

- [3D Truck Town Demo ](https://godotengine.org/asset-library/asset/2752)_


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+----------------------------------------------------------------+--------------------------------------------------------------------------+
> | :ref:`float<class_float>` | :ref:`brake<class_VehicleBody3D_property_brake>`               | ``0.0``                                                                  |
> +---------------------------+----------------------------------------------------------------+--------------------------------------------------------------------------+
> | :ref:`float<class_float>` | :ref:`engine_force<class_VehicleBody3D_property_engine_force>` | ``0.0``                                                                  |
> +---------------------------+----------------------------------------------------------------+--------------------------------------------------------------------------+
> | :ref:`float<class_float>` | mass                                                           | ``40.0`` (overrides :ref:`RigidBody3D<class_RigidBody3D_property_mass>`) |
> +---------------------------+----------------------------------------------------------------+--------------------------------------------------------------------------+
> | :ref:`float<class_float>` | :ref:`steering<class_VehicleBody3D_property_steering>`         | ``0.0``                                                                  |
> +---------------------------+----------------------------------------------------------------+--------------------------------------------------------------------------+
>

----


## Property Descriptions



[float<class_float>] **brake** = `0.0` [🔗<class_VehicleBody3D_property_brake>]


- |void| **set_brake**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_brake**\ (\ )

Slows down the vehicle by applying a braking force. The vehicle is only slowed down if the wheels are in contact with a surface. The force you need to apply to adequately slow down your vehicle depends on the [RigidBody3D.mass<class_RigidBody3D_property_mass>] of the vehicle. For a vehicle with a mass set to 1000, try a value in the 25 - 30 range for hard braking.


----



[float<class_float>] **engine_force** = `0.0` [🔗<class_VehicleBody3D_property_engine_force>]


- |void| **set_engine_force**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_engine_force**\ (\ )

Accelerates the vehicle by applying an engine force. The vehicle is only sped up if the wheels that have [VehicleWheel3D.use_as_traction<class_VehicleWheel3D_property_use_as_traction>] set to `true` and are in contact with a surface. The [RigidBody3D.mass<class_RigidBody3D_property_mass>] of the vehicle has an effect on the acceleration of the vehicle. For a vehicle with a mass set to 1000, try a value in the 25 - 50 range for acceleration.

\ **Note:** The simulation does not take the effect of gears into account, you will need to add logic for this if you wish to simulate gears.

A negative value will result in the vehicle reversing.


----



[float<class_float>] **steering** = `0.0` [🔗<class_VehicleBody3D_property_steering>]


- |void| **set_steering**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_steering**\ (\ )

The steering angle for the vehicle. Setting this to a non-zero value will result in the vehicle turning when it's moving. Wheels that have [VehicleWheel3D.use_as_steering<class_VehicleWheel3D_property_use_as_steering>] set to `true` will automatically be rotated.

\ **Note:** This property is edited in the inspector in degrees. In code the property is set in radians.

