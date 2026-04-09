rome::iter
# Trait SortedIterator 
Source 

```
pub trait SortedIterator: Iteratorwhere
    <Self as Iterator>::Item: Ord,{ }
```

## Implementors§
Source§
### impl<'g, R> SortedIterator for ObjectIter<'g, R>where
    R: ResourceBase<'g>,