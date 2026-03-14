cross::docker::remote
# Function container_stop 
Source 

```
pub fn container_stop(
    engine: &Engine,
    container: &str,
    timeout: u32,
    msg_info: &mut MessageInfo,
) -> Result<ExitStatus>
```