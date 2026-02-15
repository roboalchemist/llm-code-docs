# Styles

**Source:** [https://developer.wordpress.org/themes/global-settings-and-styles/styles/](https://developer.wordpress.org/themes/global-settings-and-styles/styles/)



# Styles




## In this article


Table of Contents- The styles property
- Styles documentation



↑Back to top



Thestylesproperty intheme.jsonlets you configure settings at the global level, for individual elements, and individual blocks. WordPress supports a standard subset of the CSS specification, but also allows you to add custom CSS directly in yourtheme.jsonfile.


When possible, it is recommended to add your theme styles via thestylesproperty, at least for standard WordPress features. This makes it possible for users to customize them viaAppearance > Editor > Styleswithout CSS specificity issues.


This document contains links for learning about the available style properties and how to apply styles to your theme via itstheme.jsonfile.


## The styles property


stylesis a top-level property intheme.jsonand has multiple nested properties that you can define. And some of those nested properties have multiple levels of nesting of their own.


The following is an overarching look at these properties in the context of atheme.jsonfile:


```
{
	"version": 2,
	"styles": {
		"elements": {},
		"blocks": {}
	}
}
```


The following is an example of what thestylesproperty could look like in a customtheme.jsonfile. This should give you a feel for how it is structured, but you will dive into this more deeply as you read through this section of the handbook:


```
{
	"version": 2,
	"styles": {
		"color": {
			"text": "#000000",
			"background": "#ffffff"
		},
		"elements": {
			"button": {
				"color": {
					"text": "#ffffff",
					"background": "#000000"
				}
			}
		},
		"blocks": {
			"core/code": {
				"color": {
					"text": "#ffffff",
					"background": "#000000"
				}
			}
		}
	}
}
```


## Styles documentation


Use the following links to explore configuring styles viatheme.jsonfile:


- Applying Styles:How to apply custom styles to your theme using the standard JSON syntax.
- Using Presets:How to use the presets that you’ve configured via thesettingsproperty in your styles.
- Styles Reference:A reference guide for the available style properties that you can use intheme.json.





First published


October 11, 2023


Last updated


December 14, 2023



[PreviousSettings ReferencePrevious: Settings Reference](https://developer.wordpress.org/themes/global-settings-and-styles/settings/settings-reference/)
[NextApplying StylesNext: Applying Styles](https://developer.wordpress.org/themes/global-settings-and-styles/styles/applying-styles/)


