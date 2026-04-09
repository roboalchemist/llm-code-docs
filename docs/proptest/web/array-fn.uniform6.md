proptest::array
# Function uniform6 
Source 

```
pub fn uniform6<S: Strategy>(
    strategy: S,
) -> UniformArrayStrategy<S, [S::Value; 6]>
```