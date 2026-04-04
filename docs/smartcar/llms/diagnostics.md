# Source: https://smartcar.com/docs/api-reference/signals/diagnostics.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Diagnostics Signals

### ABS

Signal code: `diagnostics-abs`

A diagnostic category representing the Anti-lock Braking System (ABS).

<ParamField path="status" type="string" required={false}>
  A ENUM indicating the current operational condition of the related system. (ALERT, OK)

  **Possible values:** `ALERT`, `OK`
</ParamField>

<ParamField path="description" type="string" required={false}>
  A description of the system's status, if provided by the OEM.
</ParamField>

```json Example theme={null}
{
  "status": "OK",
  "description": "ABS system functioning normally"
}
```

### Active Safety

Signal code: `diagnostics-activesafety`

Encompasses the vehicle's advanced safety technologies designed to prevent or mitigate potential accidents.

<ParamField path="status" type="string" required={false}>
  A ENUM indicating the current operational condition of the related system. (ALERT, OK)

  **Possible values:** `ALERT`, `OK`
</ParamField>

<ParamField path="description" type="string" required={false}>
  A description of the system's status, if provided by the OEM.
</ParamField>

### Airbag

Signal code: `diagnostics-airbag`

The system that monitors the vehicle's airbag readiness and functionality.

<ParamField path="status" type="string" required={false}>
  A ENUM indicating the current operational condition of the related system. (ALERT, OK)

  **Possible values:** `ALERT`, `OK`
</ParamField>

<ParamField path="description" type="string" required={false}>
  A description of the system's status, if provided by the OEM.
</ParamField>

### Brake Fluid

Signal code: `diagnostics-brakefluid`

The system that monitors the vehicle's brake fluid condition and levels.

<ParamField path="status" type="string" required={false}>
  A ENUM indicating the current operational condition of the related system. (ALERT, OK)

  **Possible values:** `ALERT`, `OK`
</ParamField>

<ParamField path="description" type="string" required={false}>
  A description of the system's status, if provided by the OEM.
</ParamField>

### DTCCount

Signal code: `diagnostics-dtccount`

The total number of active Diagnostic Trouble Codes (DTCs) currently present in the vehicle's systems.

<ParamField path="unit" type="string" required={false} />

<ParamField path="value" type="integer" required={false} />

```json Example theme={null}
{
  "unit": "count",
  "value": 2
}
```

### DTCList

Signal code: `diagnostics-dtclist`

An array containing detailed information about each active Diagnostic Trouble Code (DTC) in the vehicle.

<ParamField path="values" type="array" required={true}>
  Array of Diagnostic Trouble Code (DTC) entries.
</ParamField>

<Expandable title="Array item properties">
  <ParamField path="code" type="string" required={true}>
    The specific alphanumeric code identifying a particular diagnostic trouble code (DTC).
  </ParamField>

  <ParamField path="timestamp" type="string" required={false}>
    The precise date and time when the specific diagnostic trouble code (DTC) was first detected or logged by the vehicle's onboard diagnostic system.
  </ParamField>
</Expandable>

```json Example theme={null}
{
  "values": [
    {
      "code": "P0300",
      "timestamp": "2023-10-15T08:00:00Z"
    },
    {
      "code": "P0171",
      "timestamp": "2023-10-15T08:00:00Z"
    }
  ]
}
```

### Driver Assistance

Signal code: `diagnostics-driverassistance`

The system that monitors the vehicle's advanced driver assistance technologies.

<ParamField path="status" type="string" required={false}>
  A ENUM indicating the current operational condition of the related system. (ALERT, OK)

  **Possible values:** `ALERT`, `OK`
</ParamField>

<ParamField path="description" type="string" required={false}>
  A description of the system's status, if provided by the OEM.
</ParamField>

### EVBattery Conditioning

Signal code: `diagnostics-evbatteryconditioning`

The system that monitors the electric vehicle's high-voltage battery thermal management and conditioning.

<ParamField path="status" type="string" required={false}>
  A ENUM indicating the current operational condition of the related system. (ALERT, OK)

  **Possible values:** `ALERT`, `OK`
</ParamField>

<ParamField path="description" type="string" required={false}>
  A description of the system's status, if provided by the OEM.
</ParamField>

### EVCharging

Signal code: `diagnostics-evcharging`

The system that monitors the electric vehicle's charging processes and infrastructure.

<ParamField path="status" type="string" required={false}>
  A ENUM indicating the current operational condition of the related system. (ALERT, OK)

  **Possible values:** `ALERT`, `OK`
</ParamField>

<ParamField path="description" type="string" required={false}>
  A description of the system's status, if provided by the OEM.
</ParamField>

### EVDrive Unit

Signal code: `diagnostics-evdriveunit`

The system that monitors the electric vehicle's drive unit performance and functionality.

<ParamField path="status" type="string" required={false}>
  A ENUM indicating the current operational condition of the related system. (ALERT, OK)

  **Possible values:** `ALERT`, `OK`
</ParamField>

<ParamField path="description" type="string" required={false}>
  A description of the system's status, if provided by the OEM.
</ParamField>

### EVHVBattery

Signal code: `diagnostics-evhvbattery`

The system that monitors the electric vehicle's high-voltage battery health and performance.

<ParamField path="status" type="string" required={false}>
  A ENUM indicating the current operational condition of the related system. (ALERT, OK)

  **Possible values:** `ALERT`, `OK`
</ParamField>

<ParamField path="description" type="string" required={false}>
  A description of the system's status, if provided by the OEM.
</ParamField>

### Emissions

Signal code: `diagnostics-emissions`

The system that monitors the vehicle's exhaust emissions and pollution control mechanisms.

<ParamField path="status" type="string" required={false}>
  A ENUM indicating the current operational condition of the related system. (ALERT, OK)

  **Possible values:** `ALERT`, `OK`
</ParamField>

<ParamField path="description" type="string" required={false}>
  A description of the system's status, if provided by the OEM.
</ParamField>

### Lighting

Signal code: `diagnostics-lighting`

The system that monitors the vehicle's exterior and interior lighting functionality.

<ParamField path="status" type="string" required={false}>
  A ENUM indicating the current operational condition of the related system. (ALERT, OK)

  **Possible values:** `ALERT`, `OK`
</ParamField>

<ParamField path="description" type="string" required={false}>
  A description of the system's status, if provided by the OEM.
</ParamField>

### MIL

Signal code: `diagnostics-mil`

The system that monitors the vehicle's Malfunction Indicator Lamp (MIL) status.

<ParamField path="status" type="string" required={false}>
  A ENUM indicating the current operational condition of the related system. (ALERT, OK)

  **Possible values:** `ALERT`, `OK`
</ParamField>

<ParamField path="description" type="string" required={false}>
  A description of the system's status, if provided by the OEM.
</ParamField>

### Oil Life

Signal code: `diagnostics-oillife`

The system that monitors the vehicle's engine oil condition and remaining useful life.

<ParamField path="status" type="string" required={false}>
  A ENUM indicating the current operational condition of the related system. (ALERT, OK)

  **Possible values:** `ALERT`, `OK`
</ParamField>

<ParamField path="description" type="string" required={false}>
  A description of the system's status, if provided by the OEM.
</ParamField>

### Oil Pressure

Signal code: `diagnostics-oilpressure`

The system that monitors the vehicle's engine oil pressure and lubrication system performance.

<ParamField path="status" type="string" required={false}>
  A ENUM indicating the current operational condition of the related system. (ALERT, OK)

  **Possible values:** `ALERT`, `OK`
</ParamField>

<ParamField path="description" type="string" required={false}>
  A description of the system's status, if provided by the OEM.
</ParamField>

### Oil Temperature

Signal code: `diagnostics-oiltemperature`

The system that monitors the vehicle's engine oil temperature and thermal conditions.

<ParamField path="status" type="string" required={false}>
  A ENUM indicating the current operational condition of the related system. (ALERT, OK)

  **Possible values:** `ALERT`, `OK`
</ParamField>

<ParamField path="description" type="string" required={false}>
  A description of the system's status, if provided by the OEM.
</ParamField>

### Telematics

Signal code: `diagnostics-telematics`

The system that monitors a vehicle's connectivity

<ParamField path="status" type="string" required={false}>
  A ENUM indicating the current operational condition of the related system. (ALERT, OK)

  **Possible values:** `ALERT`, `OK`
</ParamField>

<ParamField path="description" type="string" required={false}>
  A description of the system's status, if provided by the OEM.
</ParamField>

### Tire Pressure

Signal code: `diagnostics-tirepressure`

The system that monitors tire pressure levels

<ParamField path="status" type="string" required={false}>
  A ENUM indicating the current operational condition of the related system. (ALERT, OK)

  **Possible values:** `ALERT`, `OK`
</ParamField>

<ParamField path="description" type="string" required={false}>
  A description of the system's status, if provided by the OEM.
</ParamField>

### Tire Pressure Monitoring

Signal code: `diagnostics-tirepressuremonitoring`

The status of the tire pressure monitoring system.

<ParamField path="status" type="string" required={false}>
  A ENUM indicating the current operational condition of the related system. (ALERT, OK)

  **Possible values:** `ALERT`, `OK`
</ParamField>

<ParamField path="description" type="string" required={false}>
  A description of the system's status, if provided by the OEM.
</ParamField>

### Transmission

Signal code: `diagnostics-transmission`

The system that monitors the vehicle's transmission

<ParamField path="status" type="string" required={false}>
  A ENUM indicating the current operational condition of the related system. (ALERT, OK)

  **Possible values:** `ALERT`, `OK`
</ParamField>

<ParamField path="description" type="string" required={false}>
  A description of the system's status, if provided by the OEM.
</ParamField>

### Washer Fluid

Signal code: `diagnostics-washerfluid`

The system that monitors the vehicle's washer fluid reservoir

<ParamField path="status" type="string" required={false}>
  A ENUM indicating the current operational condition of the related system. (ALERT, OK)

  **Possible values:** `ALERT`, `OK`
</ParamField>

<ParamField path="description" type="string" required={false}>
  A description of the system's status, if provided by the OEM.
</ParamField>

### Water In Fuel

Signal code: `diagnostics-waterinfuel`

The system that monitors the presence of water in the vehicle's fuel system

<ParamField path="status" type="string" required={false}>
  A ENUM indicating the current operational condition of the related system. (ALERT, OK)

  **Possible values:** `ALERT`, `OK`
</ParamField>

<ParamField path="description" type="string" required={false}>
  A description of the system's status, if provided by the OEM.
</ParamField>
