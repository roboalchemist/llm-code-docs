:github_url: hide



# OpenXRAnchorTracker

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [OpenXRSpatialEntityTracker<class_OpenXRSpatialEntityTracker>] **<** [XRPositionalTracker<class_XRPositionalTracker>] **<** [XRTracker<class_XRTracker>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Positional tracker for our spatial entity anchor extension.


## Description

Positional tracker for our OpenXR spatial entity anchor extension, it tracks a user defined location in real space and maps it to our virtual space.


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------+------------------------------------------------------+--------+
> | :ref:`String<class_String>` | :ref:`uuid<class_OpenXRAnchorTracker_property_uuid>` | ``""`` |
> +-----------------------------+------------------------------------------------------+--------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------+--------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`has_uuid<class_OpenXRAnchorTracker_method_has_uuid>`\ (\ ) |const| |
> +-------------------------+--------------------------------------------------------------------------+
>

----


## Signals



**uuid_changed**\ (\ ) [🔗<class_OpenXRAnchorTracker_signal_uuid_changed>]

Emitted when the UUID for this anchor was changed.


----


## Property Descriptions



[String<class_String>] **uuid** = `""` [🔗<class_OpenXRAnchorTracker_property_uuid>]


- |void| **set_uuid**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_uuid**\ (\ )

The UUID provided for persistent anchors.


----


## Method Descriptions



[bool<class_bool>] **has_uuid**\ (\ ) |const| [🔗<class_OpenXRAnchorTracker_method_has_uuid>]

Returns `true` if a non-zero UUID is set.

