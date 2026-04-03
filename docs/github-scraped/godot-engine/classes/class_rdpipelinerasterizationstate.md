:github_url: hide



# RDPipelineRasterizationState

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Pipeline rasterization state (used by [RenderingDevice<class_RenderingDevice>]).


## Description

This object is used by [RenderingDevice<class_RenderingDevice>].


## Properties

> **TABLE**
> :widths: auto
>
> +----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`PolygonCullMode<enum_RenderingDevice_PolygonCullMode>`   | :ref:`cull_mode<class_RDPipelineRasterizationState_property_cull_mode>`                                   | ``0``     |
> +----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>`                                      | :ref:`depth_bias_clamp<class_RDPipelineRasterizationState_property_depth_bias_clamp>`                     | ``0.0``   |
> +----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>`                                      | :ref:`depth_bias_constant_factor<class_RDPipelineRasterizationState_property_depth_bias_constant_factor>` | ``0.0``   |
> +----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                                        | :ref:`depth_bias_enabled<class_RDPipelineRasterizationState_property_depth_bias_enabled>`                 | ``false`` |
> +----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>`                                      | :ref:`depth_bias_slope_factor<class_RDPipelineRasterizationState_property_depth_bias_slope_factor>`       | ``0.0``   |
> +----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                                        | :ref:`discard_primitives<class_RDPipelineRasterizationState_property_discard_primitives>`                 | ``false`` |
> +----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                                        | :ref:`enable_depth_clamp<class_RDPipelineRasterizationState_property_enable_depth_clamp>`                 | ``false`` |
> +----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`PolygonFrontFace<enum_RenderingDevice_PolygonFrontFace>` | :ref:`front_face<class_RDPipelineRasterizationState_property_front_face>`                                 | ``0``     |
> +----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>`                                      | :ref:`line_width<class_RDPipelineRasterizationState_property_line_width>`                                 | ``1.0``   |
> +----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`int<class_int>`                                          | :ref:`patch_control_points<class_RDPipelineRasterizationState_property_patch_control_points>`             | ``1``     |
> +----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                                        | :ref:`wireframe<class_RDPipelineRasterizationState_property_wireframe>`                                   | ``false`` |
> +----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+-----------+
>

----


## Property Descriptions



[PolygonCullMode<enum_RenderingDevice_PolygonCullMode>] **cull_mode** = `0` [🔗<class_RDPipelineRasterizationState_property_cull_mode>]


- |void| **set_cull_mode**\ (\ value\: [PolygonCullMode<enum_RenderingDevice_PolygonCullMode>]\ )
- [PolygonCullMode<enum_RenderingDevice_PolygonCullMode>] **get_cull_mode**\ (\ )

The cull mode to use when drawing polygons, which determines whether front faces or backfaces are hidden.


----



[float<class_float>] **depth_bias_clamp** = `0.0` [🔗<class_RDPipelineRasterizationState_property_depth_bias_clamp>]


- |void| **set_depth_bias_clamp**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_depth_bias_clamp**\ (\ )

A limit for how much each depth value can be offset. If negative, it serves as a minimum value, but if positive, it serves as a maximum value.


----



[float<class_float>] **depth_bias_constant_factor** = `0.0` [🔗<class_RDPipelineRasterizationState_property_depth_bias_constant_factor>]


- |void| **set_depth_bias_constant_factor**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_depth_bias_constant_factor**\ (\ )

A constant offset added to each depth value. Applied after [depth_bias_slope_factor<class_RDPipelineRasterizationState_property_depth_bias_slope_factor>].


----



[bool<class_bool>] **depth_bias_enabled** = `false` [🔗<class_RDPipelineRasterizationState_property_depth_bias_enabled>]


- |void| **set_depth_bias_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_depth_bias_enabled**\ (\ )

If `true`, each generated depth value will by offset by some amount. The specific amount is generated per polygon based on the values of [depth_bias_slope_factor<class_RDPipelineRasterizationState_property_depth_bias_slope_factor>] and [depth_bias_constant_factor<class_RDPipelineRasterizationState_property_depth_bias_constant_factor>].


----



[float<class_float>] **depth_bias_slope_factor** = `0.0` [🔗<class_RDPipelineRasterizationState_property_depth_bias_slope_factor>]


- |void| **set_depth_bias_slope_factor**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_depth_bias_slope_factor**\ (\ )

A constant scale applied to the slope of each polygons' depth. Applied before [depth_bias_constant_factor<class_RDPipelineRasterizationState_property_depth_bias_constant_factor>].


----



[bool<class_bool>] **discard_primitives** = `false` [🔗<class_RDPipelineRasterizationState_property_discard_primitives>]


- |void| **set_discard_primitives**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_discard_primitives**\ (\ )

If `true`, primitives are discarded immediately before the rasterization stage.


----



[bool<class_bool>] **enable_depth_clamp** = `false` [🔗<class_RDPipelineRasterizationState_property_enable_depth_clamp>]


- |void| **set_enable_depth_clamp**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_enable_depth_clamp**\ (\ )

If `true`, clamps depth values according to the minimum and maximum depth of the associated viewport.


----



[PolygonFrontFace<enum_RenderingDevice_PolygonFrontFace>] **front_face** = `0` [🔗<class_RDPipelineRasterizationState_property_front_face>]


- |void| **set_front_face**\ (\ value\: [PolygonFrontFace<enum_RenderingDevice_PolygonFrontFace>]\ )
- [PolygonFrontFace<enum_RenderingDevice_PolygonFrontFace>] **get_front_face**\ (\ )

The winding order to use to determine which face of a triangle is considered its front face.


----



[float<class_float>] **line_width** = `1.0` [🔗<class_RDPipelineRasterizationState_property_line_width>]


- |void| **set_line_width**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_line_width**\ (\ )

The line width to use when drawing lines (in pixels). Thick lines may not be supported on all hardware.


----



[int<class_int>] **patch_control_points** = `1` [🔗<class_RDPipelineRasterizationState_property_patch_control_points>]


- |void| **set_patch_control_points**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_patch_control_points**\ (\ )

The number of control points to use when drawing a patch with tessellation enabled. Higher values result in higher quality at the cost of performance.


----



[bool<class_bool>] **wireframe** = `false` [🔗<class_RDPipelineRasterizationState_property_wireframe>]


- |void| **set_wireframe**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_wireframe**\ (\ )

If `true`, performs wireframe rendering for triangles instead of flat or textured rendering.

