# Source: https://smartcar.com/docs/api-reference/get-lock-status.md

# Lock Status

> Returns the lock status for a vehicle and the open status of its doors, windows, storage units, sunroof and charging port where available.

<Warning>
  The Vehicles API v2.0 will be deprecated by **Q3 of 2026**. We recommend migrating to the [latest version](/api-reference/vehicles-api-intro) as soon as possible to ensure continued support and access to new features.
</Warning>

## Permission

`read_security`

## Request

**Path**

<Snippet file="api-reference/path-vehicle-id.mdx" />

<RequestExample>
  <Snippet file="api-reference/core-sdk-methods/get-lock-status.mdx" />
</RequestExample>

## Response

<ResponseField name="isLocked" type="boolean">
  Indicates the current lock status of the vehicle as reported by the OEM.
</ResponseField>

<ResponseField name="doors" type="[object]">
  An array of the open status of the vehicle's doors.

  <Expandable title="doors">
    <ResponseField name="type" type="string">
      The location of the door.
    </ResponseField>

    <ResponseField name="status" type="string">
      Indicates the current state of the vehicle's door.
      `UNKNOWN` indicates the vehicle supports this status, but did not provide a valid status for the request
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="windows" type="[object]">
  An array of the open status of the vehicle's windows.

  <Expandable title="windows">
    <ResponseField name="type" type="string">
      The location of the window.
    </ResponseField>

    <ResponseField name="status" type="string">
      Indicates the current state of the vehicle's window.
      `UNKNOWN` indicates the vehicle supports this status, but did not provide a valid status for the request
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="sunroof" type="[object]">
  An array of the open status of the vehicle's sunroofs.

  <Expandable title="sunroofs">
    <ResponseField name="type" type="string">
      The location of the sunroof.
    </ResponseField>

    <ResponseField name="status" type="string">
      Indicates the current state of the vehicle's sunroof.
      `UNKNOWN` indicates the vehicle supports this status, but did not provide a valid status for the request
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="storage" type="[object]">
  An array of the open status of the vehicle's storages.
  For internal combustion and plug-in hybrid vehicles front refers to the engine hood.
  For battery vehicles, this will be the front trunk.

  <Expandable title="storage">
    <ResponseField name="type" type="string">
      The location of the storage.
    </ResponseField>

    <ResponseField name="status" type="string">
      Indicates the current state of the vehicle's storage.
      `UNKNOWN` indicates the vehicle supports this status, but did not provide a valid status for the request
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="chargingPort" type="[object]">
  An array of the open status of the vehicle's charging port.

  <Expandable title="chargingPort">
    <ResponseField name="type" type="string">
      The location of the charging port.
    </ResponseField>

    <ResponseField name="status" type="string">
      Indicates the current state of the vehicle's charging port.
      `UNKNOWN` indicates the vehicle supports this status, but did not provide a valid status for the request
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
  	"isLocked" : false,
  	"doors" : [
  		{"type": "frontLeft" , "status" : "CLOSED"},
  		{"type": "frontRight" , "status" : "OPEN"},
  		{"type": "backRight" , "status" : "CLOSED"},
  		{"type": "backLeft" , "status" : "CLOSED"}
  	],
  	"windows" : [
  		{"type": "frontLeft" , "status" : "CLOSED"},
  		{"type": "frontRight" , "status" : "CLOSED"},
  		{"type": "backRight" , "status" : "UNKNOWN"},
  		{"type": "backLeft" , "status" : "CLOSED"}
  	],
  	"sunroof" : [
  		{"type": "sunroof" , "status" : "CLOSED"}
  	], 	
  	"storage" : [
  		{"type": "rear" , "status" : "UNKNOWN"},
  		{"type": "front" , "status" : "CLOSED"}
  	],
  	"chargingPort" : [ 
  		{"type" : "chargingPort", "status" : "CLOSED" } 
  	]
  }
  ```
</ResponseExample>

# Notes

* The open status array(s) will be empty if a vehicle has partial support.
* The request will error if `lockStatus` can not be retrieved from the vehicle or the brand is not supported.
