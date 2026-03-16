# Crate proptest 
Source 
## Modules§
arbitraryDefines the `Arbitrary` trait and related free functions
and type aliases.arraySupport for strategies producing fixed-length arrays.bitsStrategies for working with bit sets.boolStrategies for generating `bool` values.charStrategies for generating `char` values.collectionStrategies for generating `std::collections` of values.numStrategies to generate numeric values (as opposed to integers used as bit
fields).optionStrategies for generating `std::Option` values.path`std`Strategies for generating [`PathBuf`] and related path types.preludeRe-exports the most commonly-needed APIs of proptest.range_subset`std`Strategies for generating values by taking samples of index ranges.resultStrategies for combining delegate strategies into `std::Result`s.sampleStrategies for generating values by taking samples of collections.strategyDefines the core traits used by Proptest.string`std`Strategies for generating strings and byte strings from regular
expressions.test_runnerState and functions for running proptest tests.tupleSupport for combining strategies into tuples.
## Macros§
prop_assertSimilar to `assert!` from std, but returns a test failure instead of
panicking if the condition fails.prop_assert_eqSimilar to `assert_eq!` from std, but returns a test failure instead of
panicking if the condition fails.prop_assert_neSimilar to `assert_ne!` from std, but returns a test failure instead of
panicking if the condition fails.prop_assumeRejects the test input if assumptions are not met.prop_composeConvenience to define functions which produce new strategies.prop_oneofProduce a strategy which picks one of the listed choices.proptestEasily define `proptest` tests.
## Attribute Macros§
property_test`attr-macro`The `property_test` procedural macro simplifies the creation of property-based tests
using the `proptest` crate. This macro provides a more concise syntax for writing tests
that automatically generate test cases based on properties.