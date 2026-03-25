proptest::array
# Function uniform22 
Source 

```
pub fn uniform22<S: Strategy>(
    strategy: S,
) -> UniformArrayStrategy<S, [S::Value; 22]>
```