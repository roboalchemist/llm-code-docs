iocraft
# Struct Element 
Source 

```
pub struct Element<'a, T: ElementType + 'a> {
    pub key: ElementKey,
    pub props: T::Props<'a>,
}
```

## Fields§
§`key: ElementKey`

The key of the element.
§`props: T::Props<'a>`

The properties of the element.

## Implementations§