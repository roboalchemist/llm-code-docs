# Crate inquire 
Source 
## Re-exports§
`pub use crate::autocompletion::Autocomplete;``pub use crate::error::CustomUserError;``pub use crate::error::InquireError;`
## Modules§
autocompletionTrait and structs used by prompts to provide autocompletion features.errorDefinitions of `inquire`’s error handlingformatterType aliases and default implementations for functions called as formatters
of a given input.list_optionUtilities used to wrap user selections in Select and
`MultiSelect` prompts.parserType aliases and default implementations for parsers called in prompts
that need to parse user input, such as Confirm or
`CustomType`.type_aliasesGeneral type aliases.uiUI-related definitions for rendered content.validatorTraits and structs used by prompts to validate user input before
returning the values to their callers.
## Macros§
length`macros`Shorthand for the built-in `ExactLengthValidator` that checks whether the answer length is
equal to the specified value.max_length`macros`Shorthand for the built-in `MaxLengthValidator` that checks whether the answer length is
smaller than or equal to the specified threshold.min_length`macros`Shorthand for the built-in `MinLengthValidator` that checks whether the answer length is
larger than or equal to the specified threshold.parse_type`macros`Built-in parser creator that checks whether the answer is able to be successfully
parsed to a given type, such as `f64`.
The given type must implement the FromStr trait.required`macros`Shorthand for the built-in `ValueRequiredValidator` that checks whether the answer is not
empty.
## Structs§
ConfirmPrompt to ask the user for simple yes/no questions, commonly known by asking the user displaying the `(y/n)` text.CustomTypeGeneric prompt suitable for when you need to parse the user input into a specific type, for example an `f64` or a `rust_decimal`, maybe even an `uuid`.DateSelect`date`Prompt that allows user to select a date (time not supported) from an interactive calendar. Available via the `date` feature.Editor`editor`This prompt is meant for cases where you need the user to write some text that might not fit in a single line, such as long descriptions or commit messages.MultiSelectPrompt suitable for when you need the user to select many options (including none if applicable) among a list of them.PasswordPrompt meant for secretive text inputs.SelectPrompt suitable for when you need the user to select one option among many.TextStandard text prompt that returns the user string input.
## Enums§
ActionTop-level type to describe the directives a prompt
receives.CustomTypePromptActionSet of actions for a CustomTypePrompt.DateSelectPromptActionSet of actions for a DateSelectPrompt.EditorPromptActionSet of actions for an EditorPrompt.InputActionSet of actions for a text input handler.MultiSelectPromptActionSet of actions for a MultiSelectPrompt.PasswordDisplayModeDisplay modes of the text input of a password prompt.PasswordPromptActionSet of actions for a PasswordPrompt.SelectPromptActionSet of actions for a SelectPrompt.TextPromptActionSet of actions for a TextPrompt.
## Traits§
InnerActionInnerActions are specialized prompt actions.
## Functions§
prompt_confirmation`one-liners`This function is a helpful one-liner to prompt the user for the confirmation of an action.prompt_date`one-liners` and `date`This function is a helpful one-liner to prompt the user for a date.prompt_f32`one-liners`This function is a helpful one-liner to prompt the user for a number and parse it to f32.prompt_f64`one-liners`This function is a helpful one-liner to prompt the user for a number and parse it to f64.prompt_secret`one-liners`This function is a helpful one-liner to prompt the user for a password, or any secret text.prompt_text`one-liners`This function is a helpful one-liner to prompt the user for a text input.prompt_u32`one-liners`This function is a helpful one-liner to prompt the user for a number and parse it to u32.prompt_u64`one-liners`This function is a helpful one-liner to prompt the user for a number and parse it to u64.prompt_u128`one-liners`This function is a helpful one-liner to prompt the user for a number and parse it to u128.prompt_usize`one-liners`This function is a helpful one-liner to prompt the user for a number and parse it to usize.set_global_render_configAcquires a write lock to the global RenderConfig object
and updates the inner value with the provided argument.
## Type Aliases§
ConfirmPromptActionSet of actions for a ConfirmPrompt.