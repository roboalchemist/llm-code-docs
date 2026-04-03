# GLTFState in English

# GLTFState
Inherits:Resource<RefCounted<Object
Inherited By:FBXState
Represents all data of a glTF file.

## Description
Contains all nodes and resources of a glTF file. This is used byGLTFDocumentas data storage, which allowsGLTFDocumentand allGLTFDocumentExtensionclasses to remain stateless.
GLTFState can be populated byGLTFDocumentreading a file or by converting a Godot scene. Then the data can either be used to create a Godot scene or save to a glTF file. The code that converts to/from a Godot scene can be intercepted at arbitrary points byGLTFDocumentExtensionclasses. This allows for custom data to be stored in the glTF file or for custom data to be converted to/from Godot nodes.

## Tutorials
- Runtime file loading and saving
Runtime file loading and saving
- glTF asset header schema
glTF asset header schema

## Properties

| float | bake_fps | 30.0 |
|---|---|---|
| String | base_path | "" |
| Array[PackedByteArray] | buffers | [] |
| String | copyright | "" |
| bool | create_animations | true |
| String | filename | "" |
| PackedByteArray | glb_data | PackedByteArray() |
| HandleBinaryImageMode | handle_binary_image_mode | 1 |
| bool | import_as_skeleton_bones | false |
| Dictionary | json | {} |
| int | major_version | 0 |
| int | minor_version | 0 |
| PackedInt32Array | root_nodes | PackedInt32Array() |
| String | scene_name | "" |
| bool | use_named_skin_binds | false |

float
bake_fps
30.0
String
base_path
Array[PackedByteArray]
buffers
String
copyright
bool
create_animations
true
String
filename
PackedByteArray
glb_data
PackedByteArray()
HandleBinaryImageMode
handle_binary_image_mode
bool
import_as_skeleton_bones
false
Dictionary
json
major_version
minor_version
PackedInt32Array
root_nodes
PackedInt32Array()
String
scene_name
bool
use_named_skin_binds
false

## Methods

| void | add_used_extension(extension_name:String, required:bool) |
|---|---|
| int | append_data_to_buffers(data:PackedByteArray, deduplication:bool) |
| int | append_gltf_node(gltf_node:GLTFNode, godot_scene_node:Node, parent_node_index:int) |
| Array[GLTFAccessor] | get_accessors()const |
| Variant | get_additional_data(extension_name:StringName)const |
| AnimationPlayer | get_animation_player(anim_player_index:int)const |
| int | get_animation_players_count(anim_player_index:int)const |
| Array[GLTFAnimation] | get_animations()const |
| Array[GLTFBufferView] | get_buffer_views()const |
| Array[GLTFCamera] | get_cameras()const |
| int | get_handle_binary_image()const |
| Array[Texture2D] | get_images()const |
| Array[GLTFLight] | get_lights()const |
| Array[Material] | get_materials()const |
| Array[GLTFMesh] | get_meshes()const |
| int | get_node_index(scene_node:Node)const |
| Array[GLTFNode] | get_nodes()const |
| Node | get_scene_node(gltf_node_index:int)const |
| Array[GLTFSkeleton] | get_skeletons()const |
| Array[GLTFSkin] | get_skins()const |
| Array[GLTFTextureSampler] | get_texture_samplers()const |
| Array[GLTFTexture] | get_textures()const |
| Array[String] | get_unique_animation_names()const |
| Array[String] | get_unique_names()const |
| void | set_accessors(accessors:Array[GLTFAccessor]) |
| void | set_additional_data(extension_name:StringName, additional_data:Variant) |
| void | set_animations(animations:Array[GLTFAnimation]) |
| void | set_buffer_views(buffer_views:Array[GLTFBufferView]) |
| void | set_cameras(cameras:Array[GLTFCamera]) |
| void | set_handle_binary_image(method:int) |
| void | set_images(images:Array[Texture2D]) |
| void | set_lights(lights:Array[GLTFLight]) |
| void | set_materials(materials:Array[Material]) |
| void | set_meshes(meshes:Array[GLTFMesh]) |
| void | set_nodes(nodes:Array[GLTFNode]) |
| void | set_skeletons(skeletons:Array[GLTFSkeleton]) |
| void | set_skins(skins:Array[GLTFSkin]) |
| void | set_texture_samplers(texture_samplers:Array[GLTFTextureSampler]) |
| void | set_textures(textures:Array[GLTFTexture]) |
| void | set_unique_animation_names(unique_animation_names:Array[String]) |
| void | set_unique_names(unique_names:Array[String]) |

void
add_used_extension(extension_name:String, required:bool)
append_data_to_buffers(data:PackedByteArray, deduplication:bool)
append_gltf_node(gltf_node:GLTFNode, godot_scene_node:Node, parent_node_index:int)
Array[GLTFAccessor]
get_accessors()const
Variant
get_additional_data(extension_name:StringName)const
AnimationPlayer
get_animation_player(anim_player_index:int)const
get_animation_players_count(anim_player_index:int)const
Array[GLTFAnimation]
get_animations()const
Array[GLTFBufferView]
get_buffer_views()const
Array[GLTFCamera]
get_cameras()const
get_handle_binary_image()const
Array[Texture2D]
get_images()const
Array[GLTFLight]
get_lights()const
Array[Material]
get_materials()const
Array[GLTFMesh]
get_meshes()const
get_node_index(scene_node:Node)const
Array[GLTFNode]
get_nodes()const
Node
get_scene_node(gltf_node_index:int)const
Array[GLTFSkeleton]
get_skeletons()const
Array[GLTFSkin]
get_skins()const
Array[GLTFTextureSampler]
get_texture_samplers()const
Array[GLTFTexture]
get_textures()const
Array[String]
get_unique_animation_names()const
Array[String]
get_unique_names()const
void
set_accessors(accessors:Array[GLTFAccessor])
void
set_additional_data(extension_name:StringName, additional_data:Variant)
void
set_animations(animations:Array[GLTFAnimation])
void
set_buffer_views(buffer_views:Array[GLTFBufferView])
void
set_cameras(cameras:Array[GLTFCamera])
void
set_handle_binary_image(method:int)
void
set_images(images:Array[Texture2D])
void
set_lights(lights:Array[GLTFLight])
void
set_materials(materials:Array[Material])
void
set_meshes(meshes:Array[GLTFMesh])
void
set_nodes(nodes:Array[GLTFNode])
void
set_skeletons(skeletons:Array[GLTFSkeleton])
void
set_skins(skins:Array[GLTFSkin])
void
set_texture_samplers(texture_samplers:Array[GLTFTextureSampler])
void
set_textures(textures:Array[GLTFTexture])
void
set_unique_animation_names(unique_animation_names:Array[String])
void
set_unique_names(unique_names:Array[String])

## Enumerations
enumHandleBinaryImageMode:🔗
HandleBinaryImageModeHANDLE_BINARY_IMAGE_MODE_DISCARD_TEXTURES=0
When importing a glTF file with embedded binary images, discards all images and uses untextured materials in their place. Images stored as separate files in theres://folder are not affected by this; those will be used as Godot imported them.
HandleBinaryImageModeHANDLE_BINARY_IMAGE_MODE_EXTRACT_TEXTURES=1
When importing a glTF file with embedded binary images, extracts them and saves them to their own files. This allows the image to be imported by Godot's image importer, which can then have their import options customized by the user, including optionally compressing the image to VRAM texture formats.
This will save the images's bytes exactly as-is, without recompression. For image formats supplied by glTF extensions, the file will have a filename ending with the file extension supplied byGLTFDocumentExtension._get_image_file_extension()of the extension class.
Note:This option is editor-only. At runtime, this acts the same asHANDLE_BINARY_IMAGE_MODE_EMBED_AS_UNCOMPRESSED.
HandleBinaryImageModeHANDLE_BINARY_IMAGE_MODE_EMBED_AS_BASISU=2
When importing a glTF file with embedded binary images, embeds textures VRAM compressed with Basis Universal into the generated scene. Images stored as separate files in theres://folder are not affected by this; those will be used as Godot imported them.
HandleBinaryImageModeHANDLE_BINARY_IMAGE_MODE_EMBED_AS_UNCOMPRESSED=3
When importing a glTF file with embedded binary images, embeds textures compressed losslessly into the generated scene. Images stored as separate files in theres://folder are not affected by this; those will be used as Godot imported them.

## Constants
HANDLE_BINARY_DISCARD_TEXTURES=0🔗
Deprecated:UseHANDLE_BINARY_IMAGE_MODE_DISCARD_TEXTURESinstead.
Discards all embedded textures and uses untextured materials.
HANDLE_BINARY_EXTRACT_TEXTURES=1🔗
Deprecated:UseHANDLE_BINARY_IMAGE_MODE_EXTRACT_TEXTURESinstead.
Extracts embedded textures to be reimported and compressed. Editor only. Acts as uncompressed at runtime.
HANDLE_BINARY_EMBED_AS_BASISU=2🔗
Deprecated:UseHANDLE_BINARY_IMAGE_MODE_EMBED_AS_BASISUinstead.
Embeds textures VRAM compressed with Basis Universal into the generated scene.
HANDLE_BINARY_EMBED_AS_UNCOMPRESSED=3🔗
Deprecated:UseHANDLE_BINARY_IMAGE_MODE_EMBED_AS_UNCOMPRESSEDinstead.
Embeds textures compressed losslessly into the generated scene, matching old behavior.

## Property Descriptions
floatbake_fps=30.0🔗
- voidset_bake_fps(value:float)
voidset_bake_fps(value:float)
- floatget_bake_fps()
floatget_bake_fps()
The baking fps of the animation for either import or export.
Stringbase_path=""🔗
- voidset_base_path(value:String)
voidset_base_path(value:String)
- Stringget_base_path()
Stringget_base_path()
The folder path associated with this glTF data. This is used to find other files the glTF file references, like images or binary buffers. This will be set during import when appending from a file, and will be set during export when writing to a file.
Array[PackedByteArray]buffers=[]🔗
- voidset_buffers(value:Array[PackedByteArray])
voidset_buffers(value:Array[PackedByteArray])
- Array[PackedByteArray]get_buffers()
Array[PackedByteArray]get_buffers()
There is currently no description for this property. Please help us bycontributing one!
Stringcopyright=""🔗
- voidset_copyright(value:String)
voidset_copyright(value:String)
- Stringget_copyright()
Stringget_copyright()
The copyright string in the asset header of the glTF file. This is set during import if present and export if non-empty. See the glTF asset header documentation for more information.
boolcreate_animations=true🔗
- voidset_create_animations(value:bool)
voidset_create_animations(value:bool)
- boolget_create_animations()
boolget_create_animations()
There is currently no description for this property. Please help us bycontributing one!
Stringfilename=""🔗
- voidset_filename(value:String)
voidset_filename(value:String)
- Stringget_filename()
Stringget_filename()
The file name associated with this glTF data. If it ends with.gltf, this is text-based glTF, otherwise this is binary GLB. This will be set during import when appending from a file, and will be set during export when writing to a file. If writing to a buffer, this will be an empty string.
PackedByteArrayglb_data=PackedByteArray()🔗
- voidset_glb_data(value:PackedByteArray)
voidset_glb_data(value:PackedByteArray)
- PackedByteArrayget_glb_data()
PackedByteArrayget_glb_data()
The binary buffer attached to a .glb file.
Note:The returned array iscopiedand any changes to it will not update the original property value. SeePackedByteArrayfor more details.
HandleBinaryImageModehandle_binary_image_mode=1🔗
- voidset_handle_binary_image_mode(value:HandleBinaryImageMode)
voidset_handle_binary_image_mode(value:HandleBinaryImageMode)
- HandleBinaryImageModeget_handle_binary_image_mode()
HandleBinaryImageModeget_handle_binary_image_mode()
When importing a glTF file with unimported raw binary images embedded inside of binary blob buffers, in data URIs, or separate files not imported by Godot, this controls how the images are handled. Images can be discarded, saved as separate files, or embedded in the scene lossily or losslessly. SeeHandleBinaryImageModefor options.
This property does nothing for image files in theres://folder imported by Godot, as those are handled by Godot's image importer directly, and then the Godot scene generated from the glTF file will use the images as Godot imported them.
boolimport_as_skeleton_bones=false🔗
- voidset_import_as_skeleton_bones(value:bool)
voidset_import_as_skeleton_bones(value:bool)
- boolget_import_as_skeleton_bones()
boolget_import_as_skeleton_bones()
Iftrue, forces all GLTFNodes in the document to be bones of a singleSkeleton3DGodot node.
Dictionaryjson={}🔗
- voidset_json(value:Dictionary)
voidset_json(value:Dictionary)
- Dictionaryget_json()
Dictionaryget_json()
The original raw JSON document corresponding to this GLTFState.
intmajor_version=0🔗
- voidset_major_version(value:int)
voidset_major_version(value:int)
- intget_major_version()
intget_major_version()
There is currently no description for this property. Please help us bycontributing one!
intminor_version=0🔗
- voidset_minor_version(value:int)
voidset_minor_version(value:int)
- intget_minor_version()
intget_minor_version()
There is currently no description for this property. Please help us bycontributing one!
PackedInt32Arrayroot_nodes=PackedInt32Array()🔗
- voidset_root_nodes(value:PackedInt32Array)
voidset_root_nodes(value:PackedInt32Array)
- PackedInt32Arrayget_root_nodes()
PackedInt32Arrayget_root_nodes()
The root nodes of the glTF file. Typically, a glTF file will only have one scene, and therefore one root node. However, a glTF file may have multiple scenes and therefore multiple root nodes, which will be generated as siblings of each other and as children of the root node of the generated Godot scene.
Note:The returned array iscopiedand any changes to it will not update the original property value. SeePackedInt32Arrayfor more details.
Stringscene_name=""🔗
- voidset_scene_name(value:String)
voidset_scene_name(value:String)
- Stringget_scene_name()
Stringget_scene_name()
The name of the scene. When importing, if not specified, this will be the file name. When exporting, if specified, the scene name will be saved to the glTF file.
booluse_named_skin_binds=false🔗
- voidset_use_named_skin_binds(value:bool)
voidset_use_named_skin_binds(value:bool)
- boolget_use_named_skin_binds()
boolget_use_named_skin_binds()
There is currently no description for this property. Please help us bycontributing one!

## Method Descriptions
voidadd_used_extension(extension_name:String, required:bool)🔗
Appends an extension to the list of extensions used by this glTF file during serialization. Ifrequiredistrue, the extension will also be added to the list of required extensions. Do not run this inGLTFDocumentExtension._export_post(), as that stage is too late to add extensions. The final list is sorted alphabetically.
intappend_data_to_buffers(data:PackedByteArray, deduplication:bool)🔗
Appends the given byte arraydatato the buffers and creates aGLTFBufferViewfor it. The index of the destinationGLTFBufferViewis returned. Ifdeduplicationistrue, the buffers are first searched for duplicate data, otherwise new bytes are always appended.
intappend_gltf_node(gltf_node:GLTFNode, godot_scene_node:Node, parent_node_index:int)🔗
Appends the givenGLTFNodeto the state, and returns its new index. This can be used to export one Godot node as multiple glTF nodes, or inject new glTF nodes at import time. On import, this must be called beforeGLTFDocumentExtension._generate_scene_node()finishes for the parent node. On export, this must be called beforeGLTFDocumentExtension._export_node()runs for the parent node.
Thegodot_scene_nodeparameter is the Godot scene node that corresponds to this glTF node. This is highly recommended to be set to a valid node, but may benullif there is no corresponding Godot scene node. One Godot scene node may be used for multiple glTF nodes, so if exporting multiple glTF nodes for one Godot scene node, use the same Godot scene node for each.
Theparent_node_indexparameter is the index of the parentGLTFNodein the state. If-1, the node will be a root node, otherwise the new node will be added to the parent's list of children. The index will also be written to theGLTFNode.parentproperty of the new node.
Array[GLTFAccessor]get_accessors()const🔗
There is currently no description for this method. Please help us bycontributing one!
Variantget_additional_data(extension_name:StringName)const🔗
Gets additional arbitrary data in thisGLTFStateinstance. This can be used to keep per-file state data inGLTFDocumentExtensionclasses, which is important because they are stateless.
The argument should be theGLTFDocumentExtensionname (does not have to match the extension name in the glTF file), and the return value can be anything you set. If nothing was set, the return value isnull.
AnimationPlayerget_animation_player(anim_player_index:int)const🔗
Returns theAnimationPlayernode with the given index. These nodes are only used during the export process when converting GodotAnimationPlayernodes to glTF animations.
intget_animation_players_count(anim_player_index:int)const🔗
Returns the number ofAnimationPlayernodes in thisGLTFState. These nodes are only used during the export process when converting GodotAnimationPlayernodes to glTF animations.
Array[GLTFAnimation]get_animations()const🔗
Returns an array of allGLTFAnimations in the glTF file. When importing, these will be generated as animations in anAnimationPlayernode. When exporting, these will be generated from GodotAnimationPlayernodes.
Array[GLTFBufferView]get_buffer_views()const🔗
There is currently no description for this method. Please help us bycontributing one!
Array[GLTFCamera]get_cameras()const🔗
Returns an array of allGLTFCameras in the glTF file. These are the cameras that theGLTFNode.cameraindex refers to.
intget_handle_binary_image()const🔗
Deprecated:Usehandle_binary_image_modeinstead.
Deprecated untyped alias forhandle_binary_image_mode. When importing a glTF file with unimported raw binary images embedded inside of binary blob buffers, in data URIs, or separate files not imported by Godot, this controls how the images are handled.
Array[Texture2D]get_images()const🔗
Gets the images of the glTF file as an array ofTexture2Ds. These are the images that theGLTFTexture.src_imageindex refers to.
Array[GLTFLight]get_lights()const🔗
Returns an array of allGLTFLights in the glTF file. These are the lights that theGLTFNode.lightindex refers to.
Array[Material]get_materials()const🔗
There is currently no description for this method. Please help us bycontributing one!
Array[GLTFMesh]get_meshes()const🔗
Returns an array of allGLTFMeshes in the glTF file. These are the meshes that theGLTFNode.meshindex refers to.
intget_node_index(scene_node:Node)const🔗
Returns the index of theGLTFNodecorresponding to this Godot scene node. This is the inverse ofget_scene_node(). Useful during the export process.
Note:Not every Godot scene node will have a correspondingGLTFNode, and not everyGLTFNodewill have a scene node generated. If there is noGLTFNodeindex for this scene node,-1is returned.
Array[GLTFNode]get_nodes()const🔗
Returns an array of allGLTFNodes in the glTF file. These are the nodes thatGLTFNode.childrenandroot_nodesrefer to. This includes nodes that may not be generated in the Godot scene, or nodes that may generate multiple Godot scene nodes.
Nodeget_scene_node(gltf_node_index:int)const🔗
Returns the Godot scene node that corresponds to the same index as theGLTFNodeit was generated from. This is the inverse ofget_node_index(). Useful during the import process.
Note:Not everyGLTFNodewill have a scene node generated, and not every generated scene node will have a correspondingGLTFNode. If there is no scene node for thisGLTFNodeindex,nullis returned.
Array[GLTFSkeleton]get_skeletons()const🔗
Returns an array of allGLTFSkeletons in the glTF file. These are the skeletons that theGLTFNode.skeletonindex refers to.
Array[GLTFSkin]get_skins()const🔗
Returns an array of allGLTFSkins in the glTF file. These are the skins that theGLTFNode.skinindex refers to.
Array[GLTFTextureSampler]get_texture_samplers()const🔗
Retrieves the array of texture samplers that are used by the textures contained in the glTF.
Array[GLTFTexture]get_textures()const🔗
There is currently no description for this method. Please help us bycontributing one!
Array[String]get_unique_animation_names()const🔗
Returns an array of unique animation names. This is only used during the import process.
Array[String]get_unique_names()const🔗
Returns an array of unique node names. This is used in both the import process and export process.
voidset_accessors(accessors:Array[GLTFAccessor])🔗
There is currently no description for this method. Please help us bycontributing one!
voidset_additional_data(extension_name:StringName, additional_data:Variant)🔗
Sets additional arbitrary data in thisGLTFStateinstance. This can be used to keep per-file state data inGLTFDocumentExtensionclasses, which is important because they are stateless.
The first argument should be theGLTFDocumentExtensionname (does not have to match the extension name in the glTF file), and the second argument can be anything you want.
voidset_animations(animations:Array[GLTFAnimation])🔗
Sets theGLTFAnimations in the state. When importing, these will be generated as animations in anAnimationPlayernode. When exporting, these will be generated from GodotAnimationPlayernodes.
voidset_buffer_views(buffer_views:Array[GLTFBufferView])🔗
There is currently no description for this method. Please help us bycontributing one!
voidset_cameras(cameras:Array[GLTFCamera])🔗
Sets theGLTFCameras in the state. These are the cameras that theGLTFNode.cameraindex refers to.
voidset_handle_binary_image(method:int)🔗
Deprecated:Usehandle_binary_image_modeinstead.
Deprecated untyped alias forhandle_binary_image_mode. When importing a glTF file with unimported raw binary images embedded inside of binary blob buffers, in data URIs, or separate files not imported by Godot, this controls how the images are handled.
voidset_images(images:Array[Texture2D])🔗
Sets the images in the state stored as an array ofTexture2Ds. This can be used during export. These are the images that theGLTFTexture.src_imageindex refers to.
voidset_lights(lights:Array[GLTFLight])🔗
Sets theGLTFLights in the state. These are the lights that theGLTFNode.lightindex refers to.
voidset_materials(materials:Array[Material])🔗
There is currently no description for this method. Please help us bycontributing one!
voidset_meshes(meshes:Array[GLTFMesh])🔗
Sets theGLTFMeshes in the state. These are the meshes that theGLTFNode.meshindex refers to.
voidset_nodes(nodes:Array[GLTFNode])🔗
Sets theGLTFNodes in the state. These are the nodes thatGLTFNode.childrenandroot_nodesrefer to. Some of the nodes set here may not be generated in the Godot scene, or may generate multiple Godot scene nodes.
voidset_skeletons(skeletons:Array[GLTFSkeleton])🔗
Sets theGLTFSkeletons in the state. These are the skeletons that theGLTFNode.skeletonindex refers to.
voidset_skins(skins:Array[GLTFSkin])🔗
Sets theGLTFSkins in the state. These are the skins that theGLTFNode.skinindex refers to.
voidset_texture_samplers(texture_samplers:Array[GLTFTextureSampler])🔗
Sets the array of texture samplers that are used by the textures contained in the glTF.
voidset_textures(textures:Array[GLTFTexture])🔗
There is currently no description for this method. Please help us bycontributing one!
voidset_unique_animation_names(unique_animation_names:Array[String])🔗
Sets the unique animation names in the state. This is only used during the import process.
voidset_unique_names(unique_names:Array[String])🔗
Sets the unique node names in the state. This is used in both the import process and export process.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.