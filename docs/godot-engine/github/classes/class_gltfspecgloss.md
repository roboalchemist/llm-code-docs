:github_url: hide



# GLTFSpecGloss

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Archived glTF extension for specular/glossy materials.


## Description

KHR_materials_pbrSpecularGlossiness is an archived glTF extension. This means that it is deprecated and not recommended for new files. However, it is still supported for loading old files.


## Tutorials

- [../tutorials/io/runtime_file_loading_and_saving](Runtime file loading and saving .md)

- [KHR_materials_pbrSpecularGlossiness glTF extension spec ](https://github.com/KhronosGroup/glTF/blob/main/extensions/2.0/Archived/KHR_materials_pbrSpecularGlossiness)_


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+----------------------------------------------------------------------+-----------------------+
> | :ref:`Color<class_Color>` | :ref:`diffuse_factor<class_GLTFSpecGloss_property_diffuse_factor>`   | ``Color(1, 1, 1, 1)`` |
> +---------------------------+----------------------------------------------------------------------+-----------------------+
> | :ref:`Image<class_Image>` | :ref:`diffuse_img<class_GLTFSpecGloss_property_diffuse_img>`         |                       |
> +---------------------------+----------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>` | :ref:`gloss_factor<class_GLTFSpecGloss_property_gloss_factor>`       | ``1.0``               |
> +---------------------------+----------------------------------------------------------------------+-----------------------+
> | :ref:`Image<class_Image>` | :ref:`spec_gloss_img<class_GLTFSpecGloss_property_spec_gloss_img>`   |                       |
> +---------------------------+----------------------------------------------------------------------+-----------------------+
> | :ref:`Color<class_Color>` | :ref:`specular_factor<class_GLTFSpecGloss_property_specular_factor>` | ``Color(1, 1, 1, 1)`` |
> +---------------------------+----------------------------------------------------------------------+-----------------------+
>

----


## Property Descriptions



[Color<class_Color>] **diffuse_factor** = `Color(1, 1, 1, 1)` [🔗<class_GLTFSpecGloss_property_diffuse_factor>]


- |void| **set_diffuse_factor**\ (\ value\: [Color<class_Color>]\ )
- [Color<class_Color>] **get_diffuse_factor**\ (\ )

The reflected diffuse factor of the material.


----



[Image<class_Image>] **diffuse_img** [🔗<class_GLTFSpecGloss_property_diffuse_img>]


- |void| **set_diffuse_img**\ (\ value\: [Image<class_Image>]\ )
- [Image<class_Image>] **get_diffuse_img**\ (\ )

The diffuse texture.


----



[float<class_float>] **gloss_factor** = `1.0` [🔗<class_GLTFSpecGloss_property_gloss_factor>]


- |void| **set_gloss_factor**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_gloss_factor**\ (\ )

The glossiness or smoothness of the material.


----



[Image<class_Image>] **spec_gloss_img** [🔗<class_GLTFSpecGloss_property_spec_gloss_img>]


- |void| **set_spec_gloss_img**\ (\ value\: [Image<class_Image>]\ )
- [Image<class_Image>] **get_spec_gloss_img**\ (\ )

The specular-glossiness texture.


----



[Color<class_Color>] **specular_factor** = `Color(1, 1, 1, 1)` [🔗<class_GLTFSpecGloss_property_specular_factor>]


- |void| **set_specular_factor**\ (\ value\: [Color<class_Color>]\ )
- [Color<class_Color>] **get_specular_factor**\ (\ )

The specular RGB color of the material. The alpha channel is unused.

