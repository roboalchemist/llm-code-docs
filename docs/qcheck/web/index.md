# Crate qcheck 
Source 
## Macros§
quickcheckA macro for writing quickcheck tests.
## Structs§
GenGen represents a PRNG.QuickCheckThe main QuickCheck type for setting configuration and running QuickCheck.TestResultDescribes the status of a single instance of a test.
## Traits§
Arbitrary`Arbitrary` describes types whose values can be randomly generated and
shrunk.Testable`Testable` describes types (e.g., a function) whose values can be
tested.
## Functions§
empty_shrinkerCreates a shrinker with zero elements.quickcheckConvenience function for running QuickCheck.single_shrinkerCreates a shrinker with a single element.