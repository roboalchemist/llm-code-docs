# VehicleBody3D

# VehicleBody3D

Inherits:RigidBody3D<PhysicsBody3D<CollisionObject3D<Node3D<Node<Object
A 3D physics body that simulates the behavior of a car.

## Description

This physics body implements all the physics logic needed to simulate a car. It is based on the raycast vehicle system commonly found in physics engines. Aside from aCollisionShape3Dfor the main body of the vehicle, you must also add aVehicleWheel3Dnode for each wheel. You should also add aMeshInstance3Dto this node for the 3D model of the vehicle, but this model should generally not include meshes for the wheels. You can control the vehicle by using thebrake,engine_force, andsteeringproperties. The position or orientation of this node shouldn't be changed directly.
Note:The local forward for this node isVector3.MODEL_FRONT.
Note:The origin point of your VehicleBody3D will determine the center of gravity of your vehicle. To make the vehicle more grounded, the origin point is usually kept low, moving theCollisionShape3DandMeshInstance3Dupwards.
Note:This class has known issues and isn't designed to provide realistic 3D vehicle physics. If you want advanced vehicle physics, you may have to write your own physics integration usingCharacterBody3DorRigidBody3D.

## Tutorials

- Physics introduction
Physics introduction
- Troubleshooting physics issues
Troubleshooting physics issues
- 3D Truck Town Demo
3D Truck Town Demo

## Properties

| float | brake | 0.0 |
|---|---|---|
| float | engine_force | 0.0 |
| float | mass | 40.0(overridesRigidBody3D) |
| float | steering | 0.0 |

float
brake
float
engine_force
float
mass
40.0(overridesRigidBody3D)
float
steering

## Property Descriptions

floatbrake=0.0🔗

- voidset_brake(value:float)
voidset_brake(value:float)
- floatget_brake()
floatget_brake()
Slows down the vehicle by applying a braking force. The vehicle is only slowed down if the wheels are in contact with a surface. The force you need to apply to adequately slow down your vehicle depends on theRigidBody3D.massof the vehicle. For a vehicle with a mass set to 1000, try a value in the 25 - 30 range for hard braking.
floatengine_force=0.0🔗
- voidset_engine_force(value:float)
voidset_engine_force(value:float)
- floatget_engine_force()
floatget_engine_force()
Accelerates the vehicle by applying an engine force. The vehicle is only sped up if the wheels that haveVehicleWheel3D.use_as_tractionset totrueand are in contact with a surface. TheRigidBody3D.massof the vehicle has an effect on the acceleration of the vehicle. For a vehicle with a mass set to 1000, try a value in the 25 - 50 range for acceleration.
Note:The simulation does not take the effect of gears into account, you will need to add logic for this if you wish to simulate gears.
A negative value will result in the vehicle reversing.
floatsteering=0.0🔗
- voidset_steering(value:float)
voidset_steering(value:float)
- floatget_steering()
floatget_steering()
The steering angle for the vehicle. Setting this to a non-zero value will result in the vehicle turning when it's moving. Wheels that haveVehicleWheel3D.use_as_steeringset totruewill automatically be rotated.
Note:This property is edited in the inspector in degrees. In code the property is set in radians.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
