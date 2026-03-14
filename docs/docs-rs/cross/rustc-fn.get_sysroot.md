cross::rustc
# Function get_sysroot 
Source 

```
pub fn get_sysroot(
    host: &Host,
    target: &Target,
    channel: Option<&str>,
    msg_info: &mut MessageInfo,
) -> Result<(String, PathBuf)>
```