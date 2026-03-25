inquire
# Trait InnerAction 
Source 

```
pub trait InnerActionwhere
    Self: Sized + Copy + Clone + PartialEq + Eq,{
    type Config;

    // Required method
    fn from_key(key: Key, config: &Self::Config) -> Option<Self>
       where Self: Sized;
}
```

## Required Associated Types§