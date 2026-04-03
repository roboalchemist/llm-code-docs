:github_url: hide



# XRControllerTracker

**Inherits:** [XRPositionalTracker<class_XRPositionalTracker>] **<** [XRTracker<class_XRTracker>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A tracked controller.


## Description

An instance of this object represents a controller that is tracked.

As controllers are turned on and the [XRInterface<class_XRInterface>] detects them, instances of this object are automatically added to this list of active tracking objects accessible through the [XRServer<class_XRServer>].

The [XRController3D<class_XRController3D>] consumes objects of this type and should be used in your project.


## Tutorials

- [../tutorials/xr/index](XR documentation index .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------+------+-------------------------------------------------------------------+
> | :ref:`TrackerType<enum_XRServer_TrackerType>` | type | ``2`` (overrides :ref:`XRTracker<class_XRTracker_property_type>`) |
> +-----------------------------------------------+------+-------------------------------------------------------------------+
>
