inquire::autocompletion
# Trait Autocomplete 
Source 

```
pub trait Autocomplete: DynClone {
    // Required methods
    fn get_suggestions(
        &mut self,
        input: &str,
    ) -> Result<Vec<String>, CustomUserError>;
    fn get_completion(
        &mut self,
        input: &str,
        highlighted_suggestion: Option<String>,
    ) -> Result<Replacement, CustomUserError>;
}
```

## Required Methods§