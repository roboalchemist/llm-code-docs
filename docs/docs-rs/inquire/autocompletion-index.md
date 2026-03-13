inquire
# Module autocompletion 
Source 
## Structs§
NoAutoCompletionEmpty struct and implementation of Autocomplete trait. Used for the default
autocompleter of `Text` prompts.
## Traits§
AutocompleteMechanism to implement autocompletion features for text inputs. The `Autocomplete` trait has two provided methods: `get_suggestions` and `get_completion`.
## Type Aliases§
ReplacementUsed when an autocompletion is triggered for the user’s text input.