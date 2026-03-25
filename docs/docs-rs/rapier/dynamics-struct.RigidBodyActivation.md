rapier3d::dynamics

# Struct RigidBodyActivation

Source

```
pub struct RigidBodyActivation {
    pub normalized_linear_threshold: f32,
    pub angular_threshold: f32,
    pub time_until_sleep: f32,
    pub time_since_can_sleep: f32,
    pub sleeping: bool,
    /* private fields */
}
```

## Fields§

§`normalized_linear_threshold: f32`

Linear velocity threshold for sleeping (scaled by `length_unit`).

If negative, body never sleeps. Default: 0.4 (in length units/second).
§`angular_threshold: f32`

Angular velocity threshold for sleeping (radians/second).

If negative, body never sleeps. Default: 0.5 rad/s.
§`time_until_sleep: f32`

How long the body must be still before sleeping (seconds).

Default: 2.0 seconds. Must be below both velocity thresholds for this duration.
§`time_since_can_sleep: f32`

Internal timer tracking how long body has been still.
§`sleeping: bool`

Is this body currently sleeping?

## Implementations§
