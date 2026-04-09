bat::theme
# Struct ThemeResult 
Source 

```
pub struct ThemeResult {
    pub theme: ThemeName,
    pub color_scheme: Option<ColorScheme>,
}
```

## Fields§
§`theme: ThemeName`

The theme selected according to the `ThemeOptions`.
§`color_scheme: Option<ColorScheme>`

Either the user’s chosen color scheme, the terminal’s color scheme, the OS’s
color scheme or `None` if the color scheme was not detected because the user chose a fixed theme.

## Trait Implementations§