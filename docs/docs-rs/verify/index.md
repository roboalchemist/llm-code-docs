# Crate verify 
Source 
## Modules§
schemars`schemars`Implementations for Schemars Schema types.serde`serde`This module contains tools to make Serde Serializable values being able to be validated.spanThis module contains Span-related definitions and common Span types.
## Traits§
ErrorThe errors returned by validators must implement this trait.ErrorExtConvenience trait for interacting with errors.ValidateValidate is implemented by values that can be validate themselves
against a given validator.ValidateMapType returned by validate_map.ValidateSeqType returned by validate_seq.ValidatorValues that implement Validate can validate themselves against
types that implement this trait.VerifierThis trait is implemented by types that validate a value internally.VerifyThis trait is implemented by types that can validate themselves.
## Derive Macros§
VerifyMacro for deriving Verify.