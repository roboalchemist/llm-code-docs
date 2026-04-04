# PackedFloat32Array in English

# PackedFloat32Array

A packed array of 32-bit floating-point values.

## Description

An array specifically designed to hold 32-bit floating-point values (float). Packs data tightly, so it saves memory for large array sizes.
If you need to pack 64-bit floats tightly, seePackedFloat64Array.
Note:Packed arrays are always passed by reference. To get a copy of an array that can be modified independently of the original array, useduplicate(). This isnotthe case for built-in properties and methods. In these cases the returned packed array is a copy, and changing it willnotaffect the original value. To update a built-in property of this type, modify the returned array and then assign it to the property again.
Note
There are notable differences when using this API with C#. SeeC# API differences to GDScriptfor more information.

## Constructors

| PackedFloat32Array | PackedFloat32Array() |
|---|---|
| PackedFloat32Array | PackedFloat32Array(from:PackedFloat32Array) |
| PackedFloat32Array | PackedFloat32Array(from:Array) |

PackedFloat32Array
PackedFloat32Array()
PackedFloat32Array
PackedFloat32Array(from:PackedFloat32Array)
PackedFloat32Array
PackedFloat32Array(from:Array)

## Methods

| bool | append(value:float) |
|---|---|
| void | append_array(array:PackedFloat32Array) |
| int | bsearch(value:float, before:bool= true)const |
| void | clear() |
| int | count(value:float)const |
| PackedFloat32Array | duplicate()const |
| bool | erase(value:float) |
| void | fill(value:float) |
| int | find(value:float, from:int= 0)const |
| float | get(index:int)const |
| bool | has(value:float)const |
| int | insert(at_index:int, value:float) |
| bool | is_empty()const |
| bool | push_back(value:float) |
| void | remove_at(index:int) |
| int | resize(new_size:int) |
| void | reverse() |
| int | rfind(value:float, from:int= -1)const |
| void | set(index:int, value:float) |
| int | size()const |
| PackedFloat32Array | slice(begin:int, end:int= 2147483647)const |
| void | sort() |
| PackedByteArray | to_byte_array()const |

bool
append(value:float)
void
append_array(array:PackedFloat32Array)
bsearch(value:float, before:bool= true)const
void
clear()
count(value:float)const
PackedFloat32Array
duplicate()const
bool
erase(value:float)
void
fill(value:float)
find(value:float, from:int= 0)const
float
get(index:int)const
bool
has(value:float)const
insert(at_index:int, value:float)
bool
is_empty()const
bool
push_back(value:float)
void
remove_at(index:int)
resize(new_size:int)
void
reverse()
rfind(value:float, from:int= -1)const
void
set(index:int, value:float)
size()const
PackedFloat32Array
slice(begin:int, end:int= 2147483647)const
void
sort()
PackedByteArray
to_byte_array()const

## Operators

| bool | operator !=(right:PackedFloat32Array) |
|---|---|
| PackedFloat32Array | operator +(right:PackedFloat32Array) |
| bool | operator ==(right:PackedFloat32Array) |
| float | operator [](index:int) |

bool
operator !=(right:PackedFloat32Array)
PackedFloat32Array
operator +(right:PackedFloat32Array)
bool
operator ==(right:PackedFloat32Array)
float
operator [](index:int)

## Constructor Descriptions

PackedFloat32ArrayPackedFloat32Array()🔗
Constructs an emptyPackedFloat32Array.
PackedFloat32ArrayPackedFloat32Array(from:PackedFloat32Array)
Constructs aPackedFloat32Arrayas a copy of the givenPackedFloat32Array.
PackedFloat32ArrayPackedFloat32Array(from:Array)
Constructs a newPackedFloat32Array. Optionally, you can pass in a genericArraythat will be converted.

## Method Descriptions

boolappend(value:float)🔗
Appends an element at the end of the array (alias ofpush_back()).
voidappend_array(array:PackedFloat32Array)🔗
Appends aPackedFloat32Arrayat the end of this array.
intbsearch(value:float, before:bool= true)const🔗
Finds the index of an existing value (or the insertion index that maintains sorting order, if the value is not yet present in the array) using binary search. Optionally, abeforespecifier can be passed. Iffalse, the returned index comes after all existing entries of the value in the array.
Note:Callingbsearch()on an unsorted array results in unexpected behavior.
Note:@GDScript.NANdoesn't behave the same as other numbers. Therefore, the results from this method may not be accurate if NaNs are included.
voidclear()🔗
Clears the array. This is equivalent to usingresize()with a size of0.
intcount(value:float)const🔗
Returns the number of times an element is in the array.
Note:@GDScript.NANdoesn't behave the same as other numbers. Therefore, the results from this method may not be accurate if NaNs are included.
PackedFloat32Arrayduplicate()const🔗
Creates a copy of the array, and returns it.
boolerase(value:float)🔗
Removes the first occurrence of a value from the array and returnstrue. If the value does not exist in the array, nothing happens andfalseis returned. To remove an element by index, useremove_at()instead.
Note:@GDScript.NANdoesn't behave the same as other numbers. Therefore, the results from this method may not be accurate if NaNs are included.
voidfill(value:float)🔗
Assigns the given value to all elements in the array. This can typically be used together withresize()to create an array with a given size and initialized elements.
intfind(value:float, from:int= 0)const🔗
Searches the array for a value and returns its index or-1if not found. Optionally, the initial search index can be passed.
Note:@GDScript.NANdoesn't behave the same as other numbers. Therefore, the results from this method may not be accurate if NaNs are included.
floatget(index:int)const🔗
Returns the 32-bit float at the givenindexin the array. Ifindexis out-of-bounds or negative, this method fails and returns0.0.
This method is similar (but not identical) to the[]operator. Most notably, when this method fails, it doesn't pause project execution if run from the editor.
boolhas(value:float)const🔗
Returnstrueif the array containsvalue.
Note:@GDScript.NANdoesn't behave the same as other numbers. Therefore, the results from this method may not be accurate if NaNs are included.
intinsert(at_index:int, value:float)🔗
Inserts a new element at a given position in the array. The position must be valid, or at the end of the array (idx==size()).
boolis_empty()const🔗
Returnstrueif the array is empty.
boolpush_back(value:float)🔗
Appends an element at the end of the array.
voidremove_at(index:int)🔗
Removes an element from the array by index.
intresize(new_size:int)🔗
Sets the size of the array. If the array is grown, reserves elements at the end of the array. If the array is shrunk, truncates the array to the new size. Callingresize()once and assigning the new values is faster than adding new elements one by one.
Returns@GlobalScope.OKon success, or one of the followingErrorconstants if this method fails:@GlobalScope.ERR_INVALID_PARAMETERif the size is negative, or@GlobalScope.ERR_OUT_OF_MEMORYif allocations fail. Usesize()to find the actual size of the array after resize.
voidreverse()🔗
Reverses the order of the elements in the array.
intrfind(value:float, from:int= -1)const🔗
Searches the array in reverse order. Optionally, a start search index can be passed. If negative, the start index is considered relative to the end of the array.
Note:@GDScript.NANdoesn't behave the same as other numbers. Therefore, the results from this method may not be accurate if NaNs are included.
voidset(index:int, value:float)🔗
Changes the float at the given index.
intsize()const🔗
Returns the number of elements in the array.
PackedFloat32Arrayslice(begin:int, end:int= 2147483647)const🔗
Returns the slice of thePackedFloat32Array, frombegin(inclusive) toend(exclusive), as a newPackedFloat32Array.
The absolute value ofbeginandendwill be clamped to the array size, so the default value forendmakes it slice to the size of the array by default (i.e.arr.slice(1)is a shorthand forarr.slice(1,arr.size())).
If eitherbeginorendare negative, they will be relative to the end of the array (i.e.arr.slice(0,-2)is a shorthand forarr.slice(0,arr.size()-2)).
voidsort()🔗
Sorts the elements of the array in ascending order.
Note:@GDScript.NANdoesn't behave the same as other numbers. Therefore, the results from this method may not be accurate if NaNs are included.
PackedByteArrayto_byte_array()const🔗
Returns a copy of the data converted to aPackedByteArray, where each element has been encoded as 4 bytes.
The size of the new array will befloat32_array.size()*4.

## Operator Descriptions

booloperator !=(right:PackedFloat32Array)🔗
Returnstrueif contents of the arrays differ.
PackedFloat32Arrayoperator +(right:PackedFloat32Array)🔗
Returns a newPackedFloat32Arraywith contents ofrightadded at the end of this array. For better performance, consider usingappend_array()instead.
booloperator ==(right:PackedFloat32Array)🔗
Returnstrueif contents of both arrays are the same, i.e. they have all equal floats at the corresponding indices.
floatoperator [](index:int)🔗
Returns thefloatat indexindex. Negative indices can be used to access the elements starting from the end. Using index out of array's bounds will result in an error.
Note thatfloattype is 64-bit, unlike the values stored in the array.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
