predicates::prelude

# Trait PredicateBoxExt

Source

```
pub trait PredicateBoxExt<Item: ?Sized>where
    Self: Predicate<Item>,{
    // Provided method
    fn boxed(self) -> BoxPredicate<Item>
       where Self: Sized + Send + Sync + 'static { ... }
}
```

## Provided Methods§
