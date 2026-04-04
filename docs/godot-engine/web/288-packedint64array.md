# PackedInt64Array

# PackedInt64Array
A packed array of 64-bit integers.

## Description
An array specifically designed to hold 64-bit integer values. Packs data tightly, so it saves memory for large array sizes.
Note:This type stores signed 64-bit integers, which means it can take values in the interval[-2^63,2^63-1], i.e.[-9223372036854775808,9223372036854775807]. Exceeding those bounds will wrap around. If you only need to pack 32-bit integers tightly, seePackedInt32Arrayfor a more memory-friendly alternative.
Differences between packed arrays, typed arrays, and untyped arrays:Packed arrays are generally faster to iterate on and modify compared to a typed array of the same type (e.g.PackedInt64ArrayversusArray[int]). Also, packed arrays consume less memory. As a downside, packed arrays are less flexible as they don't offer as many convenience methods such asArray.map(). Typed arrays are in turn faster to iterate on and modify than untyped arrays.
Note:Packed arrays are always passed by reference. To get a copy of an array that can be modified independently of the original array, useduplicate(). This isnotthe case for built-in properties and methods. In these cases the returned packed array is a copy, and changing it willnotaffect the original value. To update a built-in property of this type, modify the returned array and then assign it to the property again.
Note
There are notable differences when using this API with C#. SeeC# API differences to GDScriptfor more information.

## Constructors

| PackedInt64Array | PackedInt64Array() |
|---|---|
| PackedInt64Array | PackedInt64Array(from:PackedInt64Array) |
| PackedInt64Array | PackedInt64Array(from:Array) |

PackedInt64Array
PackedInt64Array()
PackedInt64Array
PackedInt64Array(from:PackedInt64Array)
PackedInt64Array
PackedInt64Array(from:Array)

## Methods

| bool | append(value:int) |
|---|---|
| void | append_array(array:PackedInt64Array) |
| int | bsearch(value:int, before:bool= true)const |
| void | clear() |
| int | count(value:int)const |
| PackedInt64Array | duplicate()const |
| bool | erase(value:int) |
| void | fill(value:int) |
| int | find(value:int, from:int= 0)const |
| int | get(index:int)const |
| bool | has(value:int)const |
| int | insert(at_index:int, value:int) |
| bool | is_empty()const |
| bool | push_back(value:int) |
| void | remove_at(index:int) |
| int | resize(new_size:int) |
| void | reverse() |
| int | rfind(value:int, from:int= -1)const |
| void | set(index:int, value:int) |
| int | size()const |
| PackedInt64Array | slice(begin:int, end:int= 2147483647)const |
| void | sort() |
| PackedByteArray | to_byte_array()const |

bool
append(value:int)
void
append_array(array:PackedInt64Array)
bsearch(value:int, before:bool= true)const
void
clear()
count(value:int)const
PackedInt64Array
duplicate()const
bool
erase(value:int)
void
fill(value:int)
find(value:int, from:int= 0)const
get(index:int)const
bool
has(value:int)const
insert(at_index:int, value:int)
bool
is_empty()const
bool
push_back(value:int)
void
remove_at(index:int)
resize(new_size:int)
void
reverse()
rfind(value:int, from:int= -1)const
void
set(index:int, value:int)
size()const
PackedInt64Array
slice(begin:int, end:int= 2147483647)const
void
sort()
PackedByteArray
to_byte_array()const

## Operators

| bool | operator !=(right:PackedInt64Array) |
|---|---|
| PackedInt64Array | operator +(right:PackedInt64Array) |
| bool | operator ==(right:PackedInt64Array) |
| int | operator [](index:int) |

bool
operator !=(right:PackedInt64Array)
PackedInt64Array
operator +(right:PackedInt64Array)
bool
operator ==(right:PackedInt64Array)
operator [](index:int)

## Constructor Descriptions
PackedInt64ArrayPackedInt64Array()🔗
Constructs an emptyPackedInt64Array.
PackedInt64ArrayPackedInt64Array(from:PackedInt64Array)
Constructs aPackedInt64Arrayas a copy of the givenPackedInt64Array.
PackedInt64ArrayPackedInt64Array(from:Array)
Constructs a newPackedInt64Array. Optionally, you can pass in a genericArraythat will be converted.

## Method Descriptions
boolappend(value:int)🔗
Appends an element at the end of the array (alias ofpush_back()).
voidappend_array(array:PackedInt64Array)🔗
Appends aPackedInt64Arrayat the end of this array.
intbsearch(value:int, before:bool= true)const🔗
Finds the index of an existing value (or the insertion index that maintains sorting order, if the value is not yet present in the array) using binary search. Optionally, abeforespecifier can be passed. Iffalse, the returned index comes after all existing entries of the value in the array.
Note:Callingbsearch()on an unsorted array results in unexpected behavior.
voidclear()🔗
Clears the array. This is equivalent to usingresize()with a size of0.
intcount(value:int)const🔗
Returns the number of times an element is in the array.
PackedInt64Arrayduplicate()const🔗
Creates a copy of the array, and returns it.
boolerase(value:int)🔗
Removes the first occurrence of a value from the array and returnstrue. If the value does not exist in the array, nothing happens andfalseis returned. To remove an element by index, useremove_at()instead.
voidfill(value:int)🔗
Assigns the given value to all elements in the array. This can typically be used together withresize()to create an array with a given size and initialized elements.
intfind(value:int, from:int= 0)const🔗
Searches the array for a value and returns its index or-1if not found. Optionally, the initial search index can be passed.
intget(index:int)const🔗
Returns the 64-bit integer at the givenindexin the array. Ifindexis out-of-bounds or negative, this method fails and returns0.
This method is similar (but not identical) to the[]operator. Most notably, when this method fails, it doesn't pause project execution if run from the editor.
boolhas(value:int)const🔗
Returnstrueif the array containsvalue.
intinsert(at_index:int, value:int)🔗
Inserts a new integer at a given position in the array. The position must be valid, or at the end of the array (idx==size()).
boolis_empty()const🔗
Returnstrueif the array is empty.
boolpush_back(value:int)🔗
Appends a value to the array.
voidremove_at(index:int)🔗
Removes an element from the array by index.
intresize(new_size:int)🔗
Sets the size of the array. If the array is grown, reserves elements at the end of the array. If the array is shrunk, truncates the array to the new size. Callingresize()once and assigning the new values is faster than adding new elements one by one.
Returns@GlobalScope.OKon success, or one of the followingErrorconstants if this method fails:@GlobalScope.ERR_INVALID_PARAMETERif the size is negative, or@GlobalScope.ERR_OUT_OF_MEMORYif allocations fail. Usesize()to find the actual size of the array after resize.
voidreverse()🔗
Reverses the order of the elements in the array.
intrfind(value:int, from:int= -1)const🔗
Searches the array in reverse order. Optionally, a start search index can be passed. If negative, the start index is considered relative to the end of the array.
voidset(index:int, value:int)🔗
Changes the integer at the given index.
intsize()const🔗
Returns the number of elements in the array.
PackedInt64Arrayslice(begin:int, end:int= 2147483647)const🔗
Returns the slice of thePackedInt64Array, frombegin(inclusive) toend(exclusive), as a newPackedInt64Array.
The absolute value ofbeginandendwill be clamped to the array size, so the default value forendmakes it slice to the size of the array by default (i.e.arr.slice(1)is a shorthand forarr.slice(1,arr.size())).
If eitherbeginorendare negative, they will be relative to the end of the array (i.e.arr.slice(0,-2)is a shorthand forarr.slice(0,arr.size()-2)).
voidsort()🔗
Sorts the elements of the array in ascending order.
PackedByteArrayto_byte_array()const🔗
Returns a copy of the data converted to aPackedByteArray, where each element has been encoded as 8 bytes.
The size of the new array will beint64_array.size()*8.

## Operator Descriptions
booloperator !=(right:PackedInt64Array)🔗
Returnstrueif contents of the arrays differ.
PackedInt64Arrayoperator +(right:PackedInt64Array)🔗
Returns a newPackedInt64Arraywith contents ofrightadded at the end of this array. For better performance, consider usingappend_array()instead.
booloperator ==(right:PackedInt64Array)🔗
Returnstrueif contents of both arrays are the same, i.e. they have all equal ints at the corresponding indices.
intoperator [](index:int)🔗
Returns theintat indexindex. Negative indices can be used to access the elements starting from the end. Using index out of array's bounds will result in an error.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.