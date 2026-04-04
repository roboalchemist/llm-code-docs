:github_url: hide



# ResourceUID

**Inherits:** [Object<class_Object>]

A singleton that manages the unique identifiers of all resources within a project.


## Description

Resource UIDs (Unique IDentifiers) allow the engine to keep references between resources intact, even if files are renamed or moved. They can be accessed with `uid://`.

\ **ResourceUID** keeps track of all registered resource UIDs in a project, generates new UIDs, and converts between their string and integer representations.


## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------+----------------------------------------------------------------------------------------------------------------------+
> | |void|                      | :ref:`add_id<class_ResourceUID_method_add_id>`\ (\ id\: :ref:`int<class_int>`, path\: :ref:`String<class_String>`\ ) |
> +-----------------------------+----------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`       | :ref:`create_id<class_ResourceUID_method_create_id>`\ (\ )                                                           |
> +-----------------------------+----------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`       | :ref:`create_id_for_path<class_ResourceUID_method_create_id_for_path>`\ (\ path\: :ref:`String<class_String>`\ )     |
> +-----------------------------+----------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>` | :ref:`ensure_path<class_ResourceUID_method_ensure_path>`\ (\ path_or_uid\: :ref:`String<class_String>`\ ) |static|   |
> +-----------------------------+----------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>` | :ref:`get_id_path<class_ResourceUID_method_get_id_path>`\ (\ id\: :ref:`int<class_int>`\ ) |const|                   |
> +-----------------------------+----------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`     | :ref:`has_id<class_ResourceUID_method_has_id>`\ (\ id\: :ref:`int<class_int>`\ ) |const|                             |
> +-----------------------------+----------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>` | :ref:`id_to_text<class_ResourceUID_method_id_to_text>`\ (\ id\: :ref:`int<class_int>`\ ) |const|                     |
> +-----------------------------+----------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>` | :ref:`path_to_uid<class_ResourceUID_method_path_to_uid>`\ (\ path\: :ref:`String<class_String>`\ ) |static|          |
> +-----------------------------+----------------------------------------------------------------------------------------------------------------------+
> | |void|                      | :ref:`remove_id<class_ResourceUID_method_remove_id>`\ (\ id\: :ref:`int<class_int>`\ )                               |
> +-----------------------------+----------------------------------------------------------------------------------------------------------------------+
> | |void|                      | :ref:`set_id<class_ResourceUID_method_set_id>`\ (\ id\: :ref:`int<class_int>`, path\: :ref:`String<class_String>`\ ) |
> +-----------------------------+----------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`       | :ref:`text_to_id<class_ResourceUID_method_text_to_id>`\ (\ text_id\: :ref:`String<class_String>`\ ) |const|          |
> +-----------------------------+----------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>` | :ref:`uid_to_path<class_ResourceUID_method_uid_to_path>`\ (\ uid\: :ref:`String<class_String>`\ ) |static|           |
> +-----------------------------+----------------------------------------------------------------------------------------------------------------------+
>

----


## Constants



**INVALID_ID** = `-1` [🔗<class_ResourceUID_constant_INVALID_ID>]

The value to use for an invalid UID, for example if the resource could not be loaded.

Its text representation is `uid://<invalid>`.


----


## Method Descriptions



|void| **add_id**\ (\ id\: [int<class_int>], path\: [String<class_String>]\ ) [🔗<class_ResourceUID_method_add_id>]

Adds a new UID value which is mapped to the given resource path.

Fails with an error if the UID already exists, so be sure to check [has_id()<class_ResourceUID_method_has_id>] beforehand, or use [set_id()<class_ResourceUID_method_set_id>] instead.


----



[int<class_int>] **create_id**\ (\ ) [🔗<class_ResourceUID_method_create_id>]

Generates a random resource UID which is guaranteed to be unique within the list of currently loaded UIDs.

In order for this UID to be registered, you must call [add_id()<class_ResourceUID_method_add_id>] or [set_id()<class_ResourceUID_method_set_id>].


----



[int<class_int>] **create_id_for_path**\ (\ path\: [String<class_String>]\ ) [🔗<class_ResourceUID_method_create_id_for_path>]

Like [create_id()<class_ResourceUID_method_create_id>], but the UID is seeded with the provided `path` and project name. UIDs generated for that path will be always the same within the current project.


----



[String<class_String>] **ensure_path**\ (\ path_or_uid\: [String<class_String>]\ ) |static| [🔗<class_ResourceUID_method_ensure_path>]

Returns a path, converting `path_or_uid` if necessary. Fails and returns an empty string if an invalid UID is provided.


----



[String<class_String>] **get_id_path**\ (\ id\: [int<class_int>]\ ) |const| [🔗<class_ResourceUID_method_get_id_path>]

Returns the path that the given UID value refers to.

Fails with an error if the UID does not exist, so be sure to check [has_id()<class_ResourceUID_method_has_id>] beforehand.


----



[bool<class_bool>] **has_id**\ (\ id\: [int<class_int>]\ ) |const| [🔗<class_ResourceUID_method_has_id>]

Returns whether the given UID value is known to the cache.


----



[String<class_String>] **id_to_text**\ (\ id\: [int<class_int>]\ ) |const| [🔗<class_ResourceUID_method_id_to_text>]

Converts the given UID to a `uid://` string value.


----



[String<class_String>] **path_to_uid**\ (\ path\: [String<class_String>]\ ) |static| [🔗<class_ResourceUID_method_path_to_uid>]

Converts the provided resource `path` to a UID. Returns the unchanged path if it has no associated UID.


----



|void| **remove_id**\ (\ id\: [int<class_int>]\ ) [🔗<class_ResourceUID_method_remove_id>]

Removes a loaded UID value from the cache.

Fails with an error if the UID does not exist, so be sure to check [has_id()<class_ResourceUID_method_has_id>] beforehand.


----



|void| **set_id**\ (\ id\: [int<class_int>], path\: [String<class_String>]\ ) [🔗<class_ResourceUID_method_set_id>]

Updates the resource path of an existing UID.

Fails with an error if the UID does not exist, so be sure to check [has_id()<class_ResourceUID_method_has_id>] beforehand, or use [add_id()<class_ResourceUID_method_add_id>] instead.


----



[int<class_int>] **text_to_id**\ (\ text_id\: [String<class_String>]\ ) |const| [🔗<class_ResourceUID_method_text_to_id>]

Extracts the UID value from the given `uid://` string.


----



[String<class_String>] **uid_to_path**\ (\ uid\: [String<class_String>]\ ) |static| [🔗<class_ResourceUID_method_uid_to_path>]

Converts the provided `uid` to a path. Prints an error if the UID is invalid.

