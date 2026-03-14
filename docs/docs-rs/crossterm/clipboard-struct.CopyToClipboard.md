crossterm::clipboard
# Struct CopyToClipboard 
Source 

```
pub struct CopyToClipboard<T> {
    pub content: T,
    pub destination: ClipboardSelection,
}
```

## Fields§
§`content: T`

Content to be copied
§`destination: ClipboardSelection`

Sequence of copy destinations

Not all sequences are equally supported by terminal emulators. See
`CopyToClipboard` (Terminal Support).

## Implementations§