predicates::prelude

# Trait Predicate

Source

```
pub trait Predicate<Item>: PredicateReflectionwhere
    Item: ?Sized,{
    // Required method
    fn eval(&self, variable: &Item) -> bool;

    // Provided method
    fn find_case<'a>(
        &'a self,
        expected: bool,
        variable: &Item,
    ) -> Option<Case<'a>> { ... }
}
```

## Required Methods§
