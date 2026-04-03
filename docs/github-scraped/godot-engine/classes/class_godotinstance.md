:github_url: hide



# GodotInstance

**Inherits:** [Object<class_Object>]

Provides access to an embedded Godot instance.


## Description

GodotInstance represents a running Godot instance that is controlled from an outside codebase, without a perpetual main loop. It is created by the C API `libgodot_create_godot_instance`. Only one may be created per process.


## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------+----------------------------------------------------------------+
> | |void|                  | :ref:`focus_in<class_GodotInstance_method_focus_in>`\ (\ )     |
> +-------------------------+----------------------------------------------------------------+
> | |void|                  | :ref:`focus_out<class_GodotInstance_method_focus_out>`\ (\ )   |
> +-------------------------+----------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`is_started<class_GodotInstance_method_is_started>`\ (\ ) |
> +-------------------------+----------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`iteration<class_GodotInstance_method_iteration>`\ (\ )   |
> +-------------------------+----------------------------------------------------------------+
> | |void|                  | :ref:`pause<class_GodotInstance_method_pause>`\ (\ )           |
> +-------------------------+----------------------------------------------------------------+
> | |void|                  | :ref:`resume<class_GodotInstance_method_resume>`\ (\ )         |
> +-------------------------+----------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`start<class_GodotInstance_method_start>`\ (\ )           |
> +-------------------------+----------------------------------------------------------------+
>

----


## Method Descriptions



|void| **focus_in**\ (\ ) [🔗<class_GodotInstance_method_focus_in>]

Notifies the instance that it is now in focus.


----



|void| **focus_out**\ (\ ) [🔗<class_GodotInstance_method_focus_out>]

Notifies the instance that it is now not in focus.


----



[bool<class_bool>] **is_started**\ (\ ) [🔗<class_GodotInstance_method_is_started>]

Returns `true` if this instance has been fully started.


----



[bool<class_bool>] **iteration**\ (\ ) [🔗<class_GodotInstance_method_iteration>]

Runs a single iteration of the main loop. Returns `true` if the engine is attempting to quit.


----



|void| **pause**\ (\ ) [🔗<class_GodotInstance_method_pause>]

Notifies the instance that it is going to be paused.


----



|void| **resume**\ (\ ) [🔗<class_GodotInstance_method_resume>]

Notifies the instance that it is being resumed.


----



[bool<class_bool>] **start**\ (\ ) [🔗<class_GodotInstance_method_start>]

Finishes this instance's startup sequence. Returns `true` on success.

