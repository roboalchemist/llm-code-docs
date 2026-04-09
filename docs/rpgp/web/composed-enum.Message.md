pgp::composed
# Enum Message 
Source 

```
pub enum Message<'a> {
    Literal {
        reader: LiteralDataReader<MessageReader<'a>>,
        is_nested: bool,
    },
    Compressed {
        reader: CompressedDataReader<MessageReader<'a>>,
        is_nested: bool,
    },
    Signed {
        reader: SignatureManyReader<'a>,
        is_nested: bool,
    },
    Encrypted {
        esk: Vec<Esk>,
        edata: Edata<'a>,
        is_nested: bool,
    },
}
```

## Variants§
§
### Literal