# Lightbox

**Source:** [https://developer.wordpress.org/themes/global-settings-and-styles/settings/lightbox/](https://developer.wordpress.org/themes/global-settings-and-styles/settings/lightbox/)



# Lightbox




## In this article


Table of Contents- Lightbox settingsEnabling lightbox for imagesDisabling user editing


↑Back to top



settings.lightboxis a specific setting that you can enable for supported blocks. It enables a lightbox feature that expands an image when a site visitor clicks on an image.


This setting is only available as of WordPress 6.4 and is specific to the core Image block (core/image).


## Lightbox settings


Thelightboxsetting is specific to the Image block, so the following examples will be shown in that context.


Thelightboxproperty is an object that has two nested properties that you can configure:


- enabled:Whether to enable the lightbox feature for the Image block. The default value isundefined(the equivalent of being disabled).
- allowEditing:Whether to show theExpand on clickoption in the interface, which allows the user to enable/disable lightbox for individual images. Defaults totrue.


Here is a look at the defaulttheme.json:


```
{
	"version": 2,
	"settings": {
		"blocks": {
			"core/image": {
				"lightbox": {
					"allowEditing": true
				}
			}
		}
	}
}
```


### Enabling lightbox for images


To enable the lightbox feature for Image blocks used throughout the site, you must setsettings.blocks.core/image.lightbox.enabledto true intheme.json:


```
{
	"version": 2,
	"settings": {
		"blocks": {
			"core/image": {
				"lightbox": {
					"enabled": true
				}
			}
		}
	}
}
```


On the front-end of the site, visitors will be able to expand the image when clicking on it. The image will then overlay the entire screen (including anxbutton for closing the overlay), as shown below:



### Disabling user editing


By default, WordPress will show anExpand on Clickoption under theSettingstab for the Image block:



This control allows your theme’s users to enable or disable the lightbox feature on a per-block basis.


To disallow user editing, you must setsettings.blocks.core/image.lightbox.allowEditingtofalseintheme.json:


```
{
	"version": 2,
	"settings": {
		"blocks": {
			"core/image": {
				"lightbox": {
					"allowEditing": false
				}
			}
		}
	}
}
```





First published


October 17, 2023






[PreviousLayoutPrevious: Layout](https://developer.wordpress.org/themes/global-settings-and-styles/settings/layout/)
[NextPositionNext: Position](https://developer.wordpress.org/themes/global-settings-and-styles/settings/position/)


