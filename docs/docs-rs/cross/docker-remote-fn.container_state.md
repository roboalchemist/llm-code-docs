cross::docker::remote
# Function container_state 
Source 

```
pub fn container_state(
    engine: &Engine,
    container: &str,
    msg_info: &mut MessageInfo,
) -> Result<ContainerState>
```