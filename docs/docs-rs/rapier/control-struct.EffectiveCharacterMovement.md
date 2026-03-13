rapier3d::control

# Struct EffectiveCharacterMovement

Source

```
pub struct EffectiveCharacterMovement {
    pub translation: Vector,
    pub grounded: bool,
    pub is_sliding_down_slope: bool,
}
```

## Fields§

§`translation: Vector`

The movement to apply.
§`grounded: bool`

Is the character touching the ground after applying `EffectiveKineamticMovement::translation`?
§`is_sliding_down_slope: bool`

Is the character sliding down a slope due to slope angle being larger than `min_slope_slide_angle`?

## Trait Implementations§
