:github_url: hide



# Noise

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [FastNoiseLite<class_FastNoiseLite>]

Abstract base class for noise generators.


## Description

This class defines the interface for noise generation libraries to inherit from.

A default [get_seamless_image()<class_Noise_method_get_seamless_image>] implementation is provided for libraries that do not provide seamless noise. This function requests a larger image from the [get_image()<class_Noise_method_get_image>] method, reverses the quadrants of the image, then uses the strips of extra width to blend over the seams.

Inheriting noise classes can optionally override this function to provide a more optimal algorithm.


## Methods

> **TABLE**
> :widths: auto
>
> +--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Image<class_Image>`                              | :ref:`get_image<class_Noise_method_get_image>`\ (\ width\: :ref:`int<class_int>`, height\: :ref:`int<class_int>`, invert\: :ref:`bool<class_bool>` = false, in_3d_space\: :ref:`bool<class_bool>` = false, normalize\: :ref:`bool<class_bool>` = true\ ) |const|                                                            |
> +--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`Image<class_Image>`\] | :ref:`get_image_3d<class_Noise_method_get_image_3d>`\ (\ width\: :ref:`int<class_int>`, height\: :ref:`int<class_int>`, depth\: :ref:`int<class_int>`, invert\: :ref:`bool<class_bool>` = false, normalize\: :ref:`bool<class_bool>` = true\ ) |const|                                                                      |
> +--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                              | :ref:`get_noise_1d<class_Noise_method_get_noise_1d>`\ (\ x\: :ref:`float<class_float>`\ ) |const|                                                                                                                                                                                                                           |
> +--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                              | :ref:`get_noise_2d<class_Noise_method_get_noise_2d>`\ (\ x\: :ref:`float<class_float>`, y\: :ref:`float<class_float>`\ ) |const|                                                                                                                                                                                            |
> +--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                              | :ref:`get_noise_2dv<class_Noise_method_get_noise_2dv>`\ (\ v\: :ref:`Vector2<class_Vector2>`\ ) |const|                                                                                                                                                                                                                     |
> +--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                              | :ref:`get_noise_3d<class_Noise_method_get_noise_3d>`\ (\ x\: :ref:`float<class_float>`, y\: :ref:`float<class_float>`, z\: :ref:`float<class_float>`\ ) |const|                                                                                                                                                             |
> +--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                              | :ref:`get_noise_3dv<class_Noise_method_get_noise_3dv>`\ (\ v\: :ref:`Vector3<class_Vector3>`\ ) |const|                                                                                                                                                                                                                     |
> +--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Image<class_Image>`                              | :ref:`get_seamless_image<class_Noise_method_get_seamless_image>`\ (\ width\: :ref:`int<class_int>`, height\: :ref:`int<class_int>`, invert\: :ref:`bool<class_bool>` = false, in_3d_space\: :ref:`bool<class_bool>` = false, skirt\: :ref:`float<class_float>` = 0.1, normalize\: :ref:`bool<class_bool>` = true\ ) |const| |
> +--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`Image<class_Image>`\] | :ref:`get_seamless_image_3d<class_Noise_method_get_seamless_image_3d>`\ (\ width\: :ref:`int<class_int>`, height\: :ref:`int<class_int>`, depth\: :ref:`int<class_int>`, invert\: :ref:`bool<class_bool>` = false, skirt\: :ref:`float<class_float>` = 0.1, normalize\: :ref:`bool<class_bool>` = true\ ) |const|           |
> +--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[Image<class_Image>] **get_image**\ (\ width\: [int<class_int>], height\: [int<class_int>], invert\: [bool<class_bool>] = false, in_3d_space\: [bool<class_bool>] = false, normalize\: [bool<class_bool>] = true\ ) |const| [🔗<class_Noise_method_get_image>]

Returns an [Image<class_Image>] containing 2D noise values.

\ **Note:** With `normalize` set to `false`, the default implementation expects the noise generator to return values in the range `-1.0` to `1.0`.


----



[Array<class_Array>]\[[Image<class_Image>]\] **get_image_3d**\ (\ width\: [int<class_int>], height\: [int<class_int>], depth\: [int<class_int>], invert\: [bool<class_bool>] = false, normalize\: [bool<class_bool>] = true\ ) |const| [🔗<class_Noise_method_get_image_3d>]

Returns an [Array<class_Array>] of [Image<class_Image>]\ s containing 3D noise values for use with [ImageTexture3D.create()<class_ImageTexture3D_method_create>].

\ **Note:** With `normalize` set to `false`, the default implementation expects the noise generator to return values in the range `-1.0` to `1.0`.


----



[float<class_float>] **get_noise_1d**\ (\ x\: [float<class_float>]\ ) |const| [🔗<class_Noise_method_get_noise_1d>]

Returns the 1D noise value at the given (x) coordinate.


----



[float<class_float>] **get_noise_2d**\ (\ x\: [float<class_float>], y\: [float<class_float>]\ ) |const| [🔗<class_Noise_method_get_noise_2d>]

Returns the 2D noise value at the given position.


----



[float<class_float>] **get_noise_2dv**\ (\ v\: [Vector2<class_Vector2>]\ ) |const| [🔗<class_Noise_method_get_noise_2dv>]

Returns the 2D noise value at the given position.


----



[float<class_float>] **get_noise_3d**\ (\ x\: [float<class_float>], y\: [float<class_float>], z\: [float<class_float>]\ ) |const| [🔗<class_Noise_method_get_noise_3d>]

Returns the 3D noise value at the given position.


----



[float<class_float>] **get_noise_3dv**\ (\ v\: [Vector3<class_Vector3>]\ ) |const| [🔗<class_Noise_method_get_noise_3dv>]

Returns the 3D noise value at the given position.


----



[Image<class_Image>] **get_seamless_image**\ (\ width\: [int<class_int>], height\: [int<class_int>], invert\: [bool<class_bool>] = false, in_3d_space\: [bool<class_bool>] = false, skirt\: [float<class_float>] = 0.1, normalize\: [bool<class_bool>] = true\ ) |const| [🔗<class_Noise_method_get_seamless_image>]

Returns an [Image<class_Image>] containing seamless 2D noise values.

\ **Note:** With `normalize` set to `false`, the default implementation expects the noise generator to return values in the range `-1.0` to `1.0`.


----



[Array<class_Array>]\[[Image<class_Image>]\] **get_seamless_image_3d**\ (\ width\: [int<class_int>], height\: [int<class_int>], depth\: [int<class_int>], invert\: [bool<class_bool>] = false, skirt\: [float<class_float>] = 0.1, normalize\: [bool<class_bool>] = true\ ) |const| [🔗<class_Noise_method_get_seamless_image_3d>]

Returns an [Array<class_Array>] of [Image<class_Image>]\ s containing seamless 3D noise values for use with [ImageTexture3D.create()<class_ImageTexture3D_method_create>].

\ **Note:** With `normalize` set to `false`, the default implementation expects the noise generator to return values in the range `-1.0` to `1.0`.

