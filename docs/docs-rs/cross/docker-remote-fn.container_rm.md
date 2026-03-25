cross::docker::remote
# Function container_rm 
Source 

```
pub fn container_rm(
    engine: &Engine,
    container: &str,
    msg_info: &mut MessageInfo,
) -> Result<ExitStatus>
```