rapier3d::dynamics

# Struct MassProperties

Source

```
pub struct MassProperties {
    pub local_com: Vec3,
    pub inv_mass: f32,
    pub inv_principal_inertia: Vec3,
    pub principal_inertia_local_frame: Quat,
}
```

## Fields§

§`local_com: Vec3`

The center of mass in local (shape-relative) coordinates.

This is the balance point of the object. For symmetric shapes, it’s typically
at the geometric center. All angular inertia calculations are relative to this point.
§`inv_mass: f32`

The inverse of the mass (1 / mass).

- **Positive value**: Normal object with finite mass

- **Zero**: Infinite mass (immovable/static object)

To get the actual mass, use `mass()` method or compute `1.0 / inv_mass`.
§`inv_principal_inertia: Vec3`

The inverse of the principal angular inertia values.

These are the angular inertia values along the principal inertia axes:

- **2D**: Single scalar value (rotation around perpendicular axis)

- **3D**: Vector of three values (rotation around X, Y, Z principal axes)

Angular inertia relative to the center of mass (`local_com`).
Zero components indicate infinite inertia (no rotation) along that axis.
§`principal_inertia_local_frame: Quat`

The rotation from local coordinates to principal inertia axes (3D only).

This rotation aligns the object’s coordinate system with its principal
axes of inertia, where the inertia tensor is diagonal.

## Implementations§
