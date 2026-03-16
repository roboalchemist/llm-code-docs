proptest
# Module collection 
Source 
## Structs§
BTreeMapStrategyStrategy to create `BTreeMap`s with a length in a certain range.BTreeMapValueTree`ValueTree` corresponding to `BTreeMapStrategy`.BTreeSetStrategyStrategy to create `BTreeSet`s with a length in a certain range.BTreeSetValueTree`ValueTree` corresponding to `BTreeSetStrategy`.BinaryHeapStrategyStrategy to create `BinaryHeap`s with a length in a certain range.BinaryHeapValueTree`ValueTree` corresponding to `BinaryHeapStrategy`.HashMapStrategy`std`Strategy to create `HashMap`s with a length in a certain range.HashMapValueTree`std``ValueTree` corresponding to `HashMapStrategy`.HashSetStrategy`std`Strategy to create `HashSet`s with a length in a certain range.HashSetValueTree`std``ValueTree` corresponding to `HashSetStrategy`.LinkedListStrategyStrategy to create `LinkedList`s with a length in a certain range.LinkedListValueTree`ValueTree` corresponding to `LinkedListStrategy`.SizeRangeThe minimum and maximum range/bounds on the size of a collection.
The interval must form a subset of `[0, std::usize::MAX)`.VecDequeStrategyStrategy to create `VecDeque`s with a length in a certain range.VecDequeValueTree`ValueTree` corresponding to `VecDequeStrategy`.VecStrategyStrategy to create `Vec`s with a length in a certain range.VecValueTree`ValueTree` corresponding to `VecStrategy`.
## Functions§
binary_heapCreate a strategy to generate `BinaryHeap`s containing elements drawn from
`element` and with a size range given by `size`.btree_mapCreate a strategy to generate `BTreeMap`s containing keys and values drawn
from `key` and `value` respectively, and with a size within the given
range.btree_setCreate a strategy to generate `BTreeSet`s containing elements drawn from
`element` and with a size range given by `size`.hash_map`std`Create a strategy to generate `HashMap`s containing keys and values drawn
from `key` and `value` respectively, and with a size within the given
range.hash_set`std`Create a strategy to generate `HashSet`s containing elements drawn from
`element` and with a size range given by `size`.linked_listCreate a strategy to generate `LinkedList`s containing elements drawn from
`element` and with a size range given by `size`.size_rangeCreates a `SizeRange` from some value that is convertible into it.vecCreate a strategy to generate `Vec`s containing elements drawn from
`element` and with a size range given by `size`.vec_dequeCreate a strategy to generate `VecDeque`s containing elements drawn from
`element` and with a size range given by `size`.