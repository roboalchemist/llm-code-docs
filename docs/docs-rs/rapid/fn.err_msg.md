rapid
# Function err_msg 
Source 

```
pub fn err_msg<D>(msg: D) -> Errorwhere
    D: Display + Debug + Sync + Send + 'static,
```