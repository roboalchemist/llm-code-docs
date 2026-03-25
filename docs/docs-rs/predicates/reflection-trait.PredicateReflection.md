predicates::reflection

# Trait PredicateReflection

Source

```
pub trait PredicateReflection: Display {
    // Provided methods
    fn parameters<'a>(&'a self) -> Box<dyn Iterator<Item = Parameter<'a>> + 'a> { ... }
    fn children<'a>(&'a self) -> Box<dyn Iterator<Item = Child<'a>> + 'a> { ... }
}
```

## Provided Methods§
