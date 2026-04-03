:github_url: hide



# GLTFState

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [FBXState<class_FBXState>]

Represents all data of a glTF file.


## Description

Contains all nodes and resources of a glTF file. This is used by [GLTFDocument<class_GLTFDocument>] as data storage, which allows [GLTFDocument<class_GLTFDocument>] and all [GLTFDocumentExtension<class_GLTFDocumentExtension>] classes to remain stateless.

GLTFState can be populated by [GLTFDocument<class_GLTFDocument>] reading a file or by converting a Godot scene. Then the data can either be used to create a Godot scene or save to a glTF file. The code that converts to/from a Godot scene can be intercepted at arbitrary points by [GLTFDocumentExtension<class_GLTFDocumentExtension>] classes. This allows for custom data to be stored in the glTF file or for custom data to be converted to/from Godot nodes.


## Tutorials

- [../tutorials/io/runtime_file_loading_and_saving](Runtime file loading and saving .md)

- [glTF asset header schema ](https://github.com/KhronosGroup/glTF/blob/main/specification/2.0/schema/asset.schema.json)_


## Properties

> **TABLE**
> :widths: auto
>
> +----------------------------------------------------------------------------+------------------------------------------------------------------------------------+------------------------+
> | :ref:`float<class_float>`                                                  | :ref:`bake_fps<class_GLTFState_property_bake_fps>`                                 | ``30.0``               |
> +----------------------------------------------------------------------------+------------------------------------------------------------------------------------+------------------------+
> | :ref:`String<class_String>`                                                | :ref:`base_path<class_GLTFState_property_base_path>`                               | ``""``                 |
> +----------------------------------------------------------------------------+------------------------------------------------------------------------------------+------------------------+
> | :ref:`Array<class_Array>`\[:ref:`PackedByteArray<class_PackedByteArray>`\] | :ref:`buffers<class_GLTFState_property_buffers>`                                   | ``[]``                 |
> +----------------------------------------------------------------------------+------------------------------------------------------------------------------------+------------------------+
> | :ref:`String<class_String>`                                                | :ref:`copyright<class_GLTFState_property_copyright>`                               | ``""``                 |
> +----------------------------------------------------------------------------+------------------------------------------------------------------------------------+------------------------+
> | :ref:`bool<class_bool>`                                                    | :ref:`create_animations<class_GLTFState_property_create_animations>`               | ``true``               |
> +----------------------------------------------------------------------------+------------------------------------------------------------------------------------+------------------------+
> | :ref:`String<class_String>`                                                | :ref:`filename<class_GLTFState_property_filename>`                                 | ``""``                 |
> +----------------------------------------------------------------------------+------------------------------------------------------------------------------------+------------------------+
> | :ref:`PackedByteArray<class_PackedByteArray>`                              | :ref:`glb_data<class_GLTFState_property_glb_data>`                                 | ``PackedByteArray()``  |
> +----------------------------------------------------------------------------+------------------------------------------------------------------------------------+------------------------+
> | :ref:`HandleBinaryImageMode<enum_GLTFState_HandleBinaryImageMode>`         | :ref:`handle_binary_image_mode<class_GLTFState_property_handle_binary_image_mode>` | ``1``                  |
> +----------------------------------------------------------------------------+------------------------------------------------------------------------------------+------------------------+
> | :ref:`bool<class_bool>`                                                    | :ref:`import_as_skeleton_bones<class_GLTFState_property_import_as_skeleton_bones>` | ``false``              |
> +----------------------------------------------------------------------------+------------------------------------------------------------------------------------+------------------------+
> | :ref:`Dictionary<class_Dictionary>`                                        | :ref:`json<class_GLTFState_property_json>`                                         | ``{}``                 |
> +----------------------------------------------------------------------------+------------------------------------------------------------------------------------+------------------------+
> | :ref:`int<class_int>`                                                      | :ref:`major_version<class_GLTFState_property_major_version>`                       | ``0``                  |
> +----------------------------------------------------------------------------+------------------------------------------------------------------------------------+------------------------+
> | :ref:`int<class_int>`                                                      | :ref:`minor_version<class_GLTFState_property_minor_version>`                       | ``0``                  |
> +----------------------------------------------------------------------------+------------------------------------------------------------------------------------+------------------------+
> | :ref:`PackedInt32Array<class_PackedInt32Array>`                            | :ref:`root_nodes<class_GLTFState_property_root_nodes>`                             | ``PackedInt32Array()`` |
> +----------------------------------------------------------------------------+------------------------------------------------------------------------------------+------------------------+
> | :ref:`String<class_String>`                                                | :ref:`scene_name<class_GLTFState_property_scene_name>`                             | ``""``                 |
> +----------------------------------------------------------------------------+------------------------------------------------------------------------------------+------------------------+
> | :ref:`bool<class_bool>`                                                    | :ref:`use_named_skin_binds<class_GLTFState_property_use_named_skin_binds>`         | ``false``              |
> +----------------------------------------------------------------------------+------------------------------------------------------------------------------------+------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                           | :ref:`add_used_extension<class_GLTFState_method_add_used_extension>`\ (\ extension_name\: :ref:`String<class_String>`, required\: :ref:`bool<class_bool>`\ )                                               |
> +----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                                            | :ref:`append_data_to_buffers<class_GLTFState_method_append_data_to_buffers>`\ (\ data\: :ref:`PackedByteArray<class_PackedByteArray>`, deduplication\: :ref:`bool<class_bool>`\ )                          |
> +----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                                            | :ref:`append_gltf_node<class_GLTFState_method_append_gltf_node>`\ (\ gltf_node\: :ref:`GLTFNode<class_GLTFNode>`, godot_scene_node\: :ref:`Node<class_Node>`, parent_node_index\: :ref:`int<class_int>`\ ) |
> +----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`GLTFAccessor<class_GLTFAccessor>`\]             | :ref:`get_accessors<class_GLTFState_method_get_accessors>`\ (\ ) |const|                                                                                                                                   |
> +----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>`                                                    | :ref:`get_additional_data<class_GLTFState_method_get_additional_data>`\ (\ extension_name\: :ref:`StringName<class_StringName>`\ ) |const|                                                                 |
> +----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`AnimationPlayer<class_AnimationPlayer>`                                    | :ref:`get_animation_player<class_GLTFState_method_get_animation_player>`\ (\ anim_player_index\: :ref:`int<class_int>`\ ) |const|                                                                          |
> +----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                                            | :ref:`get_animation_players_count<class_GLTFState_method_get_animation_players_count>`\ (\ anim_player_index\: :ref:`int<class_int>`\ ) |const|                                                            |
> +----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`GLTFAnimation<class_GLTFAnimation>`\]           | :ref:`get_animations<class_GLTFState_method_get_animations>`\ (\ ) |const|                                                                                                                                 |
> +----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`GLTFBufferView<class_GLTFBufferView>`\]         | :ref:`get_buffer_views<class_GLTFState_method_get_buffer_views>`\ (\ ) |const|                                                                                                                             |
> +----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`GLTFCamera<class_GLTFCamera>`\]                 | :ref:`get_cameras<class_GLTFState_method_get_cameras>`\ (\ ) |const|                                                                                                                                       |
> +----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                                            | :ref:`get_handle_binary_image<class_GLTFState_method_get_handle_binary_image>`\ (\ ) |const|                                                                                                               |
> +----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`Texture2D<class_Texture2D>`\]                   | :ref:`get_images<class_GLTFState_method_get_images>`\ (\ ) |const|                                                                                                                                         |
> +----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`GLTFLight<class_GLTFLight>`\]                   | :ref:`get_lights<class_GLTFState_method_get_lights>`\ (\ ) |const|                                                                                                                                         |
> +----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`Material<class_Material>`\]                     | :ref:`get_materials<class_GLTFState_method_get_materials>`\ (\ ) |const|                                                                                                                                   |
> +----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`GLTFMesh<class_GLTFMesh>`\]                     | :ref:`get_meshes<class_GLTFState_method_get_meshes>`\ (\ ) |const|                                                                                                                                         |
> +----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                                            | :ref:`get_node_index<class_GLTFState_method_get_node_index>`\ (\ scene_node\: :ref:`Node<class_Node>`\ ) |const|                                                                                           |
> +----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`GLTFNode<class_GLTFNode>`\]                     | :ref:`get_nodes<class_GLTFState_method_get_nodes>`\ (\ ) |const|                                                                                                                                           |
> +----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Node<class_Node>`                                                          | :ref:`get_scene_node<class_GLTFState_method_get_scene_node>`\ (\ gltf_node_index\: :ref:`int<class_int>`\ ) |const|                                                                                        |
> +----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`GLTFSkeleton<class_GLTFSkeleton>`\]             | :ref:`get_skeletons<class_GLTFState_method_get_skeletons>`\ (\ ) |const|                                                                                                                                   |
> +----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`GLTFSkin<class_GLTFSkin>`\]                     | :ref:`get_skins<class_GLTFState_method_get_skins>`\ (\ ) |const|                                                                                                                                           |
> +----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`GLTFTextureSampler<class_GLTFTextureSampler>`\] | :ref:`get_texture_samplers<class_GLTFState_method_get_texture_samplers>`\ (\ ) |const|                                                                                                                     |
> +----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`GLTFTexture<class_GLTFTexture>`\]               | :ref:`get_textures<class_GLTFState_method_get_textures>`\ (\ ) |const|                                                                                                                                     |
> +----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`String<class_String>`\]                         | :ref:`get_unique_animation_names<class_GLTFState_method_get_unique_animation_names>`\ (\ ) |const|                                                                                                         |
> +----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`String<class_String>`\]                         | :ref:`get_unique_names<class_GLTFState_method_get_unique_names>`\ (\ ) |const|                                                                                                                             |
> +----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                           | :ref:`set_accessors<class_GLTFState_method_set_accessors>`\ (\ accessors\: :ref:`Array<class_Array>`\[:ref:`GLTFAccessor<class_GLTFAccessor>`\]\ )                                                         |
> +----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                           | :ref:`set_additional_data<class_GLTFState_method_set_additional_data>`\ (\ extension_name\: :ref:`StringName<class_StringName>`, additional_data\: :ref:`Variant<class_Variant>`\ )                        |
> +----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                           | :ref:`set_animations<class_GLTFState_method_set_animations>`\ (\ animations\: :ref:`Array<class_Array>`\[:ref:`GLTFAnimation<class_GLTFAnimation>`\]\ )                                                    |
> +----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                           | :ref:`set_buffer_views<class_GLTFState_method_set_buffer_views>`\ (\ buffer_views\: :ref:`Array<class_Array>`\[:ref:`GLTFBufferView<class_GLTFBufferView>`\]\ )                                            |
> +----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                           | :ref:`set_cameras<class_GLTFState_method_set_cameras>`\ (\ cameras\: :ref:`Array<class_Array>`\[:ref:`GLTFCamera<class_GLTFCamera>`\]\ )                                                                   |
> +----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                           | :ref:`set_handle_binary_image<class_GLTFState_method_set_handle_binary_image>`\ (\ method\: :ref:`int<class_int>`\ )                                                                                       |
> +----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                           | :ref:`set_images<class_GLTFState_method_set_images>`\ (\ images\: :ref:`Array<class_Array>`\[:ref:`Texture2D<class_Texture2D>`\]\ )                                                                        |
> +----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                           | :ref:`set_lights<class_GLTFState_method_set_lights>`\ (\ lights\: :ref:`Array<class_Array>`\[:ref:`GLTFLight<class_GLTFLight>`\]\ )                                                                        |
> +----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                           | :ref:`set_materials<class_GLTFState_method_set_materials>`\ (\ materials\: :ref:`Array<class_Array>`\[:ref:`Material<class_Material>`\]\ )                                                                 |
> +----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                           | :ref:`set_meshes<class_GLTFState_method_set_meshes>`\ (\ meshes\: :ref:`Array<class_Array>`\[:ref:`GLTFMesh<class_GLTFMesh>`\]\ )                                                                          |
> +----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                           | :ref:`set_nodes<class_GLTFState_method_set_nodes>`\ (\ nodes\: :ref:`Array<class_Array>`\[:ref:`GLTFNode<class_GLTFNode>`\]\ )                                                                             |
> +----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                           | :ref:`set_skeletons<class_GLTFState_method_set_skeletons>`\ (\ skeletons\: :ref:`Array<class_Array>`\[:ref:`GLTFSkeleton<class_GLTFSkeleton>`\]\ )                                                         |
> +----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                           | :ref:`set_skins<class_GLTFState_method_set_skins>`\ (\ skins\: :ref:`Array<class_Array>`\[:ref:`GLTFSkin<class_GLTFSkin>`\]\ )                                                                             |
> +----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                           | :ref:`set_texture_samplers<class_GLTFState_method_set_texture_samplers>`\ (\ texture_samplers\: :ref:`Array<class_Array>`\[:ref:`GLTFTextureSampler<class_GLTFTextureSampler>`\]\ )                        |
> +----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                           | :ref:`set_textures<class_GLTFState_method_set_textures>`\ (\ textures\: :ref:`Array<class_Array>`\[:ref:`GLTFTexture<class_GLTFTexture>`\]\ )                                                              |
> +----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                           | :ref:`set_unique_animation_names<class_GLTFState_method_set_unique_animation_names>`\ (\ unique_animation_names\: :ref:`Array<class_Array>`\[:ref:`String<class_String>`\]\ )                              |
> +----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                           | :ref:`set_unique_names<class_GLTFState_method_set_unique_names>`\ (\ unique_names\: :ref:`Array<class_Array>`\[:ref:`String<class_String>`\]\ )                                                            |
> +----------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **HandleBinaryImageMode**: [🔗<enum_GLTFState_HandleBinaryImageMode>]



[HandleBinaryImageMode<enum_GLTFState_HandleBinaryImageMode>] **HANDLE_BINARY_IMAGE_MODE_DISCARD_TEXTURES** = `0`

When importing a glTF file with embedded binary images, discards all images and uses untextured materials in their place. Images stored as separate files in the `res://` folder are not affected by this; those will be used as Godot imported them.



[HandleBinaryImageMode<enum_GLTFState_HandleBinaryImageMode>] **HANDLE_BINARY_IMAGE_MODE_EXTRACT_TEXTURES** = `1`

When importing a glTF file with embedded binary images, extracts them and saves them to their own files. This allows the image to be imported by Godot's image importer, which can then have their import options customized by the user, including optionally compressing the image to VRAM texture formats.

This will save the images's bytes exactly as-is, without recompression. For image formats supplied by glTF extensions, the file will have a filename ending with the file extension supplied by [GLTFDocumentExtension._get_image_file_extension()<class_GLTFDocumentExtension_private_method__get_image_file_extension>] of the extension class.

\ **Note:** This option is editor-only. At runtime, this acts the same as [HANDLE_BINARY_IMAGE_MODE_EMBED_AS_UNCOMPRESSED<class_GLTFState_constant_HANDLE_BINARY_IMAGE_MODE_EMBED_AS_UNCOMPRESSED>].



[HandleBinaryImageMode<enum_GLTFState_HandleBinaryImageMode>] **HANDLE_BINARY_IMAGE_MODE_EMBED_AS_BASISU** = `2`

When importing a glTF file with embedded binary images, embeds textures VRAM compressed with Basis Universal into the generated scene. Images stored as separate files in the `res://` folder are not affected by this; those will be used as Godot imported them.



[HandleBinaryImageMode<enum_GLTFState_HandleBinaryImageMode>] **HANDLE_BINARY_IMAGE_MODE_EMBED_AS_UNCOMPRESSED** = `3`

When importing a glTF file with embedded binary images, embeds textures compressed losslessly into the generated scene. Images stored as separate files in the `res://` folder are not affected by this; those will be used as Godot imported them.


----


## Constants



**HANDLE_BINARY_DISCARD_TEXTURES** = `0` [🔗<class_GLTFState_constant_HANDLE_BINARY_DISCARD_TEXTURES>]

**Deprecated:** Use [HANDLE_BINARY_IMAGE_MODE_DISCARD_TEXTURES<class_GLTFState_constant_HANDLE_BINARY_IMAGE_MODE_DISCARD_TEXTURES>] instead.

Discards all embedded textures and uses untextured materials.



**HANDLE_BINARY_EXTRACT_TEXTURES** = `1` [🔗<class_GLTFState_constant_HANDLE_BINARY_EXTRACT_TEXTURES>]

**Deprecated:** Use [HANDLE_BINARY_IMAGE_MODE_EXTRACT_TEXTURES<class_GLTFState_constant_HANDLE_BINARY_IMAGE_MODE_EXTRACT_TEXTURES>] instead.

Extracts embedded textures to be reimported and compressed. Editor only. Acts as uncompressed at runtime.



**HANDLE_BINARY_EMBED_AS_BASISU** = `2` [🔗<class_GLTFState_constant_HANDLE_BINARY_EMBED_AS_BASISU>]

**Deprecated:** Use [HANDLE_BINARY_IMAGE_MODE_EMBED_AS_BASISU<class_GLTFState_constant_HANDLE_BINARY_IMAGE_MODE_EMBED_AS_BASISU>] instead.

Embeds textures VRAM compressed with Basis Universal into the generated scene.



**HANDLE_BINARY_EMBED_AS_UNCOMPRESSED** = `3` [🔗<class_GLTFState_constant_HANDLE_BINARY_EMBED_AS_UNCOMPRESSED>]

**Deprecated:** Use [HANDLE_BINARY_IMAGE_MODE_EMBED_AS_UNCOMPRESSED<class_GLTFState_constant_HANDLE_BINARY_IMAGE_MODE_EMBED_AS_UNCOMPRESSED>] instead.

Embeds textures compressed losslessly into the generated scene, matching old behavior.


----


## Property Descriptions



[float<class_float>] **bake_fps** = `30.0` [🔗<class_GLTFState_property_bake_fps>]


- |void| **set_bake_fps**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_bake_fps**\ (\ )

The baking fps of the animation for either import or export.


----



[String<class_String>] **base_path** = `""` [🔗<class_GLTFState_property_base_path>]


- |void| **set_base_path**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_base_path**\ (\ )

The folder path associated with this glTF data. This is used to find other files the glTF file references, like images or binary buffers. This will be set during import when appending from a file, and will be set during export when writing to a file.


----



[Array<class_Array>]\[[PackedByteArray<class_PackedByteArray>]\] **buffers** = `[]` [🔗<class_GLTFState_property_buffers>]


- |void| **set_buffers**\ (\ value\: [Array<class_Array>]\[[PackedByteArray<class_PackedByteArray>]\]\ )
- [Array<class_Array>]\[[PackedByteArray<class_PackedByteArray>]\] **get_buffers**\ (\ )

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[String<class_String>] **copyright** = `""` [🔗<class_GLTFState_property_copyright>]


- |void| **set_copyright**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_copyright**\ (\ )

The copyright string in the asset header of the glTF file. This is set during import if present and export if non-empty. See the glTF asset header documentation for more information.


----



[bool<class_bool>] **create_animations** = `true` [🔗<class_GLTFState_property_create_animations>]


- |void| **set_create_animations**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_create_animations**\ (\ )

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[String<class_String>] **filename** = `""` [🔗<class_GLTFState_property_filename>]


- |void| **set_filename**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_filename**\ (\ )

The file name associated with this glTF data. If it ends with `.gltf`, this is text-based glTF, otherwise this is binary GLB. This will be set during import when appending from a file, and will be set during export when writing to a file. If writing to a buffer, this will be an empty string.


----



[PackedByteArray<class_PackedByteArray>] **glb_data** = `PackedByteArray()` [🔗<class_GLTFState_property_glb_data>]


- |void| **set_glb_data**\ (\ value\: [PackedByteArray<class_PackedByteArray>]\ )
- [PackedByteArray<class_PackedByteArray>] **get_glb_data**\ (\ )

The binary buffer attached to a .glb file.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray<class_PackedByteArray>] for more details.


----



[HandleBinaryImageMode<enum_GLTFState_HandleBinaryImageMode>] **handle_binary_image_mode** = `1` [🔗<class_GLTFState_property_handle_binary_image_mode>]


- |void| **set_handle_binary_image_mode**\ (\ value\: [HandleBinaryImageMode<enum_GLTFState_HandleBinaryImageMode>]\ )
- [HandleBinaryImageMode<enum_GLTFState_HandleBinaryImageMode>] **get_handle_binary_image_mode**\ (\ )

When importing a glTF file with unimported raw binary images embedded inside of binary blob buffers, in data URIs, or separate files not imported by Godot, this controls how the images are handled. Images can be discarded, saved as separate files, or embedded in the scene lossily or losslessly. See [HandleBinaryImageMode<enum_GLTFState_HandleBinaryImageMode>] for options.

This property does nothing for image files in the `res://` folder imported by Godot, as those are handled by Godot's image importer directly, and then the Godot scene generated from the glTF file will use the images as Godot imported them.


----



[bool<class_bool>] **import_as_skeleton_bones** = `false` [🔗<class_GLTFState_property_import_as_skeleton_bones>]


- |void| **set_import_as_skeleton_bones**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_import_as_skeleton_bones**\ (\ )

If `true`, forces all GLTFNodes in the document to be bones of a single [Skeleton3D<class_Skeleton3D>] Godot node.


----



[Dictionary<class_Dictionary>] **json** = `{}` [🔗<class_GLTFState_property_json>]


- |void| **set_json**\ (\ value\: [Dictionary<class_Dictionary>]\ )
- [Dictionary<class_Dictionary>] **get_json**\ (\ )

The original raw JSON document corresponding to this GLTFState.


----



[int<class_int>] **major_version** = `0` [🔗<class_GLTFState_property_major_version>]


- |void| **set_major_version**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_major_version**\ (\ )

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[int<class_int>] **minor_version** = `0` [🔗<class_GLTFState_property_minor_version>]


- |void| **set_minor_version**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_minor_version**\ (\ )

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[PackedInt32Array<class_PackedInt32Array>] **root_nodes** = `PackedInt32Array()` [🔗<class_GLTFState_property_root_nodes>]


- |void| **set_root_nodes**\ (\ value\: [PackedInt32Array<class_PackedInt32Array>]\ )
- [PackedInt32Array<class_PackedInt32Array>] **get_root_nodes**\ (\ )

The root nodes of the glTF file. Typically, a glTF file will only have one scene, and therefore one root node. However, a glTF file may have multiple scenes and therefore multiple root nodes, which will be generated as siblings of each other and as children of the root node of the generated Godot scene.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedInt32Array<class_PackedInt32Array>] for more details.


----



[String<class_String>] **scene_name** = `""` [🔗<class_GLTFState_property_scene_name>]


- |void| **set_scene_name**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_scene_name**\ (\ )

The name of the scene. When importing, if not specified, this will be the file name. When exporting, if specified, the scene name will be saved to the glTF file.


----



[bool<class_bool>] **use_named_skin_binds** = `false` [🔗<class_GLTFState_property_use_named_skin_binds>]


- |void| **set_use_named_skin_binds**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_use_named_skin_binds**\ (\ )

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----


## Method Descriptions



|void| **add_used_extension**\ (\ extension_name\: [String<class_String>], required\: [bool<class_bool>]\ ) [🔗<class_GLTFState_method_add_used_extension>]

Appends an extension to the list of extensions used by this glTF file during serialization. If `required` is `true`, the extension will also be added to the list of required extensions. Do not run this in [GLTFDocumentExtension._export_post()<class_GLTFDocumentExtension_private_method__export_post>], as that stage is too late to add extensions. The final list is sorted alphabetically.


----



[int<class_int>] **append_data_to_buffers**\ (\ data\: [PackedByteArray<class_PackedByteArray>], deduplication\: [bool<class_bool>]\ ) [🔗<class_GLTFState_method_append_data_to_buffers>]

Appends the given byte array `data` to the buffers and creates a [GLTFBufferView<class_GLTFBufferView>] for it. The index of the destination [GLTFBufferView<class_GLTFBufferView>] is returned. If `deduplication` is `true`, the buffers are first searched for duplicate data, otherwise new bytes are always appended.


----



[int<class_int>] **append_gltf_node**\ (\ gltf_node\: [GLTFNode<class_GLTFNode>], godot_scene_node\: [Node<class_Node>], parent_node_index\: [int<class_int>]\ ) [🔗<class_GLTFState_method_append_gltf_node>]

Appends the given [GLTFNode<class_GLTFNode>] to the state, and returns its new index. This can be used to export one Godot node as multiple glTF nodes, or inject new glTF nodes at import time. On import, this must be called before [GLTFDocumentExtension._generate_scene_node()<class_GLTFDocumentExtension_private_method__generate_scene_node>] finishes for the parent node. On export, this must be called before [GLTFDocumentExtension._export_node()<class_GLTFDocumentExtension_private_method__export_node>] runs for the parent node.

The `godot_scene_node` parameter is the Godot scene node that corresponds to this glTF node. This is highly recommended to be set to a valid node, but may be `null` if there is no corresponding Godot scene node. One Godot scene node may be used for multiple glTF nodes, so if exporting multiple glTF nodes for one Godot scene node, use the same Godot scene node for each.

The `parent_node_index` parameter is the index of the parent [GLTFNode<class_GLTFNode>] in the state. If `-1`, the node will be a root node, otherwise the new node will be added to the parent's list of children. The index will also be written to the [GLTFNode.parent<class_GLTFNode_property_parent>] property of the new node.


----



[Array<class_Array>]\[[GLTFAccessor<class_GLTFAccessor>]\] **get_accessors**\ (\ ) |const| [🔗<class_GLTFState_method_get_accessors>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Variant<class_Variant>] **get_additional_data**\ (\ extension_name\: [StringName<class_StringName>]\ ) |const| [🔗<class_GLTFState_method_get_additional_data>]

Gets additional arbitrary data in this **GLTFState** instance. This can be used to keep per-file state data in [GLTFDocumentExtension<class_GLTFDocumentExtension>] classes, which is important because they are stateless.

The argument should be the [GLTFDocumentExtension<class_GLTFDocumentExtension>] name (does not have to match the extension name in the glTF file), and the return value can be anything you set. If nothing was set, the return value is `null`.


----



[AnimationPlayer<class_AnimationPlayer>] **get_animation_player**\ (\ anim_player_index\: [int<class_int>]\ ) |const| [🔗<class_GLTFState_method_get_animation_player>]

Returns the [AnimationPlayer<class_AnimationPlayer>] node with the given index. These nodes are only used during the export process when converting Godot [AnimationPlayer<class_AnimationPlayer>] nodes to glTF animations.


----



[int<class_int>] **get_animation_players_count**\ (\ anim_player_index\: [int<class_int>]\ ) |const| [🔗<class_GLTFState_method_get_animation_players_count>]

Returns the number of [AnimationPlayer<class_AnimationPlayer>] nodes in this **GLTFState**. These nodes are only used during the export process when converting Godot [AnimationPlayer<class_AnimationPlayer>] nodes to glTF animations.


----



[Array<class_Array>]\[[GLTFAnimation<class_GLTFAnimation>]\] **get_animations**\ (\ ) |const| [🔗<class_GLTFState_method_get_animations>]

Returns an array of all [GLTFAnimation<class_GLTFAnimation>]\ s in the glTF file. When importing, these will be generated as animations in an [AnimationPlayer<class_AnimationPlayer>] node. When exporting, these will be generated from Godot [AnimationPlayer<class_AnimationPlayer>] nodes.


----



[Array<class_Array>]\[[GLTFBufferView<class_GLTFBufferView>]\] **get_buffer_views**\ (\ ) |const| [🔗<class_GLTFState_method_get_buffer_views>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Array<class_Array>]\[[GLTFCamera<class_GLTFCamera>]\] **get_cameras**\ (\ ) |const| [🔗<class_GLTFState_method_get_cameras>]

Returns an array of all [GLTFCamera<class_GLTFCamera>]\ s in the glTF file. These are the cameras that the [GLTFNode.camera<class_GLTFNode_property_camera>] index refers to.


----



[int<class_int>] **get_handle_binary_image**\ (\ ) |const| [🔗<class_GLTFState_method_get_handle_binary_image>]

**Deprecated:** Use [handle_binary_image_mode<class_GLTFState_property_handle_binary_image_mode>] instead.

Deprecated untyped alias for [handle_binary_image_mode<class_GLTFState_property_handle_binary_image_mode>]. When importing a glTF file with unimported raw binary images embedded inside of binary blob buffers, in data URIs, or separate files not imported by Godot, this controls how the images are handled.


----



[Array<class_Array>]\[[Texture2D<class_Texture2D>]\] **get_images**\ (\ ) |const| [🔗<class_GLTFState_method_get_images>]

Gets the images of the glTF file as an array of [Texture2D<class_Texture2D>]\ s. These are the images that the [GLTFTexture.src_image<class_GLTFTexture_property_src_image>] index refers to.


----



[Array<class_Array>]\[[GLTFLight<class_GLTFLight>]\] **get_lights**\ (\ ) |const| [🔗<class_GLTFState_method_get_lights>]

Returns an array of all [GLTFLight<class_GLTFLight>]\ s in the glTF file. These are the lights that the [GLTFNode.light<class_GLTFNode_property_light>] index refers to.


----



[Array<class_Array>]\[[Material<class_Material>]\] **get_materials**\ (\ ) |const| [🔗<class_GLTFState_method_get_materials>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Array<class_Array>]\[[GLTFMesh<class_GLTFMesh>]\] **get_meshes**\ (\ ) |const| [🔗<class_GLTFState_method_get_meshes>]

Returns an array of all [GLTFMesh<class_GLTFMesh>]\ es in the glTF file. These are the meshes that the [GLTFNode.mesh<class_GLTFNode_property_mesh>] index refers to.


----



[int<class_int>] **get_node_index**\ (\ scene_node\: [Node<class_Node>]\ ) |const| [🔗<class_GLTFState_method_get_node_index>]

Returns the index of the [GLTFNode<class_GLTFNode>] corresponding to this Godot scene node. This is the inverse of [get_scene_node()<class_GLTFState_method_get_scene_node>]. Useful during the export process.

\ **Note:** Not every Godot scene node will have a corresponding [GLTFNode<class_GLTFNode>], and not every [GLTFNode<class_GLTFNode>] will have a scene node generated. If there is no [GLTFNode<class_GLTFNode>] index for this scene node, `-1` is returned.


----



[Array<class_Array>]\[[GLTFNode<class_GLTFNode>]\] **get_nodes**\ (\ ) |const| [🔗<class_GLTFState_method_get_nodes>]

Returns an array of all [GLTFNode<class_GLTFNode>]\ s in the glTF file. These are the nodes that [GLTFNode.children<class_GLTFNode_property_children>] and [root_nodes<class_GLTFState_property_root_nodes>] refer to. This includes nodes that may not be generated in the Godot scene, or nodes that may generate multiple Godot scene nodes.


----



[Node<class_Node>] **get_scene_node**\ (\ gltf_node_index\: [int<class_int>]\ ) |const| [🔗<class_GLTFState_method_get_scene_node>]

Returns the Godot scene node that corresponds to the same index as the [GLTFNode<class_GLTFNode>] it was generated from. This is the inverse of [get_node_index()<class_GLTFState_method_get_node_index>]. Useful during the import process.

\ **Note:** Not every [GLTFNode<class_GLTFNode>] will have a scene node generated, and not every generated scene node will have a corresponding [GLTFNode<class_GLTFNode>]. If there is no scene node for this [GLTFNode<class_GLTFNode>] index, `null` is returned.


----



[Array<class_Array>]\[[GLTFSkeleton<class_GLTFSkeleton>]\] **get_skeletons**\ (\ ) |const| [🔗<class_GLTFState_method_get_skeletons>]

Returns an array of all [GLTFSkeleton<class_GLTFSkeleton>]\ s in the glTF file. These are the skeletons that the [GLTFNode.skeleton<class_GLTFNode_property_skeleton>] index refers to.


----



[Array<class_Array>]\[[GLTFSkin<class_GLTFSkin>]\] **get_skins**\ (\ ) |const| [🔗<class_GLTFState_method_get_skins>]

Returns an array of all [GLTFSkin<class_GLTFSkin>]\ s in the glTF file. These are the skins that the [GLTFNode.skin<class_GLTFNode_property_skin>] index refers to.


----



[Array<class_Array>]\[[GLTFTextureSampler<class_GLTFTextureSampler>]\] **get_texture_samplers**\ (\ ) |const| [🔗<class_GLTFState_method_get_texture_samplers>]

Retrieves the array of texture samplers that are used by the textures contained in the glTF.


----



[Array<class_Array>]\[[GLTFTexture<class_GLTFTexture>]\] **get_textures**\ (\ ) |const| [🔗<class_GLTFState_method_get_textures>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Array<class_Array>]\[[String<class_String>]\] **get_unique_animation_names**\ (\ ) |const| [🔗<class_GLTFState_method_get_unique_animation_names>]

Returns an array of unique animation names. This is only used during the import process.


----



[Array<class_Array>]\[[String<class_String>]\] **get_unique_names**\ (\ ) |const| [🔗<class_GLTFState_method_get_unique_names>]

Returns an array of unique node names. This is used in both the import process and export process.


----



|void| **set_accessors**\ (\ accessors\: [Array<class_Array>]\[[GLTFAccessor<class_GLTFAccessor>]\]\ ) [🔗<class_GLTFState_method_set_accessors>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



|void| **set_additional_data**\ (\ extension_name\: [StringName<class_StringName>], additional_data\: [Variant<class_Variant>]\ ) [🔗<class_GLTFState_method_set_additional_data>]

Sets additional arbitrary data in this **GLTFState** instance. This can be used to keep per-file state data in [GLTFDocumentExtension<class_GLTFDocumentExtension>] classes, which is important because they are stateless.

The first argument should be the [GLTFDocumentExtension<class_GLTFDocumentExtension>] name (does not have to match the extension name in the glTF file), and the second argument can be anything you want.


----



|void| **set_animations**\ (\ animations\: [Array<class_Array>]\[[GLTFAnimation<class_GLTFAnimation>]\]\ ) [🔗<class_GLTFState_method_set_animations>]

Sets the [GLTFAnimation<class_GLTFAnimation>]\ s in the state. When importing, these will be generated as animations in an [AnimationPlayer<class_AnimationPlayer>] node. When exporting, these will be generated from Godot [AnimationPlayer<class_AnimationPlayer>] nodes.


----



|void| **set_buffer_views**\ (\ buffer_views\: [Array<class_Array>]\[[GLTFBufferView<class_GLTFBufferView>]\]\ ) [🔗<class_GLTFState_method_set_buffer_views>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



|void| **set_cameras**\ (\ cameras\: [Array<class_Array>]\[[GLTFCamera<class_GLTFCamera>]\]\ ) [🔗<class_GLTFState_method_set_cameras>]

Sets the [GLTFCamera<class_GLTFCamera>]\ s in the state. These are the cameras that the [GLTFNode.camera<class_GLTFNode_property_camera>] index refers to.


----



|void| **set_handle_binary_image**\ (\ method\: [int<class_int>]\ ) [🔗<class_GLTFState_method_set_handle_binary_image>]

**Deprecated:** Use [handle_binary_image_mode<class_GLTFState_property_handle_binary_image_mode>] instead.

Deprecated untyped alias for [handle_binary_image_mode<class_GLTFState_property_handle_binary_image_mode>]. When importing a glTF file with unimported raw binary images embedded inside of binary blob buffers, in data URIs, or separate files not imported by Godot, this controls how the images are handled.


----



|void| **set_images**\ (\ images\: [Array<class_Array>]\[[Texture2D<class_Texture2D>]\]\ ) [🔗<class_GLTFState_method_set_images>]

Sets the images in the state stored as an array of [Texture2D<class_Texture2D>]\ s. This can be used during export. These are the images that the [GLTFTexture.src_image<class_GLTFTexture_property_src_image>] index refers to.


----



|void| **set_lights**\ (\ lights\: [Array<class_Array>]\[[GLTFLight<class_GLTFLight>]\]\ ) [🔗<class_GLTFState_method_set_lights>]

Sets the [GLTFLight<class_GLTFLight>]\ s in the state. These are the lights that the [GLTFNode.light<class_GLTFNode_property_light>] index refers to.


----



|void| **set_materials**\ (\ materials\: [Array<class_Array>]\[[Material<class_Material>]\]\ ) [🔗<class_GLTFState_method_set_materials>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



|void| **set_meshes**\ (\ meshes\: [Array<class_Array>]\[[GLTFMesh<class_GLTFMesh>]\]\ ) [🔗<class_GLTFState_method_set_meshes>]

Sets the [GLTFMesh<class_GLTFMesh>]\ es in the state. These are the meshes that the [GLTFNode.mesh<class_GLTFNode_property_mesh>] index refers to.


----



|void| **set_nodes**\ (\ nodes\: [Array<class_Array>]\[[GLTFNode<class_GLTFNode>]\]\ ) [🔗<class_GLTFState_method_set_nodes>]

Sets the [GLTFNode<class_GLTFNode>]\ s in the state. These are the nodes that [GLTFNode.children<class_GLTFNode_property_children>] and [root_nodes<class_GLTFState_property_root_nodes>] refer to. Some of the nodes set here may not be generated in the Godot scene, or may generate multiple Godot scene nodes.


----



|void| **set_skeletons**\ (\ skeletons\: [Array<class_Array>]\[[GLTFSkeleton<class_GLTFSkeleton>]\]\ ) [🔗<class_GLTFState_method_set_skeletons>]

Sets the [GLTFSkeleton<class_GLTFSkeleton>]\ s in the state. These are the skeletons that the [GLTFNode.skeleton<class_GLTFNode_property_skeleton>] index refers to.


----



|void| **set_skins**\ (\ skins\: [Array<class_Array>]\[[GLTFSkin<class_GLTFSkin>]\]\ ) [🔗<class_GLTFState_method_set_skins>]

Sets the [GLTFSkin<class_GLTFSkin>]\ s in the state. These are the skins that the [GLTFNode.skin<class_GLTFNode_property_skin>] index refers to.


----



|void| **set_texture_samplers**\ (\ texture_samplers\: [Array<class_Array>]\[[GLTFTextureSampler<class_GLTFTextureSampler>]\]\ ) [🔗<class_GLTFState_method_set_texture_samplers>]

Sets the array of texture samplers that are used by the textures contained in the glTF.


----



|void| **set_textures**\ (\ textures\: [Array<class_Array>]\[[GLTFTexture<class_GLTFTexture>]\]\ ) [🔗<class_GLTFState_method_set_textures>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



|void| **set_unique_animation_names**\ (\ unique_animation_names\: [Array<class_Array>]\[[String<class_String>]\]\ ) [🔗<class_GLTFState_method_set_unique_animation_names>]

Sets the unique animation names in the state. This is only used during the import process.


----



|void| **set_unique_names**\ (\ unique_names\: [Array<class_Array>]\[[String<class_String>]\]\ ) [🔗<class_GLTFState_method_set_unique_names>]

Sets the unique node names in the state. This is used in both the import process and export process.

