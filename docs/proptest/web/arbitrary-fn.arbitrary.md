proptest::arbitrary
# Function arbitrary 
Source 

```
pub fn arbitrary<A, S>() -> Swhere
    S: Strategy<Value = A>,
    A: Arbitrary<Strategy = S>,
```