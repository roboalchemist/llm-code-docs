bellman
# Enum SynthesisError 
Source 

```
pub enum SynthesisError {
    AssignmentMissing,
    DivisionByZero,
    Unsatisfiable,
    PolynomialDegreeTooLarge,
    UnexpectedIdentity,
    IoError(Error),
    UnconstrainedVariable,
}
```

## Variants§
§
### AssignmentMissing