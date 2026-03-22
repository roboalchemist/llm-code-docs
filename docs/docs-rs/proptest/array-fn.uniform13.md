proptest::array
# Function uniform13 
Source 

```
pub fn uniform13<S: Strategy>(
    strategy: S,
) -> UniformArrayStrategy<S, [S::Value; 13]>
```