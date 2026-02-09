# Source: https://smartcar.com/docs/api-reference/get-nominal-capacity.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Battery Capacity

> Returns a list of nominal rated battery capacities for a vehicle.

<Warning>
  The Vehicles API v2.0 will be deprecated by **Q3 of 2026**. We recommend migrating to the [latest version](/api-reference/vehicles-api-intro) as soon as possible to ensure continued support and access to new features.
</Warning>

<Info>
  This endpoint is only available for US and European based vehicles. Please refer to [this page](/api-reference/evs/get-battery-capacity)  if you need battery capacity for Canadian based vehicles for the time being.
</Info>

## Permission

`read_battery`

## Request

**Path**

<Snippet file="api-reference/path-vehicle-id.mdx" />

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/battery/nominal_capacity" \
  -H "Authorization: Bearer {token}" \
  -X "GET"
  ```
</RequestExample>

## Response

<ResponseField name="availableCapacities" type="[capacities Object]">
  An array of capacities Objects.

  <Expandable title="capacities">
    <ResponseField name="capacity" type="number | null" default="kWh">
      The rated nominal capacity for the vehicle's battery.
    </ResponseField>

    <ResponseField name="description" type="string | null">
      A description of the uniqueness for the nominal capacity and engine type of the vehicle in the form `{ENGINE_TYPE}:{TRIM}`, for example `"BEV:Extended Range"`.

      Engine type can be one of `BEV` or `PHEV`.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="capacity" type="Object | null">
  <Expandable title="capacity">
    <ResponseField name="nominal" type="number | null" default="kWh">
      The rated nominal capacity for the vehicle's battery.
    </ResponseField>

    <ResponseField name="source" type="string | null">
      Indicates if this capacity was determined by a user or Smartcar.
      Options are `USER_SELECTED` or `SMARTCAR`.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="url" type="string | null">
  A URL that will launch the flow for a vehicle owner to specify the correct
  battery capacity for a vehicle. **Please ensure you append a
  redirect URI** for us to send a response to once the user exits the flow.

  Please see [this article](/connect/user-selected-batcap) on how to handle the URL callback.
</ResponseField>

<ResponseExample>
  ```json Response Example theme={null}
  {
      "availableCapacities": [
          {
              "capacity" :  70.9,
              "description" : null 
          },
          {
              "capacity" :  80.9,
              "description" : null
          },
          {
              "capacity" :  90.9,
              "description" : "BEV:Extended Range" 
          }
      ],
      "capacity": { 
  	    "nominal" :  80.9,
  	    "source": "USER_SELECTED" 
      },
      "url" : "https://connect.smartcar.com/battery-capacity?vehicle_id=36ab27d0-fd9d-4455-823a-ce30af709ffc&client_id=8229df9f-91a0-4ff0-a1ae-a1f38ee24d07&token=90abecb6-e7ab-4b85-864a-e1c8bf67f2ad&response_type=vehicle_id&redirect_uri="
  } 
  ```
</ResponseExample>

### Case 1: Smartcar has determined the battery capacity

```json Single capacity theme={null}
{
    "availableCapacities": [
        {
            "capacity" :  70.9,
            "description" : null  
        }
    ],
    "capacity": { 
        "nominal" :  70.9,
        "source": "SMARTCAR" 
    },
    "url" : null
} 
```

### Case 2: Unable to determine the battery capacity

```json Multiple capacities theme={null}
{
    "availableCapacities": [
        {
            "capacity" :  70.9,
            "description" : null 
        },
        {
            "capacity" :  80.9,
            "description" : null 
        },
        {
            "capacity" :  90.9,
            "description" : "BEV:Extended Range" 
        }
    ],
    "capacity": null,
    "url" : "https://connect.smartcar.com/battery-capacity?vehicle_id=36ab27d0-fd9d-4455-823a-ce30af709ffc&client_id=8229df9f-91a0-4ff0-a1ae-a1f38ee24d07&token=90abecb6-e7ab-4b85-864a-e1c8bf67f2ad&response_type=vehicle_id&redirect_uri="
} 
```

### Case 3: User selected battery capacity

Smartcar will sometimes return an `availableCapacities` object along side a Connect URL you can use to prompt users to select the battery capacity of their vehicle. This can occur when an accurate match could not be found, or vehicle owners purchased extension packs, or software upgrades specific to their vehicle.

When you redirect a vehicle owner to this Smartcar Connect url, they can select the battery capacity of their vehicle for cases where the battery capacity cannot be accurately determined.

<Frame caption="Battery capacity user selection in Connect">
  <img width="600" src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/battery-capacity-connect.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=c961d991a12ec7159956c2c019c2c3d3" data-og-width="1557" data-og-height="844" data-path="images/changelog/battery-capacity-connect.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/battery-capacity-connect.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=e5adb5112b52ea9e44dfec0560a553c0 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/battery-capacity-connect.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=39d36e8ce845e2160e7b4c53f2fc3a8d 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/battery-capacity-connect.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=98e1670947a946171f6317d42ef64395 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/battery-capacity-connect.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=e18cbf7b80707eaaadfc77ae045e96ee 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/battery-capacity-connect.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=abd113f48a42da549583afb78a8cb640 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/battery-capacity-connect.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=548482aa480e985154dbcaef33171082 2500w" />
</Frame>

When a user selects an option, Smartcar will return this value with `USER_SELECTED` as the source.

```json Multiple capacities theme={null}
{
  "availableCapacities": [
    {
      "capacity": 70.9,
      "description": null 
    },
    {
      "capacity": 80.9,
      "description": null 
    },
    {
      "capacity": 90.9,
      "description": "BEV:Extended Range" 
    }
  ],
  "capacity": { 
    "nominal": 80.9,
    "source": "USER_SELECTED" 
  },
  "url": "https://connect.smartcar.com/battery-capacity?vehicle_id=36ab27d0-fd9d-4455-823a-ce30af709ffc&client_id=8229df9f-91a0-4ff0-a1ae-a1f38ee24d07&token=90abecb6-e7ab-4b85-864a-e1c8bf67f2ad&response_type=vehicle_id&redirect_uri="
}
```
