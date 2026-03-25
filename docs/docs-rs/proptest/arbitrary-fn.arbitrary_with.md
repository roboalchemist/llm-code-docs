proptest::arbitrary
# Function arbitrary_with 
Source 

```
pub fn arbitrary_with<A, S, P>(args: P) -> Swhere
    P: Default,
    S: Strategy<Value = A>,
    A: Arbitrary<Strategy = S, Parameters = P>,
```