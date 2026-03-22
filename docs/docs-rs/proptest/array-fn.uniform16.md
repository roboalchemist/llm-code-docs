proptest::array
# Function uniform16 
Source 

```
pub fn uniform16<S: Strategy>(
    strategy: S,
) -> UniformArrayStrategy<S, [S::Value; 16]>
```