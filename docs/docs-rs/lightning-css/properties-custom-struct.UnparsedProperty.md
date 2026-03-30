lightningcss::properties::custom

# Struct UnparsedProperty

Source

```
pub struct UnparsedProperty<'i> {
    pub property_id: PropertyId<'i>,
    pub value: TokenList<'i>,
}
```

## Fields§

§`property_id: PropertyId<'i>`

The id of the property.
§`value: TokenList<'i>`

The property value, stored as a raw token list.

## Implementations§
