inquire
# Struct Text 
Source 

```
pub struct Text<'a, 'b> {
    pub message: &'a str,
    pub initial_value: Option<&'a str>,
    pub default: Option<&'a str>,
    pub placeholder: Option<&'a str>,
    pub help_message: Option<&'a str>,
    pub formatter: StringFormatter<'a>,
    pub autocompleter: Option<Box<dyn Autocomplete + 'b>>,
    pub validators: Vec<Box<dyn StringValidator + 'b>>,
    pub page_size: usize,
    pub render_config: RenderConfig<'a>,
}
```

## Fields§
§`message: &'a str`

Message to be presented to the user.
§`initial_value: Option<&'a str>`

Initial value of the prompt’s text input.

If you want to set a default value for the prompt, returned when the user’s submission is empty, see `default`.
§`default: Option<&'a str>`

Default value, returned when the user input is empty.
§`placeholder: Option<&'a str>`

Short hint that describes the expected value of the input.
§`help_message: Option<&'a str>`

Help message to be presented to the user.
§`formatter: StringFormatter<'a>`

Function that formats the user input and presents it to the user as the final rendering of the prompt.
§`autocompleter: Option<Box<dyn Autocomplete + 'b>>`

Autocompleter responsible for handling suggestions and input completions.
§`validators: Vec<Box<dyn StringValidator + 'b>>`

Collection of validators to apply to the user input.

Validators are executed in the order they are stored, stopping at and displaying to the user
only the first validation error that might appear.

The possible error is displayed to the user one line above the prompt.
§`page_size: usize`

Page size of the suggestions displayed to the user, when applicable.
§`render_config: RenderConfig<'a>`

RenderConfig to apply to the rendered interface.

Note: The default render config considers if the NO_COLOR environment variable
is set to decide whether to render the colored config or the empty one.

When overriding the config in a prompt, NO_COLOR is no longer considered and your
config is treated as the only source of truth. If you want to customize colors
and still support NO_COLOR, you will have to do this on your end.

## Implementations§