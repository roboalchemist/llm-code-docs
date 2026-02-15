# Applying Styles

**Source:** [https://developer.wordpress.org/themes/global-settings-and-styles/styles/applying-styles/](https://developer.wordpress.org/themes/global-settings-and-styles/styles/applying-styles/)



# Applying Styles




## In this article


Table of Contents- Styling the root element
- Styling elementsStyling pseudo-classes
- Styling blocksStyling elements nested in blocksStyling block style variations (block styles)


↑Back to top



Traditionally, theme authors would style everything from a stylesheet—and they still sometimes must. In modern WordPress, you can also style most, if not all, of your theme directly from yourtheme.jsonfile.


When you use this standard system, it is also reflected in theAppearance > Editor > Stylesinterface. This means your theme’s users with access to that admin screen can also make changes that easily work alongside your theme’s styles. But it also means that you can design your theme directly from this visual interface if you choose to do so.


theme.jsonsupports styles at three different levels:


- Root (global)
- Elements
- Blocks


In this document, you will learn the syntax necessary for styling each of these things via JSON.


## Styling the root element


When referring to the “root” element in WordPress themes, we’re specifically talking about the HTML<body>tag. It’s the root of the visual output for the page.


Technically, when styling the root element, you are addingglobalstyles that trickle down through the design and are used unless a more specific element or block style overrides them. For example, you’ll likely want to set a default font-family or font-size that is used across the entire design. But you’ll, of course, want to change that in specific instances.


Because these are global styles, it means that they belong directly under thestylesproperty.


So let’s add a default text and background color to show how this works:


```
{
	"version": 2,
	"styles": {
		"color": {
			"text": "#000000",
			"background": "#f5f1ea"
		}
	}
}
```


As you can see, thecolorproperty is nested directly beneath thestylesproperty. This means that thetextandbackgroundcolors are applied directly to the<body>element by WordPress, resulting in this CSS in the editor and on the front end:


```
body {
	background: #f5f1ea;
	color: #000000;
}
```


And because of the way thecascadeworks in CSS, these colors will be used for everything, unless a more specific style rule overwrites it.


If you open your site on the front end or viaAppearance > Editorin the WordPress admin, you should see your colors applied:



You are not just limited to colors. You can addtypography,spacing, and more here. The root element supports almost all of the available style properties, which you can reference in theSupported Stylesdocumentation.


Thestyles.spacing.paddingproperty has a unique use case when used in conjunction withsettings.useRootPaddingAwareAlignments. For more information on how these two work together, read theUse Root Padding Aware Alignmentsdocumentation.


## Styling elements


WordPress has a standard system for styling elements viatheme.json. In this case, “elements” usually maps to actual HTML elements. But there are cases where it’s referring to something that doesn’t map directly to a single HTML element. In general, these should be reasonably straightforward.


Just like styling the root element and blocks, which you’ll learn about below, you can apply a wide range of thesupported stylesto elements.


The currently-supported elements are:


- button:Applied to<button>elements and button-like links, such as that used for the Button block.
- caption:Applied to media captions, which are wrapped in a<figcaption>element.
- cite:Applied to the<cite>element when used for citations, such as that used for the Quote and Pullquote blocks.
- heading:Applied to all heading elements from<h1>through<h6>, but these can be overridden for individual headings.
- h1 - h6:Each of the<h1>through<h6>elements can be individually styled.
- link:Applied to the<a>tag, which is used to create links.


Let’s try a real example now. Suppose you wanted to give all buttons across the site a white text color that sits atop a red background. You need to target thetextandbackgroundproperties ofstyles.elements.button.color.


Add this code to yourtheme.jsonfile:


```
{
	"version": 2,
	"styles": {
		"elements": {
			"button": {
				"color": {
					"text": "#ffffff",
					"background": "#aa3f33"
				}
			}
		}
	}
}
```


If you view a button in the Site Editor or on the front end of the site, you should see these colors applied:



Some elements both serve as element styles and the foundation of more specific blocks. In the case of elements that also tie into blocks, the block styles will overrule the element styles. For example, the Button and Heading blocks can have their own styles but they will fall back to thebuttonandheadingelement styles.


WordPress will generate this CSS in both the editor and on the front end for yourbuttonelement styles:


```
.wp-element-button, 
.wp-block-button__link {
	background-color: #aa3f33;
	color: #ffffff;
}
```


WordPress sometimes—but not always—gives elements a specific CSS class with the naming scheme of.wp-element-{$element}. For example, button elements have the.wp-element-buttonclass. The styles you provide viatheme.jsonare then applied to that CSS class.


As you can see in the generated CSS, WordPress is targeting the.wp-element-buttonclass when styling thebuttonelement. But it’s also specifically targeting the.wp-block-button__linkclass for backward compatibility with the Button block.


### Styling pseudo-classes


You can also add style properties for a standard set of CSS pseudo-classes for some elements. Generally, this will be for features like link hover and focus styles.


Thebuttonandlinkelements support these pseudo-classes:


- :hover
- :focus
- :active
- :visited


Each pseudo-class must be added as a property nested under the element you want to style. For example, you must targetstyles.elements.link.:hoverto customize link hover styles.


Let’s look at this in context using the previous example of stylingbuttonelements. Suppose you wanted to change the background color when a user’s mouse hovers over buttons. Use thistheme.jsoncode to achieve that:


```
{
	"version": 2,
	"styles": {
		"elements": {
			"button": {
				"color": {
					"text": "#ffffff",
					"background": "#aa3f33"
				},
				":hover": {
					"color": {
						"background": "#822f27"
					}
				}
			}
		}
	}
}
```


## Styling blocks


One of the great things about the block system is that it provides a standardized system for styling any block. This means that you can add styles for core WordPress blocks as well as third-party plugin blocks directly intheme.json.


To style a specific block, you must targetstyles.blocks.blocknamein yourtheme.jsonfile. From there, you can add any of the block’ssupported styles.


Let’s take a look at a basic example. Assume that you want to give a slightly rounded border to all Image blocks. For this, you need to target theborder.radiusproperty.


Add this code to yourtheme.jsonfile:


```
{
	"version": 2,
	"styles": {
		"blocks": {
			"core/image": {
				"border": {
					"radius": "6px"
				}
			}
		}
	}
}
```


This should make any instance of the Image block on your site appear with a rounded border:



WordPress will also generate this CSS for the nested<img>element within the Image block for both the editor and front end:


```
.wp-block-image img {
	border-radius: 6px;
}
```


You can add styles for as many or as few blocks as you want. That’s entirely up to you and what you want to accomplish with your design. Have fun with it!


For a full list of core WordPress blocks that you can style, visit theCore Blocks Reference. Note that this does not include blocks from plugins and other third-party sources.


When targeting a block’s styles, you must know both its namespace and slug. Above, you learned that the Image block has the namespace (core) and slug (image), creating the namespace/slug combination ofcore/image. All core WordPress blocks have thecorenamespace, and you can find this information for any block (including from third-party plugins) in itsblock.jsonfile.


### Styling elements nested in blocks


You can also add custom styles for elements that are nested within blocks. This feature gives you a lot of flexibility for contextually styling elements directly withintheme.json.


When styling a block’s nested elements, you must pass anelementsobject directly under the block property:styles.blocks.blockname.elements.


Suppose you wanted a large font size for the PullQuote block but you wanted to create a fluid size for its nested<cite>element that never grew larger than50%of the parent block or1.5rem, whichever is the larger of the two.


For this, you need to define thetypography.fontSizefor both thecore/pullquoteblock and its nestedciteelement intheme.json:


```
{
	"version": 2,
	"styles": {
		"elements": {
			"core/pullquote": {
				"typography": {
					"fontSize": "2.25rem"
				},
				"elements": {
					"cite": {
						"typography": {
							"fontSize": "max( 50%, 1.5rem )"
						}
					}
				}
			}
		}
	}
}
```


The font-size will now look like this in the editor:



WordPress generates this CSS for styling both the Pullquote block and its nested<cite>element:


```
.wp-block-pullquote {
	font-size: 2.25rem;
}

.wp-block-pullquote cite {
	font-size: max( 50%, 1.5rem );
}
```


### Styling block style variations (block styles)


Since WordPress 6.2, you can customize the core block style variations (i.e., block styles) viatheme.json. This feature allows you to usesupported styleswithout having to write custom CSS in a separate stylesheet.


To customize a block style variation, you must add a nestedvariationsproperty within the block you want to style intheme.json. Then, each variation can use any of the block’s supported styles.


Let’s walk through an example of modifying the Button block’s Outline style variation. Suppose you wanted to define the border color, style, and width that is specific to this block style variation.


Add this code to yourtheme.json:


```
{
	"version": 2,
	"styles": {
		"blocks": {
			"core/button": {
				"variations": {
					"outline": {
						"border": {
							"color": "currentColor",
							"style": "solid",
							"width": "2px"
						}
					}
				}
			}
		}
	}
}
```


You should now see these changes reflected in the editor when the Outline block style variation is selected for the Button block:



The currently available blocks and their core WordPress style variations are:


- core/button:outline,fill
- core/image:rounded
- core/quote:plain
- core/site-logo:rounded
- core/separator:wide,dots
- core/social-links:logos-only,pill-shape
- core/table:stripes
- core/tag-cloud:outline


For a deeper dive into customizing block style variations, check outCustomizing core block style variations via theme.jsonon the WordPress Developer Blog.


Customblock style variations are not currently supported intheme.json. There is anopen ticket for the feature. For now, you are limited to the core block style variations.





First published


October 17, 2023


Last updated


January 5, 2024



[PreviousStylesPrevious: Styles](https://developer.wordpress.org/themes/global-settings-and-styles/styles/)
[NextUsing PresetsNext: Using Presets](https://developer.wordpress.org/themes/global-settings-and-styles/styles/using-presets/)


