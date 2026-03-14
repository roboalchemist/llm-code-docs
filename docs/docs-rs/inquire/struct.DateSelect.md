inquire
# Struct DateSelect 
Source 

```
pub struct DateSelect<'a> {
    pub message: &'a str,
    pub week_start: Weekday,
    pub starting_date: NaiveDate,
    pub min_date: Option<NaiveDate>,
    pub max_date: Option<NaiveDate>,
    pub help_message: Option<&'a str>,
    pub formatter: DateFormatter<'a>,
    pub validators: Vec<Box<dyn DateValidator>>,
    pub render_config: RenderConfig<'a>,
}
```
Available on **crate feature `date`** only.
## Fields§
§`message: &'a str`

Message to be presented to the user.
§`week_start: Weekday`

First day of the week when displaying week rows.
§`starting_date: NaiveDate`

Starting date to be selected.
§`min_date: Option<NaiveDate>`

Min date allowed to be selected.
§`max_date: Option<NaiveDate>`

Max date allowed to be selected.
§`help_message: Option<&'a str>`

Help message to be presented to the user.
§`formatter: DateFormatter<'a>`

Function that formats the user input and presents it to the user as the final rendering of the prompt.
§`validators: Vec<Box<dyn DateValidator>>`

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