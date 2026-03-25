iced
# Struct Settings 
Source 

```
pub struct Settings {
    pub id: Option<String>,
    pub fonts: Vec<Cow<'static, [u8]>>,
    pub default_font: Font,
    pub default_text_size: Pixels,
    pub antialiasing: bool,
    pub vsync: bool,
}
```

## Fields§
§`id: Option<String>`

The identifier of the application.

If provided, this identifier may be used to identify the application or
communicate with it through the windowing system.
§`fonts: Vec<Cow<'static, [u8]>>`

The fonts to load on boot.
§`default_font: Font`

The default `Font` to be used.

By default, it uses `Family::SansSerif`.
§`default_text_size: Pixels`

The text size that will be used by default.

The default value is `16.0`.
§`antialiasing: bool`

If set to true, the renderer will try to perform antialiasing for some
primitives.

Enabling it can produce a smoother result in some widgets, like the
`canvas` widget, at a performance cost.

By default, it is enabled.
§`vsync: bool`

Whether or not to attempt to synchronize rendering when possible.

Disabling it can improve rendering performance on some platforms.

By default, it is enabled.

## Trait Implementations§