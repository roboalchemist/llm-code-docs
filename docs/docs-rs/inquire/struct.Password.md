inquire
# Struct Password 
Source 

```
pub struct Password<'a> {
    pub message: &'a str,
    pub custom_confirmation_message: Option<&'a str>,
    pub custom_confirmation_error_message: Option<&'a str>,
    pub help_message: Option<&'a str>,
    pub formatter: StringFormatter<'a>,
    pub display_mode: PasswordDisplayMode,
    pub enable_display_toggle: bool,
    pub enable_confirmation: bool,
    pub validators: Vec<Box<dyn StringValidator>>,
    pub render_config: RenderConfig<'a>,
}
```

## Fields§
§`message: &'a str`

Message to be presented to the user.
§`custom_confirmation_message: Option<&'a str>`

Message to be presented to the user when confirming the input.
§`custom_confirmation_error_message: Option<&'a str>`

Error to be presented to the user when password confirmation fails.
§`help_message: Option<&'a str>`

Help message to be presented to the user.
§`formatter: StringFormatter<'a>`

Function that formats the user input and presents it to the user as the final rendering of the prompt.
§`display_mode: PasswordDisplayMode`

How the password input is displayed to the user.
§`enable_display_toggle: bool`

Whether to allow the user to toggle the display of the current password input by pressing the Ctrl+R hotkey.
§`enable_confirmation: bool`

Whether to ask for input twice to see if the provided passwords are the same.
§`validators: Vec<Box<dyn StringValidator>>`

Collection of validators to apply to the user input.

Validators are executed in the order they are stored, stopping at and displaying to the user
only the first validation error that might appear.

The possible error is displayed to the user one line above the prompt.
§`render_config: RenderConfig<'a>`

RenderConfig to apply to the rendered interface.

Note: The default render config considers if the NO_COLOR environment variable
is set to decide whether to render the colored config or the empty one.

When overriding the config in a prompt, NO_COLOR is no longer considered and your
config is treated as the only source of truth. If you want to customize colors
and still support NO_COLOR, you will have to do this on your end.

## Implementations§