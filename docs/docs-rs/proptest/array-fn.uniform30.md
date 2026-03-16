proptest::array
# Function uniform30 
Source 

```
pub fn uniform30<S: Strategy>(
    strategy: S,
) -> UniformArrayStrategy<S, [S::Value; 30]>
```