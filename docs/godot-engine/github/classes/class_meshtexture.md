:github_url: hide



# MeshTexture

**Inherits:** [Texture2D<class_Texture2D>] **<** [Texture<class_Texture>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Simple texture that uses a mesh to draw itself.


## Description

Simple texture that uses a mesh to draw itself. It's limited because flags can't be changed and region drawing is not supported.


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------+--------------------------------------------------------------+----------------------------------------------------------------------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`base_texture<class_MeshTexture_property_base_texture>` |                                                                                        |
> +-----------------------------------+--------------------------------------------------------------+----------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>`     | :ref:`image_size<class_MeshTexture_property_image_size>`     | ``Vector2(0, 0)``                                                                      |
> +-----------------------------------+--------------------------------------------------------------+----------------------------------------------------------------------------------------+
> | :ref:`Mesh<class_Mesh>`           | :ref:`mesh<class_MeshTexture_property_mesh>`                 |                                                                                        |
> +-----------------------------------+--------------------------------------------------------------+----------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`           | resource_local_to_scene                                      | ``false`` (overrides :ref:`Resource<class_Resource_property_resource_local_to_scene>`) |
> +-----------------------------------+--------------------------------------------------------------+----------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[Texture2D<class_Texture2D>] **base_texture** [🔗<class_MeshTexture_property_base_texture>]


- |void| **set_base_texture**\ (\ value\: [Texture2D<class_Texture2D>]\ )
- [Texture2D<class_Texture2D>] **get_base_texture**\ (\ )

Sets the base texture that the Mesh will use to draw.


----



[Vector2<class_Vector2>] **image_size** = `Vector2(0, 0)` [🔗<class_MeshTexture_property_image_size>]


- |void| **set_image_size**\ (\ value\: [Vector2<class_Vector2>]\ )
- [Vector2<class_Vector2>] **get_image_size**\ (\ )

Sets the size of the image, needed for reference.


----



[Mesh<class_Mesh>] **mesh** [🔗<class_MeshTexture_property_mesh>]


- |void| **set_mesh**\ (\ value\: [Mesh<class_Mesh>]\ )
- [Mesh<class_Mesh>] **get_mesh**\ (\ )

Sets the mesh used to draw. It must be a mesh using 2D vertices.

