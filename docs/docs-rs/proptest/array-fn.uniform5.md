proptest::array
# Function uniform5 
Source 

```
pub fn uniform5<S: Strategy>(
    strategy: S,
) -> UniformArrayStrategy<S, [S::Value; 5]>
```