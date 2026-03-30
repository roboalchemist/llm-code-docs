proptest
# Module prelude 
Source 
## Re-exports§
`pub use crate::arbitrary::any;``pub use crate::arbitrary::any_with;``pub use crate::arbitrary::Arbitrary;``pub use crate::strategy::BoxedStrategy;``pub use crate::strategy::Just;``pub use crate::strategy::SBoxedStrategy;``pub use crate::strategy::Strategy;``pub use crate::test_runner::Config as ProptestConfig;``pub use crate::test_runner::TestCaseError;``pub use crate::test_runner::ProptestResultExt;`
## Modules§
propRe-exports the entire public API of proptest so that an import of `prelude`
allows simply writing, for example, `prop::num::i32::ANY` rather than
`proptest::num::i32::ANY` plus a separate `use proptest;`.
## Macros§
prop_assertSimilar to `assert!` from std, but returns a test failure instead of
panicking if the condition fails.prop_assert_eqSimilar to `assert_eq!` from std, but returns a test failure instead of
panicking if the condition fails.prop_assert_neSimilar to `assert_ne!` from std, but returns a test failure instead of
panicking if the condition fails.prop_assumeRejects the test input if assumptions are not met.prop_composeConvenience to define functions which produce new strategies.prop_oneofProduce a strategy which picks one of the listed choices.proptestEasily define `proptest` tests.
## Traits§
RngUser-level interface for RNGsRngCoreImplementation-level interface for RNGs