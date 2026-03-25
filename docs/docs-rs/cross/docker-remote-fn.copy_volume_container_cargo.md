cross::docker::remote
# Function copy_volume_container_cargo 
Source 

```
pub fn copy_volume_container_cargo(
    engine: &Engine,
    container: &str,
    cargo_dir: &Path,
    mount_prefix: &Path,
    copy_registry: bool,
    msg_info: &mut MessageInfo,
) -> Result<()>
```