rapier3d::dynamics

# Struct MultibodyJoint

Source

```
pub struct MultibodyJoint {
    pub data: GenericJoint,
    pub kinematic: bool,
    /* private fields */
}
```

## Fields§

§`data: GenericJoint`

The joint’s description.
§`kinematic: bool`

Is the joint a kinematic joint?

Kinematic joint velocities are never changed by the physics engine. This gives the user
total control over the values of their degrees of freedoms.

## Implementations§
