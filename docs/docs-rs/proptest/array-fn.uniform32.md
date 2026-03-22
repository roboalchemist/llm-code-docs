proptest::array
# Function uniform32 
Source 

```
pub fn uniform32<S: Strategy>(
    strategy: S,
) -> UniformArrayStrategy<S, [S::Value; 32]>
```