:github_url: hide



# RichTextEffect

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A custom effect for a [RichTextLabel<class_RichTextLabel>].


## Description

A custom effect for a [RichTextLabel<class_RichTextLabel>], which can be loaded in the [RichTextLabel<class_RichTextLabel>] inspector or using [RichTextLabel.install_effect()<class_RichTextLabel_method_install_effect>].

\ **Note:** For a **RichTextEffect** to be usable, a BBCode tag must be defined as a member variable called `bbcode` in the script.


> **TABS**
>

    # The RichTextEffect will be usable like this: `[example]Some text[/example]`
    var bbcode = "example"


    // The RichTextEffect will be usable like this: `[example]Some text[/example]`
    string bbcode = "example";



\ **Note:** As soon as a [RichTextLabel<class_RichTextLabel>] contains at least one **RichTextEffect**, it will continuously process the effect unless the project is paused. This may impact battery life negatively.


## Tutorials

- [../tutorials/ui/bbcode_in_richtextlabel](BBCode in RichTextLabel .md)

- [RichTextEffect test project (third-party) ](https://github.com/Eoin-ONeill-Yokai/Godot-Rich-Text-Effect-Test-Project)_


## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`_process_custom_fx<class_RichTextEffect_private_method__process_custom_fx>`\ (\ char_fx\: :ref:`CharFXTransform<class_CharFXTransform>`\ ) |virtual| |const| |
> +-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[bool<class_bool>] **_process_custom_fx**\ (\ char_fx\: [CharFXTransform<class_CharFXTransform>]\ ) |virtual| |const| [🔗<class_RichTextEffect_private_method__process_custom_fx>]

Override this method to modify properties in `char_fx`. The method must return `true` if the character could be transformed successfully. If the method returns `false`, it will skip transformation to avoid displaying broken text.

