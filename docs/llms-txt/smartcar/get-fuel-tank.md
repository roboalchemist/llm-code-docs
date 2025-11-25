# Source: https://smartcar.com/docs/api-reference/get-fuel-tank.md

# Fuel Tank

> Returns the status of the fuel remaining in the vehicle’s fuel tank.

<Warning>
  The Vehicles API v2.0 will be deprecated by **Q3 of 2026**. We recommend migrating to the [latest version](/api-reference/vehicles-api-intro) as soon as possible to ensure continued support and access to new features.
</Warning>

## Permission

`read_fuel`

<Note>
  This endpoint may return `null` values for vehicles sold in Europe. Please see the [Notes](/api-reference/get-fuel-tank#notes) section for details.
</Note>

## Request

**Path**

<Snippet file="api-reference/path-vehicle-id.mdx" />

<RequestExample>
  <Snippet file="api-reference/core-sdk-methods/get-fuel-tank.mdx" />
</RequestExample>

## Response

<ResponseField name="percentRemaining" type="number | null">
  The remaining level of fuel in the tank as a percentage.
</ResponseField>

<ResponseField name="amountRemaining" type="number | null" default="liters">
  The amount of fuel in the tank.
</ResponseField>

<ResponseField name="range" type="number | null" default="kilometers">
  The estimated remaining distance the car can travel.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
    "amountRemaining": 53.2,
    "percentRemaining": 0.3,
    "range": 40.5
  }
  ```
</ResponseExample>

## Notes

The table below indicates values Smartcar attempts to retrieve from vehicles sold in Europe.

|                                      | `range` | `percentRemaining` | `amountRemaining` |
| ------------------------------------ | ------- | ------------------ | ----------------- |
| Audi                                 | ✅       | ✅                  |                   |
| BMW, MINI                            | ✅       | ✅                  | ✅                 |
| Citroen, DS, Opel, Peugeot, Vauxhall | ✅       |                    | ✅                 |
| Ford                                 | ✅       | ✅                  |                   |
| Hyundai                              | ✅       |                    | ✅                 |
| Jaguar, Land Rover                   | ✅       | ✅                  |                   |
| Kia                                  | ✅       | ✅                  |                   |
| Mazda                                | ✅       | ✅                  |                   |
| Mercedes                             | ✅       | ✅                  |                   |
| Renault                              | ✅       |                    | ✅                 |
| Skoda, Volkswagen                    | ✅       | ✅                  |                   |
| Volvo                                | ✅       | ✅                  | ✅                 |
