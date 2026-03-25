inquire::validator
# Trait DateValidator 
Source 

```
pub trait DateValidator: DynClone {
    // Required method
    fn validate(&self, input: NaiveDate) -> Result<Validation, CustomUserError>;
}
```
Available on **crate feature `date`** only.
## Required Methods§