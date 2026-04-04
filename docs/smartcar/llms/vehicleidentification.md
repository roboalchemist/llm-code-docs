# Source: https://smartcar.com/docs/api-reference/signals/vehicleidentification.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# VehicleIdentification Signals & Attributes

## Signals

### Nickname

Signal code: `vehicleidentification-nickname`

Name personally assigned by the vehicle by the owner.

<ParamField path="value" type="string" required={false} />

## Attributes

### Exterior Color

Signal code: `vehicleidentification-exteriorcolor`

The exterior paint color of the vehicle as specified by the manufacturer.

<ParamField path="value" type="string" required={false} />

### VIN

Signal code: `vehicleidentification-vin`

Vehicle Identification Number - A unique 17-character alphanumeric code assigned to each vehicle that serves as its identifier. Contains encoded information about the vehicle's manufacturer, model, features, and production details.

<ParamField path="value" type="string" required={false} />
