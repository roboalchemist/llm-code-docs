bat::assets
# Function build 
Source 

```
pub fn build(
    source_dir: &Path,
    include_integrated_assets: bool,
    include_acknowledgements: bool,
    target_dir: &Path,
    current_version: &str,
) -> Result<()>
```