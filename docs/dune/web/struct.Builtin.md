dune
# Struct Builtin 
Source 

```
pub struct Builtin {
    pub name: String,
    pub body: fn(Vec<Expression>, &mut Environment) -> Result<Expression, Error>,
    pub help: String,
}
```

## Fields§
§`name: String`

name of the function
§`body: fn(Vec<Expression>, &mut Environment) -> Result<Expression, Error>`

function pointer for executing the function
§`help: String`

help string

## Trait Implementations§