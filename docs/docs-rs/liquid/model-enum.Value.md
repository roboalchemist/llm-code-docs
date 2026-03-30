liquid::model
# Enum Value
Source 

```
pub enum Value {
    Scalar(ScalarCow<'static>),
    Array(Vec<Value>),
    Object(Object),
    State(State),
    Nil,
}
```

## Variants§
§
### Scalar(ScalarCow<'static>)