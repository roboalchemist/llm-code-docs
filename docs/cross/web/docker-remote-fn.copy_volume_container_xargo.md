cross::docker::remote
# Function copy_volume_container_xargo 
Source 

```
pub fn copy_volume_container_xargo(
    engine: &Engine,
    container: &str,
    xargo_dir: &Path,
    target: &Target,
    mount_prefix: &Path,
    msg_info: &mut MessageInfo,
) -> Result<()>
```