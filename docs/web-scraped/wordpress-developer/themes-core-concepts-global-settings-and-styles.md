# Global Settings and Styles

**Source:** [https://developer.wordpress.org/themes/core-concepts/global-settings-and-styles/](https://developer.wordpress.org/themes/core-concepts/global-settings-and-styles/)

## In this article

Table of Contents- What is theme.json?

- theme.json structure

- Settings and styles hierarchy

↑Back to top

As you learned inTheme Structure,theme.jsonis a standard file that WordPress looks for in your theme. While it is not technically required for a block theme, it is almost always necessary to configure various settings and styles for your theme.

This documentation is a quick introduction on whattheme.jsonis and how it works. However, it is such a massive topic that there is a dedicated chapter that explores everything you can do with it:Global Settings and Styles.

## What is theme.json?

theme.jsonis a configuration file that tells WordPress what settings you want to enable, how to style specific elements and blocks, and which templates and template parts to register.

Some of the things you can do withtheme.jsonare:

- Enable or disable features like drop caps, padding, margin, and line-height.

- Add a color palette, gradients, duotones, and shadows.

- Configure typographical features like font families, sizes, and more.

- Add CSS custom properties.

- Register custom templates and assign parts to template part areas.

Yourtheme.jsonconfiguration will be reflected in what you see in places like the post, template, and site editors in the WordPress admin. Custom styles, in particular, will be reflected in theStylesinterface:

## theme.json structure

Atheme.jsonfile can be as little as a few lines of code, such as this example that enables the appearance tools for blocks:

```text
{
    "$schema": "https://schemas.wp.org/trunk/theme.json",
    "version": 2,
    "settings": {
        "appearanceTools": true
    }
}
```text
Or it can be a massively complex file that spans 1,000s of lines of code. How many of the features you want to configure is entirely up to you.

The starting point is understanding the top-level properties that can be configured. Here is an outline of what this looks like:

```text
{
    "$schema": "https://schemas.wp.org/trunk/theme.json",
    "version": 2,
    "settings": {},
    "styles": {},
    "customTemplates": {},
    "templateParts": {},
    "patterns": []
}
```text
Here are what each of these properties define:

- $schema:Used for defining the supported JSON schema, which will integrate with many code editors to give you on-the-fly hints and error reporting.

- version:Thetheme.jsonschema version you are building for. The latest version is 2 and can always be found in thetheme.jsonLiving Reference, a document that lists the most up-to-date properties you can set.

- settings:Used to define your block controls and color palettes, font sizes, and more.

- styles:Used to apply colors, font sizes, custom CSS, and more to the website and blocks.

- customTemplates:Metadata for custom templates defined in your theme’s/templatesfolder.

- templateParts:Metadata for template parts defined in your theme’s/partsfolder.

- patterns:An array of pattern slugs to be registered from thePattern Directory.

You will learn more about these properties and their sub-properties in theGlobal Settings and Styleschapter.

## Settings and styles hierarchy

Thetheme.jsonfile in your theme is only one level in a hierarchy of setting and style configurations for a website. This means it can be overridden under certain circumstances.

The order of this hierarchy from lowest to highest is:

- WordPresstheme.json:WordPress has its owntheme.jsonfile that defines the default settings and styles.

- Themetheme.json:Anything you define in your theme’stheme.jsonfile overrides the WordPress defaults.

- Child themetheme.json:If active, a child theme’stheme.jsontakes priority over the main or “parent” theme.

- User configuration:Users can further customize how their site works underAppearance > Editorin the WordPress admin, and the JSON data is saved in their site’s database. Their choice takes priority over all other levels in the hierarchy.

There are also filter hooks available that let plugin and theme authors override the values dynamically. To learn more about these, check outHow to modify theme.json data using server-side filtersfrom the WordPress Developer Blog.

The important thing to remember is that anything configured in yourtheme.jsonfile may not take priority in the hierarchy.

First published

November 21, 2023

Last updated

December 14, 2023

[PreviousIncluding AssetsPrevious: Including Assets](https://developer.wordpress.org/themes/core-concepts/including-assets/)
[NextGlobal Settings and Styles (theme.json)Next: Global Settings and Styles (theme.json)](https://developer.wordpress.org/themes/global-settings-and-styles/)
