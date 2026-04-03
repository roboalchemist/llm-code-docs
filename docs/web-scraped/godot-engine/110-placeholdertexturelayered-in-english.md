# PlaceholderTextureLayered in English

# PlaceholderTextureLayered
Inherits:TextureLayered<Texture<Resource<RefCounted<Object
Inherited By:PlaceholderCubemap,PlaceholderCubemapArray,PlaceholderTexture2DArray
Placeholder class for a 2-dimensional texture array.

## Description
This class is used when loading a project that uses aTextureLayeredsubclass in 2 conditions:
- When running the project exported in dedicated server mode, only the texture's dimensions are kept (as they may be relied upon for gameplay purposes or positioning of other elements). This allows reducing the exported PCK's size significantly.
When running the project exported in dedicated server mode, only the texture's dimensions are kept (as they may be relied upon for gameplay purposes or positioning of other elements). This allows reducing the exported PCK's size significantly.
- When this subclass is missing due to using a different engine version or build (e.g. modules disabled).
When this subclass is missing due to using a different engine version or build (e.g. modules disabled).
Note:This is not intended to be used as an actual texture for rendering. It is not guaranteed to work like one in shaders or materials (for example when calculating UV).

## Properties

| int | layers | 1 |
|---|---|---|
| Vector2i | size | Vector2i(1,1) |

layers
Vector2i
size
Vector2i(1,1)

## Property Descriptions
intlayers=1🔗
- voidset_layers(value:int)
voidset_layers(value:int)
- intget_layers()
intget_layers()
The number of layers in the texture array.
Vector2isize=Vector2i(1,1)🔗
- voidset_size(value:Vector2i)
voidset_size(value:Vector2i)
- Vector2iget_size()
Vector2iget_size()
The size of each texture layer (in pixels).

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.