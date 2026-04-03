:github_url: hide



# GDExtension

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A native library for GDExtension.


## Description

The **GDExtension** resource type represents a [shared library ](https://en.wikipedia.org/wiki/Shared_library)_ which can expand the functionality of the engine. The [GDExtensionManager<class_GDExtensionManager>] singleton is responsible for loading, reloading, and unloading **GDExtension** resources.

\ **Note:** GDExtension itself is not a scripting language and has no relation to [GDScript<class_GDScript>] resources.


## Tutorials

- [../tutorials/scripting/gdextension/what_is_gdextension](GDExtension overview .md)

- [../tutorials/scripting/cpp/gdextension_cpp_example](GDExtension example in C++ .md)


## Methods

> **TABLE**
> :widths: auto
>
> +------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`InitializationLevel<enum_GDExtension_InitializationLevel>` | :ref:`get_minimum_library_initialization_level<class_GDExtension_method_get_minimum_library_initialization_level>`\ (\ ) |const| |
> +------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`is_library_open<class_GDExtension_method_is_library_open>`\ (\ ) |const|                                                   |
> +------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **InitializationLevel**: [🔗<enum_GDExtension_InitializationLevel>]



[InitializationLevel<enum_GDExtension_InitializationLevel>] **INITIALIZATION_LEVEL_CORE** = `0`

The library is initialized at the same time as the core features of the engine.



[InitializationLevel<enum_GDExtension_InitializationLevel>] **INITIALIZATION_LEVEL_SERVERS** = `1`

The library is initialized at the same time as the engine's servers (such as [RenderingServer<class_RenderingServer>] or [PhysicsServer3D<class_PhysicsServer3D>]).



[InitializationLevel<enum_GDExtension_InitializationLevel>] **INITIALIZATION_LEVEL_SCENE** = `2`

The library is initialized at the same time as the engine's scene-related classes.



[InitializationLevel<enum_GDExtension_InitializationLevel>] **INITIALIZATION_LEVEL_EDITOR** = `3`

The library is initialized at the same time as the engine's editor classes. Only happens when loading the GDExtension in the editor.


----


## Method Descriptions



[InitializationLevel<enum_GDExtension_InitializationLevel>] **get_minimum_library_initialization_level**\ (\ ) |const| [🔗<class_GDExtension_method_get_minimum_library_initialization_level>]

Returns the lowest level required for this extension to be properly initialized (see the [InitializationLevel<enum_GDExtension_InitializationLevel>] enum).


----



[bool<class_bool>] **is_library_open**\ (\ ) |const| [🔗<class_GDExtension_method_is_library_open>]

Returns `true` if this extension's library has been opened.

