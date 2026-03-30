rapier3d::dynamics

# Struct RigidBodyDamping

Source

```
pub struct RigidBodyDamping<T> {
    pub linear_damping: T,
    pub angular_damping: T,
}
```

## Fields§

§`linear_damping: T`

Damping factor for gradually slowing down the translational motion of the rigid-body.
§`angular_damping: T`

Damping factor for gradually slowing down the angular motion of the rigid-body.

## Trait Implementations§
