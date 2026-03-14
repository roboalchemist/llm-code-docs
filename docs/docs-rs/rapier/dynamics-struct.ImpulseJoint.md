rapier3d::dynamics

# Struct ImpulseJoint

Source

```
pub struct ImpulseJoint {
    pub body1: RigidBodyHandle,
    pub body2: RigidBodyHandle,
    pub data: GenericJoint,
    pub impulses: SpatialVector,
    /* private fields */
}
```

## Fields§

§`body1: RigidBodyHandle`

Handle to the first body attached to this joint.
§`body2: RigidBodyHandle`

Handle to the second body attached to this joint.
§`data: GenericJoint`

The joint’s description.
§`impulses: SpatialVector`

The impulses applied by this joint.

## Trait Implementations§
