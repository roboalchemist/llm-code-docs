# Quaternion in English

# Quaternion

A unit quaternion used for representing 3D rotations.

## Description

TheQuaternionbuilt-inVarianttype is a 4D data structure that represents rotation in the form of aHamilton convention quaternion. Compared to theBasistype which can store both rotation and scale, quaternions canonlystore rotation.
AQuaternionis composed by 4 floating-point components:w,x,y, andz. These components are very compact in memory, and because of this some operations are more efficient and less likely to cause floating-point errors. Methods such asget_angle(),get_axis(), andslerp()are faster than theirBasiscounterparts.
For a great introduction to quaternions, seethis video by 3Blue1Brown. You do not need to know the math behind quaternions, as Godot provides several helper methods that handle it for you. These includeslerp()andspherical_cubic_interpolate(), as well as the*operator.
Note:Quaternions must be normalized before being used for rotation (seenormalized()).
Note:Similarly toVector2andVector3, the components of a quaternion use 32-bit precision by default, unlikefloatwhich is always 64-bit. If double precision is needed, compile the engine with the optionprecision=double.
Note
There are notable differences when using this API with C#. SeeC# API differences to GDScriptfor more information.

## Tutorials

- 3Blue1Brown's video on Quaternions
3Blue1Brown's video on Quaternions
- Online Quaternion Visualization
Online Quaternion Visualization
- Using 3D transforms
Using 3D transforms
- Third Person Shooter (TPS) Demo
Third Person Shooter (TPS) Demo
- Advanced Quaternion Visualization
Advanced Quaternion Visualization

## Properties

| float | w | 1.0 |
|---|---|---|
| float | x | 0.0 |
| float | y | 0.0 |
| float | z | 0.0 |

float
float
float
float

## Constructors

| Quaternion | Quaternion() |
|---|---|
| Quaternion | Quaternion(from:Quaternion) |
| Quaternion | Quaternion(arc_from:Vector3, arc_to:Vector3) |
| Quaternion | Quaternion(axis:Vector3, angle:float) |
| Quaternion | Quaternion(from:Basis) |
| Quaternion | Quaternion(x:float, y:float, z:float, w:float) |

Quaternion
Quaternion()
Quaternion
Quaternion(from:Quaternion)
Quaternion
Quaternion(arc_from:Vector3, arc_to:Vector3)
Quaternion
Quaternion(axis:Vector3, angle:float)
Quaternion
Quaternion(from:Basis)
Quaternion
Quaternion(x:float, y:float, z:float, w:float)

## Methods

| float | angle_to(to:Quaternion)const |
|---|---|
| float | dot(with:Quaternion)const |
| Quaternion | exp()const |
| Quaternion | from_euler(euler:Vector3)static |
| float | get_angle()const |
| Vector3 | get_axis()const |
| Vector3 | get_euler(order:int= 2)const |
| Quaternion | inverse()const |
| bool | is_equal_approx(to:Quaternion)const |
| bool | is_finite()const |
| bool | is_normalized()const |
| float | length()const |
| float | length_squared()const |
| Quaternion | log()const |
| Quaternion | normalized()const |
| Quaternion | slerp(to:Quaternion, weight:float)const |
| Quaternion | slerpni(to:Quaternion, weight:float)const |
| Quaternion | spherical_cubic_interpolate(b:Quaternion, pre_a:Quaternion, post_b:Quaternion, weight:float)const |
| Quaternion | spherical_cubic_interpolate_in_time(b:Quaternion, pre_a:Quaternion, post_b:Quaternion, weight:float, b_t:float, pre_a_t:float, post_b_t:float)const |

float
angle_to(to:Quaternion)const
float
dot(with:Quaternion)const
Quaternion
exp()const
Quaternion
from_euler(euler:Vector3)static
float
get_angle()const
Vector3
get_axis()const
Vector3
get_euler(order:int= 2)const
Quaternion
inverse()const
bool
is_equal_approx(to:Quaternion)const
bool
is_finite()const
bool
is_normalized()const
float
length()const
float
length_squared()const
Quaternion
log()const
Quaternion
normalized()const
Quaternion
slerp(to:Quaternion, weight:float)const
Quaternion
slerpni(to:Quaternion, weight:float)const
Quaternion
spherical_cubic_interpolate(b:Quaternion, pre_a:Quaternion, post_b:Quaternion, weight:float)const
Quaternion
spherical_cubic_interpolate_in_time(b:Quaternion, pre_a:Quaternion, post_b:Quaternion, weight:float, b_t:float, pre_a_t:float, post_b_t:float)const

## Operators

| bool | operator !=(right:Quaternion) |
|---|---|
| Quaternion | operator *(right:Quaternion) |
| Vector3 | operator *(right:Vector3) |
| Quaternion | operator *(right:float) |
| Quaternion | operator *(right:int) |
| Quaternion | operator +(right:Quaternion) |
| Quaternion | operator -(right:Quaternion) |
| Quaternion | operator /(right:float) |
| Quaternion | operator /(right:int) |
| bool | operator ==(right:Quaternion) |
| float | operator [](index:int) |
| Quaternion | operator unary+() |
| Quaternion | operator unary-() |

bool
operator !=(right:Quaternion)
Quaternion
operator *(right:Quaternion)
Vector3
operator*(right:Vector3)
Quaternion
operator *(right:float)
Quaternion
operator*(right:int)
Quaternion
operator +(right:Quaternion)
Quaternion
operator -(right:Quaternion)
Quaternion
operator /(right:float)
Quaternion
operator /(right:int)
bool
operator ==(right:Quaternion)
float
operator [](index:int)
Quaternion
operator unary+()
Quaternion
operator unary-()

## Constants

IDENTITY=Quaternion(0,0,0,1)🔗
The identity quaternion, representing no rotation. This has the same rotation asBasis.IDENTITY.
If aVector3is rotated (multiplied) by this quaternion, it does not change.
Note:In GDScript, this constant is equivalent to creating aQuaternionwithout any arguments. It can be used to make your code clearer, and for consistency with C#.

## Property Descriptions

floatw=1.0🔗
W component of the quaternion. This is the "real" part.
Note:Quaternion components should usually not be manipulated directly.
floatx=0.0🔗
X component of the quaternion. This is the value along the "imaginary"iaxis.
Note:Quaternion components should usually not be manipulated directly.
floaty=0.0🔗
Y component of the quaternion. This is the value along the "imaginary"jaxis.
Note:Quaternion components should usually not be manipulated directly.
floatz=0.0🔗
Z component of the quaternion. This is the value along the "imaginary"kaxis.
Note:Quaternion components should usually not be manipulated directly.

## Constructor Descriptions

QuaternionQuaternion()🔗
Constructs aQuaternionidentical toIDENTITY.
Note:In C#, this constructs aQuaternionwith all of its components set to0.0.
QuaternionQuaternion(from:Quaternion)
Constructs aQuaternionas a copy of the givenQuaternion.
QuaternionQuaternion(arc_from:Vector3, arc_to:Vector3)
Constructs aQuaternionrepresenting the shortest arc betweenarc_fromandarc_to. These can be imagined as two points intersecting a sphere's surface, with a radius of1.0.
QuaternionQuaternion(axis:Vector3, angle:float)
Constructs aQuaternionrepresenting rotation around theaxisby the givenangle, in radians. The axis must be a normalized vector.
QuaternionQuaternion(from:Basis)
Constructs aQuaternionfrom the given rotationBasis.
This constructor is faster thanBasis.get_rotation_quaternion(), but the given basis must beorthonormalized(seeBasis.orthonormalized()). Otherwise, the constructor fails and returnsIDENTITY.
QuaternionQuaternion(x:float, y:float, z:float, w:float)
Constructs aQuaterniondefined by the given values.
Note:Only normalized quaternions represent rotation; if these values are not normalized, the newQuaternionwill not be a valid rotation.

## Method Descriptions

floatangle_to(to:Quaternion)const🔗
Returns the angle between this quaternion andto. This is the magnitude of the angle you would need to rotate by to get from one to the other.
Note:The magnitude of the floating-point error for this method is abnormally high, so methods such asis_zero_approxwill not work reliably.
floatdot(with:Quaternion)const🔗
Returns the dot product between this quaternion andwith.
This is equivalent to(quat.x*with.x)+(quat.y*with.y)+(quat.z*with.z)+(quat.w*with.w).
Quaternionexp()const🔗
Returns the exponential of this quaternion. The rotation axis of the result is the normalized rotation axis of this quaternion, the angle of the result is the length of the vector part of this quaternion.
Quaternionfrom_euler(euler:Vector3)static🔗
Constructs a newQuaternionfrom the givenVector3ofEuler angles, in radians. This method always uses the YXZ convention (@GlobalScope.EULER_ORDER_YXZ).
floatget_angle()const🔗
Returns the angle of the rotation represented by this quaternion.
Note:The quaternion must be normalized.
Vector3get_axis()const🔗
Returns the rotation axis of the rotation represented by this quaternion.
Vector3get_euler(order:int= 2)const🔗
Returns this quaternion's rotation as aVector3ofEuler angles, in radians.
The order of each consecutive rotation can be changed withorder(seeEulerOrderconstants). By default, the YXZ convention is used (@GlobalScope.EULER_ORDER_YXZ): Z (roll) is calculated first, then X (pitch), and lastly Y (yaw). When using the opposite methodfrom_euler(), this order is reversed.
Quaternioninverse()const🔗
Returns the inverse version of this quaternion, inverting the sign of every component exceptw.
boolis_equal_approx(to:Quaternion)const🔗
Returnstrueif this quaternion andtoare approximately equal, by calling@GlobalScope.is_equal_approx()on each component.
boolis_finite()const🔗
Returnstrueif this quaternion is finite, by calling@GlobalScope.is_finite()on each component.
boolis_normalized()const🔗
Returnstrueif this quaternion is normalized. See alsonormalized().
floatlength()const🔗
Returns this quaternion's length, also called magnitude.
floatlength_squared()const🔗
Returns this quaternion's length, squared.
Note:This method is faster thanlength(), so prefer it if you only need to compare quaternion lengths.
Quaternionlog()const🔗
Returns the logarithm of this quaternion. Multiplies this quaternion's rotation axis by its rotation angle, and stores the result in the returned quaternion's vector part (x,y, andz). The returned quaternion's real part (w) is always0.0.
Quaternionnormalized()const🔗
Returns a copy of this quaternion, normalized so that its length is1.0. See alsois_normalized().
Quaternionslerp(to:Quaternion, weight:float)const🔗
Performs a spherical-linear interpolation with thetoquaternion, given aweightand returns the result. Both this quaternion andtomust be normalized.
Quaternionslerpni(to:Quaternion, weight:float)const🔗
Performs a spherical-linear interpolation with thetoquaternion, given aweightand returns the result. Unlikeslerp(), this method does not check if the rotation path is smaller than 90 degrees. Both this quaternion andtomust be normalized.
Quaternionspherical_cubic_interpolate(b:Quaternion, pre_a:Quaternion, post_b:Quaternion, weight:float)const🔗
Performs a spherical cubic interpolation between quaternionspre_a, this vector,b, andpost_b, by the given amountweight.
Quaternionspherical_cubic_interpolate_in_time(b:Quaternion, pre_a:Quaternion, post_b:Quaternion, weight:float, b_t:float, pre_a_t:float, post_b_t:float)const🔗
Performs a spherical cubic interpolation between quaternionspre_a, this vector,b, andpost_b, by the given amountweight.
It can perform smoother interpolation thanspherical_cubic_interpolate()by the time values.

## Operator Descriptions

booloperator !=(right:Quaternion)🔗
Returnstrueif the components of both quaternions are not exactly equal.
Note:Due to floating-point precision errors, consider usingis_equal_approx()instead, which is more reliable.
Quaternionoperator *(right:Quaternion)🔗
Composes (multiplies) two quaternions. This rotates therightquaternion (the child) by this quaternion (the parent).
Vector3operator*(right:Vector3)🔗
Rotates (multiplies) therightvector by this quaternion, returning aVector3.
Quaternionoperator *(right:float)🔗
Multiplies each component of theQuaternionby the rightfloatvalue.
This operation is not meaningful on its own, but it can be used as a part of a larger expression.
Quaternionoperator*(right:int)🔗
Multiplies each component of theQuaternionby the rightintvalue.
This operation is not meaningful on its own, but it can be used as a part of a larger expression.
Quaternionoperator +(right:Quaternion)🔗
Adds each component of the leftQuaternionto the rightQuaternion.
This operation is not meaningful on its own, but it can be used as a part of a larger expression, such as approximating an intermediate rotation between two nearby rotations.
Quaternionoperator -(right:Quaternion)🔗
Subtracts each component of the leftQuaternionby the rightQuaternion.
This operation is not meaningful on its own, but it can be used as a part of a larger expression.
Quaternionoperator /(right:float)🔗
Divides each component of theQuaternionby the rightfloatvalue.
This operation is not meaningful on its own, but it can be used as a part of a larger expression.
Quaternionoperator /(right:int)🔗
Divides each component of theQuaternionby the rightintvalue.
This operation is not meaningful on its own, but it can be used as a part of a larger expression.
booloperator ==(right:Quaternion)🔗
Returnstrueif the components of both quaternions are exactly equal.
Note:Due to floating-point precision errors, consider usingis_equal_approx()instead, which is more reliable.
floatoperator [](index:int)🔗
Accesses each component of this quaternion by their index.
Index0is the same asx, index1is the same asy, index2is the same asz, and index3is the same asw.
Quaternionoperator unary+()🔗
Returns the same value as if the+was not there. Unary+does nothing, but sometimes it can make your code more readable.
Quaternionoperator unary-()🔗
Returns the negative value of theQuaternion. This is the same as multiplying all components by-1. This operation results in a quaternion that represents the same rotation.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
