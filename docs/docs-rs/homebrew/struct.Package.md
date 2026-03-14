homebrew

# Struct Package

Source

```
pub struct Package {
    pub value: HashMap<String, Value>,
    pub name: String,
    pub full_name: String,
    pub tap: String,
    pub desc: String,
    pub homepage: String,
    /* private fields */
}
```

## Fields§

§`value: HashMap<String, Value>`

`brew info [name] --json=v2` 命令原始数据
§`name: String`

= `self.formula().name`
= `self.cask().token`
§`full_name: String`

= `self.formula().full_name`
= `self.cask().full_token`
§`tap: String`

= `self.formula().tap`
= `self.cask().tap`
§`desc: String`

= `self.formula().desc`
= `Some(self.cask().desc)`
§`homepage: String`

= `self.formula().homepage`
= `self.cask().homepage`

## Implementations§
