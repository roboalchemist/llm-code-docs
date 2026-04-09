proptest::array
# Function uniform1 
Source 

```
pub fn uniform1<S: Strategy>(
    strategy: S,
) -> UniformArrayStrategy<S, [S::Value; 1]>
```