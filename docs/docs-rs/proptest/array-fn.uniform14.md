proptest::array
# Function uniform14 
Source 

```
pub fn uniform14<S: Strategy>(
    strategy: S,
) -> UniformArrayStrategy<S, [S::Value; 14]>
```