:github_url: hide



# GLTFMesh

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

GLTFMesh represents a glTF mesh.


## Description

GLTFMesh handles 3D mesh data imported from glTF files. It includes properties for blend channels, blend weights, instance materials, and the mesh itself.


## Tutorials

- [../tutorials/io/runtime_file_loading_and_saving](Runtime file loading and saving .md)


## Properties

> **TABLE**
> :widths: auto
>
> +--------------------------------------------------------------+-----------------------------------------------------------------------+--------------------------+
> | :ref:`PackedFloat32Array<class_PackedFloat32Array>`          | :ref:`blend_weights<class_GLTFMesh_property_blend_weights>`           | ``PackedFloat32Array()`` |
> +--------------------------------------------------------------+-----------------------------------------------------------------------+--------------------------+
> | :ref:`Array<class_Array>`\[:ref:`Material<class_Material>`\] | :ref:`instance_materials<class_GLTFMesh_property_instance_materials>` | ``[]``                   |
> +--------------------------------------------------------------+-----------------------------------------------------------------------+--------------------------+
> | :ref:`ImporterMesh<class_ImporterMesh>`                      | :ref:`mesh<class_GLTFMesh_property_mesh>`                             |                          |
> +--------------------------------------------------------------+-----------------------------------------------------------------------+--------------------------+
> | :ref:`String<class_String>`                                  | :ref:`original_name<class_GLTFMesh_property_original_name>`           | ``""``                   |
> +--------------------------------------------------------------+-----------------------------------------------------------------------+--------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>` | :ref:`get_additional_data<class_GLTFMesh_method_get_additional_data>`\ (\ extension_name\: :ref:`StringName<class_StringName>`\ )                                                  |
> +-------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`set_additional_data<class_GLTFMesh_method_set_additional_data>`\ (\ extension_name\: :ref:`StringName<class_StringName>`, additional_data\: :ref:`Variant<class_Variant>`\ ) |
> +-------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[PackedFloat32Array<class_PackedFloat32Array>] **blend_weights** = `PackedFloat32Array()` [🔗<class_GLTFMesh_property_blend_weights>]


- |void| **set_blend_weights**\ (\ value\: [PackedFloat32Array<class_PackedFloat32Array>]\ )
- [PackedFloat32Array<class_PackedFloat32Array>] **get_blend_weights**\ (\ )

An array of floats representing the blend weights of the mesh.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedFloat32Array<class_PackedFloat32Array>] for more details.


----



[Array<class_Array>]\[[Material<class_Material>]\] **instance_materials** = `[]` [🔗<class_GLTFMesh_property_instance_materials>]


- |void| **set_instance_materials**\ (\ value\: [Array<class_Array>]\[[Material<class_Material>]\]\ )
- [Array<class_Array>]\[[Material<class_Material>]\] **get_instance_materials**\ (\ )

An array of Material objects representing the materials used in the mesh.


----



[ImporterMesh<class_ImporterMesh>] **mesh** [🔗<class_GLTFMesh_property_mesh>]


- |void| **set_mesh**\ (\ value\: [ImporterMesh<class_ImporterMesh>]\ )
- [ImporterMesh<class_ImporterMesh>] **get_mesh**\ (\ )

The [ImporterMesh<class_ImporterMesh>] object representing the mesh itself.


----



[String<class_String>] **original_name** = `""` [🔗<class_GLTFMesh_property_original_name>]


- |void| **set_original_name**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_original_name**\ (\ )

The original name of the mesh.


----


## Method Descriptions



[Variant<class_Variant>] **get_additional_data**\ (\ extension_name\: [StringName<class_StringName>]\ ) [🔗<class_GLTFMesh_method_get_additional_data>]

Gets additional arbitrary data in this **GLTFMesh** instance. This can be used to keep per-node state data in [GLTFDocumentExtension<class_GLTFDocumentExtension>] classes, which is important because they are stateless.

The argument should be the [GLTFDocumentExtension<class_GLTFDocumentExtension>] name (does not have to match the extension name in the glTF file), and the return value can be anything you set. If nothing was set, the return value is `null`.


----



|void| **set_additional_data**\ (\ extension_name\: [StringName<class_StringName>], additional_data\: [Variant<class_Variant>]\ ) [🔗<class_GLTFMesh_method_set_additional_data>]

Sets additional arbitrary data in this **GLTFMesh** instance. This can be used to keep per-node state data in [GLTFDocumentExtension<class_GLTFDocumentExtension>] classes, which is important because they are stateless.

The first argument should be the [GLTFDocumentExtension<class_GLTFDocumentExtension>] name (does not have to match the extension name in the glTF file), and the second argument can be anything you want.

