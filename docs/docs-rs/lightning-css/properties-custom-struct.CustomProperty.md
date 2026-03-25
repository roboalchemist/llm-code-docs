lightningcss::properties::custom

# Struct CustomProperty

Source

```
pub struct CustomProperty<'i> {
    pub name: CustomPropertyName<'i>,
    pub value: TokenList<'i>,
}
```

## Fields§

§`name: CustomPropertyName<'i>`

The name of the property.
§`value: TokenList<'i>`

The property value, stored as a raw token list.

## Implementations§
