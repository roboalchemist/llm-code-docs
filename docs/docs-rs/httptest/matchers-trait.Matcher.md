httptest::matchers
# Trait Matcher 
Source 

```
pub trait Matcher<IN>: Sendwhere
    IN: ?Sized,{
    // Required methods
    fn matches(&mut self, input: &IN, ctx: &mut ExecutionContext) -> bool;
    fn fmt(&self, f: &mut Formatter<'_>) -> Result;
}
```

## Required Methods§