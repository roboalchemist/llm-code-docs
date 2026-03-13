inquire::ui
# Struct RenderConfig 
Source 

```
pub struct RenderConfig<'a> {}
```

## Fields§
§`new_line_prefix: Option<Styled<&'a str>>`

Prefix added at the beginning of a new line.
§`prompt_prefix: Styled<&'a str>`

Prefix added before prompts.

Note: a space character will be added to separate the prefix
and the prompt message.
§`answered_prompt_prefix: Styled<&'a str>`

Prefix added before answered prompts.

Note: a space character will be added to separate the prefix
and the prompt message.
§`prompt: StyleSheet`

Style of the prompt message, applicable to all prompt types.
§`default_value: StyleSheet`

Render configuration of default values.

Note: default values are displayed wrapped in parenthesis, e.g. (yes).
Non-styled space characters is added before the default value display
and after the default value, as separators.
§`placeholder: StyleSheet`

Render configuration of placeholders.

Note: placeholders are displayed wrapped in parenthesis, e.g. (yes).
Non-styled space characters is added before the default value display
and after the default value, as separators.
§`help_message: StyleSheet`

Render configuration of help messages.

Note: help messages are displayed wrapped in brackets, e.g. [Be careful!].
§`password_mask: char`

Character used to mask password text inputs when in mode
`Masked`.

Note: Styles for masked text inputs are set in the
`text_input` configuration.
§`text_input: StyleSheet`

Style sheet for text inputs.

Note: a non-styled space character is added before the text input as
a separator from the prompt message (or default value display).
§`answer: StyleSheet`

Render configuration of final prompt answers (submissions).

Note: a non-styled space character is added before the answer as
a separator from the prompt message (or default value display).
§`answer_from_new_line: bool`

If you want to print the answer on a new line, set the value to “true”.
The default value is “false”.
§`canceled_prompt_indicator: Styled<&'a str>`

Render configuration of the message printed in the place of an answer
when the prompt is canceled by the user - by pressing ESC.

Note: a non-styled space character is added before the indicator as
a separator from the prompt message.
§`error_message: ErrorMessageRenderConfig<'a>`

Render configuration for error messages.
§`highlighted_option_prefix: Styled<&'a str>`

Prefix for the current highlighted option.

Note: a space character will be added to separate the prefix
and the option value or the checkbox.
§`unhighlighted_option_prefix: Styled<&'a str>`

Prefix for an unhighlighted option.

Note: a space character will be added to separate the prefix
and the option value.
§`scroll_up_prefix: Styled<&'a str>`

Prefix for the option listed at the top of the page, when it is possible
to scroll up.

Note: a space character will be added to separate the prefix
and the option value or the checkbox.
§`scroll_down_prefix: Styled<&'a str>`

Prefix for the option listed at the bottom of the page, when it is possible
to scroll down.

Note: a space character will be added to separate the prefix
and the option value or the checkbox.
§`selected_checkbox: Styled<&'a str>`

Selected checkbox in multi-select options.

Note: a space character will be added to separate the checkbox
from a possible prefix, and to separate the checkbox from the
option value to the right.
§`unselected_checkbox: Styled<&'a str>`

Unselected checkbox in multi-select options.

Note: a space character will be added to separate the checkbox
from a possible prefix, and to separate the checkbox from the
option value to the right.
§`option_index_prefix: IndexPrefix`

Definition of index prefixes in option lists.
§`option: StyleSheet`

Style sheet for options.

Note: a non-styled space character is added before the option value as
a separator from the prefix.
§`selected_option: Option<StyleSheet>`

Style sheet for the option that is currently selected. If the value is
None, it will fall back to `option`.

Note: a non-styled space character is added before the option value as
a separator from the prefix.
§`calendar: CalendarRenderConfig<'a>`Available on **crate feature `date`** only.

Render configuration for calendar
Render configuration for date prompts`
§`editor_prompt: StyleSheet`Available on **crate feature `editor`** only.

Style sheet of the hint in editor prompts.

The hint is formatted as `[(e) to open {}, (enter) to submit]`
with the editor name.

## Implementations§