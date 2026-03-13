rapier3d::dynamics

# Struct RigidBodyPosition

Source

```
pub struct RigidBodyPosition {
    pub position: Pose,
    pub next_position: Pose,
}
```

## Fields§

§`position: Pose`

The world-space position of the rigid-body.
§`next_position: Pose`

The next position of the rigid-body.

At the beginning of the timestep, and when the
timestep is complete we must have position == next_position
except for position-based kinematic bodies.

The next_position is updated after the velocity and position
resolution. Then it is either validated (ie. we set position := set_position)
or clamped by CCD.

## Implementations§
