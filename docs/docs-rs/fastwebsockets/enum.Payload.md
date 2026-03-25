fastwebsockets

# Enum Payload

Source

```
pub enum Payload<'a> {
    BorrowedMut(&'a mut [u8]),
    Borrowed(&'a [u8]),
    Owned(Vec<u8>),
    Bytes(BytesMut),
}
```

## Variants§

§

### BorrowedMut(&'a mut [u8])
