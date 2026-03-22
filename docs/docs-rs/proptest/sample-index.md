proptest
# Module sample 
Source 
## Re-exports§
`pub use crate::collection::size_range;``pub use crate::collection::SizeRange;`
## Structs§
IndexA stand-in for an index into a slice or similar collection or conceptually
similar things.IndexStrategyStrategy to create `Index`es.IndexValueTree`ValueTree` corresponding to `IndexStrategy`.SelectStrategy to produce one value from a fixed collection of options.SelectValueTree`ValueTree` corresponding to `Select`.SelectorA value for picking random values out of iterators.SelectorStrategyStrategy to create `Selector`s.SelectorValueTree`ValueTree` corresponding to `SelectorStrategy`.SubsequenceStrategy to generate `Vec`s by sampling a subsequence from another
collection.SubsequenceValueTree`ValueTree` type for `Subsequence`.
## Functions§
selectCreate a strategy which uniformly selects one value from `values`.subsequenceSample subsequences whose size are within `size` from the given collection
`values`.