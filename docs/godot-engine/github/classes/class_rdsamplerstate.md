:github_url: hide



# RDSamplerState

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Sampler state (used by [RenderingDevice<class_RenderingDevice>]).


## Description

This object is used by [RenderingDevice<class_RenderingDevice>].


## Properties

> **TABLE**
> :widths: auto
>
> +--------------------------------------------------------------------+-------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>`                                          | :ref:`anisotropy_max<class_RDSamplerState_property_anisotropy_max>`     | ``1.0``   |
> +--------------------------------------------------------------------+-------------------------------------------------------------------------+-----------+
> | :ref:`SamplerBorderColor<enum_RenderingDevice_SamplerBorderColor>` | :ref:`border_color<class_RDSamplerState_property_border_color>`         | ``2``     |
> +--------------------------------------------------------------------+-------------------------------------------------------------------------+-----------+
> | :ref:`CompareOperator<enum_RenderingDevice_CompareOperator>`       | :ref:`compare_op<class_RDSamplerState_property_compare_op>`             | ``7``     |
> +--------------------------------------------------------------------+-------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                                            | :ref:`enable_compare<class_RDSamplerState_property_enable_compare>`     | ``false`` |
> +--------------------------------------------------------------------+-------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>`                                          | :ref:`lod_bias<class_RDSamplerState_property_lod_bias>`                 | ``0.0``   |
> +--------------------------------------------------------------------+-------------------------------------------------------------------------+-----------+
> | :ref:`SamplerFilter<enum_RenderingDevice_SamplerFilter>`           | :ref:`mag_filter<class_RDSamplerState_property_mag_filter>`             | ``0``     |
> +--------------------------------------------------------------------+-------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>`                                          | :ref:`max_lod<class_RDSamplerState_property_max_lod>`                   | ``1e+20`` |
> +--------------------------------------------------------------------+-------------------------------------------------------------------------+-----------+
> | :ref:`SamplerFilter<enum_RenderingDevice_SamplerFilter>`           | :ref:`min_filter<class_RDSamplerState_property_min_filter>`             | ``0``     |
> +--------------------------------------------------------------------+-------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>`                                          | :ref:`min_lod<class_RDSamplerState_property_min_lod>`                   | ``0.0``   |
> +--------------------------------------------------------------------+-------------------------------------------------------------------------+-----------+
> | :ref:`SamplerFilter<enum_RenderingDevice_SamplerFilter>`           | :ref:`mip_filter<class_RDSamplerState_property_mip_filter>`             | ``0``     |
> +--------------------------------------------------------------------+-------------------------------------------------------------------------+-----------+
> | :ref:`SamplerRepeatMode<enum_RenderingDevice_SamplerRepeatMode>`   | :ref:`repeat_u<class_RDSamplerState_property_repeat_u>`                 | ``2``     |
> +--------------------------------------------------------------------+-------------------------------------------------------------------------+-----------+
> | :ref:`SamplerRepeatMode<enum_RenderingDevice_SamplerRepeatMode>`   | :ref:`repeat_v<class_RDSamplerState_property_repeat_v>`                 | ``2``     |
> +--------------------------------------------------------------------+-------------------------------------------------------------------------+-----------+
> | :ref:`SamplerRepeatMode<enum_RenderingDevice_SamplerRepeatMode>`   | :ref:`repeat_w<class_RDSamplerState_property_repeat_w>`                 | ``2``     |
> +--------------------------------------------------------------------+-------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                                            | :ref:`unnormalized_uvw<class_RDSamplerState_property_unnormalized_uvw>` | ``false`` |
> +--------------------------------------------------------------------+-------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                                            | :ref:`use_anisotropy<class_RDSamplerState_property_use_anisotropy>`     | ``false`` |
> +--------------------------------------------------------------------+-------------------------------------------------------------------------+-----------+
>

----


## Property Descriptions



[float<class_float>] **anisotropy_max** = `1.0` [🔗<class_RDSamplerState_property_anisotropy_max>]


- |void| **set_anisotropy_max**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_anisotropy_max**\ (\ )

Maximum anisotropy that can be used when sampling. Only effective if [use_anisotropy<class_RDSamplerState_property_use_anisotropy>] is `true`. Higher values result in a sharper sampler at oblique angles, at the cost of performance (due to memory bandwidth). This value may be limited by the graphics hardware in use. Most graphics hardware only supports values up to `16.0`.

If [anisotropy_max<class_RDSamplerState_property_anisotropy_max>] is `1.0`, forcibly disables anisotropy even if [use_anisotropy<class_RDSamplerState_property_use_anisotropy>] is `true`.


----



[SamplerBorderColor<enum_RenderingDevice_SamplerBorderColor>] **border_color** = `2` [🔗<class_RDSamplerState_property_border_color>]


- |void| **set_border_color**\ (\ value\: [SamplerBorderColor<enum_RenderingDevice_SamplerBorderColor>]\ )
- [SamplerBorderColor<enum_RenderingDevice_SamplerBorderColor>] **get_border_color**\ (\ )

The border color that will be returned when sampling outside the sampler's bounds and the [repeat_u<class_RDSamplerState_property_repeat_u>], [repeat_v<class_RDSamplerState_property_repeat_v>] or [repeat_w<class_RDSamplerState_property_repeat_w>] modes have repeating disabled.


----



[CompareOperator<enum_RenderingDevice_CompareOperator>] **compare_op** = `7` [🔗<class_RDSamplerState_property_compare_op>]


- |void| **set_compare_op**\ (\ value\: [CompareOperator<enum_RenderingDevice_CompareOperator>]\ )
- [CompareOperator<enum_RenderingDevice_CompareOperator>] **get_compare_op**\ (\ )

The compare operation to use. Only effective if [enable_compare<class_RDSamplerState_property_enable_compare>] is `true`.


----



[bool<class_bool>] **enable_compare** = `false` [🔗<class_RDSamplerState_property_enable_compare>]


- |void| **set_enable_compare**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_enable_compare**\ (\ )

If `true`, returned values will be based on the comparison operation defined in [compare_op<class_RDSamplerState_property_compare_op>]. This is a hardware-based approach and is therefore faster than performing this manually in a shader. For example, compare operations are used for shadow map rendering by comparing depth values from a shadow sampler.


----



[float<class_float>] **lod_bias** = `0.0` [🔗<class_RDSamplerState_property_lod_bias>]


- |void| **set_lod_bias**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_lod_bias**\ (\ )

The mipmap LOD bias to use. Positive values will make the sampler blurrier at a given distance, while negative values will make the sampler sharper at a given distance (at the risk of looking grainy). Recommended values are between `-0.5` and `0.0`. Only effective if the sampler has mipmaps available.


----



[SamplerFilter<enum_RenderingDevice_SamplerFilter>] **mag_filter** = `0` [🔗<class_RDSamplerState_property_mag_filter>]


- |void| **set_mag_filter**\ (\ value\: [SamplerFilter<enum_RenderingDevice_SamplerFilter>]\ )
- [SamplerFilter<enum_RenderingDevice_SamplerFilter>] **get_mag_filter**\ (\ )

The sampler's magnification filter. It is the filtering method used when sampling texels that appear bigger than on-screen pixels.


----



[float<class_float>] **max_lod** = `1e+20` [🔗<class_RDSamplerState_property_max_lod>]


- |void| **set_max_lod**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_max_lod**\ (\ )

The maximum mipmap LOD bias to display (lowest resolution). Only effective if the sampler has mipmaps available.


----



[SamplerFilter<enum_RenderingDevice_SamplerFilter>] **min_filter** = `0` [🔗<class_RDSamplerState_property_min_filter>]


- |void| **set_min_filter**\ (\ value\: [SamplerFilter<enum_RenderingDevice_SamplerFilter>]\ )
- [SamplerFilter<enum_RenderingDevice_SamplerFilter>] **get_min_filter**\ (\ )

The sampler's minification filter. It is the filtering method used when sampling texels that appear smaller than on-screen pixels.


----



[float<class_float>] **min_lod** = `0.0` [🔗<class_RDSamplerState_property_min_lod>]


- |void| **set_min_lod**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_min_lod**\ (\ )

The minimum mipmap LOD bias to display (highest resolution). Only effective if the sampler has mipmaps available.


----



[SamplerFilter<enum_RenderingDevice_SamplerFilter>] **mip_filter** = `0` [🔗<class_RDSamplerState_property_mip_filter>]


- |void| **set_mip_filter**\ (\ value\: [SamplerFilter<enum_RenderingDevice_SamplerFilter>]\ )
- [SamplerFilter<enum_RenderingDevice_SamplerFilter>] **get_mip_filter**\ (\ )

The filtering method to use for mipmaps.


----



[SamplerRepeatMode<enum_RenderingDevice_SamplerRepeatMode>] **repeat_u** = `2` [🔗<class_RDSamplerState_property_repeat_u>]


- |void| **set_repeat_u**\ (\ value\: [SamplerRepeatMode<enum_RenderingDevice_SamplerRepeatMode>]\ )
- [SamplerRepeatMode<enum_RenderingDevice_SamplerRepeatMode>] **get_repeat_u**\ (\ )

The repeat mode to use along the U axis of UV coordinates. This affects the returned values if sampling outside the UV bounds.


----



[SamplerRepeatMode<enum_RenderingDevice_SamplerRepeatMode>] **repeat_v** = `2` [🔗<class_RDSamplerState_property_repeat_v>]


- |void| **set_repeat_v**\ (\ value\: [SamplerRepeatMode<enum_RenderingDevice_SamplerRepeatMode>]\ )
- [SamplerRepeatMode<enum_RenderingDevice_SamplerRepeatMode>] **get_repeat_v**\ (\ )

The repeat mode to use along the V axis of UV coordinates. This affects the returned values if sampling outside the UV bounds.


----



[SamplerRepeatMode<enum_RenderingDevice_SamplerRepeatMode>] **repeat_w** = `2` [🔗<class_RDSamplerState_property_repeat_w>]


- |void| **set_repeat_w**\ (\ value\: [SamplerRepeatMode<enum_RenderingDevice_SamplerRepeatMode>]\ )
- [SamplerRepeatMode<enum_RenderingDevice_SamplerRepeatMode>] **get_repeat_w**\ (\ )

The repeat mode to use along the W axis of UV coordinates. This affects the returned values if sampling outside the UV bounds. Only effective for 3D samplers.


----



[bool<class_bool>] **unnormalized_uvw** = `false` [🔗<class_RDSamplerState_property_unnormalized_uvw>]


- |void| **set_unnormalized_uvw**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_unnormalized_uvw**\ (\ )

If `true`, the texture will be sampled with coordinates ranging from 0 to the texture's resolution. Otherwise, the coordinates will be normalized and range from 0 to 1.


----



[bool<class_bool>] **use_anisotropy** = `false` [🔗<class_RDSamplerState_property_use_anisotropy>]


- |void| **set_use_anisotropy**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_use_anisotropy**\ (\ )

If `true`, perform anisotropic sampling. See [anisotropy_max<class_RDSamplerState_property_anisotropy_max>].

