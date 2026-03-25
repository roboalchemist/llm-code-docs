cargo::util::errors

# Type Alias CliResult

Source

```
pub type CliResult = Result<(), CliError>;
```

## Aliased Type§

```
pub enum CliResult {
    Ok(()),
    Err(CliError),
}
```

## Variants§

§1.0.0

### Ok(())
