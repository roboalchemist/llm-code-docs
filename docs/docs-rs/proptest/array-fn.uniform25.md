proptest::array
# Function uniform25 
Source 

```
pub fn uniform25<S: Strategy>(
    strategy: S,
) -> UniformArrayStrategy<S, [S::Value; 25]>
```