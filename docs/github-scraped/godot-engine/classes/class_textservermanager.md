:github_url: hide



# TextServerManager

**Inherits:** [Object<class_Object>]

A singleton for managing [TextServer<class_TextServer>] implementations.


## Description

**TextServerManager** is the API backend for loading, enumerating, and switching [TextServer<class_TextServer>]\ s.

\ **Note:** Switching text server at runtime is possible, but will invalidate all fonts and text buffers. Make sure to unload all controls, fonts, and themes before doing so.


## Methods

> **TABLE**
> :widths: auto
>
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`add_interface<class_TextServerManager_method_add_interface>`\ (\ interface\: :ref:`TextServer<class_TextServer>`\ )             |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`TextServer<class_TextServer>`                              | :ref:`find_interface<class_TextServerManager_method_find_interface>`\ (\ name\: :ref:`String<class_String>`\ ) |const|                |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`TextServer<class_TextServer>`                              | :ref:`get_interface<class_TextServerManager_method_get_interface>`\ (\ idx\: :ref:`int<class_int>`\ ) |const|                         |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                            | :ref:`get_interface_count<class_TextServerManager_method_get_interface_count>`\ (\ ) |const|                                          |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`Dictionary<class_Dictionary>`\] | :ref:`get_interfaces<class_TextServerManager_method_get_interfaces>`\ (\ ) |const|                                                    |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`TextServer<class_TextServer>`                              | :ref:`get_primary_interface<class_TextServerManager_method_get_primary_interface>`\ (\ ) |const|                                      |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`remove_interface<class_TextServerManager_method_remove_interface>`\ (\ interface\: :ref:`TextServer<class_TextServer>`\ )       |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`set_primary_interface<class_TextServerManager_method_set_primary_interface>`\ (\ index\: :ref:`TextServer<class_TextServer>`\ ) |
> +------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**interface_added**\ (\ interface_name\: [StringName<class_StringName>]\ ) [🔗<class_TextServerManager_signal_interface_added>]

Emitted when a new interface has been added.


----



**interface_removed**\ (\ interface_name\: [StringName<class_StringName>]\ ) [🔗<class_TextServerManager_signal_interface_removed>]

Emitted when an interface is removed.


----


## Method Descriptions



|void| **add_interface**\ (\ interface\: [TextServer<class_TextServer>]\ ) [🔗<class_TextServerManager_method_add_interface>]

Registers a [TextServer<class_TextServer>] interface.


----



[TextServer<class_TextServer>] **find_interface**\ (\ name\: [String<class_String>]\ ) |const| [🔗<class_TextServerManager_method_find_interface>]

Finds an interface by its `name`.


----



[TextServer<class_TextServer>] **get_interface**\ (\ idx\: [int<class_int>]\ ) |const| [🔗<class_TextServerManager_method_get_interface>]

Returns the interface registered at a given index.


----



[int<class_int>] **get_interface_count**\ (\ ) |const| [🔗<class_TextServerManager_method_get_interface_count>]

Returns the number of interfaces currently registered.


----



[Array<class_Array>]\[[Dictionary<class_Dictionary>]\] **get_interfaces**\ (\ ) |const| [🔗<class_TextServerManager_method_get_interfaces>]

Returns a list of available interfaces, with the index and name of each interface.


----



[TextServer<class_TextServer>] **get_primary_interface**\ (\ ) |const| [🔗<class_TextServerManager_method_get_primary_interface>]

Returns the primary [TextServer<class_TextServer>] interface currently in use.


----



|void| **remove_interface**\ (\ interface\: [TextServer<class_TextServer>]\ ) [🔗<class_TextServerManager_method_remove_interface>]

Removes an interface. All fonts and shaped text caches should be freed before removing an interface.


----



|void| **set_primary_interface**\ (\ index\: [TextServer<class_TextServer>]\ ) [🔗<class_TextServerManager_method_set_primary_interface>]

Sets the primary [TextServer<class_TextServer>] interface.

