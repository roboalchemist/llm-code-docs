# Settings

**Source:** [https://developer.wordpress.org/themes/global-settings-and-styles/settings/](https://developer.wordpress.org/themes/global-settings-and-styles/settings/)



# Settings




## In this article


Table of Contents- The settings property
- Settings documentation



↑Back to top



Thesettingsproperty intheme.jsonlets you configure a wide range of settings for a WordPress install. It covers everything from color presets, to enabling typography design tools, to layout, and a little bit of everything in between.


This document contains links for learning about each of these settings, which have their own individual documentation pages.


## The settings property


settingsis a top-level property intheme.jsonand has multiple nested properties that you can define. And some of those nested properties have multiple levels of nesting of their own.


The following is an overarching look at these properties in the context of atheme.jsonfile:


```
{
	"version": 2,
	"settings": {
		"appearanceTools": false,
		"border": {},
		"color": {},
		"custom": {},
		"dimensions": {},
		"layout": {},
		"position": {},
		"shadow": {},
		"spacing": {},
		"typography": {},
		"useRootPaddingAwareAlignments": false,
		"blocks": {}
	}
}
```


## Settings documentation


Use the following links to explore specific settings that you can configure in yourtheme.jsonfile:


- appearanceTools:A catchall setting for enabling multiple other settings.
- border:Used for controlling the border width, style, color, and radius.
- color:Lets you register a color palette, gradients, duotone and configure color-related settings.
- custom: An object for adding custom settings, which are output as CSS custom properties.
- dimensions:Lets you configure the minimum height setting.
- layout:Used for setting layout properties like the content and wide widths.
- lightbox:Lets you configure the image lightbox feature.
- position:Currently lets you define support for sticky positioning.
- shadow:Lets you configure box-shadow support and define custom shadow presets.
- spacing:Used for configuring spacing-related settings, such as margin and padding,
- typography:Used for configuring typography-related settings, defining custom font sizes, and registering font families.
- useRootPaddingAwareAlignments:A boolean setting for how padding on the root element should work.
- blocks:An object for configuring per-block settings.


The Theme Handbook also maintains areference for available settingsbased on thetheme.jsonschema.





First published


October 10, 2023


Last updated


December 14, 2023



[PreviousIntroduction to theme.jsonPrevious: Introduction to theme.json](https://developer.wordpress.org/themes/global-settings-and-styles/introduction-to-theme-json/)
[NextAppearance ToolsNext: Appearance Tools](https://developer.wordpress.org/themes/global-settings-and-styles/settings/appearance-tools/)


