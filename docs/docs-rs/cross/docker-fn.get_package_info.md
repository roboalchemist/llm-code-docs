cross::docker
# Function get_package_info 
Source 

```
pub fn get_package_info(
    engine: &Engine,
    target: &str,
    channel: Option<&str>,
    msg_info: &mut MessageInfo,
) -> Result<(Target, CargoMetadata, Directories)>
```