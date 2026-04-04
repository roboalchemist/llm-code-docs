:github_url: hide



# ResourceImporterCSVTranslation

**Inherits:** [ResourceImporter<class_ResourceImporter>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Imports comma-separated values as [Translation<class_Translation>]\ s.


## Description

Comma-separated values are a plain text table storage format. The format's simplicity makes it easy to edit in any text editor or spreadsheet software. This makes it a common choice for game localization.

In the CSV file used for translation, the first column contains string identifiers, and the first row serves as the header. The first column's header can be any value. The remaining headers indicate the locale for that column. Columns whose headers begin with an underscore (`_`) will be ignored.

\ **Example CSV file:**\ 

> **CODE**
>
> keys,en,es,ja
> GREET,"Hello, friend!","Hola, amigo!",こんにちは
> ASK,How are you?,Cómo está?,元気ですか
> BYE,Goodbye,Adiós,さようなら
> QUOTE,"""Hello"" said the man.","""Hola"" dijo el hombre.",「こんにちは」男は言いました
>
Although keys in the first column typically use uppercase string identifiers, it is not uncommon to directly use strings appearing in the game as keys. To avoid string ambiguity, you can use a special `?context` column to specify the context to use with [Object.tr()<class_Object_method_tr>].

> **CODE**
>
> en,?context,fr,ja,zh
> Letter,Alphabet,Lettre,字母,字母
> Letter,Message,Courrier,手紙,信件
>
To set the plural form of a string to use with [Object.tr_n()<class_Object_method_tr_n>], add a special `?plural` column. After setting the plural form of the source string in this column, you can add additional rows to provide translations for more plural forms. The first column and all special columns in these plural form rows must be empty.

Godot includes built-in plural rules for some languages. You can also customize them using a special `?pluralrule` row. See [GNU gettext ](https://www.gnu.org/software/gettext/manual/html_node/Plural-forms.html)_ for examples and more info.

> **CODE**
>
> en,?plural,fr,ru,zh,_Comment
> ?pluralrule,,nplurals=2; plural=(n >= 2);,,,Customize the plural rule for French
> There is %d apple,There are %d apples,Il y a %d pomme,Есть %d яблоко,那里有%d个苹果,
> ,,Il y a %d pommes,Есть %d яблока,,
> ,,,Есть %d яблок,,
>

## Tutorials

- [../tutorials/assets_pipeline/importing_translations](Importing translations .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------+---------------------------------------------------------------------------------------------------+-----------+
> | :ref:`int<class_int>`   | :ref:`compress<class_ResourceImporterCSVTranslation_property_compress>`                           | ``1``     |
> +-------------------------+---------------------------------------------------------------------------------------------------+-----------+
> | :ref:`int<class_int>`   | :ref:`delimiter<class_ResourceImporterCSVTranslation_property_delimiter>`                         | ``0``     |
> +-------------------------+---------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>` | :ref:`unescape_keys<class_ResourceImporterCSVTranslation_property_unescape_keys>`                 | ``false`` |
> +-------------------------+---------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>` | :ref:`unescape_translations<class_ResourceImporterCSVTranslation_property_unescape_translations>` | ``true``  |
> +-------------------------+---------------------------------------------------------------------------------------------------+-----------+
>

----


## Property Descriptions



[int<class_int>] **compress** = `1` [🔗<class_ResourceImporterCSVTranslation_property_compress>]

- **Disabled**: Creates a [Translation<class_Translation>].

- **Auto**: Creates an [OptimizedTranslation<class_OptimizedTranslation>] when possible. This makes the resulting file smaller at the cost of a small CPU overhead. Falls back to [Translation<class_Translation>] for translations with context or plural forms.


----



[int<class_int>] **delimiter** = `0` [🔗<class_ResourceImporterCSVTranslation_property_delimiter>]

The delimiter to use in the CSV file. The default value matches the common CSV convention. Tab-separated values are sometimes called TSV files.


----



[bool<class_bool>] **unescape_keys** = `false` [🔗<class_ResourceImporterCSVTranslation_property_unescape_keys>]

If `true`, message keys in the CSV file are unescaped using [String.c_unescape()<class_String_method_c_unescape>] during the import process.


----



[bool<class_bool>] **unescape_translations** = `true` [🔗<class_ResourceImporterCSVTranslation_property_unescape_translations>]

If `true`, message translations in the CSV file are unescaped using [String.c_unescape()<class_String_method_c_unescape>] during the import process.

