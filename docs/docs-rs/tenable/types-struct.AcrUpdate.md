tenable::types
# Struct AcrUpdate 
Source 

```
pub struct AcrUpdate<'a> {
    pub tenable: &'a Tenable<'a>,
    pub acrs: Cow<'a, [Acr]>,
}
```

## Fields§
§`tenable: &'a Tenable<'a>`

Inner tenable Client
§`acrs: Cow<'a, [Acr]>`

`Acr`s to send to tenable

## Trait Implementations§