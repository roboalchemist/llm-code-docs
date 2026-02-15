# Border

**Source:** [https://developer.wordpress.org/themes/global-settings-and-styles/settings/border/](https://developer.wordpress.org/themes/global-settings-and-styles/settings/border/)



# Border



↑Back to top



Thesettings.borderproperty intheme.jsongives you control over the global border settings for blocks in WordPress. It’s important to note that this lets you configure the available settings in the user interface, not the border styles themselves.


Each of the border settings maps to a control at the individual block level and in theStylesinterface for blocks, letting you curate which controls are available to your theme users:



## Border settings


WordPress supports four border settings that you can configure via thesettings.borderproperty intheme.json. Each of them allows you to enable or disable a specific border feature and accepts a boolean (trueorfalse) value:


- color:Enables/Disables the border-color picker.
- radius:Enables/Disables the border-radius control.
- style:Enables/Disables the border-style selector (users have the option ofsolid,dashed, ordotted).
- width: Enables/Disables the border-width input.


By default, all border properties are set tofalse, as shown in this exampletheme.jsoncode:


```
{
	"version": 2,
	"settings": {
		"border": {
			"color": false,
			"radius": false,
			"style": false,
			"width": false
		}
	}
}
```


As of WordPress 6.3,color,style, andwidthare intertwined. If any one of them is set totrue, the others will be available as options within the user interface.

Also, setting theradiusoption tofalsedoes not work for the Button block. The border-radius control in the editor always appears.





First published


October 17, 2023






[PreviousBlocksPrevious: Blocks](https://developer.wordpress.org/themes/global-settings-and-styles/settings/blocks/)
[NextColorNext: Color](https://developer.wordpress.org/themes/global-settings-and-styles/settings/color/)


