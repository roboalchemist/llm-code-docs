validator
# Trait ValidateArgs 
Source 

```
pub trait ValidateArgs<'v_a> {
    type Args;

    // Required method
    fn validate_with_args(
        &self,
        args: Self::Args,
    ) -> Result<(), ValidationErrors>;
}
```

## Required Associated Types§
Source
#### type Args