rapier3d::counters

# Struct Counters

Source

```
pub struct Counters {
    pub enabled: bool,
    pub step_time: Timer,
    pub custom: Timer,
    pub stages: StagesCounters,
    pub cd: CollisionDetectionCounters,
    pub solver: SolverCounters,
    pub ccd: CCDCounters,
}
```

## Fields§

§`enabled: bool`

Whether this counter is enabled or not.
§`step_time: Timer`

Timer for a whole timestep.
§`custom: Timer`

Timer used for debugging.
§`stages: StagesCounters`

Counters of every stage of one time step.
§`cd: CollisionDetectionCounters`

Counters of the collision-detection stage.
§`solver: SolverCounters`

Counters of the constraints resolution and force computation stage.
§`ccd: CCDCounters`

Counters for the CCD resolution stage.

## Implementations§
