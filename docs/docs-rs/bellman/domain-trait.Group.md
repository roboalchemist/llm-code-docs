bellman::domain
# Trait Group 
Source 

```
pub trait Group<Scalar: PrimeField>:
    Sized
    + Copy
    + Clone
    + Send
    + Sync {
    // Required methods
    fn group_zero() -> Self;
    fn group_mul_assign(&mut self, by: &Scalar);
    fn group_add_assign(&mut self, other: &Self);
    fn group_sub_assign(&mut self, other: &Self);
}
```

## Required Methods§
Source
#### fn group_zero() -> Self