# Crate validator 
Source 
## Structs§
ValidationErrorValidationErrors
## Enums§
ValidationErrorsKind
## Traits§
AsRegexValidateThis is the original trait that was implemented by deriving `Validate`. It will still be
implemented for struct validations that don’t take custom arguments. The call is being
forwarded to the `ValidateArgs<'v_a>` trait.ValidateArgsThis trait will be implemented by deriving `Validate`. This implementation can take one
argument and pass this on to custom validators. The default `Args` type will be `()` if
there is no custom validation with defined arguments.ValidateContainsValidateDoesNotContainValidateEmailValidates whether the given string is an email based on the HTML5 spec.
RFC 5322 is not practical in most circumstances and allows email addresses
that are unfamiliar to most users.ValidateIpValidateLengthValidates the length of the value given.
If the validator has `equal` set, it will ignore any `min` and `max` value.ValidateRangeValidates that the given `value` is inside the defined range.
The `max`, `min`, `exclusive_max` and `exclusive_min` parameters are
optional and will only be validated if they are not `None`ValidateRegexValidateRequiredValidates whether the given Option is SomeValidateUrlValidates whether the string given is a url
## Functions§
validate_must_matchValidates that the 2 given fields match.
Both fields are optionals