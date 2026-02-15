# Position

**Source:** [https://developer.wordpress.org/themes/global-settings-and-styles/settings/position/](https://developer.wordpress.org/themes/global-settings-and-styles/settings/position/)



# Position




## In this article


Table of Contents- Position settingsEnabling sticky positioning


↑Back to top



Thesettings.positionproperty intheme.jsongives you control over the global positioning settings for blocks in WordPress. It’s important to note that this lets you configure the available settings in the user interface, not the position styles.


## Position settings


positionis an object that’s nested directly within the top-levelsettingsproperty intheme.json. Currently, it only lets you set a single property:


- sticky:A boolean value for enabling block support for thePosition: Stickyoption.


Take a look at thepositionproperty in the context of atheme.jsonfile with its default values:


```
{
	"version": 2,
	"settings": {
		"position": {
			"sticky": false
		}
	}
}
```


### Enabling sticky positioning


Sticky positioning can be particularly useful in theme designs that feature a header that sticks to the top of the screen as the user scrolls down the page. This is one of the primary use cases, but it can also be useful in other scenarios.


Setting a block to the sticky position will stick the block to its most immediate parent when the user scrolls the page. Sticky positioning is only possible if enabled intheme.json.


To enable sticky positioning for blocks that support it, setsettings.position.stickytotrue:


```
{
	"version": 2,
	"settings": {
		"position": {
			"sticky": true
		}
	}
}
```


This will enable a newPositiontab in the block inspector controls (for blocks that support the position feature, such as Group). The control will show a dropdown select with the available position options:DefaultandSticky:



If you want to create a sticky header, note that you cannot use positioning on the Header template part. You must wrap it with a containing Group block and apply the sticky positioning to the Group.





First published


October 17, 2023






[PreviousLightboxPrevious: Lightbox](https://developer.wordpress.org/themes/global-settings-and-styles/settings/lightbox/)
[NextShadowNext: Shadow](https://developer.wordpress.org/themes/global-settings-and-styles/settings/shadow/)


