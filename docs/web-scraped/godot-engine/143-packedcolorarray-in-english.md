# PackedColorArray in English

# PackedColorArray
A packed array ofColors.

## Description
An array specifically designed to holdColor. Packs data tightly, so it saves memory for large array sizes.
Differences between packed arrays, typed arrays, and untyped arrays:Packed arrays are generally faster to iterate on and modify compared to a typed array of the same type (e.g.PackedColorArrayversusArray[Color]). Also, packed arrays consume less memory. As a downside, packed arrays are less flexible as they don't offer as many convenience methods such asArray.map(). Typed arrays are in turn faster to iterate on and modify than untyped arrays.
Note:Packed arrays are always passed by reference. To get a copy of an array that can be modified independently of the original array, useduplicate(). This isnotthe case for built-in properties and methods. In these cases the returned packed array is a copy, and changing it willnotaffect the original value. To update a built-in property of this type, modify the returned array and then assign it to the property again.
Note
There are notable differences when using this API with C#. SeeC# API differences to GDScriptfor more information.

## Constructors

| PackedColorArray | PackedColorArray() |
|---|---|
| PackedColorArray | PackedColorArray(from:PackedColorArray) |
| PackedColorArray | PackedColorArray(from:Array) |

PackedColorArray
PackedColorArray()
PackedColorArray
PackedColorArray(from:PackedColorArray)
PackedColorArray
PackedColorArray(from:Array)

## Methods

| bool | append(value:Color) |
|---|---|
| void | append_array(array:PackedColorArray) |
| int | bsearch(value:Color, before:bool= true)const |
| void | clear() |
| int | count(value:Color)const |
| PackedColorArray | duplicate()const |
| bool | erase(value:Color) |
| void | fill(value:Color) |
| int | find(value:Color, from:int= 0)const |
| Color | get(index:int)const |
| bool | has(value:Color)const |
| int | insert(at_index:int, value:Color) |
| bool | is_empty()const |
| bool | push_back(value:Color) |
| void | remove_at(index:int) |
| int | resize(new_size:int) |
| void | reverse() |
| int | rfind(value:Color, from:int= -1)const |
| void | set(index:int, value:Color) |
| int | size()const |
| PackedColorArray | slice(begin:int, end:int= 2147483647)const |
| void | sort() |
| PackedByteArray | to_byte_array()const |

bool
append(value:Color)
void
append_array(array:PackedColorArray)
bsearch(value:Color, before:bool= true)const
void
clear()
count(value:Color)const
PackedColorArray
duplicate()const
bool
erase(value:Color)
void
fill(value:Color)
find(value:Color, from:int= 0)const
Color
get(index:int)const
bool
has(value:Color)const
insert(at_index:int, value:Color)
bool
is_empty()const
bool
push_back(value:Color)
void
remove_at(index:int)
resize(new_size:int)
void
reverse()
rfind(value:Color, from:int= -1)const
void
set(index:int, value:Color)
size()const
PackedColorArray
slice(begin:int, end:int= 2147483647)const
void
sort()
PackedByteArray
to_byte_array()const

## Operators

| bool | operator !=(right:PackedColorArray) |
|---|---|
| PackedColorArray | operator +(right:PackedColorArray) |
| bool | operator ==(right:PackedColorArray) |
| Color | operator [](index:int) |

bool
operator !=(right:PackedColorArray)
PackedColorArray
operator +(right:PackedColorArray)
bool
operator ==(right:PackedColorArray)
Color
operator [](index:int)

## Constructor Descriptions
PackedColorArrayPackedColorArray()🔗
Constructs an emptyPackedColorArray.
PackedColorArrayPackedColorArray(from:PackedColorArray)
Constructs aPackedColorArrayas a copy of the givenPackedColorArray.
PackedColorArrayPackedColorArray(from:Array)
Constructs a newPackedColorArray. Optionally, you can pass in a genericArraythat will be converted.
Note:When initializing aPackedColorArraywith elements, it must be initialized with anArrayofColorvalues:
```
var array = PackedColorArray([Color(0.1, 0.2, 0.3), Color(0.4, 0.5, 0.6)])
```

## Method Descriptions
boolappend(value:Color)🔗
Appends an element at the end of the array (alias ofpush_back()).
voidappend_array(array:PackedColorArray)🔗
Appends aPackedColorArrayat the end of this array.
intbsearch(value:Color, before:bool= true)const🔗
Finds the index of an existing value (or the insertion index that maintains sorting order, if the value is not yet present in the array) using binary search. Optionally, abeforespecifier can be passed. Iffalse, the returned index comes after all existing entries of the value in the array.
Note:Callingbsearch()on an unsorted array results in unexpected behavior.
voidclear()🔗
Clears the array. This is equivalent to usingresize()with a size of0.
intcount(value:Color)const🔗
Returns the number of times an element is in the array.
PackedColorArrayduplicate()const🔗
Creates a copy of the array, and returns it.
boolerase(value:Color)🔗
Removes the first occurrence of a value from the array and returnstrue. If the value does not exist in the array, nothing happens andfalseis returned. To remove an element by index, useremove_at()instead.
voidfill(value:Color)🔗
Assigns the given value to all elements in the array. This can typically be used together withresize()to create an array with a given size and initialized elements.
intfind(value:Color, from:int= 0)const🔗
Searches the array for a value and returns its index or-1if not found. Optionally, the initial search index can be passed.
Colorget(index:int)const🔗
Returns theColorat the givenindexin the array. Ifindexis out-of-bounds or negative, this method fails and returnsColor(0,0,0,1).
This method is similar (but not identical) to the[]operator. Most notably, when this method fails, it doesn't pause project execution if run from the editor.
boolhas(value:Color)const🔗
Returnstrueif the array containsvalue.
intinsert(at_index:int, value:Color)🔗
Inserts a new element at a given position in the array. The position must be valid, or at the end of the array (idx==size()).
boolis_empty()const🔗
Returnstrueif the array is empty.
boolpush_back(value:Color)🔗
Appends a value to the array.
voidremove_at(index:int)🔗
Removes an element from the array by index.
intresize(new_size:int)🔗
Sets the size of the array. If the array is grown, reserves elements at the end of the array. If the array is shrunk, truncates the array to the new size. Callingresize()once and assigning the new values is faster than adding new elements one by one.
Returns@GlobalScope.OKon success, or one of the followingErrorconstants if this method fails:@GlobalScope.ERR_INVALID_PARAMETERif the size is negative, or@GlobalScope.ERR_OUT_OF_MEMORYif allocations fail. Usesize()to find the actual size of the array after resize.
voidreverse()🔗
Reverses the order of the elements in the array.
intrfind(value:Color, from:int= -1)const🔗
Searches the array in reverse order. Optionally, a start search index can be passed. If negative, the start index is considered relative to the end of the array.
voidset(index:int, value:Color)🔗
Changes theColorat the given index.
intsize()const🔗
Returns the number of elements in the array.
PackedColorArrayslice(begin:int, end:int= 2147483647)const🔗
Returns the slice of thePackedColorArray, frombegin(inclusive) toend(exclusive), as a newPackedColorArray.
The absolute value ofbeginandendwill be clamped to the array size, so the default value forendmakes it slice to the size of the array by default (i.e.arr.slice(1)is a shorthand forarr.slice(1,arr.size())).
If eitherbeginorendare negative, they will be relative to the end of the array (i.e.arr.slice(0,-2)is a shorthand forarr.slice(0,arr.size()-2)).
voidsort()🔗
Sorts the elements of the array in ascending order.
PackedByteArrayto_byte_array()const🔗
Returns aPackedByteArraywith each color encoded as bytes.

## Operator Descriptions
booloperator !=(right:PackedColorArray)🔗
Returnstrueif contents of the arrays differ.
PackedColorArrayoperator +(right:PackedColorArray)🔗
Returns a newPackedColorArraywith contents ofrightadded at the end of this array. For better performance, consider usingappend_array()instead.
booloperator ==(right:PackedColorArray)🔗
Returnstrueif contents of both arrays are the same, i.e. they have all equalColors at the corresponding indices.
Coloroperator [](index:int)🔗
Returns theColorat indexindex. Negative indices can be used to access the elements starting from the end. Using index out of array's bounds will result in an error.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.