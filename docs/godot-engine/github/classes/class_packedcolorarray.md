:github_url: hide



# PackedColorArray

A packed array of [Color<class_Color>]\ s.


## Description

An array specifically designed to hold [Color<class_Color>]. Packs data tightly, so it saves memory for large array sizes.

\ **Differences between packed arrays, typed arrays, and untyped arrays:** Packed arrays are generally faster to iterate on and modify compared to a typed array of the same type (e.g. **PackedColorArray** versus `Array[Color]`). Also, packed arrays consume less memory. As a downside, packed arrays are less flexible as they don't offer as many convenience methods such as [Array.map()<class_Array_method_map>]. Typed arrays are in turn faster to iterate on and modify than untyped arrays.

\ **Note:** Packed arrays are always passed by reference. To get a copy of an array that can be modified independently of the original array, use [duplicate()<class_PackedColorArray_method_duplicate>]. This is *not* the case for built-in properties and methods. In these cases the returned packed array is a copy, and changing it will *not* affect the original value. To update a built-in property of this type, modify the returned array and then assign it to the property again.

> **NOTE**
>
	There are notable differences when using this API with C#. See [doc_c_sharp_differences] for more information.


## Constructors

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedColorArray<class_PackedColorArray>` | :ref:`PackedColorArray<class_PackedColorArray_constructor_PackedColorArray>`\ (\ )                                                         |
> +-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedColorArray<class_PackedColorArray>` | :ref:`PackedColorArray<class_PackedColorArray_constructor_PackedColorArray>`\ (\ from\: :ref:`PackedColorArray<class_PackedColorArray>`\ ) |
> +-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedColorArray<class_PackedColorArray>` | :ref:`PackedColorArray<class_PackedColorArray_constructor_PackedColorArray>`\ (\ from\: :ref:`Array<class_Array>`\ )                       |
> +-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                         | :ref:`append<class_PackedColorArray_method_append>`\ (\ value\: :ref:`Color<class_Color>`\ )                                                    |
> +-------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                          | :ref:`append_array<class_PackedColorArray_method_append_array>`\ (\ array\: :ref:`PackedColorArray<class_PackedColorArray>`\ )                  |
> +-------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                           | :ref:`bsearch<class_PackedColorArray_method_bsearch>`\ (\ value\: :ref:`Color<class_Color>`, before\: :ref:`bool<class_bool>` = true\ ) |const| |
> +-------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                          | :ref:`clear<class_PackedColorArray_method_clear>`\ (\ )                                                                                         |
> +-------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                           | :ref:`count<class_PackedColorArray_method_count>`\ (\ value\: :ref:`Color<class_Color>`\ ) |const|                                              |
> +-------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedColorArray<class_PackedColorArray>` | :ref:`duplicate<class_PackedColorArray_method_duplicate>`\ (\ ) |const|                                                                         |
> +-------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                         | :ref:`erase<class_PackedColorArray_method_erase>`\ (\ value\: :ref:`Color<class_Color>`\ )                                                      |
> +-------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                          | :ref:`fill<class_PackedColorArray_method_fill>`\ (\ value\: :ref:`Color<class_Color>`\ )                                                        |
> +-------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                           | :ref:`find<class_PackedColorArray_method_find>`\ (\ value\: :ref:`Color<class_Color>`, from\: :ref:`int<class_int>` = 0\ ) |const|              |
> +-------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Color<class_Color>`                       | :ref:`get<class_PackedColorArray_method_get>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                      |
> +-------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                         | :ref:`has<class_PackedColorArray_method_has>`\ (\ value\: :ref:`Color<class_Color>`\ ) |const|                                                  |
> +-------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                           | :ref:`insert<class_PackedColorArray_method_insert>`\ (\ at_index\: :ref:`int<class_int>`, value\: :ref:`Color<class_Color>`\ )                  |
> +-------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                         | :ref:`is_empty<class_PackedColorArray_method_is_empty>`\ (\ ) |const|                                                                           |
> +-------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                         | :ref:`push_back<class_PackedColorArray_method_push_back>`\ (\ value\: :ref:`Color<class_Color>`\ )                                              |
> +-------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                          | :ref:`remove_at<class_PackedColorArray_method_remove_at>`\ (\ index\: :ref:`int<class_int>`\ )                                                  |
> +-------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                           | :ref:`resize<class_PackedColorArray_method_resize>`\ (\ new_size\: :ref:`int<class_int>`\ )                                                     |
> +-------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                          | :ref:`reverse<class_PackedColorArray_method_reverse>`\ (\ )                                                                                     |
> +-------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                           | :ref:`rfind<class_PackedColorArray_method_rfind>`\ (\ value\: :ref:`Color<class_Color>`, from\: :ref:`int<class_int>` = -1\ ) |const|           |
> +-------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                          | :ref:`set<class_PackedColorArray_method_set>`\ (\ index\: :ref:`int<class_int>`, value\: :ref:`Color<class_Color>`\ )                           |
> +-------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                           | :ref:`size<class_PackedColorArray_method_size>`\ (\ ) |const|                                                                                   |
> +-------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedColorArray<class_PackedColorArray>` | :ref:`slice<class_PackedColorArray_method_slice>`\ (\ begin\: :ref:`int<class_int>`, end\: :ref:`int<class_int>` = 2147483647\ ) |const|        |
> +-------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                          | :ref:`sort<class_PackedColorArray_method_sort>`\ (\ )                                                                                           |
> +-------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedByteArray<class_PackedByteArray>`   | :ref:`to_byte_array<class_PackedColorArray_method_to_byte_array>`\ (\ ) |const|                                                                 |
> +-------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
>

## Operators

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                         | :ref:`operator !=<class_PackedColorArray_operator_neq_PackedColorArray>`\ (\ right\: :ref:`PackedColorArray<class_PackedColorArray>`\ ) |
> +-------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedColorArray<class_PackedColorArray>` | :ref:`operator +<class_PackedColorArray_operator_sum_PackedColorArray>`\ (\ right\: :ref:`PackedColorArray<class_PackedColorArray>`\ )  |
> +-------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                         | :ref:`operator ==<class_PackedColorArray_operator_eq_PackedColorArray>`\ (\ right\: :ref:`PackedColorArray<class_PackedColorArray>`\ )  |
> +-------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Color<class_Color>`                       | :ref:`operator []<class_PackedColorArray_operator_idx_int>`\ (\ index\: :ref:`int<class_int>`\ )                                        |
> +-------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Constructor Descriptions



[PackedColorArray<class_PackedColorArray>] **PackedColorArray**\ (\ ) [🔗<class_PackedColorArray_constructor_PackedColorArray>]

Constructs an empty **PackedColorArray**.


----


[PackedColorArray<class_PackedColorArray>] **PackedColorArray**\ (\ from\: [PackedColorArray<class_PackedColorArray>]\ )

Constructs a **PackedColorArray** as a copy of the given **PackedColorArray**.


----


[PackedColorArray<class_PackedColorArray>] **PackedColorArray**\ (\ from\: [Array<class_Array>]\ )

Constructs a new **PackedColorArray**. Optionally, you can pass in a generic [Array<class_Array>] that will be converted.

\ **Note:** When initializing a **PackedColorArray** with elements, it must be initialized with an [Array<class_Array>] of [Color<class_Color>] values:

::

    var array = PackedColorArray([Color(0.1, 0.2, 0.3), Color(0.4, 0.5, 0.6)])


----


## Method Descriptions



[bool<class_bool>] **append**\ (\ value\: [Color<class_Color>]\ ) [🔗<class_PackedColorArray_method_append>]

Appends an element at the end of the array (alias of [push_back()<class_PackedColorArray_method_push_back>]).


----



|void| **append_array**\ (\ array\: [PackedColorArray<class_PackedColorArray>]\ ) [🔗<class_PackedColorArray_method_append_array>]

Appends a **PackedColorArray** at the end of this array.


----



[int<class_int>] **bsearch**\ (\ value\: [Color<class_Color>], before\: [bool<class_bool>] = true\ ) |const| [🔗<class_PackedColorArray_method_bsearch>]

Finds the index of an existing value (or the insertion index that maintains sorting order, if the value is not yet present in the array) using binary search. Optionally, a `before` specifier can be passed. If `false`, the returned index comes after all existing entries of the value in the array.

\ **Note:** Calling [bsearch()<class_PackedColorArray_method_bsearch>] on an unsorted array results in unexpected behavior.


----



|void| **clear**\ (\ ) [🔗<class_PackedColorArray_method_clear>]

Clears the array. This is equivalent to using [resize()<class_PackedColorArray_method_resize>] with a size of `0`.


----



[int<class_int>] **count**\ (\ value\: [Color<class_Color>]\ ) |const| [🔗<class_PackedColorArray_method_count>]

Returns the number of times an element is in the array.


----



[PackedColorArray<class_PackedColorArray>] **duplicate**\ (\ ) |const| [🔗<class_PackedColorArray_method_duplicate>]

Creates a copy of the array, and returns it.


----



[bool<class_bool>] **erase**\ (\ value\: [Color<class_Color>]\ ) [🔗<class_PackedColorArray_method_erase>]

Removes the first occurrence of a value from the array and returns `true`. If the value does not exist in the array, nothing happens and `false` is returned. To remove an element by index, use [remove_at()<class_PackedColorArray_method_remove_at>] instead.


----



|void| **fill**\ (\ value\: [Color<class_Color>]\ ) [🔗<class_PackedColorArray_method_fill>]

Assigns the given value to all elements in the array. This can typically be used together with [resize()<class_PackedColorArray_method_resize>] to create an array with a given size and initialized elements.


----



[int<class_int>] **find**\ (\ value\: [Color<class_Color>], from\: [int<class_int>] = 0\ ) |const| [🔗<class_PackedColorArray_method_find>]

Searches the array for a value and returns its index or `-1` if not found. Optionally, the initial search index can be passed.


----



[Color<class_Color>] **get**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_PackedColorArray_method_get>]

Returns the [Color<class_Color>] at the given `index` in the array. If `index` is out-of-bounds or negative, this method fails and returns `Color(0, 0, 0, 1)`.

This method is similar (but not identical) to the `[]` operator. Most notably, when this method fails, it doesn't pause project execution if run from the editor.


----



[bool<class_bool>] **has**\ (\ value\: [Color<class_Color>]\ ) |const| [🔗<class_PackedColorArray_method_has>]

Returns `true` if the array contains `value`.


----



[int<class_int>] **insert**\ (\ at_index\: [int<class_int>], value\: [Color<class_Color>]\ ) [🔗<class_PackedColorArray_method_insert>]

Inserts a new element at a given position in the array. The position must be valid, or at the end of the array (`idx == size()`).


----



[bool<class_bool>] **is_empty**\ (\ ) |const| [🔗<class_PackedColorArray_method_is_empty>]

Returns `true` if the array is empty.


----



[bool<class_bool>] **push_back**\ (\ value\: [Color<class_Color>]\ ) [🔗<class_PackedColorArray_method_push_back>]

Appends a value to the array.


----



|void| **remove_at**\ (\ index\: [int<class_int>]\ ) [🔗<class_PackedColorArray_method_remove_at>]

Removes an element from the array by index.


----



[int<class_int>] **resize**\ (\ new_size\: [int<class_int>]\ ) [🔗<class_PackedColorArray_method_resize>]

Sets the size of the array. If the array is grown, reserves elements at the end of the array. If the array is shrunk, truncates the array to the new size. Calling [resize()<class_PackedColorArray_method_resize>] once and assigning the new values is faster than adding new elements one by one.

Returns [@GlobalScope.OK<class_@GlobalScope_constant_OK>] on success, or one of the following [Error<enum_@GlobalScope_Error>] constants if this method fails: [@GlobalScope.ERR_INVALID_PARAMETER<class_@GlobalScope_constant_ERR_INVALID_PARAMETER>] if the size is negative, or [@GlobalScope.ERR_OUT_OF_MEMORY<class_@GlobalScope_constant_ERR_OUT_OF_MEMORY>] if allocations fail. Use [size()<class_PackedColorArray_method_size>] to find the actual size of the array after resize.


----



|void| **reverse**\ (\ ) [🔗<class_PackedColorArray_method_reverse>]

Reverses the order of the elements in the array.


----



[int<class_int>] **rfind**\ (\ value\: [Color<class_Color>], from\: [int<class_int>] = -1\ ) |const| [🔗<class_PackedColorArray_method_rfind>]

Searches the array in reverse order. Optionally, a start search index can be passed. If negative, the start index is considered relative to the end of the array.


----



|void| **set**\ (\ index\: [int<class_int>], value\: [Color<class_Color>]\ ) [🔗<class_PackedColorArray_method_set>]

Changes the [Color<class_Color>] at the given index.


----



[int<class_int>] **size**\ (\ ) |const| [🔗<class_PackedColorArray_method_size>]

Returns the number of elements in the array.


----



[PackedColorArray<class_PackedColorArray>] **slice**\ (\ begin\: [int<class_int>], end\: [int<class_int>] = 2147483647\ ) |const| [🔗<class_PackedColorArray_method_slice>]

Returns the slice of the **PackedColorArray**, from `begin` (inclusive) to `end` (exclusive), as a new **PackedColorArray**.

The absolute value of `begin` and `end` will be clamped to the array size, so the default value for `end` makes it slice to the size of the array by default (i.e. `arr.slice(1)` is a shorthand for `arr.slice(1, arr.size())`).

If either `begin` or `end` are negative, they will be relative to the end of the array (i.e. `arr.slice(0, -2)` is a shorthand for `arr.slice(0, arr.size() - 2)`).


----



|void| **sort**\ (\ ) [🔗<class_PackedColorArray_method_sort>]

Sorts the elements of the array in ascending order.


----



[PackedByteArray<class_PackedByteArray>] **to_byte_array**\ (\ ) |const| [🔗<class_PackedColorArray_method_to_byte_array>]

Returns a [PackedByteArray<class_PackedByteArray>] with each color encoded as bytes.


----


## Operator Descriptions



[bool<class_bool>] **operator !=**\ (\ right\: [PackedColorArray<class_PackedColorArray>]\ ) [🔗<class_PackedColorArray_operator_neq_PackedColorArray>]

Returns `true` if contents of the arrays differ.


----



[PackedColorArray<class_PackedColorArray>] **operator +**\ (\ right\: [PackedColorArray<class_PackedColorArray>]\ ) [🔗<class_PackedColorArray_operator_sum_PackedColorArray>]

Returns a new **PackedColorArray** with contents of `right` added at the end of this array. For better performance, consider using [append_array()<class_PackedColorArray_method_append_array>] instead.


----



[bool<class_bool>] **operator ==**\ (\ right\: [PackedColorArray<class_PackedColorArray>]\ ) [🔗<class_PackedColorArray_operator_eq_PackedColorArray>]

Returns `true` if contents of both arrays are the same, i.e. they have all equal [Color<class_Color>]\ s at the corresponding indices.


----



[Color<class_Color>] **operator []**\ (\ index\: [int<class_int>]\ ) [🔗<class_PackedColorArray_operator_idx_int>]

Returns the [Color<class_Color>] at index `index`. Negative indices can be used to access the elements starting from the end. Using index out of array's bounds will result in an error.

