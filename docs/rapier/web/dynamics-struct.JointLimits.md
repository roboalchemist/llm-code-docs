rapier3d::dynamics

# Struct JointLimits

Source

```
pub struct JointLimits<N> {
    pub min: N,
    pub max: N,
    pub impulse: N,
}
```

## Fields§

§`min: N`

Minimum allowed value (angle for revolute, distance for prismatic).
§`max: N`

Maximum allowed value (angle for revolute, distance for prismatic).
§`impulse: N`

Internal: impulse being applied to enforce the limit.

## Trait Implementations§
