:github_url: hide



# CompressedTexture3D

**Inherits:** [Texture3D<class_Texture3D>] **<** [Texture<class_Texture>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Texture with 3 dimensions, optionally compressed.


## Description

**CompressedTexture3D** is the VRAM-compressed counterpart of [ImageTexture3D<class_ImageTexture3D>]. The file extension for **CompressedTexture3D** files is `.ctex3d`. This file format is internal to Godot; it is created by importing other image formats with the import system.

\ **CompressedTexture3D** uses VRAM compression, which allows to reduce memory usage on the GPU when rendering the texture. This also improves loading times, as VRAM-compressed textures are faster to load compared to textures using lossless compression. VRAM compression can exhibit noticeable artifacts and is intended to be used for 3D rendering, not 2D.

See [Texture3D<class_Texture3D>] for a general description of 3D textures.


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------+----------------------------------------------------------------+--------+
> | :ref:`String<class_String>` | :ref:`load_path<class_CompressedTexture3D_property_load_path>` | ``""`` |
> +-----------------------------+----------------------------------------------------------------+--------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------+----------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>` | :ref:`load<class_CompressedTexture3D_method_load>`\ (\ path\: :ref:`String<class_String>`\ ) |
> +---------------------------------------+----------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[String<class_String>] **load_path** = `""` [🔗<class_CompressedTexture3D_property_load_path>]


- [Error<enum_@GlobalScope_Error>] **load**\ (\ path\: [String<class_String>]\ )
- [String<class_String>] **get_load_path**\ (\ )

The **CompressedTexture3D**'s file path to a `.ctex3d` file.


----


## Method Descriptions



[Error<enum_@GlobalScope_Error>] **load**\ (\ path\: [String<class_String>]\ ) [🔗<class_CompressedTexture3D_method_load>]

Loads the texture from the specified `path`.

