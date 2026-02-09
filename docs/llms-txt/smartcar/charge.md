# Source: https://smartcar.com/docs/api-reference/signals/charge.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Charge Signals

### Amperage

Signal code: `charge-amperage`

Current amperage flowing to the electric vehicle during a charging session, measured in amps.

<ParamField path="unit" type="string" required={false} />

<ParamField path="value" type="number" required={false} />

```json Example theme={null}
{
  "unit": "ampere",
  "value": 32
}
```

### Max Amperage

Signal code: `charge-amperagemax`

The maximum available amps available to charge.

<ParamField path="unit" type="string" required={false} />

<ParamField path="value" type="number" required={false} />

```json Example theme={null}
{
  "unit": "ampere",
  "value": 48
}
```

### Amperage Requested

Signal code: `charge-amperagerequested`

The requested amps to charge the vehicle.

<ParamField path="unit" type="string" required={false} />

<ParamField path="value" type="number" required={false} />

```json Example theme={null}
{
  "unit": "ampere",
  "value": 32
}
```

### Charge Limits

Signal code: `charge-chargelimits`

Object containing the default (global) charge limit configuration and configurations based on location, and charge connector type

<ParamField path="values" type="array" required={false}>
  Array of charge limit configurations, each representing a different context (global, location-based, or connector-based).
</ParamField>

<Expandable title="Array item properties">
  <ParamField path="type" type="string" required={false}>
    The type of charge limit configuration. "global" applies universally, "location" is specific to a location, and "connector" is specific to a charging connector type.

    **Possible values:** `GLOBAL`, `LOCATION`, `CONNECTOR`
  </ParamField>

  <ParamField path="limit" type="number" required={false}>
    The maximum state of charge (SoC) limit configured for this context, expressed as a percentage (0-100).
  </ParamField>

  <ParamField path="condition" type="object" required={false}>
    Additional context for location or connector-based charge limits. Null for global configurations.
  </ParamField>

  <Expandable title="condition properties">
    <ParamField path="name" type="string" required={false}>
      Name of the location or charging station where this limit applies.
    </ParamField>

    <ParamField path="address" type="string" required={false}>
      Street address of the location where this limit applies.
    </ParamField>

    <ParamField path="latitude" type="number" required={false}>
      Geographic latitude coordinate of the location where this limit applies.
    </ParamField>

    <ParamField path="longitude" type="number" required={false}>
      Geographic longitude coordinate of the location where this limit applies.
    </ParamField>

    <ParamField path="connectorType" type="string" required={false}>
      Type of charging connector where this limit applies (only used when type is "connector").
    </ParamField>
  </Expandable>
</Expandable>

<ParamField path="activeLimit" type="number" required={false}>
  Maximum state of charge (SoC) limit currently being applied to the vehicle, expressed as a percentage (0-100). This field will contain a numeric value when the vehicle is plugged in and charging, indicating which of the configured charge limits is currently active. When the vehicle is not plugged in or the active limit cannot be determined, this field will be null.
</ParamField>

<ParamField path="unit" type="string" required={false}>
  The unit of measurement for the charge limits.
</ParamField>

```json Example theme={null}
{
  "values": [
    {
      "type": "global",
      "limit": 80,
      "condition": null
    },
    {
      "type": "location",
      "limit": 90,
      "condition": {
        "name": "Home",
        "address": "123 Main St",
        "latitude": 37.7749,
        "longitude": -122.4194
      }
    }
  ],
  "activeLimit": 100,
  "unit": "percent"
}
```

### Charge Port Status Color

Signal code: `charge-chargeportstatuscolor`

Current status indicator color displayed on or around the vehicle's charging port.

<ParamField path="value" type="string" required={false}>
  **Possible values:** `GREEN`, `BLUE`, `ORANGE`, `ETC`
</ParamField>

```json Example theme={null}
{
  "value": "GREEN"
}
```

### Charge Rate

Signal code: `charge-chargerate`

Current rate at which range is being added to the vehicle during an active charging session

<ParamField path="unit" type="string" required={false} />

<ParamField path="value" type="number" required={false} />

```json Example theme={null}
{
  "unit": "km/h",
  "value": 25
}
```

### Records

Signal code: `charge-chargerecords`

Collection of historical charging session data stored by the vehicle.

<ParamField path="values" type="array" required={true}>
  Array of individual charging session records, each representing a completed or ongoing charging event.
</ParamField>

<Expandable title="Array item properties">
  <ParamField path="id" type="string" required={false}>
    Unique OEM identifier assigned to the specific charging session.
  </ParamField>

  <ParamField path="cost" type="object" required={false}>
    Detailed breakdown of the charging session costs.
  </ParamField>

  <Expandable title="cost properties">
    <ParamField path="currency" type="string" required={false}>
      Three-letter currency code (e.g., "USD", "EUR") representing the monetary unit used for the charging session transaction.
    </ParamField>

    <ParamField path="energyAmount" type="number" required={false}>
      Cost specifically for the electrical energy consumed during the charging session.
    </ParamField>

    <ParamField path="otherAmount" type="number" required={false}>
      Additional non-energy related charges (e.g., connection fees, parking fees) associated with the charging session.
    </ParamField>
  </Expandable>

  <ParamField path="endTime" type="string" required={false}>
    ISO-8601 timestamp marking when a charging session was completed or terminated.
  </ParamField>

  <ParamField path="location" type="object" required={false}>
    Details about where the charging session took place.
  </ParamField>

  <Expandable title="location properties">
    <ParamField path="name" type="string" required={false}>
      Descriptive name of the charging location (e.g., "Home Charger", "Public Station 123").
    </ParamField>

    <ParamField path="address" type="string" required={false}>
      Street address of the charging location.
    </ParamField>

    <ParamField path="latitude" type="number" required={false}>
      Geographic latitude coordinate of the charging location.
    </ParamField>

    <ParamField path="longitude" type="number" required={false}>
      Geographic longitude coordinate of the charging location.
    </ParamField>
  </Expandable>

  <ParamField path="startTime" type="string" required={false}>
    ISO-8601 timestamp marking when a charging session was initiated.
  </ParamField>

  <ParamField path="energyAdded" type="number" required={false}>
    Total amount of electrical energy delivered during the charging session, measured in kilowatt-hours (kWh).
  </ParamField>

  <ParamField path="connectorType" type="string" required={false}>
    Identifier for the type of charging connector used (e.g., "J1772", "CCS", "CHAdeMO").
  </ParamField>

  <ParamField path="isPublicCharger" type="boolean" required={false}>
    Indicates whether the charging occurred at a public charging station (true) or private location (false).
  </ParamField>

  <ParamField path="endStateOfCharge" type="number" required={false}>
    Battery's state of charge (0-100%) at the end of the charging session.
  </ParamField>

  <ParamField path="startStateOfCharge" type="number" required={false}>
    Battery's state of charge (0-100%) at the start of the charging session.
  </ParamField>
</Expandable>

```json Example theme={null}
{
  "values": [
    {
      "id": "CHG123",
      "cost": {
        "currency": "USD",
        "otherAmount": 2,
        "energyAmount": 10.5
      },
      "endTime": "2023-10-15T08:00:00Z",
      "location": {
        "name": "Home Charger",
        "address": "123 Main St",
        "latitude": 37.7749,
        "longitude": -122.4194
      },
      "startTime": "2023-10-15T00:00:00Z",
      "energyAdded": 40.5,
      "connectorType": "J1772",
      "isPublicCharger": false,
      "endStateOfCharge": 90,
      "startStateOfCharge": 20
    }
  ]
}
```

### Charge Timers

Signal code: `charge-chargetimers`

Object containing the default (global) charge timer configuration and configurations based on location, and charge connector type

<ParamField path="values" type="array" required={false}>
  Array of charging timer configurations, each defining either scheduled charging times or departure times.
</ParamField>

<Expandable title="Array item properties">
  <ParamField path="type" type="string" required={false}>
    The type of charging timer configuration. "global" applies universally, "location" is specific to a location, and "connector" is specific to a charging connector type.

    **Possible values:** `GLOBAL`, `LOCATION`, `CONNECTOR`
  </ParamField>

  <ParamField path="condition" type="object" required={false}>
    Additional context for location or connector-based charging timers. Null for global configurations.
  </ParamField>

  <Expandable title="condition properties">
    <ParamField path="name" type="string" required={false}>
      Name of the location or charging station where this timer configuration applies.
    </ParamField>

    <ParamField path="address" type="string" required={false}>
      Street address of the location where this timer configuration applies.
    </ParamField>

    <ParamField path="latitude" type="number" required={false}>
      Geographic latitude coordinate of the location where this timer configuration applies.
    </ParamField>

    <ParamField path="longitude" type="number" required={false}>
      Geographic longitude coordinate of the location where this timer configuration applies.
    </ParamField>

    <ParamField path="connectorType" type="string" required={false}>
      Type of charging connector where this timer configuration applies (only used when type is "connector").
    </ParamField>
  </Expandable>

  <ParamField path="schedules" type="array" required={false}>
    Array of time windows during which charging should occur, defined by start and end times on specific days.
  </ParamField>

  <Expandable title="Array item properties">
    <ParamField path="end" type="string" required={false}>
      The time when the charging window should end, in 24-hour format (HH:MM:SS).
    </ParamField>

    <ParamField path="days" type="array" required={false}>
      List of days of the week when this charging schedule should be active.
    </ParamField>

    <ParamField path="start" type="string" required={false}>
      The time when the charging window should begin, in 24-hour format (HH:MM:SS).
    </ParamField>
  </Expandable>

  <ParamField path="departureTimers" type="array" required={false}>
    Array of target departure times when the vehicle should be charged and ready to use.
  </ParamField>

  <Expandable title="Array item properties">
    <ParamField path="days" type="array" required={false}>
      List of days of the week when this departure timer should be active.
    </ParamField>

    <ParamField path="time" type="string" required={false}>
      The target time when the vehicle should be fully charged and ready, in 24-hour format (HH:MM:SS).
    </ParamField>
  </Expandable>

  <ParamField path="isOEMOptimizationEnabled" type="boolean" required={false}>
    Indicates whether the vehicle manufacturer's smart charging optimization features are enabled for this timer configuration.
  </ParamField>
</Expandable>

### Charger Phases

Signal code: `charge-chargerphases`

The number of phases available from the connected charger.

<ParamField path="value" type="integer" required={false} />

```json Example theme={null}
{
  "value": 3
}
```

### Charging Connector Type

Signal code: `charge-chargingconnectortype`

Identifier for the type of charging connector/inlet equipped on the vehicle.

<ParamField path="value" type="string" required={false} />

```json Example theme={null}
{
  "value": "J1772"
}
```

### Detailed Charging Status

Signal code: `charge-detailedchargingstatus`

String value that provides detailed information about the current state of the charging process.

<ParamField path="value" type="string" required={true}>
  **Possible values:** `CHARGING`, `NOT_CHARGING`, `FULLY_CHARGED`
</ParamField>

```json Example theme={null}
{
  "value": "CHARGING"
}
```

### Energy Added

Signal code: `charge-energyadded`

Cumulative amount of electrical energy delivered to the vehicle during the current or most recent charging session, measured in kilowatt-hours (kWh).

<ParamField path="unit" type="string" required={false} />

<ParamField path="value" type="number" required={false} />

```json Example theme={null}
{
  "unit": "kWh",
  "value": 25.5
}
```

### Fast Charger Type

Signal code: `charge-fastchargertype`

Identifier for the specific DC fast charging standard currently connected to the vehicle. Indicates the protocol being used for high-power charging

<ParamField path="value" type="string" required={false} />

```json Example theme={null}
{
  "value": "CCS"
}
```

### Is Charging

Signal code: `charge-ischarging`

Boolean indicator that shows whether the electric vehicle is actively receiving power from a charging station or outlet.

<ParamField path="value" type="boolean" required={false} />

```json Example theme={null}
{
  "value": true
}
```

### Is Charging Cable Connected

Signal code: `charge-ischargingcableconnected`

Boolean indicator that shows whether a charging cable is physically connected to the vehicle's charging port.

<ParamField path="value" type="boolean" required={false} />

```json Example theme={null}
{
  "value": true
}
```

### Is Charging Cable Latched

Signal code: `charge-ischargingcablelatched`

Boolean indicator that shows whether the charging cable is securely locked to the vehicle's charging port.

<ParamField path="value" type="boolean" required={false} />

```json Example theme={null}
{
  "value": true
}
```

### Is Charging Port Flap Open

Signal code: `charge-ischargingportflapopen`

Boolean indicator that shows whether the vehicle's charging port access door or flap is currently open.

<ParamField path="value" type="boolean" required={false} />

```json Example theme={null}
{
  "value": true
}
```

### Is Fast Charger Present

Signal code: `charge-isfastchargerpresent`

Boolean indicator that shows whether the vehicle is connected to a DC fast charging station.

<ParamField path="value" type="boolean" required={false} />

```json Example theme={null}
{
  "value": true
}
```

### Time To Complete

Signal code: `charge-timetocomplete`

Estimated time remaining until the charging session reaches the activeLimit in minutes.

<ParamField path="unit" type="string" required={false} />

<ParamField path="value" type="number" required={false} />

```json Example theme={null}
{
  "value": 45
}
```

### Voltage

Signal code: `charge-voltage`

Current voltage level being supplied to the electric vehicle during a charging session, measured in volts.

<ParamField path="unit" type="string" required={false} />

<ParamField path="value" type="number" required={false} />

```json Example theme={null}
{
  "unit": "volts",
  "value": 240
}
```

### Wattage

Signal code: `charge-wattage`

Current power delivery rate to the electric vehicle during a charging session, measured in watts.

<ParamField path="unit" type="string" required={false} />

<ParamField path="value" type="number" required={false} />

```json Example theme={null}
{
  "unit": "watts",
  "value": 250
}
```
