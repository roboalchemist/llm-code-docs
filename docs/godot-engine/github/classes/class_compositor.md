:github_url: hide



# Compositor

**Experimental:** More customization of the rendering pipeline will be added in the future.

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Stores attributes used to customize how a Viewport is rendered.


## Description

The compositor resource stores attributes used to customize how a [Viewport<class_Viewport>] is rendered.


## Tutorials

- [../tutorials/rendering/compositor](The Compositor .md)


## Properties

> **TABLE**
> :widths: auto
>
> +------------------------------------------------------------------------------+-------------------------------------------------------------------------+--------+
> | :ref:`Array<class_Array>`\[:ref:`CompositorEffect<class_CompositorEffect>`\] | :ref:`compositor_effects<class_Compositor_property_compositor_effects>` | ``[]`` |
> +------------------------------------------------------------------------------+-------------------------------------------------------------------------+--------+
>

----


## Property Descriptions



[Array<class_Array>]\[[CompositorEffect<class_CompositorEffect>]\] **compositor_effects** = `[]` [🔗<class_Compositor_property_compositor_effects>]


- |void| **set_compositor_effects**\ (\ value\: [Array<class_Array>]\[[CompositorEffect<class_CompositorEffect>]\]\ )
- [Array<class_Array>]\[[CompositorEffect<class_CompositorEffect>]\] **get_compositor_effects**\ (\ )

The custom [CompositorEffect<class_CompositorEffect>]\ s that are applied during rendering of viewports using this compositor.

