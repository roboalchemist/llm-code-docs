# Vector4

# Vector4
A 4D vector using floating-point coordinates.

## Description
A 4-element structure that can be used to represent 4D coordinates or any other quadruplet of numeric values.
It uses floating-point coordinates. By default, these floating-point values use 32-bit precision, unlikefloatwhich is always 64-bit. If double precision is needed, compile the engine with the optionprecision=double.
SeeVector4ifor its integer counterpart.
Note:In a boolean context, a Vector4 will evaluate tofalseif it's equal toVector4(0,0,0,0). Otherwise, a Vector4 will always evaluate totrue.

## Properties

| float | w | 0.0 |
|---|---|---|
| float | x | 0.0 |
| float | y | 0.0 |
| float | z | 0.0 |

float
float
float
float

## Constructors

| Vector4 | Vector4() |
|---|---|
| Vector4 | Vector4(from:Vector4) |
| Vector4 | Vector4(from:Vector4i) |
| Vector4 | Vector4(x:float, y:float, z:float, w:float) |

Vector4
Vector4()
Vector4
Vector4(from:Vector4)
Vector4
Vector4(from:Vector4i)
Vector4
Vector4(x:float, y:float, z:float, w:float)

## Methods

| Vector4 | abs()const |
|---|---|
| Vector4 | ceil()const |
| Vector4 | clamp(min:Vector4, max:Vector4)const |
| Vector4 | clampf(min:float, max:float)const |
| Vector4 | cubic_interpolate(b:Vector4, pre_a:Vector4, post_b:Vector4, weight:float)const |
| Vector4 | cubic_interpolate_in_time(b:Vector4, pre_a:Vector4, post_b:Vector4, weight:float, b_t:float, pre_a_t:float, post_b_t:float)const |
| Vector4 | direction_to(to:Vector4)const |
| float | distance_squared_to(to:Vector4)const |
| float | distance_to(to:Vector4)const |
| float | dot(with:Vector4)const |
| Vector4 | floor()const |
| Vector4 | inverse()const |
| bool | is_equal_approx(to:Vector4)const |
| bool | is_finite()const |
| bool | is_normalized()const |
| bool | is_zero_approx()const |
| float | length()const |
| float | length_squared()const |
| Vector4 | lerp(to:Vector4, weight:float)const |
| Vector4 | max(with:Vector4)const |
| int | max_axis_index()const |
| Vector4 | maxf(with:float)const |
| Vector4 | min(with:Vector4)const |
| int | min_axis_index()const |
| Vector4 | minf(with:float)const |
| Vector4 | normalized()const |
| Vector4 | posmod(mod:float)const |
| Vector4 | posmodv(modv:Vector4)const |
| Vector4 | round()const |
| Vector4 | sign()const |
| Vector4 | snapped(step:Vector4)const |
| Vector4 | snappedf(step:float)const |

Vector4
abs()const
Vector4
ceil()const
Vector4
clamp(min:Vector4, max:Vector4)const
Vector4
clampf(min:float, max:float)const
Vector4
cubic_interpolate(b:Vector4, pre_a:Vector4, post_b:Vector4, weight:float)const
Vector4
cubic_interpolate_in_time(b:Vector4, pre_a:Vector4, post_b:Vector4, weight:float, b_t:float, pre_a_t:float, post_b_t:float)const
Vector4
direction_to(to:Vector4)const
float
distance_squared_to(to:Vector4)const
float
distance_to(to:Vector4)const
float
dot(with:Vector4)const
Vector4
floor()const
Vector4
inverse()const
bool
is_equal_approx(to:Vector4)const
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
Vector4
lerp(to:Vector4, weight:float)const
Vector4
max(with:Vector4)const
max_axis_index()const
Vector4
maxf(with:float)const
Vector4
min(with:Vector4)const
min_axis_index()const
Vector4
minf(with:float)const
Vector4
normalized()const
Vector4
posmod(mod:float)const
Vector4
posmodv(modv:Vector4)const
Vector4
round()const
Vector4
sign()const
Vector4
snapped(step:Vector4)const
Vector4
snappedf(step:float)const

## Operators

| bool | operator !=(right:Vector4) |
|---|---|
| Vector4 | operator *(right:Projection) |
| Vector4 | operator *(right:Vector4) |
| Vector4 | operator *(right:float) |
| Vector4 | operator *(right:int) |
| Vector4 | operator +(right:Vector4) |
| Vector4 | operator -(right:Vector4) |
| Vector4 | operator /(right:Vector4) |
| Vector4 | operator /(right:float) |
| Vector4 | operator /(right:int) |
| bool | operator <(right:Vector4) |
| bool | operator <=(right:Vector4) |
| bool | operator ==(right:Vector4) |
| bool | operator >(right:Vector4) |
| bool | operator >=(right:Vector4) |
| float | operator [](index:int) |
| Vector4 | operator unary+() |
| Vector4 | operator unary-() |

bool
operator !=(right:Vector4)
Vector4
operator *(right:Projection)
Vector4
operator *(right:Vector4)
Vector4
operator *(right:float)
Vector4
operator *(right:int)
Vector4
operator +(right:Vector4)
Vector4
operator -(right:Vector4)
Vector4
operator /(right:Vector4)
Vector4
operator /(right:float)
Vector4
operator /(right:int)
bool
operator <(right:Vector4)
bool
operator <=(right:Vector4)
bool
operator ==(right:Vector4)
bool
operator >(right:Vector4)
bool
operator >=(right:Vector4)
float
operator [](index:int)
Vector4
operator unary+()
Vector4
operator unary-()

## Enumerations
enumAxis:🔗
AxisAXIS_X=0
Enumerated value for the X axis. Returned bymax_axis_index()andmin_axis_index().
AxisAXIS_Y=1
Enumerated value for the Y axis. Returned bymax_axis_index()andmin_axis_index().
AxisAXIS_Z=2
Enumerated value for the Z axis. Returned bymax_axis_index()andmin_axis_index().
AxisAXIS_W=3
Enumerated value for the W axis. Returned bymax_axis_index()andmin_axis_index().

## Constants
ZERO=Vector4(0,0,0,0)🔗
Zero vector, a vector with all components set to0.
ONE=Vector4(1,1,1,1)🔗
One vector, a vector with all components set to1.
INF=Vector4(inf,inf,inf,inf)🔗
Infinity vector, a vector with all components set to@GDScript.INF.

## Property Descriptions
floatw=0.0🔗
The vector's W component. Also accessible by using the index position[3].
floatx=0.0🔗
The vector's X component. Also accessible by using the index position[0].
floaty=0.0🔗
The vector's Y component. Also accessible by using the index position[1].
floatz=0.0🔗
The vector's Z component. Also accessible by using the index position[2].

## Constructor Descriptions
Vector4Vector4()🔗
Constructs a default-initializedVector4with all components set to0.
Vector4Vector4(from:Vector4)
Constructs aVector4as a copy of the givenVector4.
Vector4Vector4(from:Vector4i)
Constructs a newVector4from the givenVector4i.
Vector4Vector4(x:float, y:float, z:float, w:float)
Returns aVector4with the given components.

## Method Descriptions
Vector4abs()const🔗
Returns a new vector with all components in absolute values (i.e. positive).
Vector4ceil()const🔗
Returns a new vector with all components rounded up (towards positive infinity).
Vector4clamp(min:Vector4, max:Vector4)const🔗
Returns a new vector with all components clamped between the components ofminandmax, by running@GlobalScope.clamp()on each component.
Vector4clampf(min:float, max:float)const🔗
Returns a new vector with all components clamped betweenminandmax, by running@GlobalScope.clamp()on each component.
Vector4cubic_interpolate(b:Vector4, pre_a:Vector4, post_b:Vector4, weight:float)const🔗
Performs a cubic interpolation between this vector andbusingpre_aandpost_bas handles, and returns the result at positionweight.weightis on the range of 0.0 to 1.0, representing the amount of interpolation.
Vector4cubic_interpolate_in_time(b:Vector4, pre_a:Vector4, post_b:Vector4, weight:float, b_t:float, pre_a_t:float, post_b_t:float)const🔗
Performs a cubic interpolation between this vector andbusingpre_aandpost_bas handles, and returns the result at positionweight.weightis on the range of 0.0 to 1.0, representing the amount of interpolation.
It can perform smoother interpolation thancubic_interpolate()by the time values.
Vector4direction_to(to:Vector4)const🔗
Returns the normalized vector pointing from this vector toto. This is equivalent to using(b-a).normalized().
floatdistance_squared_to(to:Vector4)const🔗
Returns the squared distance between this vector andto.
This method runs faster thandistance_to(), so prefer it if you need to compare vectors or need the squared distance for some formula.
floatdistance_to(to:Vector4)const🔗
Returns the distance between this vector andto.
floatdot(with:Vector4)const🔗
Returns the dot product of this vector andwith.
Vector4floor()const🔗
Returns a new vector with all components rounded down (towards negative infinity).
Vector4inverse()const🔗
Returns the inverse of the vector. This is the same asVector4(1.0/v.x,1.0/v.y,1.0/v.z,1.0/v.w).
boolis_equal_approx(to:Vector4)const🔗
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
Vector4lerp(to:Vector4, weight:float)const🔗
Returns the result of the linear interpolation between this vector andtoby amountweight.weightis on the range of0.0to1.0, representing the amount of interpolation.
Vector4max(with:Vector4)const🔗
Returns the component-wise maximum of this andwith, equivalent toVector4(maxf(x,with.x),maxf(y,with.y),maxf(z,with.z),maxf(w,with.w)).
intmax_axis_index()const🔗
Returns the axis of the vector's highest value. SeeAXIS_*constants. If all components are equal, this method returnsAXIS_X.
Vector4maxf(with:float)const🔗
Returns the component-wise maximum of this andwith, equivalent toVector4(maxf(x,with),maxf(y,with),maxf(z,with),maxf(w,with)).
Vector4min(with:Vector4)const🔗
Returns the component-wise minimum of this andwith, equivalent toVector4(minf(x,with.x),minf(y,with.y),minf(z,with.z),minf(w,with.w)).
intmin_axis_index()const🔗
Returns the axis of the vector's lowest value. SeeAXIS_*constants. If all components are equal, this method returnsAXIS_W.
Vector4minf(with:float)const🔗
Returns the component-wise minimum of this andwith, equivalent toVector4(minf(x,with),minf(y,with),minf(z,with),minf(w,with)).
Vector4normalized()const🔗
Returns the result of scaling the vector to unit length. Equivalent tov/v.length(). Returns(0,0,0,0)ifv.length()==0. See alsois_normalized().
Note:This function may return incorrect values if the input vector length is near zero.
Vector4posmod(mod:float)const🔗
Returns a vector composed of the@GlobalScope.fposmod()of this vector's components andmod.
Vector4posmodv(modv:Vector4)const🔗
Returns a vector composed of the@GlobalScope.fposmod()of this vector's components andmodv's components.
Vector4round()const🔗
Returns a new vector with all components rounded to the nearest integer, with halfway cases rounded away from zero.
Vector4sign()const🔗
Returns a new vector with each component set to1.0if it's positive,-1.0if it's negative, and0.0if it's zero. The result is identical to calling@GlobalScope.sign()on each component.
Vector4snapped(step:Vector4)const🔗
Returns a new vector with each component snapped to the nearest multiple of the corresponding component instep. This can also be used to round the components to an arbitrary number of decimals.
Vector4snappedf(step:float)const🔗
Returns a new vector with each component snapped to the nearest multiple ofstep. This can also be used to round the components to an arbitrary number of decimals.

## Operator Descriptions
booloperator !=(right:Vector4)🔗
Returnstrueif the vectors are not equal.
Note:Due to floating-point precision errors, consider usingis_equal_approx()instead, which is more reliable.
Note:Vectors with@GDScript.NANelements don't behave the same as other vectors. Therefore, the results from this operator may not be accurate if NaNs are included.
Vector4operator *(right:Projection)🔗
Transforms (multiplies) theVector4by the transpose of the givenProjectionmatrix.
For transforming by inverse of a projectionprojection.inverse()*vectorcan be used instead. SeeProjection.inverse().
Vector4operator *(right:Vector4)🔗
Multiplies each component of theVector4by the components of the givenVector4.
```
print(Vector4(10, 20, 30, 40) * Vector4(3, 4, 5, 6)) # Prints (30.0, 80.0, 150.0, 240.0)
```
Vector4operator *(right:float)🔗
Multiplies each component of theVector4by the givenfloat.
```
print(Vector4(10, 20, 30, 40) * 2) # Prints (20.0, 40.0, 60.0, 80.0)
```
Vector4operator *(right:int)🔗
Multiplies each component of theVector4by the givenint.
Vector4operator +(right:Vector4)🔗
Adds each component of theVector4by the components of the givenVector4.
```
print(Vector4(10, 20, 30, 40) + Vector4(3, 4, 5, 6)) # Prints (13.0, 24.0, 35.0, 46.0)
```
Vector4operator -(right:Vector4)🔗
Subtracts each component of theVector4by the components of the givenVector4.
```
print(Vector4(10, 20, 30, 40) - Vector4(3, 4, 5, 6)) # Prints (7.0, 16.0, 25.0, 34.0)
```
Vector4operator /(right:Vector4)🔗
Divides each component of theVector4by the components of the givenVector4.
```
print(Vector4(10, 20, 30, 40) / Vector4(2, 5, 3, 4)) # Prints (5.0, 4.0, 10.0, 10.0)
```
Vector4operator /(right:float)🔗
Divides each component of theVector4by the givenfloat.
```
print(Vector4(10, 20, 30, 40) / 2) # Prints (5.0, 10.0, 15.0, 20.0)
```
Vector4operator /(right:int)🔗
Divides each component of theVector4by the givenint.
booloperator <(right:Vector4)🔗
Compares twoVector4vectors by first checking if the X value of the left vector is less than the X value of therightvector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors, Z values of the two vectors, and then with the W values. This operator is useful for sorting vectors.
Note:Vectors with@GDScript.NANelements don't behave the same as other vectors. Therefore, the results from this operator may not be accurate if NaNs are included.
booloperator <=(right:Vector4)🔗
Compares twoVector4vectors by first checking if the X value of the left vector is less than or equal to the X value of therightvector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors, Z values of the two vectors, and then with the W values. This operator is useful for sorting vectors.
Note:Vectors with@GDScript.NANelements don't behave the same as other vectors. Therefore, the results from this operator may not be accurate if NaNs are included.
booloperator ==(right:Vector4)🔗
Returnstrueif the vectors are exactly equal.
Note:Due to floating-point precision errors, consider usingis_equal_approx()instead, which is more reliable.
Note:Vectors with@GDScript.NANelements don't behave the same as other vectors. Therefore, the results from this operator may not be accurate if NaNs are included.
booloperator >(right:Vector4)🔗
Compares twoVector4vectors by first checking if the X value of the left vector is greater than the X value of therightvector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors, Z values of the two vectors, and then with the W values. This operator is useful for sorting vectors.
Note:Vectors with@GDScript.NANelements don't behave the same as other vectors. Therefore, the results from this operator may not be accurate if NaNs are included.
booloperator >=(right:Vector4)🔗
Compares twoVector4vectors by first checking if the X value of the left vector is greater than or equal to the X value of therightvector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors, Z values of the two vectors, and then with the W values. This operator is useful for sorting vectors.
Note:Vectors with@GDScript.NANelements don't behave the same as other vectors. Therefore, the results from this operator may not be accurate if NaNs are included.
floatoperator [](index:int)🔗
Access vector components using theirindex.v[0]is equivalent tov.x,v[1]is equivalent tov.y,v[2]is equivalent tov.z, andv[3]is equivalent tov.w.
Vector4operator unary+()🔗
Returns the same value as if the+was not there. Unary+does nothing, but sometimes it can make your code more readable.
Vector4operator unary-()🔗
Returns the negative value of theVector4. This is the same as writingVector4(-v.x,-v.y,-v.z,-v.w). This operation flips the direction of the vector while keeping the same magnitude. With floats, the number zero can be either positive or negative.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.