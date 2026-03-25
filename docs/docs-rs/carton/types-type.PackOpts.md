carton::types
# Type Alias PackOpts 
Source 

```
pub type PackOpts<T> = PackOpts<T>;
```

## Aliased Type§

```
pub struct PackOpts<T> {
    pub info: CartonInfo<T>,
    pub linked_files: Option<Vec<LinkedFile>>,
}
```

## Fields§
§`info: CartonInfo<T>`§`linked_files: Option<Vec<LinkedFile>>`

Any files to include in the carton as links (instead of the originals)