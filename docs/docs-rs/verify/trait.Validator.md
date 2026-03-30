verify
# Trait Validator 
Source 

```
pub trait Validator<S: Span>: Sized {
    type Error: Error;
    type ValidateSeq: ValidateSeq<S, Error = Self::Error>;
    type ValidateMap: ValidateMap<S, Error = Self::Error>;

}
```

## Required Associated Types§