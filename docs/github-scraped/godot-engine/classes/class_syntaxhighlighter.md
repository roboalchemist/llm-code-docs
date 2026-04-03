:github_url: hide



# SyntaxHighlighter

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [CodeHighlighter<class_CodeHighlighter>], [EditorSyntaxHighlighter<class_EditorSyntaxHighlighter>]

Base class for syntax highlighters. Provides syntax highlighting data to a [TextEdit<class_TextEdit>].


## Description

Base class for syntax highlighters. Provides syntax highlighting data to a [TextEdit<class_TextEdit>]. The associated [TextEdit<class_TextEdit>] will call into the **SyntaxHighlighter** on an as-needed basis.

\ **Note:** A **SyntaxHighlighter** instance should not be used across multiple [TextEdit<class_TextEdit>] nodes.


## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                              | :ref:`_clear_highlighting_cache<class_SyntaxHighlighter_private_method__clear_highlighting_cache>`\ (\ ) |virtual|                                               |
> +-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Dictionary<class_Dictionary>` | :ref:`_get_line_syntax_highlighting<class_SyntaxHighlighter_private_method__get_line_syntax_highlighting>`\ (\ line\: :ref:`int<class_int>`\ ) |virtual| |const| |
> +-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                              | :ref:`_update_cache<class_SyntaxHighlighter_private_method__update_cache>`\ (\ ) |virtual|                                                                       |
> +-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                              | :ref:`clear_highlighting_cache<class_SyntaxHighlighter_method_clear_highlighting_cache>`\ (\ )                                                                   |
> +-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Dictionary<class_Dictionary>` | :ref:`get_line_syntax_highlighting<class_SyntaxHighlighter_method_get_line_syntax_highlighting>`\ (\ line\: :ref:`int<class_int>`\ )                             |
> +-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`TextEdit<class_TextEdit>`     | :ref:`get_text_edit<class_SyntaxHighlighter_method_get_text_edit>`\ (\ ) |const|                                                                                 |
> +-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                              | :ref:`update_cache<class_SyntaxHighlighter_method_update_cache>`\ (\ )                                                                                           |
> +-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



|void| **_clear_highlighting_cache**\ (\ ) |virtual| [🔗<class_SyntaxHighlighter_private_method__clear_highlighting_cache>]

Virtual method which can be overridden to clear any local caches.


----



[Dictionary<class_Dictionary>] **_get_line_syntax_highlighting**\ (\ line\: [int<class_int>]\ ) |virtual| |const| [🔗<class_SyntaxHighlighter_private_method__get_line_syntax_highlighting>]

Virtual method which can be overridden to return syntax highlighting data.

See [get_line_syntax_highlighting()<class_SyntaxHighlighter_method_get_line_syntax_highlighting>] for more details.


----



|void| **_update_cache**\ (\ ) |virtual| [🔗<class_SyntaxHighlighter_private_method__update_cache>]

Virtual method which can be overridden to update any local caches.


----



|void| **clear_highlighting_cache**\ (\ ) [🔗<class_SyntaxHighlighter_method_clear_highlighting_cache>]

Clears all cached syntax highlighting data.

Then calls overridable method [_clear_highlighting_cache()<class_SyntaxHighlighter_private_method__clear_highlighting_cache>].


----



[Dictionary<class_Dictionary>] **get_line_syntax_highlighting**\ (\ line\: [int<class_int>]\ ) [🔗<class_SyntaxHighlighter_method_get_line_syntax_highlighting>]

Returns the syntax highlighting data for the line at index `line`. If the line is not cached, calls [_get_line_syntax_highlighting()<class_SyntaxHighlighter_private_method__get_line_syntax_highlighting>] first to calculate the data.

Each entry is a column number containing a nested [Dictionary<class_Dictionary>]. The column number denotes the start of a region, the region will end if another region is found, or at the end of the line. The nested [Dictionary<class_Dictionary>] contains the data for that region. Currently only the key `"color"` is supported.

\ **Example:** Possible return value. This means columns `0` to `4` should be red, and columns `5` to the end of the line should be green:

::

    {
        0: {
            "color": Color(1, 0, 0)
        },
        5: {
            "color": Color(0, 1, 0)
## }


----



[TextEdit<class_TextEdit>] **get_text_edit**\ (\ ) |const| [🔗<class_SyntaxHighlighter_method_get_text_edit>]

Returns the associated [TextEdit<class_TextEdit>] node.


----



|void| **update_cache**\ (\ ) [🔗<class_SyntaxHighlighter_method_update_cache>]

Clears then updates the **SyntaxHighlighter** caches. Override [_update_cache()<class_SyntaxHighlighter_private_method__update_cache>] for a callback.

\ **Note:** This is called automatically when the associated [TextEdit<class_TextEdit>] node, updates its own cache.

