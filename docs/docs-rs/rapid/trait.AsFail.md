rapid
# Trait AsFail 
Source 

```
pub trait AsFail {
    // Required method
    fn as_fail(&self) -> &(dyn Fail + 'static);
}
```

## Required Methods§