# Dimensions

**Source:** [https://developer.wordpress.org/themes/global-settings-and-styles/settings/dimensions/](https://developer.wordpress.org/themes/global-settings-and-styles/settings/dimensions/)



# Dimensions




## In this article


Table of Contents- Dimensions settingsMinimum Height


↑Back to top



Thesettings.dimensionsproperty intheme.jsongives you control over the global dimensions settings for blocks. This property lets you decide which dimension controls are available in the user interface.


In this document, you will learn what thedimensionsproperty is for and how you can use it in your theme.


## Dimensions settings


dimensionsis an object that’s nested directly within the top-levelsettingsproperty intheme.json. Currently, it only lets you set a single property:


- minHeight:A boolean value for enabling block support for theMinimum Heightcontrol.


Take a look at thedimensionsproperty in the context of atheme.jsonfile with its default values:


```
{
	"version": 2,
	"settings": {
		"dimensions": {
			"minHeight": false
		}
	}
}
```


### Minimum Height


Thesettings.dimensions.minHeightproperty lets you control whether theMinimum Heightfield appears for blocks that have opted into support for the feature. As of WordPress 6.3, the only core WordPress blocks that do are Group and Post Content.


To enable support for the control, you must set the property’s value totrueintheme.json:


```
{
	"version": 2,
	"settings": {
		"dimensions": {
			"minHeight": true
		}
	}
}
```


This will enable the control in the interface. As shown in this screenshot, theMinimum Heightfield appears for the Group block (Stack variation):






First published


October 17, 2023






[PreviousCustomPrevious: Custom](https://developer.wordpress.org/themes/global-settings-and-styles/settings/custom/)
[NextLayoutNext: Layout](https://developer.wordpress.org/themes/global-settings-and-styles/settings/layout/)


