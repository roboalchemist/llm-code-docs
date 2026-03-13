rapier3d::dynamics

# Struct InverseKinematicsOption

Source

```
pub struct InverseKinematicsOption {
    pub damping: f32,
    pub max_iters: usize,
    pub constrained_axes: JointAxesMask,
    pub epsilon_linear: f32,
    pub epsilon_angular: f32,
}
```

## Fields§

§`damping: f32`

A damping coefficient.

Small value can lead to overshooting preventing convergence. Large
values can slow down convergence, requiring more iterations to converge.
§`max_iters: usize`

The maximum number of iterations the iterative IK solver can take.
§`constrained_axes: JointAxesMask`

The axes the IK solver will solve for.
§`epsilon_linear: f32`

The error threshold on the linear error.

If errors on both linear and angular parts fall below this
threshold, the iterative resolution will stop.
§`epsilon_angular: f32`

The error threshold on the angular error.

If errors on both linear and angular parts fall below this
threshold, the iterative resolution will stop.

## Trait Implementations§
