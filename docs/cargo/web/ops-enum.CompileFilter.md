cargo::ops

# Enum CompileFilter

Source

```
pub enum CompileFilter {
    Default {
        required_features_filterable: bool,
    },
    Only {
        all_targets: bool,
        lib: LibRule,
        bins: FilterRule,
        examples: FilterRule,
        tests: FilterRule,
        benches: FilterRule,
    },
}
```

## Variants§

§

### Default
