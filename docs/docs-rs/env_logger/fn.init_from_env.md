env_logger
# Function init_from_env 
Source 

```
pub fn init_from_env<'a, E>(env: E)where
    E: Into<Env<'a>>,
```

##### Examples found in repository?
examples/default.rs (line 30)

```
22fn main() {
23    // The `Env` lets us tweak what the environment
24    // variables to read are and what the default
25    // value is if they're missing
26    let env = Env::default()
27        .filter_or("MY_LOG_LEVEL", "trace")
28        .write_style_or("MY_LOG_STYLE", "always");
29
30    env_logger::init_from_env(env);
31
32    trace!("some trace log");
33    debug!("some debug log");
34    info!("some information log");
35    warn!("some warning log");
36    error!("some error log");
37}
```