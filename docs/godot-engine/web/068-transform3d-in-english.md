# Transform3D in English

# Transform3D

A 3×4 matrix representing a 3D transformation.

## Description

TheTransform3Dbuilt-inVarianttype is a 3×4 matrix representing a transformation in 3D space. It contains aBasis, which on its own can represent rotation, scale, and shear. Additionally, combined with its ownorigin, the transform can also represent a translation.
For a general introduction, see theMatrices and transformstutorial.
Note:Godot uses aright-handed coordinate system, which is a common standard. For directions, the convention for built-in types likeCamera3Dis for -Z to point forward (+X is right, +Y is up, and +Z is back). Other objects may use different direction conventions. For more information, see the3D asset direction conventionstutorial.
Note
There are notable differences when using this API with C#. SeeC# API differences to GDScriptfor more information.

## Tutorials

- Math documentation index
Math documentation index
- Matrices and transforms
Matrices and transforms
- Using 3D transforms
Using 3D transforms
- Matrix Transform Demo
Matrix Transform Demo
- 3D Platformer Demo
3D Platformer Demo
- 2.5D Game Demo
2.5D Game Demo

## Properties

| Basis | basis | Basis(1,0,0,0,1,0,0,0,1) |
|---|---|---|
| Vector3 | origin | Vector3(0,0,0) |

Basis
basis
Basis(1,0,0,0,1,0,0,0,1)
Vector3
origin
Vector3(0,0,0)

## Constructors

| Transform3D | Transform3D() |
|---|---|
| Transform3D | Transform3D(from:Transform3D) |
| Transform3D | Transform3D(basis:Basis, origin:Vector3) |
| Transform3D | Transform3D(from:Projection) |
| Transform3D | Transform3D(x_axis:Vector3, y_axis:Vector3, z_axis:Vector3, origin:Vector3) |

Transform3D
Transform3D()
Transform3D
Transform3D(from:Transform3D)
Transform3D
Transform3D(basis:Basis, origin:Vector3)
Transform3D
Transform3D(from:Projection)
Transform3D
Transform3D(x_axis:Vector3, y_axis:Vector3, z_axis:Vector3, origin:Vector3)

## Methods

| Transform3D | affine_inverse()const |
|---|---|
| Transform3D | interpolate_with(xform:Transform3D, weight:float)const |
| Transform3D | inverse()const |
| bool | is_equal_approx(xform:Transform3D)const |
| bool | is_finite()const |
| Transform3D | looking_at(target:Vector3, up:Vector3= Vector3(0, 1, 0), use_model_front:bool= false)const |
| Transform3D | orthonormalized()const |
| Transform3D | rotated(axis:Vector3, angle:float)const |
| Transform3D | rotated_local(axis:Vector3, angle:float)const |
| Transform3D | scaled(scale:Vector3)const |
| Transform3D | scaled_local(scale:Vector3)const |
| Transform3D | translated(offset:Vector3)const |
| Transform3D | translated_local(offset:Vector3)const |

Transform3D
affine_inverse()const
Transform3D
interpolate_with(xform:Transform3D, weight:float)const
Transform3D
inverse()const
bool
is_equal_approx(xform:Transform3D)const
bool
is_finite()const
Transform3D
looking_at(target:Vector3, up:Vector3= Vector3(0, 1, 0), use_model_front:bool= false)const
Transform3D
orthonormalized()const
Transform3D
rotated(axis:Vector3, angle:float)const
Transform3D
rotated_local(axis:Vector3, angle:float)const
Transform3D
scaled(scale:Vector3)const
Transform3D
scaled_local(scale:Vector3)const
Transform3D
translated(offset:Vector3)const
Transform3D
translated_local(offset:Vector3)const

## Operators

| bool | operator !=(right:Transform3D) |
|---|---|
| AABB | operator *(right:AABB) |
| PackedVector3Array | operator *(right:PackedVector3Array) |
| Plane | operator *(right:Plane) |
| Transform3D | operator *(right:Transform3D) |
| Vector3 | operator *(right:Vector3) |
| Transform3D | operator *(right:float) |
| Transform3D | operator *(right:int) |
| Transform3D | operator /(right:float) |
| Transform3D | operator /(right:int) |
| bool | operator ==(right:Transform3D) |

bool
operator !=(right:Transform3D)
AABB
operator *(right:AABB)
PackedVector3Array
operator*(right:PackedVector3Array)
Plane
operator *(right:Plane)
Transform3D
operator*(right:Transform3D)
Vector3
operator *(right:Vector3)
Transform3D
operator*(right:float)
Transform3D
operator *(right:int)
Transform3D
operator /(right:float)
Transform3D
operator /(right:int)
bool
operator ==(right:Transform3D)

## Constants

IDENTITY=Transform3D(1,0,0,0,1,0,0,0,1,0,0,0)🔗
The identityTransform3D. This is a transform with no translation, no rotation, and a scale ofVector3.ONE. Itsbasisis equal toBasis.IDENTITY. This also means that:

- ItsBasis.xpoints right (Vector3.RIGHT);
ItsBasis.xpoints right (Vector3.RIGHT);
- ItsBasis.ypoints up (Vector3.UP);
ItsBasis.ypoints up (Vector3.UP);
- ItsBasis.zpoints back (Vector3.BACK).
ItsBasis.zpoints back (Vector3.BACK).

```
var transform = Transform3D.IDENTITY
var basis = transform.basis
print("| X | Y | Z | Origin")
print("| %.f | %.f | %.f | %.f" % [basis.x.x, basis.y.x, basis.z.x, transform.origin.x])
print("| %.f | %.f | %.f | %.f" % [basis.x.y, basis.y.y, basis.z.y, transform.origin.y])
print("| %.f | %.f | %.f | %.f" % [basis.x.z, basis.y.z, basis.z.z, transform.origin.z])
# Prints:
# | X | Y | Z | Origin
# | 1 | 0 | 0 | 0
# | 0 | 1 | 0 | 0
# | 0 | 0 | 1 | 0
```

If aVector3, anAABB, aPlane, aPackedVector3Array, or anotherTransform3Dis transformed (multiplied) by this constant, no transformation occurs.
Note:In GDScript, this constant is equivalent to creating aTransform3Dwithout any arguments. It can be used to make your code clearer, and for consistency with C#.
FLIP_X=Transform3D(-1,0,0,0,1,0,0,0,1,0,0,0)🔗
Transform3Dwith mirroring applied perpendicular to the YZ plane. Itsbasisis equal toBasis.FLIP_X.
FLIP_Y=Transform3D(1,0,0,0,-1,0,0,0,1,0,0,0)🔗
Transform3Dwith mirroring applied perpendicular to the XZ plane. Itsbasisis equal toBasis.FLIP_Y.
FLIP_Z=Transform3D(1,0,0,0,1,0,0,0,-1,0,0,0)🔗
Transform3Dwith mirroring applied perpendicular to the XY plane. Itsbasisis equal toBasis.FLIP_Z.

## Property Descriptions

Basisbasis=Basis(1,0,0,0,1,0,0,0,1)🔗
TheBasisof this transform. It is composed by 3 axes (Basis.x,Basis.y, andBasis.z). Together, these represent the transform's rotation, scale, and shear.
Vector3origin=Vector3(0,0,0)🔗
The translation offset of this transform. In 3D space, this can be seen as the position.

## Constructor Descriptions

Transform3DTransform3D()🔗
Constructs aTransform3Didentical toIDENTITY.
Note:In C#, this constructs aTransform3Dwith itsoriginand the components of itsbasisset toVector3.ZERO.
Transform3DTransform3D(from:Transform3D)
Constructs aTransform3Das a copy of the givenTransform3D.
Transform3DTransform3D(basis:Basis, origin:Vector3)
Constructs aTransform3Dfrom aBasisandVector3.
Transform3DTransform3D(from:Projection)
Constructs aTransform3Dfrom aProjection. BecauseTransform3Dis a 3×4 matrix andProjectionis a 4×4 matrix, this operation trims the last row of the projection matrix (from.x.w,from.y.w,from.z.w, andfrom.w.ware not included in the new transform).
Transform3DTransform3D(x_axis:Vector3, y_axis:Vector3, z_axis:Vector3, origin:Vector3)
Constructs aTransform3Dfrom fourVector3values (also called matrix columns).
The first three arguments are thebasis's axes (Basis.x,Basis.y, andBasis.z).

## Method Descriptions

Transform3Daffine_inverse()const🔗
Returns the inverted version of this transform. Unlikeinverse(), this method works with almost anybasis, including non-uniform ones, but is slower. See alsoBasis.inverse().
Note:For this method to return correctly, the transform'sbasisneeds to have a determinant that is not exactly0.0(seeBasis.determinant()).
Transform3Dinterpolate_with(xform:Transform3D, weight:float)const🔗
Returns the result of the linear interpolation between this transform andxformby the givenweight.
Theweightshould be between0.0and1.0(inclusive). Values outside this range are allowed and can be used to performextrapolationinstead.
Transform3Dinverse()const🔗
Returns theinverted version of this transform. See alsoBasis.inverse().
Note:For this method to return correctly, the transform'sbasisneeds to beorthonormal(seeorthonormalized()). That means the basis should only represent a rotation. If it does not, useaffine_inverse()instead.
boolis_equal_approx(xform:Transform3D)const🔗
Returnstrueif this transform andxformare approximately equal, by running@GlobalScope.is_equal_approx()on each component.
boolis_finite()const🔗
Returnstrueif this transform is finite, by calling@GlobalScope.is_finite()on each component.
Transform3Dlooking_at(target:Vector3, up:Vector3= Vector3(0, 1, 0), use_model_front:bool= false)const🔗
Returns a copy of this transform rotated so that the forward axis (-Z) points towards thetargetposition.
The up axis (+Y) points as close to theupvector as possible while staying perpendicular to the forward axis. The resulting transform is orthonormalized. The existing rotation, scale, and skew information from the original transform is discarded. Thetargetandupvectors cannot be zero, cannot be parallel to each other, and are defined in global/parent space.
Ifuse_model_frontistrue, the +Z axis (asset front) is treated as forward (implies +X is left) and points toward thetargetposition. By default, the -Z axis (camera forward) is treated as forward (implies +X is right).
Transform3Dorthonormalized()const🔗
Returns a copy of this transform with itsbasisorthonormalized. An orthonormal basis is bothorthogonal(the axes are perpendicular to each other) andnormalized(the axes have a length of1.0), which also means it can only represent a rotation. See alsoBasis.orthonormalized().
Transform3Drotated(axis:Vector3, angle:float)const🔗
Returns a copy of this transform rotated around the givenaxisby the givenangle(in radians).
Theaxismust be a normalized vector (seeVector3.normalized()). Ifangleis positive, the basis is rotated counter-clockwise around the axis.
This method is an optimized version of multiplying the given transformXwith a corresponding rotation transformRfrom the left, i.e.,R*X.
This can be seen as transforming with respect to the global/parent frame.
Transform3Drotated_local(axis:Vector3, angle:float)const🔗
Returns a copy of this transform rotated around the givenaxisby the givenangle(in radians).
Theaxismust be a normalized vector in the transform's local coordinate system. For example, to rotate around the local X-axis, useVector3.RIGHT.
This method is an optimized version of multiplying the given transformXwith a corresponding rotation transformRfrom the right, i.e.,X*R.
This can be seen as transforming with respect to the local frame.
Transform3Dscaled(scale:Vector3)const🔗
Returns a copy of this transform scaled by the givenscalefactor.
This method is an optimized version of multiplying the given transformXwith a corresponding scaling transformSfrom the left, i.e.,S*X.
This can be seen as transforming with respect to the global/parent frame.
Transform3Dscaled_local(scale:Vector3)const🔗
Returns a copy of this transform scaled by the givenscalefactor.
This method is an optimized version of multiplying the given transformXwith a corresponding scaling transformSfrom the right, i.e.,X*S.
This can be seen as transforming with respect to the local frame.
Transform3Dtranslated(offset:Vector3)const🔗
Returns a copy of this transform translated by the givenoffset.
This method is an optimized version of multiplying the given transformXwith a corresponding translation transformTfrom the left, i.e.,T*X.
This can be seen as transforming with respect to the global/parent frame.
Transform3Dtranslated_local(offset:Vector3)const🔗
Returns a copy of this transform translated by the givenoffset.
This method is an optimized version of multiplying the given transformXwith a corresponding translation transformTfrom the right, i.e.,X*T.
This can be seen as transforming with respect to the local frame.

## Operator Descriptions

booloperator !=(right:Transform3D)🔗
Returnstrueif the components of both transforms are not equal.
Note:Due to floating-point precision errors, consider usingis_equal_approx()instead, which is more reliable.
AABBoperator *(right:AABB)🔗
Transforms (multiplies) theAABBby this transformation matrix.
PackedVector3Arrayoperator*(right:PackedVector3Array)🔗
Transforms (multiplies) everyVector3element of the givenPackedVector3Arrayby this transformation matrix.
On larger arrays, this operation is much faster than transforming eachVector3individually.
Planeoperator *(right:Plane)🔗
Transforms (multiplies) thePlaneby this transformation matrix.
Transform3Doperator*(right:Transform3D)🔗
Transforms (multiplies) this transform by therighttransform.
This is the operation performed between parent and childNode3Ds.
Note:If you need to only modify one attribute of this transform, consider using one of the following methods, instead:

- For translation, seetranslated()ortranslated_local().
For translation, seetranslated()ortranslated_local().
- For rotation, seerotated()orrotated_local().
For rotation, seerotated()orrotated_local().
- For scale, seescaled()orscaled_local().
For scale, seescaled()orscaled_local().
Vector3operator *(right:Vector3)🔗
Transforms (multiplies) theVector3by this transformation matrix.
Transform3Doperator*(right:float)🔗
Multiplies all components of theTransform3Dby the givenfloat, including theorigin. This affects the transform's scale uniformly, scaling thebasis.
Transform3Doperator *(right:int)🔗
Multiplies all components of theTransform3Dby the givenint, including theorigin. This affects the transform's scale uniformly, scaling thebasis.
Transform3Doperator /(right:float)🔗
Divides all components of theTransform3Dby the givenfloat, including theorigin. This affects the transform's scale uniformly, scaling thebasis.
Transform3Doperator /(right:int)🔗
Divides all components of theTransform3Dby the givenint, including theorigin. This affects the transform's scale uniformly, scaling thebasis.
booloperator ==(right:Transform3D)🔗
Returnstrueif the components of both transforms are exactly equal.
Note:Due to floating-point precision errors, consider usingis_equal_approx()instead, which is more reliable.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
