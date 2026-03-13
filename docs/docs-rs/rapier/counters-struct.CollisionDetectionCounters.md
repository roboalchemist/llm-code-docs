rapier3d::counters

# Struct CollisionDetectionCounters

Source

```
pub struct CollisionDetectionCounters {
    pub ncontact_pairs: usize,
    pub broad_phase_time: Timer,
    pub final_broad_phase_time: Timer,
    pub narrow_phase_time: Timer,
}
```

## Fields§

§`ncontact_pairs: usize`

Number of contact pairs detected.
§`broad_phase_time: Timer`

Time spent for the broad-phase of the collision detection.
§`final_broad_phase_time: Timer`

Time spent by the final broad-phase AABB update after body movement to keep
user scene queries valid.
§`narrow_phase_time: Timer`

Time spent for the narrow-phase of the collision detection.

## Implementations§
