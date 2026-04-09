rapier3d::control

# Struct CharacterCollision

Source

```
pub struct CharacterCollision {
    pub handle: ColliderHandle,
    pub character_pos: Pose,
    pub translation_applied: Vector,
    pub translation_remaining: Vector,
    pub hit: ShapeCastHit,
}
```

## Fields§

§`handle: ColliderHandle`

The collider hit by the character.
§`character_pos: Pose`

The position of the character when the collider was hit.
§`translation_applied: Vector`

The translation that was already applied to the character when the hit happens.
§`translation_remaining: Vector`

The translations that was still waiting to be applied to the character when the hit happens.
§`hit: ShapeCastHit`

Geometric information about the hit.

## Trait Implementations§
