:github_url: hide



# NavigationServer2DManager

**Inherits:** [Object<class_Object>]

A singleton for managing [NavigationServer2D<class_NavigationServer2D>] implementations.


## Description

**NavigationServer2DManager** is the API for registering [NavigationServer2D<class_NavigationServer2D>] implementations and setting the default implementation.

\ **Note:** It is not possible to switch servers at runtime. This class is only used on startup at the server initialization level.


## Methods

> **TABLE**
> :widths: auto
>
> +--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`register_server<class_NavigationServer2DManager_method_register_server>`\ (\ name\: :ref:`String<class_String>`, create_callback\: :ref:`Callable<class_Callable>`\ ) |
> +--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`set_default_server<class_NavigationServer2DManager_method_set_default_server>`\ (\ name\: :ref:`String<class_String>`, priority\: :ref:`int<class_int>`\ )            |
> +--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



|void| **register_server**\ (\ name\: [String<class_String>], create_callback\: [Callable<class_Callable>]\ ) [🔗<class_NavigationServer2DManager_method_register_server>]

Registers a [NavigationServer2D<class_NavigationServer2D>] implementation by passing a `name` and a [Callable<class_Callable>] that returns a [NavigationServer2D<class_NavigationServer2D>] object.


----



|void| **set_default_server**\ (\ name\: [String<class_String>], priority\: [int<class_int>]\ ) [🔗<class_NavigationServer2DManager_method_set_default_server>]

Sets the default [NavigationServer2D<class_NavigationServer2D>] implementation to the one identified by `name`, if `priority` is greater than the priority of the current default implementation.

