rapier3d::counters

# Struct CCDCounters

Source

```
pub struct CCDCounters {
    pub num_substeps: usize,
    pub toi_computation_time: Timer,
    pub solver_time: Timer,
    pub broad_phase_time: Timer,
    pub narrow_phase_time: Timer,
}
```

## Fields§

§`num_substeps: usize`

The number of substeps actually performed by the CCD resolution.
§`toi_computation_time: Timer`

The total time spent for TOI computation in the CCD resolution.
§`solver_time: Timer`

The total time spent for force computation and integration in the CCD resolution.
§`broad_phase_time: Timer`

The total time spent by the broad-phase in the CCD resolution.
§`narrow_phase_time: Timer`

The total time spent by the narrow-phase in the CCD resolution.

## Implementations§
