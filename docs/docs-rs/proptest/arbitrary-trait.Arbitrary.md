proptest::arbitrary
# Trait Arbitrary 
Source 

```
pub trait Arbitrary: Sized + Debug {
    type Parameters: Default;
    type Strategy: Strategy<Value = Self>;

    // Required method
    fn arbitrary_with(args: Self::Parameters) -> Self::Strategy;

    // Provided method
    fn arbitrary() -> Self::Strategy { ... }
}
```

## Required Associated Types§