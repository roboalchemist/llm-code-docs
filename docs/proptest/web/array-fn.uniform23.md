proptest::array
# Function uniform23 
Source 

```
pub fn uniform23<S: Strategy>(
    strategy: S,
) -> UniformArrayStrategy<S, [S::Value; 23]>
```