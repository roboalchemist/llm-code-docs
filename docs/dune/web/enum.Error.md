dune
# Enum Error 
Source 

```
pub enum Error {
    CannotApply(Expression, Vec<Expression>),
    SymbolNotDefined(String),
    CommandFailed(String, Vec<Expression>),
    ForNonList(Expression),
    RecursionDepth(Expression),
    CustomError(String),
    SyntaxError(Str, SyntaxError),
}
```

## Variants§
§
### CannotApply(Expression, Vec<Expression>)