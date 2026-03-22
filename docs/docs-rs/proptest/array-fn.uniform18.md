proptest::array
# Function uniform18 
Source 

```
pub fn uniform18<S: Strategy>(
    strategy: S,
) -> UniformArrayStrategy<S, [S::Value; 18]>
```