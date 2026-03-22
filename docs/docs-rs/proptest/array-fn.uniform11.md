proptest::array
# Function uniform11 
Source 

```
pub fn uniform11<S: Strategy>(
    strategy: S,
) -> UniformArrayStrategy<S, [S::Value; 11]>
```