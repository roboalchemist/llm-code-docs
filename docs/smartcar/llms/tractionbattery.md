# Source: https://smartcar.com/docs/api-reference/signals/tractionbattery.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# TractionBattery Signals

### Is Heater Active

Signal code: `tractionbattery-isheateractive`

A boolean flag indicating whether the high voltage battery's heating system is currently operating.

<ParamField path="value" type="boolean" required={false} />

### Max Range Charge Counter

Signal code: `tractionbattery-maxrangechargecounter`

A counter tracking the number of times the vehicle has been charged to its maximum range capacity.

<ParamField path="unit" type="string" required={false} />

<ParamField path="value" type="integer" required={false} />

### Nominal Capacities

Signal code: `tractionbattery-nominalcapacity`

An object containing the gross battery capacity and a list of multiple available gross capacity configurations for the high voltage battery.

<ParamField path="source" type="string" required={false}>
  Identifies the origin or method used to determine the battery's gross capacity.

  **Possible values:** `SMARTCAR`, `USER_SELECTED`
</ParamField>

<ParamField path="capacity" type="number" required={false}>
  The total gross energy storage capacity of the high voltage battery, typically measured in kilowatt-hours (kWh). This value represents the nominal rated battery capacity for a vehicle.
</ParamField>

<ParamField path="availableCapacities" type="array" required={false}>
  An array of available battery capacity configurations for the vehicle.
</ParamField>

<Expandable title="Array item properties">
  <ParamField path="capacity" type="number" required={false}>
    The battery capacity value in kilowatt-hours (kWh).
  </ParamField>

  <ParamField path="description" type="string" required={false}>
    A description of the uniqueness for the nominal capacity and engine type of the vehicle in the form {ENGINE_TYPE}:{TRIM}, for example "BEV:Extended Range".
  </ParamField>
</Expandable>

<ParamField path="unit" type="string" required={false}>
  The unit of measurement for the battery capacity.
</ParamField>

```json Example theme={null}
{
  "source": "SMARTCAR",
  "capacity": 73.5,
  "availableCapacities": [
    {
      "capacity": 73.5,
      "description": "BEV:Extended Range"
    },
    {
      "capacity": 80.9,
      "description": null
    }
  ],
  "unit": "kWh"
}
```

### Range

Signal code: `tractionbattery-range`

Returns the most accurate real world estimate that is available. Estimated > Ideal > Rated.

<ParamField path="unit" type="string" required={false}>
  **Possible values:** `DEFAULT`
</ParamField>

<ParamField path="value" type="number" required={true} />

<ParamField path="additionalValues" type="array" required={true} />

<Expandable title="Array item properties">
  <ParamField path="type" type="string" required={true}>
    **Possible values:** `IDEAL_CONDITIONS`, `ESTIMATED`, `RATED`
  </ParamField>

  <ParamField path="value" type="number" required={true} />
</Expandable>

```json Example theme={null}
{
  "unit": "kilometers",
  "value": 350
}
```

### State Of Charge

Signal code: `tractionbattery-stateofcharge`

The current charge level of the high voltage battery, expressed as a percentage (0 - 100).

<ParamField path="unit" type="string" required={false} />

<ParamField path="value" type="number" required={false} />

```json Example theme={null}
{
  "unit": "percent",
  "value": 75
}
```
