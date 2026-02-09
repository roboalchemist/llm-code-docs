# Source: https://smartcar.com/docs/api-reference/signals/closure.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Closure Signals

### Doors

Signal code: `closure-doors`

An object containing information about the vehicle's doors.

<ParamField path="values" type="array" required={true}>
  An array of objects containing information about the state of the vehicle's doors.
</ParamField>

<Expandable title="Array item properties">
  <ParamField path="row" type="number" required={false}>
    Represents the row position of a specific door, front to back (0 to Doors.rowCount-1).
  </ParamField>

  <ParamField path="column" type="number" required={false}>
    Represents the column position of a specific door, left to right (0 to Door.ColumnCount-1).
  </ParamField>

  <ParamField path="isOpen" type="boolean" required={false}>
    Indicates if the door is open.
  </ParamField>

  <ParamField path="isLocked" type="boolean" required={false}>
    Indicates if the door is locked.
  </ParamField>
</Expandable>

<ParamField path="rowCount" type="number" required={false}>
  Indicates the total number of door rows present in the vehicle. This field, along with columnCount, provides information about the vehicle's door layout and the total number of doors available.
</ParamField>

<ParamField path="columnCount" type="number" required={false}>
  Indicates the total number of door columns present in the vehicle. This field, along with rowCount, provides information about the vehicle's door layout and the total number of doors available.
</ParamField>

```json Example theme={null}
{
  "values": [
    {
      "row": 0,
      "column": 0,
      "isOpen": false,
      "isLocked": true
    },
    {
      "row": 0,
      "column": 1,
      "isOpen": false,
      "isLocked": true
    }
  ],
  "rowCount": 2,
  "columnCount": 2
}
```

### Engine Cover

Signal code: `closure-enginecover`

An object containing information about the state of the vehicle's engine cover for ICE or PHEV vehicles.

<ParamField path="isOpen" type="boolean" required={false}>
  Indicates if the trunk is open.
</ParamField>

### Front Trunk

Signal code: `closure-fronttrunk`

An object containing information about the state of the vehicle's front trunk.

<ParamField path="isOpen" type="boolean" required={false}>
  Indicates if the trunk is open.
</ParamField>

<ParamField path="isLocked" type="boolean" required={false}>
  Indicates if the trunk is locked.
</ParamField>

### Is Locked

Signal code: `closure-islocked`

A boolean value indicating whether the vehicle's closures are currently locked.

<ParamField path="value" type="boolean" required={false} />

### Rear Trunk

Signal code: `closure-reartrunk`

An object containing information about the state of the vehicle's rear trunk.

<ParamField path="isOpen" type="boolean" required={false}>
  Indicates if the trunk is open.
</ParamField>

<ParamField path="isLocked" type="boolean" required={false}>
  Indicates if the trunk is locked.
</ParamField>

### Sunroof

Signal code: `closure-sunroof`

An object containing information about the state of the vehicle's sunroof.

<ParamField path="isOpen" type="boolean" required={false}>
  Indicates if the trunk is open.
</ParamField>

### Windows

Signal code: `closure-windows`

An object containing information about the vehicle's windows.

<ParamField path="values" type="array" required={true}>
  An array of objects, where each object represents a specific window in the vehicle.
</ParamField>

<Expandable title="Array item properties">
  <ParamField path="row" type="number" required={true}>
    Represents the row position of a specific window, front to back (0 to Windows.rowCount-1).
  </ParamField>

  <ParamField path="column" type="number" required={true}>
    Represents the column position of a specific window, left to right (0 to Windows.columnCount-1).
  </ParamField>

  <ParamField path="isOpen" type="boolean" required={true}>
    Indicates if the window is open.
  </ParamField>
</Expandable>

<ParamField path="rowCount" type="number" required={false}>
  Indicates the total number of window rows present in the vehicle. This field, along with columnCount, provides information about the vehicle's window layout and the total number of windows available.
</ParamField>

<ParamField path="columnCount" type="number" required={false}>
  Indicates the total number of window columns present in the vehicle. This field, along with rowCount, provides information about the vehicle's window layout and the total number of windows available.
</ParamField>

```json Example theme={null}
{
  "values": [
    {
      "row": 0,
      "column": 0,
      "isOpen": false
    },
    {
      "row": 0,
      "column": 1,
      "isOpen": false
    }
  ],
  "rowCount": 2,
  "columnCount": 2
}
```
