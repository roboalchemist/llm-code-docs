rapier3d::control

# Struct PdController

Source

```
pub struct PdController {
    pub lin_kp: Vector,
    pub lin_kd: Vector,
    pub ang_kp: AngVector,
    pub ang_kd: AngVector,
    pub axes: AxesMask,
}
```

## Fields§

§`lin_kp: Vector`

The Proportional gain applied to the instantaneous linear position errors.

This is usually set to a multiple of the inverse of simulation step time
(e.g. `60` if the delta-time is `1.0 / 60.0`).
§`lin_kd: Vector`

The Derivative gain applied to the instantaneous linear velocity errors.

This is usually set to a value in `[0.0, 1.0]` where `0.0` implies no damping
(no correction of velocity errors) and `1.0` implies complete damping (velocity errors
are corrected in a single simulation step).
§`ang_kp: AngVector`

The Proportional gain applied to the instantaneous angular position errors.

This is usually set to a multiple of the inverse of simulation step time
(e.g. `60` if the delta-time is `1.0 / 60.0`).
§`ang_kd: AngVector`

The Derivative gain applied to the instantaneous angular velocity errors.

This is usually set to a value in `[0.0, 1.0]` where `0.0` implies no damping
(no correction of velocity errors) and `1.0` implies complete damping (velocity errors
are corrected in a single simulation step).
§`axes: AxesMask`

The axes affected by this controller.

Only coordinate axes with a bit flags set to `true` will be taken into
account when calculating the errors and corrections.

## Implementations§
