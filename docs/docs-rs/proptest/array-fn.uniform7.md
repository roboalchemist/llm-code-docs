proptest::array
# Function uniform7 
Source 

```
pub fn uniform7<S: Strategy>(
    strategy: S,
) -> UniformArrayStrategy<S, [S::Value; 7]>
```