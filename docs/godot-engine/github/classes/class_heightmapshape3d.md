:github_url: hide



# HeightMapShape3D

**Inherits:** [Shape3D<class_Shape3D>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A 3D heightmap shape used for physics collision.


## Description

A 3D heightmap shape, intended for use in physics to provide a shape for a [CollisionShape3D<class_CollisionShape3D>]. This type is most commonly used for terrain with vertices placed in a fixed-width grid.

The heightmap is represented as a 2D grid of height values, which represent the position of grid points on the Y axis. Grid points are spaced 1 unit apart on the X and Z axes, and the grid is centered on the origin of the [CollisionShape3D<class_CollisionShape3D>] node. Internally, each grid square is divided into two triangles.

Due to the nature of the heightmap, it cannot be used to model overhangs or caves, which would require multiple vertices at the same vertical location. Holes can be punched through the collision by assigning [@GDScript.NAN<class_@GDScript_constant_NAN>] to the height of the desired vertices (this is supported in both GodotPhysics3D and Jolt Physics). You could then insert meshes with their own separate collision to provide overhangs, caves, and so on.

\ **Performance:** **HeightMapShape3D** is faster to check collisions against than [ConcavePolygonShape3D<class_ConcavePolygonShape3D>], but it is significantly slower than primitive shapes like [BoxShape3D<class_BoxShape3D>].

A heightmap collision shape can also be built by using an [Image<class_Image>] reference:


> **TABS**
>

    var heightmap_texture = ResourceLoader.load("res://heightmap_image.exr")
    var heightmap_image = heightmap_texture.get_image()
    heightmap_image.convert(Image.FORMAT_RF)

    var height_min = 0.0
    var height_max = 10.0

    update_map_data_from_image(heightmap_image, height_min, height_max)



\ **Note:** If you need to use a spacing different than 1 unit, you can adjust the [Node3D.scale<class_Node3D_property_scale>] of the shape. However, keep in mind that GodotPhysics3D does not support non-uniform scaling: you'll need to scale the Y axis by the same amount as the X and Z axes, which means the values in [map_data<class_HeightMapShape3D_property_map_data>] will need to be pre-scaled by the inverse of that scale. Also note that GodotPhysics3D does not support scaling at all for dynamic bodies (that is, non-frozen [RigidBody3D<class_RigidBody3D>] nodes); to use a scaled **HeightMapShape3D** with those, you will need to use Jolt Physics.


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------+-------------------------------------------------------------+------------------------------------+
> | :ref:`PackedFloat32Array<class_PackedFloat32Array>` | :ref:`map_data<class_HeightMapShape3D_property_map_data>`   | ``PackedFloat32Array(0, 0, 0, 0)`` |
> +-----------------------------------------------------+-------------------------------------------------------------+------------------------------------+
> | :ref:`int<class_int>`                               | :ref:`map_depth<class_HeightMapShape3D_property_map_depth>` | ``2``                              |
> +-----------------------------------------------------+-------------------------------------------------------------+------------------------------------+
> | :ref:`int<class_int>`                               | :ref:`map_width<class_HeightMapShape3D_property_map_width>` | ``2``                              |
> +-----------------------------------------------------+-------------------------------------------------------------+------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>` | :ref:`get_max_height<class_HeightMapShape3D_method_get_max_height>`\ (\ ) |const|                                                                                                                                    |
> +---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>` | :ref:`get_min_height<class_HeightMapShape3D_method_get_min_height>`\ (\ ) |const|                                                                                                                                    |
> +---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                    | :ref:`update_map_data_from_image<class_HeightMapShape3D_method_update_map_data_from_image>`\ (\ image\: :ref:`Image<class_Image>`, height_min\: :ref:`float<class_float>`, height_max\: :ref:`float<class_float>`\ ) |
> +---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[PackedFloat32Array<class_PackedFloat32Array>] **map_data** = `PackedFloat32Array(0, 0, 0, 0)` [🔗<class_HeightMapShape3D_property_map_data>]


- |void| **set_map_data**\ (\ value\: [PackedFloat32Array<class_PackedFloat32Array>]\ )
- [PackedFloat32Array<class_PackedFloat32Array>] **get_map_data**\ (\ )

Heightmap data. The array's size must be equal to [map_width<class_HeightMapShape3D_property_map_width>] multiplied by [map_depth<class_HeightMapShape3D_property_map_depth>].

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedFloat32Array<class_PackedFloat32Array>] for more details.


----



[int<class_int>] **map_depth** = `2` [🔗<class_HeightMapShape3D_property_map_depth>]


- |void| **set_map_depth**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_map_depth**\ (\ )

Number of vertices in the depth of the heightmap. Changing this will resize the [map_data<class_HeightMapShape3D_property_map_data>].


----



[int<class_int>] **map_width** = `2` [🔗<class_HeightMapShape3D_property_map_width>]


- |void| **set_map_width**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_map_width**\ (\ )

Number of vertices in the width of the heightmap. Changing this will resize the [map_data<class_HeightMapShape3D_property_map_data>].


----


## Method Descriptions



[float<class_float>] **get_max_height**\ (\ ) |const| [🔗<class_HeightMapShape3D_method_get_max_height>]

Returns the largest height value found in [map_data<class_HeightMapShape3D_property_map_data>]. Recalculates only when [map_data<class_HeightMapShape3D_property_map_data>] changes.


----



[float<class_float>] **get_min_height**\ (\ ) |const| [🔗<class_HeightMapShape3D_method_get_min_height>]

Returns the smallest height value found in [map_data<class_HeightMapShape3D_property_map_data>]. Recalculates only when [map_data<class_HeightMapShape3D_property_map_data>] changes.


----



|void| **update_map_data_from_image**\ (\ image\: [Image<class_Image>], height_min\: [float<class_float>], height_max\: [float<class_float>]\ ) [🔗<class_HeightMapShape3D_method_update_map_data_from_image>]

Updates [map_data<class_HeightMapShape3D_property_map_data>] with data read from an [Image<class_Image>] reference. Automatically resizes heightmap [map_width<class_HeightMapShape3D_property_map_width>] and [map_depth<class_HeightMapShape3D_property_map_depth>] to fit the full image width and height.

The image needs to be in either [Image.FORMAT_RF<class_Image_constant_FORMAT_RF>] (32 bit), [Image.FORMAT_RH<class_Image_constant_FORMAT_RH>] (16 bit), or [Image.FORMAT_R8<class_Image_constant_FORMAT_R8>] (8 bit).

Each image pixel is read in as a float on the range from `0.0` (black pixel) to `1.0` (white pixel). This range value gets remapped to `height_min` and `height_max` to form the final height value.

\ **Note:** Using a heightmap with 16-bit or 32-bit data, stored in EXR or HDR format is recommended. Using 8-bit height data, or a format like PNG that Godot imports as 8-bit, will result in a terraced terrain.

