:github_url: hide



# GLTFPhysicsBody

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Represents a glTF physics body.


## Description

Represents a physics body as an intermediary between the `OMI_physics_body` glTF data and Godot's nodes, and it's abstracted in a way that allows adding support for different glTF physics extensions in the future.


## Tutorials

- [../tutorials/io/runtime_file_loading_and_saving](Runtime file loading and saving .md)

- [OMI_physics_body glTF extension ](https://github.com/omigroup/gltf-extensions/tree/main/extensions/2.0/OMI_physics_body)_


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------------+--------------------------------------------------------------------------------+--------------------------------------+
> | :ref:`Vector3<class_Vector3>`       | :ref:`angular_velocity<class_GLTFPhysicsBody_property_angular_velocity>`       | ``Vector3(0, 0, 0)``                 |
> +-------------------------------------+--------------------------------------------------------------------------------+--------------------------------------+
> | :ref:`String<class_String>`         | :ref:`body_type<class_GLTFPhysicsBody_property_body_type>`                     | ``"rigid"``                          |
> +-------------------------------------+--------------------------------------------------------------------------------+--------------------------------------+
> | :ref:`Vector3<class_Vector3>`       | :ref:`center_of_mass<class_GLTFPhysicsBody_property_center_of_mass>`           | ``Vector3(0, 0, 0)``                 |
> +-------------------------------------+--------------------------------------------------------------------------------+--------------------------------------+
> | :ref:`Vector3<class_Vector3>`       | :ref:`inertia_diagonal<class_GLTFPhysicsBody_property_inertia_diagonal>`       | ``Vector3(0, 0, 0)``                 |
> +-------------------------------------+--------------------------------------------------------------------------------+--------------------------------------+
> | :ref:`Quaternion<class_Quaternion>` | :ref:`inertia_orientation<class_GLTFPhysicsBody_property_inertia_orientation>` | ``Quaternion(0, 0, 0, 1)``           |
> +-------------------------------------+--------------------------------------------------------------------------------+--------------------------------------+
> | :ref:`Basis<class_Basis>`           | :ref:`inertia_tensor<class_GLTFPhysicsBody_property_inertia_tensor>`           | ``Basis(0, 0, 0, 0, 0, 0, 0, 0, 0)`` |
> +-------------------------------------+--------------------------------------------------------------------------------+--------------------------------------+
> | :ref:`Vector3<class_Vector3>`       | :ref:`linear_velocity<class_GLTFPhysicsBody_property_linear_velocity>`         | ``Vector3(0, 0, 0)``                 |
> +-------------------------------------+--------------------------------------------------------------------------------+--------------------------------------+
> | :ref:`float<class_float>`           | :ref:`mass<class_GLTFPhysicsBody_property_mass>`                               | ``1.0``                              |
> +-------------------------------------+--------------------------------------------------------------------------------+--------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`GLTFPhysicsBody<class_GLTFPhysicsBody>`     | :ref:`from_dictionary<class_GLTFPhysicsBody_method_from_dictionary>`\ (\ dictionary\: :ref:`Dictionary<class_Dictionary>`\ ) |static|  |
> +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`GLTFPhysicsBody<class_GLTFPhysicsBody>`     | :ref:`from_node<class_GLTFPhysicsBody_method_from_node>`\ (\ body_node\: :ref:`CollisionObject3D<class_CollisionObject3D>`\ ) |static| |
> +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Dictionary<class_Dictionary>`               | :ref:`to_dictionary<class_GLTFPhysicsBody_method_to_dictionary>`\ (\ ) |const|                                                         |
> +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`CollisionObject3D<class_CollisionObject3D>` | :ref:`to_node<class_GLTFPhysicsBody_method_to_node>`\ (\ ) |const|                                                                     |
> +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[Vector3<class_Vector3>] **angular_velocity** = `Vector3(0, 0, 0)` [🔗<class_GLTFPhysicsBody_property_angular_velocity>]


- |void| **set_angular_velocity**\ (\ value\: [Vector3<class_Vector3>]\ )
- [Vector3<class_Vector3>] **get_angular_velocity**\ (\ )

The angular velocity of the physics body, in radians per second. This is only used when the body type is "rigid" or "vehicle".


----



[String<class_String>] **body_type** = `"rigid"` [🔗<class_GLTFPhysicsBody_property_body_type>]


- |void| **set_body_type**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_body_type**\ (\ )

The type of the body.

When importing, this controls what type of [CollisionObject3D<class_CollisionObject3D>] node Godot should generate. Valid values are `"static"`, `"animatable"`, `"character"`, `"rigid"`, `"vehicle"`, and `"trigger"`.

When exporting, this will be squashed down to one of `"static"`, `"kinematic"`, or `"dynamic"` motion types, or the `"trigger"` property.


----



[Vector3<class_Vector3>] **center_of_mass** = `Vector3(0, 0, 0)` [🔗<class_GLTFPhysicsBody_property_center_of_mass>]


- |void| **set_center_of_mass**\ (\ value\: [Vector3<class_Vector3>]\ )
- [Vector3<class_Vector3>] **get_center_of_mass**\ (\ )

The center of mass of the body, in meters. This is in local space relative to the body. By default, the center of the mass is the body's origin.


----



[Vector3<class_Vector3>] **inertia_diagonal** = `Vector3(0, 0, 0)` [🔗<class_GLTFPhysicsBody_property_inertia_diagonal>]


- |void| **set_inertia_diagonal**\ (\ value\: [Vector3<class_Vector3>]\ )
- [Vector3<class_Vector3>] **get_inertia_diagonal**\ (\ )

The inertia strength of the physics body, in kilogram meter squared (kg⋅m²). This represents the inertia around the principle axes, the diagonal of the inertia tensor matrix. This is only used when the body type is "rigid" or "vehicle".

When converted to a Godot [RigidBody3D<class_RigidBody3D>] node, if this value is zero, then the inertia will be calculated automatically.


----



[Quaternion<class_Quaternion>] **inertia_orientation** = `Quaternion(0, 0, 0, 1)` [🔗<class_GLTFPhysicsBody_property_inertia_orientation>]


- |void| **set_inertia_orientation**\ (\ value\: [Quaternion<class_Quaternion>]\ )
- [Quaternion<class_Quaternion>] **get_inertia_orientation**\ (\ )

The inertia orientation of the physics body. This defines the rotation of the inertia's principle axes relative to the object's local axes. This is only used when the body type is "rigid" or "vehicle" and [inertia_diagonal<class_GLTFPhysicsBody_property_inertia_diagonal>] is set to a non-zero value.


----



[Basis<class_Basis>] **inertia_tensor** = `Basis(0, 0, 0, 0, 0, 0, 0, 0, 0)` [🔗<class_GLTFPhysicsBody_property_inertia_tensor>]


- |void| **set_inertia_tensor**\ (\ value\: [Basis<class_Basis>]\ )
- [Basis<class_Basis>] **get_inertia_tensor**\ (\ )

**Deprecated:** This property may be changed or removed in future versions.

The inertia tensor of the physics body, in kilogram meter squared (kg⋅m²). This is only used when the body type is "rigid" or "vehicle".

When converted to a Godot [RigidBody3D<class_RigidBody3D>] node, if this value is zero, then the inertia will be calculated automatically.


----



[Vector3<class_Vector3>] **linear_velocity** = `Vector3(0, 0, 0)` [🔗<class_GLTFPhysicsBody_property_linear_velocity>]


- |void| **set_linear_velocity**\ (\ value\: [Vector3<class_Vector3>]\ )
- [Vector3<class_Vector3>] **get_linear_velocity**\ (\ )

The linear velocity of the physics body, in meters per second. This is only used when the body type is "rigid" or "vehicle".


----



[float<class_float>] **mass** = `1.0` [🔗<class_GLTFPhysicsBody_property_mass>]


- |void| **set_mass**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_mass**\ (\ )

The mass of the physics body, in kilograms. This is only used when the body type is "rigid" or "vehicle".


----


## Method Descriptions



[GLTFPhysicsBody<class_GLTFPhysicsBody>] **from_dictionary**\ (\ dictionary\: [Dictionary<class_Dictionary>]\ ) |static| [🔗<class_GLTFPhysicsBody_method_from_dictionary>]

Creates a new GLTFPhysicsBody instance by parsing the given [Dictionary<class_Dictionary>] in the `OMI_physics_body` glTF extension format.


----



[GLTFPhysicsBody<class_GLTFPhysicsBody>] **from_node**\ (\ body_node\: [CollisionObject3D<class_CollisionObject3D>]\ ) |static| [🔗<class_GLTFPhysicsBody_method_from_node>]

Creates a new GLTFPhysicsBody instance from the given Godot [CollisionObject3D<class_CollisionObject3D>] node.


----



[Dictionary<class_Dictionary>] **to_dictionary**\ (\ ) |const| [🔗<class_GLTFPhysicsBody_method_to_dictionary>]

Serializes this GLTFPhysicsBody instance into a [Dictionary<class_Dictionary>]. It will be in the format expected by the `OMI_physics_body` glTF extension.


----



[CollisionObject3D<class_CollisionObject3D>] **to_node**\ (\ ) |const| [🔗<class_GLTFPhysicsBody_method_to_node>]

Converts this GLTFPhysicsBody instance into a Godot [CollisionObject3D<class_CollisionObject3D>] node.

