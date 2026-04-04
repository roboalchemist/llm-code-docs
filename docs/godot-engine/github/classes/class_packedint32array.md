:github_url: hide



# PackedInt32Array

A packed array of 32-bit integers.


## Description

An array specifically designed to hold 32-bit integer values. Packs data tightly, so it saves memory for large array sizes.

\ **Note:** This type stores signed 32-bit integers, which means it can take values in the interval `[-2^31, 2^31 - 1]`, i.e. `[-2147483648, 2147483647]`. Exceeding those bounds will wrap around. In comparison, [int<class_int>] uses signed 64-bit integers which can hold much larger values. If you need to pack 64-bit integers tightly, see [PackedInt64Array<class_PackedInt64Array>].

\ **Note:** Packed arrays are always passed by reference. To get a copy of an array that can be modified independently of the original array, use [duplicate()<class_PackedInt32Array_method_duplicate>]. This is *not* the case for built-in properties and methods. In these cases the returned packed array is a copy, and changing it will *not* affect the original value. To update a built-in property of this type, modify the returned array and then assign it to the property again.

> **NOTE**
>
	There are notable differences when using this API with C#. See [doc_c_sharp_differences] for more information.


## Constructors

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedInt32Array<class_PackedInt32Array>` | :ref:`PackedInt32Array<class_PackedInt32Array_constructor_PackedInt32Array>`\ (\ )                                                         |
> +-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedInt32Array<class_PackedInt32Array>` | :ref:`PackedInt32Array<class_PackedInt32Array_constructor_PackedInt32Array>`\ (\ from\: :ref:`PackedInt32Array<class_PackedInt32Array>`\ ) |
> +-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedInt32Array<class_PackedInt32Array>` | :ref:`PackedInt32Array<class_PackedInt32Array_constructor_PackedInt32Array>`\ (\ from\: :ref:`Array<class_Array>`\ )                       |
> +-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                         | :ref:`append<class_PackedInt32Array_method_append>`\ (\ value\: :ref:`int<class_int>`\ )                                                    |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                          | :ref:`append_array<class_PackedInt32Array_method_append_array>`\ (\ array\: :ref:`PackedInt32Array<class_PackedInt32Array>`\ )              |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                           | :ref:`bsearch<class_PackedInt32Array_method_bsearch>`\ (\ value\: :ref:`int<class_int>`, before\: :ref:`bool<class_bool>` = true\ ) |const| |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                          | :ref:`clear<class_PackedInt32Array_method_clear>`\ (\ )                                                                                     |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                           | :ref:`count<class_PackedInt32Array_method_count>`\ (\ value\: :ref:`int<class_int>`\ ) |const|                                              |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedInt32Array<class_PackedInt32Array>` | :ref:`duplicate<class_PackedInt32Array_method_duplicate>`\ (\ ) |const|                                                                     |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                         | :ref:`erase<class_PackedInt32Array_method_erase>`\ (\ value\: :ref:`int<class_int>`\ )                                                      |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                          | :ref:`fill<class_PackedInt32Array_method_fill>`\ (\ value\: :ref:`int<class_int>`\ )                                                        |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                           | :ref:`find<class_PackedInt32Array_method_find>`\ (\ value\: :ref:`int<class_int>`, from\: :ref:`int<class_int>` = 0\ ) |const|              |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                           | :ref:`get<class_PackedInt32Array_method_get>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                  |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                         | :ref:`has<class_PackedInt32Array_method_has>`\ (\ value\: :ref:`int<class_int>`\ ) |const|                                                  |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                           | :ref:`insert<class_PackedInt32Array_method_insert>`\ (\ at_index\: :ref:`int<class_int>`, value\: :ref:`int<class_int>`\ )                  |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                         | :ref:`is_empty<class_PackedInt32Array_method_is_empty>`\ (\ ) |const|                                                                       |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                         | :ref:`push_back<class_PackedInt32Array_method_push_back>`\ (\ value\: :ref:`int<class_int>`\ )                                              |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                          | :ref:`remove_at<class_PackedInt32Array_method_remove_at>`\ (\ index\: :ref:`int<class_int>`\ )                                              |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                           | :ref:`resize<class_PackedInt32Array_method_resize>`\ (\ new_size\: :ref:`int<class_int>`\ )                                                 |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                          | :ref:`reverse<class_PackedInt32Array_method_reverse>`\ (\ )                                                                                 |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                           | :ref:`rfind<class_PackedInt32Array_method_rfind>`\ (\ value\: :ref:`int<class_int>`, from\: :ref:`int<class_int>` = -1\ ) |const|           |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                          | :ref:`set<class_PackedInt32Array_method_set>`\ (\ index\: :ref:`int<class_int>`, value\: :ref:`int<class_int>`\ )                           |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                           | :ref:`size<class_PackedInt32Array_method_size>`\ (\ ) |const|                                                                               |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedInt32Array<class_PackedInt32Array>` | :ref:`slice<class_PackedInt32Array_method_slice>`\ (\ begin\: :ref:`int<class_int>`, end\: :ref:`int<class_int>` = 2147483647\ ) |const|    |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                          | :ref:`sort<class_PackedInt32Array_method_sort>`\ (\ )                                                                                       |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedByteArray<class_PackedByteArray>`   | :ref:`to_byte_array<class_PackedInt32Array_method_to_byte_array>`\ (\ ) |const|                                                             |
> +-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
>

## Operators

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                         | :ref:`operator !=<class_PackedInt32Array_operator_neq_PackedInt32Array>`\ (\ right\: :ref:`PackedInt32Array<class_PackedInt32Array>`\ ) |
> +-------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedInt32Array<class_PackedInt32Array>` | :ref:`operator +<class_PackedInt32Array_operator_sum_PackedInt32Array>`\ (\ right\: :ref:`PackedInt32Array<class_PackedInt32Array>`\ )  |
> +-------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                         | :ref:`operator ==<class_PackedInt32Array_operator_eq_PackedInt32Array>`\ (\ right\: :ref:`PackedInt32Array<class_PackedInt32Array>`\ )  |
> +-------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                           | :ref:`operator []<class_PackedInt32Array_operator_idx_int>`\ (\ index\: :ref:`int<class_int>`\ )                                        |
> +-------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Constructor Descriptions



[PackedInt32Array<class_PackedInt32Array>] **PackedInt32Array**\ (\ ) [🔗<class_PackedInt32Array_constructor_PackedInt32Array>]

Constructs an empty **PackedInt32Array**.


----


[PackedInt32Array<class_PackedInt32Array>] **PackedInt32Array**\ (\ from\: [PackedInt32Array<class_PackedInt32Array>]\ )

Constructs a **PackedInt32Array** as a copy of the given **PackedInt32Array**.


----


[PackedInt32Array<class_PackedInt32Array>] **PackedInt32Array**\ (\ from\: [Array<class_Array>]\ )

Constructs a new **PackedInt32Array**. Optionally, you can pass in a generic [Array<class_Array>] that will be converted.


----


## Method Descriptions



[bool<class_bool>] **append**\ (\ value\: [int<class_int>]\ ) [🔗<class_PackedInt32Array_method_append>]

Appends an element at the end of the array (alias of [push_back()<class_PackedInt32Array_method_push_back>]).


----



|void| **append_array**\ (\ array\: [PackedInt32Array<class_PackedInt32Array>]\ ) [🔗<class_PackedInt32Array_method_append_array>]

Appends a **PackedInt32Array** at the end of this array.


----



[int<class_int>] **bsearch**\ (\ value\: [int<class_int>], before\: [bool<class_bool>] = true\ ) |const| [🔗<class_PackedInt32Array_method_bsearch>]

Finds the index of an existing value (or the insertion index that maintains sorting order, if the value is not yet present in the array) using binary search. Optionally, a `before` specifier can be passed. If `false`, the returned index comes after all existing entries of the value in the array.

\ **Note:** Calling [bsearch()<class_PackedInt32Array_method_bsearch>] on an unsorted array results in unexpected behavior.


----



|void| **clear**\ (\ ) [🔗<class_PackedInt32Array_method_clear>]

Clears the array. This is equivalent to using [resize()<class_PackedInt32Array_method_resize>] with a size of `0`.


----



[int<class_int>] **count**\ (\ value\: [int<class_int>]\ ) |const| [🔗<class_PackedInt32Array_method_count>]

Returns the number of times an element is in the array.


----



[PackedInt32Array<class_PackedInt32Array>] **duplicate**\ (\ ) |const| [🔗<class_PackedInt32Array_method_duplicate>]

Creates a copy of the array, and returns it.


----



[bool<class_bool>] **erase**\ (\ value\: [int<class_int>]\ ) [🔗<class_PackedInt32Array_method_erase>]

Removes the first occurrence of a value from the array and returns `true`. If the value does not exist in the array, nothing happens and `false` is returned. To remove an element by index, use [remove_at()<class_PackedInt32Array_method_remove_at>] instead.


----



|void| **fill**\ (\ value\: [int<class_int>]\ ) [🔗<class_PackedInt32Array_method_fill>]

Assigns the given value to all elements in the array. This can typically be used together with [resize()<class_PackedInt32Array_method_resize>] to create an array with a given size and initialized elements.


----



[int<class_int>] **find**\ (\ value\: [int<class_int>], from\: [int<class_int>] = 0\ ) |const| [🔗<class_PackedInt32Array_method_find>]

Searches the array for a value and returns its index or `-1` if not found. Optionally, the initial search index can be passed.


----



[int<class_int>] **get**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_PackedInt32Array_method_get>]

Returns the 32-bit integer at the given `index` in the array. If `index` is out-of-bounds or negative, this method fails and returns `0`.

This method is similar (but not identical) to the `[]` operator. Most notably, when this method fails, it doesn't pause project execution if run from the editor.


----



[bool<class_bool>] **has**\ (\ value\: [int<class_int>]\ ) |const| [🔗<class_PackedInt32Array_method_has>]

Returns `true` if the array contains `value`.


----



[int<class_int>] **insert**\ (\ at_index\: [int<class_int>], value\: [int<class_int>]\ ) [🔗<class_PackedInt32Array_method_insert>]

Inserts a new integer at a given position in the array. The position must be valid, or at the end of the array (`idx == size()`).


----



[bool<class_bool>] **is_empty**\ (\ ) |const| [🔗<class_PackedInt32Array_method_is_empty>]

Returns `true` if the array is empty.


----



[bool<class_bool>] **push_back**\ (\ value\: [int<class_int>]\ ) [🔗<class_PackedInt32Array_method_push_back>]

Appends a value to the array.


----



|void| **remove_at**\ (\ index\: [int<class_int>]\ ) [🔗<class_PackedInt32Array_method_remove_at>]

Removes an element from the array by index.


----



[int<class_int>] **resize**\ (\ new_size\: [int<class_int>]\ ) [🔗<class_PackedInt32Array_method_resize>]

Sets the size of the array. If the array is grown, reserves elements at the end of the array. If the array is shrunk, truncates the array to the new size. Calling [resize()<class_PackedInt32Array_method_resize>] once and assigning the new values is faster than adding new elements one by one.

Returns [@GlobalScope.OK<class_@GlobalScope_constant_OK>] on success, or one of the following [Error<enum_@GlobalScope_Error>] constants if this method fails: [@GlobalScope.ERR_INVALID_PARAMETER<class_@GlobalScope_constant_ERR_INVALID_PARAMETER>] if the size is negative, or [@GlobalScope.ERR_OUT_OF_MEMORY<class_@GlobalScope_constant_ERR_OUT_OF_MEMORY>] if allocations fail. Use [size()<class_PackedInt32Array_method_size>] to find the actual size of the array after resize.


----



|void| **reverse**\ (\ ) [🔗<class_PackedInt32Array_method_reverse>]

Reverses the order of the elements in the array.


----



[int<class_int>] **rfind**\ (\ value\: [int<class_int>], from\: [int<class_int>] = -1\ ) |const| [🔗<class_PackedInt32Array_method_rfind>]

Searches the array in reverse order. Optionally, a start search index can be passed. If negative, the start index is considered relative to the end of the array.


----



|void| **set**\ (\ index\: [int<class_int>], value\: [int<class_int>]\ ) [🔗<class_PackedInt32Array_method_set>]

Changes the integer at the given index.


----



[int<class_int>] **size**\ (\ ) |const| [🔗<class_PackedInt32Array_method_size>]

Returns the number of elements in the array.


----



[PackedInt32Array<class_PackedInt32Array>] **slice**\ (\ begin\: [int<class_int>], end\: [int<class_int>] = 2147483647\ ) |const| [🔗<class_PackedInt32Array_method_slice>]

Returns the slice of the **PackedInt32Array**, from `begin` (inclusive) to `end` (exclusive), as a new **PackedInt32Array**.

The absolute value of `begin` and `end` will be clamped to the array size, so the default value for `end` makes it slice to the size of the array by default (i.e. `arr.slice(1)` is a shorthand for `arr.slice(1, arr.size())`).

If either `begin` or `end` are negative, they will be relative to the end of the array (i.e. `arr.slice(0, -2)` is a shorthand for `arr.slice(0, arr.size() - 2)`).


----



|void| **sort**\ (\ ) [🔗<class_PackedInt32Array_method_sort>]

Sorts the elements of the array in ascending order.


----



[PackedByteArray<class_PackedByteArray>] **to_byte_array**\ (\ ) |const| [🔗<class_PackedInt32Array_method_to_byte_array>]

Returns a copy of the data converted to a [PackedByteArray<class_PackedByteArray>], where each element has been encoded as 4 bytes.

The size of the new array will be `int32_array.size() * 4`.


----


## Operator Descriptions



[bool<class_bool>] **operator !=**\ (\ right\: [PackedInt32Array<class_PackedInt32Array>]\ ) [🔗<class_PackedInt32Array_operator_neq_PackedInt32Array>]

Returns `true` if contents of the arrays differ.


----



[PackedInt32Array<class_PackedInt32Array>] **operator +**\ (\ right\: [PackedInt32Array<class_PackedInt32Array>]\ ) [🔗<class_PackedInt32Array_operator_sum_PackedInt32Array>]

Returns a new **PackedInt32Array** with contents of `right` added at the end of this array. For better performance, consider using [append_array()<class_PackedInt32Array_method_append_array>] instead.


----



[bool<class_bool>] **operator ==**\ (\ right\: [PackedInt32Array<class_PackedInt32Array>]\ ) [🔗<class_PackedInt32Array_operator_eq_PackedInt32Array>]

Returns `true` if contents of both arrays are the same, i.e. they have all equal ints at the corresponding indices.


----



[int<class_int>] **operator []**\ (\ index\: [int<class_int>]\ ) [🔗<class_PackedInt32Array_operator_idx_int>]

Returns the [int<class_int>] at index `index`. Negative indices can be used to access the elements starting from the end. Using index out of array's bounds will result in an error.

Note that [int<class_int>] type is 64-bit, unlike the values stored in the array.

