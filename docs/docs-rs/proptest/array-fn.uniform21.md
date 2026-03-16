proptest::array
# Function uniform21 
Source 

```
pub fn uniform21<S: Strategy>(
    strategy: S,
) -> UniformArrayStrategy<S, [S::Value; 21]>
```