:github_url: hide



# FBXState

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [GLTFState<class_GLTFState>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]


## Description

The FBXState handles the state data imported from FBX files.


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------+-----------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>` | :ref:`allow_geometry_helper_nodes<class_FBXState_property_allow_geometry_helper_nodes>` | ``false`` |
> +-------------------------+-----------------------------------------------------------------------------------------+-----------+
>

----


## Property Descriptions



[bool<class_bool>] **allow_geometry_helper_nodes** = `false` [🔗<class_FBXState_property_allow_geometry_helper_nodes>]


- |void| **set_allow_geometry_helper_nodes**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_allow_geometry_helper_nodes**\ (\ )

If `true`, the import process used auxiliary nodes called geometry helper nodes. These nodes help preserve the pivots and transformations of the original 3D model during import.

