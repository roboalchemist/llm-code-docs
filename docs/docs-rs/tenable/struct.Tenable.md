tenable
# Struct Tenable 
Source 

```
pub struct Tenable<'a> {
    pub auth: String,
    pub uri: Cow<'a, str>,
}
```

## Fields§
§`auth: String`

Authentication string
§`uri: Cow<'a, str>`

Uri to send requests against

## Implementations§