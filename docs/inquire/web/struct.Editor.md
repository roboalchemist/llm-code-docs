inquire
# Struct Editor 
Source 

```
pub struct Editor<'a> {
    pub message: &'a str,
    pub editor_command: &'a OsStr,
    pub editor_command_args: &'a [&'a OsStr],
    pub file_extension: &'a str,
    pub predefined_text: Option<&'a str>,
    pub help_message: Option<&'a str>,
    pub formatter: StringFormatter<'a>,
    pub validators: Vec<Box<dyn StringValidator>>,
    pub render_config: RenderConfig<'a>,
}
```
Available on **crate feature `editor`** only.
## Fields§
§`message: &'a str`

Message to be presented to the user.
§`editor_command: &'a OsStr`

Command to open the editor.
§`editor_command_args: &'a [&'a OsStr]`

Args to pass to the editor.
§`file_extension: &'a str`

Extension of the file opened in the text editor, useful for syntax highlighting.

The dot prefix should be included in the string, e.g. “.rs”.
§`predefined_text: Option<&'a str>`

Predefined text to be present on the text file on the text editor.
§`help_message: Option<&'a str>`

Help message to be presented to the user.
§`formatter: StringFormatter<'a>`

Function that formats the user input and presents it to the user as the final rendering of the prompt.
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