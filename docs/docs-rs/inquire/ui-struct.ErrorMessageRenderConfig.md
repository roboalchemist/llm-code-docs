inquire::ui
# Struct ErrorMessageRenderConfig 
Source 

```
pub struct ErrorMessageRenderConfig<'a> {
    pub prefix: Styled<&'a str>,
    pub separator: StyleSheet,
    pub message: StyleSheet,
    pub default_message: &'a str,
}
```

## Fields§
§`prefix: Styled<&'a str>`

Prefix style.
§`separator: StyleSheet`

Separator style.

Note: This separator is a space character. It might be useful to
style it if you want to set a background color for error messages.
§`message: StyleSheet`

Message style.
§`default_message: &'a str`

Default message used for validators that do not defined custom error messages.

## Implementations§