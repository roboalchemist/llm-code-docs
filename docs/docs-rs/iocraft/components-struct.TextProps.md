iocraft::components
# Struct TextProps 
Source 

```
#[non_exhaustive]pub struct TextProps {
    pub color: Option<Color>,
    pub content: String,
    pub weight: Weight,
    pub wrap: TextWrap,
    pub align: TextAlign,
    pub decoration: TextDecoration,
    pub italic: bool,
}
```

## Fields (Non-exhaustive)§
§`color: Option<Color>`

The color to make the text.
§`content: String`

The content of the text.
§`weight: Weight`

The weight of the text.
§`wrap: TextWrap`

The text wrapping behavior.
§`align: TextAlign`

The text alignment.
§`decoration: TextDecoration`

The text decoration.
§`italic: bool`

Whether to italicize the text.

## Trait Implementations§