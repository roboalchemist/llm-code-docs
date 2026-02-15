# Introduction to theme.json

**Source:** [https://developer.wordpress.org/themes/global-settings-and-styles/introduction-to-theme-json/](https://developer.wordpress.org/themes/global-settings-and-styles/introduction-to-theme-json/)



# Introduction to theme.json




## In this article


Table of Contents- theme.json structure
- theme.json propertiesAdding a versionAdding a JSON schemaAdding settings, styles, and more


↑Back to top



theme.jsonis a configuration file that lets you define the global settings, styles, and more for your theme. The file works with both block and classic themes.


When building a block theme,theme.jsonmay be the most important file in the entire theme. In a way, it is the foundational piece that trickles down to every other component. That’s why this chapter is one of the most extensive in the handbook.


Some of the things you can do withtheme.jsoninclude (but are not limited to):


- Enabling block features in the user interface, such as color, typography, and spacing controls.
- Configuring a custom color palette, duotone filters, and background gradients.
- Defining typographical features like font families, bundling web fonts, and more.
- Adding your own CSS custom properties.
- Adjusting the overall design by working within the core styles system.


The settings and styles that you configure intheme.jsonare ultimately reflected on both the front end of the site and WordPress’ built-in editors. As shown in this screenshot, you can see that a variation of the default Twenty Twenty-Three theme as it’s looks in theAppearance > Editorscreen in the admin:



Each part of that design is handled directly intheme.json, and the user can further customize it through the built-inStylesinterface.


theme.jsonrepresents what you might call a “common language” that allows WordPress, your theme, plugins, and users to effectively communicate. Because it is built atop a standardized system, each component plays a role in bringing the overall site to life.


## theme.json structure


Thetheme.jsonfile can be broken down into several top-level sections as shown in this code snippet:


```
{
	"$schema": "https://schemas.wp.org/trunk/theme.json",
	"version": 2,
	"settings": {},
	"styles": {},
	"customTemplates": {},
	"templateParts": {},
	"patterns": []
}
```


Throughout this chapter, you will learn about each of these properties and how you can work with them to turn the design in your imagination into a working theme.


Customizing thetheme.jsonfile directly in your theme requires that you have some familiarity with JSON code. You don’t need to be an expert (copying and pasting can get you pretty far), but having some foundational knowledge of how to format JSON will definitely help.


You should also have a baseline understanding of CSS. While you do not need to directly write CSS code intheme.json, many of the features are mapped to CSS properties and values. Understanding the relationship betweentheme.jsonsettings and styles and their CSS counterparts will help you in the long run.


For more information on JSON and CSS, read:


- MDN Web Docs: CSS
- MDN Web Docs: JSON


## theme.json properties


As you could see in the previous section, thetheme.jsonfile has several top-level properties. Some of these accept just a single value, but most have nested sub-properties with their own values.


These are the current top-level properties that you can set intheme.json:


- version:Thetheme.jsonschema version you are building for.
- $schema:Used for defining the supported JSON schema, which will integrate with many code editors to give you on-the-fly hints and error reporting.
- settings:Used to define which block controls appear, configure presets, and more.
- styles:Used to apply colors, font sizes, custom CSS, and other styles  to the website and blocks.
- customTemplates:Metadata for custom templates defined in your theme’s/templatesfolder.
- templateParts:Metadata for template parts defined in your theme’s/partsfolder.
- patterns:An array of pattern slugs to be registered from thePattern Directory.


### Adding a version


At the very least, you should set theversionproperty in yourtheme.jsonfile. This should be an integer that matches the API version used to read and understand yourtheme.jsoncode.


The API is currently at version2. You can always find the most up-to-date version via thetheme.jsonLiving Referencedocument.


The bear minimum code that yourtheme.jsonfile should have is:


```
{
	"version": 2
}
```


Alltheme.jsoncode examples in this handbook include theversionproperty because it should always be set.


Technically, you can leave the version out, but WordPress will read your code as if it was on version1of the API. Using an outdated version may mean that your code will not be valid, at least as it is documented here in the handbook.


You should always strive to keep up to date with the latest API version and make sure it is set in yourtheme.jsonfile.


### Adding a JSON schema


An optional property that you can add to yourtheme.jsonis a URL to the JSON schema. This can be particularly helpful when working with any modern code editor. Adding the$schemaproperty will give you on-the-fly hints and error reporting in many code editors and is highly recommended.


To add support for JSON schema, add this to yourtheme.jsonfile:


```
{
	"$schema": "https://schemas.wp.org/trunk/theme.json",
	"version": 2
}
```


Again, this istechnicallyan optional property. But there is rarely a good reason to leave it out. It’s just good development practice to include it.


### Adding settings, styles, and more


The other properties available to you viatheme.jsonrequire more in-depth documentation than what can be covered in this introduction. They each have their own pages (and some with multiple sub-pages) in this chapter of the handbook.


Now it’s time to really dive into learning more abouttheme.json. You can take these next documentation steps as you prefer, but these are listed in their recommended reading order:


- Settings:Documentation for each of the standard and custom settings that you can configure viatheme.json.
- Styles:Learn how to use the standard design system to apply styles throughtheme.json, which also integrate with the user interface.
- Custom Templates:How to register custom post, page, and CPT (custom post type) templates for your theme.
- Template Parts:How to register custom template parts that can be reused across your theme.
- Patterns:How to bundle patterns from the official patterns repository with your theme.
- Style Variations:Documentation on creating customtheme.jsonstyle variations, giving your users alternative designs to choose from.





First published


October 17, 2023


Last updated


December 14, 2023



[PreviousGlobal Settings and Styles (theme.json)Previous: Global Settings and Styles (theme.json)](https://developer.wordpress.org/themes/global-settings-and-styles/)
[NextSettingsNext: Settings](https://developer.wordpress.org/themes/global-settings-and-styles/settings/)


