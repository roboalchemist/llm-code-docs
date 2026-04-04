# Custom

**Source:** [https://developer.wordpress.org/themes/global-settings-and-styles/settings/custom/](https://developer.wordpress.org/themes/global-settings-and-styles/settings/custom/)

## In this article

Table of Contents- Overview of the custom setting

- How CSS custom properties are generatedAutomatic hyphenationNested properties
- Practical usageUse in theme.json stylesUse in CSS

↑Back to top

Thesettings.customproperty is unique among other settings intheme.json. As its name implies, it is a custom property. This means that you get to decide how to use it. Essentially, it provides a method for creating CSS custom properties that you might need elsewhere in your theme.

In this document, you will learn what thecustomproperty is for and how you can use it in your theme.

## Overview of the custom setting

Thesettings.customproperty accepts a single object, and this object can be used to store other values. The individual object values must be valid CSS values or an object with nested key/value pairs.

Here is an example snippet fromtheme.jsonwith no custom values set:

```json
{
    "version": 2,
    "settings": {
        "custom": {}
    }
}
```text

The great thing about thesettings.customobject is that you can use it to create your own CSS custom properties. When you add a key and value to the object, WordPress will automatically generate the CSS custom property, assign the value, and load it for you.

The generated CSS custom property will follow this pattern:--wp--custom--{key}--{value}.

Suppose you wanted to use the key offruitand give it a value ofapple. Add this to yourtheme.jsonfile:

```json
{
    "version": 2,
    "settings": {
        "custom": {
            "fruit": "apple"
        }
    }
}
```text

WordPress will then generate this CSS:

```text
body {
    --wp--custom--fruit: apple;
}
```text

## How CSS custom properties are generated

As you learned above, thesettings.custom.fruitkey name will generate the--wp--custom--fruitvariable in CSS. But there are other cases too.

### Automatic hyphenation

WordPress will automatically hyphenate camel-cased names. For example,lineHeightin the following example will becomeline-height:

```json
{
    "version": 2,
    "settings": {
        "custom": {
            "lineHeight": "1.4em"
        }
    }
}
```text

This will create the following CSS:

```text
body {
    --wp--custom--line-height: 1.4em;
}
```text

Numbers are handled the same as uppercase letters when used as a key. For example, a key ofabc123will becomeabc-1-2-3in the resulting CSS.

### Nested properties

Building off the above example, suppose you wanted to create several line-height CSS custom properties for use in your theme. For this, you might want to create an object undersettings.custom.lineHeightinstead of a single value.

Add the following to yourtheme.jsonfile:

```json
{
    "version": 2,
    "settings": {
        "custom": {
            "lineHeight": {
                "xs": "1",
                "sm": "1.25",
                "md": "1.5",
                "lg": "1.75"
            }
        }
    }
}
```text

WordPress will automatically use this nested structure when generating the CSS custom property names.

This will generate this CSS:

```text
body {
    --wp--custom--line-height--xs: 1;
    --wp--custom--line-height--sm: 1.25;
    --wp--custom--line-height--md: 1.5;
    --wp--custom--line-height--lg: 1.75;
}
```text

There is no limit to the amount of nesting you can do, but keep in mind that the more you nest, the longer your CSS custom property names become.

## Practical usage

What you use thesettings.customproperty for is entirely up to you. At its core, all it really does is generate CSS custom properties, which don’t do anything on their own. Custom properties must also be used in CSS.

In the previoustheme.jsonexample above, you created a set of line-heights. There are a number of ways you can put these into practical use.

### Use in theme.json styles

In theStyles documentation, you will learn how to apply styles to the root element, elements, and blocks viatheme.json. This will be one of the primary use cases for integrating withsettings.custom.

Suppose you wanted to register the same set of line-heights from above and make use of them. Maybe you want to set the root element to themdline-height and Paragraph blocks tolg. You can access each line-height property viavar:custom|line-height|mdandvar:custom|line-height|lg, respectively.

Use this code in yourtheme.jsonfile:

```json
{
    "version": 2,
    "settings": {
        "custom": {
            "lineHeight": {
                "xs": "1",
                "sm": "1.25",
                "md": "1.5",
                "lg": "1.75"
            }
        }
    },
    "styles": {
        "typography": {
            "lineHeight": "var:custom|line-height|md"
        }
        "blocks": {
            "core/paragraph": {
                "typography": {
                    "lineHeight": "var:custom|line-height|lg"
                }
            }
        }
    }
}
```text

You can also reference the values via their CSS custom properties. For example, instead of usingvar:custom|line-height|md, usevar( --wp--custom--line-height--md ).

Remember, you will learn more about styling viatheme.jsonfrom theStyles documentation. You can use what you learn there to combine with the techniques outlined here.

### Use in CSS

There are times when you might need to reference the generated CSS custom properties directly in CSS, such as yourstyle.cssfile. To do this, you must use the CSS custom property name.

Suppose you needed to target a class with the name of.example-classand to give it thesmline-height that you’ve registered. Use this code in your CSS:

```php
.example-class {
    line-height: var( --wp--custom--line-height--sm );
}
```text

First published

October 17, 2023

Last updated

October 17, 2023

[PreviousColorPrevious: Color](https://developer.wordpress.org/themes/global-settings-and-styles/settings/color/)
[NextDimensionsNext: Dimensions](https://developer.wordpress.org/themes/global-settings-and-styles/settings/dimensions/)
