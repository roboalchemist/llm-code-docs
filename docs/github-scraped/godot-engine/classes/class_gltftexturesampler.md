:github_url: hide



# GLTFTextureSampler

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Represents a glTF texture sampler


## Description

Represents a texture sampler as defined by the base glTF spec. Texture samplers in glTF specify how to sample data from the texture's base image, when rendering the texture on an object.


## Tutorials

- [../tutorials/io/runtime_file_loading_and_saving](Runtime file loading and saving .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------+-----------------------------------------------------------------+-----------+
> | :ref:`int<class_int>` | :ref:`mag_filter<class_GLTFTextureSampler_property_mag_filter>` | ``9729``  |
> +-----------------------+-----------------------------------------------------------------+-----------+
> | :ref:`int<class_int>` | :ref:`min_filter<class_GLTFTextureSampler_property_min_filter>` | ``9987``  |
> +-----------------------+-----------------------------------------------------------------+-----------+
> | :ref:`int<class_int>` | :ref:`wrap_s<class_GLTFTextureSampler_property_wrap_s>`         | ``10497`` |
> +-----------------------+-----------------------------------------------------------------+-----------+
> | :ref:`int<class_int>` | :ref:`wrap_t<class_GLTFTextureSampler_property_wrap_t>`         | ``10497`` |
> +-----------------------+-----------------------------------------------------------------+-----------+
>

----


## Property Descriptions



[int<class_int>] **mag_filter** = `9729` [🔗<class_GLTFTextureSampler_property_mag_filter>]


- |void| **set_mag_filter**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_mag_filter**\ (\ )

Texture's magnification filter, used when texture appears larger on screen than the source image.


----



[int<class_int>] **min_filter** = `9987` [🔗<class_GLTFTextureSampler_property_min_filter>]


- |void| **set_min_filter**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_min_filter**\ (\ )

Texture's minification filter, used when the texture appears smaller on screen than the source image.


----



[int<class_int>] **wrap_s** = `10497` [🔗<class_GLTFTextureSampler_property_wrap_s>]


- |void| **set_wrap_s**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_wrap_s**\ (\ )

Wrapping mode to use for S-axis (horizontal) texture coordinates.


----



[int<class_int>] **wrap_t** = `10497` [🔗<class_GLTFTextureSampler_property_wrap_t>]


- |void| **set_wrap_t**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_wrap_t**\ (\ )

Wrapping mode to use for T-axis (vertical) texture coordinates.

