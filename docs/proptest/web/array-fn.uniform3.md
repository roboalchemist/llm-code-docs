proptest::array
# Function uniform3 
Source 

```
pub fn uniform3<S: Strategy>(
    strategy: S,
) -> UniformArrayStrategy<S, [S::Value; 3]>
```