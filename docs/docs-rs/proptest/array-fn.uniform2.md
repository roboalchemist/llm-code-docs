proptest::array
# Function uniform2 
Source 

```
pub fn uniform2<S: Strategy>(
    strategy: S,
) -> UniformArrayStrategy<S, [S::Value; 2]>
```