inquire
# Struct CustomType 
Source 

```
pub struct CustomType<'a, T> {
    pub message: &'a str,
    pub starting_input: Option<&'a str>,
    pub default: Option<T>,
    pub placeholder: Option<&'a str>,
    pub help_message: Option<&'a str>,
    pub formatter: CustomTypeFormatter<'a, T>,
    pub default_value_formatter: CustomTypeFormatter<'a, T>,
    pub parser: CustomTypeParser<'a, T>,
    pub validators: Vec<Box<dyn CustomTypeValidator<T>>>,
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
§`default: Option<T>`

Default value, returned when the user input is empty.
§`placeholder: Option<&'a str>`

Short hint that describes the expected value of the input.
§`help_message: Option<&'a str>`

Help message to be presented to the user.
§`formatter: CustomTypeFormatter<'a, T>`

Function that formats the user input and presents it to the user as the final rendering of the prompt.
§`default_value_formatter: CustomTypeFormatter<'a, T>`

Function that formats the provided value. Useful for example when you want to format a default `true` to the string “Y/n”, common in confirmation prompts.
§`parser: CustomTypeParser<'a, T>`

Function that parses the user input and returns the result value.
§`validators: Vec<Box<dyn CustomTypeValidator<T>>>`

Collection of validators to apply to the user input.

Validators are executed in the order they are stored, stopping at and displaying to the user
only the first validation error that might appear.

The possible error is displayed to the user one line above the prompt.
§`error_message: String`

Error message displayed when value could not be parsed from input.
§`render_config: RenderConfig<'a>`

RenderConfig to apply to the rendered interface.

Note: The default render config considers if the NO_COLOR environment variable
is set to decide whether to render the colored config or the empty one.

When overriding the config in a prompt, NO_COLOR is no longer considered and your
config is treated as the only source of truth. If you want to customize colors
and still support NO_COLOR, you will have to do this on your end.

## Implementations§