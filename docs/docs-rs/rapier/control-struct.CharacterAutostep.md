rapier3d::control

# Struct CharacterAutostep

Source

```
pub struct CharacterAutostep {
    pub max_height: CharacterLength,
    pub min_width: CharacterLength,
    pub include_dynamic_bodies: bool,
}
```

## Fields§

§`max_height: CharacterLength`

The maximum step height a character can automatically step over.
§`min_width: CharacterLength`

The minimum width of free space that must be available after stepping on a stair.
§`include_dynamic_bodies: bool`

Can the character automatically step over dynamic bodies too?

## Trait Implementations§
