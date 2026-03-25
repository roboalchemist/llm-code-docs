proptest
# Module bool 
Source 
## Structs§
AnyThe type of the `ANY` constant.BoolValueTreeThe `ValueTree` to shrink booleans to false.WeightedThe return type from `weighted()`.
## Constants§
ANYGenerates boolean values by picking `true` or `false` uniformly.
## Functions§
weightedGenerates boolean values by picking `true` with the given `probability`
(1.0 = always true, 0.0 = always false).