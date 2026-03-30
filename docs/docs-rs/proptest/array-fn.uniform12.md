proptest::array
# Function uniform12 
Source 

```
pub fn uniform12<S: Strategy>(
    strategy: S,
) -> UniformArrayStrategy<S, [S::Value; 12]>
```