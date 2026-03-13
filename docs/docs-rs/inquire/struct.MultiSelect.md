inquire
# Struct MultiSelect 
Source 

```
pub struct MultiSelect<'a, T> {}
```

## Fields§
§`message: &'a str`

Message to be presented to the user.
§`options: Vec<T>`

Options displayed to the user.
§`default: Option<Vec<usize>>`

Default indexes of options to be selected from the start.
§`help_message: Option<&'a str>`

Help message to be presented to the user.
§`page_size: usize`

Page size of the options displayed to the user.
§`vim_mode: bool`

Whether vim mode is enabled. When enabled, the user can
navigate through the options using hjkl.
§`starting_cursor: usize`

Starting cursor index of the selection.
§`starting_filter_input: Option<&'a str>`

Starting filter input
§`reset_cursor: bool`

Reset cursor position to first option on filter input change.
Defaults to true.
§`filter_input_enabled: bool`

Whether to allow the option list to be filtered by user input or not.

Defaults to true.
§`scorer: Scorer<'a, T>`

Function called with the current user input to score the provided
options.
The list of options is sorted in descending order (highest score first)
§`keep_filter: bool`

Whether the current filter typed by the user is kept or cleaned after a selection is made.
§`formatter: MultiOptionFormatter<'a, T>`

Function that formats the user input and presents it to the user as the final rendering of the prompt.
§`validator: Option<Box<dyn MultiOptionValidator<T>>>`

Validator to apply to the user input.

In case of error, the message is displayed one line above the prompt.
§`render_config: RenderConfig<'a>`

RenderConfig to apply to the rendered interface.

Note: The default render config considers if the NO_COLOR environment variable
is set to decide whether to render the colored config or the empty one.

When overriding the config in a prompt, NO_COLOR is no longer considered and your
config is treated as the only source of truth. If you want to customize colors
and still support NO_COLOR, you will have to do this on your end.

## Implementations§