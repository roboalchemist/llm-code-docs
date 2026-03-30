rapier3d::dynamics

# Struct MultibodyLinkId

Source

```
pub struct MultibodyLinkId {
    pub multibody: MultibodyIndex,
    pub id: usize,
    /* private fields */
}
```

## Fields§

§`multibody: MultibodyIndex`

The multibody index to be used as `&multibody_joint_set[multibody]` to
retrieve the multibody reference.
§`id: usize`

The multibody link index to be given to `Multibody::link`.

## Trait Implementations§
