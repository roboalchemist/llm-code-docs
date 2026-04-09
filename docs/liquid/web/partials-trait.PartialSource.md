liquid::partials
# Trait PartialSource
Source 

```
pub trait PartialSource: Debug {
    // Required methods
    fn contains(&self, name: &str) -> bool;
    fn names(&self) -> Vec<&str>;
    fn try_get<'a>(&'a self, name: &str) -> Option<Cow<'a, str>>;

    // Provided method
    fn get<'a>(&'a self, name: &str) -> Result<Cow<'a, str>, Error> { ... }
}
```

## Required Methods§