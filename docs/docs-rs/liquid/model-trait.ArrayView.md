liquid::model
# Trait ArrayView
Source 

```
pub trait ArrayView: ValueView {
    // Required methods
    fn as_value(&self) -> &dyn ValueView;
    fn size(&self) -> i64;
    fn values<'k>(&'k self) -> Box<dyn Iterator<Item = &'k dyn ValueView> + 'k>;
    fn contains_key(&self, index: i64) -> bool;
    fn get(&self, index: i64) -> Option<&dyn ValueView>;

    // Provided methods
    fn first(&self) -> Option<&dyn ValueView> { ... }
    fn last(&self) -> Option<&dyn ValueView> { ... }
}
```

## Required Methods§