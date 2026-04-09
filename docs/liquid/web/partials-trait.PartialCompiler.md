liquid::partials
# Trait PartialCompiler
Source 

```
pub trait PartialCompiler {
    // Required methods
    fn compile(
        self,
        language: Arc<Language>,
    ) -> Result<Box<dyn PartialStore + Send + Sync>, Error>;
    fn source(&self) -> &dyn PartialSource;
}
```

## Required Methods§