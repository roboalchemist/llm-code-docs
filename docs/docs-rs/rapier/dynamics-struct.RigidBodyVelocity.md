rapier3d::dynamics

# Struct RigidBodyVelocity

Source

```
pub struct RigidBodyVelocity<T: ScalarType> {
    pub linvel: T::Vector,
    pub angvel: T::AngVector,
}
```

## Fields§

§`linvel: T::Vector`

The linear velocity of the rigid-body.
§`angvel: T::AngVector`

The angular velocity of the rigid-body.

## Implementations§
