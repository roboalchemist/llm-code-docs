# PackedVector4Array

# PackedVector4Array
A packed array ofVector4s.

## Description
An array specifically designed to holdVector4. Packs data tightly, so it saves memory for large array sizes.
Differences between packed arrays, typed arrays, and untyped arrays:Packed arrays are generally faster to iterate on and modify compared to a typed array of the same type (e.g.PackedVector4ArrayversusArray[Vector4]). Also, packed arrays consume less memory. As a downside, packed arrays are less flexible as they don't offer as many convenience methods such asArray.map(). Typed arrays are in turn faster to iterate on and modify than untyped arrays.
Note:Packed arrays are always passed by reference. To get a copy of an array that can be modified independently of the original array, useduplicate(). This isnotthe case for built-in properties and methods. In these cases the returned packed array is a copy, and changing it willnotaffect the original value. To update a built-in property of this type, modify the returned array and then assign it to the property again.
Note
There are notable differences when using this API with C#. SeeC# API differences to GDScriptfor more information.

## Constructors

| PackedVector4Array | PackedVector4Array() |
|---|---|
| PackedVector4Array | PackedVector4Array(from:PackedVector4Array) |
| PackedVector4Array | PackedVector4Array(from:Array) |

PackedVector4Array
PackedVector4Array()
PackedVector4Array
PackedVector4Array(from:PackedVector4Array)
PackedVector4Array
PackedVector4Array(from:Array)

## Methods

| bool | append(value:Vector4) |
|---|---|
| void | append_array(array:PackedVector4Array) |
| int | bsearch(value:Vector4, before:bool= true)const |
| void | clear() |
| int | count(value:Vector4)const |
| PackedVector4Array | duplicate()const |
| bool | erase(value:Vector4) |
| void | fill(value:Vector4) |
| int | find(value:Vector4, from:int= 0)const |
| Vector4 | get(index:int)const |
| bool | has(value:Vector4)const |
| int | insert(at_index:int, value:Vector4) |
| bool | is_empty()const |
| bool | push_back(value:Vector4) |
| void | remove_at(index:int) |
| int | resize(new_size:int) |
| void | reverse() |
| int | rfind(value:Vector4, from:int= -1)const |
| void | set(index:int, value:Vector4) |
| int | size()const |
| PackedVector4Array | slice(begin:int, end:int= 2147483647)const |
| void | sort() |
| PackedByteArray | to_byte_array()const |

bool
append(value:Vector4)
void
append_array(array:PackedVector4Array)
bsearch(value:Vector4, before:bool= true)const
void
clear()
count(value:Vector4)const
PackedVector4Array
duplicate()const
bool
erase(value:Vector4)
void
fill(value:Vector4)
find(value:Vector4, from:int= 0)const
Vector4
get(index:int)const
bool
has(value:Vector4)const
insert(at_index:int, value:Vector4)
bool
is_empty()const
bool
push_back(value:Vector4)
void
remove_at(index:int)
resize(new_size:int)
void
reverse()
rfind(value:Vector4, from:int= -1)const
void
set(index:int, value:Vector4)
size()const
PackedVector4Array
slice(begin:int, end:int= 2147483647)const
void
sort()
PackedByteArray
to_byte_array()const

## Operators

| bool | operator !=(right:PackedVector4Array) |
|---|---|
| PackedVector4Array | operator +(right:PackedVector4Array) |
| bool | operator ==(right:PackedVector4Array) |
| Vector4 | operator [](index:int) |

bool
operator !=(right:PackedVector4Array)
PackedVector4Array
operator +(right:PackedVector4Array)
bool
operator ==(right:PackedVector4Array)
Vector4
operator [](index:int)

## Constructor Descriptions
PackedVector4ArrayPackedVector4Array()🔗
Constructs an emptyPackedVector4Array.
PackedVector4ArrayPackedVector4Array(from:PackedVector4Array)
Constructs aPackedVector4Arrayas a copy of the givenPackedVector4Array.
PackedVector4ArrayPackedVector4Array(from:Array)
Constructs a newPackedVector4Array. Optionally, you can pass in a genericArraythat will be converted.
Note:When initializing aPackedVector4Arraywith elements, it must be initialized with anArrayofVector4values:
```
var array = PackedVector4Array([Vector4(12, 34, 56, 78), Vector4(90, 12, 34, 56)])
```

## Method Descriptions
boolappend(value:Vector4)🔗
Appends an element at the end of the array (alias ofpush_back()).
voidappend_array(array:PackedVector4Array)🔗
Appends aPackedVector4Arrayat the end of this array.
intbsearch(value:Vector4, before:bool= true)const🔗
Finds the index of an existing value (or the insertion index that maintains sorting order, if the value is not yet present in the array) using binary search. Optionally, abeforespecifier can be passed. Iffalse, the returned index comes after all existing entries of the value in the array.
Note:Callingbsearch()on an unsorted array results in unexpected behavior.
Note:Vectors with@GDScript.NANelements don't behave the same as other vectors. Therefore, the results from this method may not be accurate if NaNs are included.
voidclear()🔗
Clears the array. This is equivalent to usingresize()with a size of0.
intcount(value:Vector4)const🔗
Returns the number of times an element is in the array.
Note:Vectors with@GDScript.NANelements don't behave the same as other vectors. Therefore, the results from this method may not be accurate if NaNs are included.
PackedVector4Arrayduplicate()const🔗
Creates a copy of the array, and returns it.
boolerase(value:Vector4)🔗
Removes the first occurrence of a value from the array and returnstrue. If the value does not exist in the array, nothing happens andfalseis returned. To remove an element by index, useremove_at()instead.
Note:Vectors with@GDScript.NANelements don't behave the same as other vectors. Therefore, the results from this method may not be accurate if NaNs are included.
voidfill(value:Vector4)🔗
Assigns the given value to all elements in the array. This can typically be used together withresize()to create an array with a given size and initialized elements.
intfind(value:Vector4, from:int= 0)const🔗
Searches the array for a value and returns its index or-1if not found. Optionally, the initial search index can be passed.
Note:Vectors with@GDScript.NANelements don't behave the same as other vectors. Therefore, the results from this method may not be accurate if NaNs are included.
Vector4get(index:int)const🔗
Returns theVector4at the givenindexin the array. Ifindexis out-of-bounds or negative, this method fails and returnsVector4(0,0,0,0).
This method is similar (but not identical) to the[]operator. Most notably, when this method fails, it doesn't pause project execution if run from the editor.
boolhas(value:Vector4)const🔗
Returnstrueif the array containsvalue.
Note:Vectors with@GDScript.NANelements don't behave the same as other vectors. Therefore, the results from this method may not be accurate if NaNs are included.
intinsert(at_index:int, value:Vector4)🔗
Inserts a new element at a given position in the array. The position must be valid, or at the end of the array (idx==size()).
boolis_empty()const🔗
Returnstrueif the array is empty.
boolpush_back(value:Vector4)🔗
Inserts aVector4at the end.
voidremove_at(index:int)🔗
Removes an element from the array by index.
intresize(new_size:int)🔗
Sets the size of the array. If the array is grown, reserves elements at the end of the array. If the array is shrunk, truncates the array to the new size. Callingresize()once and assigning the new values is faster than adding new elements one by one.
Returns@GlobalScope.OKon success, or one of the followingErrorconstants if this method fails:@GlobalScope.ERR_INVALID_PARAMETERif the size is negative, or@GlobalScope.ERR_OUT_OF_MEMORYif allocations fail. Usesize()to find the actual size of the array after resize.
voidreverse()🔗
Reverses the order of the elements in the array.
intrfind(value:Vector4, from:int= -1)const🔗
Searches the array in reverse order. Optionally, a start search index can be passed. If negative, the start index is considered relative to the end of the array.
Note:Vectors with@GDScript.NANelements don't behave the same as other vectors. Therefore, the results from this method may not be accurate if NaNs are included.
voidset(index:int, value:Vector4)🔗
Changes theVector4at the given index.
intsize()const🔗
Returns the number of elements in the array.
PackedVector4Arrayslice(begin:int, end:int= 2147483647)const🔗
Returns the slice of thePackedVector4Array, frombegin(inclusive) toend(exclusive), as a newPackedVector4Array.
The absolute value ofbeginandendwill be clamped to the array size, so the default value forendmakes it slice to the size of the array by default (i.e.arr.slice(1)is a shorthand forarr.slice(1,arr.size())).
If eitherbeginorendare negative, they will be relative to the end of the array (i.e.arr.slice(0,-2)is a shorthand forarr.slice(0,arr.size()-2)).
voidsort()🔗
Sorts the elements of the array in ascending order.
Note:Vectors with@GDScript.NANelements don't behave the same as other vectors. Therefore, the results from this method may not be accurate if NaNs are included.
PackedByteArrayto_byte_array()const🔗
Returns aPackedByteArraywith each vector encoded as bytes.

## Operator Descriptions
booloperator !=(right:PackedVector4Array)🔗
Returnstrueif contents of the arrays differ.
PackedVector4Arrayoperator +(right:PackedVector4Array)🔗
Returns a newPackedVector4Arraywith contents ofrightadded at the end of this array. For better performance, consider usingappend_array()instead.
booloperator ==(right:PackedVector4Array)🔗
Returnstrueif contents of both arrays are the same, i.e. they have all equalVector4s at the corresponding indices.
Vector4operator [](index:int)🔗
Returns theVector4at indexindex. Negative indices can be used to access the elements starting from the end. Using index out of array's bounds will result in an error.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.