# CompressedTextureLayered in English

# CompressedTextureLayered

Inherits:TextureLayered<Texture<Resource<RefCounted<Object
Inherited By:CompressedCubemap,CompressedCubemapArray,CompressedTexture2DArray
Base class for texture arrays that can optionally be compressed.

## Description

Base class forCompressedTexture2DArrayandCompressedTexture3D. Cannot be used directly, but contains all the functions necessary for accessing the derived resource types. See alsoTextureLayered.

## Properties

| String | load_path | "" |

String
load_path

## Methods

| Error | load(path:String) |

Error
load(path:String)

## Property Descriptions

Stringload_path=""🔗

- Errorload(path:String)
Errorload(path:String)
- Stringget_load_path()
Stringget_load_path()
The path the texture should be loaded from.

## Method Descriptions

Errorload(path:String)🔗
Loads the texture atpath.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
