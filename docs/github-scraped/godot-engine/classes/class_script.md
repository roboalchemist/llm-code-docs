:github_url: hide



# Script

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [CSharpScript<class_CSharpScript>], [GDScript<class_GDScript>], [ScriptExtension<class_ScriptExtension>]

A class stored as a resource.


## Description

A class stored as a resource. A script extends the functionality of all objects that instantiate it.

This is the base class for all scripts and should not be used directly. Trying to create a new script with this class will result in an error.

The `new` method of a script subclass creates a new instance. [Object.set_script()<class_Object_method_set_script>] extends an existing object, if that object's class matches one of the script's base classes.


## Tutorials

- [../tutorials/scripting/index](Scripting documentation index .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------+-------------------------------------------------------+
> | :ref:`String<class_String>` | :ref:`source_code<class_Script_property_source_code>` |
> +-----------------------------+-------------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`can_instantiate<class_Script_method_can_instantiate>`\ (\ ) |const|                                                               |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Script<class_Script>`                                      | :ref:`get_base_script<class_Script_method_get_base_script>`\ (\ ) |const|                                                               |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`StringName<class_StringName>`                              | :ref:`get_global_name<class_Script_method_get_global_name>`\ (\ ) |const|                                                               |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`StringName<class_StringName>`                              | :ref:`get_instance_base_type<class_Script_method_get_instance_base_type>`\ (\ ) |const|                                                 |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>`                                    | :ref:`get_property_default_value<class_Script_method_get_property_default_value>`\ (\ property\: :ref:`StringName<class_StringName>`\ ) |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>`                                    | :ref:`get_rpc_config<class_Script_method_get_rpc_config>`\ (\ ) |const|                                                                 |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Dictionary<class_Dictionary>`                              | :ref:`get_script_constant_map<class_Script_method_get_script_constant_map>`\ (\ )                                                       |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`Dictionary<class_Dictionary>`\] | :ref:`get_script_method_list<class_Script_method_get_script_method_list>`\ (\ )                                                         |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`Dictionary<class_Dictionary>`\] | :ref:`get_script_property_list<class_Script_method_get_script_property_list>`\ (\ )                                                     |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`Dictionary<class_Dictionary>`\] | :ref:`get_script_signal_list<class_Script_method_get_script_signal_list>`\ (\ )                                                         |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`has_script_signal<class_Script_method_has_script_signal>`\ (\ signal_name\: :ref:`StringName<class_StringName>`\ ) |const|        |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`has_source_code<class_Script_method_has_source_code>`\ (\ ) |const|                                                               |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`instance_has<class_Script_method_instance_has>`\ (\ base_object\: :ref:`Object<class_Object>`\ ) |const|                          |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`is_abstract<class_Script_method_is_abstract>`\ (\ ) |const|                                                                       |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`is_tool<class_Script_method_is_tool>`\ (\ ) |const|                                                                               |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>`                            | :ref:`reload<class_Script_method_reload>`\ (\ keep_state\: :ref:`bool<class_bool>` = false\ )                                           |
> +------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[String<class_String>] **source_code** [🔗<class_Script_property_source_code>]


- |void| **set_source_code**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_source_code**\ (\ )

The script source code or an empty string if source code is not available. When set, does not reload the class implementation automatically.


----


## Method Descriptions



[bool<class_bool>] **can_instantiate**\ (\ ) |const| [🔗<class_Script_method_can_instantiate>]

Returns `true` if the script can be instantiated.


----



[Script<class_Script>] **get_base_script**\ (\ ) |const| [🔗<class_Script_method_get_base_script>]

Returns the script directly inherited by this script.


----



[StringName<class_StringName>] **get_global_name**\ (\ ) |const| [🔗<class_Script_method_get_global_name>]

Returns the class name associated with the script, if there is one. Returns an empty string otherwise.

To give the script a global name, you can use the `class_name` keyword in GDScript and the `[GlobalClass]` attribute in C#.


> **TABS**
>

    class_name MyNode
    extends Node


    using Godot;

    [GlobalClass]
    public partial class MyNode : Node
## {




----



[StringName<class_StringName>] **get_instance_base_type**\ (\ ) |const| [🔗<class_Script_method_get_instance_base_type>]

Returns the script's base type.


----



[Variant<class_Variant>] **get_property_default_value**\ (\ property\: [StringName<class_StringName>]\ ) [🔗<class_Script_method_get_property_default_value>]

Returns the default value of the specified property.


----



[Variant<class_Variant>] **get_rpc_config**\ (\ ) |const| [🔗<class_Script_method_get_rpc_config>]

Returns a [Dictionary<class_Dictionary>] mapping method names to their RPC configuration defined by this script.


----



[Dictionary<class_Dictionary>] **get_script_constant_map**\ (\ ) [🔗<class_Script_method_get_script_constant_map>]

Returns a dictionary containing constant names and their values.


----



[Array<class_Array>]\[[Dictionary<class_Dictionary>]\] **get_script_method_list**\ (\ ) [🔗<class_Script_method_get_script_method_list>]

Returns the list of methods in this **Script**.

\ **Note:** The dictionaries returned by this method are formatted identically to those returned by [Object.get_method_list()<class_Object_method_get_method_list>].


----



[Array<class_Array>]\[[Dictionary<class_Dictionary>]\] **get_script_property_list**\ (\ ) [🔗<class_Script_method_get_script_property_list>]

Returns the list of properties in this **Script**.

\ **Note:** The dictionaries returned by this method are formatted identically to those returned by [Object.get_property_list()<class_Object_method_get_property_list>].


----



[Array<class_Array>]\[[Dictionary<class_Dictionary>]\] **get_script_signal_list**\ (\ ) [🔗<class_Script_method_get_script_signal_list>]

Returns the list of signals defined in this **Script**.

\ **Note:** The dictionaries returned by this method are formatted identically to those returned by [Object.get_signal_list()<class_Object_method_get_signal_list>].


----



[bool<class_bool>] **has_script_signal**\ (\ signal_name\: [StringName<class_StringName>]\ ) |const| [🔗<class_Script_method_has_script_signal>]

Returns `true` if the script, or a base class, defines a signal with the given name.


----



[bool<class_bool>] **has_source_code**\ (\ ) |const| [🔗<class_Script_method_has_source_code>]

Returns `true` if the script contains non-empty source code.

\ **Note:** If a script does not have source code, this does not mean that it is invalid or unusable. For example, a [GDScript<class_GDScript>] that was exported with binary tokenization has no source code, but still behaves as expected and could be instantiated. This can be checked with [can_instantiate()<class_Script_method_can_instantiate>].


----



[bool<class_bool>] **instance_has**\ (\ base_object\: [Object<class_Object>]\ ) |const| [🔗<class_Script_method_instance_has>]

Returns `true` if `base_object` is an instance of this script.


----



[bool<class_bool>] **is_abstract**\ (\ ) |const| [🔗<class_Script_method_is_abstract>]

Returns `true` if the script is an abstract script. An abstract script does not have a constructor and cannot be instantiated.


----



[bool<class_bool>] **is_tool**\ (\ ) |const| [🔗<class_Script_method_is_tool>]

Returns `true` if the script is a tool script. A tool script can run in the editor.


----



[Error<enum_@GlobalScope_Error>] **reload**\ (\ keep_state\: [bool<class_bool>] = false\ ) [🔗<class_Script_method_reload>]

Reloads the script's class implementation. Returns an error code.

