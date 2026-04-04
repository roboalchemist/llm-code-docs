:github_url: hide



# PackedFloat32Array

A packed array of 32-bit floating-point values.


## Description

An array specifically designed to hold 32-bit floating-point values (float). Packs data tightly, so it saves memory for large array sizes.

If you need to pack 64-bit floats tightly, see [PackedFloat64Array<class_PackedFloat64Array>].

\ **Note:** Packed arrays are always passed by reference. To get a copy of an array that can be modified independently of the original array, use [duplicate()<class_PackedFloat32Array_method_duplicate>]. This is *not* the case for built-in properties and methods. In these cases the returned packed array is a copy, and changing it will *not* affect the original value. To update a built-in property of this type, modify the returned array and then assign it to the property again.

> **NOTE**
>
	There are notable differences when using this API with C#. See [doc_c_sharp_differences] for more information.


## Constructors

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedFloat32Array<class_PackedFloat32Array>` | :ref:`PackedFloat32Array<class_PackedFloat32Array_constructor_PackedFloat32Array>`\ (\ )                                                             |
> +-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedFloat32Array<class_PackedFloat32Array>` | :ref:`PackedFloat32Array<class_PackedFloat32Array_constructor_PackedFloat32Array>`\ (\ from\: :ref:`PackedFloat32Array<class_PackedFloat32Array>`\ ) |
> +-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedFloat32Array<class_PackedFloat32Array>` | :ref:`PackedFloat32Array<class_PackedFloat32Array_constructor_PackedFloat32Array>`\ (\ from\: :ref:`Array<class_Array>`\ )                           |
> +-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                             | :ref:`append<class_PackedFloat32Array_method_append>`\ (\ value\: :ref:`float<class_float>`\ )                                                    |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`append_array<class_PackedFloat32Array_method_append_array>`\ (\ array\: :ref:`PackedFloat32Array<class_PackedFloat32Array>`\ )              |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                               | :ref:`bsearch<class_PackedFloat32Array_method_bsearch>`\ (\ value\: :ref:`float<class_float>`, before\: :ref:`bool<class_bool>` = true\ ) |const| |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`clear<class_PackedFloat32Array_method_clear>`\ (\ )                                                                                         |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                               | :ref:`count<class_PackedFloat32Array_method_count>`\ (\ value\: :ref:`float<class_float>`\ ) |const|                                              |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedFloat32Array<class_PackedFloat32Array>` | :ref:`duplicate<class_PackedFloat32Array_method_duplicate>`\ (\ ) |const|                                                                         |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                             | :ref:`erase<class_PackedFloat32Array_method_erase>`\ (\ value\: :ref:`float<class_float>`\ )                                                      |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`fill<class_PackedFloat32Array_method_fill>`\ (\ value\: :ref:`float<class_float>`\ )                                                        |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                               | :ref:`find<class_PackedFloat32Array_method_find>`\ (\ value\: :ref:`float<class_float>`, from\: :ref:`int<class_int>` = 0\ ) |const|              |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                           | :ref:`get<class_PackedFloat32Array_method_get>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                      |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                             | :ref:`has<class_PackedFloat32Array_method_has>`\ (\ value\: :ref:`float<class_float>`\ ) |const|                                                  |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                               | :ref:`insert<class_PackedFloat32Array_method_insert>`\ (\ at_index\: :ref:`int<class_int>`, value\: :ref:`float<class_float>`\ )                  |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                             | :ref:`is_empty<class_PackedFloat32Array_method_is_empty>`\ (\ ) |const|                                                                           |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                             | :ref:`push_back<class_PackedFloat32Array_method_push_back>`\ (\ value\: :ref:`float<class_float>`\ )                                              |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`remove_at<class_PackedFloat32Array_method_remove_at>`\ (\ index\: :ref:`int<class_int>`\ )                                                  |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                               | :ref:`resize<class_PackedFloat32Array_method_resize>`\ (\ new_size\: :ref:`int<class_int>`\ )                                                     |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`reverse<class_PackedFloat32Array_method_reverse>`\ (\ )                                                                                     |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                               | :ref:`rfind<class_PackedFloat32Array_method_rfind>`\ (\ value\: :ref:`float<class_float>`, from\: :ref:`int<class_int>` = -1\ ) |const|           |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`set<class_PackedFloat32Array_method_set>`\ (\ index\: :ref:`int<class_int>`, value\: :ref:`float<class_float>`\ )                           |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                               | :ref:`size<class_PackedFloat32Array_method_size>`\ (\ ) |const|                                                                                   |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedFloat32Array<class_PackedFloat32Array>` | :ref:`slice<class_PackedFloat32Array_method_slice>`\ (\ begin\: :ref:`int<class_int>`, end\: :ref:`int<class_int>` = 2147483647\ ) |const|        |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`sort<class_PackedFloat32Array_method_sort>`\ (\ )                                                                                           |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedByteArray<class_PackedByteArray>`       | :ref:`to_byte_array<class_PackedFloat32Array_method_to_byte_array>`\ (\ ) |const|                                                                 |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
>

## Operators

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                             | :ref:`operator !=<class_PackedFloat32Array_operator_neq_PackedFloat32Array>`\ (\ right\: :ref:`PackedFloat32Array<class_PackedFloat32Array>`\ ) |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedFloat32Array<class_PackedFloat32Array>` | :ref:`operator +<class_PackedFloat32Array_operator_sum_PackedFloat32Array>`\ (\ right\: :ref:`PackedFloat32Array<class_PackedFloat32Array>`\ )  |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                             | :ref:`operator ==<class_PackedFloat32Array_operator_eq_PackedFloat32Array>`\ (\ right\: :ref:`PackedFloat32Array<class_PackedFloat32Array>`\ )  |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                           | :ref:`operator []<class_PackedFloat32Array_operator_idx_int>`\ (\ index\: :ref:`int<class_int>`\ )                                              |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Constructor Descriptions



[PackedFloat32Array<class_PackedFloat32Array>] **PackedFloat32Array**\ (\ ) [🔗<class_PackedFloat32Array_constructor_PackedFloat32Array>]

Constructs an empty **PackedFloat32Array**.


----


[PackedFloat32Array<class_PackedFloat32Array>] **PackedFloat32Array**\ (\ from\: [PackedFloat32Array<class_PackedFloat32Array>]\ )

Constructs a **PackedFloat32Array** as a copy of the given **PackedFloat32Array**.


----


[PackedFloat32Array<class_PackedFloat32Array>] **PackedFloat32Array**\ (\ from\: [Array<class_Array>]\ )

Constructs a new **PackedFloat32Array**. Optionally, you can pass in a generic [Array<class_Array>] that will be converted.


----


## Method Descriptions



[bool<class_bool>] **append**\ (\ value\: [float<class_float>]\ ) [🔗<class_PackedFloat32Array_method_append>]

Appends an element at the end of the array (alias of [push_back()<class_PackedFloat32Array_method_push_back>]).


----



|void| **append_array**\ (\ array\: [PackedFloat32Array<class_PackedFloat32Array>]\ ) [🔗<class_PackedFloat32Array_method_append_array>]

Appends a **PackedFloat32Array** at the end of this array.


----



[int<class_int>] **bsearch**\ (\ value\: [float<class_float>], before\: [bool<class_bool>] = true\ ) |const| [🔗<class_PackedFloat32Array_method_bsearch>]

Finds the index of an existing value (or the insertion index that maintains sorting order, if the value is not yet present in the array) using binary search. Optionally, a `before` specifier can be passed. If `false`, the returned index comes after all existing entries of the value in the array.

\ **Note:** Calling [bsearch()<class_PackedFloat32Array_method_bsearch>] on an unsorted array results in unexpected behavior.

\ **Note:** [@GDScript.NAN<class_@GDScript_constant_NAN>] doesn't behave the same as other numbers. Therefore, the results from this method may not be accurate if NaNs are included.


----



|void| **clear**\ (\ ) [🔗<class_PackedFloat32Array_method_clear>]

Clears the array. This is equivalent to using [resize()<class_PackedFloat32Array_method_resize>] with a size of `0`.


----



[int<class_int>] **count**\ (\ value\: [float<class_float>]\ ) |const| [🔗<class_PackedFloat32Array_method_count>]

Returns the number of times an element is in the array.

\ **Note:** [@GDScript.NAN<class_@GDScript_constant_NAN>] doesn't behave the same as other numbers. Therefore, the results from this method may not be accurate if NaNs are included.


----



[PackedFloat32Array<class_PackedFloat32Array>] **duplicate**\ (\ ) |const| [🔗<class_PackedFloat32Array_method_duplicate>]

Creates a copy of the array, and returns it.


----



[bool<class_bool>] **erase**\ (\ value\: [float<class_float>]\ ) [🔗<class_PackedFloat32Array_method_erase>]

Removes the first occurrence of a value from the array and returns `true`. If the value does not exist in the array, nothing happens and `false` is returned. To remove an element by index, use [remove_at()<class_PackedFloat32Array_method_remove_at>] instead.

\ **Note:** [@GDScript.NAN<class_@GDScript_constant_NAN>] doesn't behave the same as other numbers. Therefore, the results from this method may not be accurate if NaNs are included.


----



|void| **fill**\ (\ value\: [float<class_float>]\ ) [🔗<class_PackedFloat32Array_method_fill>]

Assigns the given value to all elements in the array. This can typically be used together with [resize()<class_PackedFloat32Array_method_resize>] to create an array with a given size and initialized elements.


----



[int<class_int>] **find**\ (\ value\: [float<class_float>], from\: [int<class_int>] = 0\ ) |const| [🔗<class_PackedFloat32Array_method_find>]

Searches the array for a value and returns its index or `-1` if not found. Optionally, the initial search index can be passed.

\ **Note:** [@GDScript.NAN<class_@GDScript_constant_NAN>] doesn't behave the same as other numbers. Therefore, the results from this method may not be accurate if NaNs are included.


----



[float<class_float>] **get**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_PackedFloat32Array_method_get>]

Returns the 32-bit float at the given `index` in the array. If `index` is out-of-bounds or negative, this method fails and returns `0.0`.

This method is similar (but not identical) to the `[]` operator. Most notably, when this method fails, it doesn't pause project execution if run from the editor.


----



[bool<class_bool>] **has**\ (\ value\: [float<class_float>]\ ) |const| [🔗<class_PackedFloat32Array_method_has>]

Returns `true` if the array contains `value`.

\ **Note:** [@GDScript.NAN<class_@GDScript_constant_NAN>] doesn't behave the same as other numbers. Therefore, the results from this method may not be accurate if NaNs are included.


----



[int<class_int>] **insert**\ (\ at_index\: [int<class_int>], value\: [float<class_float>]\ ) [🔗<class_PackedFloat32Array_method_insert>]

Inserts a new element at a given position in the array. The position must be valid, or at the end of the array (`idx == size()`).


----



[bool<class_bool>] **is_empty**\ (\ ) |const| [🔗<class_PackedFloat32Array_method_is_empty>]

Returns `true` if the array is empty.


----



[bool<class_bool>] **push_back**\ (\ value\: [float<class_float>]\ ) [🔗<class_PackedFloat32Array_method_push_back>]

Appends an element at the end of the array.


----



|void| **remove_at**\ (\ index\: [int<class_int>]\ ) [🔗<class_PackedFloat32Array_method_remove_at>]

Removes an element from the array by index.


----



[int<class_int>] **resize**\ (\ new_size\: [int<class_int>]\ ) [🔗<class_PackedFloat32Array_method_resize>]

Sets the size of the array. If the array is grown, reserves elements at the end of the array. If the array is shrunk, truncates the array to the new size. Calling [resize()<class_PackedFloat32Array_method_resize>] once and assigning the new values is faster than adding new elements one by one.

Returns [@GlobalScope.OK<class_@GlobalScope_constant_OK>] on success, or one of the following [Error<enum_@GlobalScope_Error>] constants if this method fails: [@GlobalScope.ERR_INVALID_PARAMETER<class_@GlobalScope_constant_ERR_INVALID_PARAMETER>] if the size is negative, or [@GlobalScope.ERR_OUT_OF_MEMORY<class_@GlobalScope_constant_ERR_OUT_OF_MEMORY>] if allocations fail. Use [size()<class_PackedFloat32Array_method_size>] to find the actual size of the array after resize.


----



|void| **reverse**\ (\ ) [🔗<class_PackedFloat32Array_method_reverse>]

Reverses the order of the elements in the array.


----



[int<class_int>] **rfind**\ (\ value\: [float<class_float>], from\: [int<class_int>] = -1\ ) |const| [🔗<class_PackedFloat32Array_method_rfind>]

Searches the array in reverse order. Optionally, a start search index can be passed. If negative, the start index is considered relative to the end of the array.

\ **Note:** [@GDScript.NAN<class_@GDScript_constant_NAN>] doesn't behave the same as other numbers. Therefore, the results from this method may not be accurate if NaNs are included.


----



|void| **set**\ (\ index\: [int<class_int>], value\: [float<class_float>]\ ) [🔗<class_PackedFloat32Array_method_set>]

Changes the float at the given index.


----



[int<class_int>] **size**\ (\ ) |const| [🔗<class_PackedFloat32Array_method_size>]

Returns the number of elements in the array.


----



[PackedFloat32Array<class_PackedFloat32Array>] **slice**\ (\ begin\: [int<class_int>], end\: [int<class_int>] = 2147483647\ ) |const| [🔗<class_PackedFloat32Array_method_slice>]

Returns the slice of the **PackedFloat32Array**, from `begin` (inclusive) to `end` (exclusive), as a new **PackedFloat32Array**.

The absolute value of `begin` and `end` will be clamped to the array size, so the default value for `end` makes it slice to the size of the array by default (i.e. `arr.slice(1)` is a shorthand for `arr.slice(1, arr.size())`).

If either `begin` or `end` are negative, they will be relative to the end of the array (i.e. `arr.slice(0, -2)` is a shorthand for `arr.slice(0, arr.size() - 2)`).


----



|void| **sort**\ (\ ) [🔗<class_PackedFloat32Array_method_sort>]

Sorts the elements of the array in ascending order.

\ **Note:** [@GDScript.NAN<class_@GDScript_constant_NAN>] doesn't behave the same as other numbers. Therefore, the results from this method may not be accurate if NaNs are included.


----



[PackedByteArray<class_PackedByteArray>] **to_byte_array**\ (\ ) |const| [🔗<class_PackedFloat32Array_method_to_byte_array>]

Returns a copy of the data converted to a [PackedByteArray<class_PackedByteArray>], where each element has been encoded as 4 bytes.

The size of the new array will be `float32_array.size() * 4`.


----


## Operator Descriptions



[bool<class_bool>] **operator !=**\ (\ right\: [PackedFloat32Array<class_PackedFloat32Array>]\ ) [🔗<class_PackedFloat32Array_operator_neq_PackedFloat32Array>]

Returns `true` if contents of the arrays differ.


----



[PackedFloat32Array<class_PackedFloat32Array>] **operator +**\ (\ right\: [PackedFloat32Array<class_PackedFloat32Array>]\ ) [🔗<class_PackedFloat32Array_operator_sum_PackedFloat32Array>]

Returns a new **PackedFloat32Array** with contents of `right` added at the end of this array. For better performance, consider using [append_array()<class_PackedFloat32Array_method_append_array>] instead.


----



[bool<class_bool>] **operator ==**\ (\ right\: [PackedFloat32Array<class_PackedFloat32Array>]\ ) [🔗<class_PackedFloat32Array_operator_eq_PackedFloat32Array>]

Returns `true` if contents of both arrays are the same, i.e. they have all equal floats at the corresponding indices.


----



[float<class_float>] **operator []**\ (\ index\: [int<class_int>]\ ) [🔗<class_PackedFloat32Array_operator_idx_int>]

Returns the [float<class_float>] at index `index`. Negative indices can be used to access the elements starting from the end. Using index out of array's bounds will result in an error.

Note that [float<class_float>] type is 64-bit, unlike the values stored in the array.

