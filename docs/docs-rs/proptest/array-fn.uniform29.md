proptest::array
# Function uniform29 
Source 

```
pub fn uniform29<S: Strategy>(
    strategy: S,
) -> UniformArrayStrategy<S, [S::Value; 29]>
```