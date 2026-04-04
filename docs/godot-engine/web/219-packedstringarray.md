# PackedStringArray

# PackedStringArray
A packed array ofStrings.

## Description
An array specifically designed to holdStrings. Packs data tightly, so it saves memory for large array sizes.
If you want to join the strings in the array, useString.join().
```
var string_array = PackedStringArray(["hello", "world"])
var string = " ".join(string_array)
print(string) # "hello world"
```
Differences between packed arrays, typed arrays, and untyped arrays:Packed arrays are generally faster to iterate on and modify compared to a typed array of the same type (e.g.PackedStringArrayversusArray[String]). Also, packed arrays consume less memory. As a downside, packed arrays are less flexible as they don't offer as many convenience methods such asArray.map(). Typed arrays are in turn faster to iterate on and modify than untyped arrays.
Note:Packed arrays are always passed by reference. To get a copy of an array that can be modified independently of the original array, useduplicate(). This isnotthe case for built-in properties and methods. In these cases the returned packed array is a copy, and changing it willnotaffect the original value. To update a built-in property of this type, modify the returned array and then assign it to the property again.
Note
There are notable differences when using this API with C#. SeeC# API differences to GDScriptfor more information.

## Tutorials
- Operating System Testing Demo
Operating System Testing Demo

## Constructors

| PackedStringArray | PackedStringArray() |
|---|---|
| PackedStringArray | PackedStringArray(from:PackedStringArray) |
| PackedStringArray | PackedStringArray(from:Array) |

PackedStringArray
PackedStringArray()
PackedStringArray
PackedStringArray(from:PackedStringArray)
PackedStringArray
PackedStringArray(from:Array)

## Methods

| bool | append(value:String) |
|---|---|
| void | append_array(array:PackedStringArray) |
| int | bsearch(value:String, before:bool= true)const |
| void | clear() |
| int | count(value:String)const |
| PackedStringArray | duplicate()const |
| bool | erase(value:String) |
| void | fill(value:String) |
| int | find(value:String, from:int= 0)const |
| String | get(index:int)const |
| bool | has(value:String)const |
| int | insert(at_index:int, value:String) |
| bool | is_empty()const |
| bool | push_back(value:String) |
| void | remove_at(index:int) |
| int | resize(new_size:int) |
| void | reverse() |
| int | rfind(value:String, from:int= -1)const |
| void | set(index:int, value:String) |
| int | size()const |
| PackedStringArray | slice(begin:int, end:int= 2147483647)const |
| void | sort() |
| PackedByteArray | to_byte_array()const |

bool
append(value:String)
void
append_array(array:PackedStringArray)
bsearch(value:String, before:bool= true)const
void
clear()
count(value:String)const
PackedStringArray
duplicate()const
bool
erase(value:String)
void
fill(value:String)
find(value:String, from:int= 0)const
String
get(index:int)const
bool
has(value:String)const
insert(at_index:int, value:String)
bool
is_empty()const
bool
push_back(value:String)
void
remove_at(index:int)
resize(new_size:int)
void
reverse()
rfind(value:String, from:int= -1)const
void
set(index:int, value:String)
size()const
PackedStringArray
slice(begin:int, end:int= 2147483647)const
void
sort()
PackedByteArray
to_byte_array()const

## Operators

| bool | operator !=(right:PackedStringArray) |
|---|---|
| PackedStringArray | operator +(right:PackedStringArray) |
| bool | operator ==(right:PackedStringArray) |
| String | operator [](index:int) |

bool
operator !=(right:PackedStringArray)
PackedStringArray
operator +(right:PackedStringArray)
bool
operator ==(right:PackedStringArray)
String
operator [](index:int)

## Constructor Descriptions
PackedStringArrayPackedStringArray()🔗
Constructs an emptyPackedStringArray.
PackedStringArrayPackedStringArray(from:PackedStringArray)
Constructs aPackedStringArrayas a copy of the givenPackedStringArray.
PackedStringArrayPackedStringArray(from:Array)
Constructs a newPackedStringArray. Optionally, you can pass in a genericArraythat will be converted.

## Method Descriptions
boolappend(value:String)🔗
Appends an element at the end of the array (alias ofpush_back()).
voidappend_array(array:PackedStringArray)🔗
Appends aPackedStringArrayat the end of this array.
intbsearch(value:String, before:bool= true)const🔗
Finds the index of an existing value (or the insertion index that maintains sorting order, if the value is not yet present in the array) using binary search. Optionally, abeforespecifier can be passed. Iffalse, the returned index comes after all existing entries of the value in the array.
Note:Callingbsearch()on an unsorted array results in unexpected behavior.
voidclear()🔗
Clears the array. This is equivalent to usingresize()with a size of0.
intcount(value:String)const🔗
Returns the number of times an element is in the array.
PackedStringArrayduplicate()const🔗
Creates a copy of the array, and returns it.
boolerase(value:String)🔗
Removes the first occurrence of a value from the array and returnstrue. If the value does not exist in the array, nothing happens andfalseis returned. To remove an element by index, useremove_at()instead.
voidfill(value:String)🔗
Assigns the given value to all elements in the array. This can typically be used together withresize()to create an array with a given size and initialized elements.
intfind(value:String, from:int= 0)const🔗
Searches the array for a value and returns its index or-1if not found. Optionally, the initial search index can be passed.
Stringget(index:int)const🔗
Returns theStringat the givenindexin the array. Ifindexis out-of-bounds or negative, this method fails and returns an empty string.
This method is similar (but not identical) to the[]operator. Most notably, when this method fails, it doesn't pause project execution if run from the editor.
boolhas(value:String)const🔗
Returnstrueif the array containsvalue.
intinsert(at_index:int, value:String)🔗
Inserts a new element at a given position in the array. The position must be valid, or at the end of the array (idx==size()).
boolis_empty()const🔗
Returnstrueif the array is empty.
boolpush_back(value:String)🔗
Appends a string element at end of the array.
voidremove_at(index:int)🔗
Removes an element from the array by index.
intresize(new_size:int)🔗
Sets the size of the array. If the array is grown, reserves elements at the end of the array. If the array is shrunk, truncates the array to the new size. Callingresize()once and assigning the new values is faster than adding new elements one by one.
Returns@GlobalScope.OKon success, or one of the followingErrorconstants if this method fails:@GlobalScope.ERR_INVALID_PARAMETERif the size is negative, or@GlobalScope.ERR_OUT_OF_MEMORYif allocations fail. Usesize()to find the actual size of the array after resize.
voidreverse()🔗
Reverses the order of the elements in the array.
intrfind(value:String, from:int= -1)const🔗
Searches the array in reverse order. Optionally, a start search index can be passed. If negative, the start index is considered relative to the end of the array.
voidset(index:int, value:String)🔗
Changes theStringat the given index.
intsize()const🔗
Returns the number of elements in the array.
PackedStringArrayslice(begin:int, end:int= 2147483647)const🔗
Returns the slice of thePackedStringArray, frombegin(inclusive) toend(exclusive), as a newPackedStringArray.
The absolute value ofbeginandendwill be clamped to the array size, so the default value forendmakes it slice to the size of the array by default (i.e.arr.slice(1)is a shorthand forarr.slice(1,arr.size())).
If eitherbeginorendare negative, they will be relative to the end of the array (i.e.arr.slice(0,-2)is a shorthand forarr.slice(0,arr.size()-2)).
voidsort()🔗
Sorts the elements of the array in ascending order.
PackedByteArrayto_byte_array()const🔗
Returns aPackedByteArraywith each string encoded as UTF-8. Strings arenullterminated.

## Operator Descriptions
booloperator !=(right:PackedStringArray)🔗
Returnstrueif contents of the arrays differ.
PackedStringArrayoperator +(right:PackedStringArray)🔗
Returns a newPackedStringArraywith contents ofrightadded at the end of this array. For better performance, consider usingappend_array()instead.
booloperator ==(right:PackedStringArray)🔗
Returnstrueif contents of both arrays are the same, i.e. they have all equalStrings at the corresponding indices.
Stringoperator [](index:int)🔗
Returns theStringat indexindex. Negative indices can be used to access the elements starting from the end. Using index out of array's bounds will result in an error.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.