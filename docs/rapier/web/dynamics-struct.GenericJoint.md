rapier3d::dynamics

# Struct GenericJoint

Source

```
pub struct GenericJoint {
    pub local_frame1: Pose,
    pub local_frame2: Pose,
    pub locked_axes: JointAxesMask,
    pub limit_axes: JointAxesMask,
    pub motor_axes: JointAxesMask,
    pub coupled_axes: JointAxesMask,
    pub limits: [JointLimits<f32>; 6],
    pub motors: [JointMotor; 6],
    pub softness: SpringCoefficients<f32>,
    pub contacts_enabled: bool,
    pub enabled: JointEnabled,
    pub user_data: u128,
}
```

## Fields§

§`local_frame1: Pose`

The joint’s frame, expressed in the first rigid-body’s local-space.
§`local_frame2: Pose`

The joint’s frame, expressed in the second rigid-body’s local-space.
§`locked_axes: JointAxesMask`

The degrees-of-freedoms locked by this joint.
§`limit_axes: JointAxesMask`

The degrees-of-freedoms limited by this joint.
§`motor_axes: JointAxesMask`

The degrees-of-freedoms motorised by this joint.
§`coupled_axes: JointAxesMask`

The coupled degrees of freedom of this joint.

Note that coupling degrees of freedoms (DoF) changes the interpretation of the coupled joint’s limits and motors.
If multiple linear DoF are limited/motorized, only the limits/motor configuration for the first
coupled linear DoF is applied to all coupled linear DoF. Similarly, if multiple angular DoF are limited/motorized
only the limits/motor configuration for the first coupled angular DoF is applied to all coupled angular DoF.
§`limits: [JointLimits<f32>; 6]`

The limits, along each degree of freedoms of this joint.

Note that the limit must also be explicitly enabled by the `limit_axes` bitmask.
For coupled degrees of freedoms (DoF), only the first linear (resp. angular) coupled DoF limit and `limit_axis`
bitmask is applied to the coupled linear (resp. angular) axes.
§`motors: [JointMotor; 6]`

The motors, along each degree of freedoms of this joint.

Note that the motor must also be explicitly enabled by the `motor_axes` bitmask.
For coupled degrees of freedoms (DoF), only the first linear (resp. angular) coupled DoF motor and `motor_axes`
bitmask is applied to the coupled linear (resp. angular) axes.
§`softness: SpringCoefficients<f32>`

The coefficients controlling the joint constraints’ softness.
§`contacts_enabled: bool`

Are contacts between the attached rigid-bodies enabled?
§`enabled: JointEnabled`

Whether the joint is enabled.
§`user_data: u128`

User-defined data associated to this joint.

## Implementations§
