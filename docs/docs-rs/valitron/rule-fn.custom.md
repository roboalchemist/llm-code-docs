valitron::rule

# Function custom

Source

```
pub fn custom<F, V, Input, Msg>(f: F) -> RuleList<Input, Msg>where
    F: FnOnce(&mut V) -> Result<(), Msg> + CoreRule<Input, V, Message = Msg>,
    V: FromValue + 'static,
    Msg: 'static,
```
