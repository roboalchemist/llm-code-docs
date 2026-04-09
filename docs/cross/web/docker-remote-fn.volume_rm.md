cross::docker::remote
# Function volume_rm 
Source 

```
pub fn volume_rm(
    engine: &Engine,
    volume: &str,
    msg_info: &mut MessageInfo,
) -> Result<ExitStatus>
```