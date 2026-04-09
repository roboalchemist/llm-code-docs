cross
# Function pretty_path 
Source 

```
pub fn pretty_path(
    path: impl AsRef<Path>,
    strip: impl for<'a> Fn(&'a str) -> bool,
) -> String
```