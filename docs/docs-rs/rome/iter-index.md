rome
# Module iter 
Source 
## Re-exports§
`pub use self::merge_iterator::MergeIterator;``pub use self::transitive_iterator::TransitiveIterator;`
## Modules§
merge_iteratorIterator that merges other iterators.transitive_iteratorIterator that is a collection of iterators.
## Traits§
SortedIteratorIterator that gives out items in ascending order
This trait only indicates that the iterator works like this.
The implementations of the trait are responsible for ensuring that
items are sorted and that each value occurs only once.