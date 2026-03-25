proptest::array
# Function uniform27 
Source 

```
pub fn uniform27<S: Strategy>(
    strategy: S,
) -> UniformArrayStrategy<S, [S::Value; 27]>
```