rapier3d::counters

# Struct StagesCounters

Source

```
pub struct StagesCounters {
    pub update_time: Timer,
    pub collision_detection_time: Timer,
    pub island_construction_time: Timer,
    pub island_constraints_collection_time: Timer,
    pub solver_time: Timer,
    pub ccd_time: Timer,
    pub user_changes: Timer,
}
```

## Fields§

§`update_time: Timer`

Time spent for updating the kinematic and dynamics of every body.
§`collision_detection_time: Timer`

Total time spent for the collision detection (including both broad- and narrow- phases).
§`island_construction_time: Timer`

Time spent for the computation of collision island and body activation/deactivation (sleeping).
§`island_constraints_collection_time: Timer`

Time spent for collecting awake constraints from islands.
§`solver_time: Timer`

Total time spent for the constraints resolution and position update.t
§`ccd_time: Timer`

Total time spent for CCD and CCD resolution.
§`user_changes: Timer`

Total time spent propagating user changes.

## Implementations§
