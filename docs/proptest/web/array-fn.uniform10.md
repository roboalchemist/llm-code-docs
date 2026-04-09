proptest::array
# Function uniform10 
Source 

```
pub fn uniform10<S: Strategy>(
    strategy: S,
) -> UniformArrayStrategy<S, [S::Value; 10]>
```