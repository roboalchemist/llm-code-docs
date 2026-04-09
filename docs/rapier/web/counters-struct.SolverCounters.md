rapier3d::counters

# Struct SolverCounters

Source

```
pub struct SolverCounters {
    pub nconstraints: usize,
    pub ncontacts: usize,
    pub velocity_resolution_time: Timer,
    pub velocity_assembly_time: Timer,
    pub velocity_assembly_time_solver_bodies: Timer,
    pub velocity_assembly_time_constraints_init: Timer,
    pub velocity_update_time: Timer,
    pub velocity_writeback_time: Timer,
}
```

## Fields§

§`nconstraints: usize`

Number of constraints generated.
§`ncontacts: usize`

Number of contacts found.
§`velocity_resolution_time: Timer`

Time spent for the resolution of the constraints (force computation).
§`velocity_assembly_time: Timer`

Time spent for the assembly of all the velocity constraints.
§`velocity_assembly_time_solver_bodies: Timer`

Time spent by the velocity assembly for initializing solver bodies.
§`velocity_assembly_time_constraints_init: Timer`

Time spent by the velocity assemble for initializing the constraints.
§`velocity_update_time: Timer`

Time spent for the update of the velocity of the bodies.
§`velocity_writeback_time: Timer`

Time spent to write force back to user-accessible data.

## Implementations§
