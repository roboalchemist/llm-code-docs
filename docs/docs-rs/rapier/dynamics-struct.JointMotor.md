rapier3d::dynamics

# Struct JointMotor

Source

```
pub struct JointMotor {
    pub target_vel: f32,
    pub target_pos: f32,
    pub stiffness: f32,
    pub damping: f32,
    pub max_force: f32,
    pub impulse: f32,
    pub model: MotorModel,
}
```

## Fields§

§`target_vel: f32`

Target velocity (units/sec for prismatic, rad/sec for revolute).
§`target_pos: f32`

Target position (units for prismatic, radians for revolute).
§`stiffness: f32`

Spring constant - how strongly to pull toward target position.
§`damping: f32`

Damping coefficient - resistance to motion (prevents oscillation).
§`max_force: f32`

Maximum force the motor can apply (Newtons for prismatic, Nm for revolute).
§`impulse: f32`

Internal: current impulse being applied.
§`model: MotorModel`

Force-based or acceleration-based motor model.

## Trait Implementations§
