proptest::array
# Function uniform9 
Source 

```
pub fn uniform9<S: Strategy>(
    strategy: S,
) -> UniformArrayStrategy<S, [S::Value; 9]>
```