proptest
# Module test_runner 
Source 
## Structs§
ConfigConfiguration for how a proptest test should be run.MapFailurePersistenceFailure persistence option that loads and saves seeds in memory
on the heap. This may be useful when accumulating test failures
across multiple `TestRunner` instances for external reporting
or batched persistence.PersistedSeedOpaque struct representing a seed which can be persisted.ReasonThe reason for why something, such as a generated value, was rejected.ResultCacheKeyA key used for the result cache.TestRngProptest’s random number generator.TestRunnerState used when running a proptest test.
## Enums§
FileFailurePersistence`std`Describes how failing test cases are persisted.RngAlgorithmIdentifies a particular RNG algorithm supported by proptest.RngSeedThe seed for the RNG, can either be random or specified as a u64.TestCaseErrorErrors which can be returned from test cases to indicate non-successful
completion.TestErrorA failure state from running test cases for a single test.
## Constants§
INFO_LOGVerbose level 1 to show failures. In state machine tests this level is used
to print transitions.
## Traits§
FailurePersistenceProvides external persistence for historical test failures by storing seeds.ProptestResultExtExtension trait for `Result<T, E>` to provide additional functionality
specifically for prop test cases.ResultCacheAn object which can cache the outcomes of tests.
## Functions§
basic_result_cache`std`A basic result cache.contextualize_config`std` and non-WebAssemblyOverride the config fields from environment variables, if any are set.
Without the `std` feature this function returns config unchanged.noop_result_cacheA result cache that does nothing.
## Type Aliases§
TestCaseResultConvenience for the type returned by test cases.