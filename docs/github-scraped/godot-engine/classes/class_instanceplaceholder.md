:github_url: hide



# InstancePlaceholder

**Inherits:** [Node<class_Node>] **<** [Object<class_Object>]

Placeholder for the root [Node<class_Node>] of a [PackedScene<class_PackedScene>].


## Description

Turning on the option **Load As Placeholder** for an instantiated scene in the editor causes it to be replaced by an **InstancePlaceholder** when running the game, this will not replace the node in the editor. This makes it possible to delay actually loading the scene until calling [create_instance()<class_InstancePlaceholder_method_create_instance>]. This is useful to avoid loading large scenes all at once by loading parts of it selectively.

\ **Note:** Like [Node<class_Node>], **InstancePlaceholder** does not have a transform. This causes any child nodes to be positioned relatively to the [Viewport<class_Viewport>] origin, rather than their parent as displayed in the editor. Replacing the placeholder with a scene with a transform will transform children relatively to their parent again.


## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Node<class_Node>`             | :ref:`create_instance<class_InstancePlaceholder_method_create_instance>`\ (\ replace\: :ref:`bool<class_bool>` = false, custom_scene\: :ref:`PackedScene<class_PackedScene>` = null\ ) |
> +-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`         | :ref:`get_instance_path<class_InstancePlaceholder_method_get_instance_path>`\ (\ ) |const|                                                                                             |
> +-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Dictionary<class_Dictionary>` | :ref:`get_stored_values<class_InstancePlaceholder_method_get_stored_values>`\ (\ with_order\: :ref:`bool<class_bool>` = false\ )                                                       |
> +-------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[Node<class_Node>] **create_instance**\ (\ replace\: [bool<class_bool>] = false, custom_scene\: [PackedScene<class_PackedScene>] = null\ ) [🔗<class_InstancePlaceholder_method_create_instance>]

Call this method to actually load in the node. The created node will be placed as a sibling *above* the **InstancePlaceholder** in the scene tree. The [Node<class_Node>]'s reference is also returned for convenience.

\ **Note:** [create_instance()<class_InstancePlaceholder_method_create_instance>] is not thread-safe. Use [Object.call_deferred()<class_Object_method_call_deferred>] if calling from a thread.


----



[String<class_String>] **get_instance_path**\ (\ ) |const| [🔗<class_InstancePlaceholder_method_get_instance_path>]

Gets the path to the [PackedScene<class_PackedScene>] resource file that is loaded by default when calling [create_instance()<class_InstancePlaceholder_method_create_instance>]. Not thread-safe. Use [Object.call_deferred()<class_Object_method_call_deferred>] if calling from a thread.


----



[Dictionary<class_Dictionary>] **get_stored_values**\ (\ with_order\: [bool<class_bool>] = false\ ) [🔗<class_InstancePlaceholder_method_get_stored_values>]

Returns the list of properties that will be applied to the node when [create_instance()<class_InstancePlaceholder_method_create_instance>] is called.

If `with_order` is `true`, a key named `.order` (note the leading period) is added to the dictionary. This `.order` key is an [Array<class_Array>] of [String<class_String>] property names specifying the order in which properties will be applied (with index 0 being the first).

