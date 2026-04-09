verify
# Trait Validate 
Source 

```
pub trait Validate: Spanned {
    // Required method
    fn validate<V: Validator<Self::Span>>(
        &self,
        validator: V,
    ) -> Result<(), V::Error>;
}
```

## Required Methods§