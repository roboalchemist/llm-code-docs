proptest::array
# Function uniform26 
Source 

```
pub fn uniform26<S: Strategy>(
    strategy: S,
) -> UniformArrayStrategy<S, [S::Value; 26]>
```