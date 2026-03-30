proptest::array
# Function uniform15 
Source 

```
pub fn uniform15<S: Strategy>(
    strategy: S,
) -> UniformArrayStrategy<S, [S::Value; 15]>
```