proptest::array
# Function uniform19 
Source 

```
pub fn uniform19<S: Strategy>(
    strategy: S,
) -> UniformArrayStrategy<S, [S::Value; 19]>
```