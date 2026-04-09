rapid
# Macro log_process 
Source 

```
macro_rules! log_process {
    ($msg:expr, $($params:expr),* => $block:block) => { ... };
    ($msg:expr, $($params:expr),* => $block:block) => { ... };
    ($msg:expr => $block:block) => { ... };
}
```