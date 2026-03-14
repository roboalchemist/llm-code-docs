bat::theme
# Struct ThemeOptions 
Source 

```
pub struct ThemeOptions {
    pub theme: ThemePreference,
    pub theme_dark: Option<ThemeName>,
    pub theme_light: Option<ThemeName>,
}
```

## Fields§
§`theme: ThemePreference`

Configures how the theme is chosen. If set to a `ThemePreference::Fixed` value,
then the given theme is used regardless of the terminal’s background color.
This corresponds with the `BAT_THEME` environment variable and the `--theme` option.
§`theme_dark: Option<ThemeName>`

The theme to use in case the terminal uses a dark background with light text.
This corresponds with the `BAT_THEME_DARK` environment variable and the `--theme-dark` option.
§`theme_light: Option<ThemeName>`

The theme to use in case the terminal uses a light background with dark text.
This corresponds with the `BAT_THEME_LIGHT` environment variable and the `--theme-light` option.

## Trait Implementations§