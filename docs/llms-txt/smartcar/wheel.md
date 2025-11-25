# Source: https://smartcar.com/docs/api-reference/signals/wheel.md

# Wheel Signals & Attributes

## Signals

### Tires

Signal code: `wheel-tires`

An array of objects, where each object represents a specific wheel on the vehicle.

<ParamField path="values" type="array" required={true}>
  An array of objects containing information about the vehicle's wheels.
</ParamField>

<Expandable title="Array item properties">
  <ParamField path="row" type="number" required={true}>
    Represents the row position of a specific wheel, front to back (0 to Wheels.rowCount-1).
  </ParamField>

  <ParamField path="column" type="number" required={true}>
    Represents the column position of a specific wheel, left to right (0 to Wheels.columnCount-1).
  </ParamField>

  <ParamField path="tirePressure" type="number" required={true}>
    Indicates the current tire pressure of the wheel.
  </ParamField>
</Expandable>

<ParamField path="rowCount" type="number" required={false}>
  Indicates the total number of wheel rows present in the vehicle. This signal, along with WheelColumnCount, provides information about the vehicle's wheel layout and the total number of wheels available.
</ParamField>

<ParamField path="columnCount" type="number" required={false}>
  Indicates the total number of wheel columns present in the vehicle. This signal, along with WheelRowCount, provides information about the vehicle's wheel layout and the total number of wheels available.
</ParamField>

## Attributes

### Style

Signal code: `wheel-style`

Wheel style of the vehicle.

<ParamField path="value" type="string" required={false} />
