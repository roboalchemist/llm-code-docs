rapier3d::control

# Struct DynamicRayCastVehicleController

Source

```
pub struct DynamicRayCastVehicleController {
    pub current_vehicle_speed: f32,
    pub chassis: RigidBodyHandle,
    pub index_up_axis: usize,
    pub index_forward_axis: usize,
    /* private fields */
}
```

## Fields§

§`current_vehicle_speed: f32`

The current forward speed of the vehicle.
§`chassis: RigidBodyHandle`

Handle of the vehicle’s chassis.
§`index_up_axis: usize`

The chassis’ local *up* direction (`0 = x, 1 = y, 2 = z`)
§`index_forward_axis: usize`

The chassis’ local *forward* direction (`0 = x, 1 = y, 2 = z`)

## Implementations§
