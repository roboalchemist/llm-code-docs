:github_url: hide



# TranslationDomain

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A self-contained collection of [Translation<class_Translation>] resources.


## Description

**TranslationDomain** is a self-contained collection of [Translation<class_Translation>] resources. Translations can be added to or removed from it.

If you're working with the main translation domain, it is more convenient to use the wrap methods on [TranslationServer<class_TranslationServer>].


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------+------------------------------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`     | :ref:`enabled<class_TranslationDomain_property_enabled>`                                                                           | ``true``  |
> +-----------------------------+------------------------------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`     | :ref:`pseudolocalization_accents_enabled<class_TranslationDomain_property_pseudolocalization_accents_enabled>`                     | ``true``  |
> +-----------------------------+------------------------------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`     | :ref:`pseudolocalization_double_vowels_enabled<class_TranslationDomain_property_pseudolocalization_double_vowels_enabled>`         | ``false`` |
> +-----------------------------+------------------------------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`     | :ref:`pseudolocalization_enabled<class_TranslationDomain_property_pseudolocalization_enabled>`                                     | ``false`` |
> +-----------------------------+------------------------------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>`   | :ref:`pseudolocalization_expansion_ratio<class_TranslationDomain_property_pseudolocalization_expansion_ratio>`                     | ``0.0``   |
> +-----------------------------+------------------------------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`     | :ref:`pseudolocalization_fake_bidi_enabled<class_TranslationDomain_property_pseudolocalization_fake_bidi_enabled>`                 | ``false`` |
> +-----------------------------+------------------------------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`     | :ref:`pseudolocalization_override_enabled<class_TranslationDomain_property_pseudolocalization_override_enabled>`                   | ``false`` |
> +-----------------------------+------------------------------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`String<class_String>` | :ref:`pseudolocalization_prefix<class_TranslationDomain_property_pseudolocalization_prefix>`                                       | ``"["``   |
> +-----------------------------+------------------------------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`     | :ref:`pseudolocalization_skip_placeholders_enabled<class_TranslationDomain_property_pseudolocalization_skip_placeholders_enabled>` | ``true``  |
> +-----------------------------+------------------------------------------------------------------------------------------------------------------------------------+-----------+
> | :ref:`String<class_String>` | :ref:`pseudolocalization_suffix<class_TranslationDomain_property_pseudolocalization_suffix>`                                       | ``"]"``   |
> +-----------------------------+------------------------------------------------------------------------------------------------------------------------------------+-----------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                             | :ref:`add_translation<class_TranslationDomain_method_add_translation>`\ (\ translation\: :ref:`Translation<class_Translation>`\ )                                                                                                                                           |
> +--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                             | :ref:`clear<class_TranslationDomain_method_clear>`\ (\ )                                                                                                                                                                                                                    |
> +--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`Translation<class_Translation>`\] | :ref:`find_translations<class_TranslationDomain_method_find_translations>`\ (\ locale\: :ref:`String<class_String>`, exact\: :ref:`bool<class_bool>`\ ) |const|                                                                                                             |
> +--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                                        | :ref:`get_locale_override<class_TranslationDomain_method_get_locale_override>`\ (\ ) |const|                                                                                                                                                                                |
> +--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Translation<class_Translation>`                              | :ref:`get_translation_object<class_TranslationDomain_method_get_translation_object>`\ (\ locale\: :ref:`String<class_String>`\ ) |const|                                                                                                                                    |
> +--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`Translation<class_Translation>`\] | :ref:`get_translations<class_TranslationDomain_method_get_translations>`\ (\ ) |const|                                                                                                                                                                                      |
> +--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                            | :ref:`has_translation<class_TranslationDomain_method_has_translation>`\ (\ translation\: :ref:`Translation<class_Translation>`\ ) |const|                                                                                                                                   |
> +--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                            | :ref:`has_translation_for_locale<class_TranslationDomain_method_has_translation_for_locale>`\ (\ locale\: :ref:`String<class_String>`, exact\: :ref:`bool<class_bool>`\ ) |const|                                                                                           |
> +--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`StringName<class_StringName>`                                | :ref:`pseudolocalize<class_TranslationDomain_method_pseudolocalize>`\ (\ message\: :ref:`StringName<class_StringName>`\ ) |const|                                                                                                                                           |
> +--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                             | :ref:`remove_translation<class_TranslationDomain_method_remove_translation>`\ (\ translation\: :ref:`Translation<class_Translation>`\ )                                                                                                                                     |
> +--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                             | :ref:`set_locale_override<class_TranslationDomain_method_set_locale_override>`\ (\ locale\: :ref:`String<class_String>`\ )                                                                                                                                                  |
> +--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`StringName<class_StringName>`                                | :ref:`translate<class_TranslationDomain_method_translate>`\ (\ message\: :ref:`StringName<class_StringName>`, context\: :ref:`StringName<class_StringName>` = &""\ ) |const|                                                                                                |
> +--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`StringName<class_StringName>`                                | :ref:`translate_plural<class_TranslationDomain_method_translate_plural>`\ (\ message\: :ref:`StringName<class_StringName>`, message_plural\: :ref:`StringName<class_StringName>`, n\: :ref:`int<class_int>`, context\: :ref:`StringName<class_StringName>` = &""\ ) |const| |
> +--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[bool<class_bool>] **enabled** = `true` [🔗<class_TranslationDomain_property_enabled>]


- |void| **set_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_enabled**\ (\ )

If `true`, translation is enabled. Otherwise, [translate()<class_TranslationDomain_method_translate>] and [translate_plural()<class_TranslationDomain_method_translate_plural>] will return the input message unchanged regardless of the current locale.


----



[bool<class_bool>] **pseudolocalization_accents_enabled** = `true` [🔗<class_TranslationDomain_property_pseudolocalization_accents_enabled>]


- |void| **set_pseudolocalization_accents_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_pseudolocalization_accents_enabled**\ (\ )

Replace all characters with their accented variants during pseudolocalization.

\ **Note:** Updating this property does not automatically update texts in the scene tree. Please propagate the [MainLoop.NOTIFICATION_TRANSLATION_CHANGED<class_MainLoop_constant_NOTIFICATION_TRANSLATION_CHANGED>] notification manually after you have finished modifying pseudolocalization related options.


----



[bool<class_bool>] **pseudolocalization_double_vowels_enabled** = `false` [🔗<class_TranslationDomain_property_pseudolocalization_double_vowels_enabled>]


- |void| **set_pseudolocalization_double_vowels_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_pseudolocalization_double_vowels_enabled**\ (\ )

Double vowels in strings during pseudolocalization to simulate the lengthening of text due to localization.

\ **Note:** Updating this property does not automatically update texts in the scene tree. Please propagate the [MainLoop.NOTIFICATION_TRANSLATION_CHANGED<class_MainLoop_constant_NOTIFICATION_TRANSLATION_CHANGED>] notification manually after you have finished modifying pseudolocalization related options.


----



[bool<class_bool>] **pseudolocalization_enabled** = `false` [🔗<class_TranslationDomain_property_pseudolocalization_enabled>]


- |void| **set_pseudolocalization_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_pseudolocalization_enabled**\ (\ )

If `true`, enables pseudolocalization for the project. This can be used to spot untranslatable strings or layout issues that may occur once the project is localized to languages that have longer strings than the source language.

\ **Note:** Updating this property does not automatically update texts in the scene tree. Please propagate the [MainLoop.NOTIFICATION_TRANSLATION_CHANGED<class_MainLoop_constant_NOTIFICATION_TRANSLATION_CHANGED>] notification manually after you have finished modifying pseudolocalization related options.


----



[float<class_float>] **pseudolocalization_expansion_ratio** = `0.0` [🔗<class_TranslationDomain_property_pseudolocalization_expansion_ratio>]


- |void| **set_pseudolocalization_expansion_ratio**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_pseudolocalization_expansion_ratio**\ (\ )

The expansion ratio to use during pseudolocalization. A value of `0.3` is sufficient for most practical purposes, and will increase the length of each string by 30%.

\ **Note:** Updating this property does not automatically update texts in the scene tree. Please propagate the [MainLoop.NOTIFICATION_TRANSLATION_CHANGED<class_MainLoop_constant_NOTIFICATION_TRANSLATION_CHANGED>] notification manually after you have finished modifying pseudolocalization related options.


----



[bool<class_bool>] **pseudolocalization_fake_bidi_enabled** = `false` [🔗<class_TranslationDomain_property_pseudolocalization_fake_bidi_enabled>]


- |void| **set_pseudolocalization_fake_bidi_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_pseudolocalization_fake_bidi_enabled**\ (\ )

If `true`, emulate bidirectional (right-to-left) text when pseudolocalization is enabled. This can be used to spot issues with RTL layout and UI mirroring that will crop up if the project is localized to RTL languages such as Arabic or Hebrew.

\ **Note:** Updating this property does not automatically update texts in the scene tree. Please propagate the [MainLoop.NOTIFICATION_TRANSLATION_CHANGED<class_MainLoop_constant_NOTIFICATION_TRANSLATION_CHANGED>] notification manually after you have finished modifying pseudolocalization related options.


----



[bool<class_bool>] **pseudolocalization_override_enabled** = `false` [🔗<class_TranslationDomain_property_pseudolocalization_override_enabled>]


- |void| **set_pseudolocalization_override_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_pseudolocalization_override_enabled**\ (\ )

Replace all characters in the string with `*`. Useful for finding non-localizable strings.

\ **Note:** Updating this property does not automatically update texts in the scene tree. Please propagate the [MainLoop.NOTIFICATION_TRANSLATION_CHANGED<class_MainLoop_constant_NOTIFICATION_TRANSLATION_CHANGED>] notification manually after you have finished modifying pseudolocalization related options.


----



[String<class_String>] **pseudolocalization_prefix** = `"["` [🔗<class_TranslationDomain_property_pseudolocalization_prefix>]


- |void| **set_pseudolocalization_prefix**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_pseudolocalization_prefix**\ (\ )

Prefix that will be prepended to the pseudolocalized string.

\ **Note:** Updating this property does not automatically update texts in the scene tree. Please propagate the [MainLoop.NOTIFICATION_TRANSLATION_CHANGED<class_MainLoop_constant_NOTIFICATION_TRANSLATION_CHANGED>] notification manually after you have finished modifying pseudolocalization related options.


----



[bool<class_bool>] **pseudolocalization_skip_placeholders_enabled** = `true` [🔗<class_TranslationDomain_property_pseudolocalization_skip_placeholders_enabled>]


- |void| **set_pseudolocalization_skip_placeholders_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_pseudolocalization_skip_placeholders_enabled**\ (\ )

Skip placeholders for string formatting like `%s` or `%f` during pseudolocalization. Useful to identify strings which need additional control characters to display correctly.

\ **Note:** Updating this property does not automatically update texts in the scene tree. Please propagate the [MainLoop.NOTIFICATION_TRANSLATION_CHANGED<class_MainLoop_constant_NOTIFICATION_TRANSLATION_CHANGED>] notification manually after you have finished modifying pseudolocalization related options.


----



[String<class_String>] **pseudolocalization_suffix** = `"]"` [🔗<class_TranslationDomain_property_pseudolocalization_suffix>]


- |void| **set_pseudolocalization_suffix**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_pseudolocalization_suffix**\ (\ )

Suffix that will be appended to the pseudolocalized string.

\ **Note:** Updating this property does not automatically update texts in the scene tree. Please propagate the [MainLoop.NOTIFICATION_TRANSLATION_CHANGED<class_MainLoop_constant_NOTIFICATION_TRANSLATION_CHANGED>] notification manually after you have finished modifying pseudolocalization related options.


----


## Method Descriptions



|void| **add_translation**\ (\ translation\: [Translation<class_Translation>]\ ) [🔗<class_TranslationDomain_method_add_translation>]

Adds a translation.


----



|void| **clear**\ (\ ) [🔗<class_TranslationDomain_method_clear>]

Removes all translations.


----



[Array<class_Array>]\[[Translation<class_Translation>]\] **find_translations**\ (\ locale\: [String<class_String>], exact\: [bool<class_bool>]\ ) |const| [🔗<class_TranslationDomain_method_find_translations>]

Returns the [Translation<class_Translation>] instances that match `locale` (see [TranslationServer.compare_locales()<class_TranslationServer_method_compare_locales>]). If `exact` is `true`, only instances whose locale exactly equals `locale` will be returned.


----



[String<class_String>] **get_locale_override**\ (\ ) |const| [🔗<class_TranslationDomain_method_get_locale_override>]

Returns the locale override of the domain. Returns an empty string if locale override is disabled.


----



[Translation<class_Translation>] **get_translation_object**\ (\ locale\: [String<class_String>]\ ) |const| [🔗<class_TranslationDomain_method_get_translation_object>]

**Deprecated:** Use [find_translations()<class_TranslationDomain_method_find_translations>] instead.

Returns the [Translation<class_Translation>] instance that best matches `locale`. Returns `null` if there are no matches.


----



[Array<class_Array>]\[[Translation<class_Translation>]\] **get_translations**\ (\ ) |const| [🔗<class_TranslationDomain_method_get_translations>]

Returns all available [Translation<class_Translation>] instances as added by [add_translation()<class_TranslationDomain_method_add_translation>].


----



[bool<class_bool>] **has_translation**\ (\ translation\: [Translation<class_Translation>]\ ) |const| [🔗<class_TranslationDomain_method_has_translation>]

Returns `true` if this translation domain contains the given `translation`.


----



[bool<class_bool>] **has_translation_for_locale**\ (\ locale\: [String<class_String>], exact\: [bool<class_bool>]\ ) |const| [🔗<class_TranslationDomain_method_has_translation_for_locale>]

Returns `true` if there are any [Translation<class_Translation>] instances that match `locale` (see [TranslationServer.compare_locales()<class_TranslationServer_method_compare_locales>]). If `exact` is `true`, only instances whose locale exactly equals `locale` are considered.


----



[StringName<class_StringName>] **pseudolocalize**\ (\ message\: [StringName<class_StringName>]\ ) |const| [🔗<class_TranslationDomain_method_pseudolocalize>]

Returns the pseudolocalized string based on the `message` passed in.


----



|void| **remove_translation**\ (\ translation\: [Translation<class_Translation>]\ ) [🔗<class_TranslationDomain_method_remove_translation>]

Removes the given translation.


----



|void| **set_locale_override**\ (\ locale\: [String<class_String>]\ ) [🔗<class_TranslationDomain_method_set_locale_override>]

Sets the locale override of the domain.

If `locale` is an empty string, locale override is disabled. Otherwise, `locale` will be standardized to match known locales (e.g. `en-US` would be matched to `en_US`).

\ **Note:** Calling this method does not automatically update texts in the scene tree. Please propagate the [MainLoop.NOTIFICATION_TRANSLATION_CHANGED<class_MainLoop_constant_NOTIFICATION_TRANSLATION_CHANGED>] signal manually.


----



[StringName<class_StringName>] **translate**\ (\ message\: [StringName<class_StringName>], context\: [StringName<class_StringName>] = &""\ ) |const| [🔗<class_TranslationDomain_method_translate>]

Returns the current locale's translation for the given message and context.


----



[StringName<class_StringName>] **translate_plural**\ (\ message\: [StringName<class_StringName>], message_plural\: [StringName<class_StringName>], n\: [int<class_int>], context\: [StringName<class_StringName>] = &""\ ) |const| [🔗<class_TranslationDomain_method_translate_plural>]

Returns the current locale's translation for the given message, plural message and context.

The number `n` is the number or quantity of the plural object. It will be used to guide the translation system to fetch the correct plural form for the selected language.

