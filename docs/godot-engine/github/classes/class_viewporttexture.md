:github_url: hide



# ViewportTexture

**Inherits:** [Texture2D<class_Texture2D>] **<** [Texture<class_Texture>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Provides the content of a [Viewport<class_Viewport>] as a dynamic texture.


## Description

A **ViewportTexture** provides the content of a [Viewport<class_Viewport>] as a dynamic [Texture2D<class_Texture2D>]. This can be used to combine the rendering of [Control<class_Control>], [Node2D<class_Node2D>] and [Node3D<class_Node3D>] nodes. For example, you can use this texture to display a 3D scene inside a [TextureRect<class_TextureRect>], or a 2D overlay in a [Sprite3D<class_Sprite3D>].

To get a **ViewportTexture** in code, use the [Viewport.get_texture()<class_Viewport_method_get_texture>] method on the target viewport.

\ **Note:** A **ViewportTexture** is always local to its scene (see [Resource.resource_local_to_scene<class_Resource_property_resource_local_to_scene>]). If the scene root is not ready, it may return incorrect data (see [Node.ready<class_Node_signal_ready>]).

\ **Note:** Instantiating scenes containing a high-resolution **ViewportTexture** may cause noticeable stutter.

\ **Note:** When using a [Viewport<class_Viewport>] with [Viewport.use_hdr_2d<class_Viewport_property_use_hdr_2d>] set to `true`, the returned texture will be an HDR image that uses linear encoding. This may look darker than normal when displayed directly on screen. To convert to nonlinear sRGB encoding, you can do the following:

::

    img.convert(Image.FORMAT_RGBA8)
    img.linear_to_srgb()

\ **Note:** Some nodes such as [Decal<class_Decal>], [Light3D<class_Light3D>], and [PointLight2D<class_PointLight2D>] do not support using **ViewportTexture** directly. To use texture data from a **ViewportTexture** in these nodes, you need to create an [ImageTexture<class_ImageTexture>] by calling [Texture2D.get_image()<class_Texture2D_method_get_image>] on the **ViewportTexture** and passing the result to [ImageTexture.create_from_image()<class_ImageTexture_method_create_from_image>]. This conversion is a slow operation, so it should not be performed every frame.


## Tutorials

- [GUI in 3D Viewport Demo ](https://godotengine.org/asset-library/asset/2807)_

- [3D in 2D Viewport Demo ](https://godotengine.org/asset-library/asset/2804)_

- [2D in 3D Viewport Demo ](https://godotengine.org/asset-library/asset/2803)_

- [3D Resolution Scaling Demo ](https://godotengine.org/asset-library/asset/2805)_


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------+--------------------------------------------------------------------+------------------+
> | :ref:`NodePath<class_NodePath>` | :ref:`viewport_path<class_ViewportTexture_property_viewport_path>` | ``NodePath("")`` |
> +---------------------------------+--------------------------------------------------------------------+------------------+
>

----


## Property Descriptions



[NodePath<class_NodePath>] **viewport_path** = `NodePath("")` [🔗<class_ViewportTexture_property_viewport_path>]


- |void| **set_viewport_path_in_scene**\ (\ value\: [NodePath<class_NodePath>]\ )
- [NodePath<class_NodePath>] **get_viewport_path_in_scene**\ (\ )

The path to the [Viewport<class_Viewport>] node to display. This is relative to the local scene root (see [Resource.get_local_scene()<class_Resource_method_get_local_scene>]), **not** to the nodes that use this texture.

\ **Note:** In the editor, this path is automatically updated when the target viewport or one of its ancestors is renamed or moved. At runtime, this path may not automatically update if the scene root cannot be found.

