:github_url: hide



# ImageTextureLayered

**Inherits:** [TextureLayered<class_TextureLayered>] **<** [Texture<class_Texture>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [Cubemap<class_Cubemap>], [CubemapArray<class_CubemapArray>], [Texture2DArray<class_Texture2DArray>]

Base class for texture types which contain the data of multiple [ImageTexture<class_ImageTexture>]\ s. Each image is of the same size and format.


## Description

Base class for [Texture2DArray<class_Texture2DArray>], [Cubemap<class_Cubemap>] and [CubemapArray<class_CubemapArray>]. Cannot be used directly, but contains all the functions necessary for accessing the derived resource types. See also [Texture3D<class_Texture3D>].


## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>` | :ref:`create_from_images<class_ImageTextureLayered_method_create_from_images>`\ (\ images\: :ref:`Array<class_Array>`\[:ref:`Image<class_Image>`\]\ ) |
> +---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                | :ref:`update_layer<class_ImageTextureLayered_method_update_layer>`\ (\ image\: :ref:`Image<class_Image>`, layer\: :ref:`int<class_int>`\ )            |
> +---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[Error<enum_@GlobalScope_Error>] **create_from_images**\ (\ images\: [Array<class_Array>]\[[Image<class_Image>]\]\ ) [🔗<class_ImageTextureLayered_method_create_from_images>]

Creates an **ImageTextureLayered** from an array of [Image<class_Image>]\ s. See [Image.create()<class_Image_method_create>] for the expected data format. The first image decides the width, height, image format and mipmapping setting. The other images *must* have the same width, height, image format and mipmapping setting.

Each [Image<class_Image>] represents one `layer`.

::

    # Fill in an array of Images with different colors.
    var images = []
    const LAYERS = 6
    for i in LAYERS:
        var image = Image.create_empty(128, 128, false, Image.FORMAT_RGB8)
        if i % 3 == 0:
            image.fill(Color.RED)
        elif i % 3 == 1:
            image.fill(Color.GREEN)
        else:
            image.fill(Color.BLUE)
        images.push_back(image)

    # Create and save a 2D texture array. The array of images must have at least 1 Image.
    var texture_2d_array = Texture2DArray.new()
    texture_2d_array.create_from_images(images)
    ResourceSaver.save(texture_2d_array, "res://texture_2d_array.res", ResourceSaver.FLAG_COMPRESS)

    # Create and save a cubemap. The array of images must have exactly 6 Images.
    # The cubemap's images are specified in this order: X+, X-, Y+, Y-, Z+, Z-
    # (in Godot's coordinate system, so Y+ is "up" and Z- is "forward").
    var cubemap = Cubemap.new()
    cubemap.create_from_images(images)
    ResourceSaver.save(cubemap, "res://cubemap.res", ResourceSaver.FLAG_COMPRESS)

    # Create and save a cubemap array. The array of images must have a multiple of 6 Images.
    # Each cubemap's images are specified in this order: X+, X-, Y+, Y-, Z+, Z-
    # (in Godot's coordinate system, so Y+ is "up" and Z- is "forward").
    var cubemap_array = CubemapArray.new()
    cubemap_array.create_from_images(images)
    ResourceSaver.save(cubemap_array, "res://cubemap_array.res", ResourceSaver.FLAG_COMPRESS)


----



|void| **update_layer**\ (\ image\: [Image<class_Image>], layer\: [int<class_int>]\ ) [🔗<class_ImageTextureLayered_method_update_layer>]

Replaces the existing [Image<class_Image>] data at the given `layer` with this new image.

The given [Image<class_Image>] must have the same width, height, image format, and mipmapping flag as the rest of the referenced images.

If the image format is unsupported, it will be decompressed and converted to a similar and supported [Format<enum_Image_Format>].

The update is immediate: it's synchronized with drawing.

