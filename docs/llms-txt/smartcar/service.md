# Source: https://smartcar.com/docs/api-reference/signals/service.md

# Service Signals

### Is In Service

Signal code: `service-isinservice`

A boolean that Indicates if the vehicle is currently in service

<ParamField path="value" type="boolean" required={false}>
  Boolean indicating if the vehicle is in service
</ParamField>

```json Example theme={null}
{
  "value": false
}
```

### Records

Signal code: `service-records`

An array containing records of service that has been performed on the vehicle.

<ParamField path="values" type="array" required={true}>
  An array of service records.
</ParamField>

<Expandable title="Array item properties">
  <ParamField path="id" type="string" required={false}>
    A unique identifier for the service record.
  </ParamField>

  <ParamField path="cost" type="object" required={false}>
    The monetary amount billed by the service provider for the service.
  </ParamField>

  <Expandable title="cost properties">
    <ParamField path="amount" type="number" required={false}>
      The numerical portion of the amount.
    </ParamField>

    <ParamField path="currency" type="string" required={false}>
      The currency for the amount.
    </ParamField>
  </Expandable>

  <ParamField path="time" type="string" required={false}>
    The timestamp of when the service occurred.
  </ParamField>

  <ParamField path="tasks" type="array" required={false}>
    An array containing information about tasks performed as part of the service.
  </ParamField>

  <Expandable title="Array item properties">
    <ParamField path="id" type="string" required={false}>
      A unique identifier for the task.
    </ParamField>

    <ParamField path="description" type="string" required={false}>
      A description of the task that was performed.
    </ParamField>
  </Expandable>

  <ParamField path="details" type="array" required={false}>
    An array containing additional details about the service.
  </ParamField>

  <Expandable title="Array item properties">
    <ParamField path="id" type="string" required={false}>
      A unique identifier for the additional detail item.
    </ParamField>

    <ParamField path="description" type="string" required={false}>
      A text string describing the additional detail item.
    </ParamField>
  </Expandable>

  <ParamField path="odometer" type="number" required={false}>
    The vehicle's odometer at the time of the service.
  </ParamField>
</Expandable>

```json Example theme={null}
{
  "values": [
    {
      "id": "SVC-2024-001",
      "cost": {
        "amount": 150,
        "currency": "USD"
      },
      "time": "2024-01-15T14:30:00Z",
      "tasks": [
        {
          "id": "TSK-001",
          "description": "Oil Change"
        }
      ],
      "details": [
        {
          "id": "DTL-001",
          "description": "5W-30 Synthetic Oil Used"
        }
      ],
      "odometer": 50000
    }
  ]
}
```
