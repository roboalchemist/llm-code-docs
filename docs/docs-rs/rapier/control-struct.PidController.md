rapier3d::control

# Struct PidController

Source

```
pub struct PidController {
    pub pd: PdController,
    pub lin_integral: Vector,
    pub ang_integral: AngVector,
    pub lin_ki: Vector,
    pub ang_ki: AngVector,
}
```

## Fields§

§`pd: PdController`

The Proportional-Derivative (PD) part of this PID controller.
§`lin_integral: Vector`

The translational error accumulated through time for the Integral part of the PID controller.
§`ang_integral: AngVector`

The angular error accumulated through time for the Integral part of the PID controller.
§`lin_ki: Vector`

The linear gain applied to the Integral part of the PID controller.
§`ang_ki: AngVector`

The angular gain applied to the Integral part of the PID controller.

## Implementations§
