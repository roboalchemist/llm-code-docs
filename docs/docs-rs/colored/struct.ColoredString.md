colored
# Struct ColoredString 
Source 

```
#[non_exhaustive]pub struct ColoredString {
    pub input: String,
    pub fgcolor: Option<Color>,
    pub bgcolor: Option<Color>,
    pub style: Style,
}
```

## Fields (Non-exhaustive)§
§`input: String`

The plain text that will have color and style applied to it.
§`fgcolor: Option<Color>`

The color of the text as it will be printed.
§`bgcolor: Option<Color>`

The background color (if any). None means that the text will be printed
without a special background.
§`style: Style`

Any special styling to be applied to the text (see Styles for a list of
available options).

## Implementations§