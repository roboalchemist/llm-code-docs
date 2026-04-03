# Vector2 in English

# Vector2
A 2D vector using floating-point coordinates.

## Description
A 2-element structure that can be used to represent 2D coordinates or any other pair of numeric values.
It uses floating-point coordinates. By default, these floating-point values use 32-bit precision, unlikefloatwhich is always 64-bit. If double precision is needed, compile the engine with the optionprecision=double.
SeeVector2ifor its integer counterpart.
Note:In a boolean context, a Vector2 will evaluate tofalseif it's equal toVector2(0,0). Otherwise, a Vector2 will always evaluate totrue.

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
- All 2D Demos
All 2D Demos

## Properties

| float | x | 0.0 |
|---|---|---|
| float | y | 0.0 |

float
float

## Constructors

| Vector2 | Vector2() |
|---|---|
| Vector2 | Vector2(from:Vector2) |
| Vector2 | Vector2(from:Vector2i) |
| Vector2 | Vector2(x:float, y:float) |

Vector2
Vector2()
Vector2
Vector2(from:Vector2)
Vector2
Vector2(from:Vector2i)
Vector2
Vector2(x:float, y:float)

## Methods

| Vector2 | abs()const |
|---|---|
| float | angle()const |
| float | angle_to(to:Vector2)const |
| float | angle_to_point(to:Vector2)const |
| float | aspect()const |
| Vector2 | bezier_derivative(control_1:Vector2, control_2:Vector2, end:Vector2, t:float)const |
| Vector2 | bezier_interpolate(control_1:Vector2, control_2:Vector2, end:Vector2, t:float)const |
| Vector2 | bounce(n:Vector2)const |
| Vector2 | ceil()const |
| Vector2 | clamp(min:Vector2, max:Vector2)const |
| Vector2 | clampf(min:float, max:float)const |
| float | cross(with:Vector2)const |
| Vector2 | cubic_interpolate(b:Vector2, pre_a:Vector2, post_b:Vector2, weight:float)const |
| Vector2 | cubic_interpolate_in_time(b:Vector2, pre_a:Vector2, post_b:Vector2, weight:float, b_t:float, pre_a_t:float, post_b_t:float)const |
| Vector2 | direction_to(to:Vector2)const |
| float | distance_squared_to(to:Vector2)const |
| float | distance_to(to:Vector2)const |
| float | dot(with:Vector2)const |
| Vector2 | floor()const |
| Vector2 | from_angle(angle:float)static |
| bool | is_equal_approx(to:Vector2)const |
| bool | is_finite()const |
| bool | is_normalized()const |
| bool | is_zero_approx()const |
| float | length()const |
| float | length_squared()const |
| Vector2 | lerp(to:Vector2, weight:float)const |
| Vector2 | limit_length(length:float= 1.0)const |
| Vector2 | max(with:Vector2)const |
| int | max_axis_index()const |
| Vector2 | maxf(with:float)const |
| Vector2 | min(with:Vector2)const |
| int | min_axis_index()const |
| Vector2 | minf(with:float)const |
| Vector2 | move_toward(to:Vector2, delta:float)const |
| Vector2 | normalized()const |
| Vector2 | orthogonal()const |
| Vector2 | posmod(mod:float)const |
| Vector2 | posmodv(modv:Vector2)const |
| Vector2 | project(b:Vector2)const |
| Vector2 | reflect(line:Vector2)const |
| Vector2 | rotated(angle:float)const |
| Vector2 | round()const |
| Vector2 | sign()const |
| Vector2 | slerp(to:Vector2, weight:float)const |
| Vector2 | slide(n:Vector2)const |
| Vector2 | snapped(step:Vector2)const |
| Vector2 | snappedf(step:float)const |

Vector2
abs()const
float
angle()const
float
angle_to(to:Vector2)const
float
angle_to_point(to:Vector2)const
float
aspect()const
Vector2
bezier_derivative(control_1:Vector2, control_2:Vector2, end:Vector2, t:float)const
Vector2
bezier_interpolate(control_1:Vector2, control_2:Vector2, end:Vector2, t:float)const
Vector2
bounce(n:Vector2)const
Vector2
ceil()const
Vector2
clamp(min:Vector2, max:Vector2)const
Vector2
clampf(min:float, max:float)const
float
cross(with:Vector2)const
Vector2
cubic_interpolate(b:Vector2, pre_a:Vector2, post_b:Vector2, weight:float)const
Vector2
cubic_interpolate_in_time(b:Vector2, pre_a:Vector2, post_b:Vector2, weight:float, b_t:float, pre_a_t:float, post_b_t:float)const
Vector2
direction_to(to:Vector2)const
float
distance_squared_to(to:Vector2)const
float
distance_to(to:Vector2)const
float
dot(with:Vector2)const
Vector2
floor()const
Vector2
from_angle(angle:float)static
bool
is_equal_approx(to:Vector2)const
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
Vector2
lerp(to:Vector2, weight:float)const
Vector2
limit_length(length:float= 1.0)const
Vector2
max(with:Vector2)const
max_axis_index()const
Vector2
maxf(with:float)const
Vector2
min(with:Vector2)const
min_axis_index()const
Vector2
minf(with:float)const
Vector2
move_toward(to:Vector2, delta:float)const
Vector2
normalized()const
Vector2
orthogonal()const
Vector2
posmod(mod:float)const
Vector2
posmodv(modv:Vector2)const
Vector2
project(b:Vector2)const
Vector2
reflect(line:Vector2)const
Vector2
rotated(angle:float)const
Vector2
round()const
Vector2
sign()const
Vector2
slerp(to:Vector2, weight:float)const
Vector2
slide(n:Vector2)const
Vector2
snapped(step:Vector2)const
Vector2
snappedf(step:float)const

## Operators

| bool | operator !=(right:Vector2) |
|---|---|
| Vector2 | operator *(right:Transform2D) |
| Vector2 | operator *(right:Vector2) |
| Vector2 | operator *(right:float) |
| Vector2 | operator *(right:int) |
| Vector2 | operator +(right:Vector2) |
| Vector2 | operator -(right:Vector2) |
| Vector2 | operator /(right:Vector2) |
| Vector2 | operator /(right:float) |
| Vector2 | operator /(right:int) |
| bool | operator <(right:Vector2) |
| bool | operator <=(right:Vector2) |
| bool | operator ==(right:Vector2) |
| bool | operator >(right:Vector2) |
| bool | operator >=(right:Vector2) |
| float | operator [](index:int) |
| Vector2 | operator unary+() |
| Vector2 | operator unary-() |

bool
operator !=(right:Vector2)
Vector2
operator *(right:Transform2D)
Vector2
operator *(right:Vector2)
Vector2
operator *(right:float)
Vector2
operator *(right:int)
Vector2
operator +(right:Vector2)
Vector2
operator -(right:Vector2)
Vector2
operator /(right:Vector2)
Vector2
operator /(right:float)
Vector2
operator /(right:int)
bool
operator <(right:Vector2)
bool
operator <=(right:Vector2)
bool
operator ==(right:Vector2)
bool
operator >(right:Vector2)
bool
operator >=(right:Vector2)
float
operator [](index:int)
Vector2
operator unary+()
Vector2
operator unary-()

## Enumerations
enumAxis:🔗
AxisAXIS_X=0
Enumerated value for the X axis. Returned bymax_axis_index()andmin_axis_index().
AxisAXIS_Y=1
Enumerated value for the Y axis. Returned bymax_axis_index()andmin_axis_index().

## Constants
ZERO=Vector2(0,0)🔗
Zero vector, a vector with all components set to0.
ONE=Vector2(1,1)🔗
One vector, a vector with all components set to1.
INF=Vector2(inf,inf)🔗
Infinity vector, a vector with all components set to@GDScript.INF.
LEFT=Vector2(-1,0)🔗
Left unit vector. Represents the direction of left.
RIGHT=Vector2(1,0)🔗
Right unit vector. Represents the direction of right.
UP=Vector2(0,-1)🔗
Up unit vector. Y is down in 2D, so this vector points -Y.
DOWN=Vector2(0,1)🔗
Down unit vector. Y is down in 2D, so this vector points +Y.

## Property Descriptions
floatx=0.0🔗
The vector's X component. Also accessible by using the index position[0].
floaty=0.0🔗
The vector's Y component. Also accessible by using the index position[1].

## Constructor Descriptions
Vector2Vector2()🔗
Constructs a default-initializedVector2with all components set to0.
Vector2Vector2(from:Vector2)
Constructs aVector2as a copy of the givenVector2.
Vector2Vector2(from:Vector2i)
Constructs a newVector2fromVector2i.
Vector2Vector2(x:float, y:float)
Constructs a newVector2from the givenxandy.

## Method Descriptions
Vector2abs()const🔗
Returns a new vector with all components in absolute values (i.e. positive).
floatangle()const🔗
Returns this vector's angle with respect to the positive X axis, or(1,0)vector, in radians.
For example,Vector2.RIGHT.angle()will return zero,Vector2.DOWN.angle()will returnPI/2(a quarter turn, or 90 degrees), andVector2(1,-1).angle()will return-PI/4(a negative eighth turn, or -45 degrees).
This is equivalent to calling@GlobalScope.atan2()withyandx.
Illustration of the returned angle.
floatangle_to(to:Vector2)const🔗
Returns the signed angle to the given vector, in radians. The result ranges from-PItoPI(inclusive).
Illustration of the returned angle.
floatangle_to_point(to:Vector2)const🔗
Returns the signed angle between the X axis and the line from this vector to pointto, in radians. The result ranges from-PItoPI(inclusive).
a.angle_to_point(b)is equivalent to(b-a).angle(). See alsoangle().
Illustration of the returned angle.
floataspect()const🔗
Returns this vector's aspect ratio, which isxdivided byy.
Vector2bezier_derivative(control_1:Vector2, control_2:Vector2, end:Vector2, t:float)const🔗
Returns the derivative at the giventon theBézier curvedefined by this vector and the givencontrol_1,control_2, andendpoints.
Vector2bezier_interpolate(control_1:Vector2, control_2:Vector2, end:Vector2, t:float)const🔗
Returns the point at the giventon theBézier curvedefined by this vector and the givencontrol_1,control_2, andendpoints.
Vector2bounce(n:Vector2)const🔗
Returns the vector "bounced off" from a line defined by the given normalnperpendicular to the line.
Note:bounce()performs the operation that most engines and frameworks callreflect().
Vector2ceil()const🔗
Returns a new vector with all components rounded up (towards positive infinity).
Vector2clamp(min:Vector2, max:Vector2)const🔗
Returns a new vector with all components clamped between the components ofminandmax, by running@GlobalScope.clamp()on each component.
Vector2clampf(min:float, max:float)const🔗
Returns a new vector with all components clamped betweenminandmax, by running@GlobalScope.clamp()on each component.
floatcross(with:Vector2)const🔗
Returns the 2D analog of the cross product for this vector andwith.
This is the signed area of the parallelogram formed by the two vectors. If the second vector is clockwise from the first vector, then the cross product is the positive area. If counter-clockwise, the cross product is the negative area. If the two vectors are parallel this returns zero, making it useful for testing if two vectors are parallel.
Note:Cross product is not defined in 2D mathematically. This method embeds the 2D vectors in the XY plane of 3D space and uses their cross product's Z component as the analog.
Vector2cubic_interpolate(b:Vector2, pre_a:Vector2, post_b:Vector2, weight:float)const🔗
Performs a cubic interpolation between this vector andbusingpre_aandpost_bas handles, and returns the result at positionweight.weightis on the range of 0.0 to 1.0, representing the amount of interpolation.
Vector2cubic_interpolate_in_time(b:Vector2, pre_a:Vector2, post_b:Vector2, weight:float, b_t:float, pre_a_t:float, post_b_t:float)const🔗
Performs a cubic interpolation between this vector andbusingpre_aandpost_bas handles, and returns the result at positionweight.weightis on the range of 0.0 to 1.0, representing the amount of interpolation.
It can perform smoother interpolation thancubic_interpolate()by the time values.
Vector2direction_to(to:Vector2)const🔗
Returns the normalized vector pointing from this vector toto.
a.direction_to(b)is equivalent to(b-a).normalized(). See alsonormalized().
floatdistance_squared_to(to:Vector2)const🔗
Returns the squared distance between this vector andto.
This method runs faster thandistance_to(), so prefer it if you need to compare vectors or need the squared distance for some formula.
floatdistance_to(to:Vector2)const🔗
Returns the distance between this vector andto.
floatdot(with:Vector2)const🔗
Returns the dot product of this vector andwith. This can be used to compare the angle between two vectors. For example, this can be used to determine whether an enemy is facing the player.
The dot product will be0for a right angle (90 degrees), greater than 0 for angles narrower than 90 degrees and lower than 0 for angles wider than 90 degrees.
When using unit (normalized) vectors, the result will always be between-1.0(180 degree angle) when the vectors are facing opposite directions, and1.0(0 degree angle) when the vectors are aligned.
Note:a.dot(b)is equivalent tob.dot(a).
Vector2floor()const🔗
Returns a new vector with all components rounded down (towards negative infinity).
Vector2from_angle(angle:float)static🔗
Creates aVector2rotated to the givenanglein radians. This is equivalent to doingVector2(cos(angle),sin(angle))orVector2.RIGHT.rotated(angle).
```
print(Vector2.from_angle(0)) # Prints (1.0, 0.0)
print(Vector2(1, 0).angle()) # Prints 0.0, which is the angle used above.
print(Vector2.from_angle(PI / 2)) # Prints (0.0, 1.0)
```
Note:The length of the returnedVector2isapproximately1.0, but is is not guaranteed to be exactly1.0due to floating-point precision issues. Callnormalized()on the returnedVector2if you require a unit vector.
boolis_equal_approx(to:Vector2)const🔗
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
Vector2lerp(to:Vector2, weight:float)const🔗
Returns the result of the linear interpolation between this vector andtoby amountweight.weightis on the range of0.0to1.0, representing the amount of interpolation.
Vector2limit_length(length:float= 1.0)const🔗
Returns the vector with a maximum length by limiting its length tolength. If the vector is non-finite, the result is undefined.
Vector2max(with:Vector2)const🔗
Returns the component-wise maximum of this andwith, equivalent toVector2(maxf(x,with.x),maxf(y,with.y)).
intmax_axis_index()const🔗
Returns the axis of the vector's highest value. SeeAXIS_*constants. If all components are equal, this method returnsAXIS_X.
Vector2maxf(with:float)const🔗
Returns the component-wise maximum of this andwith, equivalent toVector2(maxf(x,with),maxf(y,with)).
Vector2min(with:Vector2)const🔗
Returns the component-wise minimum of this andwith, equivalent toVector2(minf(x,with.x),minf(y,with.y)).
intmin_axis_index()const🔗
Returns the axis of the vector's lowest value. SeeAXIS_*constants. If all components are equal, this method returnsAXIS_Y.
Vector2minf(with:float)const🔗
Returns the component-wise minimum of this andwith, equivalent toVector2(minf(x,with),minf(y,with)).
Vector2move_toward(to:Vector2, delta:float)const🔗
Returns a new vector moved towardtoby the fixeddeltaamount. Will not go past the final value.
Vector2normalized()const🔗
Returns the result of scaling the vector to unit length. Equivalent tov/v.length(). Returns(0,0)ifv.length()==0. See alsois_normalized().
Note:This function may return incorrect values if the input vector length is near zero.
Vector2orthogonal()const🔗
Returns a perpendicular vector rotated 90 degrees counter-clockwise compared to the original, with the same length.
Vector2posmod(mod:float)const🔗
Returns a vector composed of the@GlobalScope.fposmod()of this vector's components andmod.
Vector2posmodv(modv:Vector2)const🔗
Returns a vector composed of the@GlobalScope.fposmod()of this vector's components andmodv's components.
Vector2project(b:Vector2)const🔗
Returns a new vector resulting from projecting this vector onto the given vectorb. The resulting new vector is parallel tob. See alsoslide().
Note:If the vectorbis a zero vector, the components of the resulting new vector will be@GDScript.NAN.
Vector2reflect(line:Vector2)const🔗
Returns the result of reflecting the vector from a line defined by the given direction vectorline.
Note:reflect()differs from what other engines and frameworks callreflect(). In other engines,reflect()takes a normal direction which is a direction perpendicular to the line. In Godot, you specify the direction of the line directly. See alsobounce()which does what most engines callreflect().
Vector2rotated(angle:float)const🔗
Returns the result of rotating this vector byangle(in radians). See also@GlobalScope.deg_to_rad().
Vector2round()const🔗
Returns a new vector with all components rounded to the nearest integer, with halfway cases rounded away from zero.
Vector2sign()const🔗
Returns a new vector with each component set to1.0if it's positive,-1.0if it's negative, and0.0if it's zero. The result is identical to calling@GlobalScope.sign()on each component.
Vector2slerp(to:Vector2, weight:float)const🔗
Returns the result of spherical linear interpolation between this vector andto, by amountweight.weightis on the range of 0.0 to 1.0, representing the amount of interpolation.
This method also handles interpolating the lengths if the input vectors have different lengths. For the special case of one or both input vectors having zero length, this method behaves likelerp().
Vector2slide(n:Vector2)const🔗
Returns a new vector resulting from sliding this vector along a line with normaln. The resulting new vector is perpendicular ton, and is equivalent to this vector minus its projection onn. See alsoproject().
Note:The vectornmust be normalized. See alsonormalized().
Vector2snapped(step:Vector2)const🔗
Returns a new vector with each component snapped to the nearest multiple of the corresponding component instep. This can also be used to round the components to an arbitrary number of decimals.
Vector2snappedf(step:float)const🔗
Returns a new vector with each component snapped to the nearest multiple ofstep. This can also be used to round the components to an arbitrary number of decimals.

## Operator Descriptions
booloperator !=(right:Vector2)🔗
Returnstrueif the vectors are not equal.
Note:Due to floating-point precision errors, consider usingis_equal_approx()instead, which is more reliable.
Note:Vectors with@GDScript.NANelements don't behave the same as other vectors. Therefore, the results from this operator may not be accurate if NaNs are included.
Vector2operator *(right:Transform2D)🔗
Inversely transforms (multiplies) theVector2by the givenTransform2Dtransformation matrix, under the assumption that the transformation basis is orthonormal (i.e. rotation/reflection is fine, scaling/skew is not).
vector*transformis equivalent totransform.inverse()*vector. SeeTransform2D.inverse().
For transforming by inverse of an affine transformation (e.g. with scaling)transform.affine_inverse()*vectorcan be used instead. SeeTransform2D.affine_inverse().
Vector2operator *(right:Vector2)🔗
Multiplies each component of theVector2by the components of the givenVector2.
```
print(Vector2(10, 20) * Vector2(3, 4)) # Prints (30.0, 80.0)
```
Vector2operator *(right:float)🔗
Multiplies each component of theVector2by the givenfloat.
Vector2operator *(right:int)🔗
Multiplies each component of theVector2by the givenint.
Vector2operator +(right:Vector2)🔗
Adds each component of theVector2by the components of the givenVector2.
```
print(Vector2(10, 20) + Vector2(3, 4)) # Prints (13.0, 24.0)
```
Vector2operator -(right:Vector2)🔗
Subtracts each component of theVector2by the components of the givenVector2.
```
print(Vector2(10, 20) - Vector2(3, 4)) # Prints (7.0, 16.0)
```
Vector2operator /(right:Vector2)🔗
Divides each component of theVector2by the components of the givenVector2.
```
print(Vector2(10, 20) / Vector2(2, 5)) # Prints (5.0, 4.0)
```
Vector2operator /(right:float)🔗
Divides each component of theVector2by the givenfloat.
Vector2operator /(right:int)🔗
Divides each component of theVector2by the givenint.
booloperator <(right:Vector2)🔗
Compares twoVector2vectors by first checking if the X value of the left vector is less than the X value of therightvector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors. This operator is useful for sorting vectors.
Note:Vectors with@GDScript.NANelements don't behave the same as other vectors. Therefore, the results from this operator may not be accurate if NaNs are included.
booloperator <=(right:Vector2)🔗
Compares twoVector2vectors by first checking if the X value of the left vector is less than or equal to the X value of therightvector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors. This operator is useful for sorting vectors.
Note:Vectors with@GDScript.NANelements don't behave the same as other vectors. Therefore, the results from this operator may not be accurate if NaNs are included.
booloperator ==(right:Vector2)🔗
Returnstrueif the vectors are exactly equal.
Note:Due to floating-point precision errors, consider usingis_equal_approx()instead, which is more reliable.
Note:Vectors with@GDScript.NANelements don't behave the same as other vectors. Therefore, the results from this operator may not be accurate if NaNs are included.
booloperator >(right:Vector2)🔗
Compares twoVector2vectors by first checking if the X value of the left vector is greater than the X value of therightvector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors. This operator is useful for sorting vectors.
Note:Vectors with@GDScript.NANelements don't behave the same as other vectors. Therefore, the results from this operator may not be accurate if NaNs are included.
booloperator >=(right:Vector2)🔗
Compares twoVector2vectors by first checking if the X value of the left vector is greater than or equal to the X value of therightvector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors. This operator is useful for sorting vectors.
Note:Vectors with@GDScript.NANelements don't behave the same as other vectors. Therefore, the results from this operator may not be accurate if NaNs are included.
floatoperator [](index:int)🔗
Access vector components using theirindex.v[0]is equivalent tov.x, andv[1]is equivalent tov.y.
Vector2operator unary+()🔗
Returns the same value as if the+was not there. Unary+does nothing, but sometimes it can make your code more readable.
Vector2operator unary-()🔗
Returns the negative value of theVector2. This is the same as writingVector2(-v.x,-v.y). This operation flips the direction of the vector while keeping the same magnitude. With floats, the number zero can be either positive or negative.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.