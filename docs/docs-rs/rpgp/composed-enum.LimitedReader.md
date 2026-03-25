pgp::composed
# Enum LimitedReader 
Source 

```
pub enum LimitedReader<R: BufRead> {
    Fixed {
        reader: Take<R>,
    },
    Indeterminate(R),
    Partial(Take<R>),
}
```

## Variants§
§
### Fixed