# ImageTexture in English

# ImageTexture
Inherits:Texture2D<Texture<Resource<RefCounted<Object
ATexture2Dbased on anImage.

## Description
ATexture2Dbased on anImage. For an image to be displayed, anImageTexturehas to be created from it using thecreate_from_image()method:
```
var image = Image.load_from_file("res://icon.svg")
var texture = ImageTexture.create_from_image(image)
$Sprite2D.texture = texture
```
This way, textures can be created at run-time by loading images both from within the editor and externally.
Warning:Prefer to load imported textures with@GDScript.load()over loading them from within the filesystem dynamically withImage.load(), as it may not work in exported projects:
```
var texture = load("res://icon.svg")
$Sprite2D.texture = texture
```
This is because images have to be imported as aCompressedTexture2Dfirst to be loaded with@GDScript.load(). If you'd still like to load an image file just like any otherResource, import it as anImageresource instead, and then load it normally using the@GDScript.load()method.
Note:The image can be retrieved from an imported texture using theTexture2D.get_image()method, which returns a copy of the image:
```
var texture = load("res://icon.svg")
var image = texture.get_image()
```
AnImageTextureis not meant to be operated from within the editor interface directly, and is mostly useful for rendering images on screen dynamically via code. If you need to generate images procedurally from within the editor, consider saving and importing images as custom texture resources implementing a newEditorImportPlugin.
Note:The maximum texture size is 16384×16384 pixels due to graphics hardware limitations.

## Tutorials
- Importing images
Importing images

## Properties

| bool | resource_local_to_scene | false(overridesResource) |

bool
resource_local_to_scene
false(overridesResource)

## Methods

| ImageTexture | create_from_image(image:Image)static |
|---|---|
| Format | get_format()const |
| void | set_image(image:Image) |
| void | set_size_override(size:Vector2i) |
| void | update(image:Image) |

ImageTexture
create_from_image(image:Image)static
Format
get_format()const
void
set_image(image:Image)
void
set_size_override(size:Vector2i)
void
update(image:Image)

## Method Descriptions
ImageTexturecreate_from_image(image:Image)static🔗
Creates a newImageTextureand initializes it by allocating and setting the data from anImage.
Formatget_format()const🔗
Returns the format of the texture.
voidset_image(image:Image)🔗
Replaces the texture's data with a newImage. This will re-allocate new memory for the texture.
If you want to update the image, but don't need to change its parameters (format, size), useupdate()instead for better performance.
voidset_size_override(size:Vector2i)🔗
Resizes the texture to the specified dimensions.
voidupdate(image:Image)🔗
Replaces the texture's data with a newImage.
Note:The texture has to be created usingcreate_from_image()or initialized first with theset_image()method before it can be updated. The new image dimensions, format, and mipmaps configuration should match the existing texture's image configuration.
Use this method overset_image()if you need to update the texture frequently, which is faster than allocating additional memory for a new texture each time.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.