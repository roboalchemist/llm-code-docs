rapier3d::dynamics

# Struct IntegrationParameters

Source

```
pub struct IntegrationParameters {}
```

## Fields§

§`dt: f32`

The timestep length - how much simulated time passes per physics step (default: `1.0 / 60.0`).

Set this to `1.0 / your_target_fps`. For example:

- 60 FPS: `1.0 / 60.0` ≈ 0.0167 seconds

- 120 FPS: `1.0 / 120.0` ≈ 0.0083 seconds

Smaller timesteps are more accurate but require more CPU time per second of simulated time.
§`min_ccd_dt: f32`

Minimum timestep size when using CCD with multiple substeps (default: `1.0 / 60.0 / 100.0`).

When CCD with multiple substeps is enabled, the timestep is subdivided
into smaller pieces. This timestep subdivision won’t generate timestep
lengths smaller than `min_ccd_dt`.

Setting this to a large value will reduce the opportunity to performing
CCD substepping, resulting in potentially more time dropped by the
motion-clamping mechanism. Setting this to an very small value may lead
to numerical instabilities.
§`contact_softness: SpringCoefficients<f32>`

Softness coefficients for contact constraints.
§`warmstart_coefficient: f32`

The coefficient in `[0, 1]` applied to warmstart impulses, i.e., impulses that are used as the
initial solution (instead of 0) at the next simulation step.

This should generally be set to 1.

(default `1.0`).
§`length_unit: f32`

The scale factor for your world if you’re not using meters (default: `1.0`).

Rapier is tuned for human-scale objects measured in meters. If your game uses different
units, set this to how many of your units equal 1 meter in the real world.

**Examples:**

- Your game uses meters: `length_unit = 1.0` (default)

- Your game uses centimeters: `length_unit = 100.0` (100 cm = 1 m)

- Pixel-based 2D game where typical objects are 100 pixels tall: `length_unit = 100.0`

- Your game uses feet: `length_unit = 3.28` (approximately)

This automatically scales various internal tolerances and thresholds to work correctly
with your chosen units.
§`normalized_allowed_linear_error: f32`

Amount of penetration the engine won’t attempt to correct (default: `0.001m`).

This value is implicitly scaled by `IntegrationParameters::length_unit`.
§`normalized_max_corrective_velocity: f32`

Maximum amount of penetration the solver will attempt to resolve in one timestep (default: `10.0`).

This value is implicitly scaled by `IntegrationParameters::length_unit`.
§`normalized_prediction_distance: f32`

The maximal distance separating two objects that will generate predictive contacts (default: `0.002m`).

This value is implicitly scaled by `IntegrationParameters::length_unit`.
§`num_solver_iterations: usize`

The number of solver iterations run by the constraints solver for calculating forces (default: `4`).

Higher values produce more accurate and stable simulations at the cost of performance.

- `4` (default): Good balance for most games

- `8-12`: Use for demanding scenarios (stacks of objects, complex machinery)

- `1-2`: Use if performance is critical and accuracy can be sacrificed

§`num_internal_pgs_iterations: usize`

Number of internal Project Gauss Seidel (PGS) iterations run at each solver iteration (default: `1`).
§`num_internal_stabilization_iterations: usize`

The number of stabilization iterations run at each solver iterations (default: `1`).
§`min_island_size: usize`

Minimum number of dynamic bodies on each active island (default: `128`).
§`max_ccd_substeps: usize`

Maximum number of substeps performed by the  solver (default: `1`).
§`friction_model: FrictionModel`

The type of friction constraints used in the simulation.

## Implementations§
