proptest::array
# Function uniform8 
Source 

```
pub fn uniform8<S: Strategy>(
    strategy: S,
) -> UniformArrayStrategy<S, [S::Value; 8]>
```