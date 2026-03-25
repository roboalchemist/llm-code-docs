rapier3d::dynamics

# Struct RigidBodyCcd

Source

```
pub struct RigidBodyCcd {
    pub ccd_thickness: f32,
    pub ccd_max_dist: f32,
    pub ccd_active: bool,
    pub ccd_enabled: bool,
    pub soft_ccd_prediction: f32,
}
```

## Fields§

§`ccd_thickness: f32`

The distance used by the CCD solver to decide if a movement would
result in a tunnelling problem.
§`ccd_max_dist: f32`

The max distance between this rigid-body’s center of mass and its
furthest collider point.
§`ccd_active: bool`

Is CCD active for this rigid-body?

If `self.ccd_enabled` is `true`, then this is automatically set to
`true` when the CCD solver detects that the rigid-body is moving fast
enough to potential cause a tunneling problem.
§`ccd_enabled: bool`

Is CCD enabled for this rigid-body?
§`soft_ccd_prediction: f32`

The soft-CCD prediction distance for this rigid-body.

## Implementations§
