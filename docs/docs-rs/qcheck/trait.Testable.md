qcheck
# Trait Testable 
Source 

```
pub trait Testable: 'static {
    // Required method
    fn result(&self, _: &mut Gen) -> TestResult;
}
```

## Required Methods§
Source
#### fn result(&self, _: &mut Gen) -> TestResult