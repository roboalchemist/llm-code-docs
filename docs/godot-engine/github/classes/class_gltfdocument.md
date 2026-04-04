:github_url: hide



# GLTFDocument

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [FBXDocument<class_FBXDocument>]

Class for importing and exporting glTF files in and out of Godot.


## Description

GLTFDocument supports reading data from a glTF file, buffer, or Godot scene. This data can then be written to the filesystem, buffer, or used to create a Godot scene.

All of the data in a glTF scene is stored in the [GLTFState<class_GLTFState>] class. GLTFDocument processes state objects, but does not contain any scene data itself. GLTFDocument has member variables to store export configuration settings such as the image format, but is otherwise stateless. Multiple scenes can be processed with the same settings using the same GLTFDocument object and different [GLTFState<class_GLTFState>] objects.

GLTFDocument can be extended with arbitrary functionality by extending the [GLTFDocumentExtension<class_GLTFDocumentExtension>] class and registering it with GLTFDocument via [register_gltf_document_extension()<class_GLTFDocument_method_register_gltf_document_extension>]. This allows for custom data to be imported and exported.


## Tutorials

- [../tutorials/io/runtime_file_loading_and_saving](Runtime file loading and saving .md)

- [glTF 'What the duck?' guide ](https://www.khronos.org/files/gltf20-reference-guide.pdf)_

- [Khronos glTF specification ](https://registry.khronos.org/glTF/)_


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------------+-----------------------------------------------------------------------------------+------------+
> | :ref:`String<class_String>`                             | :ref:`fallback_image_format<class_GLTFDocument_property_fallback_image_format>`   | ``"None"`` |
> +---------------------------------------------------------+-----------------------------------------------------------------------------------+------------+
> | :ref:`float<class_float>`                               | :ref:`fallback_image_quality<class_GLTFDocument_property_fallback_image_quality>` | ``0.25``   |
> +---------------------------------------------------------+-----------------------------------------------------------------------------------+------------+
> | :ref:`String<class_String>`                             | :ref:`image_format<class_GLTFDocument_property_image_format>`                     | ``"PNG"``  |
> +---------------------------------------------------------+-----------------------------------------------------------------------------------+------------+
> | :ref:`float<class_float>`                               | :ref:`lossy_quality<class_GLTFDocument_property_lossy_quality>`                   | ``0.75``   |
> +---------------------------------------------------------+-----------------------------------------------------------------------------------+------------+
> | :ref:`RootNodeMode<enum_GLTFDocument_RootNodeMode>`     | :ref:`root_node_mode<class_GLTFDocument_property_root_node_mode>`                 | ``0``      |
> +---------------------------------------------------------+-----------------------------------------------------------------------------------+------------+
> | :ref:`VisibilityMode<enum_GLTFDocument_VisibilityMode>` | :ref:`visibility_mode<class_GLTFDocument_property_visibility_mode>`               | ``0``      |
> +---------------------------------------------------------+-----------------------------------------------------------------------------------+------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>`                         | :ref:`append_from_buffer<class_GLTFDocument_method_append_from_buffer>`\ (\ bytes\: :ref:`PackedByteArray<class_PackedByteArray>`, base_path\: :ref:`String<class_String>`, state\: :ref:`GLTFState<class_GLTFState>`, flags\: :ref:`int<class_int>` = 0\ )                       |
> +---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>`                         | :ref:`append_from_file<class_GLTFDocument_method_append_from_file>`\ (\ path\: :ref:`String<class_String>`, state\: :ref:`GLTFState<class_GLTFState>`, flags\: :ref:`int<class_int>` = 0, base_path\: :ref:`String<class_String>` = ""\ )                                         |
> +---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>`                         | :ref:`append_from_scene<class_GLTFDocument_method_append_from_scene>`\ (\ node\: :ref:`Node<class_Node>`, state\: :ref:`GLTFState<class_GLTFState>`, flags\: :ref:`int<class_int>` = 0\ )                                                                                         |
> +---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`GLTFObjectModelProperty<class_GLTFObjectModelProperty>` | :ref:`export_object_model_property<class_GLTFDocument_method_export_object_model_property>`\ (\ state\: :ref:`GLTFState<class_GLTFState>`, node_path\: :ref:`NodePath<class_NodePath>`, godot_node\: :ref:`Node<class_Node>`, gltf_node_index\: :ref:`int<class_int>`\ ) |static| |
> +---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedByteArray<class_PackedByteArray>`                 | :ref:`generate_buffer<class_GLTFDocument_method_generate_buffer>`\ (\ state\: :ref:`GLTFState<class_GLTFState>`\ )                                                                                                                                                                |
> +---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Node<class_Node>`                                       | :ref:`generate_scene<class_GLTFDocument_method_generate_scene>`\ (\ state\: :ref:`GLTFState<class_GLTFState>`, bake_fps\: :ref:`float<class_float>` = 30, trimming\: :ref:`bool<class_bool>` = false, remove_immutable_tracks\: :ref:`bool<class_bool>` = true\ )                 |
> +---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedStringArray<class_PackedStringArray>`             | :ref:`get_supported_gltf_extensions<class_GLTFDocument_method_get_supported_gltf_extensions>`\ (\ ) |static|                                                                                                                                                                      |
> +---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`GLTFObjectModelProperty<class_GLTFObjectModelProperty>` | :ref:`import_object_model_property<class_GLTFDocument_method_import_object_model_property>`\ (\ state\: :ref:`GLTFState<class_GLTFState>`, json_pointer\: :ref:`String<class_String>`\ ) |static|                                                                                 |
> +---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                        | :ref:`register_gltf_document_extension<class_GLTFDocument_method_register_gltf_document_extension>`\ (\ extension\: :ref:`GLTFDocumentExtension<class_GLTFDocumentExtension>`, first_priority\: :ref:`bool<class_bool>` = false\ ) |static|                                       |
> +---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                        | :ref:`unregister_gltf_document_extension<class_GLTFDocument_method_unregister_gltf_document_extension>`\ (\ extension\: :ref:`GLTFDocumentExtension<class_GLTFDocumentExtension>`\ ) |static|                                                                                     |
> +---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>`                         | :ref:`write_to_filesystem<class_GLTFDocument_method_write_to_filesystem>`\ (\ state\: :ref:`GLTFState<class_GLTFState>`, path\: :ref:`String<class_String>`\ )                                                                                                                    |
> +---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **RootNodeMode**: [🔗<enum_GLTFDocument_RootNodeMode>]



[RootNodeMode<enum_GLTFDocument_RootNodeMode>] **ROOT_NODE_MODE_SINGLE_ROOT** = `0`

Treat the Godot scene's root node as the root node of the glTF file, and mark it as the single root node via the `GODOT_single_root` glTF extension. This will be parsed the same as [ROOT_NODE_MODE_KEEP_ROOT<class_GLTFDocument_constant_ROOT_NODE_MODE_KEEP_ROOT>] if the implementation does not support `GODOT_single_root`.



[RootNodeMode<enum_GLTFDocument_RootNodeMode>] **ROOT_NODE_MODE_KEEP_ROOT** = `1`

Treat the Godot scene's root node as the root node of the glTF file, but do not mark it as anything special. An extra root node will be generated when importing into Godot. This uses only vanilla glTF features. This is equivalent to the behavior in Godot 4.1 and earlier.



[RootNodeMode<enum_GLTFDocument_RootNodeMode>] **ROOT_NODE_MODE_MULTI_ROOT** = `2`

Treat the Godot scene's root node as the name of the glTF scene, and add all of its children as root nodes of the glTF file. This uses only vanilla glTF features. This avoids an extra root node, but only the name of the Godot scene's root node will be preserved, as it will not be saved as a node.


----



enum **VisibilityMode**: [🔗<enum_GLTFDocument_VisibilityMode>]



[VisibilityMode<enum_GLTFDocument_VisibilityMode>] **VISIBILITY_MODE_INCLUDE_REQUIRED** = `0`

If the scene contains any non-visible nodes, include them, mark them as non-visible with `KHR_node_visibility`, and require that importers respect their non-visibility. Downside: If the importer does not support `KHR_node_visibility`, the file cannot be imported.



[VisibilityMode<enum_GLTFDocument_VisibilityMode>] **VISIBILITY_MODE_INCLUDE_OPTIONAL** = `1`

If the scene contains any non-visible nodes, include them, mark them as non-visible with `KHR_node_visibility`, and do not impose any requirements on importers. Downside: If the importer does not support `KHR_node_visibility`, invisible objects will be visible.



[VisibilityMode<enum_GLTFDocument_VisibilityMode>] **VISIBILITY_MODE_EXCLUDE** = `2`

If the scene contains any non-visible nodes, do not include them in the export. This is the same as the behavior in Godot 4.4 and earlier. Downside: Invisible nodes will not exist in the exported file.


----


## Property Descriptions



[String<class_String>] **fallback_image_format** = `"None"` [🔗<class_GLTFDocument_property_fallback_image_format>]


- |void| **set_fallback_image_format**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_fallback_image_format**\ (\ )

The user-friendly name of the fallback image format. This is used when exporting the glTF file, including writing to a file and writing to a byte array.

This property may only be one of "None", "PNG", or "JPEG", and is only used when the [image_format<class_GLTFDocument_property_image_format>] is not one of "None", "PNG", or "JPEG". If having multiple extension image formats is desired, that can be done using a [GLTFDocumentExtension<class_GLTFDocumentExtension>] class - this property only covers the use case of providing a base glTF fallback image when using a custom image format.


----



[float<class_float>] **fallback_image_quality** = `0.25` [🔗<class_GLTFDocument_property_fallback_image_quality>]


- |void| **set_fallback_image_quality**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_fallback_image_quality**\ (\ )

The quality of the fallback image, if any. For PNG files, this downscales the image on both dimensions by this factor. For JPEG files, this is the lossy quality of the image. A low value is recommended, since including multiple high quality images in a glTF file defeats the file size gains of using a more efficient image format.


----



[String<class_String>] **image_format** = `"PNG"` [🔗<class_GLTFDocument_property_image_format>]


- |void| **set_image_format**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_image_format**\ (\ )

The user-friendly name of the export image format. This is used when exporting the glTF file, including writing to a file and writing to a byte array.

By default, Godot allows the following options: "None", "PNG", "JPEG", "Lossless WebP", and "Lossy WebP". Support for more image formats can be added in [GLTFDocumentExtension<class_GLTFDocumentExtension>] classes. A single extension class can provide multiple options for the specific format to use, or even an option that uses multiple formats at once.


----



[float<class_float>] **lossy_quality** = `0.75` [🔗<class_GLTFDocument_property_lossy_quality>]


- |void| **set_lossy_quality**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_lossy_quality**\ (\ )

If [image_format<class_GLTFDocument_property_image_format>] is a lossy image format, this determines the lossy quality of the image. On a range of `0.0` to `1.0`, where `0.0` is the lowest quality and `1.0` is the highest quality. A lossy quality of `1.0` is not the same as lossless.


----



[RootNodeMode<enum_GLTFDocument_RootNodeMode>] **root_node_mode** = `0` [🔗<class_GLTFDocument_property_root_node_mode>]


- |void| **set_root_node_mode**\ (\ value\: [RootNodeMode<enum_GLTFDocument_RootNodeMode>]\ )
- [RootNodeMode<enum_GLTFDocument_RootNodeMode>] **get_root_node_mode**\ (\ )

How to process the root node during export. The default and recommended value is [ROOT_NODE_MODE_SINGLE_ROOT<class_GLTFDocument_constant_ROOT_NODE_MODE_SINGLE_ROOT>].

\ **Note:** Regardless of how the glTF file is exported, when importing, the root node type and name can be overridden in the scene import settings tab.


----



[VisibilityMode<enum_GLTFDocument_VisibilityMode>] **visibility_mode** = `0` [🔗<class_GLTFDocument_property_visibility_mode>]


- |void| **set_visibility_mode**\ (\ value\: [VisibilityMode<enum_GLTFDocument_VisibilityMode>]\ )
- [VisibilityMode<enum_GLTFDocument_VisibilityMode>] **get_visibility_mode**\ (\ )

How to deal with node visibility during export. This setting does nothing if all nodes are visible. The default and recommended value is [VISIBILITY_MODE_INCLUDE_REQUIRED<class_GLTFDocument_constant_VISIBILITY_MODE_INCLUDE_REQUIRED>], which uses the `KHR_node_visibility` extension.


----


## Method Descriptions



[Error<enum_@GlobalScope_Error>] **append_from_buffer**\ (\ bytes\: [PackedByteArray<class_PackedByteArray>], base_path\: [String<class_String>], state\: [GLTFState<class_GLTFState>], flags\: [int<class_int>] = 0\ ) [🔗<class_GLTFDocument_method_append_from_buffer>]

Takes a [PackedByteArray<class_PackedByteArray>] defining a glTF and imports the data to the given [GLTFState<class_GLTFState>] object through the `state` parameter.

\ **Note:** The `base_path` tells [append_from_buffer()<class_GLTFDocument_method_append_from_buffer>] where to find dependencies and can be empty.


----



[Error<enum_@GlobalScope_Error>] **append_from_file**\ (\ path\: [String<class_String>], state\: [GLTFState<class_GLTFState>], flags\: [int<class_int>] = 0, base_path\: [String<class_String>] = ""\ ) [🔗<class_GLTFDocument_method_append_from_file>]

Takes a path to a glTF file and imports the data at that file path to the given [GLTFState<class_GLTFState>] object through the `state` parameter.

\ **Note:** The `base_path` tells [append_from_file()<class_GLTFDocument_method_append_from_file>] where to find dependencies and can be empty.


----



[Error<enum_@GlobalScope_Error>] **append_from_scene**\ (\ node\: [Node<class_Node>], state\: [GLTFState<class_GLTFState>], flags\: [int<class_int>] = 0\ ) [🔗<class_GLTFDocument_method_append_from_scene>]

Takes a Godot Engine scene node and exports it and its descendants to the given [GLTFState<class_GLTFState>] object through the `state` parameter.


----



[GLTFObjectModelProperty<class_GLTFObjectModelProperty>] **export_object_model_property**\ (\ state\: [GLTFState<class_GLTFState>], node_path\: [NodePath<class_NodePath>], godot_node\: [Node<class_Node>], gltf_node_index\: [int<class_int>]\ ) |static| [🔗<class_GLTFDocument_method_export_object_model_property>]

Determines a mapping between the given Godot `node_path` and the corresponding glTF Object Model JSON pointer(s) in the generated glTF file. The details of this mapping are returned in a [GLTFObjectModelProperty<class_GLTFObjectModelProperty>] object. Additional mappings can be supplied via the [GLTFDocumentExtension._import_object_model_property()<class_GLTFDocumentExtension_private_method__import_object_model_property>] callback method.


----



[PackedByteArray<class_PackedByteArray>] **generate_buffer**\ (\ state\: [GLTFState<class_GLTFState>]\ ) [🔗<class_GLTFDocument_method_generate_buffer>]

Takes a [GLTFState<class_GLTFState>] object through the `state` parameter and returns a glTF [PackedByteArray<class_PackedByteArray>].


----



[Node<class_Node>] **generate_scene**\ (\ state\: [GLTFState<class_GLTFState>], bake_fps\: [float<class_float>] = 30, trimming\: [bool<class_bool>] = false, remove_immutable_tracks\: [bool<class_bool>] = true\ ) [🔗<class_GLTFDocument_method_generate_scene>]

Takes a [GLTFState<class_GLTFState>] object through the `state` parameter and returns a Godot Engine scene node.

The `bake_fps` parameter overrides the bake_fps in `state`.


----



[PackedStringArray<class_PackedStringArray>] **get_supported_gltf_extensions**\ (\ ) |static| [🔗<class_GLTFDocument_method_get_supported_gltf_extensions>]

Returns a list of all support glTF extensions, including extensions supported directly by the engine, and extensions supported by user plugins registering [GLTFDocumentExtension<class_GLTFDocumentExtension>] classes.

\ **Note:** If this method is run before a GLTFDocumentExtension is registered, its extensions won't be included in the list. Be sure to only run this method after all extensions are registered. If you run this when the engine starts, consider waiting a frame before calling this method to ensure all extensions are registered.


----



[GLTFObjectModelProperty<class_GLTFObjectModelProperty>] **import_object_model_property**\ (\ state\: [GLTFState<class_GLTFState>], json_pointer\: [String<class_String>]\ ) |static| [🔗<class_GLTFDocument_method_import_object_model_property>]

Determines a mapping between the given glTF Object Model `json_pointer` and the corresponding Godot node path(s) in the generated Godot scene. The details of this mapping are returned in a [GLTFObjectModelProperty<class_GLTFObjectModelProperty>] object. Additional mappings can be supplied via the [GLTFDocumentExtension._export_object_model_property()<class_GLTFDocumentExtension_private_method__export_object_model_property>] callback method.


----



|void| **register_gltf_document_extension**\ (\ extension\: [GLTFDocumentExtension<class_GLTFDocumentExtension>], first_priority\: [bool<class_bool>] = false\ ) |static| [🔗<class_GLTFDocument_method_register_gltf_document_extension>]

Registers the given [GLTFDocumentExtension<class_GLTFDocumentExtension>] instance with GLTFDocument. If `first_priority` is `true`, this extension will be run first. Otherwise, it will be run last.

\ **Note:** Like GLTFDocument itself, all GLTFDocumentExtension classes must be stateless in order to function properly. If you need to store data, use the `set_additional_data` and `get_additional_data` methods in [GLTFState<class_GLTFState>] or [GLTFNode<class_GLTFNode>].


----



|void| **unregister_gltf_document_extension**\ (\ extension\: [GLTFDocumentExtension<class_GLTFDocumentExtension>]\ ) |static| [🔗<class_GLTFDocument_method_unregister_gltf_document_extension>]

Unregisters the given [GLTFDocumentExtension<class_GLTFDocumentExtension>] instance.


----



[Error<enum_@GlobalScope_Error>] **write_to_filesystem**\ (\ state\: [GLTFState<class_GLTFState>], path\: [String<class_String>]\ ) [🔗<class_GLTFDocument_method_write_to_filesystem>]

Takes a [GLTFState<class_GLTFState>] object through the `state` parameter and writes a glTF file to the filesystem.

\ **Note:** The extension of the glTF file determines if it is a .glb binary file or a .gltf text file.

