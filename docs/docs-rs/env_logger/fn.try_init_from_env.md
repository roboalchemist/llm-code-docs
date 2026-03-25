env_logger
# Function try_init_from_env 
Source 

```
pub fn try_init_from_env<'a, E>(env: E) -> Result<(), SetLoggerError>where
    E: Into<Env<'a>>,
```