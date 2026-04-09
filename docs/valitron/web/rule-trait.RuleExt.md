valitron::rule

# Trait RuleExt

Source

```
pub trait RuleExt<Input, Msg>: Sealed<Input> {
    // Required methods
    fn and<R>(self, other: R) -> RuleList<Input, Msg>
       where R: CoreRule<Input, (), Message = Msg>;
    fn custom<F, V>(self, other: F) -> RuleList<Input, Msg>
       where F: for<'a> FnOnce(&'a mut V) -> Result<(), Msg> + CoreRule<Input, V, Message = Msg>,
             V: FromValue + 'static;
}
```

## Required Methods§

Source

#### fn and<R>(self, other: R) -> RuleList<Input, Msg>where

    R: CoreRule<Input, (), Message = Msg>,
