proptest::array
# Function uniform17 
Source 

```
pub fn uniform17<S: Strategy>(
    strategy: S,
) -> UniformArrayStrategy<S, [S::Value; 17]>
```