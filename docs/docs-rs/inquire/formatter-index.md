inquire
# Module formatter 
Source 
## Constants§
DEFAULT_BOOL_FORMATTERString formatter used by default in Confirm prompts.
Translates `bool` to `"Yes"` and `false` to `"No"`.DEFAULT_DATE_FORMATTER`date`String formatter used by default in `DateSelect` prompts.
Prints the selected date in the format: Month Day, Year.DEFAULT_STRING_FORMATTERString formatter used by default in inputs that return a `String` as input.
Its behavior is to just echo the received input.
## Type Aliases§
BoolFormatterType alias for formatters used in Confirm prompts.CustomTypeFormatterType alias for formatters used in `CustomType` prompts.DateFormatter`date`Type alias for formatters used in `DateSelect` prompts.MultiOptionFormatterType alias for formatters used in `MultiSelect` prompts.OptionFormatterType alias for formatters used in Select prompts.StringFormatterType alias for formatters that receive a string slice as the input,
required by Text and Password for example.