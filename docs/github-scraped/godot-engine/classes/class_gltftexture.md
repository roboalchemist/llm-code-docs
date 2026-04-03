:github_url: hide



# GLTFTexture

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

GLTFTexture represents a texture in a glTF file.


## Tutorials

- [../tutorials/io/runtime_file_loading_and_saving](Runtime file loading and saving .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------+--------------------------------------------------------+--------+
> | :ref:`int<class_int>` | :ref:`sampler<class_GLTFTexture_property_sampler>`     | ``-1`` |
> +-----------------------+--------------------------------------------------------+--------+
> | :ref:`int<class_int>` | :ref:`src_image<class_GLTFTexture_property_src_image>` | ``-1`` |
> +-----------------------+--------------------------------------------------------+--------+
>

----


## Property Descriptions



[int<class_int>] **sampler** = `-1` [🔗<class_GLTFTexture_property_sampler>]


- |void| **set_sampler**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_sampler**\ (\ )

ID of the texture sampler to use when sampling the image. If -1, then the default texture sampler is used (linear filtering, and repeat wrapping in both axes).


----



[int<class_int>] **src_image** = `-1` [🔗<class_GLTFTexture_property_src_image>]


- |void| **set_src_image**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_src_image**\ (\ )

The index of the image associated with this texture, see [GLTFState.get_images()<class_GLTFState_method_get_images>]. If -1, then this texture does not have an image assigned.

