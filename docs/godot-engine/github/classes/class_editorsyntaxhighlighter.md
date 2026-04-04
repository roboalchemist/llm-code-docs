:github_url: hide



# EditorSyntaxHighlighter

**Inherits:** [SyntaxHighlighter<class_SyntaxHighlighter>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [GDScriptSyntaxHighlighter<class_GDScriptSyntaxHighlighter>]

Base class for [SyntaxHighlighter<class_SyntaxHighlighter>] used by the [ScriptEditor<class_ScriptEditor>].


## Description

Base class that all [SyntaxHighlighter<class_SyntaxHighlighter>]\ s used by the [ScriptEditor<class_ScriptEditor>] extend from.

Add a syntax highlighter to an individual script by calling [ScriptEditorBase.add_syntax_highlighter()<class_ScriptEditorBase_method_add_syntax_highlighter>]. To apply to all scripts on open, call [ScriptEditor.register_syntax_highlighter()<class_ScriptEditor_method_register_syntax_highlighter>].


## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`EditorSyntaxHighlighter<class_EditorSyntaxHighlighter>` | :ref:`_create<class_EditorSyntaxHighlighter_private_method__create>`\ (\ ) |virtual| |const|                                   |
> +---------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                                   | :ref:`_get_name<class_EditorSyntaxHighlighter_private_method__get_name>`\ (\ ) |virtual| |const|                               |
> +---------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedStringArray<class_PackedStringArray>`             | :ref:`_get_supported_languages<class_EditorSyntaxHighlighter_private_method__get_supported_languages>`\ (\ ) |virtual| |const| |
> +---------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[EditorSyntaxHighlighter<class_EditorSyntaxHighlighter>] **_create**\ (\ ) |virtual| |const| [🔗<class_EditorSyntaxHighlighter_private_method__create>]

Virtual method which creates a new instance of the syntax highlighter.


----



[String<class_String>] **_get_name**\ (\ ) |virtual| |const| [🔗<class_EditorSyntaxHighlighter_private_method__get_name>]

Virtual method which can be overridden to return the syntax highlighter name.


----



[PackedStringArray<class_PackedStringArray>] **_get_supported_languages**\ (\ ) |virtual| |const| [🔗<class_EditorSyntaxHighlighter_private_method__get_supported_languages>]

Virtual method which can be overridden to return the supported language names.

