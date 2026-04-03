# Vector3

# Vector3
A 3D vector using floating-point coordinates.

## Description
A 3-element structure that can be used to represent 3D coordinates or any other triplet of numeric values.
It uses floating-point coordinates. By default, these floating-point values use 32-bit precision, unlikefloatwhich is always 64-bit. If double precision is needed, compile the engine with the optionprecision=double.
SeeVector3ifor its integer counterpart.
Note:In a boolean context, a Vector3 will evaluate tofalseif it's equal toVector3(0,0,0). Otherwise, a Vector3 will always evaluate totrue.

## Tutorials
- Math documentation index
Math documentation index
- Vector math
Vector math
- Advanced vector math
Advanced vector math
- 3Blue1Brown Essence of Linear Algebra
3Blue1Brown Essence of Linear Algebra
- Matrix Transform Demo
Matrix Transform Demo
- All 3D Demos
All 3D Demos

## Properties

| float | x | 0.0 |
|---|---|---|
| float | y | 0.0 |
| float | z | 0.0 |

float
float
float

## Constructors

| Vector3 | Vector3() |
|---|---|
| Vector3 | Vector3(from:Vector3) |
| Vector3 | Vector3(from:Vector3i) |
| Vector3 | Vector3(x:float, y:float, z:float) |

Vector3
Vector3()
Vector3
Vector3(from:Vector3)
Vector3
Vector3(from:Vector3i)
Vector3
Vector3(x:float, y:float, z:float)

## Methods

| Vector3 | abs()const |
|---|---|
| float | angle_to(to:Vector3)const |
| Vector3 | bezier_derivative(control_1:Vector3, control_2:Vector3, end:Vector3, t:float)const |
| Vector3 | bezier_interpolate(control_1:Vector3, control_2:Vector3, end:Vector3, t:float)const |
| Vector3 | bounce(n:Vector3)const |
| Vector3 | ceil()const |
| Vector3 | clamp(min:Vector3, max:Vector3)const |
| Vector3 | clampf(min:float, max:float)const |
| Vector3 | cross(with:Vector3)const |
| Vector3 | cubic_interpolate(b:Vector3, pre_a:Vector3, post_b:Vector3, weight:float)const |
| Vector3 | cubic_interpolate_in_time(b:Vector3, pre_a:Vector3, post_b:Vector3, weight:float, b_t:float, pre_a_t:float, post_b_t:float)const |
| Vector3 | direction_to(to:Vector3)const |
| float | distance_squared_to(to:Vector3)const |
| float | distance_to(to:Vector3)const |
| float | dot(with:Vector3)const |
| Vector3 | floor()const |
| Vector3 | inverse()const |
| bool | is_equal_approx(to:Vector3)const |
| bool | is_finite()const |
| bool | is_normalized()const |
| bool | is_zero_approx()const |
| float | length()const |
| float | length_squared()const |
| Vector3 | lerp(to:Vector3, weight:float)const |
| Vector3 | limit_length(length:float= 1.0)const |
| Vector3 | max(with:Vector3)const |
| int | max_axis_index()const |
| Vector3 | maxf(with:float)const |
| Vector3 | min(with:Vector3)const |
| int | min_axis_index()const |
| Vector3 | minf(with:float)const |
| Vector3 | move_toward(to:Vector3, delta:float)const |
| Vector3 | normalized()const |
| Vector3 | octahedron_decode(uv:Vector2)static |
| Vector2 | octahedron_encode()const |
| Basis | outer(with:Vector3)const |
| Vector3 | posmod(mod:float)const |
| Vector3 | posmodv(modv:Vector3)const |
| Vector3 | project(b:Vector3)const |
| Vector3 | reflect(n:Vector3)const |
| Vector3 | rotated(axis:Vector3, angle:float)const |
| Vector3 | round()const |
| Vector3 | sign()const |
| float | signed_angle_to(to:Vector3, axis:Vector3)const |
| Vector3 | slerp(to:Vector3, weight:float)const |
| Vector3 | slide(n:Vector3)const |
| Vector3 | snapped(step:Vector3)const |
| Vector3 | snappedf(step:float)const |

Vector3
abs()const
float
angle_to(to:Vector3)const
Vector3
bezier_derivative(control_1:Vector3, control_2:Vector3, end:Vector3, t:float)const
Vector3
bezier_interpolate(control_1:Vector3, control_2:Vector3, end:Vector3, t:float)const
Vector3
bounce(n:Vector3)const
Vector3
ceil()const
Vector3
clamp(min:Vector3, max:Vector3)const
Vector3
clampf(min:float, max:float)const
Vector3
cross(with:Vector3)const
Vector3
cubic_interpolate(b:Vector3, pre_a:Vector3, post_b:Vector3, weight:float)const
Vector3
cubic_interpolate_in_time(b:Vector3, pre_a:Vector3, post_b:Vector3, weight:float, b_t:float, pre_a_t:float, post_b_t:float)const
Vector3
direction_to(to:Vector3)const
float
distance_squared_to(to:Vector3)const
float
distance_to(to:Vector3)const
float
dot(with:Vector3)const
Vector3
floor()const
Vector3
inverse()const
bool
is_equal_approx(to:Vector3)const
bool
is_finite()const
bool
is_normalized()const
bool
is_zero_approx()const
float
length()const
float
length_squared()const
Vector3
lerp(to:Vector3, weight:float)const
Vector3
limit_length(length:float= 1.0)const
Vector3
max(with:Vector3)const
max_axis_index()const
Vector3
maxf(with:float)const
Vector3
min(with:Vector3)const
min_axis_index()const
Vector3
minf(with:float)const
Vector3
move_toward(to:Vector3, delta:float)const
Vector3
normalized()const
Vector3
octahedron_decode(uv:Vector2)static
Vector2
octahedron_encode()const
Basis
outer(with:Vector3)const
Vector3
posmod(mod:float)const
Vector3
posmodv(modv:Vector3)const
Vector3
project(b:Vector3)const
Vector3
reflect(n:Vector3)const
Vector3
rotated(axis:Vector3, angle:float)const
Vector3
round()const
Vector3
sign()const
float
signed_angle_to(to:Vector3, axis:Vector3)const
Vector3
slerp(to:Vector3, weight:float)const
Vector3
slide(n:Vector3)const
Vector3
snapped(step:Vector3)const
Vector3
snappedf(step:float)const

## Operators

| bool | operator !=(right:Vector3) |
|---|---|
| Vector3 | operator *(right:Basis) |
| Vector3 | operator *(right:Quaternion) |
| Vector3 | operator *(right:Transform3D) |
| Vector3 | operator *(right:Vector3) |
| Vector3 | operator *(right:float) |
| Vector3 | operator *(right:int) |
| Vector3 | operator +(right:Vector3) |
| Vector3 | operator -(right:Vector3) |
| Vector3 | operator /(right:Vector3) |
| Vector3 | operator /(right:float) |
| Vector3 | operator /(right:int) |
| bool | operator <(right:Vector3) |
| bool | operator <=(right:Vector3) |
| bool | operator ==(right:Vector3) |
| bool | operator >(right:Vector3) |
| bool | operator >=(right:Vector3) |
| float | operator [](index:int) |
| Vector3 | operator unary+() |
| Vector3 | operator unary-() |

bool
operator !=(right:Vector3)
Vector3
operator *(right:Basis)
Vector3
operator *(right:Quaternion)
Vector3
operator *(right:Transform3D)
Vector3
operator *(right:Vector3)
Vector3
operator *(right:float)
Vector3
operator *(right:int)
Vector3
operator +(right:Vector3)
Vector3
operator -(right:Vector3)
Vector3
operator /(right:Vector3)
Vector3
operator /(right:float)
Vector3
operator /(right:int)
bool
operator <(right:Vector3)
bool
operator <=(right:Vector3)
bool
operator ==(right:Vector3)
bool
operator >(right:Vector3)
bool
operator >=(right:Vector3)
float
operator [](index:int)
Vector3
operator unary+()
Vector3
operator unary-()

## Enumerations
enumAxis:🔗
AxisAXIS_X=0
Enumerated value for the X axis. Returned bymax_axis_index()andmin_axis_index().
AxisAXIS_Y=1
Enumerated value for the Y axis. Returned bymax_axis_index()andmin_axis_index().
AxisAXIS_Z=2
Enumerated value for the Z axis. Returned bymax_axis_index()andmin_axis_index().

## Constants
ZERO=Vector3(0,0,0)🔗
Zero vector, a vector with all components set to0.
ONE=Vector3(1,1,1)🔗
One vector, a vector with all components set to1.
INF=Vector3(inf,inf,inf)🔗
Infinity vector, a vector with all components set to@GDScript.INF.
LEFT=Vector3(-1,0,0)🔗
Left unit vector. Represents the local direction of left, and the global direction of west.
RIGHT=Vector3(1,0,0)🔗
Right unit vector. Represents the local direction of right, and the global direction of east.
UP=Vector3(0,1,0)🔗
Up unit vector.
DOWN=Vector3(0,-1,0)🔗
Down unit vector.
FORWARD=Vector3(0,0,-1)🔗
Forward unit vector. Represents the local direction of forward, and the global direction of north. Keep in mind that the forward direction for lights, cameras, etc is different from 3D assets like characters, which face towards the camera by convention. UseMODEL_FRONTand similar constants when working in 3D asset space.
BACK=Vector3(0,0,1)🔗
Back unit vector. Represents the local direction of back, and the global direction of south.
MODEL_LEFT=Vector3(1,0,0)🔗
Unit vector pointing towards the left side of imported 3D assets.
MODEL_RIGHT=Vector3(-1,0,0)🔗
Unit vector pointing towards the right side of imported 3D assets.
MODEL_TOP=Vector3(0,1,0)🔗
Unit vector pointing towards the top side (up) of imported 3D assets.
MODEL_BOTTOM=Vector3(0,-1,0)🔗
Unit vector pointing towards the bottom side (down) of imported 3D assets.
MODEL_FRONT=Vector3(0,0,1)🔗
Unit vector pointing towards the front side (facing forward) of imported 3D assets.
MODEL_REAR=Vector3(0,0,-1)🔗
Unit vector pointing towards the rear side (back) of imported 3D assets.

## Property Descriptions
floatx=0.0🔗
The vector's X component. Also accessible by using the index position[0].
floaty=0.0🔗
The vector's Y component. Also accessible by using the index position[1].
floatz=0.0🔗
The vector's Z component. Also accessible by using the index position[2].

## Constructor Descriptions
Vector3Vector3()🔗
Constructs a default-initializedVector3with all components set to0.
Vector3Vector3(from:Vector3)
Constructs aVector3as a copy of the givenVector3.
Vector3Vector3(from:Vector3i)
Constructs a newVector3fromVector3i.
Vector3Vector3(x:float, y:float, z:float)
Returns aVector3with the given components.

## Method Descriptions
Vector3abs()const🔗
Returns a new vector with all components in absolute values (i.e. positive).
floatangle_to(to:Vector3)const🔗
Returns the unsigned minimum angle to the given vector, in radians.
Vector3bezier_derivative(control_1:Vector3, control_2:Vector3, end:Vector3, t:float)const🔗
Returns the derivative at the giventon theBézier curvedefined by this vector and the givencontrol_1,control_2, andendpoints.
Vector3bezier_interpolate(control_1:Vector3, control_2:Vector3, end:Vector3, t:float)const🔗
Returns the point at the giventon theBézier curvedefined by this vector and the givencontrol_1,control_2, andendpoints.
Vector3bounce(n:Vector3)const🔗
Returns the vector "bounced off" from a plane defined by the given normaln.
Note:bounce()performs the operation that most engines and frameworks callreflect().
Vector3ceil()const🔗
Returns a new vector with all components rounded up (towards positive infinity).
Vector3clamp(min:Vector3, max:Vector3)const🔗
Returns a new vector with all components clamped between the components ofminandmax, by running@GlobalScope.clamp()on each component.
Vector3clampf(min:float, max:float)const🔗
Returns a new vector with all components clamped betweenminandmax, by running@GlobalScope.clamp()on each component.
Vector3cross(with:Vector3)const🔗
Returns the cross product of this vector andwith.
This returns a vector perpendicular to both this andwith, which would be the normal vector of the plane defined by the two vectors. As there are two such vectors, in opposite directions, this method returns the vector defined by a right-handed coordinate system. If the two vectors are parallel this returns an empty vector, making it useful for testing if two vectors are parallel.
Vector3cubic_interpolate(b:Vector3, pre_a:Vector3, post_b:Vector3, weight:float)const🔗
Performs a cubic interpolation between this vector andbusingpre_aandpost_bas handles, and returns the result at positionweight.weightis on the range of 0.0 to 1.0, representing the amount of interpolation.
Vector3cubic_interpolate_in_time(b:Vector3, pre_a:Vector3, post_b:Vector3, weight:float, b_t:float, pre_a_t:float, post_b_t:float)const🔗
Performs a cubic interpolation between this vector andbusingpre_aandpost_bas handles, and returns the result at positionweight.weightis on the range of 0.0 to 1.0, representing the amount of interpolation.
It can perform smoother interpolation thancubic_interpolate()by the time values.
Vector3direction_to(to:Vector3)const🔗
Returns the normalized vector pointing from this vector toto. This is equivalent to using(b-a).normalized().
floatdistance_squared_to(to:Vector3)const🔗
Returns the squared distance between this vector andto.
This method runs faster thandistance_to(), so prefer it if you need to compare vectors or need the squared distance for some formula.
floatdistance_to(to:Vector3)const🔗
Returns the distance between this vector andto.
floatdot(with:Vector3)const🔗
Returns the dot product of this vector andwith. This can be used to compare the angle between two vectors. For example, this can be used to determine whether an enemy is facing the player.
The dot product will be0for a right angle (90 degrees), greater than 0 for angles narrower than 90 degrees and lower than 0 for angles wider than 90 degrees.
When using unit (normalized) vectors, the result will always be between-1.0(180 degree angle) when the vectors are facing opposite directions, and1.0(0 degree angle) when the vectors are aligned.
Note:a.dot(b)is equivalent tob.dot(a).
Vector3floor()const🔗
Returns a new vector with all components rounded down (towards negative infinity).
Vector3inverse()const🔗
Returns the inverse of the vector. This is the same asVector3(1.0/v.x,1.0/v.y,1.0/v.z).
boolis_equal_approx(to:Vector3)const🔗
Returnstrueif this vector andtoare approximately equal, by running@GlobalScope.is_equal_approx()on each component.
boolis_finite()const🔗
Returnstrueif this vector is finite, by calling@GlobalScope.is_finite()on each component.
boolis_normalized()const🔗
Returnstrueif the vector is normalized, i.e. its length is approximately equal to 1.
boolis_zero_approx()const🔗
Returnstrueif this vector's values are approximately zero, by running@GlobalScope.is_zero_approx()on each component.
This method is faster than usingis_equal_approx()with one value as a zero vector.
floatlength()const🔗
Returns the length (magnitude) of this vector.
floatlength_squared()const🔗
Returns the squared length (squared magnitude) of this vector.
This method runs faster thanlength(), so prefer it if you need to compare vectors or need the squared distance for some formula.
Vector3lerp(to:Vector3, weight:float)const🔗
Returns the result of the linear interpolation between this vector andtoby amountweight.weightis on the range of0.0to1.0, representing the amount of interpolation.
Vector3limit_length(length:float= 1.0)const🔗
Returns the vector with a maximum length by limiting its length tolength. If the vector is non-finite, the result is undefined.
Vector3max(with:Vector3)const🔗
Returns the component-wise maximum of this andwith, equivalent toVector3(maxf(x,with.x),maxf(y,with.y),maxf(z,with.z)).
intmax_axis_index()const🔗
Returns the axis of the vector's highest value. SeeAXIS_*constants. If all components are equal, this method returnsAXIS_X.
Vector3maxf(with:float)const🔗
Returns the component-wise maximum of this andwith, equivalent toVector3(maxf(x,with),maxf(y,with),maxf(z,with)).
Vector3min(with:Vector3)const🔗
Returns the component-wise minimum of this andwith, equivalent toVector3(minf(x,with.x),minf(y,with.y),minf(z,with.z)).
intmin_axis_index()const🔗
Returns the axis of the vector's lowest value. SeeAXIS_*constants. If all components are equal, this method returnsAXIS_Z.
Vector3minf(with:float)const🔗
Returns the component-wise minimum of this andwith, equivalent toVector3(minf(x,with),minf(y,with),minf(z,with)).
Vector3move_toward(to:Vector3, delta:float)const🔗
Returns a new vector moved towardtoby the fixeddeltaamount. Will not go past the final value.
Vector3normalized()const🔗
Returns the result of scaling the vector to unit length. Equivalent tov/v.length(). Returns(0,0,0)ifv.length()==0. See alsois_normalized().
Note:This function may return incorrect values if the input vector length is near zero.
Vector3octahedron_decode(uv:Vector2)static🔗
Returns theVector3from an octahedral-compressed form created usingoctahedron_encode()(stored as aVector2).
Vector2octahedron_encode()const🔗
Returns the octahedral-encoded (oct32) form of thisVector3as aVector2. Since aVector2occupies 1/3 less memory compared toVector3, this form of compression can be used to pass greater amounts ofnormalized()Vector3s without increasing storage or memory requirements. See alsooctahedron_decode().
Note:octahedron_encode()can only be used fornormalized()vectors.octahedron_encode()doesnotcheck whether thisVector3is normalized, and will return a value that does not decompress to the original value if theVector3is not normalized.
Note:Octahedral compression islossy, although visual differences are rarely perceptible in real world scenarios.
Basisouter(with:Vector3)const🔗
Returns the outer product withwith.
Vector3posmod(mod:float)const🔗
Returns a vector composed of the@GlobalScope.fposmod()of this vector's components andmod.
Vector3posmodv(modv:Vector3)const🔗
Returns a vector composed of the@GlobalScope.fposmod()of this vector's components andmodv's components.
Vector3project(b:Vector3)const🔗
Returns a new vector resulting from projecting this vector onto the given vectorb. The resulting new vector is parallel tob. See alsoslide().
Note:If the vectorbis a zero vector, the components of the resulting new vector will be@GDScript.NAN.
Vector3reflect(n:Vector3)const🔗
Returns the result of reflecting the vector through a plane defined by the given normal vectorn.
Note:reflect()differs from what other engines and frameworks callreflect(). In other engines,reflect()returns the result of the vector reflected by the given plane. The reflection thus passes through the given normal. While in Godot the reflection passes through the plane and can be thought of as bouncing off the normal. See alsobounce()which does what most engines callreflect().
Vector3rotated(axis:Vector3, angle:float)const🔗
Returns the result of rotating this vector around a given axis byangle(in radians). The axis must be a normalized vector. See also@GlobalScope.deg_to_rad().
Vector3round()const🔗
Returns a new vector with all components rounded to the nearest integer, with halfway cases rounded away from zero.
Vector3sign()const🔗
Returns a new vector with each component set to1.0if it's positive,-1.0if it's negative, and0.0if it's zero. The result is identical to calling@GlobalScope.sign()on each component.
floatsigned_angle_to(to:Vector3, axis:Vector3)const🔗
Returns the signed angle to the given vector, in radians. The sign of the angle is positive in a counter-clockwise direction and negative in a clockwise direction when viewed from the side specified by theaxis.
Vector3slerp(to:Vector3, weight:float)const🔗
Returns the result of spherical linear interpolation between this vector andto, by amountweight.weightis on the range of 0.0 to 1.0, representing the amount of interpolation.
This method also handles interpolating the lengths if the input vectors have different lengths. For the special case of one or both input vectors having zero length, this method behaves likelerp().
Vector3slide(n:Vector3)const🔗
Returns a new vector resulting from sliding this vector along a plane with normaln. The resulting new vector is perpendicular ton, and is equivalent to this vector minus its projection onn. See alsoproject().
Note:The vectornmust be normalized. See alsonormalized().
Vector3snapped(step:Vector3)const🔗
Returns a new vector with each component snapped to the nearest multiple of the corresponding component instep. This can also be used to round the components to an arbitrary number of decimals.
Vector3snappedf(step:float)const🔗
Returns a new vector with each component snapped to the nearest multiple ofstep. This can also be used to round the components to an arbitrary number of decimals.

## Operator Descriptions
booloperator !=(right:Vector3)🔗
Returnstrueif the vectors are not equal.
Note:Due to floating-point precision errors, consider usingis_equal_approx()instead, which is more reliable.
Note:Vectors with@GDScript.NANelements don't behave the same as other vectors. Therefore, the results from this operator may not be accurate if NaNs are included.
Vector3operator *(right:Basis)🔗
Inversely transforms (multiplies) theVector3by the givenBasismatrix, under the assumption that the basis is orthonormal (i.e. rotation/reflection is fine, scaling/skew is not).
vector*basisis equivalent tobasis.transposed()*vector. SeeBasis.transposed().
For transforming by inverse of a non-orthonormal basis (e.g. with scaling)basis.inverse()*vectorcan be used instead. SeeBasis.inverse().
Vector3operator *(right:Quaternion)🔗
Inversely transforms (multiplies) theVector3by the givenQuaternion.
vector*quaternionis equivalent toquaternion.inverse()*vector. SeeQuaternion.inverse().
Vector3operator *(right:Transform3D)🔗
Inversely transforms (multiplies) theVector3by the givenTransform3Dtransformation matrix, under the assumption that the transformation basis is orthonormal (i.e. rotation/reflection is fine, scaling/skew is not).
vector*transformis equivalent totransform.inverse()*vector. SeeTransform3D.inverse().
For transforming by inverse of an affine transformation (e.g. with scaling)transform.affine_inverse()*vectorcan be used instead. SeeTransform3D.affine_inverse().
Vector3operator *(right:Vector3)🔗
Multiplies each component of theVector3by the components of the givenVector3.
```
print(Vector3(10, 20, 30) * Vector3(3, 4, 5)) # Prints (30.0, 80.0, 150.0)
```
Vector3operator *(right:float)🔗
Multiplies each component of theVector3by the givenfloat.
Vector3operator *(right:int)🔗
Multiplies each component of theVector3by the givenint.
Vector3operator +(right:Vector3)🔗
Adds each component of theVector3by the components of the givenVector3.
```
print(Vector3(10, 20, 30) + Vector3(3, 4, 5)) # Prints (13.0, 24.0, 35.0)
```
Vector3operator -(right:Vector3)🔗
Subtracts each component of theVector3by the components of the givenVector3.
```
print(Vector3(10, 20, 30) - Vector3(3, 4, 5)) # Prints (7.0, 16.0, 25.0)
```
Vector3operator /(right:Vector3)🔗
Divides each component of theVector3by the components of the givenVector3.
```
print(Vector3(10, 20, 30) / Vector3(2, 5, 3)) # Prints (5.0, 4.0, 10.0)
```
Vector3operator /(right:float)🔗
Divides each component of theVector3by the givenfloat.
Vector3operator /(right:int)🔗
Divides each component of theVector3by the givenint.
booloperator <(right:Vector3)🔗
Compares twoVector3vectors by first checking if the X value of the left vector is less than the X value of therightvector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors, and then with the Z values. This operator is useful for sorting vectors.
Note:Vectors with@GDScript.NANelements don't behave the same as other vectors. Therefore, the results from this operator may not be accurate if NaNs are included.
booloperator <=(right:Vector3)🔗
Compares twoVector3vectors by first checking if the X value of the left vector is less than or equal to the X value of therightvector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors, and then with the Z values. This operator is useful for sorting vectors.
Note:Vectors with@GDScript.NANelements don't behave the same as other vectors. Therefore, the results from this operator may not be accurate if NaNs are included.
booloperator ==(right:Vector3)🔗
Returnstrueif the vectors are exactly equal.
Note:Due to floating-point precision errors, consider usingis_equal_approx()instead, which is more reliable.
Note:Vectors with@GDScript.NANelements don't behave the same as other vectors. Therefore, the results from this operator may not be accurate if NaNs are included.
booloperator >(right:Vector3)🔗
Compares twoVector3vectors by first checking if the X value of the left vector is greater than the X value of therightvector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors, and then with the Z values. This operator is useful for sorting vectors.
Note:Vectors with@GDScript.NANelements don't behave the same as other vectors. Therefore, the results from this operator may not be accurate if NaNs are included.
booloperator >=(right:Vector3)🔗
Compares twoVector3vectors by first checking if the X value of the left vector is greater than or equal to the X value of therightvector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors, and then with the Z values. This operator is useful for sorting vectors.
Note:Vectors with@GDScript.NANelements don't behave the same as other vectors. Therefore, the results from this operator may not be accurate if NaNs are included.
floatoperator [](index:int)🔗
Access vector components using theirindex.v[0]is equivalent tov.x,v[1]is equivalent tov.y, andv[2]is equivalent tov.z.
Vector3operator unary+()🔗
Returns the same value as if the+was not there. Unary+does nothing, but sometimes it can make your code more readable.
Vector3operator unary-()🔗
Returns the negative value of theVector3. This is the same as writingVector3(-v.x,-v.y,-v.z). This operation flips the direction of the vector while keeping the same magnitude. With floats, the number zero can be either positive or negative.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.