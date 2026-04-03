:github_url: hide



# OpenXRCompositionLayerEquirect

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRCompositionLayer<class_OpenXRCompositionLayer>] **<** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

An OpenXR composition layer that is rendered as an internal slice of a sphere.


## Description

An OpenXR composition layer that allows rendering a [SubViewport<class_SubViewport>] on an internal slice of a sphere.


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+---------------------------------------------------------------------------------------------------------+---------------+
> | :ref:`float<class_float>` | :ref:`central_horizontal_angle<class_OpenXRCompositionLayerEquirect_property_central_horizontal_angle>` | ``1.5707964`` |
> +---------------------------+---------------------------------------------------------------------------------------------------------+---------------+
> | :ref:`int<class_int>`     | :ref:`fallback_segments<class_OpenXRCompositionLayerEquirect_property_fallback_segments>`               | ``10``        |
> +---------------------------+---------------------------------------------------------------------------------------------------------+---------------+
> | :ref:`float<class_float>` | :ref:`lower_vertical_angle<class_OpenXRCompositionLayerEquirect_property_lower_vertical_angle>`         | ``0.7853982`` |
> +---------------------------+---------------------------------------------------------------------------------------------------------+---------------+
> | :ref:`float<class_float>` | :ref:`radius<class_OpenXRCompositionLayerEquirect_property_radius>`                                     | ``1.0``       |
> +---------------------------+---------------------------------------------------------------------------------------------------------+---------------+
> | :ref:`float<class_float>` | :ref:`upper_vertical_angle<class_OpenXRCompositionLayerEquirect_property_upper_vertical_angle>`         | ``0.7853982`` |
> +---------------------------+---------------------------------------------------------------------------------------------------------+---------------+
>

----


## Property Descriptions



[float<class_float>] **central_horizontal_angle** = `1.5707964` [🔗<class_OpenXRCompositionLayerEquirect_property_central_horizontal_angle>]


- |void| **set_central_horizontal_angle**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_central_horizontal_angle**\ (\ )

The central horizontal angle of the sphere. Used to set the width.


----



[int<class_int>] **fallback_segments** = `10` [🔗<class_OpenXRCompositionLayerEquirect_property_fallback_segments>]


- |void| **set_fallback_segments**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_fallback_segments**\ (\ )

The number of segments to use in the fallback mesh.


----



[float<class_float>] **lower_vertical_angle** = `0.7853982` [🔗<class_OpenXRCompositionLayerEquirect_property_lower_vertical_angle>]


- |void| **set_lower_vertical_angle**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_lower_vertical_angle**\ (\ )

The lower vertical angle of the sphere. Used (together with [upper_vertical_angle<class_OpenXRCompositionLayerEquirect_property_upper_vertical_angle>]) to set the height.


----



[float<class_float>] **radius** = `1.0` [🔗<class_OpenXRCompositionLayerEquirect_property_radius>]


- |void| **set_radius**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_radius**\ (\ )

The radius of the sphere.


----



[float<class_float>] **upper_vertical_angle** = `0.7853982` [🔗<class_OpenXRCompositionLayerEquirect_property_upper_vertical_angle>]


- |void| **set_upper_vertical_angle**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_upper_vertical_angle**\ (\ )

The upper vertical angle of the sphere. Used (together with [lower_vertical_angle<class_OpenXRCompositionLayerEquirect_property_lower_vertical_angle>]) to set the height.

