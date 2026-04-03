:github_url: hide



# OptimizedTranslation

**Inherits:** [Translation<class_Translation>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

An optimized translation.


## Description

An optimized translation. Uses real-time compressed translations, which results in very small dictionaries.

This class does not store the untranslated strings for optimization purposes. Therefore, [Translation.get_message_list()<class_Translation_method_get_message_list>] always returns an empty array, and [Translation.get_message_count()<class_Translation_method_get_message_count>] always returns `0`.


## Methods

> **TABLE**
> :widths: auto
>
> +--------+-----------------------------------------------------------------------------------------------------------------+
> | |void| | :ref:`generate<class_OptimizedTranslation_method_generate>`\ (\ from\: :ref:`Translation<class_Translation>`\ ) |
> +--------+-----------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



|void| **generate**\ (\ from\: [Translation<class_Translation>]\ ) [🔗<class_OptimizedTranslation_method_generate>]

Generates and sets an optimized translation from the given [Translation<class_Translation>] resource.

\ **Note:** Messages in `from` should not use context or plural forms.

\ **Note:** This method is intended to be used in the editor. It does nothing when called from an exported project.

