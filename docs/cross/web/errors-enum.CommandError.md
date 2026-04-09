cross::errors
# Enum CommandError 
Source 

```
pub enum CommandError {
    NonZeroExitCode {
        status: ExitStatus,
        command: String,
        stderr: Vec<u8>,
        stdout: Vec<u8>,
    },
    CouldNotExecute {
        source: Box<dyn Error + Send + Sync>,
        command: String,
    },
    Utf8Error(FromUtf8Error, Output),
}
```

## Variants§
§
### NonZeroExitCode