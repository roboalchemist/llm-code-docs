:github_url: hide



# RDPipelineDepthStencilState

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Pipeline depth/stencil state (used by [RenderingDevice<class_RenderingDevice>]).


## Description

**RDPipelineDepthStencilState** controls the way depth and stencil comparisons are performed when sampling those values using [RenderingDevice<class_RenderingDevice>].


## Properties

> **TABLE**
> :widths: auto
>
> +----------------------------------------------------------------+--------------------------------------------------------------------------------------------------+-----------+
> | :ref:`CompareOperator<enum_RenderingDevice_CompareOperator>`   | :ref:`back_op_compare<class_RDPipelineDepthStencilState_property_back_op_compare>`               | ``7``     |
> +----------------------------------------------------------------+--------------------------------------------------------------------------------------------------+-----------+
> | :ref:`int<class_int>`                                          | :ref:`back_op_compare_mask<class_RDPipelineDepthStencilState_property_back_op_compare_mask>`     | ``0``     |
> +----------------------------------------------------------------+--------------------------------------------------------------------------------------------------+-----------+
> | :ref:`StencilOperation<enum_RenderingDevice_StencilOperation>` | :ref:`back_op_depth_fail<class_RDPipelineDepthStencilState_property_back_op_depth_fail>`         | ``1``     |
> +----------------------------------------------------------------+--------------------------------------------------------------------------------------------------+-----------+
> | :ref:`StencilOperation<enum_RenderingDevice_StencilOperation>` | :ref:`back_op_fail<class_RDPipelineDepthStencilState_property_back_op_fail>`                     | ``1``     |
> +----------------------------------------------------------------+--------------------------------------------------------------------------------------------------+-----------+
> | :ref:`StencilOperation<enum_RenderingDevice_StencilOperation>` | :ref:`back_op_pass<class_RDPipelineDepthStencilState_property_back_op_pass>`                     | ``1``     |
> +----------------------------------------------------------------+--------------------------------------------------------------------------------------------------+-----------+
> | :ref:`int<class_int>`                                          | :ref:`back_op_reference<class_RDPipelineDepthStencilState_property_back_op_reference>`           | ``0``     |
> +----------------------------------------------------------------+--------------------------------------------------------------------------------------------------+-----------+
> | :ref:`int<class_int>`                                          | :ref:`back_op_write_mask<class_RDPipelineDepthStencilState_property_back_op_write_mask>`         | ``0``     |
> +----------------------------------------------------------------+--------------------------------------------------------------------------------------------------+-----------+
> | :ref:`CompareOperator<enum_RenderingDevice_CompareOperator>`   | :ref:`depth_compare_operator<class_RDPipelineDepthStencilState_property_depth_compare_operator>` | ``7``     |
> +----------------------------------------------------------------+--------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>`                                      | :ref:`depth_range_max<class_RDPipelineDepthStencilState_property_depth_range_max>`               | ``0.0``   |
> +----------------------------------------------------------------+--------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>`                                      | :ref:`depth_range_min<class_RDPipelineDepthStencilState_property_depth_range_min>`               | ``0.0``   |
> +----------------------------------------------------------------+--------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                                        | :ref:`enable_depth_range<class_RDPipelineDepthStencilState_property_enable_depth_range>`         | ``false`` |
> +----------------------------------------------------------------+--------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                                        | :ref:`enable_depth_test<class_RDPipelineDepthStencilState_property_enable_depth_test>`           | ``false`` |
> +----------------------------------------------------------------+--------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                                        | :ref:`enable_depth_write<class_RDPipelineDepthStencilState_property_enable_depth_write>`         | ``false`` |
> +----------------------------------------------------------------+--------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                                        | :ref:`enable_stencil<class_RDPipelineDepthStencilState_property_enable_stencil>`                 | ``false`` |
> +----------------------------------------------------------------+--------------------------------------------------------------------------------------------------+-----------+
> | :ref:`CompareOperator<enum_RenderingDevice_CompareOperator>`   | :ref:`front_op_compare<class_RDPipelineDepthStencilState_property_front_op_compare>`             | ``7``     |
> +----------------------------------------------------------------+--------------------------------------------------------------------------------------------------+-----------+
> | :ref:`int<class_int>`                                          | :ref:`front_op_compare_mask<class_RDPipelineDepthStencilState_property_front_op_compare_mask>`   | ``0``     |
> +----------------------------------------------------------------+--------------------------------------------------------------------------------------------------+-----------+
> | :ref:`StencilOperation<enum_RenderingDevice_StencilOperation>` | :ref:`front_op_depth_fail<class_RDPipelineDepthStencilState_property_front_op_depth_fail>`       | ``1``     |
> +----------------------------------------------------------------+--------------------------------------------------------------------------------------------------+-----------+
> | :ref:`StencilOperation<enum_RenderingDevice_StencilOperation>` | :ref:`front_op_fail<class_RDPipelineDepthStencilState_property_front_op_fail>`                   | ``1``     |
> +----------------------------------------------------------------+--------------------------------------------------------------------------------------------------+-----------+
> | :ref:`StencilOperation<enum_RenderingDevice_StencilOperation>` | :ref:`front_op_pass<class_RDPipelineDepthStencilState_property_front_op_pass>`                   | ``1``     |
> +----------------------------------------------------------------+--------------------------------------------------------------------------------------------------+-----------+
> | :ref:`int<class_int>`                                          | :ref:`front_op_reference<class_RDPipelineDepthStencilState_property_front_op_reference>`         | ``0``     |
> +----------------------------------------------------------------+--------------------------------------------------------------------------------------------------+-----------+
> | :ref:`int<class_int>`                                          | :ref:`front_op_write_mask<class_RDPipelineDepthStencilState_property_front_op_write_mask>`       | ``0``     |
> +----------------------------------------------------------------+--------------------------------------------------------------------------------------------------+-----------+
>

----


## Property Descriptions



[CompareOperator<enum_RenderingDevice_CompareOperator>] **back_op_compare** = `7` [🔗<class_RDPipelineDepthStencilState_property_back_op_compare>]


- |void| **set_back_op_compare**\ (\ value\: [CompareOperator<enum_RenderingDevice_CompareOperator>]\ )
- [CompareOperator<enum_RenderingDevice_CompareOperator>] **get_back_op_compare**\ (\ )

The method used for comparing the previous back stencil value and [back_op_reference<class_RDPipelineDepthStencilState_property_back_op_reference>].


----



[int<class_int>] **back_op_compare_mask** = `0` [🔗<class_RDPipelineDepthStencilState_property_back_op_compare_mask>]


- |void| **set_back_op_compare_mask**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_back_op_compare_mask**\ (\ )

Selects which bits from the back stencil value will be compared.


----



[StencilOperation<enum_RenderingDevice_StencilOperation>] **back_op_depth_fail** = `1` [🔗<class_RDPipelineDepthStencilState_property_back_op_depth_fail>]


- |void| **set_back_op_depth_fail**\ (\ value\: [StencilOperation<enum_RenderingDevice_StencilOperation>]\ )
- [StencilOperation<enum_RenderingDevice_StencilOperation>] **get_back_op_depth_fail**\ (\ )

The operation to perform on the stencil buffer for back pixels that pass the stencil test but fail the depth test.


----



[StencilOperation<enum_RenderingDevice_StencilOperation>] **back_op_fail** = `1` [🔗<class_RDPipelineDepthStencilState_property_back_op_fail>]


- |void| **set_back_op_fail**\ (\ value\: [StencilOperation<enum_RenderingDevice_StencilOperation>]\ )
- [StencilOperation<enum_RenderingDevice_StencilOperation>] **get_back_op_fail**\ (\ )

The operation to perform on the stencil buffer for back pixels that fail the stencil test.


----



[StencilOperation<enum_RenderingDevice_StencilOperation>] **back_op_pass** = `1` [🔗<class_RDPipelineDepthStencilState_property_back_op_pass>]


- |void| **set_back_op_pass**\ (\ value\: [StencilOperation<enum_RenderingDevice_StencilOperation>]\ )
- [StencilOperation<enum_RenderingDevice_StencilOperation>] **get_back_op_pass**\ (\ )

The operation to perform on the stencil buffer for back pixels that pass the stencil test.


----



[int<class_int>] **back_op_reference** = `0` [🔗<class_RDPipelineDepthStencilState_property_back_op_reference>]


- |void| **set_back_op_reference**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_back_op_reference**\ (\ )

The value the previous back stencil value will be compared to.


----



[int<class_int>] **back_op_write_mask** = `0` [🔗<class_RDPipelineDepthStencilState_property_back_op_write_mask>]


- |void| **set_back_op_write_mask**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_back_op_write_mask**\ (\ )

Selects which bits from the back stencil value will be changed.


----



[CompareOperator<enum_RenderingDevice_CompareOperator>] **depth_compare_operator** = `7` [🔗<class_RDPipelineDepthStencilState_property_depth_compare_operator>]


- |void| **set_depth_compare_operator**\ (\ value\: [CompareOperator<enum_RenderingDevice_CompareOperator>]\ )
- [CompareOperator<enum_RenderingDevice_CompareOperator>] **get_depth_compare_operator**\ (\ )

The method used for comparing the previous and current depth values.


----



[float<class_float>] **depth_range_max** = `0.0` [🔗<class_RDPipelineDepthStencilState_property_depth_range_max>]


- |void| **set_depth_range_max**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_depth_range_max**\ (\ )

The maximum depth that returns `true` for [enable_depth_range<class_RDPipelineDepthStencilState_property_enable_depth_range>].


----



[float<class_float>] **depth_range_min** = `0.0` [🔗<class_RDPipelineDepthStencilState_property_depth_range_min>]


- |void| **set_depth_range_min**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_depth_range_min**\ (\ )

The minimum depth that returns `true` for [enable_depth_range<class_RDPipelineDepthStencilState_property_enable_depth_range>].


----



[bool<class_bool>] **enable_depth_range** = `false` [🔗<class_RDPipelineDepthStencilState_property_enable_depth_range>]


- |void| **set_enable_depth_range**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_enable_depth_range**\ (\ )

If `true`, each depth value will be tested to see if it is between [depth_range_min<class_RDPipelineDepthStencilState_property_depth_range_min>] and [depth_range_max<class_RDPipelineDepthStencilState_property_depth_range_max>]. If it is outside of these values, it is discarded.


----



[bool<class_bool>] **enable_depth_test** = `false` [🔗<class_RDPipelineDepthStencilState_property_enable_depth_test>]


- |void| **set_enable_depth_test**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_enable_depth_test**\ (\ )

If `true`, enables depth testing which allows objects to be automatically occluded by other objects based on their depth. This also allows objects to be partially occluded by other objects. If `false`, objects will appear in the order they were drawn (like in Godot's 2D renderer).


----



[bool<class_bool>] **enable_depth_write** = `false` [🔗<class_RDPipelineDepthStencilState_property_enable_depth_write>]


- |void| **set_enable_depth_write**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_enable_depth_write**\ (\ )

If `true`, writes to the depth buffer whenever the depth test returns `true`. Only works when enable_depth_test is also `true`.


----



[bool<class_bool>] **enable_stencil** = `false` [🔗<class_RDPipelineDepthStencilState_property_enable_stencil>]


- |void| **set_enable_stencil**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_enable_stencil**\ (\ )

If `true`, enables stencil testing. There are separate stencil buffers for front-facing triangles and back-facing triangles. See properties that begin with "front_op" and properties with "back_op" for each.


----



[CompareOperator<enum_RenderingDevice_CompareOperator>] **front_op_compare** = `7` [🔗<class_RDPipelineDepthStencilState_property_front_op_compare>]


- |void| **set_front_op_compare**\ (\ value\: [CompareOperator<enum_RenderingDevice_CompareOperator>]\ )
- [CompareOperator<enum_RenderingDevice_CompareOperator>] **get_front_op_compare**\ (\ )

The method used for comparing the previous front stencil value and [front_op_reference<class_RDPipelineDepthStencilState_property_front_op_reference>].


----



[int<class_int>] **front_op_compare_mask** = `0` [🔗<class_RDPipelineDepthStencilState_property_front_op_compare_mask>]


- |void| **set_front_op_compare_mask**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_front_op_compare_mask**\ (\ )

Selects which bits from the front stencil value will be compared.


----



[StencilOperation<enum_RenderingDevice_StencilOperation>] **front_op_depth_fail** = `1` [🔗<class_RDPipelineDepthStencilState_property_front_op_depth_fail>]


- |void| **set_front_op_depth_fail**\ (\ value\: [StencilOperation<enum_RenderingDevice_StencilOperation>]\ )
- [StencilOperation<enum_RenderingDevice_StencilOperation>] **get_front_op_depth_fail**\ (\ )

The operation to perform on the stencil buffer for front pixels that pass the stencil test but fail the depth test.


----



[StencilOperation<enum_RenderingDevice_StencilOperation>] **front_op_fail** = `1` [🔗<class_RDPipelineDepthStencilState_property_front_op_fail>]


- |void| **set_front_op_fail**\ (\ value\: [StencilOperation<enum_RenderingDevice_StencilOperation>]\ )
- [StencilOperation<enum_RenderingDevice_StencilOperation>] **get_front_op_fail**\ (\ )

The operation to perform on the stencil buffer for front pixels that fail the stencil test.


----



[StencilOperation<enum_RenderingDevice_StencilOperation>] **front_op_pass** = `1` [🔗<class_RDPipelineDepthStencilState_property_front_op_pass>]


- |void| **set_front_op_pass**\ (\ value\: [StencilOperation<enum_RenderingDevice_StencilOperation>]\ )
- [StencilOperation<enum_RenderingDevice_StencilOperation>] **get_front_op_pass**\ (\ )

The operation to perform on the stencil buffer for front pixels that pass the stencil test.


----



[int<class_int>] **front_op_reference** = `0` [🔗<class_RDPipelineDepthStencilState_property_front_op_reference>]


- |void| **set_front_op_reference**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_front_op_reference**\ (\ )

The value the previous front stencil value will be compared to.


----



[int<class_int>] **front_op_write_mask** = `0` [🔗<class_RDPipelineDepthStencilState_property_front_op_write_mask>]


- |void| **set_front_op_write_mask**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_front_op_write_mask**\ (\ )

Selects which bits from the front stencil value will be changed.

