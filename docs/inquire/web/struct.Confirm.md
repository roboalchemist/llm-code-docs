inquire
# Struct Confirm 
Source 

```
pub struct Confirm<'a> {
    pub message: &'a str,
    pub starting_input: Option<&'a str>,
    pub default: Option<bool>,
    pub placeholder: Option<&'a str>,
    pub help_message: Option<&'a str>,
    pub formatter: BoolFormatter<'a>,
    pub parser: BoolParser<'a>,
    pub default_value_formatter: BoolFormatter<'a>,
    pub error_message: String,
    pub render_config: RenderConfig<'a>,
}
```

## Fields§
§`message: &'a str`

Message to be presented to the user.
§`starting_input: Option<&'a str>`

Initial value of the prompt’s text input.

If you want to set a default value for the prompt, returned when the user’s submission is empty, see `default`.
§`default: Option<bool>`

Default value, returned when the user input is empty.
§`placeholder: Option<&'a str>`

Short hint that describes the expected value of the input.
§`help_message: Option<&'a str>`

Help message to be presented to the user.
§`formatter: BoolFormatter<'a>`

Function that formats the user input and presents it to the user as the final rendering of the prompt.
§`parser: BoolParser<'a>`

Function that parses the user input and returns the result value.
§`default_value_formatter: BoolFormatter<'a>`

Function that formats the default value to be presented to the user
§`error_message: String`

Error message displayed when a value could not be parsed from input.
§`render_config: RenderConfig<'a>`

RenderConfig to apply to the rendered interface.

Note: The default render config considers if the NO_COLOR environment variable
is set to decide whether to render the colored config or the empty one.

When overriding the config in a prompt, NO_COLOR is no longer considered and your
config is treated as the only source of truth. If you want to customize colors
and still support NO_COLOR, you will have to do this on your end.

## Implementations§