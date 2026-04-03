:github_url: hide



# OpenXRCompositionLayerCylinder

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRCompositionLayer<class_OpenXRCompositionLayer>] **<** [Node3D<class_Node3D>] **<** [Node<class_Node>] **<** [Object<class_Object>]

An OpenXR composition layer that is rendered as an internal slice of a cylinder.


## Description

An OpenXR composition layer that allows rendering a [SubViewport<class_SubViewport>] on an internal slice of a cylinder.


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+-------------------------------------------------------------------------------------------+---------------+
> | :ref:`float<class_float>` | :ref:`aspect_ratio<class_OpenXRCompositionLayerCylinder_property_aspect_ratio>`           | ``1.0``       |
> +---------------------------+-------------------------------------------------------------------------------------------+---------------+
> | :ref:`float<class_float>` | :ref:`central_angle<class_OpenXRCompositionLayerCylinder_property_central_angle>`         | ``1.5707964`` |
> +---------------------------+-------------------------------------------------------------------------------------------+---------------+
> | :ref:`int<class_int>`     | :ref:`fallback_segments<class_OpenXRCompositionLayerCylinder_property_fallback_segments>` | ``10``        |
> +---------------------------+-------------------------------------------------------------------------------------------+---------------+
> | :ref:`float<class_float>` | :ref:`radius<class_OpenXRCompositionLayerCylinder_property_radius>`                       | ``1.0``       |
> +---------------------------+-------------------------------------------------------------------------------------------+---------------+
>

----


## Property Descriptions



[float<class_float>] **aspect_ratio** = `1.0` [🔗<class_OpenXRCompositionLayerCylinder_property_aspect_ratio>]


- |void| **set_aspect_ratio**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_aspect_ratio**\ (\ )

The aspect ratio of the slice. Used to set the height relative to the width.


----



[float<class_float>] **central_angle** = `1.5707964` [🔗<class_OpenXRCompositionLayerCylinder_property_central_angle>]


- |void| **set_central_angle**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_central_angle**\ (\ )

The central angle of the cylinder. Used to set the width.


----



[int<class_int>] **fallback_segments** = `10` [🔗<class_OpenXRCompositionLayerCylinder_property_fallback_segments>]


- |void| **set_fallback_segments**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_fallback_segments**\ (\ )

The number of segments to use in the fallback mesh.


----



[float<class_float>] **radius** = `1.0` [🔗<class_OpenXRCompositionLayerCylinder_property_radius>]


- |void| **set_radius**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_radius**\ (\ )

The radius of the cylinder.

