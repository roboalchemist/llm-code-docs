# GLTFTexture in English

# GLTFTexture
Inherits:Resource<RefCounted<Object
GLTFTexture represents a texture in a glTF file.

## Tutorials
- Runtime file loading and saving
Runtime file loading and saving

## Properties

| int | sampler | -1 |
|---|---|---|
| int | src_image | -1 |

sampler
src_image

## Property Descriptions
intsampler=-1🔗
- voidset_sampler(value:int)
voidset_sampler(value:int)
- intget_sampler()
intget_sampler()
ID of the texture sampler to use when sampling the image. If -1, then the default texture sampler is used (linear filtering, and repeat wrapping in both axes).
intsrc_image=-1🔗
- voidset_src_image(value:int)
voidset_src_image(value:int)
- intget_src_image()
intget_src_image()
The index of the image associated with this texture, seeGLTFState.get_images(). If -1, then this texture does not have an image assigned.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.