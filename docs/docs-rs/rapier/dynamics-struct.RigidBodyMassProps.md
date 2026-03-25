rapier3d::dynamics

# Struct RigidBodyMassProps

Source

```
pub struct RigidBodyMassProps {
    pub world_com: Vector,
    pub effective_inv_mass: Vector,
    pub effective_world_inv_inertia: AngularInertia,
    pub local_mprops: MassProperties,
    pub flags: LockedAxes,
    pub additional_local_mprops: Option<Box<RigidBodyAdditionalMassProps>>,
}
```

## Fields§

§`world_com: Vector`

The world-space center of mass of the rigid-body.
§`effective_inv_mass: Vector`

The inverse mass taking into account translation locking.
§`effective_world_inv_inertia: AngularInertia`

The square-root of the world-space inverse angular inertia tensor of the rigid-body,
taking into account rotation locking.
§`local_mprops: MassProperties`

The local mass properties of the rigid-body.
§`flags: LockedAxes`

Flags for locking rotation and translation.
§`additional_local_mprops: Option<Box<RigidBodyAdditionalMassProps>>`

Mass-properties of this rigid-bodies, added to the contributions of its attached colliders.

## Implementations§
