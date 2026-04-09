druid

# Struct KeyEvent

Source

```
#[non_exhaustive]pub struct KeyEvent {
    pub state: KeyState,
    pub key: Key,
    pub code: Code,
    pub location: Location,
    pub mods: Modifiers,
    pub repeat: bool,
    pub is_composing: bool,
}
```

## Fields (Non-exhaustive)§

§`state: KeyState`

Whether the key is pressed or released.
§`key: Key`

Logical key value.
§`code: Code`

Physical key position.
§`location: Location`

Location for keys with multiple instances on common keyboards.
§`mods: Modifiers`

Flags for pressed modifier keys.
§`repeat: bool`

True if the key is currently auto-repeated.
§`is_composing: bool`

Events with this flag should be ignored in a text editor
and instead composition events should be used.

## Trait Implementations§
