liquid
# Trait ObjectView
Source 

```
pub trait ObjectView: ValueView {
    // Required methods
    fn as_value(&self) -> &dyn ValueView;
    fn size(&self) -> i64;
    fn keys<'k>(&'k self) -> Box<dyn Iterator<Item = KStringCowBase<'k>> + 'k>;
    fn values<'k>(&'k self) -> Box<dyn Iterator<Item = &'k dyn ValueView> + 'k>;
    fn iter<'k>(
        &'k self,
    ) -> Box<dyn Iterator<Item = (KStringCowBase<'k>, &'k dyn ValueView)> + 'k>;
    fn contains_key(&self, index: &str) -> bool;
    fn get<'s>(&'s self, index: &str) -> Option<&'s dyn ValueView>;
}
```

## Required Methods§