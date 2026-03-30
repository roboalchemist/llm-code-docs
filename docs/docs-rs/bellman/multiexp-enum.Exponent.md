bellman::multiexp
# Enum Exponent 
Source 

```
pub enum Exponent<F: PrimeFieldBits> {
    Zero,
    One,
    Bits(FieldBits<F::ReprBits>),
}
```

## Variants§
§
### Zero