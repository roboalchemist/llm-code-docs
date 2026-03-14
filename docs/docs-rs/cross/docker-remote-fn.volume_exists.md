cross::docker::remote
# Function volume_exists 
Source 

```
pub fn volume_exists(
    engine: &Engine,
    volume: &str,
    msg_info: &mut MessageInfo,
) -> Result<bool>
```