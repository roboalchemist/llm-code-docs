# Spacing

**Source:** [https://developer.wordpress.org/themes/global-settings-and-styles/settings/spacing/](https://developer.wordpress.org/themes/global-settings-and-styles/settings/spacing/)

## In this article

Table of Contents- Spacing settings

- Enabling or disabling spacing optionsEnabling block spacing (block gap)Enabling margin and paddingDisabling user-defined spacing sizes
- Defining allowed spacing units
- Spacing scale and sizesCustom spacing scaleCustom spacing sizes

↑Back to top

Spacing is one of the most complex parts of web design. It involves combining things like margin, padding, gap, line height, font size, and more into a harmonious flow. Doing this well requires a keen eye and a foundational understanding of how each of these pieces come together.

Thesettings.spacingproperty intheme.jsoncovers settings related specifically to margin, padding, and gap.

This handbook also has documentation fortypography settingsandapplying stylesto blocks, both of which play roles in wrangling the spacing for your overall design.

## Spacing settings

Thesettings.spacingobject has several properties that you can configure:

- blockGap:Whether to enable theBlock Spacingoption for blocks that support it. Can be a boolean value (true/false). Defaults tonull. If set to null, WordPress’ generated CSS is also disabled.
- margin:Whether to enable theMarginoption for supported blocks. Defaults tofalse.
- padding:Whether to enable thePaddingoption for supported blocks. Defaults tofalse.
- customSpacingSize:Whether to allow users to input custom spacing values for supported blocks. Defaults totrue.
- spacingScale:A configuration object for defining a custom spacing scale. WordPress defines a default scale with seven steps that increment by1.5rem.
- spacingSizes:An array of custom size objects that may overrule the spacing scale or add to it.
- units:An array of possible CSS units that users can select from when adding custom spacing.

Here is what spacing settings look like the default WordPresstheme.json:

```json
{
    "version": 2,
    "settings": {
        "spacing": {
            "blockGap": null,
            "customSpacingSize": true,
            "margin": false,
            "padding": false,
            "spacingScale": {
                "operator": "*",
                "increment": 1.5,
                "steps": 7,
                "mediumStep": 1.5,
                "unit": "rem"
            },
            "spacingSizes": [],
            "units": [ "px", "em", "rem", "vh", "vw", "%" ]
        }
    }
}
```text

## Enabling or disabling spacing options

As noted in the default settings in the previous section, there are several settings that are merely for enabling or disabling elements in the user interface. In this section, you will learn how to configure each of these.

### Enabling block spacing (block gap)

In WordPress, the “block gap” refers to the spacing between blocks on a page. In most cases, this is the vertical spacing between blocks. But it can also refer to horizontal spacing when blocks are set in horizontal flex or in a grid layout.

In flow layouts (the default), the block gap is applied using the CSSmargin-topproperty to sibling elements. In flex or grid layouts, it is applied using the CSSgapproperty.

WordPress will automatically output the CSS for the block gap if this setting is not disabled entirely (the default).

You will learn more about defining block gap styles in theStyles documentation, but having a baseline understanding of the terminology should help you decide how to work with this option.

The primary purpose of thesettings.spacing.blockGapis to enable or disable the user interface for theBlock Spacingcontrol for blocks that support it. You can do this by setting it totrueorfalse.

However, you can also leave it asnull(the default value). This disables the user interface. In addition, it removes the WordPress-generated block spacing CSS.

Leaving this to the defaultnullvalue is not usually recommended except in special cases. Generally, you would want consistent spacing as part of your design’s vertical rhythm. If set tonull, you will need to handle that manually via custom CSS.

Use this table as a reference when determining which value to assign tosettings.spacing.blockGap:

`blockGap` ValueBlock Spacing ControlWordPress-generated CSS`null`NoNo`true`YesYes`false`NoYes
Now try configuring the setting. Open yourtheme.jsonfile and set the property totrue:

```json
{
    "version": 2,
    "settings": {
        "spacing": {
            "blockGap": true
        }
    }
}
```text

For blocks that support the property, you should now see theBlock Spacingcontrol appear. Here is a screenshot of what that looks like on the Post Template block:

Because of the way the layout system works in WordPress, it will output CSS that is specific to individual containers to handle the gap between blocks nested within those containers. For the screenshot example, here’s what that CSS looks like:

```text
.wp-container-17.wp-container-17 > :first-child:first-child {
    margin-block-start: 0;
}

.wp-container-17.wp-container-17 > * {
    margin-block-start: var(--wp--preset--spacing--plus-4);
    margin-block-end: 0;
}
```text

Of course, the ID (17) and value will be different on a case-by-case basis.

### Enabling margin and padding

The margin and padding settings are a little more straightforward. They are both disabled by default, and you can enable them by setting their values totrueintheme.json:

```json
{
    "version": 2,
    "settings": {
        "spacing": {
            "margin": true,
            "padding": true
        }
    }
}
```text

This will make theMarginandPaddingcontrols appear for supported blocks in their inspector controls in the sidebar:

Of course, you are free to leave both of these to the default value offalseor configure them to your liking.

### Disabling user-defined spacing sizes

When any one of theblockGap,margin, orpaddingspacing settings are enabled, WordPress will output a user interface for setting those values for blocks that support them. By default, users can select from a list of preset spacing sizes (see “Spacing scale and sizes” below) or input a custom value.

In this screenshot, you can see that there is a customBlock Spacingsetting chosen for the Buttons block:

You may want to limit users to your predefined spacing scale or sizes for your theme. This is often a good idea if you want to ensure consistent spacing throughout your design.

To do this, you must set thecustomSpacingSizessetting tofalse. This disables the custom spacing option in the editor UI but leaves the control for the theme’s defined sizes available:

```json
{
    "version": 2,
    "settings": {
        "spacing": {
            "customSpacingSize": false
        }
    }
}
```text

With custom spacing sizes disabled, theBlock Spacingoption from the Buttons block example will be limited to the theme’s preset sizes:

## Defining allowed spacing units

If you choose to enable thesettings.spacing.customSpaceSizeoption covered in the previous section, you will need to make another choice: which CSS unit values will your theme allow?

By default, WordPress lets users select from a subset of possible CSS units (there are dozens in the CSS specification). To choose which units you want to support, you must add them into thesettings.spacing.unitsarray intheme.json(shown with the defaults):

```json
{
    "version": 2,
    "settings": {
        "spacing": {
            "units": [ "px", "em", "rem", "vh", "vw", "%" ]
        }
    }
}
```text

The currently-allowed possible units that you can choose from are:

- px
- %
- em
- rem
- vw
- vh
- vmin
- vmax
- ch
- ex
- cm
- mm
- in
- pc
- pt

As of WordPress 6.3, the allowed units are limited to the above list. There is anopen ticketto expand these to support more modern units.

## Spacing scale and sizes

One of the most important things that you should configure in yourtheme.jsonfile is your spacing presets. WordPress will generate these presets as CSS custom properties, loading them in the editor and front end.

Most designers will use some type of standard scaling system for handling spacing, and WordPress gives you the flexibility to use whatever system you choose.

There are two methods for registering your spacing presets:

- spacingScale:A generated scale based on your configuration values.
- spacingSizes:Completely custom-defined spacing sizes.

Technically, you can use both of these methods, mixing and matching them. But it is generally recommended to choose one over the other for simplicity.

Spacing presets appear as choices for theBlock Spacing,Margin, andPaddingblock controls (for blocks that support them). This means that you can present users with spacing options that are specific to your theme. You can also use these presets in theStylessection in yourtheme.jsonor custom CSS.

WordPress generates a default spacing scale, as shown in this table:

CSS Custom PropertyCSS ValueLabel`--wp-preset--spacing--20``0.44rem`2X-Small`--wp-preset--spacing--30``0.67rem`X-Small`--wp-preset--spacing--40``1rem`Small`--wp-preset--spacing--50``1.5rem`Medium`--wp-preset--spacing--60``2.25rem`Large`--wp-preset--spacing--70``3.38rem`X-Large`--wp-preset--spacing--80``5.06rem`2X-Large
It is unlikely that this scale matches your design. So you will want to choose a method for overriding these default values.

### Custom spacing scale

WordPress allows theme authors to create a custom spacing scale by providing a set of configuration instructions. Each step in the scale generates a custom CSS property with the slug of--wp--preset--spacing--{step}(steps appear in increments of 10, regardless of their value).

ThespacingScaleobject has five sub-settings that themes can configure:

- operator:The operator used to increment the scale. The available options are+(addition) and*(multiplication). The default value is*.
- increment:A number in which to increment the scale by when used in conjunction with theoperatorsetting. The default value is1.5.
- steps:The total number of steps in the scale. The default value is7.
- mediumStep:The medium value of the scale. The default value is1.5.
- unit:A valid CSS spacing unit. The available options arepx,em,rem,vh,vw, and%. The default value isrem.

The following example is a custom scale with seven steps that increments by0.25rem:

```json
{
    "version": 2,
    "settings": {
        "spacing": {
            "spacingScale": {
                "operator": "+",
                "increment": 0.25,
                "steps": 7,
                "mediumStep": 1,
                "unit": "rem"
            }
        }
    }
}
```text

As shown in the screenshot, you should see a range slider thePadding,Margin, andBlock Spacingcontrols for setting your registered values:

When there are seven or fewer spacing presets, the interface will show a range slider for spacing controls. But more than seven displays a dropdown select. This applies to both thespacingScalemethod used here and thespacingSizesmethod in the next section.

This table represents your custom spacing scale (compare to the default scale to see how things have changed):

CSS Custom PropertyCSS ValueLabel`--wp-preset--spacing--20``0.25rem`2X-Small`--wp-preset--spacing--30``0.5rem`X-Small`--wp-preset--spacing--40``0.75rem`Small`--wp-preset--spacing--50``1rem`Medium`--wp-preset--spacing--60``1.25rem`Large`--wp-preset--spacing--70``1.5rem`X-Large`--wp-preset--spacing--80``1.75rem`2X-Large
ThemediumStepvalue is always assigned to the--wp--preset--spacing--50preset when WordPress generates the CSS, and the other preset slugs in the scale extend up/down from this middle number in increments of 10.

The spacing scale will never go below--wp--preset--spacing--10. For scales with more than 10 steps, the bottom end of the scale will not generate presets because themediumStepis always set to--wp--preset--spacing--50.

#### Disable the spacing scale

If you want to disable WordPress’ spacing scale altogether, you can setstepsto0intheme.json:

```json
{
    "version": 2,
    "settings": {
        "spacing": {
            "spacingScale": {
                "steps": 0
            }
        }
    }
}
```text

This can be useful when choosing to register completely custom spacing sizes, as covered in the next section.

### Custom spacing sizes

If you want more precise control over the spacing options, you can build out the individual spacing sizes instead of using the WordPress spacing scale system. This provides control over each option’s name, size, and slug.

ThespacingSizesproperty lets you define an array of size objects. Each size object accepts three values:

- name:The human-readable title for the size, which can be translated.
- size:A valid CSS size. This can be a number and unit, a fluid size usingclamp(), or a reference to another custom CSS property.
- slug:The slug for the size, which will be appended to a generated CSS custom property:--wp--preset--spacing--{slug}.

The following is an example of creating a five-step scale that increments by0.25rem:

```json
{
    "version": 2,
    "settings": {
        "spacing": {
            "spacingSizes": [
                {
                    "name": "Step 1",
                    "size": "0.25rem",
                    "slug": "10"
                },
                {
                    "name": "Step 2",
                    "size": "0.5rem",
                    "slug": "20"
                },
                {
                    "name": "Step 3",
                    "size": "0.75rem",
                    "slug": "30"
                },
                {
                    "name": "Step 4",
                    "size": "1rem",
                    "slug": "40"
                },
                {
                    "name": "Step 5",
                    "size": "1.25rem",
                    "slug": "50"
                }
            ]
        }
    }
}
```text

You should see a range slider thePadding,Margin, andBlock Spacingcontrols for setting your registered values, as shown here:

This table represents your custom spacing sizes:

CSS Custom PropertyCSS ValueLabel`--wp-preset--spacing--10``0.25rem`Step 1`--wp-preset--spacing--20``0.5rem`Step 2`--wp-preset--spacing--30``0.75rem`Step 3`--wp-preset--spacing--40``1rem`Step 4`--wp-preset--spacing--50``1.25rem`Step 5

#### Creating fluid sizes


If you want to use fluid spacing, you must use thesettings.spacing.spacingSizesmethod for controlling the size presets.

To use fluid sizes, you merely need to add them as thesizeparameter for each of the size objects undersettings.spacing.spacingSizes.clamp(),min(),max(), and other valid CSS values are supported.

Here is an example of a seven-step fluid spacing scale registered as individual sizes intheme.json:

```json
{
    "version": 2,
    "settings": {
        "spacing": {
            "spacingSizes": [
                {
                    "name": "Fluid Scale -3",
                    "size": "clamp( 0.31rem, 0.11vw + 0.28rem,  0.35rem )",
                    "slug": "minus-3"
                },
                {
                    "name": "Fluid Scale -2",
                    "size": "clamp( 0.47rem, 0.16vw + 0.42rem,  0.53rem )",
                    "slug": "minus-2"
                },
                {
                    "name": "Fluid Scale -1",
                    "size": "clamp( 0.71rem, 0.25vw + 0.63rem,  0.79rem )",
                    "slug": "minus-1"
                },
                {
                    "name": "Fluid Scale +/- 0 (Base)",
                    "size": "clamp( 1.06rem, 0.37vw + 0.95rem,  1.19rem )",
                    "slug": "base"
                },
                {
                    "name": "Fluid Scale +1",
                    "size": "clamp( 1.20rem, 0.85vw + 0.94rem,  1.48rem )",
                    "slug": "plus-1"
                },
                {
                    "name": "Fluid Scale +2",
                    "size": "clamp( 1.34rem, 1.5vw + 0.89rem,  1.86rem )",
                    "slug": "plus-2"
                },
                {
                    "name": "Fluid Scale +3",
                    "size": "clamp( 1.86rem, 3.7vw + -0.05rem,  2.32rem )",
                    "slug": "plus-3"
                }
            ]
        }
    }
}
```text

This results in the following values, as shown in this table:

CSS Custom PropertyCSS ValueLabel`--wp-preset--spacing--minus-1``clamp( 0.31rem, 0.11vw + 0.28rem,  0.35rem )`Fluid Scale -3`--wp-preset--spacing--minus-2``clamp( 0.47rem, 0.16vw + 0.42rem,  0.53rem )`Fluid Scale -2`--wp-preset--spacing--minus-3``clamp( 0.71rem, 0.25vw + 0.63rem,  0.79rem )`Fluid Scale -1`--wp-preset--spacing--base``clamp( 1.06rem, 0.37vw + 0.95rem,  1.19rem )`Fluid Scale +/- 0 (Base)`--wp-preset--spacing--plus-1``clamp( 1.20rem, 0.85vw + 0.94rem,  1.48rem )`Fluid Scale +1`--wp-preset--spacing--plus-2``clamp( 1.34rem, 1.5vw + 0.89rem,  1.86rem )`Fluid Scale +2`--wp-preset--spacing--plus-3``clamp( 1.86rem, 3.7vw + -0.05rem,  2.32rem )`Fluid Scale +3

First published

October 17, 2023

Last updated

October 17, 2023

[PreviousShadowPrevious: Shadow](https://developer.wordpress.org/themes/global-settings-and-styles/settings/shadow/)
[NextTypographyNext: Typography](https://developer.wordpress.org/themes/global-settings-and-styles/settings/typography/)
