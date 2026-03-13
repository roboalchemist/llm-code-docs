bat
# Module theme 
Source 
## Modules§
envEnvironment variable names.
## Structs§
ThemeOptionsOptions for configuring the theme used for syntax highlighting.
Used together with `theme`.ThemeResultThe resolved theme and the color scheme as determined from
the terminal, OS or fallback.
## Enums§
ColorSchemeThe color scheme used to pick a fitting theme. Defaults to `ColorScheme::Dark`.DetectColorSchemeThemeNameThe name of a theme or the default theme.ThemePreferenceWhat theme should `bat` use?
## Functions§
color_schemeDetects the color scheme from the terminal.default_themeThe default theme, suitable for the given color scheme.
Use `theme` if you want to automatically detect the color scheme from the terminal.themeChooses an appropriate theme or falls back to a default theme
based on the user-provided options and the color scheme of the terminal.