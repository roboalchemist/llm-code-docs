cargo::ops

# Enum RegistryCredentialConfig

Source

```
pub enum RegistryCredentialConfig {
    None,
    Token(Secret<String>),
    Process(Vec<PathAndArgs>),
    AsymmetricKey((Secret<String>, Option<String>)),
}
```

## Variants§

§

### None
