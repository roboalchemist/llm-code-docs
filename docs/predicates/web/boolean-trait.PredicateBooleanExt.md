predicates::boolean

# Trait PredicateBooleanExt

Source

```
pub trait PredicateBooleanExt<Item: ?Sized>where
    Self: Predicate<Item>,{
    // Provided methods
    fn and<B>(self, other: B) -> AndPredicate<Self, B, Item>
       where B: Predicate<Item>,
             Self: Sized { ... }
    fn or<B>(self, other: B) -> OrPredicate<Self, B, Item>
       where B: Predicate<Item>,
             Self: Sized { ... }
    fn not(self) -> NotPredicate<Self, Item>
       where Self: Sized { ... }
}
```

## Provided Methods§
