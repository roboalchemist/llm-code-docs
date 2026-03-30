rapier3d::control

# Struct Wheel

Source

```
pub struct Wheel {}
```

## Fields§

§`chassis_connection_point_cs: Vector`

The position of the wheel, relative to the chassis.
§`direction_cs: Vector`

The direction of the wheel’s suspension, relative to the chassis.

The ray-casting will happen following this direction to detect the ground.
§`axle_cs: Vector`

The wheel’s axle axis, relative to the chassis.
§`suspension_rest_length: f32`

The rest length of the wheel’s suspension spring.
§`max_suspension_travel: f32`

The maximum distance the suspension can travel before and after its resting length.
§`radius: f32`

The wheel’s radius.
§`suspension_stiffness: f32`

The suspension stiffness.

Increase this value if the suspension appears to not push the vehicle strong enough.
§`damping_compression: f32`

The suspension’s damping when it is being compressed.
§`damping_relaxation: f32`

The suspension’s damping when it is being released.

Increase this value if the suspension appears to overshoot.
§`friction_slip: f32`

Parameter controlling how much traction the tire has.

The larger the value, the more instantaneous braking will happen (with the risk of
causing the vehicle to flip if it’s too strong).
§`side_friction_stiffness: f32`

The multiplier of friction between a tire and the collider it’s on top of.
§`rotation: f32`

The wheel’s current rotation on its axle.
§`max_suspension_force: f32`

The maximum force applied by the suspension.
§`forward_impulse: f32`

The forward impulses applied by the wheel on the chassis.
§`side_impulse: f32`

The side impulses applied by the wheel on the chassis.
§`steering: f32`

The steering angle for this wheel.
§`engine_force: f32`

The forward force applied by this wheel on the chassis.
§`brake: f32`

The maximum amount of braking impulse applied to slow down the vehicle.
§`wheel_suspension_force: f32`

The force applied by the suspension.

## Implementations§
