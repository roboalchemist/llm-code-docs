:github_url: hide



# Translation

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [OptimizedTranslation<class_OptimizedTranslation>]

A language translation that maps a collection of strings to their individual translations.


## Description

**Translation** maps a collection of strings to their individual translations, and also provides convenience methods for pluralization.

A **Translation** consists of messages. A message is identified by its context and untranslated string. Unlike [gettext ](https://www.gnu.org/software/gettext/)_, using an empty context string in Godot means not using any context.


## Tutorials

- [../tutorials/i18n/internationalizing_games](Internationalizing games .md)

- [../tutorials/i18n/localization_using_gettext](Localization using gettext .md)

- [../tutorials/i18n/locales](Locales .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------+--------------------------------------------------------------------------------+----------+
> | :ref:`String<class_String>` | :ref:`locale<class_Translation_property_locale>`                               | ``"en"`` |
> +-----------------------------+--------------------------------------------------------------------------------+----------+
> | :ref:`String<class_String>` | :ref:`plural_rules_override<class_Translation_property_plural_rules_override>` | ``""``   |
> +-----------------------------+--------------------------------------------------------------------------------+----------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`StringName<class_StringName>`               | :ref:`_get_message<class_Translation_private_method__get_message>`\ (\ src_message\: :ref:`StringName<class_StringName>`, context\: :ref:`StringName<class_StringName>`\ ) |virtual| |const|                                                                                                    |
> +---------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`StringName<class_StringName>`               | :ref:`_get_plural_message<class_Translation_private_method__get_plural_message>`\ (\ src_message\: :ref:`StringName<class_StringName>`, src_plural_message\: :ref:`StringName<class_StringName>`, n\: :ref:`int<class_int>`, context\: :ref:`StringName<class_StringName>`\ ) |virtual| |const| |
> +---------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                            | :ref:`add_message<class_Translation_method_add_message>`\ (\ src_message\: :ref:`StringName<class_StringName>`, xlated_message\: :ref:`StringName<class_StringName>`, context\: :ref:`StringName<class_StringName>` = &""\ )                                                                    |
> +---------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                            | :ref:`add_plural_message<class_Translation_method_add_plural_message>`\ (\ src_message\: :ref:`StringName<class_StringName>`, xlated_messages\: :ref:`PackedStringArray<class_PackedStringArray>`, context\: :ref:`StringName<class_StringName>` = &""\ )                                       |
> +---------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                            | :ref:`erase_message<class_Translation_method_erase_message>`\ (\ src_message\: :ref:`StringName<class_StringName>`, context\: :ref:`StringName<class_StringName>` = &""\ )                                                                                                                      |
> +---------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`StringName<class_StringName>`               | :ref:`get_message<class_Translation_method_get_message>`\ (\ src_message\: :ref:`StringName<class_StringName>`, context\: :ref:`StringName<class_StringName>` = &""\ ) |const|                                                                                                                  |
> +---------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                             | :ref:`get_message_count<class_Translation_method_get_message_count>`\ (\ ) |const|                                                                                                                                                                                                              |
> +---------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedStringArray<class_PackedStringArray>` | :ref:`get_message_list<class_Translation_method_get_message_list>`\ (\ ) |const|                                                                                                                                                                                                                |
> +---------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`StringName<class_StringName>`               | :ref:`get_plural_message<class_Translation_method_get_plural_message>`\ (\ src_message\: :ref:`StringName<class_StringName>`, src_plural_message\: :ref:`StringName<class_StringName>`, n\: :ref:`int<class_int>`, context\: :ref:`StringName<class_StringName>` = &""\ ) |const|               |
> +---------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedStringArray<class_PackedStringArray>` | :ref:`get_translated_message_list<class_Translation_method_get_translated_message_list>`\ (\ ) |const|                                                                                                                                                                                          |
> +---------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[String<class_String>] **locale** = `"en"` [🔗<class_Translation_property_locale>]


- |void| **set_locale**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_locale**\ (\ )

The locale of the translation.


----



[String<class_String>] **plural_rules_override** = `""` [🔗<class_Translation_property_plural_rules_override>]


- |void| **set_plural_rules_override**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_plural_rules_override**\ (\ )

The plural rules string to enforce. See [GNU gettext ](https://www.gnu.org/software/gettext/manual/html_node/Plural-forms.html)_ for examples and more info.

If empty or invalid, default plural rules from [TranslationServer.get_plural_rules()<class_TranslationServer_method_get_plural_rules>] are used. The English plural rules are used as a fallback.


----


## Method Descriptions



[StringName<class_StringName>] **_get_message**\ (\ src_message\: [StringName<class_StringName>], context\: [StringName<class_StringName>]\ ) |virtual| |const| [🔗<class_Translation_private_method__get_message>]

Virtual method to override [get_message()<class_Translation_method_get_message>].


----



[StringName<class_StringName>] **_get_plural_message**\ (\ src_message\: [StringName<class_StringName>], src_plural_message\: [StringName<class_StringName>], n\: [int<class_int>], context\: [StringName<class_StringName>]\ ) |virtual| |const| [🔗<class_Translation_private_method__get_plural_message>]

Virtual method to override [get_plural_message()<class_Translation_method_get_plural_message>].


----



|void| **add_message**\ (\ src_message\: [StringName<class_StringName>], xlated_message\: [StringName<class_StringName>], context\: [StringName<class_StringName>] = &""\ ) [🔗<class_Translation_method_add_message>]

Adds a message if nonexistent, followed by its translation.

An additional context could be used to specify the translation context or differentiate polysemic words.


----



|void| **add_plural_message**\ (\ src_message\: [StringName<class_StringName>], xlated_messages\: [PackedStringArray<class_PackedStringArray>], context\: [StringName<class_StringName>] = &""\ ) [🔗<class_Translation_method_add_plural_message>]

Adds a message involving plural translation if nonexistent, followed by its translation.

An additional context could be used to specify the translation context or differentiate polysemic words.


----



|void| **erase_message**\ (\ src_message\: [StringName<class_StringName>], context\: [StringName<class_StringName>] = &""\ ) [🔗<class_Translation_method_erase_message>]

Erases a message.


----



[StringName<class_StringName>] **get_message**\ (\ src_message\: [StringName<class_StringName>], context\: [StringName<class_StringName>] = &""\ ) |const| [🔗<class_Translation_method_get_message>]

Returns a message's translation.


----



[int<class_int>] **get_message_count**\ (\ ) |const| [🔗<class_Translation_method_get_message_count>]

Returns the number of existing messages.


----



[PackedStringArray<class_PackedStringArray>] **get_message_list**\ (\ ) |const| [🔗<class_Translation_method_get_message_list>]

Returns the keys of all messages, that is, the context and untranslated strings of each message.

\ **Note:** If a message does not use a context, the corresponding element is the untranslated string. Otherwise, the corresponding element is the context and untranslated string separated by the EOT character (`U+0004`). This is done for compatibility purposes.

::

    for key in translation.get_message_list():
        var p = key.find("\u0004")
        if p == -1:
            var untranslated = key
            print("Message %s" % untranslated)
        else:
            var context = key.substr(0, p)
            var untranslated = key.substr(p + 1)
            print("Message %s with context %s" % [untranslated, context])


----



[StringName<class_StringName>] **get_plural_message**\ (\ src_message\: [StringName<class_StringName>], src_plural_message\: [StringName<class_StringName>], n\: [int<class_int>], context\: [StringName<class_StringName>] = &""\ ) |const| [🔗<class_Translation_method_get_plural_message>]

Returns a message's translation involving plurals.

The number `n` is the number or quantity of the plural object. It will be used to guide the translation system to fetch the correct plural form for the selected language.

\ **Note:** Plurals are only supported in [../tutorials/i18n/localization_using_gettext](gettext-based translations (PO) .md), not CSV.


----



[PackedStringArray<class_PackedStringArray>] **get_translated_message_list**\ (\ ) |const| [🔗<class_Translation_method_get_translated_message_list>]

Returns all the translated strings.

