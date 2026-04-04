:github_url: hide



# RID

A handle for a [Resource<class_Resource>]'s unique identifier.


## Description

The RID [Variant<class_Variant>] type is used to access a low-level resource by its unique ID. RIDs are opaque, which means they do not grant access to the resource by themselves. They are used by the low-level server classes, such as [DisplayServer<class_DisplayServer>], [RenderingServer<class_RenderingServer>], [TextServer<class_TextServer>], etc.

A low-level resource may correspond to a high-level [Resource<class_Resource>], such as [Texture<class_Texture>] or [Mesh<class_Mesh>].

\ **Note:** RIDs are only useful during the current session. It won't correspond to a similar resource if sent over a network, or loaded from a file at a later time.

> **NOTE**
>
	There are notable differences when using this API with C#. See [doc_c_sharp_differences] for more information.


## Constructors

> **TABLE**
> :widths: auto
>
> +-----------------------+---------------------------------------------------------------------------+
> | :ref:`RID<class_RID>` | :ref:`RID<class_RID_constructor_RID>`\ (\ )                               |
> +-----------------------+---------------------------------------------------------------------------+
> | :ref:`RID<class_RID>` | :ref:`RID<class_RID_constructor_RID>`\ (\ from\: :ref:`RID<class_RID>`\ ) |
> +-----------------------+---------------------------------------------------------------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------+----------------------------------------------------------+
> | :ref:`int<class_int>`   | :ref:`get_id<class_RID_method_get_id>`\ (\ ) |const|     |
> +-------------------------+----------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`is_valid<class_RID_method_is_valid>`\ (\ ) |const| |
> +-------------------------+----------------------------------------------------------+
>

## Operators

> **TABLE**
> :widths: auto
>
> +-------------------------+--------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`operator !=<class_RID_operator_neq_RID>`\ (\ right\: :ref:`RID<class_RID>`\ )  |
> +-------------------------+--------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`operator \<<class_RID_operator_lt_RID>`\ (\ right\: :ref:`RID<class_RID>`\ )   |
> +-------------------------+--------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`operator \<=<class_RID_operator_lte_RID>`\ (\ right\: :ref:`RID<class_RID>`\ ) |
> +-------------------------+--------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`operator ==<class_RID_operator_eq_RID>`\ (\ right\: :ref:`RID<class_RID>`\ )   |
> +-------------------------+--------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`operator ><class_RID_operator_gt_RID>`\ (\ right\: :ref:`RID<class_RID>`\ )    |
> +-------------------------+--------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`operator >=<class_RID_operator_gte_RID>`\ (\ right\: :ref:`RID<class_RID>`\ )  |
> +-------------------------+--------------------------------------------------------------------------------------+
>

----


## Constructor Descriptions



[RID<class_RID>] **RID**\ (\ ) [🔗<class_RID_constructor_RID>]

Constructs an empty **RID** with the invalid ID `0`.


----


[RID<class_RID>] **RID**\ (\ from\: [RID<class_RID>]\ )

Constructs an **RID** as a copy of the given **RID**.


----


## Method Descriptions



[int<class_int>] **get_id**\ (\ ) |const| [🔗<class_RID_method_get_id>]

Returns the ID of the referenced low-level resource.


----



[bool<class_bool>] **is_valid**\ (\ ) |const| [🔗<class_RID_method_is_valid>]

Returns `true` if the **RID** is not `0`.


----


## Operator Descriptions



[bool<class_bool>] **operator !=**\ (\ right\: [RID<class_RID>]\ ) [🔗<class_RID_operator_neq_RID>]

Returns `true` if the **RID**\ s are not equal.


----



[bool<class_bool>] **operator <**\ (\ right\: [RID<class_RID>]\ ) [🔗<class_RID_operator_lt_RID>]

Returns `true` if the **RID**'s ID is less than `right`'s ID.


----



[bool<class_bool>] **operator <=**\ (\ right\: [RID<class_RID>]\ ) [🔗<class_RID_operator_lte_RID>]

Returns `true` if the **RID**'s ID is less than or equal to `right`'s ID.


----



[bool<class_bool>] **operator ==**\ (\ right\: [RID<class_RID>]\ ) [🔗<class_RID_operator_eq_RID>]

Returns `true` if both **RID**\ s are equal, which means they both refer to the same low-level resource.


----



[bool<class_bool>] **operator >**\ (\ right\: [RID<class_RID>]\ ) [🔗<class_RID_operator_gt_RID>]

Returns `true` if the **RID**'s ID is greater than `right`'s ID.


----



[bool<class_bool>] **operator >=**\ (\ right\: [RID<class_RID>]\ ) [🔗<class_RID_operator_gte_RID>]

Returns `true` if the **RID**'s ID is greater than or equal to `right`'s ID.

