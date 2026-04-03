# Basis in English

# Basis
A 3×3 matrix for representing 3D rotation and scale.

## Description
TheBasisbuilt-inVarianttype is a 3×3matrixused to represent 3D rotation, scale, and shear. It is frequently used within aTransform3D.
ABasisis composed by 3 axis vectors, each representing a column of the matrix:x,y, andz. The length of each axis (Vector3.length()) influences the basis's scale, while the direction of all axes influence the rotation. Usually, these axes are perpendicular to one another. However, when you rotate any axis individually, the basis becomes sheared. Applying a sheared basis to a 3D model will make the model appear distorted.
ABasisis:
- Orthogonalif its axes are perpendicular to each other.
Orthogonalif its axes are perpendicular to each other.
- Normalizedif the length of every axis is1.0.
Normalizedif the length of every axis is1.0.
- Uniformif all axes share the same length (seeget_scale()).
Uniformif all axes share the same length (seeget_scale()).
- Orthonormalif it is both orthogonal and normalized, which allows it to only represent rotations (seeorthonormalized()).
Orthonormalif it is both orthogonal and normalized, which allows it to only represent rotations (seeorthonormalized()).
- Conformalif it is both orthogonal and uniform, which ensures it is not distorted.
Conformalif it is both orthogonal and uniform, which ensures it is not distorted.
For a general introduction, see theMatrices and transformstutorial.
Note:Godot uses aright-handed coordinate system, which is a common standard. For directions, the convention for built-in types likeCamera3Dis for -Z to point forward (+X is right, +Y is up, and +Z is back). Other objects may use different direction conventions. For more information, see the3D asset direction conventionstutorial.
Note:The basis matrices are exposed ascolumn-majororder, which is the same as OpenGL. However, they are stored internally in row-major order, which is the same as DirectX.
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
- 3D Voxel Demo
3D Voxel Demo
- 2.5D Game Demo
2.5D Game Demo

## Properties

| Vector3 | x | Vector3(1,0,0) |
|---|---|---|
| Vector3 | y | Vector3(0,1,0) |
| Vector3 | z | Vector3(0,0,1) |

Vector3
Vector3(1,0,0)
Vector3
Vector3(0,1,0)
Vector3
Vector3(0,0,1)

## Constructors

| Basis | Basis() |
|---|---|
| Basis | Basis(from:Basis) |
| Basis | Basis(axis:Vector3, angle:float) |
| Basis | Basis(from:Quaternion) |
| Basis | Basis(x_axis:Vector3, y_axis:Vector3, z_axis:Vector3) |

Basis
Basis()
Basis
Basis(from:Basis)
Basis
Basis(axis:Vector3, angle:float)
Basis
Basis(from:Quaternion)
Basis
Basis(x_axis:Vector3, y_axis:Vector3, z_axis:Vector3)

## Methods

| float | determinant()const |
|---|---|
| Basis | from_euler(euler:Vector3, order:int= 2)static |
| Basis | from_scale(scale:Vector3)static |
| Vector3 | get_euler(order:int= 2)const |
| Quaternion | get_rotation_quaternion()const |
| Vector3 | get_scale()const |
| Basis | inverse()const |
| bool | is_conformal()const |
| bool | is_equal_approx(b:Basis)const |
| bool | is_finite()const |
| Basis | looking_at(target:Vector3, up:Vector3= Vector3(0, 1, 0), use_model_front:bool= false)static |
| Basis | orthonormalized()const |
| Basis | rotated(axis:Vector3, angle:float)const |
| Basis | scaled(scale:Vector3)const |
| Basis | scaled_local(scale:Vector3)const |
| Basis | slerp(to:Basis, weight:float)const |
| float | tdotx(with:Vector3)const |
| float | tdoty(with:Vector3)const |
| float | tdotz(with:Vector3)const |
| Basis | transposed()const |

float
determinant()const
Basis
from_euler(euler:Vector3, order:int= 2)static
Basis
from_scale(scale:Vector3)static
Vector3
get_euler(order:int= 2)const
Quaternion
get_rotation_quaternion()const
Vector3
get_scale()const
Basis
inverse()const
bool
is_conformal()const
bool
is_equal_approx(b:Basis)const
bool
is_finite()const
Basis
looking_at(target:Vector3, up:Vector3= Vector3(0, 1, 0), use_model_front:bool= false)static
Basis
orthonormalized()const
Basis
rotated(axis:Vector3, angle:float)const
Basis
scaled(scale:Vector3)const
Basis
scaled_local(scale:Vector3)const
Basis
slerp(to:Basis, weight:float)const
float
tdotx(with:Vector3)const
float
tdoty(with:Vector3)const
float
tdotz(with:Vector3)const
Basis
transposed()const

## Operators

| bool | operator !=(right:Basis) |
|---|---|
| Basis | operator *(right:Basis) |
| Vector3 | operator *(right:Vector3) |
| Basis | operator *(right:float) |
| Basis | operator *(right:int) |
| Basis | operator /(right:float) |
| Basis | operator /(right:int) |
| bool | operator ==(right:Basis) |
| Vector3 | operator [](index:int) |

bool
operator !=(right:Basis)
Basis
operator *(right:Basis)
Vector3
operator *(right:Vector3)
Basis
operator *(right:float)
Basis
operator *(right:int)
Basis
operator /(right:float)
Basis
operator /(right:int)
bool
operator ==(right:Basis)
Vector3
operator [](index:int)

## Constants
IDENTITY=Basis(1,0,0,0,1,0,0,0,1)🔗
The identityBasis. This is an orthonormal basis with no rotation, no shear, and a scale ofVector3.ONE. This also means that:
- Thexpoints right (Vector3.RIGHT);
Thexpoints right (Vector3.RIGHT);
- Theypoints up (Vector3.UP);
Theypoints up (Vector3.UP);
- Thezpoints back (Vector3.BACK).
Thezpoints back (Vector3.BACK).
```
var basis = Basis.IDENTITY
print("| X | Y | Z")
print("| %.f | %.f | %.f" % [basis.x.x, basis.y.x, basis.z.x])
print("| %.f | %.f | %.f" % [basis.x.y, basis.y.y, basis.z.y])
print("| %.f | %.f | %.f" % [basis.x.z, basis.y.z, basis.z.z])
# Prints:
# | X | Y | Z
# | 1 | 0 | 0
# | 0 | 1 | 0
# | 0 | 0 | 1
```
If aVector3or anotherBasisis transformed (multiplied) by this constant, no transformation occurs.
Note:In GDScript, this constant is equivalent to creating aBasiswithout any arguments. It can be used to make your code clearer, and for consistency with C#.
FLIP_X=Basis(-1,0,0,0,1,0,0,0,1)🔗
When any basis is multiplied byFLIP_X, it negates all components of thexaxis (the X column).
WhenFLIP_Xis multiplied by any basis, it negates theVector3.xcomponent of all axes (the X row).
FLIP_Y=Basis(1,0,0,0,-1,0,0,0,1)🔗
When any basis is multiplied byFLIP_Y, it negates all components of theyaxis (the Y column).
WhenFLIP_Yis multiplied by any basis, it negates theVector3.ycomponent of all axes (the Y row).
FLIP_Z=Basis(1,0,0,0,1,0,0,0,-1)🔗
When any basis is multiplied byFLIP_Z, it negates all components of thezaxis (the Z column).
WhenFLIP_Zis multiplied by any basis, it negates theVector3.zcomponent of all axes (the Z row).

## Property Descriptions
Vector3x=Vector3(1,0,0)🔗
The basis's X axis, and the column0of the matrix.
On the identity basis, this vector points right (Vector3.RIGHT).
Vector3y=Vector3(0,1,0)🔗
The basis's Y axis, and the column1of the matrix.
On the identity basis, this vector points up (Vector3.UP).
Vector3z=Vector3(0,0,1)🔗
The basis's Z axis, and the column2of the matrix.
On the identity basis, this vector points back (Vector3.BACK).

## Constructor Descriptions
BasisBasis()🔗
Constructs aBasisidentical toIDENTITY.
Note:In C#, this constructs aBasiswith all of its components set toVector3.ZERO.
BasisBasis(from:Basis)
Constructs aBasisas a copy of the givenBasis.
BasisBasis(axis:Vector3, angle:float)
Constructs aBasisthat only represents rotation, rotated around theaxisby the givenangle, in radians. The axis must be a normalized vector.
Note:This is the same as usingrotated()on theIDENTITYbasis. With more than one angle consider usingfrom_euler(), instead.
BasisBasis(from:Quaternion)
Constructs aBasisthat only represents rotation from the givenQuaternion.
Note:Quaternionsonlystore rotation, not scale. Because of this, conversions fromBasistoQuaternioncannot always be reversed.
BasisBasis(x_axis:Vector3, y_axis:Vector3, z_axis:Vector3)
Constructs aBasisfrom 3 axis vectors. These are the columns of the basis matrix.

## Method Descriptions
floatdeterminant()const🔗
Returns thedeterminantof this basis's matrix. For advanced math, this number can be used to determine a few attributes:
- If the determinant is exactly0.0, the basis is not invertible (seeinverse()).
If the determinant is exactly0.0, the basis is not invertible (seeinverse()).
- If the determinant is a negative number, the basis represents a negative scale.
If the determinant is a negative number, the basis represents a negative scale.
Note:If the basis's scale is the same for every axis, its determinant is always that scale by the power of 3.
Basisfrom_euler(euler:Vector3, order:int= 2)static🔗
Constructs a newBasisthat only represents rotation from the givenVector3ofEuler angles, in radians.
- TheVector3.xshould contain the angle around thexaxis (pitch);
TheVector3.xshould contain the angle around thexaxis (pitch);
- TheVector3.yshould contain the angle around theyaxis (yaw);
TheVector3.yshould contain the angle around theyaxis (yaw);
- TheVector3.zshould contain the angle around thezaxis (roll).
TheVector3.zshould contain the angle around thezaxis (roll).
```
# Creates a Basis whose z axis points down.
var my_basis = Basis.from_euler(Vector3(TAU / 4, 0, 0))

print(my_basis.z) # Prints (0.0, -1.0, 0.0)
```
```
// Creates a Basis whose z axis points down.
var myBasis = Basis.FromEuler(new Vector3(Mathf.Tau / 4.0f, 0.0f, 0.0f));

GD.Print(myBasis.Z); // Prints (0, -1, 0)
```
The order of each consecutive rotation can be changed withorder(seeEulerOrderconstants). By default, the YXZ convention is used (@GlobalScope.EULER_ORDER_YXZ): the basis rotates first around the Y axis (yaw), then X (pitch), and lastly Z (roll). When using the opposite methodget_euler(), this order is reversed.
Basisfrom_scale(scale:Vector3)static🔗
Constructs a newBasisthat only represents scale, with no rotation or shear, from the givenscalevector.
```
var my_basis = Basis.from_scale(Vector3(2, 4, 8))

print(my_basis.x) # Prints (2.0, 0.0, 0.0)
print(my_basis.y) # Prints (0.0, 4.0, 0.0)
print(my_basis.z) # Prints (0.0, 0.0, 8.0)
```
```
var myBasis = Basis.FromScale(new Vector3(2.0f, 4.0f, 8.0f));

GD.Print(myBasis.X); // Prints (2, 0, 0)
GD.Print(myBasis.Y); // Prints (0, 4, 0)
GD.Print(myBasis.Z); // Prints (0, 0, 8)
```
Note:In linear algebra, the matrix of this basis is also known as adiagonal matrix.
Vector3get_euler(order:int= 2)const🔗
Returns this basis's rotation as aVector3ofEuler angles, in radians. For the returned value:
- TheVector3.xcontains the angle around thexaxis (pitch);
TheVector3.xcontains the angle around thexaxis (pitch);
- TheVector3.ycontains the angle around theyaxis (yaw);
TheVector3.ycontains the angle around theyaxis (yaw);
- TheVector3.zcontains the angle around thezaxis (roll).
TheVector3.zcontains the angle around thezaxis (roll).
The order of each consecutive rotation can be changed withorder(seeEulerOrderconstants). By default, the YXZ convention is used (@GlobalScope.EULER_ORDER_YXZ): Z (roll) is calculated first, then X (pitch), and lastly Y (yaw). When using the opposite methodfrom_euler(), this order is reversed.
Note:For this method to return correctly, the basis needs to beorthonormal(seeorthonormalized()).
Note:Euler angles are much more intuitive but are not suitable for 3D math. Because of this, consider using theget_rotation_quaternion()method instead, which returns aQuaternion.
Note:In the Inspector dock, a basis's rotation is often displayed in Euler angles (in degrees), as is the case with theNode3D.rotationproperty.
Quaternionget_rotation_quaternion()const🔗
Returns this basis's rotation as aQuaternion.
Note:Quaternions are much more suitable for 3D math but are less intuitive. For user interfaces, consider using theget_euler()method, which returns Euler angles.
Vector3get_scale()const🔗
Returns the length of each axis of this basis, as aVector3. If the basis is not sheared, this value is the scaling factor. It is not affected by rotation.
```
var my_basis = Basis(
    Vector3(2, 0, 0),
    Vector3(0, 4, 0),
    Vector3(0, 0, 8)
)
# Rotating the Basis in any way preserves its scale.
my_basis = my_basis.rotated(Vector3.UP, TAU / 2)
my_basis = my_basis.rotated(Vector3.RIGHT, TAU / 4)

print(my_basis.get_scale()) # Prints (2.0, 4.0, 8.0)
```
```
var myBasis = new Basis(
    Vector3(2.0f, 0.0f, 0.0f),
    Vector3(0.0f, 4.0f, 0.0f),
    Vector3(0.0f, 0.0f, 8.0f)
);
// Rotating the Basis in any way preserves its scale.
myBasis = myBasis.Rotated(Vector3.Up, Mathf.Tau / 2.0f);
myBasis = myBasis.Rotated(Vector3.Right, Mathf.Tau / 4.0f);

GD.Print(myBasis.Scale); // Prints (2, 4, 8)
```
Note:If the value returned bydeterminant()is negative, the scale is also negative.
Basisinverse()const🔗
Returns theinverse of this basis's matrix.
boolis_conformal()const🔗
Returnstrueif this basis is conformal. A conformal basis is bothorthogonal(the axes are perpendicular to each other) anduniform(the axes share the same length). This method can be especially useful during physics calculations.
boolis_equal_approx(b:Basis)const🔗
Returnstrueif this basis andbare approximately equal, by calling@GlobalScope.is_equal_approx()on all vector components.
boolis_finite()const🔗
Returnstrueif this basis is finite, by calling@GlobalScope.is_finite()on all vector components.
Basislooking_at(target:Vector3, up:Vector3= Vector3(0, 1, 0), use_model_front:bool= false)static🔗
Creates a newBasiswith a rotation such that the forward axis (-Z) points towards thetargetposition.
By default, the -Z axis (camera forward) is treated as forward (implies +X is right). Ifuse_model_frontistrue, the +Z axis (asset front) is treated as forward (implies +X is left) and points toward thetargetposition.
The up axis (+Y) points as close to theupvector as possible while staying perpendicular to the forward axis. The returned basis is orthonormalized (seeorthonormalized()).
Thetargetand theupcannot beVector3.ZERO, and shouldn't be colinear to avoid unintended rotation around local Z axis.
Basisorthonormalized()const🔗
Returns the orthonormalized version of this basis. An orthonormal basis is bothorthogonal(the axes are perpendicular to each other) andnormalized(the axes have a length of1.0), which also means it can only represent a rotation.
It is often useful to call this method to avoid rounding errors on a rotating basis:
```
# Rotate this Node3D every frame.
func _process(delta):
    basis = basis.rotated(Vector3.UP, TAU * delta)
    basis = basis.rotated(Vector3.RIGHT, TAU * delta)
    basis = basis.orthonormalized()
```
```
// Rotate this Node3D every frame.
public override void _Process(double delta)
{
    Basis = Basis.Rotated(Vector3.Up, Mathf.Tau * (float)delta)
            .Rotated(Vector3.Right, Mathf.Tau * (float)delta)
            .Orthonormalized();
}
```
Basisrotated(axis:Vector3, angle:float)const🔗
Returns a copy of this basis rotated around the givenaxisby the givenangle(in radians).
Theaxismust be a normalized vector (seeVector3.normalized()). Ifangleis positive, the basis is rotated counter-clockwise around the axis.
```
var my_basis = Basis.IDENTITY
var angle = TAU / 2

my_basis = my_basis.rotated(Vector3.UP, angle)    # Rotate around the up axis (yaw).
my_basis = my_basis.rotated(Vector3.RIGHT, angle) # Rotate around the right axis (pitch).
my_basis = my_basis.rotated(Vector3.BACK, angle)  # Rotate around the back axis (roll).
```
```
var myBasis = Basis.Identity;
var angle = Mathf.Tau / 2.0f;

myBasis = myBasis.Rotated(Vector3.Up, angle);    // Rotate around the up axis (yaw).
myBasis = myBasis.Rotated(Vector3.Right, angle); // Rotate around the right axis (pitch).
myBasis = myBasis.Rotated(Vector3.Back, angle);  // Rotate around the back axis (roll).
```
Basisscaled(scale:Vector3)const🔗
Returns this basis with each axis's components scaled by the givenscale's components.
The basis matrix's rows are multiplied byscale's components. This operation is a global scale (relative to the parent).
```
var my_basis = Basis(
    Vector3(1, 1, 1),
    Vector3(2, 2, 2),
    Vector3(3, 3, 3)
)
my_basis = my_basis.scaled(Vector3(0, 2, -2))

print(my_basis.x) # Prints (0.0, 2.0, -2.0)
print(my_basis.y) # Prints (0.0, 4.0, -4.0)
print(my_basis.z) # Prints (0.0, 6.0, -6.0)
```
```
var myBasis = new Basis(
    new Vector3(1.0f, 1.0f, 1.0f),
    new Vector3(2.0f, 2.0f, 2.0f),
    new Vector3(3.0f, 3.0f, 3.0f)
);
myBasis = myBasis.Scaled(new Vector3(0.0f, 2.0f, -2.0f));

GD.Print(myBasis.X); // Prints (0, 2, -2)
GD.Print(myBasis.Y); // Prints (0, 4, -4)
GD.Print(myBasis.Z); // Prints (0, 6, -6)
```
Basisscaled_local(scale:Vector3)const🔗
Returns this basis with each axis scaled by the corresponding component in the givenscale.
The basis matrix's columns are multiplied byscale's components. This operation is a local scale (relative to self).
```
var my_basis = Basis(
    Vector3(1, 1, 1),
    Vector3(2, 2, 2),
    Vector3(3, 3, 3)
)
my_basis = my_basis.scaled_local(Vector3(0, 2, -2))

print(my_basis.x) # Prints (0.0, 0.0, 0.0)
print(my_basis.y) # Prints (4.0, 4.0, 4.0)
print(my_basis.z) # Prints (-6.0, -6.0, -6.0)
```
```
var myBasis = new Basis(
    new Vector3(1.0f, 1.0f, 1.0f),
    new Vector3(2.0f, 2.0f, 2.0f),
    new Vector3(3.0f, 3.0f, 3.0f)
);
myBasis = myBasis.ScaledLocal(new Vector3(0.0f, 2.0f, -2.0f));

GD.Print(myBasis.X); // Prints (0, 0, 0)
GD.Print(myBasis.Y); // Prints (4, 4, 4)
GD.Print(myBasis.Z); // Prints (-6, -6, -6)
```
Basisslerp(to:Basis, weight:float)const🔗
Performs a spherical-linear interpolation with thetobasis, given aweight. Both this basis andtoshould represent a rotation.
Example:Smoothly rotate aNode3Dto the target basis over time, with aTween:
```
var start_basis = Basis.IDENTITY
var target_basis = Basis.IDENTITY.rotated(Vector3.UP, TAU / 2)

func _ready():
    create_tween().tween_method(interpolate, 0.0, 1.0, 5.0).set_trans(Tween.TRANS_EXPO)

func interpolate(weight):
    basis = start_basis.slerp(target_basis, weight)
```
floattdotx(with:Vector3)const🔗
Returns the transposed dot product betweenwithand thexaxis (seetransposed()).
This is equivalent tobasis.x.dot(vector).
floattdoty(with:Vector3)const🔗
Returns the transposed dot product betweenwithand theyaxis (seetransposed()).
This is equivalent tobasis.y.dot(vector).
floattdotz(with:Vector3)const🔗
Returns the transposed dot product betweenwithand thezaxis (seetransposed()).
This is equivalent tobasis.z.dot(vector).
Basistransposed()const🔗
Returns the transposed version of this basis. This turns the basis matrix's columns into rows, and its rows into columns.
```
var my_basis = Basis(
    Vector3(1, 2, 3),
    Vector3(4, 5, 6),
    Vector3(7, 8, 9)
)
my_basis = my_basis.transposed()

print(my_basis.x) # Prints (1.0, 4.0, 7.0)
print(my_basis.y) # Prints (2.0, 5.0, 8.0)
print(my_basis.z) # Prints (3.0, 6.0, 9.0)
```
```
var myBasis = new Basis(
    new Vector3(1.0f, 2.0f, 3.0f),
    new Vector3(4.0f, 5.0f, 6.0f),
    new Vector3(7.0f, 8.0f, 9.0f)
);
myBasis = myBasis.Transposed();

GD.Print(myBasis.X); // Prints (1, 4, 7)
GD.Print(myBasis.Y); // Prints (2, 5, 8)
GD.Print(myBasis.Z); // Prints (3, 6, 9)
```

## Operator Descriptions
booloperator !=(right:Basis)🔗
Returnstrueif the components of bothBasismatrices are not equal.
Note:Due to floating-point precision errors, consider usingis_equal_approx()instead, which is more reliable.
Basisoperator *(right:Basis)🔗
Transforms (multiplies) therightbasis by this basis.
This is the operation performed between parent and childNode3Ds.
Vector3operator *(right:Vector3)🔗
Transforms (multiplies) therightvector by this basis, returning aVector3.
```
# Basis that swaps the X/Z axes and doubles the scale.
var my_basis = Basis(Vector3(0, 2, 0), Vector3(2, 0, 0), Vector3(0, 0, 2))
print(my_basis * Vector3(1, 2, 3)) # Prints (4.0, 2.0, 6.0)
```
```
// Basis that swaps the X/Z axes and doubles the scale.
var myBasis = new Basis(new Vector3(0, 2, 0), new Vector3(2, 0, 0), new Vector3(0, 0, 2));
GD.Print(myBasis * new Vector3(1, 2, 3)); // Prints (4, 2, 6)
```
Basisoperator *(right:float)🔗
Multiplies all components of theBasisby the givenfloat. This affects the basis's scale uniformly, resizing all 3 axes by therightvalue.
Basisoperator *(right:int)🔗
Multiplies all components of theBasisby the givenint. This affects the basis's scale uniformly, resizing all 3 axes by therightvalue.
Basisoperator /(right:float)🔗
Divides all components of theBasisby the givenfloat. This affects the basis's scale uniformly, resizing all 3 axes by therightvalue.
Basisoperator /(right:int)🔗
Divides all components of theBasisby the givenint. This affects the basis's scale uniformly, resizing all 3 axes by therightvalue.
booloperator ==(right:Basis)🔗
Returnstrueif the components of bothBasismatrices are exactly equal.
Note:Due to floating-point precision errors, consider usingis_equal_approx()instead, which is more reliable.
Vector3operator [](index:int)🔗
Accesses each axis (column) of this basis by their index. Index0is the same asx, index1is the same asy, and index2is the same asz.
Note:In C++, this operator accesses the rows of the basis matrix,notthe columns. For the same behavior as scripting languages, use theset_columnandget_columnmethods.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.