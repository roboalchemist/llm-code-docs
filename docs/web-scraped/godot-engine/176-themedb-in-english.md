# ThemeDB in English

# ThemeDB
Inherits:Object
A singleton that provides access to static information aboutThemeresources used by the engine and by your project.

## Description
This singleton provides access to static information aboutThemeresources used by the engine and by your projects. You can fetch the default engine theme, as well as your project configured theme.
ThemeDBalso contains fallback values for theme properties.

## Properties

| float | fallback_base_scale | 1.0 |
|---|---|---|
| Font | fallback_font |  |
| int | fallback_font_size | 16 |
| Texture2D | fallback_icon |  |
| StyleBox | fallback_stylebox |  |

float
fallback_base_scale
Font
fallback_font
fallback_font_size
Texture2D
fallback_icon
StyleBox
fallback_stylebox

## Methods

| Theme | get_default_theme() |
|---|---|
| Theme | get_project_theme() |

Theme
get_default_theme()
Theme
get_project_theme()

## Signals
fallback_changed()🔗
Emitted when one of the fallback values had been changed. Use it to refresh the look of controls that may rely on the fallback theme items.

## Property Descriptions
floatfallback_base_scale=1.0🔗
- voidset_fallback_base_scale(value:float)
voidset_fallback_base_scale(value:float)
- floatget_fallback_base_scale()
floatget_fallback_base_scale()
The fallback base scale factor of everyControlnode andThemeresource. Used when no other value is available to the control.
See alsoTheme.default_base_scale.
Fontfallback_font🔗
- voidset_fallback_font(value:Font)
voidset_fallback_font(value:Font)
- Fontget_fallback_font()
Fontget_fallback_font()
The fallback font of everyControlnode andThemeresource. Used when no other value is available to the control.
See alsoTheme.default_font.
intfallback_font_size=16🔗
- voidset_fallback_font_size(value:int)
voidset_fallback_font_size(value:int)
- intget_fallback_font_size()
intget_fallback_font_size()
The fallback font size of everyControlnode andThemeresource. Used when no other value is available to the control.
See alsoTheme.default_font_size.
Texture2Dfallback_icon🔗
- voidset_fallback_icon(value:Texture2D)
voidset_fallback_icon(value:Texture2D)
- Texture2Dget_fallback_icon()
Texture2Dget_fallback_icon()
The fallback icon of everyControlnode andThemeresource. Used when no other value is available to the control.
StyleBoxfallback_stylebox🔗
- voidset_fallback_stylebox(value:StyleBox)
voidset_fallback_stylebox(value:StyleBox)
- StyleBoxget_fallback_stylebox()
StyleBoxget_fallback_stylebox()
The fallback stylebox of everyControlnode andThemeresource. Used when no other value is available to the control.

## Method Descriptions
Themeget_default_theme()🔗
Returns a reference to the default engineTheme. This theme resource is responsible for the out-of-the-box look ofControlnodes and cannot be overridden.
Themeget_project_theme()🔗
Returns a reference to the custom projectTheme. This theme resources allows to override the default engine theme for every control node in the project.
To set the project theme, seeProjectSettings.gui/theme/custom.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.