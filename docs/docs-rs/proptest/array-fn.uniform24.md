proptest::array
# Function uniform24 
Source 

```
pub fn uniform24<S: Strategy>(
    strategy: S,
) -> UniformArrayStrategy<S, [S::Value; 24]>
```