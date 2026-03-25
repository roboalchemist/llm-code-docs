rapid::fail_methods
# Trait ErrorMethods 
Source 

```
pub trait ErrorMethods {
    // Required methods
    fn traverse<F: FnMut(String)>(&self, action: F);
    fn log_error(&self);
    fn log_warning(&self);
    fn stringify(&self) -> String;
}
```

## Required Methods§
Source
#### fn traverse<F: FnMut(String)>(&self, action: F)