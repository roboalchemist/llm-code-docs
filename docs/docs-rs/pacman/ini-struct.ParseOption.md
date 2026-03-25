pacman::ini
# Struct ParseOption 
Source 

```
pub struct ParseOption {
    pub enabled_quote: bool,
    pub enabled_escape: bool,
}
```

## Fields§
§`enabled_quote: bool`

Allow quote (“ or ’) in value
For example

```
[Section]
Key1="Quoted value"
Key2='Single Quote' with extra value
```

In this example, Value of `Key1` is `Quoted value`,
and value of `Key2` is `Single Quote with extra value`
if `enabled_quote` is set to `true`.
§`enabled_escape: bool`

Interpret `\` as an escape character
For example

```
[Section]
Key1=C:\Windows
```

If `enabled_escape` is true, then the value of `Key` will become `C:Windows` (`\W` equals to `W`).

## Trait Implementations§