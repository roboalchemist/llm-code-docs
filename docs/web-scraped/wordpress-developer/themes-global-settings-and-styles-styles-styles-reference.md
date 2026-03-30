# Styles Reference

**Source:** [https://developer.wordpress.org/themes/global-settings-and-styles/styles/styles-reference/](https://developer.wordpress.org/themes/global-settings-and-styles/styles/styles-reference/)

## In this article

Table of Contents- Border

- Color
- Dimensions
- Filter
- Shadow
- Spacing
- Typography
- CSS

↑Back to top

This is a reference to the available style properties that you can apply to the root element (global), individual elements, and individual blocks intheme.json. Please review theApplying Stylesdocumentation to learn how to apply styles to your theme.

## Border

There are two methods for working with theborderstyle property. The first is to target all sides of a block or element with the properties shown in the table:

PropertyTypeCSS Property`border.radius`string, object[border-radius](https://developer.mozilla.org/en-US/docs/Web/CSS/border-radius)`border.color`string, object[border-color](https://developer.mozilla.org/en-US/docs/Web/CSS/border-color)`border.style`string, object[border-style](https://developer.mozilla.org/en-US/docs/Web/CSS/border-style)`border.width`string, object[border-width](https://developer.mozilla.org/en-US/docs/Web/CSS/border-width)
Example usage intheme.json:

```json
{
    "version": 2,
    "styles": {
        "border": {
            "color": "#000000",
            "style": "solid",
            "width": "1px"
        }
    }
}
```

The second method is to specifically target thetop,right,bottom, andleftsides:

PropertyTypeCSS Property`border.<side>.color`string, object`border-<side>-color``border.<side>.style`string, object`border-<side>-style``border.<side>.width`string, object`border-<side>-width`
Example usage intheme.json:

```json
{
    "version": 2,
    "styles": {
        "border": {
            "top": {
                "color": "#000000",
                "style": "solid",
                "width": "1px"
            }
        }
    }
}
```

## Color

Thecolorstyle property lets you define the default text, background, and link colors for a block or element:

PropertyTypeCSS Property`color.text`string, object[color](https://developer.mozilla.org/en-US/docs/Web/CSS/color)`color.background-color`string, object[background-color](https://developer.mozilla.org/en-US/docs/Web/CSS/background-color)`color.link`string, object[color](https://developer.mozilla.org/en-US/docs/Web/CSS/color) (applied to nested `<a>` elements)
Example usage intheme.json:

```json
{
    "version": 2,
    "styles": {
        "blocks": {
            "core/group": {
                "color": {
                    "text": "#000000",
                    "background": "#ffffff",
                    "link": "#777777"
                }
            }
        }
    }
}
```

## Dimensions

Thedimensionsstyle property lets you define the minimum height for a block or element:

PropertyTypeCSS Property`dimensions.minHeight`string, object[min-height](https://developer.mozilla.org/en-US/docs/Web/CSS/min-height)
Example usage intheme.json:

```json
{
    "version": 2,
    "styles": {
        "blocks": {
            "core/cover": {
                "dimensions": {
                    "minHeight": "50vh"
                }
            }
        }
    }
}
```

## Filter

Thefilterstyle property lets you define filters for a block or element. Currently, you can set a default duotone filter:

PropertyTypeCSS Property`filter.duotone`string, object[filter](https://developer.mozilla.org/en-US/docs/Web/CSS/filter)
Example usage intheme.json:

```json
{
    "version": 2,
    "styles": {
        "blocks": {
            "core/image": {
                "filter": {
                    "duotone": "var(--wp--preset--duotone--default-filter)"
                }
            }
        }
    }
}
```

## Shadow

Theshadowstyle property lets you define the default box-shadow style for a block or element:

PropertyTypeCSS Property`shadow`string, object[box-shadow](https://developer.mozilla.org/en-US/docs/Web/CSS/box-shadow)
Example usage intheme.json:

```json
{
    "version": 2,
    "styles": {
        "blocks": {
            "core/heading": {
                "shadow": "0 1px 2px 0 rgb(0 0 0 / 0.05)"
            }
        }
    }
}
```

## Spacing

Thespacingstyle property lets you define the default gap, margin, and padding for a block or element:

PropertyTypeCSS Property`blockGap`string, object[margin-top](https://developer.mozilla.org/en-US/docs/Web/CSS/margin-top), [gap](https://developer.mozilla.org/en-US/docs/Web/CSS/gap)`margin.<side>`string, object[margin-<side>](https://developer.mozilla.org/en-US/docs/Web/CSS/margin)`padding.<side>`string, object[padding-<side>](https://developer.mozilla.org/en-US/docs/Web/CSS/padding)
You can define any or all of the sides (top,right,bottom,left) for themarginandpaddingstyle properties.

Example usage intheme.json:

```json
{
    "version": 2,
    "styles": {
        "spacing": {
            "blockGap": "2rem",
            "margin": {
                "top": "2rem",
                "bottom": "2rem"
            },
            "padding": {
                "left": "2rem",
                "right": "2rem"
            }
        }
    }
}
```

## Typography

Thetypographystyle property lets you define default font and text-related styles for a block or element:

PropertyTypeCSS Property`fontFamily`string, object[font-family](https://developer.mozilla.org/en-US/docs/Web/CSS/font-family)`fontSize`string, object[font-size](https://developer.mozilla.org/en-US/docs/Web/CSS/font-size)`fontStyle`string, object[font-style](https://developer.mozilla.org/en-US/docs/Web/CSS/font-style)`fontWeight`string, object[font-weight](https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight)`letterSpacing`string, object[letter-spacing](https://developer.mozilla.org/en-US/docs/Web/CSS/letter-spacing)`lineHeight`string, object[line-height](https://developer.mozilla.org/en-US/docs/Web/CSS/line-height)`textColumns`string[columns](https://developer.mozilla.org/en-US/docs/Web/CSS/columns)`textDecoration`string, object[text-decoration](https://developer.mozilla.org/en-US/docs/Web/CSS/text-decoration)`writingMode`string, object[writing-mode](https://developer.mozilla.org/en-US/docs/Web/CSS/writing-mode)
Example usage intheme.json:

```json
{
    "version": 2,
    "styles": {
        "blocks": {
            "core/paragraph": {
                "typography": {
                    "fontFamily": "Georgia, serif",
                    "fontSize": "1.25rem",
                    "fontStyle": "normal",
                    "fontWeight": "500",
                    "letterSpacing": "0",
                    "lineHeight": "1.6",
                    "textDecoration": "none"
                }
            }
        }
    }
}
```

## CSS

Thecssproperty lets you write custom CSS directly intheme.jsonfor a block or element:

PropertyTypeCSS Property`css`string—
Example usage intheme.json:

```json
{
    "version": 2,
    "styles": {
        "blocks": {
            "core/gallery": {
                "css": "--wp--style--gallery-gap-default: 1rem;"
            }
        }
    }
}
```

For an in-depth look at how to use thecssstyle property, readPer-block CSS withtheme.jsonon the WordPress Developer Blog.

First published

October 17, 2023

Last updated

December 14, 2023

[PreviousUsing PresetsPrevious: Using Presets](https://developer.wordpress.org/themes/global-settings-and-styles/styles/using-presets/)
[NextCustom TemplatesNext: Custom Templates](https://developer.wordpress.org/themes/global-settings-and-styles/custom-templates/)
