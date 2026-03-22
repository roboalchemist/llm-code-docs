proptest::array
# Function uniform 
Source 

```
pub fn uniform<S: Strategy, const N: usize>(
    strategy: S,
) -> UniformArrayStrategy<S, [S::Value; N]>
```