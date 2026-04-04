:github_url: hide



# GDScript

**Inherits:** [Script<class_Script>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A script implemented in the GDScript programming language.


## Description

A script implemented in the GDScript programming language, saved with the `.gd` extension. The script extends the functionality of all objects that instantiate it.

Calling [new()<class_GDScript_method_new>] creates a new instance of the script. [Object.set_script()<class_Object_method_set_script>] extends an existing object, if that object's class matches one of the script's base classes.

If you are looking for GDScript's built-in functions, see [@GDScript<class_@GDScript>] instead.


## Tutorials

- [../tutorials/scripting/gdscript/index](GDScript documentation index .md)


## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------+-----------------------------------------------------------+
> | :ref:`Variant<class_Variant>` | :ref:`new<class_GDScript_method_new>`\ (\ ...\ ) |vararg| |
> +-------------------------------+-----------------------------------------------------------+
>

----


## Method Descriptions



[Variant<class_Variant>] **new**\ (\ ...\ ) |vararg| [🔗<class_GDScript_method_new>]

Returns a new instance of the script.

::

    var MyClass = load("myclass.gd")
    var instance = MyClass.new()
    print(instance.get_script() == MyClass) # Prints true

