rpm
# Struct Package 
Source 

```
pub struct Package {
    pub metadata: PackageMetadata,
    pub content: Vec<u8>,
}
```

## Fields§
§`metadata: PackageMetadata`

Header and metadata structures.

Contains the constant lead as well as the metadata store.
§`content: Vec<u8>`

The compressed or uncompressed files.

## Implementations§