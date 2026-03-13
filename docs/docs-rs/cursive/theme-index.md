cursive
# Module theme 
Source 
## Structs§
ColorPairCombines a front and back color.ColorStylePossible color style for a cell.ConcreteStyleCombine a concrete color and effects.EffectsA set of effects status.NoSuchColorError parsing a color.PaletteColor configuration for the application.StyleCombine a color and effects.ThemeRepresents the style a Cursive application will use.
## Enums§
BaseColorOne of the 8 base colors.BorderStyleSpecifies how some borders should be drawn.ColorRepresents a color used by the theme.ColorTypeEither a color from the palette, or a direct color.EffectText effectEffectStatusDescribes what to do with an effect.ErrorPossible error returned when loading a theme.PaletteColorColor entry in a palette.PaletteNodeA node in the palette tree.PaletteStyleStyle entry in a palette.StyleTypeType of style to apply to some text.
## Functions§
load_defaultLoads the default theme, and returns its representation.load_theme_file`toml`Loads a theme from file.load_toml`toml`Loads a theme string and sets it as active.
## Type Aliases§
ConcreteEffectsA concrete set of effects to enable.