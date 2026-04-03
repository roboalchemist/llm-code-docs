:github_url: hide



# BitMap

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Boolean matrix.


## Description

A two-dimensional array of boolean values, can be used to efficiently store a binary matrix (every matrix element takes only one bit) and query the values using natural cartesian coordinates.


## Methods

> **TABLE**
> :widths: auto
>
> +----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Image<class_Image>`                                                        | :ref:`convert_to_image<class_BitMap_method_convert_to_image>`\ (\ ) |const|                                                                                       |
> +----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                           | :ref:`create<class_BitMap_method_create>`\ (\ size\: :ref:`Vector2i<class_Vector2i>`\ )                                                                           |
> +----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                           | :ref:`create_from_image_alpha<class_BitMap_method_create_from_image_alpha>`\ (\ image\: :ref:`Image<class_Image>`, threshold\: :ref:`float<class_float>` = 0.1\ ) |
> +----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                                          | :ref:`get_bit<class_BitMap_method_get_bit>`\ (\ x\: :ref:`int<class_int>`, y\: :ref:`int<class_int>`\ ) |const|                                                   |
> +----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                                          | :ref:`get_bitv<class_BitMap_method_get_bitv>`\ (\ position\: :ref:`Vector2i<class_Vector2i>`\ ) |const|                                                           |
> +----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2i<class_Vector2i>`                                                  | :ref:`get_size<class_BitMap_method_get_size>`\ (\ ) |const|                                                                                                       |
> +----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                                            | :ref:`get_true_bit_count<class_BitMap_method_get_true_bit_count>`\ (\ ) |const|                                                                                   |
> +----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                           | :ref:`grow_mask<class_BitMap_method_grow_mask>`\ (\ pixels\: :ref:`int<class_int>`, rect\: :ref:`Rect2i<class_Rect2i>`\ )                                         |
> +----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`PackedVector2Array<class_PackedVector2Array>`\] | :ref:`opaque_to_polygons<class_BitMap_method_opaque_to_polygons>`\ (\ rect\: :ref:`Rect2i<class_Rect2i>`, epsilon\: :ref:`float<class_float>` = 2.0\ ) |const|    |
> +----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                           | :ref:`resize<class_BitMap_method_resize>`\ (\ new_size\: :ref:`Vector2i<class_Vector2i>`\ )                                                                       |
> +----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                           | :ref:`set_bit<class_BitMap_method_set_bit>`\ (\ x\: :ref:`int<class_int>`, y\: :ref:`int<class_int>`, bit\: :ref:`bool<class_bool>`\ )                            |
> +----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                           | :ref:`set_bit_rect<class_BitMap_method_set_bit_rect>`\ (\ rect\: :ref:`Rect2i<class_Rect2i>`, bit\: :ref:`bool<class_bool>`\ )                                    |
> +----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                           | :ref:`set_bitv<class_BitMap_method_set_bitv>`\ (\ position\: :ref:`Vector2i<class_Vector2i>`, bit\: :ref:`bool<class_bool>`\ )                                    |
> +----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[Image<class_Image>] **convert_to_image**\ (\ ) |const| [🔗<class_BitMap_method_convert_to_image>]

Returns an image of the same size as the bitmap and with an [Format<enum_Image_Format>] of type [Image.FORMAT_L8<class_Image_constant_FORMAT_L8>]. `true` bits of the bitmap are being converted into white pixels, and `false` bits into black.


----



|void| **create**\ (\ size\: [Vector2i<class_Vector2i>]\ ) [🔗<class_BitMap_method_create>]

Creates a bitmap with the specified size, filled with `false`.


----



|void| **create_from_image_alpha**\ (\ image\: [Image<class_Image>], threshold\: [float<class_float>] = 0.1\ ) [🔗<class_BitMap_method_create_from_image_alpha>]

Creates a bitmap that matches the given image dimensions, every element of the bitmap is set to `false` if the alpha value of the image at that position is equal to `threshold` or less, and `true` in other case.


----



[bool<class_bool>] **get_bit**\ (\ x\: [int<class_int>], y\: [int<class_int>]\ ) |const| [🔗<class_BitMap_method_get_bit>]

Returns bitmap's value at the specified position.


----



[bool<class_bool>] **get_bitv**\ (\ position\: [Vector2i<class_Vector2i>]\ ) |const| [🔗<class_BitMap_method_get_bitv>]

Returns bitmap's value at the specified position.


----



[Vector2i<class_Vector2i>] **get_size**\ (\ ) |const| [🔗<class_BitMap_method_get_size>]

Returns bitmap's dimensions.


----



[int<class_int>] **get_true_bit_count**\ (\ ) |const| [🔗<class_BitMap_method_get_true_bit_count>]

Returns the number of bitmap elements that are set to `true`.


----



|void| **grow_mask**\ (\ pixels\: [int<class_int>], rect\: [Rect2i<class_Rect2i>]\ ) [🔗<class_BitMap_method_grow_mask>]

Applies morphological dilation or erosion to the bitmap. If `pixels` is positive, dilation is applied to the bitmap. If `pixels` is negative, erosion is applied to the bitmap. `rect` defines the area where the morphological operation is applied. Pixels located outside the `rect` are unaffected by [grow_mask()<class_BitMap_method_grow_mask>].


----



[Array<class_Array>]\[[PackedVector2Array<class_PackedVector2Array>]\] **opaque_to_polygons**\ (\ rect\: [Rect2i<class_Rect2i>], epsilon\: [float<class_float>] = 2.0\ ) |const| [🔗<class_BitMap_method_opaque_to_polygons>]

Creates an [Array<class_Array>] of polygons covering a rectangular portion of the bitmap. It uses a marching squares algorithm, followed by Ramer-Douglas-Peucker (RDP) reduction of the number of vertices. Each polygon is described as a [PackedVector2Array<class_PackedVector2Array>] of its vertices.

To get polygons covering the whole bitmap, pass:

::

    Rect2(Vector2(), get_size())

\ `epsilon` is passed to RDP to control how accurately the polygons cover the bitmap: a lower `epsilon` corresponds to more points in the polygons.


----



|void| **resize**\ (\ new_size\: [Vector2i<class_Vector2i>]\ ) [🔗<class_BitMap_method_resize>]

Resizes the image to `new_size`.


----



|void| **set_bit**\ (\ x\: [int<class_int>], y\: [int<class_int>], bit\: [bool<class_bool>]\ ) [🔗<class_BitMap_method_set_bit>]

Sets the bitmap's element at the specified position, to the specified value.


----



|void| **set_bit_rect**\ (\ rect\: [Rect2i<class_Rect2i>], bit\: [bool<class_bool>]\ ) [🔗<class_BitMap_method_set_bit_rect>]

Sets a rectangular portion of the bitmap to the specified value.


----



|void| **set_bitv**\ (\ position\: [Vector2i<class_Vector2i>], bit\: [bool<class_bool>]\ ) [🔗<class_BitMap_method_set_bitv>]

Sets the bitmap's element at the specified position, to the specified value.

