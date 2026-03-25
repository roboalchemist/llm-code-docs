inquire
# Module validator 
Source 
## Structs§
ExactLengthValidatorBuilt-in validator that checks whether the answer length is equal to
the specified value.MaxLengthValidatorBuilt-in validator that checks whether the answer length is smaller than
or equal to the specified threshold.MinLengthValidatorBuilt-in validator that checks whether the answer length is larger than
or equal to the specified threshold.ValueRequiredValidatorBuilt-in validator that checks whether the answer is not empty.
## Enums§
ErrorMessageError message that is displayed to the users when their input is considered not
valid by registered validators.ValidationThe result type of validation operations when the execution of the validator
function succeeds.
## Traits§
CustomTypeValidatorValidator used in `CustomType` prompts.DateValidator`date`Validator used in `DateSelect` prompts.InquireLengthCustom trait to call correct method to retrieve input length.MultiOptionValidatorValidator used in `MultiSelect` prompts.StringValidatorValidator that receives a string slice as the input, such as `Text` and
`Password`.