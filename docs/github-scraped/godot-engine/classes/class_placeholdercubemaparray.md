:github_url: hide



# PlaceholderCubemapArray

**Inherits:** [PlaceholderTextureLayered<class_PlaceholderTextureLayered>] **<** [TextureLayered<class_TextureLayered>] **<** [Texture<class_Texture>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A [CubemapArray<class_CubemapArray>] without image data.


## Description

This class replaces a [CubemapArray<class_CubemapArray>] or a [CubemapArray<class_CubemapArray>]-derived class in 2 conditions:

- In dedicated server mode, where the image data shouldn't affect game logic. This allows reducing the exported PCK's size significantly.

- When the [CubemapArray<class_CubemapArray>]-derived class is missing, for example when using a different engine version.

\ **Note:** This class is not intended for rendering or for use in shaders. Operations like calculating UV are not guaranteed to work.

