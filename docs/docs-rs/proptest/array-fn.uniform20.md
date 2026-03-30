proptest::array
# Function uniform20 
Source 

```
pub fn uniform20<S: Strategy>(
    strategy: S,
) -> UniformArrayStrategy<S, [S::Value; 20]>
```