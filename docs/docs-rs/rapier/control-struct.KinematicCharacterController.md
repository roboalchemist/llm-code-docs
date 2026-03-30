rapier3d::control

# Struct KinematicCharacterController

Source

```
pub struct KinematicCharacterController {
    pub up: Vector,
    pub offset: CharacterLength,
    pub slide: bool,
    pub autostep: Option<CharacterAutostep>,
    pub max_slope_climb_angle: f32,
    pub min_slope_slide_angle: f32,
    pub snap_to_ground: Option<CharacterLength>,
    pub normal_nudge_factor: f32,
}
```

## Fields§

§`up: Vector`

The direction that goes “up”. Used to determine where the floor is, and the floor’s angle.
§`offset: CharacterLength`

A small gap to preserve between the character and its surroundings.

This value should not be too large to avoid visual artifacts, but shouldn’t be too small
(must not be zero) to improve numerical stability of the character controller.
§`slide: bool`

Should the character try to slide against the floor if it hits it?
§`autostep: Option<CharacterAutostep>`

Should the character automatically step over small obstacles? (disabled by default)

Note that autostepping is currently a very computationally expensive feature, so it
is disabled by default.
§`max_slope_climb_angle: f32`

The maximum angle (radians) between the floor’s normal and the `up` vector that the
character is able to climb.
§`min_slope_slide_angle: f32`

The minimum angle (radians) between the floor’s normal and the `up` vector before the
character starts to slide down automatically.
§`snap_to_ground: Option<CharacterLength>`

Should the character be automatically snapped to the ground if the distance between
the ground and its feed are smaller than the specified threshold?
§`normal_nudge_factor: f32`

Increase this number if your character appears to get stuck when sliding against surfaces.

This is a small distance applied to the movement toward the contact normals of shapes hit
by the character controller. This helps shape-casting not getting stuck in an always-penetrating
state during the sliding calculation.

This value should remain fairly small since it can introduce artificial “bumps” when sliding
along a flat surface.

## Implementations§
