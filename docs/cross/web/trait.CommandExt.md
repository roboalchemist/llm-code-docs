cross
# Trait CommandExt 
Source 

```
pub trait CommandExt {
    // Required methods
    fn fmt_message(&self, msg_info: &mut MessageInfo) -> String;
    fn status_result(
        &self,
        msg_info: &mut MessageInfo,
        status: ExitStatus,
        output: Option<&Output>,
    ) -> Result<(), CommandError>;
    fn run(
        &mut self,
        msg_info: &mut MessageInfo,
        silence_stdout: bool,
    ) -> Result<()>;
    fn run_and_get_status(
        &mut self,
        msg_info: &mut MessageInfo,
        silence_stdout: bool,
    ) -> Result<ExitStatus>;
    fn run_and_get_stdout(
        &mut self,
        msg_info: &mut MessageInfo,
    ) -> Result<String>;
    fn run_and_get_output(
        &mut self,
        msg_info: &mut MessageInfo,
    ) -> Result<Output>;
    fn command_pretty(
        &self,
        msg_info: &mut MessageInfo,
        strip: impl for<'a> Fn(&'a str) -> bool,
    ) -> String;

    // Provided methods
    fn print(&self, msg_info: &mut MessageInfo) -> Result<()> { ... }
    fn info(&self, msg_info: &mut MessageInfo) -> Result<()> { ... }
    fn debug(&self, msg_info: &mut MessageInfo) -> Result<()> { ... }
}
```

## Required Methods§
Source
#### fn fmt_message(&self, msg_info: &mut MessageInfo) -> String