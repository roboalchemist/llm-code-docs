assemble::command
# Function run 
Source 

```
pub fn run(
    cmd: &str,
    env: &BTreeMap<String, String>,
) -> Result<Child, Box<dyn Error>>
```