# Vector3i in English

# Vector3i

A 3D vector using integer coordinates.

## Description

A 3-element structure that can be used to represent 3D grid coordinates or any other triplet of integers.
It uses integer coordinates and is therefore preferable toVector3when exact precision is required. Note that the values are limited to 32 bits, and unlikeVector3this cannot be configured with an engine build option. UseintorPackedInt64Arrayif 64-bit values are needed.
Note:In a boolean context, a Vector3i will evaluate tofalseif it's equal toVector3i(0,0,0). Otherwise, a Vector3i will always evaluate totrue.

## Tutorials

- Math documentation index
Math documentation index
- Vector math
Vector math
- 3Blue1Brown Essence of Linear Algebra
3Blue1Brown Essence of Linear Algebra

## Properties

| int | x | 0 |
|---|---|---|
| int | y | 0 |
| int | z | 0 |

## Constructors

| Vector3i | Vector3i() |
|---|---|
| Vector3i | Vector3i(from:Vector3i) |
| Vector3i | Vector3i(from:Vector3) |
| Vector3i | Vector3i(x:int, y:int, z:int) |

Vector3i
Vector3i()
Vector3i
Vector3i(from:Vector3i)
Vector3i
Vector3i(from:Vector3)
Vector3i
Vector3i(x:int, y:int, z:int)

## Methods

| Vector3i | abs()const |
|---|---|
| Vector3i | clamp(min:Vector3i, max:Vector3i)const |
| Vector3i | clampi(min:int, max:int)const |
| int | distance_squared_to(to:Vector3i)const |
| float | distance_to(to:Vector3i)const |
| float | length()const |
| int | length_squared()const |
| Vector3i | max(with:Vector3i)const |
| int | max_axis_index()const |
| Vector3i | maxi(with:int)const |
| Vector3i | min(with:Vector3i)const |
| int | min_axis_index()const |
| Vector3i | mini(with:int)const |
| Vector3i | sign()const |
| Vector3i | snapped(step:Vector3i)const |
| Vector3i | snappedi(step:int)const |

Vector3i
abs()const
Vector3i
clamp(min:Vector3i, max:Vector3i)const
Vector3i
clampi(min:int, max:int)const
distance_squared_to(to:Vector3i)const
float
distance_to(to:Vector3i)const
float
length()const
length_squared()const
Vector3i
max(with:Vector3i)const
max_axis_index()const
Vector3i
maxi(with:int)const
Vector3i
min(with:Vector3i)const
min_axis_index()const
Vector3i
mini(with:int)const
Vector3i
sign()const
Vector3i
snapped(step:Vector3i)const
Vector3i
snappedi(step:int)const

## Operators

| bool | operator !=(right:Vector3i) |
|---|---|
| Vector3i | operator %(right:Vector3i) |
| Vector3i | operator %(right:int) |
| Vector3i | operator *(right:Vector3i) |
| Vector3 | operator *(right:float) |
| Vector3i | operator *(right:int) |
| Vector3i | operator +(right:Vector3i) |
| Vector3i | operator -(right:Vector3i) |
| Vector3i | operator /(right:Vector3i) |
| Vector3 | operator /(right:float) |
| Vector3i | operator /(right:int) |
| bool | operator <(right:Vector3i) |
| bool | operator <=(right:Vector3i) |
| bool | operator ==(right:Vector3i) |
| bool | operator >(right:Vector3i) |
| bool | operator >=(right:Vector3i) |
| int | operator [](index:int) |
| Vector3i | operator unary+() |
| Vector3i | operator unary-() |

bool
operator !=(right:Vector3i)
Vector3i
operator %(right:Vector3i)
Vector3i
operator %(right:int)
Vector3i
operator *(right:Vector3i)
Vector3
operator*(right:float)
Vector3i
operator *(right:int)
Vector3i
operator +(right:Vector3i)
Vector3i
operator -(right:Vector3i)
Vector3i
operator /(right:Vector3i)
Vector3
operator /(right:float)
Vector3i
operator /(right:int)
bool
operator <(right:Vector3i)
bool
operator <=(right:Vector3i)
bool
operator ==(right:Vector3i)
bool
operator >(right:Vector3i)
bool
operator >=(right:Vector3i)
operator [](index:int)
Vector3i
operator unary+()
Vector3i
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

ZERO=Vector3i(0,0,0)🔗
Zero vector, a vector with all components set to0.
ONE=Vector3i(1,1,1)🔗
One vector, a vector with all components set to1.
MIN=Vector3i(-2147483648,-2147483648,-2147483648)🔗
Min vector, a vector with all components equal toINT32_MIN. Can be used as a negative integer equivalent ofVector3.INF.
MAX=Vector3i(2147483647,2147483647,2147483647)🔗
Max vector, a vector with all components equal toINT32_MAX. Can be used as an integer equivalent ofVector3.INF.
LEFT=Vector3i(-1,0,0)🔗
Left unit vector. Represents the local direction of left, and the global direction of west.
RIGHT=Vector3i(1,0,0)🔗
Right unit vector. Represents the local direction of right, and the global direction of east.
UP=Vector3i(0,1,0)🔗
Up unit vector.
DOWN=Vector3i(0,-1,0)🔗
Down unit vector.
FORWARD=Vector3i(0,0,-1)🔗
Forward unit vector. Represents the local direction of forward, and the global direction of north.
BACK=Vector3i(0,0,1)🔗
Back unit vector. Represents the local direction of back, and the global direction of south.

## Property Descriptions

intx=0🔗
The vector's X component. Also accessible by using the index position[0].
inty=0🔗
The vector's Y component. Also accessible by using the index position[1].
intz=0🔗
The vector's Z component. Also accessible by using the index position[2].

## Constructor Descriptions

Vector3iVector3i()🔗
Constructs a default-initializedVector3iwith all components set to0.
Vector3iVector3i(from:Vector3i)
Constructs aVector3ias a copy of the givenVector3i.
Vector3iVector3i(from:Vector3)
Constructs a newVector3ifrom the givenVector3by truncating components' fractional parts (rounding towards zero). For a different behavior consider passing the result ofVector3.ceil(),Vector3.floor()orVector3.round()to this constructor instead.
Vector3iVector3i(x:int, y:int, z:int)
Returns aVector3iwith the given components.

## Method Descriptions

Vector3iabs()const🔗
Returns a new vector with all components in absolute values (i.e. positive).
Vector3iclamp(min:Vector3i, max:Vector3i)const🔗
Returns a new vector with all components clamped between the components ofminandmax, by running@GlobalScope.clamp()on each component.
Vector3iclampi(min:int, max:int)const🔗
Returns a new vector with all components clamped betweenminandmax, by running@GlobalScope.clamp()on each component.
intdistance_squared_to(to:Vector3i)const🔗
Returns the squared distance between this vector andto.
This method runs faster thandistance_to(), so prefer it if you need to compare vectors or need the squared distance for some formula.
floatdistance_to(to:Vector3i)const🔗
Returns the distance between this vector andto.
floatlength()const🔗
Returns the length (magnitude) of this vector.
intlength_squared()const🔗
Returns the squared length (squared magnitude) of this vector.
This method runs faster thanlength(), so prefer it if you need to compare vectors or need the squared distance for some formula.
Vector3imax(with:Vector3i)const🔗
Returns the component-wise maximum of this andwith, equivalent toVector3i(maxi(x,with.x),maxi(y,with.y),maxi(z,with.z)).
intmax_axis_index()const🔗
Returns the axis of the vector's highest value. SeeAXIS_*constants. If all components are equal, this method returnsAXIS_X.
Vector3imaxi(with:int)const🔗
Returns the component-wise maximum of this andwith, equivalent toVector3i(maxi(x,with),maxi(y,with),maxi(z,with)).
Vector3imin(with:Vector3i)const🔗
Returns the component-wise minimum of this andwith, equivalent toVector3i(mini(x,with.x),mini(y,with.y),mini(z,with.z)).
intmin_axis_index()const🔗
Returns the axis of the vector's lowest value. SeeAXIS_*constants. If all components are equal, this method returnsAXIS_Z.
Vector3imini(with:int)const🔗
Returns the component-wise minimum of this andwith, equivalent toVector3i(mini(x,with),mini(y,with),mini(z,with)).
Vector3isign()const🔗
Returns a new vector with each component set to1if it's positive,-1if it's negative, and0if it's zero. The result is identical to calling@GlobalScope.sign()on each component.
Vector3isnapped(step:Vector3i)const🔗
Returns a new vector with each component snapped to the closest multiple of the corresponding component instep.
Vector3isnappedi(step:int)const🔗
Returns a new vector with each component snapped to the closest multiple ofstep.

## Operator Descriptions

booloperator !=(right:Vector3i)🔗
Returnstrueif the vectors are not equal.
Vector3ioperator %(right:Vector3i)🔗
Gets the remainder of each component of theVector3iwith the components of the givenVector3i. This operation uses truncated division, which is often not desired as it does not work well with negative numbers. Consider using@GlobalScope.posmod()instead if you want to handle negative numbers.

```
print(Vector3i(10, -20, 30) % Vector3i(7, 8, 9)) # Prints (3, -4, 3)
```

Vector3ioperator %(right:int)🔗
Gets the remainder of each component of theVector3iwith the givenint. This operation uses truncated division, which is often not desired as it does not work well with negative numbers. Consider using@GlobalScope.posmod()instead if you want to handle negative numbers.

```
print(Vector3i(10, -20, 30) % 7) # Prints (3, -6, 2)
```

Vector3ioperator *(right:Vector3i)🔗
Multiplies each component of theVector3iby the components of the givenVector3i.

```
print(Vector3i(10, 20, 30) * Vector3i(3, 4, 5)) # Prints (30, 80, 150)
```

Vector3operator *(right:float)🔗
Multiplies each component of theVector3iby the givenfloat. Returns aVector3.

```
print(Vector3i(10, 15, 20) * 0.9) # Prints (9.0, 13.5, 18.0)
```

Vector3ioperator *(right:int)🔗
Multiplies each component of theVector3iby the givenint.
Vector3ioperator +(right:Vector3i)🔗
Adds each component of theVector3iby the components of the givenVector3i.

```
print(Vector3i(10, 20, 30) + Vector3i(3, 4, 5)) # Prints (13, 24, 35)
```

Vector3ioperator -(right:Vector3i)🔗
Subtracts each component of theVector3iby the components of the givenVector3i.

```
print(Vector3i(10, 20, 30) - Vector3i(3, 4, 5)) # Prints (7, 16, 25)
```

Vector3ioperator /(right:Vector3i)🔗
Divides each component of theVector3iby the components of the givenVector3i.

```
print(Vector3i(10, 20, 30) / Vector3i(2, 5, 3)) # Prints (5, 4, 10)
```

Vector3operator /(right:float)🔗
Divides each component of theVector3iby the givenfloat. Returns aVector3.

```
print(Vector3i(1, 2, 3) / 2.5) # Prints (0.4, 0.8, 1.2)
```

Vector3ioperator /(right:int)🔗
Divides each component of theVector3iby the givenint.
booloperator <(right:Vector3i)🔗
Compares twoVector3ivectors by first checking if the X value of the left vector is less than the X value of therightvector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors, and then with the Z values. This operator is useful for sorting vectors.
booloperator <=(right:Vector3i)🔗
Compares twoVector3ivectors by first checking if the X value of the left vector is less than or equal to the X value of therightvector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors, and then with the Z values. This operator is useful for sorting vectors.
booloperator ==(right:Vector3i)🔗
Returnstrueif the vectors are equal.
booloperator >(right:Vector3i)🔗
Compares twoVector3ivectors by first checking if the X value of the left vector is greater than the X value of therightvector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors, and then with the Z values. This operator is useful for sorting vectors.
booloperator >=(right:Vector3i)🔗
Compares twoVector3ivectors by first checking if the X value of the left vector is greater than or equal to the X value of therightvector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors, and then with the Z values. This operator is useful for sorting vectors.
intoperator [](index:int)🔗
Access vector components using theirindex.v[0]is equivalent tov.x,v[1]is equivalent tov.y, andv[2]is equivalent tov.z.
Vector3ioperator unary+()🔗
Returns the same value as if the+was not there. Unary+does nothing, but sometimes it can make your code more readable.
Vector3ioperator unary-()🔗
Returns the negative value of theVector3i. This is the same as writingVector3i(-v.x,-v.y,-v.z). This operation flips the direction of the vector while keeping the same magnitude.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
