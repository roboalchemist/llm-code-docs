rapier3d::dynamics

# Struct RigidBodyBuilder

Source

```
pub struct RigidBodyBuilder {}
```

## Fields§

§`position: Pose`

The initial position of the rigid-body to be built.
§`linvel: Vector`

The linear velocity of the rigid-body to be built.
§`angvel: AngVector`

The angular velocity of the rigid-body to be built.
§`gravity_scale: f32`

The scale factor applied to the gravity affecting the rigid-body to be built, `1.0` by default.
§`linear_damping: f32`

Damping factor for gradually slowing down the translational motion of the rigid-body, `0.0` by default.
§`angular_damping: f32`

Damping factor for gradually slowing down the angular motion of the rigid-body, `0.0` by default.
§`body_type: RigidBodyType`

The type of rigid-body being constructed.
§`can_sleep: bool`

Whether the rigid-body to be created can sleep if it reaches a dynamic equilibrium.
§`sleeping: bool`

Whether the rigid-body is to be created asleep.
§`ccd_enabled: bool`

Whether Continuous Collision-Detection is enabled for the rigid-body to be built.

CCD prevents tunneling, but may still allow limited interpenetration of colliders.
§`soft_ccd_prediction: f32`

The maximum prediction distance Soft Continuous Collision-Detection.

When set to 0, soft CCD is disabled. Soft-CCD helps prevent tunneling especially of
slow-but-thin to moderately fast objects. The soft CCD prediction distance indicates how
far in the object’s path the CCD algorithm is allowed to inspect. Large values can impact
performance badly by increasing the work needed from the broad-phase.

It is a generally cheaper variant of regular CCD (that can be enabled with
`RigidBodyBuilder::ccd_enabled` since it relies on predictive constraints instead of
shape-cast and substeps.
§`dominance_group: i8`

The dominance group of the rigid-body to be built.
§`enabled: bool`

Will the rigid-body being built be enabled?
§`user_data: u128`

An arbitrary user-defined 128-bit integer associated to the rigid-bodies built by this builder.
§`additional_solver_iterations: usize`

The additional number of solver iterations run for this rigid-body and
everything interacting with it.

See `RigidBody::set_additional_solver_iterations` for additional information.
§`gyroscopic_forces_enabled: bool`

Are gyroscopic forces enabled for this rigid-body?

## Implementations§
