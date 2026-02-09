# Source: https://smartcar.com/docs/connect/user-selected-batcap.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# User Selected Battery Capacity

> This flow can be launched using the URL provided by the [battery capacity](/docs/api-reference/get-nominal-capacity) endpoint.

## Automatic Battery Capacity Selection

When you request the `read_battery` permission, users will automatically be prompted to select their vehicle's battery capacity during the Smartcar Connect flow if we cannot determine the specific capacity for their vehicle(s). This ensures accurate battery information for your application is readily available.

<Frame caption="Battery capacity selection during Smartcar Connect" width="200">
  <img src="https://mintcdn.com/smartcar-docs/JqEHibg7VKARCx7z/images/connect/battery-capacity-selection.png?fit=max&auto=format&n=JqEHibg7VKARCx7z&q=85&s=ae0a84b03f024606bfce72e9c1f4a66b" style={{ width: '250px' }} data-og-width="388" width="388" data-og-height="842" height="842" data-path="images/connect/battery-capacity-selection.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/JqEHibg7VKARCx7z/images/connect/battery-capacity-selection.png?w=280&fit=max&auto=format&n=JqEHibg7VKARCx7z&q=85&s=0efc0d1d7b90e454505fe7243a4695a9 280w, https://mintcdn.com/smartcar-docs/JqEHibg7VKARCx7z/images/connect/battery-capacity-selection.png?w=560&fit=max&auto=format&n=JqEHibg7VKARCx7z&q=85&s=d8622e19ba50d06c2f9a03b44c426475 560w, https://mintcdn.com/smartcar-docs/JqEHibg7VKARCx7z/images/connect/battery-capacity-selection.png?w=840&fit=max&auto=format&n=JqEHibg7VKARCx7z&q=85&s=1628e58db5cbcb928930c083347fcbc5 840w, https://mintcdn.com/smartcar-docs/JqEHibg7VKARCx7z/images/connect/battery-capacity-selection.png?w=1100&fit=max&auto=format&n=JqEHibg7VKARCx7z&q=85&s=474b6ff769fd376096adcca85a67f05f 1100w, https://mintcdn.com/smartcar-docs/JqEHibg7VKARCx7z/images/connect/battery-capacity-selection.png?w=1650&fit=max&auto=format&n=JqEHibg7VKARCx7z&q=85&s=0940140efeb5fc2101b3119fd83bcb01 1650w, https://mintcdn.com/smartcar-docs/JqEHibg7VKARCx7z/images/connect/battery-capacity-selection.png?w=2500&fit=max&auto=format&n=JqEHibg7VKARCx7z&q=85&s=d246877f0146b9d4241e0280fb33be5d 2500w" />
</Frame>

For users that skip the selection prompt or were connected prior to September 18th, 2025, you can still launch the battery capacity selection flow manually using the URL provided by the [GET /battery/nominal\_capacity](/api-reference/get-nominal-capacity) endpoint.

### Append your redirect URI

Smartcar will provide a URL with the following parameters from the [GET
/battery/nominal\_capacity](/api-reference/get-nominal-capacity) endpoint:

```http  theme={null}
https://connect.smartcar.com/battery-capacity
?vehicle_id=36ab27d0-fd9d-4455-823a-ce30af709ffc
&client_id=8229df9f-91a0-4ff0-a1ae-a1f38ee24d07
&token=90abecb6-e7ab-4b85-864a-e1c8bf67f2ad
&response_type=vehicle_id
&redirect_uri=
```

<ParamField path="vehicle_id" type="string" required>
  The Smartcar vehicle Id.
</ParamField>

<ParamField path="client_id" type="string" required>
  The `client_id` from the Smartcar Dashboard for your application.
</ParamField>

<ParamField path="response_type" type="string" required>
  Must be set to `vehicle_id`.
</ParamField>

<ParamField path="redirect_uri" type="string" required>
  The URI you would like the response sent to after a user exits the
  flow.

  **NOTE:** this is the only parameter that will **not** be prepopulated as
  part of the API response. You **must** append it in order to launch the
  flow successfully and receive confirmation the user has exited the flow.
</ParamField>

<ParamField path="token" type="string">
  A token to validate that the URL was provided from a [battery capacity](/api-reference/get-nominal-capacity)
  response for your application. The token is valid for 30 days. If a token is not provided or is no longer valid,
  the user will be directed to re-auth prior to selecting their capacity.
</ParamField>

## Response

### Success

After the user selects a capacity and completes the flow, Smartcar will send
the following to your redirect URI:

```http Success theme={null}
https://example.com/home
?vehicle_id=36ab27d0-fd9d-4455-823a-ce30af709ffc
&selected_capacity=80.9
&reason=battery_capacity
```

Upon receiving a success response, you can access the `selected_capacity` by calling the GET
[/battery/nominal\_capacity](/api-reference/get-nominal-capacity) endpoint to
view the selection in the `capacity.nominal` field.

### Error

When you redirect the user to select a battery capacity and they select "I don't know the battery capacity", Smartcar will send the
following to your redirect URI:

```http Error theme={null}
https://example.com/home
?error=battery_capacity_no_selection
&error_description=user did not know battery capacity
&vehicle_id=36ab27d0-fd9d-4455-823a-ce30af709ffc
```

## Flow Example

<Frame caption="User selected battery capacity flow">
  <img src="https://mintcdn.com/smartcar-docs/JqEHibg7VKARCx7z/images/connect/bat-cap-selection.png?fit=max&auto=format&n=JqEHibg7VKARCx7z&q=85&s=9fa1c16c336a9e445dc2e3e916c819af" data-og-width="2970" width="2970" data-og-height="2184" height="2184" data-path="images/connect/bat-cap-selection.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/JqEHibg7VKARCx7z/images/connect/bat-cap-selection.png?w=280&fit=max&auto=format&n=JqEHibg7VKARCx7z&q=85&s=e648bb495da3728489c780ffdc86b75c 280w, https://mintcdn.com/smartcar-docs/JqEHibg7VKARCx7z/images/connect/bat-cap-selection.png?w=560&fit=max&auto=format&n=JqEHibg7VKARCx7z&q=85&s=d15a4aff788c5ca7802f693868e1a6e0 560w, https://mintcdn.com/smartcar-docs/JqEHibg7VKARCx7z/images/connect/bat-cap-selection.png?w=840&fit=max&auto=format&n=JqEHibg7VKARCx7z&q=85&s=c94b84d74787bb0c495acf30365fc4c8 840w, https://mintcdn.com/smartcar-docs/JqEHibg7VKARCx7z/images/connect/bat-cap-selection.png?w=1100&fit=max&auto=format&n=JqEHibg7VKARCx7z&q=85&s=a6ec28bfc7f81eb115b740458fc2b624 1100w, https://mintcdn.com/smartcar-docs/JqEHibg7VKARCx7z/images/connect/bat-cap-selection.png?w=1650&fit=max&auto=format&n=JqEHibg7VKARCx7z&q=85&s=9b422b8f6379358443fe40234183b25b 1650w, https://mintcdn.com/smartcar-docs/JqEHibg7VKARCx7z/images/connect/bat-cap-selection.png?w=2500&fit=max&auto=format&n=JqEHibg7VKARCx7z&q=85&s=5f7cfc619fc293e0bae0ec972fe59ad6 2500w" />
</Frame>
