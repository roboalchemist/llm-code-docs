proptest
# Module result 
Source 
## Re-exports§
`pub use crate::option::prob;``pub use crate::option::Probability;`
## Structs§
MaybeErrStrategy which generates `Result`s using `Ok` and `Err` values from two
delegate strategies.MaybeErrValueTree`ValueTree` type corresponding to `MaybeErr`.MaybeOkStrategy which generates `Result`s using `Ok` and `Err` values from two
delegate strategies.MaybeOkValueTree`ValueTree` type corresponding to `MaybeOk`.
## Functions§
maybe_errCreate a strategy for `Result`s where `Ok` values are taken from `t` and
`Err` values are taken from `e`.maybe_err_weightedCreate a strategy for `Result`s where `Ok` values are taken from `t` and
`Err` values are taken from `e`.maybe_okCreate a strategy for `Result`s where `Ok` values are taken from `t` and
`Err` values are taken from `e`.maybe_ok_weightedCreate a strategy for `Result`s where `Ok` values are taken from `t` and
`Err` values are taken from `e`.