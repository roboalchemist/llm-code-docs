cross::docker::remote
# Function copy_volume_container_rust 
Source 

```
pub fn copy_volume_container_rust(
    engine: &Engine,
    container: &str,
    sysroot: &Path,
    target: &Target,
    mount_prefix: &Path,
    skip_target: bool,
    msg_info: &mut MessageInfo,
) -> Result<()>
```