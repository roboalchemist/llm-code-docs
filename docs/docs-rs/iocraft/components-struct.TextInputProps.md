iocraft::components
# Struct TextInputProps 
Source 

```
#[non_exhaustive]pub struct TextInputProps {
    pub color: Option<Color>,
    pub value: String,
    pub has_focus: bool,
    pub on_change: HandlerMut<'static, String>,
    pub multiline: bool,
    pub cursor_color: Option<Color>,
    pub handle: Option<Ref<TextInputHandle>>,
}
```

## Fields (Non-exhaustive)§
§`color: Option<Color>`

The color to make the text.
§`value: String`

The current value.
§`has_focus: bool`

True if the input has focus and should process keyboard input.
§`on_change: HandlerMut<'static, String>`

The handler to invoke when the value changes.
§`multiline: bool`

If true, the input will fill 100% of the height of its container and handle multiline input.
§`cursor_color: Option<Color>`

The color to make the cursor. Defaults to gray.
§`handle: Option<Ref<TextInputHandle>>`

An optional handle which can be used for imperative control of the input.

## Trait Implementations§