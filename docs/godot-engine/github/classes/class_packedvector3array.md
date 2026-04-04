:github_url: hide



# PackedVector3Array

A packed array of [Vector3<class_Vector3>]\ s.


## Description

An array specifically designed to hold [Vector3<class_Vector3>]. Packs data tightly, so it saves memory for large array sizes.

\ **Differences between packed arrays, typed arrays, and untyped arrays:** Packed arrays are generally faster to iterate on and modify compared to a typed array of the same type (e.g. **PackedVector3Array** versus `Array[Vector3]`). Also, packed arrays consume less memory. As a downside, packed arrays are less flexible as they don't offer as many convenience methods such as [Array.map()<class_Array_method_map>]. Typed arrays are in turn faster to iterate on and modify than untyped arrays.

\ **Note:** Packed arrays are always passed by reference. To get a copy of an array that can be modified independently of the original array, use [duplicate()<class_PackedVector3Array_method_duplicate>]. This is *not* the case for built-in properties and methods. In these cases the returned packed array is a copy, and changing it will *not* affect the original value. To update a built-in property of this type, modify the returned array and then assign it to the property again.

> **NOTE**
>
	There are notable differences when using this API with C#. See [doc_c_sharp_differences] for more information.


## Constructors

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedVector3Array<class_PackedVector3Array>` | :ref:`PackedVector3Array<class_PackedVector3Array_constructor_PackedVector3Array>`\ (\ )                                                             |
> +-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedVector3Array<class_PackedVector3Array>` | :ref:`PackedVector3Array<class_PackedVector3Array_constructor_PackedVector3Array>`\ (\ from\: :ref:`PackedVector3Array<class_PackedVector3Array>`\ ) |
> +-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedVector3Array<class_PackedVector3Array>` | :ref:`PackedVector3Array<class_PackedVector3Array_constructor_PackedVector3Array>`\ (\ from\: :ref:`Array<class_Array>`\ )                           |
> +-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                             | :ref:`append<class_PackedVector3Array_method_append>`\ (\ value\: :ref:`Vector3<class_Vector3>`\ )                                                    |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`append_array<class_PackedVector3Array_method_append_array>`\ (\ array\: :ref:`PackedVector3Array<class_PackedVector3Array>`\ )                  |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                               | :ref:`bsearch<class_PackedVector3Array_method_bsearch>`\ (\ value\: :ref:`Vector3<class_Vector3>`, before\: :ref:`bool<class_bool>` = true\ ) |const| |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`clear<class_PackedVector3Array_method_clear>`\ (\ )                                                                                             |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                               | :ref:`count<class_PackedVector3Array_method_count>`\ (\ value\: :ref:`Vector3<class_Vector3>`\ ) |const|                                              |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedVector3Array<class_PackedVector3Array>` | :ref:`duplicate<class_PackedVector3Array_method_duplicate>`\ (\ ) |const|                                                                             |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                             | :ref:`erase<class_PackedVector3Array_method_erase>`\ (\ value\: :ref:`Vector3<class_Vector3>`\ )                                                      |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`fill<class_PackedVector3Array_method_fill>`\ (\ value\: :ref:`Vector3<class_Vector3>`\ )                                                        |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                               | :ref:`find<class_PackedVector3Array_method_find>`\ (\ value\: :ref:`Vector3<class_Vector3>`, from\: :ref:`int<class_int>` = 0\ ) |const|              |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                       | :ref:`get<class_PackedVector3Array_method_get>`\ (\ index\: :ref:`int<class_int>`\ ) |const|                                                          |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                             | :ref:`has<class_PackedVector3Array_method_has>`\ (\ value\: :ref:`Vector3<class_Vector3>`\ ) |const|                                                  |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                               | :ref:`insert<class_PackedVector3Array_method_insert>`\ (\ at_index\: :ref:`int<class_int>`, value\: :ref:`Vector3<class_Vector3>`\ )                  |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                             | :ref:`is_empty<class_PackedVector3Array_method_is_empty>`\ (\ ) |const|                                                                               |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                             | :ref:`push_back<class_PackedVector3Array_method_push_back>`\ (\ value\: :ref:`Vector3<class_Vector3>`\ )                                              |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`remove_at<class_PackedVector3Array_method_remove_at>`\ (\ index\: :ref:`int<class_int>`\ )                                                      |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                               | :ref:`resize<class_PackedVector3Array_method_resize>`\ (\ new_size\: :ref:`int<class_int>`\ )                                                         |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`reverse<class_PackedVector3Array_method_reverse>`\ (\ )                                                                                         |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                               | :ref:`rfind<class_PackedVector3Array_method_rfind>`\ (\ value\: :ref:`Vector3<class_Vector3>`, from\: :ref:`int<class_int>` = -1\ ) |const|           |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`set<class_PackedVector3Array_method_set>`\ (\ index\: :ref:`int<class_int>`, value\: :ref:`Vector3<class_Vector3>`\ )                           |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                               | :ref:`size<class_PackedVector3Array_method_size>`\ (\ ) |const|                                                                                       |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedVector3Array<class_PackedVector3Array>` | :ref:`slice<class_PackedVector3Array_method_slice>`\ (\ begin\: :ref:`int<class_int>`, end\: :ref:`int<class_int>` = 2147483647\ ) |const|            |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`sort<class_PackedVector3Array_method_sort>`\ (\ )                                                                                               |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedByteArray<class_PackedByteArray>`       | :ref:`to_byte_array<class_PackedVector3Array_method_to_byte_array>`\ (\ ) |const|                                                                     |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
>

## Operators

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                             | :ref:`operator !=<class_PackedVector3Array_operator_neq_PackedVector3Array>`\ (\ right\: :ref:`PackedVector3Array<class_PackedVector3Array>`\ ) |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedVector3Array<class_PackedVector3Array>` | :ref:`operator *<class_PackedVector3Array_operator_mul_Transform3D>`\ (\ right\: :ref:`Transform3D<class_Transform3D>`\ )                       |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedVector3Array<class_PackedVector3Array>` | :ref:`operator +<class_PackedVector3Array_operator_sum_PackedVector3Array>`\ (\ right\: :ref:`PackedVector3Array<class_PackedVector3Array>`\ )  |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                             | :ref:`operator ==<class_PackedVector3Array_operator_eq_PackedVector3Array>`\ (\ right\: :ref:`PackedVector3Array<class_PackedVector3Array>`\ )  |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector3<class_Vector3>`                       | :ref:`operator []<class_PackedVector3Array_operator_idx_int>`\ (\ index\: :ref:`int<class_int>`\ )                                              |
> +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Constructor Descriptions



[PackedVector3Array<class_PackedVector3Array>] **PackedVector3Array**\ (\ ) [🔗<class_PackedVector3Array_constructor_PackedVector3Array>]

Constructs an empty **PackedVector3Array**.


----


[PackedVector3Array<class_PackedVector3Array>] **PackedVector3Array**\ (\ from\: [PackedVector3Array<class_PackedVector3Array>]\ )

Constructs a **PackedVector3Array** as a copy of the given **PackedVector3Array**.


----


[PackedVector3Array<class_PackedVector3Array>] **PackedVector3Array**\ (\ from\: [Array<class_Array>]\ )

Constructs a new **PackedVector3Array**. Optionally, you can pass in a generic [Array<class_Array>] that will be converted.

\ **Note:** When initializing a **PackedVector3Array** with elements, it must be initialized with an [Array<class_Array>] of [Vector3<class_Vector3>] values:

::

    var array = PackedVector3Array([Vector3(12, 34, 56), Vector3(78, 90, 12)])


----


## Method Descriptions



[bool<class_bool>] **append**\ (\ value\: [Vector3<class_Vector3>]\ ) [🔗<class_PackedVector3Array_method_append>]

Appends an element at the end of the array (alias of [push_back()<class_PackedVector3Array_method_push_back>]).


----



|void| **append_array**\ (\ array\: [PackedVector3Array<class_PackedVector3Array>]\ ) [🔗<class_PackedVector3Array_method_append_array>]

Appends a **PackedVector3Array** at the end of this array.


----



[int<class_int>] **bsearch**\ (\ value\: [Vector3<class_Vector3>], before\: [bool<class_bool>] = true\ ) |const| [🔗<class_PackedVector3Array_method_bsearch>]

Finds the index of an existing value (or the insertion index that maintains sorting order, if the value is not yet present in the array) using binary search. Optionally, a `before` specifier can be passed. If `false`, the returned index comes after all existing entries of the value in the array.

\ **Note:** Calling [bsearch()<class_PackedVector3Array_method_bsearch>] on an unsorted array results in unexpected behavior.

\ **Note:** Vectors with [@GDScript.NAN<class_@GDScript_constant_NAN>] elements don't behave the same as other vectors. Therefore, the results from this method may not be accurate if NaNs are included.


----



|void| **clear**\ (\ ) [🔗<class_PackedVector3Array_method_clear>]

Clears the array. This is equivalent to using [resize()<class_PackedVector3Array_method_resize>] with a size of `0`.


----



[int<class_int>] **count**\ (\ value\: [Vector3<class_Vector3>]\ ) |const| [🔗<class_PackedVector3Array_method_count>]

Returns the number of times an element is in the array.

\ **Note:** Vectors with [@GDScript.NAN<class_@GDScript_constant_NAN>] elements don't behave the same as other vectors. Therefore, the results from this method may not be accurate if NaNs are included.


----



[PackedVector3Array<class_PackedVector3Array>] **duplicate**\ (\ ) |const| [🔗<class_PackedVector3Array_method_duplicate>]

Creates a copy of the array, and returns it.


----



[bool<class_bool>] **erase**\ (\ value\: [Vector3<class_Vector3>]\ ) [🔗<class_PackedVector3Array_method_erase>]

Removes the first occurrence of a value from the array and returns `true`. If the value does not exist in the array, nothing happens and `false` is returned. To remove an element by index, use [remove_at()<class_PackedVector3Array_method_remove_at>] instead.

\ **Note:** Vectors with [@GDScript.NAN<class_@GDScript_constant_NAN>] elements don't behave the same as other vectors. Therefore, the results from this method may not be accurate if NaNs are included.


----



|void| **fill**\ (\ value\: [Vector3<class_Vector3>]\ ) [🔗<class_PackedVector3Array_method_fill>]

Assigns the given value to all elements in the array. This can typically be used together with [resize()<class_PackedVector3Array_method_resize>] to create an array with a given size and initialized elements.


----



[int<class_int>] **find**\ (\ value\: [Vector3<class_Vector3>], from\: [int<class_int>] = 0\ ) |const| [🔗<class_PackedVector3Array_method_find>]

Searches the array for a value and returns its index or `-1` if not found. Optionally, the initial search index can be passed.

\ **Note:** Vectors with [@GDScript.NAN<class_@GDScript_constant_NAN>] elements don't behave the same as other vectors. Therefore, the results from this method may not be accurate if NaNs are included.


----



[Vector3<class_Vector3>] **get**\ (\ index\: [int<class_int>]\ ) |const| [🔗<class_PackedVector3Array_method_get>]

Returns the [Vector3<class_Vector3>] at the given `index` in the array. If `index` is out-of-bounds or negative, this method fails and returns `Vector3(0, 0, 0)`.

This method is similar (but not identical) to the `[]` operator. Most notably, when this method fails, it doesn't pause project execution if run from the editor.


----



[bool<class_bool>] **has**\ (\ value\: [Vector3<class_Vector3>]\ ) |const| [🔗<class_PackedVector3Array_method_has>]

Returns `true` if the array contains `value`.

\ **Note:** Vectors with [@GDScript.NAN<class_@GDScript_constant_NAN>] elements don't behave the same as other vectors. Therefore, the results from this method may not be accurate if NaNs are included.


----



[int<class_int>] **insert**\ (\ at_index\: [int<class_int>], value\: [Vector3<class_Vector3>]\ ) [🔗<class_PackedVector3Array_method_insert>]

Inserts a new element at a given position in the array. The position must be valid, or at the end of the array (`idx == size()`).


----



[bool<class_bool>] **is_empty**\ (\ ) |const| [🔗<class_PackedVector3Array_method_is_empty>]

Returns `true` if the array is empty.


----



[bool<class_bool>] **push_back**\ (\ value\: [Vector3<class_Vector3>]\ ) [🔗<class_PackedVector3Array_method_push_back>]

Inserts a [Vector3<class_Vector3>] at the end.


----



|void| **remove_at**\ (\ index\: [int<class_int>]\ ) [🔗<class_PackedVector3Array_method_remove_at>]

Removes an element from the array by index.


----



[int<class_int>] **resize**\ (\ new_size\: [int<class_int>]\ ) [🔗<class_PackedVector3Array_method_resize>]

Sets the size of the array. If the array is grown, reserves elements at the end of the array. If the array is shrunk, truncates the array to the new size. Calling [resize()<class_PackedVector3Array_method_resize>] once and assigning the new values is faster than adding new elements one by one.

Returns [@GlobalScope.OK<class_@GlobalScope_constant_OK>] on success, or one of the following [Error<enum_@GlobalScope_Error>] constants if this method fails: [@GlobalScope.ERR_INVALID_PARAMETER<class_@GlobalScope_constant_ERR_INVALID_PARAMETER>] if the size is negative, or [@GlobalScope.ERR_OUT_OF_MEMORY<class_@GlobalScope_constant_ERR_OUT_OF_MEMORY>] if allocations fail. Use [size()<class_PackedVector3Array_method_size>] to find the actual size of the array after resize.


----



|void| **reverse**\ (\ ) [🔗<class_PackedVector3Array_method_reverse>]

Reverses the order of the elements in the array.


----



[int<class_int>] **rfind**\ (\ value\: [Vector3<class_Vector3>], from\: [int<class_int>] = -1\ ) |const| [🔗<class_PackedVector3Array_method_rfind>]

Searches the array in reverse order. Optionally, a start search index can be passed. If negative, the start index is considered relative to the end of the array.

\ **Note:** Vectors with [@GDScript.NAN<class_@GDScript_constant_NAN>] elements don't behave the same as other vectors. Therefore, the results from this method may not be accurate if NaNs are included.


----



|void| **set**\ (\ index\: [int<class_int>], value\: [Vector3<class_Vector3>]\ ) [🔗<class_PackedVector3Array_method_set>]

Changes the [Vector3<class_Vector3>] at the given index.


----



[int<class_int>] **size**\ (\ ) |const| [🔗<class_PackedVector3Array_method_size>]

Returns the number of elements in the array.


----



[PackedVector3Array<class_PackedVector3Array>] **slice**\ (\ begin\: [int<class_int>], end\: [int<class_int>] = 2147483647\ ) |const| [🔗<class_PackedVector3Array_method_slice>]

Returns the slice of the **PackedVector3Array**, from `begin` (inclusive) to `end` (exclusive), as a new **PackedVector3Array**.

The absolute value of `begin` and `end` will be clamped to the array size, so the default value for `end` makes it slice to the size of the array by default (i.e. `arr.slice(1)` is a shorthand for `arr.slice(1, arr.size())`).

If either `begin` or `end` are negative, they will be relative to the end of the array (i.e. `arr.slice(0, -2)` is a shorthand for `arr.slice(0, arr.size() - 2)`).


----



|void| **sort**\ (\ ) [🔗<class_PackedVector3Array_method_sort>]

Sorts the elements of the array in ascending order.

\ **Note:** Vectors with [@GDScript.NAN<class_@GDScript_constant_NAN>] elements don't behave the same as other vectors. Therefore, the results from this method may not be accurate if NaNs are included.


----



[PackedByteArray<class_PackedByteArray>] **to_byte_array**\ (\ ) |const| [🔗<class_PackedVector3Array_method_to_byte_array>]

Returns a [PackedByteArray<class_PackedByteArray>] with each vector encoded as bytes.


----


## Operator Descriptions



[bool<class_bool>] **operator !=**\ (\ right\: [PackedVector3Array<class_PackedVector3Array>]\ ) [🔗<class_PackedVector3Array_operator_neq_PackedVector3Array>]

Returns `true` if contents of the arrays differ.


----



[PackedVector3Array<class_PackedVector3Array>] **operator ***\ (\ right\: [Transform3D<class_Transform3D>]\ ) [🔗<class_PackedVector3Array_operator_mul_Transform3D>]

Returns a new **PackedVector3Array** with all vectors in this array inversely transformed (multiplied) by the given [Transform3D<class_Transform3D>] transformation matrix, under the assumption that the transformation basis is orthonormal (i.e. rotation/reflection is fine, scaling/skew is not).

\ `array * transform` is equivalent to `transform.inverse() * array`. See [Transform3D.inverse()<class_Transform3D_method_inverse>].

For transforming by inverse of an affine transformation (e.g. with scaling) `transform.affine_inverse() * array` can be used instead. See [Transform3D.affine_inverse()<class_Transform3D_method_affine_inverse>].


----



[PackedVector3Array<class_PackedVector3Array>] **operator +**\ (\ right\: [PackedVector3Array<class_PackedVector3Array>]\ ) [🔗<class_PackedVector3Array_operator_sum_PackedVector3Array>]

Returns a new **PackedVector3Array** with contents of `right` added at the end of this array. For better performance, consider using [append_array()<class_PackedVector3Array_method_append_array>] instead.


----



[bool<class_bool>] **operator ==**\ (\ right\: [PackedVector3Array<class_PackedVector3Array>]\ ) [🔗<class_PackedVector3Array_operator_eq_PackedVector3Array>]

Returns `true` if contents of both arrays are the same, i.e. they have all equal [Vector3<class_Vector3>]\ s at the corresponding indices.


----



[Vector3<class_Vector3>] **operator []**\ (\ index\: [int<class_int>]\ ) [🔗<class_PackedVector3Array_operator_idx_int>]

Returns the [Vector3<class_Vector3>] at index `index`. Negative indices can be used to access the elements starting from the end. Using index out of array's bounds will result in an error.

