valitron::rule::string

# Trait StringRuleExt

Source

```
pub trait StringRuleExt<M>: Sealed {
    // Required methods
    fn and<R>(self, other: R) -> RuleList<String, M>
       where R: CoreRule<String, (), Message = M>;
    fn custom<F>(self, other: F) -> RuleList<String, M>
       where F: FnOnce(&mut String) -> Result<(), M> + Clone + 'static;
}
```

## Required Methods§

Source

#### fn and<R>(self, other: R) -> RuleList<String, M>where

    R: CoreRule<String, (), Message = M>,
