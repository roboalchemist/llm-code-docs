cross::docker::remote
# Function copy_volume_container_rust_triple 
Source 

```
pub fn copy_volume_container_rust_triple(
    engine: &Engine,
    container: &str,
    sysroot: &Path,
    triple: &str,
    mount_prefix: &Path,
    skip_exists: bool,
    msg_info: &mut MessageInfo,
) -> Result<()>
```