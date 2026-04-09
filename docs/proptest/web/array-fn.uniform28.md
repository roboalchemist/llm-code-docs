proptest::array
# Function uniform28 
Source 

```
pub fn uniform28<S: Strategy>(
    strategy: S,
) -> UniformArrayStrategy<S, [S::Value; 28]>
```