rome::iter::transitive_iterator
# Struct TransitiveIterator 
Source 

```
pub struct TransitiveIterator<I, J, F>where
    I: SortedIterator,
    I::Item: Ord + Clone,
    J: SortedIterator<Item = I::Item>,
    F: Fn(&J::Item) -> J,{ /* private fields */ }
```

## Implementations§