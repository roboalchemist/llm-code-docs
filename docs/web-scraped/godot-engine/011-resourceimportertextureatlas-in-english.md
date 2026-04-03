# ResourceImporterTextureAtlas in English

# ResourceImporterTextureAtlas
Inherits:ResourceImporter<RefCounted<Object
Imports a collection of textures from a PNG image into an optimizedAtlasTexturefor 2D rendering.

## Description
This imports a collection of textures from a PNG image into anAtlasTextureor 2DArrayMesh. This can be used to save memory when importing 2D animations from spritesheets. Texture atlases are only supported in 2D rendering, not 3D. See alsoResourceImporterTextureandResourceImporterLayeredTexture.
Note:ResourceImporterTextureAtlasdoes not handle importingTileSetAtlasSource, which is created using theTileSeteditor instead.

## Properties

| String | atlas_file | "" |
|---|---|---|
| bool | crop_to_region | false |
| int | import_mode | 0 |
| bool | trim_alpha_border_from_region | true |

String
atlas_file
bool
crop_to_region
false
import_mode
bool
trim_alpha_border_from_region
true

## Property Descriptions
Stringatlas_file=""🔗
Path to the atlas spritesheet. Thismustbe set to valid path to a PNG image. Otherwise, the atlas will fail to import.
boolcrop_to_region=false🔗
Iftrue, discards empty areas from the atlas. This only affects final sprite positioning, not storage. See alsotrim_alpha_border_from_region.
Note:Only effective ifimport_modeisRegion.
intimport_mode=0🔗
Region:Imports the atlas in anAtlasTextureresource, which is rendered as a rectangle. This is fast to render, but transparent areas still have to be rendered if they can't be trimmed effectively bytrim_alpha_border_from_region. This can reduce performance when rendering large sprites on screen.
Mesh:Imports the atlas as anArrayMeshresource, keeping the original bitmap visible (but rendered as a polygon). This can be used to reduce fill rate when rendering large transparent sprites, at the cost of slower rendering if there are little to no transparent areas in the sprite.
booltrim_alpha_border_from_region=true🔗
Iftrue, trims the region to exclude fully transparent pixels using a clipping rectangle (which is never rotated). This can be used to save memory. See alsocrop_to_region.
Note:Only effective ifimport_modeisRegion.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.