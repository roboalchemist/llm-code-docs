proptest::array
# Function uniform4 
Source 

```
pub fn uniform4<S: Strategy>(
    strategy: S,
) -> UniformArrayStrategy<S, [S::Value; 4]>
```