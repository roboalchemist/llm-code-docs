rpm
# Struct Scriptlet 
Source 

```
pub struct Scriptlet {
    pub script: String,
    pub flags: Option<ScriptletFlags>,
    pub program: Option<Vec<String>>,
}
```

## Fields§
§`script: String`

Content of the scriptlet
§`flags: Option<ScriptletFlags>`

Optional scriptlet flags
§`program: Option<Vec<String>>`

Optional scriptlet interpreter/arguments

## Implementations§