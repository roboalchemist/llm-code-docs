:github_url: hide



# PhysicsServer3DManager

**Inherits:** [Object<class_Object>]

A singleton for managing [PhysicsServer3D<class_PhysicsServer3D>] implementations.


## Description

**PhysicsServer3DManager** is the API for registering [PhysicsServer3D<class_PhysicsServer3D>] implementations and for setting the default implementation.

\ **Note:** It is not possible to switch physics servers at runtime. This class is only used on startup at the server initialization level, by Godot itself and possibly by GDExtensions.


## Methods

> **TABLE**
> :widths: auto
>
> +--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`register_server<class_PhysicsServer3DManager_method_register_server>`\ (\ name\: :ref:`String<class_String>`, create_callback\: :ref:`Callable<class_Callable>`\ ) |
> +--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`set_default_server<class_PhysicsServer3DManager_method_set_default_server>`\ (\ name\: :ref:`String<class_String>`, priority\: :ref:`int<class_int>`\ )            |
> +--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



|void| **register_server**\ (\ name\: [String<class_String>], create_callback\: [Callable<class_Callable>]\ ) [🔗<class_PhysicsServer3DManager_method_register_server>]

Register a [PhysicsServer3D<class_PhysicsServer3D>] implementation by passing a `name` and a [Callable<class_Callable>] that returns a [PhysicsServer3D<class_PhysicsServer3D>] object.


----



|void| **set_default_server**\ (\ name\: [String<class_String>], priority\: [int<class_int>]\ ) [🔗<class_PhysicsServer3DManager_method_set_default_server>]

Set the default [PhysicsServer3D<class_PhysicsServer3D>] implementation to the one identified by `name`, if `priority` is greater than the priority of the current default implementation.

