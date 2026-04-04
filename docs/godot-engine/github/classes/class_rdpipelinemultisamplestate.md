:github_url: hide



# RDPipelineMultisampleState

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Pipeline multisample state (used by [RenderingDevice<class_RenderingDevice>]).


## Description

**RDPipelineMultisampleState** is used to control how multisample or supersample antialiasing is being performed when rendering using [RenderingDevice<class_RenderingDevice>].


## Properties

> **TABLE**
> :widths: auto
>
> +------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                                    | :ref:`enable_alpha_to_coverage<class_RDPipelineMultisampleState_property_enable_alpha_to_coverage>` | ``false`` |
> +------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                                    | :ref:`enable_alpha_to_one<class_RDPipelineMultisampleState_property_enable_alpha_to_one>`           | ``false`` |
> +------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                                    | :ref:`enable_sample_shading<class_RDPipelineMultisampleState_property_enable_sample_shading>`       | ``false`` |
> +------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>`                                  | :ref:`min_sample_shading<class_RDPipelineMultisampleState_property_min_sample_shading>`             | ``0.0``   |
> +------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+-----------+
> | :ref:`TextureSamples<enum_RenderingDevice_TextureSamples>` | :ref:`sample_count<class_RDPipelineMultisampleState_property_sample_count>`                         | ``0``     |
> +------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+-----------+
> | :ref:`Array<class_Array>`\[:ref:`int<class_int>`\]         | :ref:`sample_masks<class_RDPipelineMultisampleState_property_sample_masks>`                         | ``[]``    |
> +------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+-----------+
>

----


## Property Descriptions



[bool<class_bool>] **enable_alpha_to_coverage** = `false` [🔗<class_RDPipelineMultisampleState_property_enable_alpha_to_coverage>]


- |void| **set_enable_alpha_to_coverage**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_enable_alpha_to_coverage**\ (\ )

If `true`, alpha to coverage is enabled. This generates a temporary coverage value based on the alpha component of the fragment's first color output. This allows alpha transparency to make use of multisample antialiasing.


----



[bool<class_bool>] **enable_alpha_to_one** = `false` [🔗<class_RDPipelineMultisampleState_property_enable_alpha_to_one>]


- |void| **set_enable_alpha_to_one**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_enable_alpha_to_one**\ (\ )

If `true`, alpha is forced to either `0.0` or `1.0`. This allows hardening the edges of antialiased alpha transparencies. Only relevant if [enable_alpha_to_coverage<class_RDPipelineMultisampleState_property_enable_alpha_to_coverage>] is `true`.


----



[bool<class_bool>] **enable_sample_shading** = `false` [🔗<class_RDPipelineMultisampleState_property_enable_sample_shading>]


- |void| **set_enable_sample_shading**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_enable_sample_shading**\ (\ )

If `true`, enables per-sample shading which replaces MSAA by SSAA. This provides higher quality antialiasing that works with transparent (alpha scissor) edges. This has a very high performance cost. See also [min_sample_shading<class_RDPipelineMultisampleState_property_min_sample_shading>]. See the [per-sample shading Vulkan documentation ](https://registry.khronos.org/vulkan/specs/1.3-extensions/html/vkspec.html#primsrast-sampleshading)_ for more details.


----



[float<class_float>] **min_sample_shading** = `0.0` [🔗<class_RDPipelineMultisampleState_property_min_sample_shading>]


- |void| **set_min_sample_shading**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_min_sample_shading**\ (\ )

The multiplier of [sample_count<class_RDPipelineMultisampleState_property_sample_count>] that determines how many samples are performed for each fragment. Must be between `0.0` and `1.0` (inclusive). Only effective if [enable_sample_shading<class_RDPipelineMultisampleState_property_enable_sample_shading>] is `true`. If [min_sample_shading<class_RDPipelineMultisampleState_property_min_sample_shading>] is `1.0`, fragment invocation must only read from the coverage index sample. Tile image access must not be used if [enable_sample_shading<class_RDPipelineMultisampleState_property_enable_sample_shading>] is *not* `1.0`.


----



[TextureSamples<enum_RenderingDevice_TextureSamples>] **sample_count** = `0` [🔗<class_RDPipelineMultisampleState_property_sample_count>]


- |void| **set_sample_count**\ (\ value\: [TextureSamples<enum_RenderingDevice_TextureSamples>]\ )
- [TextureSamples<enum_RenderingDevice_TextureSamples>] **get_sample_count**\ (\ )

The number of MSAA samples (or SSAA samples if [enable_sample_shading<class_RDPipelineMultisampleState_property_enable_sample_shading>] is `true`) to perform. Higher values result in better antialiasing, at the cost of performance.


----



[Array<class_Array>]\[[int<class_int>]\] **sample_masks** = `[]` [🔗<class_RDPipelineMultisampleState_property_sample_masks>]


- |void| **set_sample_masks**\ (\ value\: [Array<class_Array>]\[[int<class_int>]\]\ )
- [Array<class_Array>]\[[int<class_int>]\] **get_sample_masks**\ (\ )

The sample mask array. See the [sample mask Vulkan documentation ](https://registry.khronos.org/vulkan/specs/1.3-extensions/html/vkspec.html#fragops-samplemask)_ for more details.

