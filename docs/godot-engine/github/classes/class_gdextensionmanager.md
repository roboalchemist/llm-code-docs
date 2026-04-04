:github_url: hide



# GDExtensionManager

**Inherits:** [Object<class_Object>]

Provides access to GDExtension functionality.


## Description

The GDExtensionManager loads, initializes, and keeps track of all available [GDExtension<class_GDExtension>] libraries in the project.

\ **Note:** Do not worry about GDExtension unless you know what you are doing.


## Tutorials

- [../tutorials/scripting/gdextension/what_is_gdextension](GDExtension overview .md)

- [../tutorials/scripting/cpp/gdextension_cpp_example](GDExtension example in C++ .md)


## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`GDExtension<class_GDExtension>`                 | :ref:`get_extension<class_GDExtensionManager_method_get_extension>`\ (\ path\: :ref:`String<class_String>`\ )                                                                                         |
> +-------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedStringArray<class_PackedStringArray>`     | :ref:`get_loaded_extensions<class_GDExtensionManager_method_get_loaded_extensions>`\ (\ ) |const|                                                                                                     |
> +-------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                               | :ref:`is_extension_loaded<class_GDExtensionManager_method_is_extension_loaded>`\ (\ path\: :ref:`String<class_String>`\ ) |const|                                                                     |
> +-------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`LoadStatus<enum_GDExtensionManager_LoadStatus>` | :ref:`load_extension<class_GDExtensionManager_method_load_extension>`\ (\ path\: :ref:`String<class_String>`\ )                                                                                       |
> +-------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`LoadStatus<enum_GDExtensionManager_LoadStatus>` | :ref:`load_extension_from_function<class_GDExtensionManager_method_load_extension_from_function>`\ (\ path\: :ref:`String<class_String>`, init_func\: ``const GDExtensionInitializationFunction*``\ ) |
> +-------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`LoadStatus<enum_GDExtensionManager_LoadStatus>` | :ref:`reload_extension<class_GDExtensionManager_method_reload_extension>`\ (\ path\: :ref:`String<class_String>`\ )                                                                                   |
> +-------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`LoadStatus<enum_GDExtensionManager_LoadStatus>` | :ref:`unload_extension<class_GDExtensionManager_method_unload_extension>`\ (\ path\: :ref:`String<class_String>`\ )                                                                                   |
> +-------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**extension_loaded**\ (\ extension\: [GDExtension<class_GDExtension>]\ ) [🔗<class_GDExtensionManager_signal_extension_loaded>]

Emitted after the editor has finished loading a new extension.

\ **Note:** This signal is only emitted in editor builds.


----



**extension_unloading**\ (\ extension\: [GDExtension<class_GDExtension>]\ ) [🔗<class_GDExtensionManager_signal_extension_unloading>]

Emitted before the editor starts unloading an extension.

\ **Note:** This signal is only emitted in editor builds.


----



**extensions_reloaded**\ (\ ) [🔗<class_GDExtensionManager_signal_extensions_reloaded>]

Emitted after the editor has finished reloading one or more extensions.


----


## Enumerations



enum **LoadStatus**: [🔗<enum_GDExtensionManager_LoadStatus>]



[LoadStatus<enum_GDExtensionManager_LoadStatus>] **LOAD_STATUS_OK** = `0`

The extension has loaded successfully.



[LoadStatus<enum_GDExtensionManager_LoadStatus>] **LOAD_STATUS_FAILED** = `1`

The extension has failed to load, possibly because it does not exist or has missing dependencies.



[LoadStatus<enum_GDExtensionManager_LoadStatus>] **LOAD_STATUS_ALREADY_LOADED** = `2`

The extension has already been loaded.



[LoadStatus<enum_GDExtensionManager_LoadStatus>] **LOAD_STATUS_NOT_LOADED** = `3`

The extension has not been loaded.



[LoadStatus<enum_GDExtensionManager_LoadStatus>] **LOAD_STATUS_NEEDS_RESTART** = `4`

The extension requires the application to restart to fully load.


----


## Method Descriptions



[GDExtension<class_GDExtension>] **get_extension**\ (\ path\: [String<class_String>]\ ) [🔗<class_GDExtensionManager_method_get_extension>]

Returns the [GDExtension<class_GDExtension>] at the given file `path`, or `null` if it has not been loaded or does not exist.


----



[PackedStringArray<class_PackedStringArray>] **get_loaded_extensions**\ (\ ) |const| [🔗<class_GDExtensionManager_method_get_loaded_extensions>]

Returns the file paths of all currently loaded extensions.


----



[bool<class_bool>] **is_extension_loaded**\ (\ path\: [String<class_String>]\ ) |const| [🔗<class_GDExtensionManager_method_is_extension_loaded>]

Returns `true` if the extension at the given file `path` has already been loaded successfully. See also [get_loaded_extensions()<class_GDExtensionManager_method_get_loaded_extensions>].


----



[LoadStatus<enum_GDExtensionManager_LoadStatus>] **load_extension**\ (\ path\: [String<class_String>]\ ) [🔗<class_GDExtensionManager_method_load_extension>]

Loads an extension by absolute file path. The `path` needs to point to a valid [GDExtension<class_GDExtension>]. Returns [LOAD_STATUS_OK<class_GDExtensionManager_constant_LOAD_STATUS_OK>] if successful.


----



[LoadStatus<enum_GDExtensionManager_LoadStatus>] **load_extension_from_function**\ (\ path\: [String<class_String>], init_func\: `const GDExtensionInitializationFunction*`\ ) [🔗<class_GDExtensionManager_method_load_extension_from_function>]

Loads the extension already in address space via the given path and initialization function. The `path` needs to be unique and start with `"libgodot://"`. Returns [LOAD_STATUS_OK<class_GDExtensionManager_constant_LOAD_STATUS_OK>] if successful.


----



[LoadStatus<enum_GDExtensionManager_LoadStatus>] **reload_extension**\ (\ path\: [String<class_String>]\ ) [🔗<class_GDExtensionManager_method_reload_extension>]

Reloads the extension at the given file path. The `path` needs to point to a valid [GDExtension<class_GDExtension>], otherwise this method may return either [LOAD_STATUS_NOT_LOADED<class_GDExtensionManager_constant_LOAD_STATUS_NOT_LOADED>] or [LOAD_STATUS_FAILED<class_GDExtensionManager_constant_LOAD_STATUS_FAILED>].

\ **Note:** You can only reload extensions in the editor. In release builds, this method always fails and returns [LOAD_STATUS_FAILED<class_GDExtensionManager_constant_LOAD_STATUS_FAILED>].


----



[LoadStatus<enum_GDExtensionManager_LoadStatus>] **unload_extension**\ (\ path\: [String<class_String>]\ ) [🔗<class_GDExtensionManager_method_unload_extension>]

Unloads an extension by file path. The `path` needs to point to an already loaded [GDExtension<class_GDExtension>], otherwise this method returns [LOAD_STATUS_NOT_LOADED<class_GDExtensionManager_constant_LOAD_STATUS_NOT_LOADED>].

