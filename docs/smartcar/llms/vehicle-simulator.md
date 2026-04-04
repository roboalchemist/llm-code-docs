# Source: https://smartcar.com/docs/help/vehicle-simulator.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Vehicle Simulator

> Learn about what to expect from Vehicle Simulator and how it compares to Live mode.

Vehicle Simulator allows you to test your application in realistic scenarios with a simulated Smartcar-compatible vehicle. Simulator responds to API requests just like a real vehicle. You can choose a simulated trip for your vehicle to take, and track it over time.

You can use the simulator for initial testing before you have a real vehicle to connect, or as part of an end-to-end testing suite.

## Creating a Simulated Vehicle

Simulated vehicles are managed in the Smartcar Dashboard.

Select "Add a vehicle" and select a vehicle by Make, Model, and Year, or provide a VIN for a US-based vehicle that you want to simulate. You'll be able to preview the API endpoints that are supported for the vehicle model you select.

Once you create your simulated vehicle, you'll select a simulated trip profile that the vehicle will follow. This profile can run automatically over time, or you can manually select a stage of the trip for the vehicle in the Dashboard.

## Connecting a Simulated Vehicle

Simulated vehicles generate a special set of credentials that mimic what a real-world vehicle owner would have. You'll use these credentials to establish a vehicle connection through the same Smartcar Connect flow that you will use for live vehicles.

In order for Connect to know you're using credentials generated from Vehicle Simulator, you'll need to pass `mode=simulated` in the [Connect URL](/connect/redirect-to-connect).

<Info>
  Please ensure you're passing or changing the country flag for Connect based on the region you've created your vehicle for.
  Failure to do so will result in an invalid credential error on login. You can read more about country selection for Connect [here](/connect/advanced-config/country-flag).
</Info>

<AccordionGroup>
  <Accordion title="SDKs">
    You can set `mode` in the auth client builder to `simulated`.
  </Accordion>

  <Accordion title="No SDK">
    You'll need to pass `mode=simulated` in the Connect URL
  </Accordion>
</AccordionGroup>

## Making requests to a Simulated Vehicle

Once your simulated vehicle is connected, you can make API requests to it just as you would a real vehicle.

Supported endpoints for the simulated vehicle will send responses with simulated data - unsupported endpoints will return errors just as they would with a real vehicle.

You can also send commands to simulated vehicles, like start/stop charge or lock/unlock doors. These requests will send responses that mimic that of a real vehicle, but the vehicle state will continue to reflect the simulated trip that was selected.

## Expected Responses

### Data

| Permission          | Request Method / Path | Example Response                                                                            |
| ------------------- | --------------------- | ------------------------------------------------------------------------------------------- |
| `read_engine_oil`   | GET /engine/oil       | `{ lifeRemaining: 0.35 }`                                                                   |
| `read_battery`      | GET /battery          | `{ percentRemaining: 0.3, range: 40.5 }`                                                    |
| `read_battery`      | GET /battery/capacity | `{ capacity: 28 }`                                                                          |
| `read_charge`       | GET /charge           | `{ isPluggedIn: true, state: 'FULLY_CHARGED' }`                                             |
| `read_charge`       | GET /charge/limit     | `{ limit: 1 }`                                                                              |
| `read_fuel`         | GET /fuel             | `{ amountRemaining: 53.2, percentRemaining: 0.3, range: 40.5 }`                             |
| `read_location`     | GET /location         | `{ latitude: 37.4292, longitude: 122.1382 }`                                                |
| `read_odometer`     | GET /odometer         | `{ distance: 104.32 }`                                                                      |
| `read_tires`        | GET /tires/pressure   | `{ backLeft: 219.3, backRight: 219.3, frontLeft: 219.3, frontRight: 219.3 }`                |
| `read_vehicle_info` | GET /                 | `{ id: 36ab27d0-fd9d-4455-823a-ce30af709ffc, make: "TESLA", model: "Model S", year: 2014 }` |
| `read_vin`          | GET /vin              | `{ vin: 1234A67Q90F2T4567 }`                                                                |

### Commands

Below are the various action requests that can be made to simulated vehicles, and what responses to expect based on the simulated vehicle's current state or simulator support.

Not listed here are the standard API errors that will be returned if the vehicle does not support the capability or the application has not been granted permission.

| Permission         | Request (method / path) | Action request | Vehicle state                     | Response                                                       |
| ------------------ | ----------------------- | -------------- | --------------------------------- | -------------------------------------------------------------- |
| `control_security` | POST /security          | `LOCK`         | Parked / Charging                 | `{ status: "success" }`                                        |
| `control_security` | POST /security          | `UNLOCK`       | Parked / Charging                 | `{ status: "success" }`                                        |
| `control_security` | POST /security          | `LOCK`         | Driving                           | `{ type: VEHICLE_STATE, code: IN_MOTION }`                     |
| `control_security` | POST /security          | `UNLOCK`       | Driving                           | `{ type: VEHICLE_STATE, code: IN_MOTION }`                     |
| `control_charge`   | POST /charge            | `START`        | Charging                          | `{ status: "success" }`                                        |
| `control_charge`   | POST /charge            | `STOP`         | Charging                          | `{ status: "success" }`                                        |
| `control_charge`   | POST /charge            | `STOP`         | Parked / Driving (not plugged in) | `{ type: VEHICLE_STATE, code: CHARGING_PLUG_NOT_CONNECTED }`   |
| `control_charge`   | POST /charge            | `START`        | Parked / Driving (not plugged in) | `{ type: VEHICLE_STATE, code: CHARGING_PLUG_NOT_CONNECTED }`   |
| `control_charge`   | POST /charge-limit      | `<limit>`      | Charging                          | `{ "type": "COMPATIBILITY", "code": "SMARTCAR_NOT_CAPABLE", }` |
| `control_charge`   | POST /charge-limit      | `<limit>`      | Parked / Driving (not plugged in) | `{ type: VEHICLE_STATE, code: CHARGING_PLUG_NOT_CONNECTED }`   |

### Errors

| Event                                                                                                               | Error response                                                                     | Suggested resolution                                                                                                                                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Making an API request to a simulated vehicle before connecting the vehicle to your application via Smartcar Connect | `{ type: "PERMISSION", statusCode: 403, resolution: "REAUTHENTICATE" }`            | Locate the 'Connect Credentials' button at the top of the simulation screen in the Smartcar Dashboard for your simulated vehicle. There you will find the credentials necessary to connect the vehicle to your application as well as instructions for doing so through Smartcar Connect. |
| Making an API request to a simulated vehicle before a simulation has been started on Dashboard                      | `{ type: "CONNECTED_SERVICES_ACCOUNT", code: "ACCOUNT_ISSUE", statusCode: 400 }`   | Open the Simulator tab in the Smartcar Dashboard and navigate to your target vehicle. If you haven't yet selected a vehicle state, do so now, and then start the simulation using the 'Play' button on the simulation screen.                                                             |
| Making an API request to a simulated vehicle that is not associated with  your application                          | `{ type: "CONNECTED_SERVICES_ACCOUNT", code: "VEHICLE_MISSING", statusCode: 400 }` | Ensure the simulated vehicle you are making requests to has been created in the Simulator within your Smartcar Dashboard.                                                                                                                                                                 |

## Mode Comparison

| <div style={{ width:180 }} />Feature | <div style={{ width:80 }} />Simulator | <div style={{ width:80 }} />Live |   |
| ------------------------------------ | ------------------------------------- | -------------------------------- | - |
| Single Select                        | ✅                                     | ✅                                |   |
| Brand Select                         | ✅                                     | ✅                                |   |
| Compatibility API\*                  | ✅                                     | ✅                                |   |
| `control_security`                   | ✅                                     | ✅                                |   |
| `control_charge`                     | ✅                                     | ✅                                |   |
| Make-Specific Endpoints              | ❌                                     | ✅                                |   |
| Scheduled Webhooks                   | ❌                                     | ✅                                |   |
| Event Based Webhooks\*\*             | ❌                                     | ✅                                |   |

<sub>
  <sup>
    \*When a real VIN is used either through `VIN@smartcar` for `test` mode, or generating a simulated vehicle with a real VIN.
  </sup>

  <sup>
    0SC and 1SC prefixed VINs will not work.
  </sup>
</sub>

<sub>
  <sup>
    \*\*For supported brands - Toyota, Ford and Tesla.
  </sup>
</sub>

## FAQs

<AccordionGroup>
  <Accordion title="How are tokens handled?">
    Access and refresh tokens behave as they do in `live` mode:

    * Access Tokens are valid for 2 hours
    * Refresh Tokens are valid for 60 days.
    * Using a refresh token to fetch an new access/refresh token pair will invalidate the refresh token that you used.

    **Reusing simulated vehicle credentials**<br />
    If you use the same simulated credentials for multiple Connect flow sessions, we'll issue a new set of tokens each time.
    This will not invalidate any existing tokens from previous logins so you'll be able to keep them refreshed in parallel without impacting the validity of the others.
  </Accordion>

  <Accordion title="Are there any limits on how many vehicles I can create?">
    The number of simulated vehicles that can be created depends on your Smartcar plan tier. Please see [here](https://smartcar.com/pricing#plans) for more information.
  </Accordion>

  <Accordion title="I'm getting an invalid credentials error when I try to sign in to a connected service account.">
    * Please check that you have launched Connect with the `mode=simulated` parameter
    * Please check that you are passing the country feature flag for the region you've set up your vehicle with.
      Please see [Country Selection](/connect/advanced-config/country-flag)for Connect for more information.
  </Accordion>
</AccordionGroup>
