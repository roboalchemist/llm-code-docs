rapier3d::control

# Struct WheelTuning

Source

```
pub struct WheelTuning {
    pub suspension_stiffness: f32,
    pub suspension_compression: f32,
    pub suspension_damping: f32,
    pub max_suspension_travel: f32,
    pub side_friction_stiffness: f32,
    pub friction_slip: f32,
    pub max_suspension_force: f32,
}
```

## Fields§

§`suspension_stiffness: f32`

The suspension stiffness.

Increase this value if the suspension appears to not push the vehicle strong enough.
§`suspension_compression: f32`

The suspension’s damping when it is being compressed.
§`suspension_damping: f32`

The suspension’s damping when it is being released.

Increase this value if the suspension appears to overshoot.
§`max_suspension_travel: f32`

The maximum distance the suspension can travel before and after its resting length.
§`side_friction_stiffness: f32`

The multiplier of friction between a tire and the collider it’s on top of.
§`friction_slip: f32`

Parameter controlling how much traction the tire has.

The larger the value, the more instantaneous braking will happen (with the risk of
causing the vehicle to flip if it’s too strong).
§`max_suspension_force: f32`

The maximum force applied by the suspension.

## Trait Implementations§
