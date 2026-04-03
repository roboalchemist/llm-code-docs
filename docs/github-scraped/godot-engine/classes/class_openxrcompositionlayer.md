:github_url: hide



# OpenXRCompositionLayer

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

**Inherited By:** [OpenXRCompositionLayerCylinder<class_OpenXRCompositionLayerCylinder>], [OpenXRCompositionLayerEquirect<class_OpenXRCompositionLayerEquirect>], [OpenXRCompositionLayerQuad<class_OpenXRCompositionLayerQuad>]

The parent class of all OpenXR composition layer nodes.


## Description

Composition layers allow 2D viewports to be displayed inside of the headset by the XR compositor through special projections that retain their quality. This allows for rendering clear text while keeping the layer at a native resolution.

\ **Note:** If the OpenXR runtime doesn't support the given composition layer type, a fallback mesh can be generated with a [ViewportTexture<class_ViewportTexture>], in order to emulate the composition layer.


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+--------------------------+
> | :ref:`bool<class_bool>`                                   | :ref:`alpha_blend<class_OpenXRCompositionLayer_property_alpha_blend>`                                         | ``false``                |
> +-----------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+--------------------------+
> | :ref:`Vector2i<class_Vector2i>`                           | :ref:`android_surface_size<class_OpenXRCompositionLayer_property_android_surface_size>`                       | ``Vector2i(1024, 1024)`` |
> +-----------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+--------------------------+
> | :ref:`bool<class_bool>`                                   | :ref:`enable_hole_punch<class_OpenXRCompositionLayer_property_enable_hole_punch>`                             | ``false``                |
> +-----------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+--------------------------+
> | :ref:`SubViewport<class_SubViewport>`                     | :ref:`layer_viewport<class_OpenXRCompositionLayer_property_layer_viewport>`                                   |                          |
> +-----------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+--------------------------+
> | :ref:`bool<class_bool>`                                   | :ref:`protected_content<class_OpenXRCompositionLayer_property_protected_content>`                             | ``false``                |
> +-----------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+--------------------------+
> | :ref:`int<class_int>`                                     | :ref:`sort_order<class_OpenXRCompositionLayer_property_sort_order>`                                           | ``1``                    |
> +-----------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+--------------------------+
> | :ref:`Swizzle<enum_OpenXRCompositionLayer_Swizzle>`       | :ref:`swapchain_state_alpha_swizzle<class_OpenXRCompositionLayer_property_swapchain_state_alpha_swizzle>`     | ``3``                    |
> +-----------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+--------------------------+
> | :ref:`Swizzle<enum_OpenXRCompositionLayer_Swizzle>`       | :ref:`swapchain_state_blue_swizzle<class_OpenXRCompositionLayer_property_swapchain_state_blue_swizzle>`       | ``2``                    |
> +-----------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+--------------------------+
> | :ref:`Color<class_Color>`                                 | :ref:`swapchain_state_border_color<class_OpenXRCompositionLayer_property_swapchain_state_border_color>`       | ``Color(0, 0, 0, 0)``    |
> +-----------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+--------------------------+
> | :ref:`Swizzle<enum_OpenXRCompositionLayer_Swizzle>`       | :ref:`swapchain_state_green_swizzle<class_OpenXRCompositionLayer_property_swapchain_state_green_swizzle>`     | ``1``                    |
> +-----------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+--------------------------+
> | :ref:`Wrap<enum_OpenXRCompositionLayer_Wrap>`             | :ref:`swapchain_state_horizontal_wrap<class_OpenXRCompositionLayer_property_swapchain_state_horizontal_wrap>` | ``0``                    |
> +-----------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+--------------------------+
> | :ref:`Filter<enum_OpenXRCompositionLayer_Filter>`         | :ref:`swapchain_state_mag_filter<class_OpenXRCompositionLayer_property_swapchain_state_mag_filter>`           | ``1``                    |
> +-----------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+--------------------------+
> | :ref:`float<class_float>`                                 | :ref:`swapchain_state_max_anisotropy<class_OpenXRCompositionLayer_property_swapchain_state_max_anisotropy>`   | ``1.0``                  |
> +-----------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+--------------------------+
> | :ref:`Filter<enum_OpenXRCompositionLayer_Filter>`         | :ref:`swapchain_state_min_filter<class_OpenXRCompositionLayer_property_swapchain_state_min_filter>`           | ``1``                    |
> +-----------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+--------------------------+
> | :ref:`MipmapMode<enum_OpenXRCompositionLayer_MipmapMode>` | :ref:`swapchain_state_mipmap_mode<class_OpenXRCompositionLayer_property_swapchain_state_mipmap_mode>`         | ``2``                    |
> +-----------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+--------------------------+
> | :ref:`Swizzle<enum_OpenXRCompositionLayer_Swizzle>`       | :ref:`swapchain_state_red_swizzle<class_OpenXRCompositionLayer_property_swapchain_state_red_swizzle>`         | ``0``                    |
> +-----------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+--------------------------+
> | :ref:`Wrap<enum_OpenXRCompositionLayer_Wrap>`             | :ref:`swapchain_state_vertical_wrap<class_OpenXRCompositionLayer_property_swapchain_state_vertical_wrap>`     | ``0``                    |
> +-----------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+--------------------------+
> | :ref:`bool<class_bool>`                                   | :ref:`use_android_surface<class_OpenXRCompositionLayer_property_use_android_surface>`                         | ``false``                |
> +-----------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+--------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`JavaObject<class_JavaObject>` | :ref:`get_android_surface<class_OpenXRCompositionLayer_method_get_android_surface>`\ (\ )                                                                                  |
> +-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>`       | :ref:`intersects_ray<class_OpenXRCompositionLayer_method_intersects_ray>`\ (\ origin\: :ref:`Vector3<class_Vector3>`, direction\: :ref:`Vector3<class_Vector3>`\ ) |const| |
> +-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`             | :ref:`is_natively_supported<class_OpenXRCompositionLayer_method_is_natively_supported>`\ (\ ) |const|                                                                      |
> +-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **Filter**: [🔗<enum_OpenXRCompositionLayer_Filter>]



[Filter<enum_OpenXRCompositionLayer_Filter>] **FILTER_NEAREST** = `0`

Perform nearest-neighbor filtering when sampling the texture.



[Filter<enum_OpenXRCompositionLayer_Filter>] **FILTER_LINEAR** = `1`

Perform linear filtering when sampling the texture.



[Filter<enum_OpenXRCompositionLayer_Filter>] **FILTER_CUBIC** = `2`

Perform cubic filtering when sampling the texture.


----



enum **MipmapMode**: [🔗<enum_OpenXRCompositionLayer_MipmapMode>]



[MipmapMode<enum_OpenXRCompositionLayer_MipmapMode>] **MIPMAP_MODE_DISABLED** = `0`

Disable mipmapping.

\ **Note:** Mipmapping can only be disabled in the Compatibility renderer.



[MipmapMode<enum_OpenXRCompositionLayer_MipmapMode>] **MIPMAP_MODE_NEAREST** = `1`

Use the mipmap of the nearest resolution.



[MipmapMode<enum_OpenXRCompositionLayer_MipmapMode>] **MIPMAP_MODE_LINEAR** = `2`

Use linear interpolation of the two mipmaps of the nearest resolution.


----



enum **Wrap**: [🔗<enum_OpenXRCompositionLayer_Wrap>]



[Wrap<enum_OpenXRCompositionLayer_Wrap>] **WRAP_CLAMP_TO_BORDER** = `0`

Clamp the texture to its specified border color.



[Wrap<enum_OpenXRCompositionLayer_Wrap>] **WRAP_CLAMP_TO_EDGE** = `1`

Clamp the texture to its edge color.



[Wrap<enum_OpenXRCompositionLayer_Wrap>] **WRAP_REPEAT** = `2`

Repeat the texture infinitely.



[Wrap<enum_OpenXRCompositionLayer_Wrap>] **WRAP_MIRRORED_REPEAT** = `3`

Repeat the texture infinitely, mirroring it on each repeat.



[Wrap<enum_OpenXRCompositionLayer_Wrap>] **WRAP_MIRROR_CLAMP_TO_EDGE** = `4`

Mirror the texture once and then clamp the texture to its edge color.

\ **Note:** This wrap mode is not available in the Compatibility renderer.


----



enum **Swizzle**: [🔗<enum_OpenXRCompositionLayer_Swizzle>]



[Swizzle<enum_OpenXRCompositionLayer_Swizzle>] **SWIZZLE_RED** = `0`

Maps a color channel to the value of the red channel.



[Swizzle<enum_OpenXRCompositionLayer_Swizzle>] **SWIZZLE_GREEN** = `1`

Maps a color channel to the value of the green channel.



[Swizzle<enum_OpenXRCompositionLayer_Swizzle>] **SWIZZLE_BLUE** = `2`

Maps a color channel to the value of the blue channel.



[Swizzle<enum_OpenXRCompositionLayer_Swizzle>] **SWIZZLE_ALPHA** = `3`

Maps a color channel to the value of the alpha channel.



[Swizzle<enum_OpenXRCompositionLayer_Swizzle>] **SWIZZLE_ZERO** = `4`

Maps a color channel to the value of zero.



[Swizzle<enum_OpenXRCompositionLayer_Swizzle>] **SWIZZLE_ONE** = `5`

Maps a color channel to the value of one.


----


## Property Descriptions



[bool<class_bool>] **alpha_blend** = `false` [🔗<class_OpenXRCompositionLayer_property_alpha_blend>]


- |void| **set_alpha_blend**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_alpha_blend**\ (\ )

Enables the blending the layer using its alpha channel.

Can be combined with [Viewport.transparent_bg<class_Viewport_property_transparent_bg>] to give the layer a transparent background.


----



[Vector2i<class_Vector2i>] **android_surface_size** = `Vector2i(1024, 1024)` [🔗<class_OpenXRCompositionLayer_property_android_surface_size>]


- |void| **set_android_surface_size**\ (\ value\: [Vector2i<class_Vector2i>]\ )
- [Vector2i<class_Vector2i>] **get_android_surface_size**\ (\ )

The size of the Android surface to create if [use_android_surface<class_OpenXRCompositionLayer_property_use_android_surface>] is enabled.


----



[bool<class_bool>] **enable_hole_punch** = `false` [🔗<class_OpenXRCompositionLayer_property_enable_hole_punch>]


- |void| **set_enable_hole_punch**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_enable_hole_punch**\ (\ )

Enables a technique called "hole punching", which allows putting the composition layer behind the main projection layer (i.e. setting [sort_order<class_OpenXRCompositionLayer_property_sort_order>] to a negative value) while "punching a hole" through everything rendered by Godot so that the layer is still visible.

This can be used to create the illusion that the composition layer exists in the same 3D space as everything rendered by Godot, allowing objects to appear to pass both behind or in front of the composition layer.


----



[SubViewport<class_SubViewport>] **layer_viewport** [🔗<class_OpenXRCompositionLayer_property_layer_viewport>]


- |void| **set_layer_viewport**\ (\ value\: [SubViewport<class_SubViewport>]\ )
- [SubViewport<class_SubViewport>] **get_layer_viewport**\ (\ )

The [SubViewport<class_SubViewport>] to render on the composition layer.


----



[bool<class_bool>] **protected_content** = `false` [🔗<class_OpenXRCompositionLayer_property_protected_content>]


- |void| **set_protected_content**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_protected_content**\ (\ )

If enabled, the OpenXR swapchain will be created with the `XR_SWAPCHAIN_CREATE_PROTECTED_CONTENT_BIT` flag, which will protect its contents from CPU access.

When used with an Android Surface, this may allow DRM content to be presented, and will only take effect when the Surface is first created; later changes to this property will have no effect.


----



[int<class_int>] **sort_order** = `1` [🔗<class_OpenXRCompositionLayer_property_sort_order>]


- |void| **set_sort_order**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_sort_order**\ (\ )

The sort order for this composition layer. Higher numbers will be shown in front of lower numbers.

\ **Note:** This will have no effect if a fallback mesh is being used.


----



[Swizzle<enum_OpenXRCompositionLayer_Swizzle>] **swapchain_state_alpha_swizzle** = `3` [🔗<class_OpenXRCompositionLayer_property_swapchain_state_alpha_swizzle>]


- |void| **set_alpha_swizzle**\ (\ value\: [Swizzle<enum_OpenXRCompositionLayer_Swizzle>]\ )
- [Swizzle<enum_OpenXRCompositionLayer_Swizzle>] **get_alpha_swizzle**\ (\ )

The swizzle value for the alpha channel of the swapchain state.

\ **Note:** This property only has an effect on devices that support the OpenXR XR_FB_swapchain_update_state OpenGLES/Vulkan extensions.


----



[Swizzle<enum_OpenXRCompositionLayer_Swizzle>] **swapchain_state_blue_swizzle** = `2` [🔗<class_OpenXRCompositionLayer_property_swapchain_state_blue_swizzle>]


- |void| **set_blue_swizzle**\ (\ value\: [Swizzle<enum_OpenXRCompositionLayer_Swizzle>]\ )
- [Swizzle<enum_OpenXRCompositionLayer_Swizzle>] **get_blue_swizzle**\ (\ )

The swizzle value for the blue channel of the swapchain state.

\ **Note:** This property only has an effect on devices that support the OpenXR XR_FB_swapchain_update_state OpenGLES/Vulkan extensions.


----



[Color<class_Color>] **swapchain_state_border_color** = `Color(0, 0, 0, 0)` [🔗<class_OpenXRCompositionLayer_property_swapchain_state_border_color>]


- |void| **set_border_color**\ (\ value\: [Color<class_Color>]\ )
- [Color<class_Color>] **get_border_color**\ (\ )

The border color of the swapchain state that is used when the wrap mode clamps to the border.

\ **Note:** This property only has an effect on devices that support the OpenXR XR_FB_swapchain_update_state OpenGLES/Vulkan extensions.


----



[Swizzle<enum_OpenXRCompositionLayer_Swizzle>] **swapchain_state_green_swizzle** = `1` [🔗<class_OpenXRCompositionLayer_property_swapchain_state_green_swizzle>]


- |void| **set_green_swizzle**\ (\ value\: [Swizzle<enum_OpenXRCompositionLayer_Swizzle>]\ )
- [Swizzle<enum_OpenXRCompositionLayer_Swizzle>] **get_green_swizzle**\ (\ )

The swizzle value for the green channel of the swapchain state.

\ **Note:** This property only has an effect on devices that support the OpenXR XR_FB_swapchain_update_state OpenGLES/Vulkan extensions.


----



[Wrap<enum_OpenXRCompositionLayer_Wrap>] **swapchain_state_horizontal_wrap** = `0` [🔗<class_OpenXRCompositionLayer_property_swapchain_state_horizontal_wrap>]


- |void| **set_horizontal_wrap**\ (\ value\: [Wrap<enum_OpenXRCompositionLayer_Wrap>]\ )
- [Wrap<enum_OpenXRCompositionLayer_Wrap>] **get_horizontal_wrap**\ (\ )

The horizontal wrap mode of the swapchain state.

\ **Note:** This property only has an effect on devices that support the OpenXR XR_FB_swapchain_update_state OpenGLES/Vulkan extensions.


----



[Filter<enum_OpenXRCompositionLayer_Filter>] **swapchain_state_mag_filter** = `1` [🔗<class_OpenXRCompositionLayer_property_swapchain_state_mag_filter>]


- |void| **set_mag_filter**\ (\ value\: [Filter<enum_OpenXRCompositionLayer_Filter>]\ )
- [Filter<enum_OpenXRCompositionLayer_Filter>] **get_mag_filter**\ (\ )

The magnification filter of the swapchain state.

\ **Note:** This property only has an effect on devices that support the OpenXR XR_FB_swapchain_update_state OpenGLES/Vulkan extensions.


----



[float<class_float>] **swapchain_state_max_anisotropy** = `1.0` [🔗<class_OpenXRCompositionLayer_property_swapchain_state_max_anisotropy>]


- |void| **set_max_anisotropy**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_max_anisotropy**\ (\ )

The max anisotropy of the swapchain state.

\ **Note:** This property only has an effect on devices that support the OpenXR XR_FB_swapchain_update_state OpenGLES/Vulkan extensions.


----



[Filter<enum_OpenXRCompositionLayer_Filter>] **swapchain_state_min_filter** = `1` [🔗<class_OpenXRCompositionLayer_property_swapchain_state_min_filter>]


- |void| **set_min_filter**\ (\ value\: [Filter<enum_OpenXRCompositionLayer_Filter>]\ )
- [Filter<enum_OpenXRCompositionLayer_Filter>] **get_min_filter**\ (\ )

The minification filter of the swapchain state.

\ **Note:** This property only has an effect on devices that support the OpenXR XR_FB_swapchain_update_state OpenGLES/Vulkan extensions.


----



[MipmapMode<enum_OpenXRCompositionLayer_MipmapMode>] **swapchain_state_mipmap_mode** = `2` [🔗<class_OpenXRCompositionLayer_property_swapchain_state_mipmap_mode>]


- |void| **set_mipmap_mode**\ (\ value\: [MipmapMode<enum_OpenXRCompositionLayer_MipmapMode>]\ )
- [MipmapMode<enum_OpenXRCompositionLayer_MipmapMode>] **get_mipmap_mode**\ (\ )

The mipmap mode of the swapchain state.

\ **Note:** This property only has an effect on devices that support the OpenXR XR_FB_swapchain_update_state OpenGLES/Vulkan extensions.


----



[Swizzle<enum_OpenXRCompositionLayer_Swizzle>] **swapchain_state_red_swizzle** = `0` [🔗<class_OpenXRCompositionLayer_property_swapchain_state_red_swizzle>]


- |void| **set_red_swizzle**\ (\ value\: [Swizzle<enum_OpenXRCompositionLayer_Swizzle>]\ )
- [Swizzle<enum_OpenXRCompositionLayer_Swizzle>] **get_red_swizzle**\ (\ )

The swizzle value for the red channel of the swapchain state.

\ **Note:** This property only has an effect on devices that support the OpenXR XR_FB_swapchain_update_state OpenGLES/Vulkan extensions.


----



[Wrap<enum_OpenXRCompositionLayer_Wrap>] **swapchain_state_vertical_wrap** = `0` [🔗<class_OpenXRCompositionLayer_property_swapchain_state_vertical_wrap>]


- |void| **set_vertical_wrap**\ (\ value\: [Wrap<enum_OpenXRCompositionLayer_Wrap>]\ )
- [Wrap<enum_OpenXRCompositionLayer_Wrap>] **get_vertical_wrap**\ (\ )

The vertical wrap mode of the swapchain state.

\ **Note:** This property only has an effect on devices that support the OpenXR XR_FB_swapchain_update_state OpenGLES/Vulkan extensions.


----



[bool<class_bool>] **use_android_surface** = `false` [🔗<class_OpenXRCompositionLayer_property_use_android_surface>]


- |void| **set_use_android_surface**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_use_android_surface**\ (\ )

If enabled, an Android surface will be created (with the dimensions from [android_surface_size<class_OpenXRCompositionLayer_property_android_surface_size>]) which will provide the 2D content for the composition layer, rather than using [layer_viewport<class_OpenXRCompositionLayer_property_layer_viewport>].

See [get_android_surface()<class_OpenXRCompositionLayer_method_get_android_surface>] for information about how to get the surface so that your application can draw to it.

\ **Note:** This will only work in Android builds.


----


## Method Descriptions



[JavaObject<class_JavaObject>] **get_android_surface**\ (\ ) [🔗<class_OpenXRCompositionLayer_method_get_android_surface>]

Returns a [JavaObject<class_JavaObject>] representing an `android.view.Surface` if [use_android_surface<class_OpenXRCompositionLayer_property_use_android_surface>] is enabled and OpenXR has created the surface. Otherwise, this will return `null`.

\ **Note:** The surface can only be created during an active OpenXR session. So, if [use_android_surface<class_OpenXRCompositionLayer_property_use_android_surface>] is enabled outside of an OpenXR session, it won't be created until a new session fully starts.


----



[Vector2<class_Vector2>] **intersects_ray**\ (\ origin\: [Vector3<class_Vector3>], direction\: [Vector3<class_Vector3>]\ ) |const| [🔗<class_OpenXRCompositionLayer_method_intersects_ray>]

Returns UV coordinates where the given ray intersects with the composition layer. `origin` and `direction` must be in global space.

Returns `Vector2(-1.0, -1.0)` if the ray doesn't intersect.


----



[bool<class_bool>] **is_natively_supported**\ (\ ) |const| [🔗<class_OpenXRCompositionLayer_method_is_natively_supported>]

Returns `true` if the OpenXR runtime natively supports this composition layer type.

\ **Note:** This will only return an accurate result after the OpenXR session has started.

