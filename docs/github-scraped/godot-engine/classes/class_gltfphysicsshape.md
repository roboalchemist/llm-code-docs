:github_url: hide



# GLTFPhysicsShape

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Represents a glTF physics shape.


## Description

Represents a physics shape as defined by the `OMI_physics_shape` or `OMI_collider` glTF extensions. This class is an intermediary between the glTF data and Godot's nodes, and it's abstracted in a way that allows adding support for different glTF physics extensions in the future.


## Tutorials

- [../tutorials/io/runtime_file_loading_and_saving](Runtime file loading and saving .md)

- [OMI_physics_shape glTF extension ](https://github.com/omigroup/gltf-extensions/tree/main/extensions/2.0/OMI_physics_shape)_

- [OMI_collider glTF extension ](https://github.com/omigroup/gltf-extensions/tree/main/extensions/2.0/Archived/OMI_collider)_


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------------+---------------------------------------------------------------------+----------------------+
> | :ref:`float<class_float>`               | :ref:`height<class_GLTFPhysicsShape_property_height>`               | ``2.0``              |
> +-----------------------------------------+---------------------------------------------------------------------+----------------------+
> | :ref:`ImporterMesh<class_ImporterMesh>` | :ref:`importer_mesh<class_GLTFPhysicsShape_property_importer_mesh>` |                      |
> +-----------------------------------------+---------------------------------------------------------------------+----------------------+
> | :ref:`bool<class_bool>`                 | :ref:`is_trigger<class_GLTFPhysicsShape_property_is_trigger>`       | ``false``            |
> +-----------------------------------------+---------------------------------------------------------------------+----------------------+
> | :ref:`int<class_int>`                   | :ref:`mesh_index<class_GLTFPhysicsShape_property_mesh_index>`       | ``-1``               |
> +-----------------------------------------+---------------------------------------------------------------------+----------------------+
> | :ref:`float<class_float>`               | :ref:`radius<class_GLTFPhysicsShape_property_radius>`               | ``0.5``              |
> +-----------------------------------------+---------------------------------------------------------------------+----------------------+
> | :ref:`String<class_String>`             | :ref:`shape_type<class_GLTFPhysicsShape_property_shape_type>`       | ``""``               |
> +-----------------------------------------+---------------------------------------------------------------------+----------------------+
> | :ref:`Vector3<class_Vector3>`           | :ref:`size<class_GLTFPhysicsShape_property_size>`                   | ``Vector3(1, 1, 1)`` |
> +-----------------------------------------+---------------------------------------------------------------------+----------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`GLTFPhysicsShape<class_GLTFPhysicsShape>` | :ref:`from_dictionary<class_GLTFPhysicsShape_method_from_dictionary>`\ (\ dictionary\: :ref:`Dictionary<class_Dictionary>`\ ) |static| |
> +-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`GLTFPhysicsShape<class_GLTFPhysicsShape>` | :ref:`from_node<class_GLTFPhysicsShape_method_from_node>`\ (\ shape_node\: :ref:`CollisionShape3D<class_CollisionShape3D>`\ ) |static| |
> +-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`GLTFPhysicsShape<class_GLTFPhysicsShape>` | :ref:`from_resource<class_GLTFPhysicsShape_method_from_resource>`\ (\ shape_resource\: :ref:`Shape3D<class_Shape3D>`\ ) |static|       |
> +-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Dictionary<class_Dictionary>`             | :ref:`to_dictionary<class_GLTFPhysicsShape_method_to_dictionary>`\ (\ ) |const|                                                        |
> +-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`CollisionShape3D<class_CollisionShape3D>` | :ref:`to_node<class_GLTFPhysicsShape_method_to_node>`\ (\ cache_shapes\: :ref:`bool<class_bool>` = false\ )                            |
> +-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Shape3D<class_Shape3D>`                   | :ref:`to_resource<class_GLTFPhysicsShape_method_to_resource>`\ (\ cache_shapes\: :ref:`bool<class_bool>` = false\ )                    |
> +-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[float<class_float>] **height** = `2.0` [🔗<class_GLTFPhysicsShape_property_height>]


- |void| **set_height**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_height**\ (\ )

The height of the shape, in meters. This is only used when the shape type is `"capsule"` or `"cylinder"`. This value should not be negative, and for `"capsule"` it should be at least twice the radius.


----



[ImporterMesh<class_ImporterMesh>] **importer_mesh** [🔗<class_GLTFPhysicsShape_property_importer_mesh>]


- |void| **set_importer_mesh**\ (\ value\: [ImporterMesh<class_ImporterMesh>]\ )
- [ImporterMesh<class_ImporterMesh>] **get_importer_mesh**\ (\ )

The [ImporterMesh<class_ImporterMesh>] resource of the shape. This is only used when the shape type is `"hull"` (convex hull) or `"trimesh"` (concave trimesh).


----



[bool<class_bool>] **is_trigger** = `false` [🔗<class_GLTFPhysicsShape_property_is_trigger>]


- |void| **set_is_trigger**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_is_trigger**\ (\ )

If `true`, indicates that this shape is a trigger. For Godot, this means that the shape should be a child of an [Area3D<class_Area3D>] node.

This is the only variable not used in the [to_node()<class_GLTFPhysicsShape_method_to_node>] method, it's intended to be used alongside when deciding where to add the generated node as a child.


----



[int<class_int>] **mesh_index** = `-1` [🔗<class_GLTFPhysicsShape_property_mesh_index>]


- |void| **set_mesh_index**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_mesh_index**\ (\ )

The index of the shape's mesh in the glTF file. This is only used when the shape type is `"hull"` (convex hull) or `"trimesh"` (concave trimesh).


----



[float<class_float>] **radius** = `0.5` [🔗<class_GLTFPhysicsShape_property_radius>]


- |void| **set_radius**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_radius**\ (\ )

The radius of the shape, in meters. This is only used when the shape type is `"capsule"`, `"cylinder"`, or `"sphere"`. This value should not be negative.


----



[String<class_String>] **shape_type** = `""` [🔗<class_GLTFPhysicsShape_property_shape_type>]


- |void| **set_shape_type**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_shape_type**\ (\ )

The type of shape this shape represents. Valid values are `"box"`, `"capsule"`, `"cylinder"`, `"sphere"`, `"hull"`, and `"trimesh"`.


----



[Vector3<class_Vector3>] **size** = `Vector3(1, 1, 1)` [🔗<class_GLTFPhysicsShape_property_size>]


- |void| **set_size**\ (\ value\: [Vector3<class_Vector3>]\ )
- [Vector3<class_Vector3>] **get_size**\ (\ )

The size of the shape, in meters. This is only used when the shape type is `"box"`, and it represents the `"diameter"` of the box. This value should not be negative.


----


## Method Descriptions



[GLTFPhysicsShape<class_GLTFPhysicsShape>] **from_dictionary**\ (\ dictionary\: [Dictionary<class_Dictionary>]\ ) |static| [🔗<class_GLTFPhysicsShape_method_from_dictionary>]

Creates a new GLTFPhysicsShape instance by parsing the given [Dictionary<class_Dictionary>].


----



[GLTFPhysicsShape<class_GLTFPhysicsShape>] **from_node**\ (\ shape_node\: [CollisionShape3D<class_CollisionShape3D>]\ ) |static| [🔗<class_GLTFPhysicsShape_method_from_node>]

Creates a new GLTFPhysicsShape instance from the given Godot [CollisionShape3D<class_CollisionShape3D>] node.


----



[GLTFPhysicsShape<class_GLTFPhysicsShape>] **from_resource**\ (\ shape_resource\: [Shape3D<class_Shape3D>]\ ) |static| [🔗<class_GLTFPhysicsShape_method_from_resource>]

Creates a new GLTFPhysicsShape instance from the given Godot [Shape3D<class_Shape3D>] resource.


----



[Dictionary<class_Dictionary>] **to_dictionary**\ (\ ) |const| [🔗<class_GLTFPhysicsShape_method_to_dictionary>]

Serializes this GLTFPhysicsShape instance into a [Dictionary<class_Dictionary>] in the format defined by `OMI_physics_shape`.


----



[CollisionShape3D<class_CollisionShape3D>] **to_node**\ (\ cache_shapes\: [bool<class_bool>] = false\ ) [🔗<class_GLTFPhysicsShape_method_to_node>]

Converts this GLTFPhysicsShape instance into a Godot [CollisionShape3D<class_CollisionShape3D>] node.


----



[Shape3D<class_Shape3D>] **to_resource**\ (\ cache_shapes\: [bool<class_bool>] = false\ ) [🔗<class_GLTFPhysicsShape_method_to_resource>]

Converts this GLTFPhysicsShape instance into a Godot [Shape3D<class_Shape3D>] resource.

