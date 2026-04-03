:github_url: hide



# UniformSetCacheRD

**Inherits:** [Object<class_Object>]

Uniform set cache manager for Rendering Device based renderers.


## Description

Uniform set cache manager for [RenderingDevice<class_RenderingDevice>]-based renderers. Provides a way to create a uniform set and reuse it in subsequent calls for as long as the uniform set exists. Uniform set will automatically be cleaned up when dependent objects are freed.


## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`RID<class_RID>` | :ref:`get_cache<class_UniformSetCacheRD_method_get_cache>`\ (\ shader\: :ref:`RID<class_RID>`, set\: :ref:`int<class_int>`, uniforms\: :ref:`Array<class_Array>`\[:ref:`RDUniform<class_RDUniform>`\]\ ) |static| |
> +-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[RID<class_RID>] **get_cache**\ (\ shader\: [RID<class_RID>], set\: [int<class_int>], uniforms\: [Array<class_Array>]\[[RDUniform<class_RDUniform>]\]\ ) |static| [🔗<class_UniformSetCacheRD_method_get_cache>]

Creates/returns a cached uniform set based on the provided uniforms for a given shader.

