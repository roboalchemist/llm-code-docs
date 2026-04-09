tenable::types
# Struct AssetsMove 
Source 

```
pub struct AssetsMove<'a> {
    pub tenable: &'a Tenable<'a>,
    pub assets_move_def: Cow<'a, AssetsMoveDef>,
}
```

## Fields§
§`tenable: &'a Tenable<'a>`

Inner tenable Client
§`assets_move_def: Cow<'a, AssetsMoveDef>`

Definition which details the move operation

## Trait Implementations§