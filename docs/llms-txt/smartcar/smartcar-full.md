# Smartcar Documentation

Source: https://smartcar.com/docs/llms-full.txt

---

# Make Specific Endpoints
Source: https://smartcar.com/docs/api-reference/about-brand-specific



<Warning>
  The Vehicles API v2.0 will be deprecated by **Q3 of 2026**. We recommend migrating to the [latest version](/api-reference/vehicles-api-intro) as soon as possible to ensure continued support and access to new features.
</Warning>

In cases where there are many differences in how each OEM provides the same data, Smartcar would provide you with a make-specific endpoint before making it widely available to all supported makes.

This allowed customers to take advantage of these endpoints and share feedback with Smartcar. Based on the feedback, we realized that these endpoints often required customers to write make-specific code, which is not ideal for a standardized API.

These endpoints will be deprecated along with API V2.0.

<Info>When using make specific endpoints, please ensure to specify the [make](/api-reference/makes) in lower case format. Using upper case letters will result in a PERMISSION error.</Info>


# Errors Overview
Source: https://smartcar.com/docs/api-reference/api-errors

A comprehensive breakout of all Smartcar errors.

# Connect Errors

| Error Type           | Error Code                                                           | Description                                                                                                                     |
| -------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Access Denied        | [access\_denied](/errors/connect-errors/access-denied)               | This error occurs when a user denies your application access to the requested scope of permissions.                             |
| Invalid Subscription | [invalid\_subscription](/errors/connect-errors/invalid-subscription) | This error occurs when a user’s vehicle is compatible but their connected services subscription is inactive or never activated. |
| Configuration Error  | [configuration\_error](/errors/connect-errors/configuration-error)   | This error occurs when the user has encountered an Error page in Connect and has chosen to return to your application.          |
| No Vehicles          | [no\_vehicles](/errors/connect-errors/no-vehicles)                   | This error occurs when a vehicle owner has a connected services account, but there are no vehicles associated with the account. |
| Vehicle Incompatible | [vehicle\_incompatible](/errors/connect-errors/vehicle-incompatible) | This error occurs when a user tries to authorize an incompatible vehicle in Smartcar Connect.                                   |
| Server Error         | [server\_error](/errors/connect-errors/server-error)                 | If there is a server error, the user will return to your application.                                                           |

<br />

# API Errors

API errors are returned from requests made via Smartcar API.
Smartcar uses HTTP status codes to indicate success or failure of API requests. This includes:

* `2XX`: indicates success
* `4XX`: indicates an invalid request (e.g. a required parameter is missing from the request body)
* `5XX`: indicates Smartcar-related issues (e.g. a vehicle is not capable of fulfilling a request).

## Error Response

All Smartcar errors contain the following fields:

| Name        | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ----------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| type        | string | A unique identifier that groups codes into broad categories of errors                                                                                                                                                                                                                                                                                                                                                                                        |
| code        | string | A short, descriptive identifier for the error that occurred                                                                                                                                                                                                                                                                                                                                                                                                  |
| description | string | A short description of the code that provides additional information about the error. The description is always provided in English.                                                                                                                                                                                                                                                                                                                         |
| docURL      | string | A link to Smartcar’s doc center guide for the given type and code                                                                                                                                                                                                                                                                                                                                                                                            |
| statusCode  | number | The HTTP status code                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| requestId   | string | Smartcar’s request ID                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| resolution  | object | An object with at least one enumerated property named as "type" that specifies which action can be taken to resolve this error. There are three possible values for the property "type": `RETRY_LATER` - Retry the request at a later time; `REAUTHENTICATE` - Prompt the user to re-authenticate in Smartcar Connect; and `CONTACT_SUPPORT` - Contact Smartcar’s support team. This object could contain other properties depending on the "type" of error. |

<br />

| Error Type                   | Error Code                                                                                            | Status | Description                                                                                                                                                                                                   |
| ---------------------------- | ----------------------------------------------------------------------------------------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `AUTHENTICATION`             | [NULL](/errors/api-errors/authentication-errors#null)                                                 | 401    | Thrown when there is an issue with your authorization headers.                                                                                                                                                |
| `BILLING`                    | [INVALID\_PLAN](/errors/api-errors/billing-errors#invalid-plan)                                       | 430    | Thrown when limits have been reached based on your plan or if the feature is not available.                                                                                                                   |
| `BILLING`                    | [VEHICLE\_LIMIT](/errors/api-errors/billing-errors#vehicle-limit)                                     | 430    | Thrown when limits have been reached based on your plan or if the feature is not available.                                                                                                                   |
| `BILLING`                    | [VEHICLE\_REQUEST\_LIMIT](/errors/api-errors/billing-errors#vehicle-request-limit)                    | 430    | Thrown when limits have been reached based on your plan or if the feature is not available.                                                                                                                   |
| `BILLING`                    | [ACCOUNT\_SUSPENDED](/errors/api-errors/billing-errors#account-suspended)                             | 430    | Thrown when limits have been reached based on your plan or if the feature is not available.                                                                                                                   |
| `COMPATIBILITY`              | [MAKE\_NOT\_COMPATIBLE](/errors/api-errors/compatibility-errors#make-not-compatible)                  | 501    | Thrown when Smartcar does not support a make or feature for a vehicle.                                                                                                                                        |
| `COMPATIBILITY`              | [SMARTCAR\_NOT\_CAPABLE](/errors/api-errors/compatibility-errors#smartcar-not-capable)                | 501    | Thrown when Smartcar does not support a make or feature for a vehicle.                                                                                                                                        |
| `COMPATIBILITY`              | [VEHICLE\_NOT\_CAPABLE](/errors/api-errors/compatibility-errors#vehicle-not-capable)                  | 501    | Thrown when Smartcar does not support a make or feature for a vehicle.                                                                                                                                        |
| `CONNECTED_SERVICES_ACCOUNT` | [ACCOUNT\_ISSUE](/errors/api-errors/connected-services-account-errors#account-issue)                  | 400    | Thrown when there are issues with the user's connected service account.                                                                                                                                       |
| `CONNECTED_SERVICES_ACCOUNT` | [AUTHENTICATION\_FAILED](/errors/api-errors/connected-services-account-errors#authentication-failed)  | 400    | Thrown when there are issues with the user's connected service account.                                                                                                                                       |
| `CONNECTED_SERVICES_ACCOUNT` | [NO\_VEHICLES](/errors/api-errors/connected-services-account-errors#no-vehicles)                      | 400    | Thrown when there are issues with the user's connected service account.                                                                                                                                       |
| `CONNECTED_SERVICES_ACCOUNT` | [SUBSCRIPTION](/errors/api-errors/connected-services-account-errors#subscription)                     | 400    | Thrown when there are issues with the user's connected service account.                                                                                                                                       |
| `CONNECTED_SERVICES_ACCOUNT` | [VEHICLE\_MISSING](/errors/api-errors/connected-services-account-errors#vehicle-missing)              | 400    | Thrown when there are issues with the user's connected service account.                                                                                                                                       |
| `CONNECTED_SERVICES_ACCOUNT` | [PERMISSION](/errors/api-errors/connected-services-account-errors#permission)                         | 400    | Thrown when there are permission issues with the user's connected service account.                                                                                                                            |
| `CONNECTED_SERVICES_ACCOUNT` | [VIRTUAL\_KEY\_REQUIRED](/errors/api-errors/connected-services-account-errors#virtual-key-required)   | 400    | Thrown when a virtual key is required to complete the request.                                                                                                                                                |
| `PERMISSION`                 | [NULL](/errors/api-errors/permission-errors#null)                                                     | 403    | Thrown when you make a requests to an endpoint associated with permissions not yet granted to your application.                                                                                               |
| `RATE_LIMIT`                 | [SMARTCAR\_API](/errors/api-errors/rate-limit-errors#smartcar-api)                                    | 429    | Thrown when there is an issue with the frequency of your requests.                                                                                                                                            |
| `RATE_LIMIT`                 | [VEHICLE](/errors/api-errors/rate-limit-errors#vehicle)                                               | 429    | Thrown when there is an issue with the frequency of your requests.                                                                                                                                            |
| `RESOURCE_NOT_FOUND`         | [PATH](/api-reference/api-errors#resource-errors-path)                                                | 404    | Thrown if the requested path does not exist.                                                                                                                                                                  |
| `RESOURCE_NOT_FOUND`         | [VERSION](/api-reference/api-errors#resource-errors-version)                                          | 404    | Thrown if the requested path does not exist.                                                                                                                                                                  |
| `SERVER`                     | [INTERNAL](/errors/api-errors/server-errors#internal)                                                 | 500    | Thrown when Smartcar runs into an unexpected issue and was unable to process the request.                                                                                                                     |
| `SERVER`                     | [MULTIPLE\_RECORDS\_FOUND](/errors/api-errors/server-errors#multiple-records-found)                   | 500    | Thrown when multiple records are found but only one was expected.                                                                                                                                             |
| `SERVER`                     | [RECORD\_NOT\_FOUND](/errors/api-errors/server-errors#record-not-found)                               | 500    | Thrown when a required record could not be found.                                                                                                                                                             |
| `UPSTREAM`                   | [INVALID\_DATA](/errors/api-errors/upstream-errors#invalid-data)                                      | 502    | Thrown when the OEM or vehicle failed to process the request.                                                                                                                                                 |
| `UPSTREAM`                   | [KNOWN\_ISSUE](/errors/api-errors/upstream-errors#known-issue)                                        | 502    | Thrown when the OEM or vehicle failed to process the request.                                                                                                                                                 |
| `UPSTREAM`                   | [NO\_RESPONSE](/errors/api-errors/upstream-errors#no-response)                                        | 502    | Thrown when the OEM or vehicle failed to process the request.                                                                                                                                                 |
| `UPSTREAM`                   | [RATE\_LIMIT](/errors/api-errors/upstream-errors#rate-limit)                                          | 502    | Thrown when the OEM or vehicle failed to process the request.                                                                                                                                                 |
| `UPSTREAM`                   | [UNKNOWN\_ISSUE](/errors/api-errors/upstream-errors#unknown-issue)                                    | 502    | Thrown when the OEM or vehicle failed to process the request.                                                                                                                                                 |
| `VALIDATION`                 | [NULL](/errors/api-errors/validation-errors#null)                                                     | 400    | Thrown if there is an issue with the format of the request or body.                                                                                                                                           |
| `VALIDATION`                 | [PARAMETER](/errors/api-errors/validation-errors#parameter)                                           | 400    | Thrown if there is an issue with the format of the request or body.                                                                                                                                           |
| `VEHICLE_STATE`              | [ASLEEP](/errors/api-errors/vehicle-state-errors#asleep)                                              | 409    | Thrown when a request fails due to the state of a vehicle or logically cannot be completed—for example, you can't retrieve vehicle data because the vehicle is asleep and not responding to network requests. |
| `VEHICLE_STATE`              | [CHARGING\_IN\_PROGRESS](/errors/api-errors/vehicle-state-errors#charging-in-progress)                | 409    | Thrown when a request fails due to the state of a vehicle or logically cannot be completed—for example, you can't unlock the charge port while the vehicle is actively charging.                              |
| `VEHICLE_STATE`              | [CHARGING\_PLUG\_NOT\_CONNECTED](/errors/api-errors/vehicle-state-errors#charging-plug-not-connected) | 409    | Thrown when a request fails due to the state of a vehicle or logically cannot be completed—for example, you can't start charging the vehicle if the cable is not plugged in.                                  |
| `VEHICLE_STATE`              | [DOOR\_OPEN](/errors/api-errors/vehicle-state-errors#door-open)                                       | 409    | Thrown when a request fails due to the state of a vehicle or logically cannot be completed—for example, you can't lock the vehicle if a door is open.                                                         |
| `VEHICLE_STATE`              | [FULLY\_CHARGED](/errors/api-errors/vehicle-state-errors#fully-charged)                               | 409    | Thrown when a request fails due to the state of a vehicle or logically cannot be completed—for example, you can't start charging because the battery is already fully charged.                                |
| `VEHICLE_STATE`              | [NOT\_CHARGING](/errors/api-errors/vehicle-state-errors#not-charging)                                 | 409    | Thrown when a request fails due to the state of a vehicle or logically cannot be completed—for example, you can't stop charging because the vehicle is not currently charging.                                |
| `VEHICLE_STATE`              | [CHARGE\_FAULT](/errors/api-errors/vehicle-state-errors#charge-fault)                                 | 409    | Thrown when a request fails due to the state of a vehicle or logically cannot be completed—for example, you can't start charging because the vehicle has detected a charging system fault.                    |
| `VEHICLE_STATE`              | [HOOD\_OPEN](/errors/api-errors/vehicle-state-errors#hood-open)                                       | 409    | Thrown when a request fails due to the state of a vehicle or logically cannot be completed—for example, you can't start the engine if the hood is open.                                                       |
| `VEHICLE_STATE`              | [IGNITION\_ON](/errors/api-errors/vehicle-state-errors#ignition-on)                                   | 409    | Thrown when a request fails due to the state of a vehicle or logically cannot be completed—for example, you can't perform certain remote actions while the ignition is on.                                    |
| `VEHICLE_STATE`              | [IN\_MOTION](/errors/api-errors/vehicle-state-errors#in-motion)                                       | 409    | Thrown when a request fails due to the state of a vehicle or logically cannot be completed—for example, you can't lock the doors while the vehicle is in motion.                                              |
| `VEHICLE_STATE`              | [REMOTE\_ACCESS\_DISABLED](/errors/api-errors/vehicle-state-errors#remote-access-disabled)            | 409    | Thrown when a request fails due to the state of a vehicle or logically cannot be completed—for example, you can't send remote commands because remote access is disabled in the vehicle settings.             |
| `VEHICLE_STATE`              | [TRUNK\_OPEN](/errors/api-errors/vehicle-state-errors#trunk-open)                                     | 409    | Thrown when a request fails due to the state of a vehicle or logically cannot be completed—for example, you can't lock the vehicle if the trunk is open.                                                      |
| `VEHICLE_STATE`              | [UNKNOWN](/errors/api-errors/vehicle-state-errors#unknown)                                            | 409    | Thrown when a request fails due to the state of a vehicle or logically cannot be completed—for example, the vehicle reports an unknown state that prevents the requested action.                              |
| `VEHICLE_STATE`              | [UNREACHABLE](/errors/api-errors/vehicle-state-errors#unreachable)                                    | 409    | Thrown when a request fails due to the state of a vehicle or logically cannot be completed—for example, you can't send commands because the vehicle is offline or out of network range.                       |
| `VEHICLE_STATE`              | [VEHICLE\_OFFLINE\_FOR\_SERVICE](/errors/api-errors/vehicle-state-errors#vehicle-offline-for-service) | 409    | Thrown when a request fails due to the state of a vehicle or logically cannot be completed—for example, you can't access vehicle data because the vehicle is offline for maintenance or service.              |


# SDKs
Source: https://smartcar.com/docs/api-reference/api-sdks



Our backend SDKs simplify the process of making calls to our Vehicle API.

<Snippet file="sdks/api-sdk-card-group.mdx" />

<br />

<Tip>
  While we provide a number of SDKs for popular languages, you do not need to use an SDK to integrate with our API.
  Our APIs are just standard HTTP endpoints that can be reached with any HTTP library of your choice.
</Tip>


# Permissions
Source: https://smartcar.com/docs/api-reference/application-permissions

GET https://api.smartcar.com/v2.0/vehicles/{id}/permissions
Returns a list of the permissions that have been granted to your application in relation to this vehicle.

## Request

<ParamField path="id" type="string" required>
  The vehicle id.
</ParamField>

<RequestExample>
  <Snippet file="api-reference/core-sdk-methods/application-permissions.mdx" />
</RequestExample>

## Response

<ResponseField name="permissions" type="[permissions]">
  An array of [permissions](/api-reference/permissions).
</ResponseField>

<ResponseField name="paging" type="object">
  Metadata about the current list of elements.

  <Expandable>
    <ResponseField name="count" type="integer">
      The total number of elements for the entire query (not just the given page).
    </ResponseField>

    <ResponseField name="offset" type="integer">
      The current start index of the returned list of elements.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseExample>
  ```json Example Response theme={null}
  {
      "paging": {
          "count": 25,
          "offset": 10
      },
      "permissions": [
          "read_vehicle_info"
      ]
  } 
  ```
</ResponseExample>


# Audi: Charge Status
Source: https://smartcar.com/docs/api-reference/audi/get-charge

GET https://api.smartcar.com/v2.0/vehicles/{id}/{make}/charge
Returns all charging related data for an Audi vehicle.

<Snippet file="api-reference/note-bse-audi.mdx" />

## Permission

`read_charge`

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/charge" \
  -H "Authorization: Bearer {token}" \
  -X "GET"
  ```

  ```python Python theme={null}
  charge =  vehicle.request(
        "GET", 
        "{make}/charge"
  )
  ```

  ```js Node theme={null}
  const charge =  await vehicle.request(
        "GET", 
        "{make}/charge"
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("GET")
        .path("{make}/charge")
        .build();
  VehicleResponse charge =  vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  charge =  vehicle.request(
        "GET", 
        "{make}/charge"
  )
  ```
</RequestExample>

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

## Response

<ResponseField name="chargingStatus" type="string | null">
  Indicates the charging status of the vehicle
</ResponseField>

<ResponseField name="isPluggedIn" type="bool | null">
  Indicates if the vehicle is plugged in
</ResponseField>

<ResponseField name="wattage" type="number | null">
  The instant power measured by the vehicle (in kilowatts).
</ResponseField>

<ResponseField name="chargeRate" type="number | null">
  The rate of range added in the charging session (in kilometers added / hour).
</ResponseField>

<ResponseField name="chargeType" type="string | null">
  Indicates the type of charger.
</ResponseField>

<ResponseField name="chargePortColor" type="string | null">
  The indicator light color of the connector.
</ResponseField>

<ResponseField name="chargePortLatch" type="string | null">
  Indicates if the charge port latch status.
</ResponseField>

<ResponseField name="completionTime" type="string | null">
  An ISO8601 formatted datetime (YYYY-MM-DDTHH:mm:ss.SSSZ) for the time at which the vehicle expects to complete this charging session.
</ResponseField>

<ResponseField name="chargeMode" type="string | null">
  Indicates if the vehicle is set to charge on a timer. One of `manual` or `timer`.
</ResponseField>

<ResponseField name="socLimit" type="number | null">
  Indicates the level at which the vehicle will stop charging and be considered fully charged as a percentage.
</ResponseField>

<ResponseField name="externalPowerStatus" type="string | null">
  When plugged in indicates if the charging station is able to provide power to the vehicle.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
      {
            "chargingStatus": "CHARGING",
            "isPluggedIn": null,
            "chargeRate": 21,
            "chargeType": "ac",
            "chargePortColor": "green",
            "chargePortLatch": "locked",
            "completionTime": "2022-01-13T22:52:55.358Z",
            "chargeMode": "manual",
            "socLimit": 0.8,
            "externalPowerStatus": "active",
            "wattage" : 1.5
      }
  ```
</ResponseExample>


# Auth Code Exchange
Source: https://smartcar.com/docs/api-reference/authorization/auth-code-exchange

POST https://auth.smartcar.com/oauth/token
To interact with the Smartcar API, you will need to exchange your authorization code from the [Connect redirect](https://smartcar.com/docs/connect/handle-the-response) for an access token. Check the [overview](https://smartcar.com/docs/api-reference/authorization/overview) page for how to manage your tokens.

## Requesting Access Tokens

**Headers**

<Snippet file="header-basic-auth.mdx" />

<ParamField header="Content-Type" type="string" initialValue="application/x-www-form-urlencoded" required>
  Must be set to `application/x-www-form-urlencoded`, matching the format of the request body.
</ParamField>

<ParamField header="User-Agent" type="string" required>
  A valid HTTP User Agent value. This value is typically included in the HTTP requests by the client that is making the request. You usually don't have to set this manually.
</ParamField>

**Body**

<ParamField query="code" type="string" required>
  The authorization code received in the handle response step.
</ParamField>

<ParamField query="grant_type" type="string" required>
  This value must be set to `authorization_code`
</ParamField>

<ParamField query="redirect_uri" type="string" required>
  The `redirect_uri` provided in the redirect to Connect step. This value is checked to match the URI sent when the user was directed to Connect.
</ParamField>

<Info>
  If you launch Connect from a single-page or mobile application, `redirect_uri` **must** match the URI passed in your Connect URL, not the redirect for your backend.
</Info>

<RequestExample>
  ```bash cURL theme={null}
  curl https://auth.smartcar.com/oauth/token \
  -X POST \
  -H 'Authorization: Basic base64({client_id}:{client_secret})' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'grant_type=authorization_code&code=35a59c0b-745c-436c-a8a2-7758e718dcb8&redirect_uri=https://example.com/home'
  ```

  ```python Python SDK theme={null}
    access = client.exchange_code('{code}')
  ```

  ```node Node SDK theme={null}
    access = client.exchangeCode('{code}');;
  ```

  ```java Java SDK theme={null}
    Auth access = authClient.exchangeCode("{code}");
  ```

  ```ruby Ruby SDK theme={null}
    access = client.exchange_code("{code}")
  ```
</RequestExample>

## Response

<Snippet file="response-token-pair.mdx" />


# Overview
Source: https://smartcar.com/docs/api-reference/authorization/overview

Understand how to manage access and refresh tokens to maintain persistent access to vehicles.

Smartcar uses OAuth 2.0 access tokens to secure API requests. Managing these tokens correctly is critical for ensuring your application can reliably interact with vehicles.

* **Access Tokens**: Short-lived tokens (2 hours) used to authorize requests to the Smartcar API.
* **Refresh Tokens**: Long-lived tokens (60 days) used to obtain new access tokens without requiring the user to re-authenticate.

## Token Management

* **[Auth Code Exchange](/api-reference/authorization/auth-code-exchange)**: The initial exchange of an authorization code for your first access and refresh token pair.
* **[Access Tokens Refresh](/api-reference/authorization/refreshing-access-token)**: How to get a new token set when the current one expires.

<Warning>
  When you use a refresh token, you receive a **new refresh token** in the response. You must save this new refresh token for future use, as the old one is invalidated.
</Warning>

## Storing access tokens

### Default and Brand Select Connect Flow

By default tokens are scoped to the user's connected services account.

<Note>This means that if there are multiple vehicles
on the account - and they are selected at the time of authorization, the access token is valid for all those vehicle Ids.</Note>

To manage this, we recommend using the [Smartcar User Id](/api-reference/user) to link tokens to your corresponding user id. The diagram below
will also allow multiple users to connect to vehicles on the same account.

<Frame type="simple">
  <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/connect/StandardFlowDBDiagram.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=6ed076cedb2755b7ae11daa09475f614" data-og-width="850" width="850" data-og-height="324" height="324" data-path="images/connect/StandardFlowDBDiagram.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/connect/StandardFlowDBDiagram.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=215549f52afa07960e4e79170e2ef433 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/connect/StandardFlowDBDiagram.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=1ef28f61d60c6e497951fe1699b5cd92 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/connect/StandardFlowDBDiagram.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=29d52ce9358bfd402e377322317b3f5d 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/connect/StandardFlowDBDiagram.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=cfb0b8f36d52241651c4c36624f6926e 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/connect/StandardFlowDBDiagram.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=d0910d5555b6a82c37b46e9e1b279ccb 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/connect/StandardFlowDBDiagram.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=0dca721dfb26cc28dc307e25873fa8fe 2500w" />
</Frame>

### Single Select Connect Flow

When using the Single Select flow, tokens are strictly scoped to the vehicle that was authorized for that Connect session.
This means that if a user connects multiple vehicles under the same connected services account, each vehicle id will be tied
to its own set of tokens.

<Frame type="simple">
  <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/connect/ConnectMatchDBDiagram.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=0543e3075f012e372b8a5328509d5161" data-og-width="850" width="850" data-og-height="551" height="551" data-path="images/connect/ConnectMatchDBDiagram.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/connect/ConnectMatchDBDiagram.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=3c1d425f8b4449673fdda5e2761ce74d 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/connect/ConnectMatchDBDiagram.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=17c9fb393808fb58c070ac138cd89a5e 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/connect/ConnectMatchDBDiagram.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=1529833e0983bf57768dd22917dbbea5 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/connect/ConnectMatchDBDiagram.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=41a7223d2aef7827e14fdf1e77ca7da2 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/connect/ConnectMatchDBDiagram.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=0d75de09cc972859a9b71913cff846fb 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/connect/ConnectMatchDBDiagram.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=9519db1db5666638998cede5a393e47a 2500w" />
</Frame>

## Token expiry

Access tokens are valid for 2 hours, while refresh tokens are valid for 60 days. You can use the corresponding refresh token to fetch a new token pair
once an access token has expired.

In order to maintain access to a vehicle without having a user go through Connect again, you'll want to make sure the refresh token never expires.
Whenever you fetch a new token pair, we will return a **new access and refresh token**.

Prior to expiry, access tokens will remain valid until their expiry when fetching a new token pair. Refresh tokens on the other hand are invalidated
1 minute after they're used.

To avoid common 401 Authentication errors, please ensure you are **persisting both the access and refresh token** we return whenever you fetch a new pair.

<Tip>
  In addition to any logic that checks access token expiry when making an API request, we strongly recommend having another job that periodically
  checks for refresh tokens that are close to expiry and refreshes them.
</Tip>


# Refreshing Access Tokens
Source: https://smartcar.com/docs/api-reference/authorization/refreshing-access-token

POST https://auth.smartcar.com/oauth/token
Your access token will expire **2 hours** after it is issued. When this happens, your application can retrieve a new one by using the corresponding `REFRESH_TOKEN` without requiring the user to re-authenticate.

<Warning>
  A refresh token is invalidated 10 minutes after use. If your first attempt at refreshing tokens fails, ensure you retry within 10 minutes.
  Please ensure you're persisting **both the newly minted access and refresh token**. Failure to do so will require the user to authenticate again after the access token has expired.
</Warning>

## Request

**Headers**

<Snippet file="header-basic-auth.mdx" />

<ParamField header="Content-Type" type="string" initialValue="application/x-www-form-urlencoded" required>
  Must be set to `application/x-www-form-urlencoded`, matching the format of the request body.
</ParamField>

<ParamField header="User-Agent" type="string" required>
  A valid HTTP User Agent value. This value is typically included in the HTTP requests by the client that is making the request. You usually don't have to set this manually.
</ParamField>

<RequestExample>
  <Snippet file="authorization/code-group-token-refresh.mdx" />
</RequestExample>

**Body**

<ParamField query="grant_type" type="string" initialValue="refresh_token" required>
  This value must be set to `refresh_token`
</ParamField>

<ParamField query="refresh_token" type="string" initialValue="3e565aed-d4b2-4296-9b4c-aec35825a6aa" required>
  The refresh token received in the response with the access token from an [auth code exchange](/api-reference/authorization/auth-code-exchange)
  or prior token refresh.
</ParamField>

**Response**

<Snippet file="response-token-pair.mdx" />


# Batch
Source: https://smartcar.com/docs/api-reference/batch

POST https://api.smartcar.com/v2.0/vehicles/{id}/batch
Returns a list of responses from multiple Smartcar `GET` endpoints, all combined into a single request.

<Warning>
  The Vehicles API v2.0 will be deprecated by **Q3 of 2026**. We recommend migrating to the [latest version](/api-reference/vehicles-api-intro) as soon as possible to ensure continued support and access to new features.
</Warning>

<Info>
  Each endpoint in the batch counts against your [request limit](/errors/api-errors/billing-errors) for a vehicle.
</Info>

## Request

**Path**

<Snippet file="api-reference/path-vehicle-id.mdx" />

**Body**

<ParamField body="requests" type="array" required>
  An array of requests to make.

  <Expandable>
    <ParamField body="path" type="string" required>
      The Smartcar endpoint to request data from.
    </ParamField>
  </Expandable>
</ParamField>

<RequestExample>
  <Snippet file="api-reference/core-sdk-methods/batch.mdx" />
</RequestExample>

## Response

<ResponseField name="responses" type="array">
  The responses from Smartcar.

  <Expandable title="response" defaultOpen="true">
    <ResponseField name="headers" type="object">
      The headers for this response.

      <Expandable title="headers">
        <ResponseField name="sc-unit-system" type="string">
          The unit system to use for the request.
        </ResponseField>

        <ResponseField name="sc-data-age" type="string">
          The timestamp (ISO-8601 format) of when the returned data was recorded by the vehicle.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="code" type="number">
      The HTTP response status code.
    </ResponseField>

    <ResponseField name="path" type="string">
      The Smartcar endpoint to request data from.
    </ResponseField>

    <ResponseField name="body" type="string">
      The response body of this request. The structure of this object will vary by endpoint. See the corresponding endpoint specification.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
    "responses": [
      {
        "path": "/odometer",
        "body": {
          "distance": 37829
        },
        "code": 200,
        "headers": {
          "sc-data-age": "2019-10-24T00:43:46.000Z",
          "sc-unit-system": "metric"
        }
      },
      {
        "path": "/location",
        "body": {
          "latitude": 37.4292,
          "longitude": 122.1381
        },
        "code": 200,
        "headers": {
          "sc-data-age": "2019-10-24T00:43:46.000Z"
        }
      }
    ]
  }
  ```
</ResponseExample>


# Charge Records
Source: https://smartcar.com/docs/api-reference/bmw/get-charge-records

GET https://api.smartcar.com/v2.0/vehicles/{id}/{make}/charge/records
Returns data associated with completed charging sessions for a vehicle. Limited to the last 30 days or when the owner first granted your application access, which ever is shorter.

<Note>
  This endpoint is currently available for `bmw` and `mini`
</Note>

## Permission

`read_charge_records`

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

**Query**

<ParamField query="startDate">
  Date of the first record to return in YYYY-MM-DD format.
  Defaults to 30 days prior  or when the owner first granted your application access, whichever is shorter.
</ParamField>

<ParamField query="endDate">
  Date of the final record to return in YYYY-MM-DD format. Defaults to the date of the request.
</ParamField>

## Response

<ResponseField name="records" type="[object]">
  An array of charge records for the vehicle.

  <Expandable defaultOpen="true">
    <ResponseField name="chargeStart" type="string">
      The start date of the charging record, formatted in ISO 8601 standard
    </ResponseField>

    <ResponseField name="chargeEnd" type="string">
      The end date of the charging record, formatted in ISO 8601 standard
    </ResponseField>

    <ResponseField name="location" type="string">
      Location of the charge session.
    </ResponseField>

    <ResponseField name="energy" type="number" default="kWh">
      The amount of energy consumed during the charging session.
    </ResponseField>

    <ResponseField name="isPublic" type="bool">
      Indicates whether the charging location is public or not.
    </ResponseField>

    <ResponseField name="startPercentRemaining" type="number">
      The remaining battery soc at the start of the charging session.
    </ResponseField>

    <ResponseField name="endPercentRemaining" type="number">
      The remaining battery soc at the end of the charging session.
    </ResponseField>

    <ResponseField name="chargingType" type="string">
      The type of charger used for the session.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
    "records": [
      {
        "chargeStart" : "2023-03-08T12:54:44Z",
        "chargeEnd" : "2023-03-08T14:14:44Z",
        "location": "Cockfosters Road, Barnet, EN4 0",
        "energy"  : 34.22998046875,
        "isPublic" : true,
        "startPercentRemaining" : 0.57,
        "endPercentRemaining" : 1, 
        "chargingType" : "DC" 
      }
    ]
  }
  ```
</ResponseExample>


# Compatibility API Overview
Source: https://smartcar.com/docs/api-reference/compatibility-api-intro

The Compatibility API helps you determine if a specific vehicle is supported by Smartcar before launching the Connect flow. This allows you to provide a seamless user experience by verifying eligibility up front.

## What You Can Do

* Check if a vehicle is compatible by VIN
* Query supported makes and regions

## Authentication

The Compatibility API uses a bearer token, which you can obtain from your Smartcar Dashboard or via the OAuth2 flow.

## Base URL

```
https://api.smartcar.com/compatibility/v2.0
```

## Key Resources

* [Check Compatibility by VIN](/api-reference/compatibility/by-vin)
* [Check Compatibility by Region and Make](/api-reference/compatibility/by-region-and-make)

## Example Use Cases

* Pre-qualifying users before showing Smartcar Connect
* Displaying supported makes and models in your app
* Reducing user friction by avoiding unsupported vehicles

<Info>
  For more details on using the Compatibility API, see [Compatibility API Reference](/api-reference/compatibility/by-vin).
</Info>


# By Region and Make
Source: https://smartcar.com/docs/api-reference/compatibility/by-region-and-make

GET https://api.smartcar.com/v2.0/compatibility/matrix
Compatibility will vary by model, year, and trim. This API is for reference purposes only and it showcases vehicle makes and models that may be compatible with Smartcar and it does not guarantee that a specific vehicle will be compatible.

<Info>
  The Compatibility API is an Enterprise feature. Please [contact us](https://smartcar.com/pricing/) to upgrade your plan.
</Info>

Compatibility by region and make allows developers to query the latest version of our Compatibility Matrix based on region, engine type, make, and permission.

## Request

**Headers**

<Snippet file="header-basic-auth.mdx" />

**Query**

<ParamField query="region" type="string" required>
  One of the following regions: `US`, `CA` or `EUROPE`
</ParamField>

<ParamField query="type" type="string">
  Queries for all engine types if none are specified.

  <Expandable>
    <ResponseField name="ICE" />

    <ResponseField name="BEV" />

    <ResponseField name="PHEV" />

    <ResponseField name="HEV" />
  </Expandable>
</ParamField>

<ParamField query="make" type="string">
  A space-separated list of [makes](/api-reference/makes). This field is optional. If no make is specified, all makes will be returned.
</ParamField>

<ParamField query="scope" type="string">
  A space-separated list of [permissions](/api-reference/permissions).
  Queries for all permissions if none are specified.
</ParamField>

<RequestExample>
  ```bash cURL theme={null}
  curl --request GET \
    --url 'https://api.smartcar.com/v2.0/compatibility/matrix?region=US&type=BEV&make=tesla&scope=read_battery%20read_charge' \
    --header 'Authorization: Basic bXktY2xpZW50LWlkOm15LWNsaWVudC1zZWNyZXQ='
  ```

  ```javascript JavaScript theme={null}
  const response = await fetch('https://api.smartcar.com/v2.0/compatibility/matrix?region=US&type=BEV&make=tesla&scope=read_battery%20read_charge', {
    method: 'GET',
    headers: {
      'Authorization': 'Basic bXktY2xpZW50LWlkOm15LWNsaWVudC1zZWNyZXQ='
    }
  });

  const data = await response.json();
  ```

  ```python Python theme={null}
  import requests

  url = "https://api.smartcar.com/v2.0/compatibility/matrix"
  params = {
      "region": "US",
      "type": "BEV", 
      "make": "tesla",
      "scope": "read_battery read_charge"
  }
  headers = {
      "Authorization": "Basic bXktY2xpZW50LWlkOm15LWNsaWVudC1zZWNyZXQ="
  }

  response = requests.get(url, params=params, headers=headers)
  data = response.json()
  ```
</RequestExample>

## Response

<ResponseField name="make" type="array">
  An array of models supported for the given `make`.

  <Expandable title="make">
    <ResponseField name="model" type="string">
      `model` for the given `make`.
    </ResponseField>

    <ResponseField name="startYear" type="number">
      The earliest model year supported by Smartcar.
    </ResponseField>

    <ResponseField name="endYear" type="number">
      The latest model year supported by Smartcar.
    </ResponseField>

    <ResponseField name="type" type="string">
      Engine type for the given `model`.

      <Expandable title="type">
        <ResponseField name="ICE" />

        <ResponseField name="BEV" />

        <ResponseField name="PHEV" />

        <ResponseField name="HEV" />
      </Expandable>
    </ResponseField>

    <ResponseField name="endpoints" type="array">
      An array of endpoints supported for the given `model`.
    </ResponseField>

    <ResponseField name="permissions" type="array">
      An array of `permissions` supported for the given `model`.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseExample>
  ```json Example Response theme={null}
    {
      "NISSAN": [
        {
          "model": "LEAF",
          "startYear": 2018,
          "endYear": 2022,
          "type": "BEV",
          "endpoints": [
            "EV battery",
            "EV charging status",
            "Location",
            "Lock & unlock",
            "Odometer"
          ],
          "permissions": [
            "read_battery",
            "read_charge",
            "read_location",
            "control_security",
            "read_odometer"
          ]
        }
      ],
      "TESLA": [
        {
          "model": "3",
          "startYear": 2017,
          "endYear": 2023,
          "type": "BEV",
          "endpoints": [
            "EV battery",
            "EV charging status",
            "EV start & stop charge",
            "Location",
            "Lock & unlock",
            "Odometer",
            "Tire pressure"
          ],
          "permissions": [
            "read_battery",
            "read_charge",
            "control_charge",
            "read_location",
            "control_security",
            "read_odometer",
            "read_tires"
          ]
        }
      ]
    }
  ```
</ResponseExample>


# By VIN
Source: https://smartcar.com/docs/api-reference/compatibility/by-vin

GET https://api.smartcar.com/v2.0/compatibility
Compatibility will vary by model, year, and trim. This API is for reference purposes only and it showcases vehicle makes and models that may be compatible with Smartcar and it does not guarantee that a specific vehicle will be compatible.

<Info>
  The Compatibility API is an Enterprise feature. Please [contact us](https://smartcar.com/pricing/) to upgrade your plan.
</Info>

Compatibility by VIN allows developers to determine if a specific vehicle could be compatible with Smartcar.

A vehicle is capable of a given feature if:

1. The vehicle supports the feature (e.g., a Ford Escape supports /fuel but a Mustang Mach-e does not)
2. Smartcar supports the feature for the vehicle's make

This endpoint only supports checking capabilities for vehicles sold in the United States. It **does not** support checking `capabilities` for VINs in Canada and Europe.

## Request

**Headers**

<Snippet file="header-basic-auth.mdx" />

**Parameters**

<ParamField query="vin" type="string" required>
  The VIN (Vehicle Identification Number) of the vehicle.
</ParamField>

<ParamField query="scope" type="string" required>
  A space-separated list of permissions.
</ParamField>

<ParamField query="country" default="US" type="string">
  An optional country code string according to ISO 3166-1 alpha-2.
</ParamField>

<RequestExample />

## Response

<ResponseField name="compatible" type="boolean">
  `true` if the vehicle is likely compatible, `false` otherwise.
</ResponseField>

<ResponseField name="reason" type="string | null">
  One of the reasons described below if compatible is `false`, `null` otherwise

  <Expandable title="reasons">
    <ResponseField name="VEHICLE_NOT_COMPATIBLE">
      The vehicle does not have the hardware required for internet connectivity
    </ResponseField>

    <ResponseField name="MAKE_NOT_COMPATIBLE">
      Smartcar is not yet compatible with the vehicle's make in the specified country
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="capabilities" type="array">
  An array containing capability objects for the set of endpoints that the provided scope value can provide authorization for.
  This array will be empty if `compatible` is `false`.

  <Expandable title="Capability object">
    <ResponseField name="permission" type="string">
      One of the permissions provided in the scope parameter
    </ResponseField>

    <ResponseField name="endpoint" type="string">
      One of the endpoints that the permission authorizes access to
    </ResponseField>

    <ResponseField name="capable" type="boolean">
      `true` if the vehicle is likely capable of this feature, `false` otherwise
    </ResponseField>

    <ResponseField name="reason" type="string | null">
      One of the reasons described below if capable is `false`, `null` otherwise

      <Expandable title="reasons">
        <ResponseField name="VEHICLE_NOT_CAPABLE">
          The vehicle does not support this feature
        </ResponseField>

        <ResponseField name="SMARTCAR_NOT_CAPABLE">
          Smartcar is not capable of supporting the given feature on the vehicle's make
        </ResponseField>
      </Expandable>
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseExample>
  ```json Example Response theme={null}
    {
    "compatible": true,
    "reason": null,
    "capabilities": [
      {
        "capable": false,
        "endpoint": "/engine/oil",
        "permission": "read_engine_oil",
        "reason": "SMARTCAR_NOT_CAPABLE"
      },
      {
        "capable": true,
        "endpoint": "/battery",
        "permission": "read_battery",
        "reason": null
      },
      {
        "capable": true,
        "endpoint": "/battery/capacity",
        "permission": "read_battery",
        "reason": null
      },
      {
        "capable": true,
        "endpoint": "/vin",
        "permission": "read_vin",
        "reason": null
      }
    ]
  }
  ```
</ResponseExample>

<Info>
  A vehicle's compatibility depends on many factors such as its make, model, model year, trim, etc. The API optimizes returning false positives.
</Info>


# Lock & Unlock
Source: https://smartcar.com/docs/api-reference/control-lock-unlock

POST https://api.smartcar.com/v2.0/vehicles/{id}/security
Lock or unlock the vehicle.

<Note>
  2.0 is still the only supported version for sending remote commands. If you need to send commands, please continue using v2.0 until commands are supported in the latest version later this year.
</Note>

## Permission

`control_security`

## Request

**Path**

<Snippet file="api-reference/path-vehicle-id.mdx" />

**Body**

<ParamField body="action" type="string" initialValue="UNLOCK" required>
  `LOCK` or `UNLOCK` the vehicle’s doors.
</ParamField>

<RequestExample>
  <Snippet file="api-reference/core-sdk-methods/control-lock-unlock.mdx" />
</RequestExample>

## Response

<ResponseField name="status" type="string">
  If the request is successful, Smartcar will return “success” (HTTP 200 status).
</ResponseField>

<ResponseField name="message" type="string">
  If the request is successful, Smartcar will return a message (HTTP 200 status).
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
      "message": "Successfully sent request to vehicle",
      "status": "success"
  }
  ```
</ResponseExample>


# Start & Stop Charge
Source: https://smartcar.com/docs/api-reference/evs/control-charge

POST https://api.smartcar.com/v2.0/vehicles/{id}/charge
Start or stop the vehicle charging.

<Note>
  2.0 is still the only supported version for sending remote commands. If you need to send commands, please continue using v2.0 until commands are supported in the latest version later this year.
</Note>

## Permission

`control_charge`

## Request

**Path**

<Snippet file="api-reference/path-vehicle-id.mdx" />

**Body**

<ParamField body="action" type="string" initialValue="START" required>
  `START` or `STOP` the vehicle charging.
</ParamField>

<RequestExample>
  <Snippet file="api-reference/core-sdk-methods/control-charge.mdx" />
</RequestExample>

## Response

<ResponseField name="status" type="string">
  If the request is successful, Smartcar will return “success”.
</ResponseField>

<ResponseField name="message" type="string">
  If the request is successful, Smartcar will return a message.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
      {
          "message": "Successfully sent request to vehicle",
          "status": "success"
      }   
  ```
</ResponseExample>

## Notes

**BMW and MINI**<br />
Vehicle needs to be on OS Version 8+

**Ford and Lincoln**<br />
Issuing a start command while the vehicle has a schedule in place for its current charging location will result in the vehicle charging to 100%.

Please see [charge schedule by location](/api-reference/ford/set-charge-schedule-by-location) for details on setting a charge limit with preferred charging times
or clearing schedules.

**Nissan**<br />
Currently only START charge commands are supported in the US. See [Set Charge Schedule](/api-reference/nissan/set-charge-schedule) for details on setting a charge schedule for Nissan vehicles.

**Chevrolet, GMC, Buick and Cadillac**<br />
These vehicles require a minimum charge of 50% in order to be able to start or stop charging via the API.


# Battery Level
Source: https://smartcar.com/docs/api-reference/evs/get-battery-level

GET https://api.smartcar.com/v2.0/vehicles/{id}/battery
Returns the state of charge and the remaining range of an electric vehicle's high voltage battery.

## Permission

`read_battery`

<Warning>
  The Vehicles API v2.0 will be deprecated by **Q3 of 2026**. We recommend migrating to the [latest version](/api-reference/vehicles-api-intro) as soon as possible to ensure continued support and access to new features.
</Warning>

<Note>
  This endpoint is only available for BEVs and PHEVs.
</Note>

## Request

**Path**

<Snippet file="api-reference/path-vehicle-id.mdx" />

<RequestExample>
  <Snippet file="api-reference/core-sdk-methods/get-battery-level.mdx" />
</RequestExample>

## Response

<ResponseField name="percentRemaining" type="number">
  The EV's state of charge as a percentage.
</ResponseField>

<ResponseField name="range" type="number" default="kilometers">
  The estimated remaining distance the vehicle can travel powered by its high voltage battery.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
      "percentRemaining": 0.3,
      "range": 40.5
  }
  ```
</ResponseExample>


# Charge Limit
Source: https://smartcar.com/docs/api-reference/evs/get-charge-limit

GET https://api.smartcar.com/v2.0/vehicles/{id}/charge/limit
Returns the charge limit configuration for the vehicle.

<Warning>
  The Vehicles API v2.0 will be deprecated by **Q3 of 2026**. We recommend migrating to the [latest version](/api-reference/vehicles-api-intro) as soon as possible to ensure continued support and access to new features.
</Warning>

## Permission

`read_charge`

## Request

**Path**

<Snippet file="api-reference/path-vehicle-id.mdx" />

<RequestExample>
  <Snippet file="api-reference/core-sdk-methods/get-charge-limit.mdx" />
</RequestExample>

## Response

<ResponseField name="limit" type="number">
  The level at which the vehicle will stop charging and be considered fully charged as a percentage.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
      "limit": 0.8,
  }
  ```
</ResponseExample>

## Notes

This endpoint will return a [`CHARGING_PLUG_NOT_CONNECTED`](/errors/api-errors/vehicle-state-errors#charging-plug-not-connected)
error if the OEM is unable to provide a charge limit unless the vehicle is plugged in.

**Ford and Lincoln**<br />
If a vehicle starts charging as a result of a [start charge](/api-reference/evs/control-charge) request, this endpoint will always return `1` if the charging location has a schedule in place.

For the vehicle to respect its charge limit, please set one along with preferred charge times or clear the schedule through through the [charge schedule by location](/api-reference/ford/set-charge-schedule-by-location) endpoint.

**BMW and MINI**<br />
Vehicle needs to be on OS Version 8+


# Charge Status
Source: https://smartcar.com/docs/api-reference/evs/get-charge-status

GET https://api.smartcar.com/v2.0/vehicles/{id}/charge
Returns the charge status for the vehicle.

<Warning>
  The Vehicles API v2.0 will be deprecated by **Q3 of 2026**. We recommend migrating to the [latest version](/api-reference/vehicles-api-intro) as soon as possible to ensure continued support and access to new features.
</Warning>

## Permission

`read_charge`

## Request

**Path**

<Snippet file="api-reference/path-vehicle-id.mdx" />

<RequestExample>
  <Snippet file="api-reference/core-sdk-methods/get-charge-status.mdx" />
</RequestExample>

## Response

<ResponseField name="isPluggedIn" type="bool">
  Indicates whether a charging cable is currently plugged into the vehicle’s charge port.
</ResponseField>

<ResponseField name="state" type="string">
  Returns the current charge status of a vehicle. A vehicle can be `FULLY_CHARGED` at less than 100% SoC if its [Charge Limit](/api-reference/evs/get-charge-limit) is less than `1`.

  <Expandable title="states">
    <ResponseField name="CHARGING" />

    <ResponseField name="FULLY_CHARGED" />

    <ResponseField name="NOT_CHARGING" />
  </Expandable>
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
      "isPluggedIn": true,
      "state": "FULLY_CHARGED"
  }
  ```
</ResponseExample>


# Charge Limit
Source: https://smartcar.com/docs/api-reference/evs/set-charge-limit

POST https://api.smartcar.com/v2.0/vehicles/{id}/charge/limit
Set the  charge limit of an electric vehicle.

<Note>
  2.0 is still the only supported version for sending remote commands. If you need to send commands, please continue using v2.0 until commands are supported in the latest version later this year.
</Note>

## Permission

`control_charge`

## Request

**Path**

<Snippet file="api-reference/path-vehicle-id.mdx" />

**Body**

<ParamField body="limit" type="number" initialValue="0.7" required>
  The level at which the vehicle should stop charging and be considered fully charged.
  Cannot be less than `0.5`, or greater than `1`.
</ParamField>

<RequestExample>
  <Snippet file="api-reference/core-sdk-methods/set-charge-limit.mdx" />
</RequestExample>

## Response

<ResponseField name="status" type="string">
  If the request is successful, Smartcar will return “success” (HTTP 200 status).
</ResponseField>

<ResponseField name="message" type="string">
  If the request is successful, Smartcar will return a message (HTTP 200 status).
</ResponseField>

## Notes

This endpoint will return a [`CHARGING_PLUG_NOT_CONNECTED`](/errors/api-errors/vehicle-state-errors#charging-plug-not-connected) error if
the OEM is unable to set a charge limit while the vehicle is unpluged.

**Ford and Lincoln**<br />
If a vehicle starts charging as a result of a [start charge](/api-reference/evs/control-charge) request it will always charge to 100%
if the charging location has a schedule in place.

For the vehicle to respect its charge limit, please set one along with preferred charge
times or clear the schedule through the [charge schedule by location](/api-reference/ford/set-charge-schedule-by-location) endpoint.

**BMW and MINI**<br />
Vehicle needs to be on OS Version 8+

<ResponseExample>
  ```json Example Response  theme={null}
  {
      "message": "Successfully sent request to vehicle",
      "status": "success"
  }   
  ```
</ResponseExample>


# Charge Schedule by Location
Source: https://smartcar.com/docs/api-reference/ford/get-charge-schedule-by-location

GET https://api.smartcar.com/v2.0/vehicles/{id}/{make}/charge/schedule_by_location
Returns all saved charging locations for a vehicle and their associated charging limits, schedules and configurations.

<Snippet file="api-reference/note-bse-ford.mdx" />

## Permission

`read_charge_locations`

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/charge/schedule_by_location" \
  -H "Authorization: Bearer {token}" \
  -X "GET"
  ```

  ```python Python theme={null}
  chargeScheduleByLocation = vehicle.request(
          "GET", 
          "{make}/charge/schedule_by_location"
      )
  ```

  ```js Node theme={null}
  const chargeScheduleByLocation = await vehicle.request(
          "GET", 
          "{make}/charge/schedule_by_location"
      );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("GET")
        .path("{make}/charge/schedule_by_location")
        .build();
  VehicleResponse getChargeScheduleByLocation = vehicle.request(request)
  ```

  ```ruby Ruby theme={null}
  chargeScheduleByLocation = vehicle.request(
          "GET", 
          "{make}/charge/schedule_by_location"
      )
  ```
</RequestExample>

## Response

<ResponseField name="chargingLocations" type="[object] | [empty]">
  An array of charging locations. Empty if none are currently set on the vehicle.

  <Expandable>
    <ResponseField name="chargeLimit" type="number">
      The maximum charge limit for the vehicle at the location as a percent.
    </ResponseField>

    <ResponseField name="location" type="object">
      The latitude and longitude of the charging location.

      <Expandable title="location">
        <ResponseField name="longitude" type="number">
          The longitude of the charging location.
        </ResponseField>

        <ResponseField name="latitude" type="number">
          The latitude of the charging location.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="chargingSchedules" type="object">
      The weekday and weekend charging schedules for the vehicle at the location.

      <Expandable>
        <ResponseField name="weekday" type="[object] | [empty]">
          The charging schedule for the vehicle on weekdays (Monday - Friday).

          <Expandable>
            <ResponseField name="start" type="string">
              The exact hour a vehicle should start charging in HH:00 e.g. 17:00.
            </ResponseField>

            <ResponseField name="end" type="string">
              The exact hour a vehicle should stop charging in HH:00 e.g. 21:00.
            </ResponseField>
          </Expandable>
        </ResponseField>

        <ResponseField name="weekend" type="[object] | [empty]">
          The charging schedule for the vehicle on weekends (Saturday - Sunday).

          <Expandable>
            <ResponseField name="start" type="string">
              The exact hour a vehicle should start charging in HH:00 e.g. 17:00.
            </ResponseField>

            <ResponseField name="end" type="string">
              The exact hour a vehicle should stop charging in HH:00 e.g. 21:00.
            </ResponseField>
          </Expandable>
        </ResponseField>
      </Expandable>
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
    "chargingLocations": [
      {
        "chargeLimit": 0.8,
        "chargingSchedules": {
          "weekday": [
            {
              "end": "17:00",
              "start": "09:00"
            }
          ],
          "weekend": [
            {
              "end": "17:00",
              "start": "09:00"
            }
          ]
        },
        "location": {
          "latitude": 48.8566,
          "longitude": 2.3522
        }
      }
    ]
  }
  ```
</ResponseExample>

## Example Schedule States

<AccordionGroup>
  <Accordion title="Vehicle will charge at any time">
    ```json  theme={null}
    {
      "chargingLocations": [
        {
          "chargeLimit": 0.8,
          "chargingSchedules": {
            "weekday": [],
            "weekend": []
          },
          "location": {
            "latitude": 48.8566,
            "longitude": 2.3522
          }
        }
      ]
    }
    ```
  </Accordion>

  <Accordion title="Vehicle has a schedule for Weekdays only">
    ```json  theme={null}
    {
      "chargingLocations": [
        {
          "chargeLimit": 0.8,
          "chargingSchedules": {
            "weekday": [
              {
                "end": "17:00",
                "start": "09:00"
              }
            ],
            "weekend": []
          },
          "location": {
            "latitude": 48.8566,
            "longitude": 2.3522
          }
        }
      ]
    }
    ```
  </Accordion>

  <Accordion title="Vehicle has a schedule for Weekends only">
    ```json  theme={null}
    {
        "chargingLocation" : {   
            "chargeLimit": 0.9, 
            "chargingSchedules": {
                "weekday": [], 
                "weekend": [
                    {   
                        "start": "16:00", 
                        "end": "07:00"
                    }
                ]
            }
        }
    }
    ```
  </Accordion>
</AccordionGroup>


# Charge Schedule by Location
Source: https://smartcar.com/docs/api-reference/ford/set-charge-schedule-by-location

PUT https://api.smartcar.com/v2.0/vehicles/{id}/{make}/charge/schedule_by_location
Set all schedules for the specified charging location.

<Snippet file="api-reference/note-bse-ford.mdx" />

## Permission

`control_charge`

## Request

<Info>
  In order to set a schedule, you must use a location from the [`GET Charge Schedule by Location`](/api-reference/ford/get-charge-schedule-by-location) endpoint.
  If the location you want to manage is not in the response, the vehicle owner has not charged at that location within the last 90 days and it has been
  removed from their app's saved charging location list.
</Info>

**Path**

<Snippet file="api-reference/path-bse.mdx" />

**Query**

<ParamField query="longitude" type="number" required>
  The longitude of a charging location from [`GET Charge Schedule by Location`](/api-reference/ford/get-charge-schedule-by-location)
</ParamField>

<ParamField query="latitude" type="number" required>
  The latitude of a charging location from [`GET Charge Schedule by Location`](/api-reference/ford/get-charge-schedule-by-location)
</ParamField>

**Body**

<ParamField body="chargingLocation" type="object" required>
  <Expandable defaultOpen="true" title="chargingLocation">
    <ParamField body="chargeLimit" type="number" required>
      The maximum charge limit for the vehicle at the location as a percent between `0.5` and `1`.
    </ParamField>

    <ParamField body="chargingWindows" type="object" required>
      The weekday and weekend charging schedules for the vehicle at the location.

      <Expandable defaultOpen="true">
        <ParamField body="weekday" type="[object]" required>
          The charging schedule for the vehicle on weekdays (Monday - Friday).

          <Expandable defaultOpen="true">
            <ParamField body="start" type="string" required>
              The exact hour a vehicle should start charging in HH:00 e.g. 17:00.
            </ParamField>

            <ParamField body="end" type="string" required>
              The exact hour a vehicle should stop charging in HH:00 e.g. 21:00.
            </ParamField>
          </Expandable>
        </ParamField>

        <ParamField body="weekend" type="[object]" required>
          The charging schedule for the vehicle on weekends (Saturday - Sunday).

          <Expandable defaultOpen="true">
            <ParamField body="start" type="string" required>
              The exact hour a vehicle should start charging in HH:00 e.g. 17:00.
            </ParamField>

            <ParamField body="end" type="string" required>
              The exact hour a vehicle should stop charging in HH:00 e.g. 21:00.
            </ParamField>
          </Expandable>
        </ParamField>
      </Expandable>
    </ParamField>
  </Expandable>
</ParamField>

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/charge/schedule_by_location?longitude=2.3522&latitude=48.8566" \
      -H "Authorization: Bearer {token}" \
      -X "PUT" \
      -H "Content-Type: application/json" \
      -d '{chargingLocation:{"chargeLimit": 0.9, "chargingWindows": {"weekday": [{"start": "09:00", "end": "17:00"}], "weekend": [{"start": "09:00", "end": "17:00"}]}}}'
  ```

  ```python Python theme={null}
  setChargeScheduleByLocation = vehicle.request(
          "PUT", 
          "{make}/charge/schedule_by_location?longitude=2.3522&latitude=48.8566", 
          {
            "chargingLocation" : {   
                "chargeLimit": 0.9, 
                "chargingWindows": {
                    "weekday": [
                        {   
                            "start": "09:00", 
                            "end": "10:00"
                        }
                    ], 
                    "weekend": [
                        {   
                            "start": "09:00", 
                            "end": "10:00"
                        }
                    ]
                }
            }
        }
      )
  ```

  ```js Node theme={null}
  const setChargeScheduleByLocation = vehicle.request(
        "PUT", 
        "{make}/charge/schedule_by_location?longitude=2.3522&latitude=48.8566", 
        {
          "chargingLocation" : {   
              "chargeLimit": 0.9, 
              "chargingWindows": {
                  "weekday": [
                      {   
                          "start": "09:00", 
                          "end": "10:00"
                      }
                  ], 
                  "weekend": [
                      {   
                          "start": "09:00", 
                          "end": "10:00"
                      }
                  ]
              }
          }
        }
      );
  ```

  ```java Java theme={null}
  JsonArrayBuilder weekday = Json.createArrayBuilder().add(
      Json.createObjectBuilder().add("start", "05:00").add("end", "07:00"));

  JsonArrayBuilder weekend = Json.createArrayBuilder().add(
      Json.createObjectBuilder().add("start", "06:00").add("end", "07:00"));

  JsonObject chargingWindows = Json.createObjectBuilder()
                                      .add("weekday", weekday)
                                      .add("weekend", weekend)
                                      .build();

  JsonObject chargingLocation = Json.createObjectBuilder()
                                      .add("chargeLimit", 1.0)
                                      .add("chargingWindows", chargingWindows)
                                      .build();

  SmartcarVehicleRequest request =
      new SmartcarVehicleRequest.Builder()
          .method("PUT")
          .path("ford/charge/schedule_by_location")
          .addQueryParameter("latitude", "37.749008")
          .addQueryParameter("longitude", "-122.46981")
          .addBodyParameter("chargingLocation", chargingLocation)
          .build();

  VehicleResponse chargeSched = vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  setChargeScheduleByLocation = vehicle.request(
        "PUT", 
        "{make}/charge/schedule_by_location?longitude=2.3522&latitude=48.8566", 
        {
          "chargingLocation" : {   
              "chargeLimit": 0.9, 
              "chargingWindows": {
                  "weekday": [
                      {   
                          "start": "09:00", 
                          "end": "10:00"
                      }
                  ], 
                  "weekend": [
                      {   
                          "start": "09:00", 
                          "end": "10:00"
                      }
                  ]
              }
          }
        }
      )
  ```
</RequestExample>

## Response

<ResponseField name="message" type="string">
  If the request is successful, Smartcar will return a message.
</ResponseField>

<ResponseField name="status" type="string">
  If the request is successful, Smartcar will return `success`.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
    "message": "Successfully sent request to vehicle",
    "status": "success"
  }
  ```
</ResponseExample>

## Example Request Bodies

<AccordionGroup>
  <Accordion title="Set a schedule for Weekdays and Weekends">
    ```json  theme={null}
    {
      "chargingLocation" : {   
          "chargeLimit": 0.9, 
          "chargingWindows": {
              "weekday": [
                  {   
                      "start": "17:00", 
                      "end": "06:00"
                  }
              ], 
              "weekend": [
                  {   
                      "start": "16:00", 
                      "end": "07:00"
                  }
              ]
          }
      }
    }
    ```
  </Accordion>

  <Accordion title="Set a schedule for only Weekdays">
    ```json  theme={null}
    {
      "chargingLocation" : {   
          "chargeLimit": 0.9, 
          "chargingWindows": {
              "weekday": [
                  {   
                      "start": "17:00", 
                      "end": "06:00"
                  }
              ], 
              "weekend": []
          }
      }
    }
    ```
  </Accordion>

  <Accordion title="Set a schedule for only Weekends">
    ```json  theme={null}
    {
        "chargingLocation" : {   
            "chargeLimit": 0.9, 
            "chargingWindows": {
                "weekday": [], 
                "weekend": [
                    {   
                        "start": "16:00", 
                        "end": "07:00"
                    }
                ]
            }
        }
    }
    ```
  </Accordion>

  <Accordion title="Clear schedules">
    ```json  theme={null}
    {
        "chargingLocation" : {   
            "chargeLimit": 0.9, 
            "chargingWindows": {
                "weekday": [], 
                "weekend": []
            }
        }
    }
    ```
  </Accordion>
</AccordionGroup>


# Diagnostic Trouble Codes
Source: https://smartcar.com/docs/api-reference/get-dtcs

GET https://api.smartcar.com/v2.0/vehicles/{id}/diagnostics/dtcs
Provides a list of active Diagnostic Trouble Codes (DTCs) reported by the vehicle. Currently supporting GM brands including Chevrolet and GMC.

<Warning>
  The Vehicles API v2.0 will be deprecated by **Q3 of 2026**. We recommend migrating to the [latest version](/api-reference/vehicles-api-intro) as soon as possible to ensure continued support and access to new features.
</Warning>

## Permission

`read_diagnostics`

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/diagnostics/dtcs" \
      -H "Authorization: Bearer {token}" \
      -X "GET"
  ```

  ```python Python theme={null}
  diagnostic_trouble_codes = vehicle.diagnostic_trouble_codes()
  ```

  ```js Node theme={null}
  const diagnosticTroubleCodes = await vehicle.diagnosticTroubleCodes();
  ```

  ```java Java theme={null}
  VehicleDiagnosticTroubleCodes diagnosticTroubleCodes = vehicle.diagnosticTroubleCodes();
  ```

  ```ruby Ruby theme={null}
  diagnostic_trouble_codes = vehicle.diagnostic_trouble_codes
  ```
</RequestExample>

## Request

**Path**

<Snippet file="api-reference/path-vehicle-id.mdx" />

## Response

<ResponseField name="activeCodes" type="array">
  Array of active diagnostic trouble codes.

  <Expandable>
    <ResponseField name="code" type="string">
      The Diagnostic Trouble Code reported by the vehicle.
    </ResponseField>

    <ResponseField name="timestamp" type="timestamp">
      The date and time the trouble code last became active.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
    {
      "activeCodes": [
        {
          "code": "P302D",
          "timestamp": "2024-09-05T14:48:00.000Z"
        },
        {
          "code": "xxxxx",
          "timestamp": null
        }
        
        ... 
      ]
    }
  ```
</ResponseExample>


# Oil Life
Source: https://smartcar.com/docs/api-reference/get-engine-oil-life

GET https://api.smartcar.com/v2.0/vehicles/{id}/engine/oil
Returns the remaining life span of a vehicle’s engine oil.

<Warning>
  The Vehicles API v2.0 will be deprecated by **Q3 of 2026**. We recommend migrating to the [latest version](/api-reference/vehicles-api-intro) as soon as possible to ensure continued support and access to new features.
</Warning>

## Permission

`read_engine_oil`

## Request

**Path**

<Snippet file="api-reference/path-vehicle-id.mdx" />

<RequestExample>
  <Snippet file="api-reference/core-sdk-methods/get-engine-oil-life.mdx" />
</RequestExample>

## Response

<ResponseField name="lifeRemaining" type="number">
  The engine oil’s remaining life span based on the current quality of the oil as a percentage.
  `1` indicates the oil was changed recently and `0` indicates the oil should be changed immediately.
  It is not a representation of how much oil is left in the vehicle.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
    "lifeRemaining": 0.35
  }
  ```
</ResponseExample>


# Fuel Tank
Source: https://smartcar.com/docs/api-reference/get-fuel-tank

GET https://api.smartcar.com/v2.0/vehicles/{id}/fuel
Returns the status of the fuel remaining in the vehicle’s fuel tank.

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


# Location
Source: https://smartcar.com/docs/api-reference/get-location

GET https://api.smartcar.com/v2.0/vehicles/{id}/location
Returns the vehicle's last known location.

<Warning>
  The Vehicles API v2.0 will be deprecated by **Q3 of 2026**. We recommend migrating to the [latest version](/api-reference/vehicles-api-intro) as soon as possible to ensure continued support and access to new features.
</Warning>

## Permission

`read_location`

## Request

**Path**

<Snippet file="api-reference/path-vehicle-id.mdx" />

<RequestExample>
  <Snippet file="api-reference/core-sdk-methods/get-location.mdx" />
</RequestExample>

## Response

<ResponseField name="latitude" type="number">
  The latitude in degrees.
</ResponseField>

<ResponseField name="longitude" type="number">
  The longitude in degrees.
</ResponseField>

<ResponseExample>
  ```json Example Response theme={null}
  {
    "latitude": 37.4292,
    "longitude": 122.1381
  }
  ```
</ResponseExample>


# Lock Status
Source: https://smartcar.com/docs/api-reference/get-lock-status

GET https://api.smartcar.com/v2.0/vehicles/{id}/security
Returns the lock status for a vehicle and the open status of its doors, windows, storage units, sunroof and charging port where available.

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


# Battery Capacity
Source: https://smartcar.com/docs/api-reference/get-nominal-capacity

GET https://api.smartcar.com/v2.0/vehicles/{id}/battery/nominal_capacity
Returns a list of nominal rated battery capacities for a vehicle.

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


# Odometer
Source: https://smartcar.com/docs/api-reference/get-odometer

GET https://api.smartcar.com/v2.0/vehicles/{id}/odometer
Returns the vehicle’s last known odometer reading.

<Warning>
  The Vehicles API v2.0 will be deprecated by **Q3 of 2026**. We recommend migrating to the [latest version](/api-reference/vehicles-api-intro) as soon as possible to ensure continued support and access to new features.
</Warning>

## Permission

`read_odometer`

## Request

**Path**

<Snippet file="api-reference/path-vehicle-id.mdx" />

<RequestExample>
  <Snippet file="api-reference/core-sdk-methods/get-odometer.mdx" />
</RequestExample>

## Response

<ResponseField name="distance" type="number" default="kilometers">
  The current odometer of the vehicle.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
    "distance": 104.32
  }
  ```
</ResponseExample>


# Service History
Source: https://smartcar.com/docs/api-reference/get-service-records

GET https://api.smartcar.com/v2.0/vehicles/{id}/service/history
Retrieve service records tracked by the vehicle's dealer or manually added by the vehicle owner. Currently supporting Ford, Lincoln, Toyota, Lexus, Mazda and Volkswagen (US)

<Warning>
  The Vehicles API v2.0 will be deprecated by **Q3 of 2026**. We recommend migrating to the [latest version](/api-reference/vehicles-api-intro) as soon as possible to ensure continued support and access to new features.
</Warning>

## Permission

`read_service_history`

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/service/history" \
  -H "Authorization: Bearer {token}" \
  -X "GET"
  ```

  ```python Python theme={null}
  service = vehicle.request(
        "GET", 
        "service/history"
  )
  ```

  ```js Node theme={null}
  const service = await vehicle.request(
        "GET", 
        "service/history"
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("GET")
        .path("service/history")
        .build();
  VehicleResponse service =vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  Service = vehicle.request(
        "GET", 
        "service/history"
  )
  ```
</RequestExample>

## Request

**Path**

<Snippet file="api-reference/path-vehicle-id.mdx" />

## Response

<ResponseField name="serviceID" type="string | null">
  A unique identifier of the service record.
</ResponseField>

<ResponseField name="serviceDate" type="timestamp | null">
  The date and time the vehicle was serviced
</ResponseField>

<ResponseField name="odometerDistance" type="string | null">
  The odometer of the vehicle at time of service in kilometers.
</ResponseField>

<Expandable title="serviceTasks" description="An overview of specific tasks completed in the service event.">
  <ResponseField name="taskID" type="string | null">
    The unique identifier of the tasks completed as part of the service event.
  </ResponseField>

  <ResponseField name="taskDescription" type="string | null">
    Tasks completed as part of the service event. Note that not all makes provide service tasks.
  </ResponseField>
</Expandable>

Additional service details.

<Expandable title="service details">
  <ResponseField name="type" type="string | null">
    Indicates if the service event was completed by a dealership or manually entered by the vehicle owner.
  </ResponseField>
</Expandable>

An overview of service costs.

<Expandable title="service cost">
  <ResponseField name="totalCost" type="string | null">
    The total cost of the service event. Note that not all makes provide service cost.
  </ResponseField>

  <ResponseField name="currency" type="string | null">
    Identifies the currency used for service cost.
  </ResponseField>
</Expandable>

<ResponseExample>
  ```json Example Response  theme={null}
  {
        "serviceId": null,
        "odometerDistance": 46047.22,
        "serviceDate": "2023-06-28T22:21:41.583Z",
        "serviceTasks": [
              {
              "taskId": "3262",
              "taskDescription": "Service Task 0"
              },
              {
              "taskId": "3041",
              "taskDescription": null
              },
              {
              "taskId": null,
              "taskDescription": null
              }
        ],
        "serviceDetails": [
              {
              "type": "Service Details Type 0",
              "value": "Service Details Value 0"
              },
              {
              "type": "Service Details Type 1",
              "value": null
              }
        ],
        "serviceCost": {
              "totalCost": null,
              "currency": null
        }
  }
  ```
</ResponseExample>


# Signal
Source: https://smartcar.com/docs/api-reference/get-signal

get /vehicles/{vehicleId}/signals/{signalCode}
Get a specific Signal for a Vehicle.



# Signals
Source: https://smartcar.com/docs/api-reference/get-signals

get /vehicles/{vehicleId}/signals
Get all available Signals for a Vehicle



# System Status
Source: https://smartcar.com/docs/api-reference/get-system-status

GET https://api.smartcar.com/v2.0/vehicles/{id}/diagnostics/system_status
Provides a list of vehicle systems and their current health status. Currently supporting FCA and GM brands including RAM, Jeep, Chrysler, Dodge, Fiat, Alfa Romeo, Buick, Cadillac, Chevrolet and GMC. See [Diagnostic Systems](/docs/help/diagnostic-systems) for a complete list of Smartcar System IDs.

<Warning>
  The Vehicles API v2.0 will be deprecated by **Q3 of 2026**. We recommend migrating to the [latest version](/api-reference/vehicles-api-intro) as soon as possible to ensure continued support and access to new features.
</Warning>

## Permission

`read_diagnostics`

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/diagnostics/system_status" \\
      -H "Authorization: Bearer {token}" \\
      -X "GET"
  ```

  ```python Python theme={null}
  diagnostic_system_status = vehicle.diagnostic_system_status()
  ```

  ```js Node theme={null}
  const diagnosticSystemStatus = await vehicle.diagnosticSystemStatus();
  ```

  ```java Java theme={null}
  VehicleDiagnosticSystemStatus diagnosticSystemStatus = vehicle.diagnosticSystemStatus();
  ```

  ```ruby Ruby theme={null}
  diagnostic_system_status = vehicle.diagnostic_system_status
  ```
</RequestExample>

## Request

**Path**

<Snippet file="api-reference/path-vehicle-id.mdx" />

## Response

<ResponseField name="systems" type="array">
  An overview of systems reported by the vehicle.
</ResponseField>

<ResponseField name="systemID" type="string">
  The unique identifier of a system reported by the vehicle.
</ResponseField>

<ResponseField name="status" type="string">
  The status of a vehicle, expected as "OK" or "ALERT".
</ResponseField>

<ResponseField name="description" type="string | null">
  A plain-text description of the status, if available.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
        "systems": [
            {
                // System ID from Smartcar unified system definition list
                "systemId": "SYSTEM_TPMS",
                "status": "ALERT",
                "description": "Left rear tire sensor battery low"
            },
            {
                "systemId": "SYSTEM_AIRBAG",
                "status": "OK",
                "description": null
            },
            {
                "systemId": "SYSTEM_MIL",
                "status": "OK",
                "description": null
            },
            ...
        ]
  }
  ```
</ResponseExample>


# Tire Pressure
Source: https://smartcar.com/docs/api-reference/get-tire-pressure

GET https://api.smartcar.com/v2.0/vehicles/{id}/tires/pressure
Returns the air pressure of each of the vehicle’s tires.

<Warning>
  The Vehicles API v2.0 will be deprecated by **Q3 of 2026**. We recommend migrating to the [latest version](/api-reference/vehicles-api-intro) as soon as possible to ensure continued support and access to new features.
</Warning>

## Permission

`read_tires`

## Request

**Path**

<Snippet file="api-reference/path-vehicle-id.mdx" />

<RequestExample>
  <Snippet file="api-reference/core-sdk-methods/get-tire-pressure.mdx" />
</RequestExample>

## Response

<ResponseField name="frontLeft" type="number" default="kilopascals">
  The current air pressure of the front left tire.
</ResponseField>

<ResponseField name="frontRight" type="number" default="kilopascals">
  The current air pressure of the front right tire.
</ResponseField>

<ResponseField name="backLeft" type="number" default="kilopascals">
  The current air pressure of the back left tire.
</ResponseField>

<ResponseField name="backRight" type="number" default="kilopascals">
  The current air pressure of the back right tire.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
      "backLeft": 219.3,
      "backRight": 219.3,
      "frontLeft": 219.3,
      "frontRight": 219.3
  }
  ```
</ResponseExample>


# Vehicle
Source: https://smartcar.com/docs/api-reference/get-vehicle

get /vehicles/{vehicleId}
Get details for a single Vehicle.



# Vehicle Attributes
Source: https://smartcar.com/docs/api-reference/get-vehicle-info

GET https://api.smartcar.com/v2.0/vehicles/{id}
Returns a single vehicle object, containing identifying information.

<Warning>
  The Vehicles API v2.0 will be deprecated by **Q3 of 2026**. We recommend migrating to the [latest version](/api-reference/vehicles-api-intro) as soon as possible to ensure continued support and access to new features.
</Warning>

## Permission

`read_vehicle_info`

## Request

**Path**

<Snippet file="api-reference/path-vehicle-id.mdx" />

<RequestExample>
  <Snippet file="api-reference/core-sdk-methods/get-vehicle-info.mdx" />
</RequestExample>

## Response

<ResponseField name="id" type="string">
  The ID for the vehicle.
</ResponseField>

<ResponseField name="make" type="string">
  The manufacturer of the vehicle.
</ResponseField>

<ResponseField name="model" type="string">
  The model of the vehicle.
</ResponseField>

<ResponseField name="year" type="integer">
  The model year.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
      "id": "36ab27d0-fd9d-4455-823a-ce30af709ffc",
      "make": "TESLA",
      "model": "Model S",
      "year": "2014"
  }
  ```
</ResponseExample>


# VIN
Source: https://smartcar.com/docs/api-reference/get-vin

GET https://api.smartcar.com/v2.0/vehicles/{id}/vin
Returns the vehicle’s manufacturer identifier.

<Warning>
  The Vehicles API v2.0 will be deprecated by **Q3 of 2026**. We recommend migrating to the [latest version](/api-reference/vehicles-api-intro) as soon as possible to ensure continued support and access to new features.
</Warning>

## Permission

`read_vin`

## Request

**Path**

<Snippet file="api-reference/path-vehicle-id.mdx" />

<RequestExample>
  <Snippet file="api-reference/core-sdk-methods/get-vin.mdx" />
</RequestExample>

## Response

<ResponseField name="vin" type="string">
  The manufacturer unique identifier.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
    "vin": "5YJSA1CN5DFP00101"
  }
  ```
</ResponseExample>


# Charge Completion Time
Source: https://smartcar.com/docs/api-reference/gm/get-charge-completion-time

GET https://api.smartcar.com/v2.0/vehicles/{id}/{make}/charge/completion
When the vehicle is charging, returns the date and time the vehicle expects to "complete" this charging session.  When the vehicle is not charging, this endpoint results in a vehicle state error.

<Note>
  This endpoint is currently available for `cadillac` and `chevrolet`.
</Note>

## Permission

`read_charge`

## Request

<ParamField path="id" type="string" required>
  `vehicle_id` of the vehicle you are making the request to.
</ParamField>

<ParamField path="make" type="string" required>
  The make to pass in the URL.
</ParamField>

<RequestExample>
  <Snippet file="api-reference/bse/get-charge-completion-time.mdx" />
</RequestExample>

## Response

<ResponseField name="time" type="string">
  An ISO8601 formatted datetime (`YYYY-MM-DDTHH:mm:ss.SSSZ`) for the time at which the vehicle expects to complete this charging session.
</ResponseField>

<ResponseExample>
  ```json Example Response theme={null}
  {
    "time": "2022-01-13T22:52:55.358Z"
  }
  ```
</ResponseExample>


# Voltage
Source: https://smartcar.com/docs/api-reference/gm/get-charge-voltmeter

GET https://api.smartcar.com/v2.0/vehicles/{id}/{make}/charge/voltmeter
When the vehicle is plugged in, returns the charging voltage measured by the vehicle. When the vehicle is not plugged in, this endpoint results in a vehicle state error.

<Note>
  This endpoint is currently available for `cadillac` and `chevrolet`.
</Note>

## Permission

`read_charge`

## Request

<Snippet file="api-reference/path-bse.mdx" />

<RequestExample>
  <Snippet file="api-reference/bse/get-charge-voltmeter.mdx" />
</RequestExample>

## Response

<ResponseField name="voltage" type="number">
  The potential difference measured by the vehicle in volts (V).
</ResponseField>

<ResponseExample>
  ```json Example Response theme={null}
  {
    "voltage": 240
  }
  ```
</ResponseExample>


# Headers
Source: https://smartcar.com/docs/api-reference/headers



Smartcar uses the following headers for requests and responses.

## Request

<ParamField header="SC-Unit-System" type="string" default="metric">
  Smartcar supports both `metric` and `imperial` unit systems of measurement.
</ParamField>

<RequestExample>
  ```bash Request Headers theme={null}
  SC-Unit-System: metric
  ```
</RequestExample>

## Response

<ResponseField name="SC-Data-Age" type="string">
  Indicates the timestamp (ISO-8601 format) of when the returned data was recorded by the vehicle.
</ResponseField>

<ResponseField name="SC-Fetched-At" type="string">
  Indicates the timestamp (ISO-8601 format) of when Smartcar fetched the data from the OEM.
</ResponseField>

<ResponseField name="SC-Unit-System" type="string">
  Indicates whether the unit system used in the returned data is `imperial` or `metric`.
</ResponseField>

<ResponseField name="SC-Request-Id" type="string">
  Each response from Smartcar's API has a unique request identifier. If you need to contact us about a specific request, providing the request identifier will ensure the fastest possible resolution.
</ResponseField>

<ResponseExample>
  ```bash Response Headers theme={null}
  SC-Data-Age: 2018-06-20T01:33:37.078Z
  SC-Fetched-At: 2018-06-20T01:48:37.078Z
  SC-Unit-System: metric
  SC-Request-Id: 26c14915-0c26-43c5-8e42-9edfc2a66a0f
  ```
</ResponseExample>


# Smartcar APIs
Source: https://smartcar.com/docs/api-reference/intro

Here you'll find everything you need to integrate with Smartcar via REST APIs. Learn how to connect and manage Smartcar's Vehicles API, Management API, and Compatibility API through a simple interface.

Welcome to the Smartcar API Reference! Here you’ll find everything you need to integrate with Smartcar and build applications that can reach to millions of vehicles.

Smartcar provides three main APIs, each designed for a specific part of your integration:

## Vehicles API

The **Vehicles API** lets you access standardized vehicle data and send commands to connected vehicles. Use this API to:

* Retrieve signals such as battery level, odometer, location, and more
* Issue commands like lock/unlock or start/stop charging
* Access vehicle attributes and diagnostic information

All requests to the Vehicles API require an access token obtained via the [OAuth2 authorization flow](/getting-started/how-to/get-an-access-token).

The Vehicles API is designed primarily for exploration and non-frequent data retrieval. This API is not designed for continuous polling or real-time monitoring. Data is typically updated once every 24 hours unless the vehicle is actively subscribed to a webhook, which enables more frequent updates. For most use cases, you should avoid polling the Vehicles API at high frequency leverage [webhooks](/integrations/webhooks/overview) instead.

* [Vehicles API Reference](/api-reference/vehicles-api-intro)
* [Standard Signal Schema](/api-reference/signals/schema)
* [Permissions](/api-reference/permissions)

## Management API

The **Management API** allows you to manage vehicle connections at the application level. Use this API to:

* List all vehicles connected to your application
* Remove (disconnect) vehicles
* Unsubscribe vehicles from a webhook

The Management API uses a separate management token for authentication, which you can find in your [Smartcar Dashboard](https://dashboard.smartcar.com/).

* [Management API Reference](/api-reference/management/get-vehicle-connections)
* [Delete Vehicle Connections](/api-reference/management/delete-vehicle-connections)
* [Unsubscribe Webhook](/api-reference/webhooks/unsubscribe-webhook)

## Compatibility API

The **Compatibility API** helps you determine if a specific vehicle is supported by Smartcar before launching the Connect flow. Use this API to:

* Query supported makes and regions

This API is useful for improving user experience by verifying eligibility up front.

* [Compatibility by VIN](/api-reference/compatibility/by-vin)
* [Compatibility by Region and Make](/api-reference/compatibility/by-region-and-make)

***

<Card title="Starter app" icon="github-alt" href="https://github.com/smartcar/starter-app-react-node" horizontal="true">
  Easily connect a vehicle and make API requests using our starter app.
</Card>

<Card title="Postman" icon="rocket" href="https://www.postman.com/smartcar/smartcar-api/collection/fqmwehs/smartcar-api" horizontal="true">
  Get a feel for the API using our Postman collection.
</Card>


# Management API Overview
Source: https://smartcar.com/docs/api-reference/management-api-intro

The Management API allows you to manage vehicle connections and webhook subscriptions at the application level. It is designed for administrative tasks that go beyond individual vehicle data access.

## What You Can Do

* List all vehicles connected to your application
* Remove (disconnect) vehicles from your app
* Manage webhook subscriptions (subscribe/unsubscribe vehicles)

## Authentication

The Management API uses a management token, which you can generate in your [Smartcar Dashboard](https://dashboard.smartcar.com/).

## Base URL

```
https://api.smartcar.com/management/v2.0
```

## Key Resources

* [Get Vehicle Connections](/api-reference/management/get-vehicle-connections)
* [Delete Vehicle Connections](/api-reference/management/delete-vehicle-connections)
* [Webhook Management](/api-reference/webhooks/unsubscribe-webhook)

## Example Use Cases

* Removing vehicles when a user deletes their account
* Managing webhook event delivery
* Auditing connected vehicles for compliance

<Info>
  For more details on using the Management API, see [Management API Reference](/api-reference/management/get-vehicle-connections).
</Info>


# Vehicle Connections
Source: https://smartcar.com/docs/api-reference/management/delete-vehicle-connections

DELETE https://management.smartcar.com/v2.0/management/connections
Deletes all vehicle connections associated with a Smartcar user ID or a specific vehicle.

## Request

**Header**

<ParamField header="Authorization" type="string" required>
  In the format `Basic base64(default:{application_management_token})`. You can find your `application_management_token` under
  your Application Configuration in the Smartcar Dashboard.
</ParamField>

**Query**

<ParamField query="user_id" type="string" />

<ParamField query="vehicle_id" type="string" />

You can delete connections in three ways:

* Provide a `vehicle_id` to remove all connections for that vehicle across all users.
* Provide a `user_id` to remove all vehicles linked to that user.
* Provide both a `vehicle_id` and `user_id` to remove only that vehicle for that specific user.

<RequestExample>
  ```bash cURL theme={null}
    curl -X DELETE "https://management.smartcar.com/v2.0/management/connections/?user_id=UUID12345&vehicle_id=UUID67890" \
    -H "Authorization: Basic $(echo -n "default:$SMARTCAR_APP_MANAGEMENT_TOKEN" | base64)"
  ```

  ```python Python theme={null}
    import os
    import base64
    import requests

    user_id = "UUID12345"
    vehicle_id = "UUID67890"
    token = os.getenv("SMARTCAR_APP_MANAGEMENT_TOKEN")

    auth_header = base64.b64encode(f"default:{token}".encode()).decode()
    headers = {
        "Authorization": f"Basic {auth_header}",
        "Content-Type": "application/json",
    }

    url = (
        "https://management.smartcar.com/v2.0/management/connections/"
        f"?user_id={user_id}&vehicle_id={vehicle_id}"
    )

    response = requests.delete(url, headers=headers)
  ```

  ```javascript Node theme={null}
    const basicAuth = Buffer.from(`default:${process.env.SMARTCAR_APP_MANAGEMENT_TOKEN}`).toString('base64');
    const disconnectResponse = await fetch(
    `https://management.smartcar.com/v2.0/management/connections/?user_id=${smartcar_user_id}&vehicle_id=${smartcar_vehicle_id}`,
    {
        method: 'DELETE',
        headers: {
          'Authorization': `Basic ${basicAuth}`,
          'Content-Type': 'application/json',
        },
      }
    );
  ```

  ```java Java theme={null}
    import java.net.HttpURLConnection;
    import java.net.URL;
    import java.util.Base64;

    String userId = "UUID12345";
    String vehicleId = "UUID67890";
    String token = System.getenv("SMARTCAR_APP_MANAGEMENT_TOKEN");
    String auth = Base64.getEncoder().encodeToString(("default:" + token).getBytes());

    URL url = new URL("https://management.smartcar.com/v2.0/management/connections/?user_id=" + userId + "&vehicle_id=" + vehicleId);
    HttpURLConnection conn = (HttpURLConnection) url.openConnection();
    conn.setRequestMethod("DELETE");
    conn.setRequestProperty("Authorization", "Basic " + auth);
    conn.setRequestProperty("Content-Type", "application/json");

    int responseCode = conn.getResponseCode();
  ```

  ```ruby Ruby theme={null}
    require 'net/http'
    require 'uri'
    require 'base64'

    user_id = "UUID12345"
    vehicle_id = "UUID67890"
    token = ENV['SMARTCAR_APP_MANAGEMENT_TOKEN']
    auth = Base64.strict_encode64("default:#{token}")
    uri = URI("https://management.smartcar.com/v2.0/management/connections/?user_id=#{user_id}&vehicle_id=#{vehicle_id}")
    request = Net::HTTP::Delete.new(uri)
    request['Authorization'] = "Basic #{auth}"
    request['Content-Type'] = 'application/json'
    response = Net::HTTP.start(uri.hostname, uri.port, use_ssl: true) do |http|
      http.request(request)
    end
    puts response.body
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={null}
  {
    "connections": [
      {
        "userId": "<string>",
        "vehicleId": "<string>"
      }
    ]
  }
  ```
</ResponseExample>

## Response

<ResponseField name="connections" type="array">
  An array of connections

  <Expandable title="connections">
    <ResponseField name="userId" type="string">
      ID of the user that authorized the deleted connection (UUID v4)
    </ResponseField>

    <ResponseField name="vehicleId" type="string">
      ID of the vehicle disconnected (UUID v4)
    </ResponseField>
  </Expandable>
</ResponseField>


# Vehicle Connections
Source: https://smartcar.com/docs/api-reference/management/get-vehicle-connections

GET https://management.smartcar.com/v2.0/management/connections
Returns a paged list of all vehicles that are connected to the application associated with the management API token used, sorted in descending order by connection date.

## Request

**Header**

<ParamField header="Authorization" type="string" required>
  In the format `Basic base64(default:{application_management_token})`. You can find your `application_management_token` under
  your Application Configuration in the Smartcar Dashboard.
</ParamField>

**Query**

<ParamField query="limit" default="10" type="integer">
  Number of connections to return per page. `Max: 100`
</ParamField>

<ParamField query="cursor" type="string">
  Used for accessing pages other than the first page. Each page returned has a cursor value
  that can be passed here to fetch the “next” page.
</ParamField>

<ParamField query="user_id" type="string">
  Filter for connections created by the provider user ID.
</ParamField>

<ParamField query="vehicle_id" type="string">
  Filter for connections to the provided vehicle ID.
</ParamField>

<ParamField query="mode" type="string">
  Filter for connections by either `live`, `simulated`, or the deprecated `test` mode.
</ParamField>

<RequestExample>
  ```bash cURL theme={null}
  curl -X GET "https://management.smartcar.com/v2.0/management/connections" \
    -H "Authorization: Basic $(echo -n "default:$SMARTCAR_APP_MANAGEMENT_TOKEN" | base64)" \
    -H "Content-Type: application/json"
  ```

  ```python Python theme={null}
  import os
  import base64
  import requests

  token = os.getenv("SMARTCAR_APP_MANAGEMENT_TOKEN")
  auth_header = base64.b64encode(f"default:{token}".encode()).decode()

  headers = {
      "Authorization": f"Basic {auth_header}",
      "Content-Type": "application/json"
  }

  response = requests.get(
      "https://management.smartcar.com/v2.0/management/connections",
      headers=headers
  )
  ```

  ```javascript Node theme={null}
  const basicAuth = Buffer.from(`default:${process.env.SMARTCAR_APP_MANAGEMENT_TOKEN}`).toString('base64');

  const response = await fetch(
      "https://management.smartcar.com/v2.0/management/connections",
      {
          method: 'GET',
          headers: {
              'Authorization': `Basic ${basicAuth}`,
              'Content-Type': 'application/json'
          }
      }
  );
  ```

  ```java Java theme={null}
  import java.net.HttpURLConnection;
  import java.net.URL;
  import java.util.Base64;

  String token = System.getenv("SMARTCAR_APP_MANAGEMENT_TOKEN");
  String auth = Base64.getEncoder().encodeToString(("default:" + token).getBytes());

  URL url = new URL("https://management.smartcar.com/v2.0/management/connections");
  HttpURLConnection conn = (HttpURLConnection) url.openConnection();
  conn.setRequestMethod("GET");
  conn.setRequestProperty("Authorization", "Basic " + auth);
  conn.setRequestProperty("Content-Type", "application/json");

  int responseCode = conn.getResponseCode();
  ```

  ```ruby Ruby theme={null}
  require 'net/http'
  require 'uri'
  require 'base64'

  token = ENV['SMARTCAR_APP_MANAGEMENT_TOKEN']
  auth = Base64.strict_encode64("default:#{token}")

  uri = URI("https://management.smartcar.com/v2.0/management/connections")
  request = Net::HTTP::Get.new(uri)
  request['Authorization'] = "Basic #{auth}"
  request['Content-Type'] = 'application/json'

  response = Net::HTTP.start(uri.hostname, uri.port, use_ssl: true) do |http|
    http.request(request)
  end
  ```
</RequestExample>

## Response

<ResponseField name="connections" type="array">
  An array of connections

  <Expandable title="connections">
    <ResponseField name="userId" type="string">
      ID of the user that authorized this connection (UUID v4).
    </ResponseField>

    <ResponseField name="vehicleId" type="string">
      ID of the vehicle connected (UUID v4).
    </ResponseField>

    <ResponseField name="connectedAt" type="string">
      Time at which the connection was created in UTC.
    </ResponseField>

    <ResponseField name="mode" type="string">
      Vehicle mode: live, simulated, or test (deprecated).
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="paging" type="Object">
  Metadata about the current query

  <Expandable>
    <ResponseField name="cursor" type="string">
      The cursor parameter that should be used to fetch the next page of results.
      This field will be null if there are no more pages.
    </ResponseField>
  </Expandable>
</ResponseField>


# Charge Schedule
Source: https://smartcar.com/docs/api-reference/nissan/get-charge-schedule

GET https://api.smartcar.com/v2.0/vehicles/{id}/{make}/charge/schedule
Returns the charging schedule of a vehicle. The response contains the start time and departure time of the vehicle's charging schedule.

<Note>
  This endpoint is currently available for `nissan` EVs on the `MyNISSAN` platform.
</Note>

## Permission

`read_charge`

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

<RequestExample>
  <Snippet file="api-reference/bse/get-charge-schedule.mdx" />
</RequestExample>

## Response

<ResponseField name="chargeSchedules" type="array">
  An array of charge schedules. Maximum of 3 schedules, empty if no schedules are set.

  <Expandable>
    <ResponseField name="start" type="array">
      HH:mm in UTC for a schedule start time.
    </ResponseField>

    <ResponseField name="end" type="array">
      HH:mm in UTC for a schedule end time.
    </ResponseField>

    <ResponseField name="days" type="array">
      An array of days the schedule applies to.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
    "chargeSchedules": [
      {
        "end": "2020-01-01T02:00:00.000Z",
        "start": "2020-01-01T01:00:00.000Z",
        "days": [
          "MONDAY",
          "WEDNESDAY",
          "FRIDAY"
        ]
      }
    ]
  }
  ```
</ResponseExample>


# Charge Schedule
Source: https://smartcar.com/docs/api-reference/nissan/set-charge-schedule

PUT https://api.smartcar.com/v2.0/vehicles/{id}/{make}/charge/schedule
Sets the charging schedule for a vehicle.

<Note>
  This endpoint is currently available for `nissan` EVs on the `MyNISSAN` platform
</Note>

## Permission

`control_charge`

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

**Body**

<ParamField body="chargeSchedules" type="array" required>
  An array of charge schedules. A maximum of 3 schedules can be set.

  <Expandable defaultOpen="true">
    <ParamField body="start" type="string" required>
      HH:mm in UTC for a schedule start time.
    </ParamField>

    <ParamField body="end" type="string" required>
      HH:mm in UTC for a schedule start time.
    </ParamField>

    <ParamField body="days" type="[days]" required>
      An array of days for the schedule to be applied.
      Options: `MONDAY` `TUESDAY` `WEDNESDAY` `THURSDAY` `FRIDAY` `SATURDAY` `SUNDAY`
    </ParamField>
  </Expandable>
</ParamField>

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/charge/schedule" \
  -H "Authorization: Bearer {token}" \
  -X "PUT" \
  -H "Content-Type: application/json" \
  -d '{
      "chargeSchedules": [
          {
              "start": "08:00",
              "end": "12:00",
              "days": ["MONDAY", "WEDNESDAY", "FRIDAY"]
          },
          {
              "start": "14:00",
              "end": "18:00",
              "days": ["TUESDAY", "THURSDAY", "SATURDAY"]
          }
      ]
  }'
  ```

  ```python Python theme={null}
  charge_schedule = vehicle.request("PUT", "{make}/charge/schedule", {
      "chargeSchedules": [
          {
              "start": "08:00",
              "end": "12:00",
              "days": ["MONDAY", "WEDNESDAY", "FRIDAY"]
          },
          {
              "start": "14:00",
              "end": "18:00",
              "days": ["TUESDAY", "THURSDAY", "SATURDAY"]
          }
      ]
  })
  ```

  ```js Node theme={null}
  const chargeSchedule = vehicle.request("PUT", "{make}/charge/schedule", {
      "chargeSchedules": [
          {
              "start": "08:00",
              "end": "12:00",
              "days": ["MONDAY", "WEDNESDAY", "FRIDAY"]
          },
          {
              "start": "14:00",
              "end": "18:00",
              "days": ["TUESDAY", "THURSDAY", "SATURDAY"]
          }
      ]
  });
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
      .method("PUT")
      .path("{make}/charge/schedule")
      .addBodyParameter("chargeSchedules", [
          {
              "start": "08:00",
              "end": "12:00",
              "days": ["MONDAY", "WEDNESDAY", "FRIDAY"]
          },
          {
              "start": "14:00",
              "end": "18:00",
              "days": ["TUESDAY", "THURSDAY", "SATURDAY"]
          }
      ])
      .build();
  ChargeSchedule chargeSchedule = vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  charge_schedule = vehicle.request("PUT", "{make}/charge/schedule", {
      "chargeSchedules": [
          {
              "start": "08:00",
              "end": "12:00",
              "days": ["MONDAY", "WEDNESDAY", "FRIDAY"]
          },
          {
              "start": "14:00",
              "end": "18:00",
              "days": ["TUESDAY", "THURSDAY", "SATURDAY"]
          }
      ]
  })
  ```
</RequestExample>

## Response

<ResponseField name="message" type="string">
  If the request is successful, Smartcar will return a message.
</ResponseField>

<ResponseField name="status" type="string">
  If the request is successful, Smartcar will return `success`.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
    "message": "Successfully sent request to vehicle",
    "status": "success"
  }
  ```
</ResponseExample>


# Permissions
Source: https://smartcar.com/docs/api-reference/permissions

In order to use an endpoint or webhook, you'll need to request the associated permissions from your user in [Connect](/docs/connect/what-is-connect).

When requesting permissions, it's crucial to only ask for the data that is absolutely necessary for your application's functionality. Avoid collecting additional permissions "just in case" you might need them later. This practice not only protects vehicle owners' privacy but also increases the likelihood of users granting consent during the Connect flow. Users are more likely to trust and authorize applications that clearly demonstrate respect for their privacy by requesting minimal, purposeful access to their vehicle data.

## Vehicle Access

Smartcar's **Vehicle Access** configuration page (Dashboard → Configuration → Vehicle Access) lets you select the *vehicle data* (signals) and *commands* without needing to know which individual permission is needed for a given signal. Based on the signals you choose, Smartcar automatically determines the minimum set of OAuth permissions required and surfaces them during the Connect flow.

<Info>
  **Signals vs Permissions**: Permissions (e.g. `read_location`, `control_security`) are OAuth scopes requested from the user. Signals are the granular data points (e.g. state of charge, tire pressure) defined in the <a href="/api-reference/signals/schema">Signal Schema</a>. Vehicle Access starts from signals and derives the needed permissions for you.
</Info>

### Why use Vehicle Access?

* Enforces least-privilege automatically
* Reduces guesswork mapping data needs to permissions
* Prevents over-requesting and improves user trust
* Keeps configuration centralized in the Dashboard

### How it works

1. You open the Vehicle Access page in the Dashboard.
2. You search or browse for the signals you need (see the <a href="/api-reference/signals/schema">Signal Schema</a> for structure and definitions).
3. Smartcar instantly computes the required permissions for those signals.
4. You save the configuration; the derived permissions are locked in for subsequent Connect authorizations.
5. During Connect, Smartcar presents only those permissions—no need to manually maintain a scope list.

<Note>
  Updating Vehicle Access changes the permissions requested in **future** Connect authorizations. Existing refresh/access tokens retain previously granted scopes until the user re-authenticates.
</Note>

<Note>
  Passing the `scope` parameter in the Connect URL overrides the permissions derived from Vehicle Access for that authorization. This allows you to request different permissions for specific Connect flows without changing your overall Vehicle Access configuration.
</Note>

### Example

Selecting signals for battery state of charge, charging status, and odometer will automatically derive permissions such as `read_battery`, `read_charge`, and \`read\_odometer. You don't need to add those manually.

## Read Permissions

Permissions prefixed with `read_` allow your application to get data from a vehicle as part of `GET` requests.

|                              |                                                                                                                        |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `read_alerts`                | Read alerts from the vehicle                                                                                           |
| `read_battery`               | Read an EV's high voltage battery data                                                                                 |
| `read_charge`                | Read charging data                                                                                                     |
| `read_charge_locations`      | Access previous charging locations and their associated charging configurations                                        |
| `read_charge_records`        | Read charge records and associated billing information                                                                 |
| `read_charge_events`         | Receive notifications for events associated with charging                                                              |
| `read_climate`               | Read the status and settings of the vehicle's climate control system                                                   |
| `read_compass`               | Read the compass direction the vehicle is facing                                                                       |
| `read_diagnostics`           | Read a vehicle's system status and/or Diagnostic Trouble Codes                                                         |
| `read_engine_oil`            | Read vehicle engine oil health                                                                                         |
| `read_extended_vehicle_info` | Read vehicle configuration information from a vehicle                                                                  |
| `read_fuel`                  | Read fuel tank level                                                                                                   |
| `read_location`              | Access the vehicle's location                                                                                          |
| `read_odometer`              | Retrieve total distance traveled                                                                                       |
| `read_security`              | Read the lock status of doors, windows, charging port, etc.                                                            |
| `read_service_history`       | Read a vehicle's dealer service history                                                                                |
| `read_speedometer`           | Read a vehicle's speed                                                                                                 |
| `read_thermometer`           | Read temperatures from inside and outside the vehicle                                                                  |
| `read_tires`                 | Read a vehicle's tire status                                                                                           |
| `read_user_profile`          | Read the information associated with a user's connected services account profile such as their email and phone number. |
| `read_vehicle_info`          | Know make, model, and year                                                                                             |
| `read_vin`                   | Read VIN                                                                                                               |

## Control Permissions

Permissions prefixed with `control_` allow your application to issue commands or apply settings to a vehicle as part of `POST` or `PUT` requests.

|                      |                                                                     |
| -------------------- | ------------------------------------------------------------------- |
| `control_charge`     | Control a vehicle's charge state                                    |
| `control_climate`    | Set the status and settings of the vehicle's climate control system |
| `control_navigation` | Send commands to the vehicle's navigation system                    |
| `control_security`   | Lock or unlock the vehicle                                          |
| `control_pin`        | Modify a PIN and enable the PIN to Drive feature for the vehicle.   |
| `control_trunk`      | Open a vehicle's trunk or frunk                                     |


# Send Destination
Source: https://smartcar.com/docs/api-reference/send-destination-to-vehicle

POST https://api.smartcar.com/v2.0/vehicles/{id}/navigation/destination
Send destination coordinates to the vehicle's navigation system.

<Note>
  2.0 is still the only supported version for sending remote commands. If you need to send commands, please continue using v2.0 until commands are supported in the latest version later this year.
</Note>

## Permission

`control_navigation`

## Request

**Path**

<Snippet file="api-reference/path-vehicle-id.mdx" />

**Body**

<ParamField body="latitude" type="number" initialValue="51.5007" required>
  The latitude of the location you wish to set the vehicle's navigation to.
</ParamField>

<ParamField body="longitude" type="number" initialValue="0.1246" required>
  The longitude of the location you wish to set the vehicle's navigation to.
</ParamField>

<RequestExample>
  <Snippet file="api-reference/core-sdk-methods/send-destination-to-vehicle.mdx" />
</RequestExample>

## Response

<ResponseField name="status" type="string">
  If the request is successful, Smartcar will return “success” (HTTP 200 status).
</ResponseField>

<ResponseField name="message" type="string">
  If the request is successful, Smartcar will return a message (HTTP 200 status).
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
      "message": "Successfully sent request to vehicle",
      "status": "success"
  }   
  ```
</ResponseExample>


# Charge Signals
Source: https://smartcar.com/docs/api-reference/signals/charge



### Amperage

Signal code: `charge-amperage`

Current amperage flowing to the electric vehicle during a charging session, measured in amps.

<ParamField path="unit" type="string" required={false} />

<ParamField path="value" type="number" required={false} />

```json Example theme={null}
{
  "unit": "amps",
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
  "unit": "amps",
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
  "unit": "amps",
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
  "unit": "miles_per_hour",
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

<ParamField path="unit" type="string" required={false} />

<ParamField path="value" type="integer" required={false} />

```json Example theme={null}
{
  "unit": "count",
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
  "unit": "kilowatt_hours",
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


# Climate Signals
Source: https://smartcar.com/docs/api-reference/signals/climate



### External Temperature

Signal code: `climate-externaltemperature`

The current temperature measured outside the vehicle.

<ParamField path="unit" type="string" required={false}>
  The unit of temperature measurement (celsius or fahrenheit)
</ParamField>

<ParamField path="value" type="number" required={false}>
  The temperature value
</ParamField>

```json Example theme={null}
{
  "unit": "celsius",
  "value": 22.5
}
```

### Internal Temperature

Signal code: `climate-internaltemperature`

The current temperature measured inside the vehicle's cabin.

<ParamField path="unit" type="string" required={false}>
  The unit of temperature measurement (celsius or fahrenheit)
</ParamField>

<ParamField path="value" type="number" required={false}>
  The temperature value
</ParamField>

```json Example theme={null}
{
  "unit": "celsius",
  "value": 21.5
}
```


# Closure Signals
Source: https://smartcar.com/docs/api-reference/signals/closure



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


# ConnectivitySoftware Signals
Source: https://smartcar.com/docs/api-reference/signals/connectivitysoftware



### Current Firmware Version

Signal code: `connectivitysoftware-currentfirmwareversion`

Current version number of the firmware installed on the vehicle's telematics control unit or connected hardware.

<ParamField path="value" type="string" required={false} />

```json Example theme={null}
{
  "value": "2024.4.5"
}
```


# ConnectivityStatus Signals
Source: https://smartcar.com/docs/api-reference/signals/connectivitystatus



### Is Asleep

Signal code: `connectivitystatus-isasleep`

Boolean indicator that shows whether the vehicle is in a low-power or sleep state.

<ParamField path="value" type="boolean" required={false} />

```json Example theme={null}
{
  "value": false
}
```

### Is Digital Key Paired

Signal code: `connectivitystatus-isdigitalkeypaired`

Boolean indicator that shows whether a digital key has been successfully paired with the vehicle.

<ParamField path="value" type="boolean" required={false} />

```json Example theme={null}
{
  "value": true
}
```

### Is Online

Signal code: `connectivitystatus-isonline`

Boolean indicator that shows the connectivity status of the vehicle.

<ParamField path="value" type="boolean" required={false} />

```json Example theme={null}
{
  "value": true
}
```


# Diagnostics Signals
Source: https://smartcar.com/docs/api-reference/signals/diagnostics



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


# HVAC Signals
Source: https://smartcar.com/docs/api-reference/signals/hvac



### Cabin Target Temperature

Signal code: `hvac-cabintargettemperature`

The target temperature set for the vehicle's cabin.

<ParamField path="unit" type="string" required={false}>
  The temperature unit (e.g., celsius, fahrenheit)
</ParamField>

<ParamField path="value" type="number" required={false}>
  The target temperature value
</ParamField>

```json Example theme={null}
{
  "unit": "celsius",
  "value": 22
}
```

### Is Cabin HVACActive

Signal code: `hvac-iscabinhvacactive`

A boolean value indicating if the cabin HVAC system is active.

<ParamField path="value" type="boolean" required={false} />

```json Example theme={null}
{
  "value": true
}
```

### Is Front Defroster Active

Signal code: `hvac-isfrontdefrosteractive`

A boolean value indicating if the front windshield defroster is active.

<ParamField path="value" type="boolean" required={false} />

```json Example theme={null}
{
  "value": false
}
```

### Is Rear Defroster Active

Signal code: `hvac-isreardefrosteractive`

A boolean value indicating if the rear windshield defroster is active.

<ParamField path="value" type="boolean" required={false} />

```json Example theme={null}
{
  "value": false
}
```

### Is Steering Heater Active

Signal code: `hvac-issteeringheateractive`

A boolean value indicating if the steering wheel heater is active.

<ParamField path="value" type="boolean" required={false} />

```json Example theme={null}
{
  "value": true
}
```


# InternalCombustionEngine Signals
Source: https://smartcar.com/docs/api-reference/signals/internalcombustionengine



### Amount Remaining

Signal code: `internalcombustionengine-amountremaining`

The quantity of fuel remaining in the vehicle's tank

<ParamField path="unit" type="string" required={false}>
  The unit of measurement for the fuel amount (e.g., liters, gallons)
</ParamField>

<ParamField path="value" type="number" required={false}>
  The quantity value of remaining fuel
</ParamField>

```json Example theme={null}
{
  "unit": "liters",
  "value": 45.5
}
```

### Fuel Level

Signal code: `internalcombustionengine-fuellevel`

The current amount of fuel in the vehicle's tank, expressed as a percentage (0 - 100)

<ParamField path="unit" type="string" required={false}>
  The unit for fuel level (always percent)
</ParamField>

<ParamField path="value" type="number" required={false}>
  The fuel level as a percentage between 0 and 100
</ParamField>

```json Example theme={null}
{
  "unit": "percent",
  "value": 75
}
```

### Oil Life

Signal code: `internalcombustionengine-oillife`

The engine oil’s remaining life span based on the current quality of the oil, expressed as a percentage. 100 indicates the oil was changed recently and 0 indicates the oil should be changed immediately. It is not a representation of how much oil is left in the vehicle.

<ParamField path="unit" type="string" required={false}>
  The unit for oil life (always percent)
</ParamField>

<ParamField path="value" type="number" required={false}>
  The oil life remaining as a percentage between 0 and 100
</ParamField>

```json Example theme={null}
{
  "unit": "percent",
  "value": 85
}
```

### Range

Signal code: `internalcombustionengine-range`

The estimated driving distance possible with the current amount of fuel

<ParamField path="unit" type="string" required={false}>
  The unit for range measurement (e.g., kilometers, miles)
</ParamField>

<ParamField path="value" type="number" required={false}>
  The estimated driving distance value
</ParamField>

```json Example theme={null}
{
  "unit": "kilometers",
  "value": 450
}
```


# Location Signals
Source: https://smartcar.com/docs/api-reference/signals/location



### IsAtHome

Signal code: `location-isathome`

A boolean indicating if the vehicle is at home. Vehicle owners can set their home location in their OEM application.

<ParamField path="value" type="boolean" required={false}>
  Boolean indicating if the vehicle is at the configured home location
</ParamField>

```json Example theme={null}
{
  "value": true
}
```

### Location

Signal code: `location-preciselocation`

An object containing information about a vehicle's precise location.

<ParamField path="heading" type="number" required={false}>
  The precise angular heading of the vehicle.
</ParamField>

<ParamField path="latitude" type="number" required={false}>
  The vehicle's current geographic latitude coordinate.
</ParamField>

<ParamField path="direction" type="string" required={false}>
  A cardinal or intercardinal direction representing the vehicle's current heading or orientation.

  **Possible values:** `N`, `NE`, `E`, `SE`, `S`, `SW`, `W`, `NW`
</ParamField>

<ParamField path="longitude" type="number" required={false}>
  The vehicle's current geographic longitude coordinate.
</ParamField>

<ParamField path="locationType" type="string" required={false}>
  Indicates whether the location-related fields are expected to update in real time or when the vehicle is parked.

  **Possible values:** `LAST_PARKED`, `CURRENT`
</ParamField>

```json Example theme={null}
{
  "heading": 45.5,
  "latitude": 37.7749,
  "longitude": -122.4194,
  "direction": "NE",
  "locationType": "CURRENT"
}
```


# LowVoltageBattery Signals
Source: https://smartcar.com/docs/api-reference/signals/lowvoltagebattery



### State Of Charge

Signal code: `lowvoltagebattery-stateofcharge`

Indicates the current charge level of the low voltage battery as a percentage (0 - 100)

<ParamField path="unit" type="string" required={false}>
  The unit for state of charge (always percent)
</ParamField>

<ParamField path="value" type="number" required={false}>
  The battery charge level as a percentage between 0 and 100
</ParamField>

```json Example theme={null}
{
  "unit": "percent",
  "value": 95
}
```

### Status

Signal code: `lowvoltagebattery-status`

Represents the current operational status of the low voltage battery. (GOOD, WARN, BAD)

<ParamField path="value" type="string" required={false}>
  The operational status of the battery

  **Possible values:** `GOOD`, `WARN`, `BAD`
</ParamField>

```json Example theme={null}
{
  "value": "GOOD"
}
```


# Motion Signals
Source: https://smartcar.com/docs/api-reference/signals/motion



### Current Speed

Signal code: `motion-currentspeed`

The vehicle's current driving speed, or 0 if it is not currently driving.

<ParamField path="unit" type="string" required={false}>
  The unit of speed measurement (e.g., kph, mph)
</ParamField>

<ParamField path="value" type="number" required={false}>
  The current speed value
</ParamField>

```json Example theme={null}
{
  "unit": "kph",
  "value": 65
}
```


# Odometer Signals
Source: https://smartcar.com/docs/api-reference/signals/odometer



### Traveled Distance

Signal code: `odometer-traveleddistance`

The total distance the vehicle has traveled since its initial use

<ParamField path="unit" type="string" required={false}>
  The unit for distance measurement (e.g., kilometers, miles)
</ParamField>

<ParamField path="value" type="number" required={false}>
  The total distance traveled
</ParamField>

```json Example theme={null}
{
  "unit": "kilometers",
  "value": 50000
}
```


# Smartcar Signals & Attributes Overview
Source: https://smartcar.com/docs/api-reference/signals/schema

Smartcar's standard list of vehicle signals and attributes across all compatible OEMs.

Below are the list of signals and attributes supported by Smartcar.

## Attributes

Attributes are static vehicle data that typically does not change in value.

* [Surveillance](/api-reference/signals/surveillance)
* [VehicleIdentification](/api-reference/signals/vehicleidentification)
* [Wheel](/api-reference/signals/wheel)

## Signals

With Smartcar you can configure your application to receive a webhook when the value of any of these signals change. Some change more frequently than others.

Below you will find the signal groups and their respective signals. Each signal has a code that you can use to [request the latest value](/api-reference/get-the-values-for-an-individual-signal) for that signal.

* [Charge](/api-reference/signals/charge)
* [Climate](/api-reference/signals/climate)
* [Closure](/api-reference/signals/closure)
* [ConnectivitySoftware](/api-reference/signals/connectivitysoftware)
* [ConnectivityStatus](/api-reference/signals/connectivitystatus)
* [Diagnostics](/api-reference/signals/diagnostics)
* [HVAC](/api-reference/signals/hvac)
* [InternalCombustionEngine](/api-reference/signals/internalcombustionengine)
* [Location](/api-reference/signals/location)
* [LowVoltageBattery](/api-reference/signals/lowvoltagebattery)
* [Motion](/api-reference/signals/motion)
* [Odometer](/api-reference/signals/odometer)
* [Service](/api-reference/signals/service)
* [Surveillance](/api-reference/signals/surveillance)
* [TractionBattery](/api-reference/signals/tractionbattery)
* [Transmission](/api-reference/signals/transmission)
* [VehicleIdentification](/api-reference/signals/vehicleidentification)
* [VehicleUserAccount](/api-reference/signals/vehicleuseraccount)
* [Wheel](/api-reference/signals/wheel)


# Service Signals
Source: https://smartcar.com/docs/api-reference/signals/service



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


# Surveillance Signals & Attributes
Source: https://smartcar.com/docs/api-reference/signals/surveillance



## Signals

### Is Enabled

Signal code: `surveillance-isenabled`

Indicates if the surveillance system is enabled

<ParamField path="value" type="boolean" required={false}>
  Boolean indicating if surveillance is active
</ParamField>

```json Example theme={null}
{
  "value": true
}
```

## Attributes

### Brand

Signal code: `surveillance-brand`

Indicates the brand of surveillance available on the vehicle e.g. for Tesla this would be Sentry Mode

<ParamField path="value" type="string" required={false}>
  The brand name or type of surveillance system
</ParamField>

```json Example theme={null}
{
  "value": "Sentry Mode"
}
```


# TractionBattery Signals
Source: https://smartcar.com/docs/api-reference/signals/tractionbattery



### Is Heater Active

Signal code: `tractionbattery-isheateractive`

A boolean flag indicating whether the high voltage battery's heating system is currently operating.

<ParamField path="value" type="boolean" required={false} />

### Max Range Charge Counter

Signal code: `tractionbattery-maxrangechargecounter`

A counter tracking the number of times the vehicle has been charged to its maximum range capacity.

<ParamField path="unit" type="string" required={false} />

<ParamField path="value" type="integer" required={false} />

### Nominal Capacities

Signal code: `tractionbattery-nominalcapacity`

An object containing the gross battery capacity and a list of multiple available gross capacity configurations for the high voltage battery.

<ParamField path="source" type="string" required={false}>
  Identifies the origin or method used to determine the battery's gross capacity.

  **Possible values:** `SMARTCAR`, `USER_SELECTED`
</ParamField>

<ParamField path="capacity" type="number" required={false}>
  The total gross energy storage capacity of the high voltage battery, typically measured in kilowatt-hours (kWh). This value represents the nominal rated battery capacity for a vehicle.
</ParamField>

<ParamField path="availableCapacities" type="array" required={false}>
  An array of available battery capacity configurations for the vehicle.
</ParamField>

<Expandable title="Array item properties">
  <ParamField path="capacity" type="number" required={false}>
    The battery capacity value in kilowatt-hours (kWh).
  </ParamField>

  <ParamField path="description" type="string" required={false}>
    A description of the uniqueness for the nominal capacity and engine type of the vehicle in the form {ENGINE_TYPE}:{TRIM}, for example "BEV:Extended Range".
  </ParamField>
</Expandable>

<ParamField path="unit" type="string" required={false}>
  The unit of measurement for the battery capacity.
</ParamField>

```json Example theme={null}
{
  "source": "SMARTCAR",
  "capacity": 73.5,
  "availableCapacities": [
    {
      "capacity": 73.5,
      "description": "BEV:Extended Range"
    },
    {
      "capacity": 80.9,
      "description": null
    }
  ],
  "unit": "kWhr"
}
```

### Range

Signal code: `tractionbattery-range`

Returns the most accurate real world estimate that is available. Estimated > Ideal > Rated.

<ParamField path="unit" type="string" required={false}>
  **Possible values:** `DEFAULT`
</ParamField>

<ParamField path="value" type="number" required={true} />

<ParamField path="additionalValues" type="array" required={true} />

<Expandable title="Array item properties">
  <ParamField path="type" type="string" required={true}>
    **Possible values:** `IDEAL_CONDITIONS`, `ESTIMATED`, `RATED`
  </ParamField>

  <ParamField path="value" type="number" required={true} />
</Expandable>

```json Example theme={null}
{
  "unit": "kilometers",
  "value": 350
}
```

### State Of Charge

Signal code: `tractionbattery-stateofcharge`

The current charge level of the high voltage battery, expressed as a percentage (0 - 100).

<ParamField path="unit" type="string" required={false} />

<ParamField path="value" type="number" required={false} />

```json Example theme={null}
{
  "unit": "percent",
  "value": 75
}
```


# Transmission Signals
Source: https://smartcar.com/docs/api-reference/signals/transmission



### Gear State

Signal code: `transmission-gearstate`

The current gear selection of the vehicle's transmission.

<ParamField path="value" type="string" required={true}>
  The current gear selection of the vehicle's transmission.

  **Possible values:** `PARK`, `DRIVE`, `REVERSE`, `NEUTRAL`
</ParamField>

### Drive Mode

Signal code: `transmission-drivemode`

Represents the current drive mode selected in the vehicle's transmission system

<ParamField path="canonical" type="string" required={true}>
  The standardized drive mode value
</ParamField>

<ParamField path="oemDisplayName" type="string" required={true}>
  The display name for the drive mode as shown by the OEM
</ParamField>

```json Example theme={null}
{
  "canonical": "NORMAL",
  "oemDisplayName": "everyday"
}
```


# VehicleIdentification Signals & Attributes
Source: https://smartcar.com/docs/api-reference/signals/vehicleidentification



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


# VehicleUserAccount Signals
Source: https://smartcar.com/docs/api-reference/signals/vehicleuseraccount



### Permissions

Signal code: `vehicleuseraccount-permissions`

Permissions granted by the connecting account with the OEM. These may be different than your application's Smartcar permissions as they can be managed directly with the OEM.

<ParamField path="values" type="array" required={true}>
  An array containing permissions granted by the connecting account with the OEM.
</ParamField>

```json Example theme={null}
{
  "values": [
    "vehicle_cmds",
    "vehicle_device_data"
  ]
}
```

### Role

Signal code: `vehicleuseraccount-role`

Indicates the access level to the vehicle for the connecting account as defined by the OEM. While the OEM representation may vary, these can be thought of as "secondary" and "primary" accounts where "secondary" accounts may have more limited access than an "primary" account. "secondary" accounts are granted access to vehicle by "primary" accounts.

<ParamField path="value" type="string" required={false} />

```json Example theme={null}
{
  "value": "Driver"
}
```


# Wheel Signals & Attributes
Source: https://smartcar.com/docs/api-reference/signals/wheel



## Signals

### Tires

Signal code: `wheel-tires`

An array of objects, where each object represents a specific wheel on the vehicle.

<ParamField path="values" type="array" required={true}>
  An array of objects containing information about the vehicle's wheels.
</ParamField>

<Expandable title="Array item properties">
  <ParamField path="row" type="number" required={true}>
    Represents the row position of a specific wheel, front to back (0 to Wheels.rowCount-1).
  </ParamField>

  <ParamField path="column" type="number" required={true}>
    Represents the column position of a specific wheel, left to right (0 to Wheels.columnCount-1).
  </ParamField>

  <ParamField path="tirePressure" type="number" required={true}>
    Indicates the current tire pressure of the wheel.
  </ParamField>
</Expandable>

<ParamField path="rowCount" type="number" required={false}>
  Indicates the total number of wheel rows present in the vehicle. This signal, along with WheelColumnCount, provides information about the vehicle's wheel layout and the total number of wheels available.
</ParamField>

<ParamField path="columnCount" type="number" required={false}>
  Indicates the total number of wheel columns present in the vehicle. This signal, along with WheelRowCount, provides information about the vehicle's wheel layout and the total number of wheels available.
</ParamField>

## Attributes

### Style

Signal code: `wheel-style`

Wheel style of the vehicle.

<ParamField path="value" type="string" required={false} />


# Clear PIN to Drive
Source: https://smartcar.com/docs/api-reference/tesla/clear-pin-to-drive

DELETE https://api.smartcar.com/v2.0/vehicles/{id}/{make}/pin
Disables this feature on the vehicle and resets the PIN.

<Snippet file="api-reference/note-bse-tesla.mdx" />

## Permission

`control_pin`

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/pin" \
  -H "Authorization: Bearer {token}" \
  -X "DELETE" \
  -H "Content-Type: application/json" \
  ```

  ```python Python theme={null}
  pin = vehicle.request(
    "DELETE", 
    "{make}/pin"
  )
  ```

  ```js Node theme={null}
  const pin = vehicle.request(
    "DELETE", 
    "{make}/pin"
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("DELETE")
        .path("{make}/pin")
        .build();
  VehicleResponse pin =  vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  pin =  vehicle.request(
    "DELETE", 
    "{make}/pin"
  )
  ```
</RequestExample>

## Response

<ResponseField name="status" type="string">
  If the request is successful, Smartcar will return “success”.
</ResponseField>

<ResponseField name="message" type="string">
  If the request is successful, Smartcar will return a message.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
      {
          "message": "Successfully sent request to vehicle",
          "status": "success"
      }   
  ```
</ResponseExample>

## Notes

* Call `POST` [PIN to Drive](/api-reference/tesla/set-pin-to-drive) in order to enable this feature and set the PIN
* Currently both owner and driver account types can clear a PIN for the vehicle and disable the feature via the API.


# Charge Port
Source: https://smartcar.com/docs/api-reference/tesla/control-charge-port

POST https://api.smartcar.com/v2.0/vehicles/{id}/{make}/charge/charge_port_door
Open or close the vehicle's charge port door.

<Snippet file="api-reference/note-bse-tesla.mdx" />

## Permission

`control_charge`

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

**Body**

<ParamField body="action" type="string" required>
  Indicate whether to open or close the charge port door.
  Options: `OPEN` or `CLOSE`
</ParamField>

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/charge/charge_port_door" \
  -H "Authorization: Bearer {token}" \
  -X "POST" \
  -H "Content-Type: application/json" \
  -d '{"action" : "OPEN"}'
  ```

  ```python Python theme={null}
  charge_port = vehicle.request(
    "POST", 
    "{make}/charge/charge_port_door", 
    {"action" : "OPEN"}
  )
  ```

  ```js Node theme={null}
  const chargePort = vehicle.request(
    "POST", 
    "{make}/charge/charge_port_door", 
    {"action" : "OPEN"}
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("POST")
        .path("{make}/charge/charge_port_door")
        .addBodyParameter("action" : "OPEN")
        .build();
  VehicleResponse chargePort =  vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  charge_port =  vehicle.request(
    "POST", 
    "{make}/charge/charge_port_door", 
    {"action" : "OPEN"}
  )
  ```
</RequestExample>

## Response

<ResponseField name="status" type="string">
  If the request is successful, Smartcar will return “success”.
</ResponseField>

<ResponseField name="message" type="string">
  If the request is successful, Smartcar will return a message.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
      {
          "message": "Successfully sent request to vehicle",
          "status": "success"
      }   
  ```
</ResponseExample>


# Frunk
Source: https://smartcar.com/docs/api-reference/tesla/control-frunk

POST https://api.smartcar.com/v2.0/vehicles/{id}/{make}/security/frunk
Open or close the frunk (front trunk) of the Tesla vehicle.

<Snippet file="api-reference/note-bse-tesla.mdx" />

## Permission

`control_trunk`

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

**Body**

<ParamField body="action" type="string" required>
  Indicate whether to open or close the charge port door.
  Options: `OPEN` or `CLOSE`
</ParamField>

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/security/frunk" \
  -H "Authorization: Bearer {token}" \
  -X "POST" \
  -H "Content-Type: application/json" \
  -d '{"action" : "OPEN"}'
  ```

  ```python Python theme={null}
  frunk = vehicle.request(
    "POST", 
    "{make}/security/frunk", 
    {"action" : "OPEN"}
  )
  ```

  ```js Node theme={null}
  const frunk = vehicle.request(
    "POST", 
    "{make}/security/frunk", 
    {"action" : "OPEN"}
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("POST")
        .path("{make}/security/frunk")
        .addBodyParameter("action" : "OPEN")
        .build();
  VehicleResponse frunk =  vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  frunk =  vehicle.request(
    "POST", 
    "{make}/security/frunk", 
    {"action" : "OPEN"}
  )
  ```
</RequestExample>

## Response

<ResponseField name="status" type="string">
  If the request is successful, Smartcar will return “success”.
</ResponseField>

<ResponseField name="message" type="string">
  If the request is successful, Smartcar will return a message.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
      {
          "message": "Successfully sent request to vehicle",
          "status": "success"
      }   
  ```
</ResponseExample>


# Trunk
Source: https://smartcar.com/docs/api-reference/tesla/control-trunk

POST https://api.smartcar.com/v2.0/vehicles/{id}/{make}/security/trunk
Open or close the trunk of the Tesla vehicle.

<Snippet file="api-reference/note-bse-tesla.mdx" />

## Permission

`control_trunk`

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

**Body**

<ParamField body="action" type="string" required>
  Indicate whether to open or close the charge port door.
  Options: `OPEN` or `CLOSE`
</ParamField>

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/security/trunk" \
  -H "Authorization: Bearer {token}" \
  -X "POST" \
  -H "Content-Type: application/json" \
  -d '{"action" : "OPEN"}'
  ```

  ```python Python theme={null}
  trunk = vehicle.request(
    "POST", 
    "{make}/security/trunk", 
    {"action" : "OPEN"}
  )
  ```

  ```js Node theme={null}
  const trunk = vehicle.request(
    "POST", 
    "{make}/security/trunk", 
    {"action" : "OPEN"}
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("POST")
        .path("{make}/security/trunk")
        .addBodyParameter("action" : "OPEN")
        .build();
  VehicleResponse trunk =  vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  trunk =  vehicle.request(
    "POST", 
    "{make}/security/trunk", 
    {"action" : "OPEN"}
  )
  ```
</RequestExample>

## Response

<ResponseField name="status" type="string">
  If the request is successful, Smartcar will return “success”.
</ResponseField>

<ResponseField name="message" type="string">
  If the request is successful, Smartcar will return a message.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
      {
          "message": "Successfully sent request to vehicle",
          "status": "success"
      }   
  ```
</ResponseExample>


# Alerts
Source: https://smartcar.com/docs/api-reference/tesla/get-alerts

GET https://api.smartcar.com/v2.0/vehicles/{id}/{make}/alerts
Returns recent alerts from the vehicle.

<Snippet file="api-reference/note-bse-tesla.mdx" />

## Permission

`read_alerts`

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/alerts" \
  -H "Authorization: Bearer {token}" \
  -X "GET"
  ```

  ```python Python theme={null}
  alerts = vehicle.request(
        "GET", 
        "{make}/alerts"
  )
  ```

  ```js Node theme={null}
  const alerts = await vehicle.request(
        "GET", 
        "{make}/alerts"
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("GET")
        .path("{make}/alerts")
        .build();
  VehicleResponse alerts =vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  alerts = vehicle.request(
        "GET", 
        "{make}/alerts"
  )
  ```
</RequestExample>

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

## Response

<ResponseField name="alerts" type="[alert] | null">
  <Expandable title="alert">
    <ResponseField name="name" type="string | null">
      The name of the alert.
    </ResponseField>

    <ResponseField name="dateTime" type="timestamp | null">
      Date and time of the alert.
    </ResponseField>

    <ResponseField name="audience" type="[string] | null">
      Indicates recipients of the alert.
    </ResponseField>

    <ResponseField name="userText" type="[string] | null">
      Additional context related to the alert.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
      "alerts" : [
            {
                  "name": "Name_Of_The_Alert",
                  "dateTime": "2022-07-10T16:20:00.000Z",
                  "audience": [
                        "service-fix",
                        "customer"
                  ],
                  "userText": "additional description text"
            }
      ]
  }
  ```
</ResponseExample>


# Tesla: Battery Status
Source: https://smartcar.com/docs/api-reference/tesla/get-battery

GET https://api.smartcar.com/v2.0/vehicles/{id}/{make}/battery
Returns all battery related data for a Tesla vehicle.

<Snippet file="api-reference/note-bse-tesla.mdx" />

<Warning>
  The following fields are not supported for streaming vehicles:

  * TeslaBatteryPercentRemainingUsable
  * TeslaBatteryMaxRangeChargeCounter
</Warning>

## Permission

`read_battery`

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/battery" \
  -H "Authorization: Bearer {token}" \
  -X "GET"
  ```

  ```python Python theme={null}
  battery =  vehicle.request(
        "GET", 
        "{make}/battery"
  )
  ```

  ```js Node theme={null}
  const battery =  await vehicle.request(
        "GET", 
        "{make}/battery"
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("GET")
        .path("{make}/battery")
        .build();
  VehicleResponse battery = vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  battery =  vehicle.request(
        "GET", 
        "{make}/battery"
  )
  ```
</RequestExample>

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

## Response

<ResponseField name="percentRemaining" type="number | null">
  The EV’s state of charge as a percentage.
</ResponseField>

<ResponseField name="range" type="number | null">
  The distance the vehicle can travel powered by it’s high voltage battery.
</ResponseField>

<ResponseField name="heaterOn" type="bool | null">
  Indicates if the battery heater is on.
</ResponseField>

<ResponseField name="rangeEstimated" type="number | null">
  The estimated remaining distance the vehicle can travel powered by it’s high voltage battery as determined by Tesla.
</ResponseField>

<ResponseField name="rangeIdeal" type="number | null">
  The ideal remaining distance the vehicle can travel powered by it’s high voltage battery as determined by Tesla.
</ResponseField>

<ResponseField name="percentRemainingUsable" type="number | null">
  The EV’s useable state of charge as a percentage as reported by Tesla.
</ResponseField>

<ResponseField name="maxRangeChargeCounter" type="number | null">
  The number of times the vehicle has been charged to 100% as reported by Tesla.
</ResponseField>

<ResponseField name="notEnoughPowerToHeat" type="bool | null">
  Indicates if there is enough power to heat the battery.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
      "heaterOn": null,
      "maxRangeChargeCounter" : null,
      "notEnoughPowerToHeat" : true, 
      "percentRemaining": 0.3,
      "percentRemainingUsable" : 0.29,
      "range": 40.5,
      "rangeEstimated": 39.01,
      "rangeIdeal" : 40.5
  }
  ```
</ResponseExample>


# Cabin Climate
Source: https://smartcar.com/docs/api-reference/tesla/get-cabin

GET https://api.smartcar.com/v2.0/vehicles/{id}/{make}/climate/cabin
Returns the current state and target temperature setting of a vehicle's cabin climate system.

<Snippet file="api-reference/note-bse-tesla.mdx" />

## Permission

`read_climate`

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/climate/cabin" \
  -H "Authorization: Bearer {token}" \
  -X "GET"
  ```

  ```python Python theme={null}
  cabin = vehicle.request(
        "GET", 
        "{make}/climate/cabin"
  )
  ```

  ```js Node theme={null}
  const chargeCompletion = await vehicle.request(
        "GET", 
        "{make}/climate/cabin"
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("GET")
        .path("{make}/climate/cabin")
        .build();
  VehicleResponse chargeCompletion = vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  chargeCompletion = vehicle.request(
        "GET", 
        "{make}/climate/cabin"
  )
  ```
</RequestExample>

## Response

<ResponseField name="status" type="string">
  The current state of the climate cabin system.
</ResponseField>

<ResponseField name="temperature" type="number">
  The target temperature setting of the vehicle when the climate system is on (in Celsius by default or in Fahrenheit using the sc-unit-system).
</ResponseField>

<ResponseExample>
  ```json Example Response theme={null}
  {
    "status": "ON",
    "temperature": 20
  }
  ```
</ResponseExample>


# Tesla: Charge Status
Source: https://smartcar.com/docs/api-reference/tesla/get-charge

GET https://api.smartcar.com/v2.0/vehicles/{id}/{make}/charge
Returns all charging related data for a Tesla vehicle.

<Snippet file="api-reference/note-bse-tesla.mdx" />

<Warning>
  The following fields are not supported for streaming vehicles:

  * TeslaChargeRangeAddedRated
  * TeslaChargeRangeAddedIdeal
  * TeslaChargeChargeRate
  * TeslaChargeAmperageMaxCharger
  * TeslaChargeChargePortColor
</Warning>

## Permission

`read_charge`

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/charge" \
  -H "Authorization: Bearer {token}" \
  -X "GET"
  ```

  ```python Python theme={null}
  charge =  vehicle.request(
        "GET", 
        "{make}/charge"
  )
  ```

  ```js Node theme={null}
  const charge =  await vehicle.request(
        "GET", 
        "{make}/charge"
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("GET")
        .path("{make}/charge")
        .build();
  VehicleResponse charge =  vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  charge =  vehicle.request(
        "GET", 
        "{make}/charge"
  )
  ```
</RequestExample>

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

## Response

<ResponseField name="amperage" type="number | null">
  The rate that the vehicle is charging at (in amperes).
</ResponseField>

<ResponseField name="completionTime" type="string | null">
  An ISO8601 formatted datetime (YYYY-MM-DDTHH:mm:ss.SSSZ) for the time at which the vehicle expects to complete this charging session.
</ResponseField>

<ResponseField name="wattage" type="number | null">
  The instant power measured by the vehicle (in kilowatts).
</ResponseField>

<ResponseField name="isPluggedIn" type="bool | null">
  Indicates if the vehicle is plugged in
</ResponseField>

<ResponseField name="state" type="string | null">
  Indicates the charging status of the vehicle
</ResponseField>

<ResponseField name="socLimit" type="number | null">
  Indicates the level at which the vehicle will stop charging and be considered fully charged as a percentage.
</ResponseField>

<ResponseField name="amperageMaxVehicle" type="number | null">
  Indicates the max amperage the vehicle can request from the charger.
</ResponseField>

<ResponseField name="socLimitMax" type="number | null">
  Indicates the max SoC limit that can be set.
</ResponseField>

<ResponseField name="socLimitMin" type="number | null">
  Indicates the min SoC limit that can be set.
</ResponseField>

<ResponseField name="socLimitDefault" type="number | null">
  Indicates the default SoC limit of the vehicle.
</ResponseField>

<ResponseField name="amperageRequested" type="number | null">
  Indicates the amperage requested from the charger by the vehicle.
</ResponseField>

<ResponseField name="energyAdded" type="number | null">
  Energy added in the current charging session or most recent session if the vehicle is not charging (in kilowatts).
</ResponseField>

<ResponseField name="rangeAddedRated" type="number | null">
  The rated range as determined by Tesla added in the current charging session or most recent session if the vehicle is not charging (in kilometers added).
</ResponseField>

<ResponseField name="rangeAddedIdeal" type="number | null">
  The ideal range as determined by Tesla added in the current charging session or most recent session if the vehicle is not charging (in kilometers added).
</ResponseField>

<ResponseField name="chargeRate" type="number | null">
  The rate of range added in the charging session (in kilometers added / hour).
</ResponseField>

<ResponseField name="connector" type="string | null">
  Standard of the connector e.g. SAE
</ResponseField>

<ResponseField name="fastChargerPresent" type="bool | null">
  When charging, indicates if the vehicle connected to a fast charger.
</ResponseField>

<ResponseField name="fastChargerType" type="string | null">
  Indicates the type of fast charger.
</ResponseField>

<ResponseField name="fastChargerBrand" type="string | null">
  Indicates the brand of fast charger.
</ResponseField>

<ResponseField name="amperageMaxCharger" type="number | null">
  Indicates the max amperage supported by the charger.
</ResponseField>

<ResponseField name="chargePortColor" type="string | null">
  The indicator light color of the connector.
</ResponseField>

<ResponseField name="chargePortOpen" type="bool | null">
  Indicates if th charge port door is open.
</ResponseField>

<ResponseField name="chargePortLatch" type="string | null">
  Indicates if the charge port latch status.
</ResponseField>

<ResponseField name="chargerPhases" type="number | null">
  Indicates the charging phase.
</ResponseField>

<ResponseExample>
  ```json Example Response theme={null}
      {
            "amperage": 0,
            "completionTime": null,
            "wattage": 0,
            "voltage": 1,
            "isPluggedIn": false,
            "state": "NOT_CHARGING",
            "socLimit": 0.8,
            "amperageMaxVehicle": 48,
            "socLimitMax": 1,
            "socLimitMin": 0.5,
            "socLimitDefault": 0.8,
            "amperageRequested": 48,
            "energyAdded": 11.52,
            "rangeAddedRated": 70.811,
            "rangeAddedIdeal": 70.811,
            "chargeRate": 0,
            "connector": "<invalid>",
            "fastChargerPresent": false,
            "fastChargerType": "<invalid>",
            "fastChargerBrand": "<invalid>",
            "amperageMaxCharger": 48,
            "chargePortColor": "<invalid>",
            "chargePortOpen": false,
            "chargePortLatch": "Engaged",
            "chargerPhases": null
      }
  ```
</ResponseExample>


# Charge Completion Time
Source: https://smartcar.com/docs/api-reference/tesla/get-charge-completion-time

GET https://api.smartcar.com/v2.0/vehicles/{id}/{make}/charge/completion
When the vehicle is charging, returns the date and time when the vehicle is expected to reach its charge limit. When the vehicle is not charging, this endpoint results in a vehicle state error.

<Note>
  This endpoint is currently available for `tesla`.
</Note>

## Permission

`read_charge`

## Request

<ParamField path="id" type="string" required>
  `vehicle_id` of the vehicle you are making the request to.
</ParamField>

<ParamField path="make" type="string" required>
  The make to pass in the URL.
</ParamField>

<RequestExample>
  <Snippet file="api-reference/bse/get-charge-completion-time.mdx" />
</RequestExample>

## Response

<ResponseField name="time" type="string">
  An ISO8601 formatted datetime (`YYYY-MM-DDTHH:mm:ss.SSSZ`) for the time at which the vehicle expects to complete this charging session.
</ResponseField>

<ResponseExample>
  ```json Example Response theme={null}
  {
    "time": "2022-01-13T22:52:55.358Z"
  }
  ```
</ResponseExample>


# Charge Billing Records
Source: https://smartcar.com/docs/api-reference/tesla/get-charge-records-billing

GET https://api.smartcar.com/v2.0/vehicles/{id}/{make}/charge/records/billing
Returns information about charging sessions for Tesla vehicles at public Tesla chargers including cost and charging site.

<Snippet file="api-reference/note-bse-tesla.mdx" />

## Permission

`read_charge_records`

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

**Query**

<ParamField query="startDate">
  Date of the first record to return in YYYY-MM-DD format.
  Defaults to 30 days prior  or when the owner first granted your application access, whichever is shorter.
</ParamField>

<ParamField query="endDate">
  Date of the final record to return in YYYY-MM-DD format. Defaults to the date of the request.
</ParamField>

<ParamField query="page">
  The page number to fetch from Tesla where page 1 contains the most recent records.
</ParamField>

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/charge/records/billing?page=12&startDate=2023-08-24" \
      -H "Authorization: Bearer {token}" \
      -X "GET" \
      -H "Content-Type: application/json" \
  ```

  ```python Python theme={null}
  billing = vehicle.request(
    "GET", 
    "{make}/charge/records/billing?startDate=2023-08-24&page=12"
  )
  ```

  ```js Node theme={null}
  const billing = vehicle.request(
    "GET", 
    "{make}/charge/records/billing?startDate=2023-08-24&page=12"
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request =
      new SmartcarVehicleRequest.Builder()
          .method("GET")
          .path("ford/charge/schedule_by_location")
          .addQueryParameter("startDate", "2023-08-24")
          .addQueryParameter("page", "12")
          .build();

  VehicleResponse billing = vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  billing = vehicle.request(
    "GET", 
    "{make}/charge/records/billing?startDate=2023-08-24&page=12"
  )
  ```
</RequestExample>

## Response

<ResponseField name="records" type="[object]">
  An array of billing records for the vehicle associated with charging at public Tesla charging stations.

  Can be empty if the specified page does not contain any records for the vehicle.
  This **does not** mean that subsequent pages will also contain no records. Please check the `hasMoreData` field for confirmation instead.

  <Expandable defaultOpen="true">
    <ResponseField name="chargeStart" type="string">
      The date and time of charging session start, formatted in ISO 8601 standard.
    </ResponseField>

    <ResponseField name="chargeEnd" type="string">
      The date and time of charging session end, formatted in ISO 8601 standard.
    </ResponseField>

    <ResponseField name="energyConsumed" type="number" default="kWh">
      Energy consumed in the charging session.
    </ResponseField>

    <ResponseField name="cost" type="object">
      A cost breakout of the charging session.

      <Expandable defaultOpen="true">
        <ResponseField name="currency" type="string">
          The currency code for the fees.
        </ResponseField>

        <ResponseField name="energy" type="number">
          Fess associated with charging the vehicle.
        </ResponseField>

        <ResponseField name="other" type="number">
          Fees associated with the session other than charging the vehicle e.g. parking.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="location" type="string">
      The name of the charging site.
    </ResponseField>

    <ResponseField name="recordId" type="string">
      Tesla’s id for this charging session.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="hasMoreData" type="bool">
  Indicates if there are any more records to fetch from Tesla for this vehicle. **Does not** guarantee a non-empty list for the next page when `true`.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
    "records": [
        {
            "chargeEnd": "2022-07-10T16:20:00.000Z",
            "chargeStart": "2022-07-10T15:40:00.000Z",
            "energyConsumed": 44.10293884
            "cost": {
                "currency": "USD",
                "energy": "41",
                "other": "41"
            },
            "location": "Los Gatos, CA",
            "recordId": "GF220075000028-3-1682903685"
        }
    ],
    "hasMoreData" : false
  }
  ```
</ResponseExample>


# Charge Schedule
Source: https://smartcar.com/docs/api-reference/tesla/get-charge-schedule

GET https://api.smartcar.com/v2.0/vehicles/{id}/{make}/charge/schedule
Returns the charging schedule of a vehicle. The response contains the start time and departure time of the vehicle's charging schedule.

<Snippet file="api-reference/note-bse-tesla.mdx" />

## Permission

`read_charge`

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

<RequestExample>
  <Snippet file="api-reference/bse/get-charge-schedule.mdx" />
</RequestExample>

## Response

<ResponseField name="departureTime" type="object">
  The departure time configuration for the charging schedule.

  <Expandable title="departureTime">
    <ResponseField name="enabled" type="boolean">
      Indicates whether this schedule type is enabled or disabled.
      Only one of `departureTime` or `departureTime` can be enabled at a time.
    </ResponseField>

    <ResponseField name="time" type="string | null">
      When plugged in, the vehicle **may** delay starting a charging session as long as it can reach its
      [charge limit](/api-reference/evs/get-charge-limit) by this time in HH:mm.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="startTime" type="object">
  The start time configuration for the charging schedule.

  <Expandable title="startTime">
    <ResponseField name="enabled" type="boolean">
      Indicates whether this schedule type is enabled or disabled.
      Only one of `departureTime` or `departureTime` can be enabled at a time.
    </ResponseField>

    <ResponseField name="time" type="string | null">
      When plugged in, the vehicle will delay starting a charging session until this time in HH:mm.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
    "departureTime": {
      "enabled": false,
      "time": null
    },
    "startTime": {
      "enabled": true,
      "time": "18:30"
    }
  }
  ```
</ResponseExample>


# Voltage
Source: https://smartcar.com/docs/api-reference/tesla/get-charge-voltmeter

GET https://api.smartcar.com/v2.0/vehicles/{id}/{make}/charge/voltmeter
When the vehicle is plugged in, returns the charging voltage measured by the vehicle. When the vehicle is not plugged in, this endpoint results in a vehicle state error.

<Note>
  This endpoint is currently available for `tesla`.
</Note>

## Permission

`read_charge`

## Request

<Snippet file="api-reference/path-bse.mdx" />

<RequestExample>
  <Snippet file="api-reference/bse/get-charge-voltmeter.mdx" />
</RequestExample>

## Response

<ResponseField name="voltage" type="number">
  The potential difference measured by the vehicle in volts (V).
</ResponseField>

<ResponseExample>
  ```json Example Response theme={null}
  {
    "voltage": 240
  }
  ```
</ResponseExample>


# Wattage
Source: https://smartcar.com/docs/api-reference/tesla/get-charge-wattmeter

GET https://api.smartcar.com/v2.0/vehicles/{id}/{make}/charge/wattmeter
When the vehicle is charging, returns the instant charging wattage as measured by the vehicle. When the vehicle is not charging, this endpoint results in a vehicle state error.

<Snippet file="api-reference/note-bse-tesla.mdx" />

## Permission

`read_charge`

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/charge/wattmeter" \
  -H "Authorization: Bearer {token}" \
  -X "GET"
  ```

  ```python Python theme={null}
  wattmeter = vehicle.request(
        "GET", 
        "{make}/charge/wattmeter"
  )
  ```

  ```js Node theme={null}
  const wattmeter = await vehicle.request(
        "GET", 
        "{make}/charge/wattmeter"
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("GET")
        .path("{make}/charge/wattmeter")
        .build();
  VehicleResponse wattmeter = vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  wattmeter = vehicle.request(
        "GET", 
        "{make}/charge/wattmeter"
  )
  ```
</RequestExample>

## Response

<ResponseField name="wattage" type="number">
  The instant power measured by the vehicle (in kilowatts).
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
    "wattage": 3.5
  }
  ```
</ResponseExample>


# Compass
Source: https://smartcar.com/docs/api-reference/tesla/get-compass-heading

GET https://api.smartcar.com/v2.0/vehicles/{id}/{make}/compass
Returns the current compass heading and direction of the vehicle.

<Snippet file="api-reference/note-bse-tesla.mdx" />

## Permission

`read_compass`

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/compass" \
  -H "Authorization: Bearer {token}" \
  -X "GET"
  ```

  ```python Python theme={null}
  compass = vehicle.request(
        "GET", 
        "{make}/compass"
  )
  ```

  ```js Node theme={null}
  const compass = await vehicle.request(
        "GET", 
        "{make}/compass"
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("GET")
        .path("{make}/compass")
        .build();
  VehicleResponse compass = vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  compass = vehicle.request(
        "GET", 
        "{make}/compass"
  )
  ```
</RequestExample>

## Response

<ResponseField name="direction" type="string">
  The current direction of the vehicle.
</ResponseField>

<ResponseField name="heading" type="number">
  The current compass heading of the vehicle (in degrees).
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
    "direction": "SW",
    "heading": 185
  }
  ```
</ResponseExample>


# Defroster
Source: https://smartcar.com/docs/api-reference/tesla/get-defroster

GET https://api.smartcar.com/v2.0/vehicles/{is}/{make}/climate/defroster
Returns the current state of a vehicle's front and rear defroster.

<Snippet file="api-reference/note-bse-tesla.mdx" />

## Permission

`read_climate`

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/climate/defroster" \
  -H "Authorization: Bearer {token}" \
  -X "GET"
  ```

  ```python Python theme={null}
  defroster = vehicle.request(
        "GET", 
        "{make}/climate/defroster"
  )
  ```

  ```js Node theme={null}
  const defroster = await vehicle.request(
        "GET", 
        "{make}/climate/defroster"
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("GET")
        .path("{make}/climate/defroster")
        .build();
  VehicleResponse defroster = vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  defroster = vehicle.request(
        "GET", 
        "{make}/climate/defroster"
  )
  ```
</RequestExample>

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

## Response

<ResponseField name="frontStatus" type="string">
  The current state of the front defroster.
</ResponseField>

<ResponseField name="rearStatus" type="string">
  The current state of the rear defroster.
</ResponseField>

<ResponseExample>
  ```json Example Response   theme={null}
  {
    "frontStatus": "ON",
    "rearStatus": "OFF"
  }
  ```
</ResponseExample>


# Extended Vehicle Info
Source: https://smartcar.com/docs/api-reference/tesla/get-ext-vehicle-info

GET https://api.smartcar.com/v2.0/vehicles/{id}/{make}/attributes
Returns detailed configuration information for a vehicle.

<Snippet file="api-reference/note-bse-tesla.mdx" />

## Permission

`read_extended_vehicle_info`

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/attributes" \
  -H "Authorization: Bearer {token}" \
  -X "GET"
  ```

  ```python Python theme={null}
  attributes = vehicle.request(
        "GET", 
        "{make}/attributes"
  )
  ```

  ```js Node theme={null}
  const attributes = await vehicle.request(
        "GET", 
        "{make}/attributes"
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("GET")
        .path("{make}/attributes")
        .build();
  VehicleResponse attributes = vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  attributes = vehicle.request(
        "GET", 
        "{make}/attributes"
  )
  ```
</RequestExample>

## Response

<ResponseField name="id" type="string">
  A vehicle ID (UUID v4).
</ResponseField>

<ResponseField name="make" type="string">
  The manufacturer of the vehicle.
</ResponseField>

<ResponseField name="model" type="string">
  The model of the vehicle.
</ResponseField>

<ResponseField name="year" type="integer">
  The model year.
</ResponseField>

<ResponseField name="firmwareVersion" type="string">
  Vehicle's current firmware.
</ResponseField>

<ResponseField name="trimBadging" type="string">
  Indicates the Tesla's trim.
</ResponseField>

<ResponseField name="efficiencyPackage" type="string">
  Efficiency package.
</ResponseField>

<ResponseField name="performancePackage" type="string">
  Performance package.
</ResponseField>

<ResponseField name="nickname" type="string">
  Vehicle's nickname.
</ResponseField>

<ResponseField name="driverAssistVersion" type="string">
  Driver Assist version.
</ResponseField>

<ResponseField name="atHome" type="bool">
  Indicates `true` if the vehicle is currently at the home address set in the vehicle. `False` indicates the vehicle is not at home or home location is not set. This value is `null` if `atHome` status could not be determined.
  This field comes back as `null` if the vehicle is not capable of supporting Tesla's Telemetry API (streaming).
</ResponseField>

<ResponseField name="sentryMode" type="object">
  Sentry Mode status and availability.

  <Expandable>
    <ResponseField name="available" type="bool">
      Does the vehicle support Sentry Mode.
    </ResponseField>

    <ResponseField name="enabled" type="bool">
      Is Sentry Mode currently enabled for a vehicle.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="style" type="object">
  Descriptors of the vehicle's interior and exterior.

  <Expandable>
    <ResponseField name="exteriorColor" type="string">
      Exterior color.
    </ResponseField>

    <ResponseField name="exteriorTrim" type="string">
      Exterior trim.
    </ResponseField>

    <ResponseField name="interiorTrim" type="string">
      Interior trim.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="wheel" type="object">
  Descriptors of the vehicle's wheel.

  <Expandable>
    <ResponseField name="style" type="string">
      Style of the wheel.
    </ResponseField>

    <ResponseField name="diameter" type="number" default="millimeters">
      Diameter of the wheel.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="driveUnit" type="object">
  Details on the vehicle's drive unit(s).

  <Expandable>
    <ResponseField name="rear" type="string">
      Rear drive unit.
    </ResponseField>

    <ResponseField name="front" type="string">
      Front drive unit.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseExample>
  ```json Example Response theme={null}
  {
      "driveUnit": {
          "front": "PM216MOSFET",
          "rear": "NoneOrSmall"
      },
      "driverAssistVersion": "TeslaAP3",
      "efficiencyPackage": "MY2021",
      "firmwareVersion": "2022.8.10.12 0ce482dac45d",
      "id": "36ab27d0-fd9d-4455-823a-ce30af709ffc",
      "make": "TESLA",
      "model": "Model S",
      "nickname": "Tommy",
      "performancePackage": "Base",
      "sentryMode": {
          "available": false,
          "enabled": true
      },
      "style": {
          "exteriorColor": "SolidBlack",
          "exteriorTrim": "Black",
          "interiorTrim": "Black2"
      },
      "trimBadging": "74d",
      "wheel": {
          "diameter": 482.6,
          "style": "Apollo"
      },
      "year": 2022,
      "atHome": true
  }
  ```
</ResponseExample>


# Exterior Temperature
Source: https://smartcar.com/docs/api-reference/tesla/get-exterior-temperature

GET https://api.smartcar.com/v2.0/vehicles/{id}/{make}/thermometer/exterior
Returns the vehicle’s last known exterior thermometer reading. See our [climate setting](/docs/api-reference/tesla/get-cabin) endpoints for managing a cabin temperature.

<Snippet file="api-reference/note-bse-tesla.mdx" />

## Permission

`read_thermometer`

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/thermometer/exterior" \
  -H "Authorization: Bearer {token}" \
  -X "GET"
  ```

  ```python Python theme={null}
  temperature = vehicle.request(
        "GET", 
        "{make}/thermometer/exterior"
  )
  ```

  ```js Node theme={null}
  const temperature = await vehicle.request(
        "GET", 
        "{make}/thermometer/exterior"
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("GET")
        .path("{make}/thermometer/exterior")
        .build();
  VehicleResponse temperature = vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  temperature = vehicle.request(
        "GET", 
        "{make}/thermometer/exterior"
  )
  ```
</RequestExample>

## Response

<ResponseField name="temperature" default="celsius" type="number">
  The current exterior temperature of the vehicle.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
    "temperature": 33.42
  }
  ```
</ResponseExample>


# Interior Temperature
Source: https://smartcar.com/docs/api-reference/tesla/get-interior-temperature

GET https://api.smartcar.com/v2.0/vehicles/{id}/{make}/thermometer/interior
Returns the vehicle’s last known interior thermometer reading. See our [climate setting](/docs/api-reference/tesla/get-cabin) endpoints for managing a cabin temperature.

<Snippet file="api-reference/note-bse-tesla.mdx" />

## Permission

`read_thermometer`

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/thermometer/interior" \
  -H "Authorization: Bearer {token}" \
  -X "GET"
  ```

  ```python Python theme={null}
  temperature = vehicle.request(
        "GET", 
        "{make}/thermometer/interior"
  )
  ```

  ```js Node theme={null}
  const temperature = await vehicle.request(
        "GET", 
        "{make}/thermometer/interior"
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("GET")
        .path("{make}/thermometer/interior")
        .build();
  VehicleResponse temperature = vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  temperature = vehicle.request(
        "GET", 
        "{make}/thermometer/interior"
  )
  ```
</RequestExample>

## Response

<ResponseField name="temperature" default="celsius" type="number">
  The current interior temperature of the vehicle.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
    "temperature": 25.64
  }
  ```
</ResponseExample>


# Migration Status
Source: https://smartcar.com/docs/api-reference/tesla/get-migration-status

GET https://api.smartcar.com/v2.0/vehicles/{id}/{make}/migration
Indicates if the vehicle needs to migrate to Tesla's new API. See [Tesla - What's New](https://smartcar.com/docs/help/oem-integrations/tesla/whats-new) for more details.

<Snippet file="api-reference/note-bse-tesla.mdx" />

## Permission

`read_vehicle_info`

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/migration" \
  -H "Authorization: Bearer {token}" \
  -X "GET"
  ```

  ```python Python theme={null}
  status = vehicle.request(
        "GET", 
        "{make}/migration"
  )
  ```

  ```js Node theme={null}
  const status = await vehicle.request(
        "GET", 
        "{make}/migration"
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("GET")
        .path("{make}/migration")
        .build();
  VehicleResponse status = vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  status = vehicle.request(
        "GET", 
        "{make}/migration"
  )
  ```
</RequestExample>

## Response

<ResponseField name="requiresMigration" type="boolean">
  Set to `false` if the vehicle is connected to Smartcar via Tesla's new integration. See [Tesla - What's New](/help/oem-integrations/tesla/whats-new) for more details.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
      "requiresMigration": false
  }
  ```
</ResponseExample>


# Speed
Source: https://smartcar.com/docs/api-reference/tesla/get-speedometer

GET https://api.smartcar.com/v2.0/vehicles/{id}/{make}/speedometer
Returns the current speed of the vehicle.

<Snippet file="api-reference/note-bse-tesla.mdx" />

## Permission

`read_speedometer`

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/speedometer" \
  -H "Authorization: Bearer {token}" \
  -X "GET"
  ```

  ```python Python theme={null}
  speed = vehicle.request(
        "GET", 
        "{make}/speedometer"
  )
  ```

  ```js Node theme={null}
  const speed = await vehicle.request(
        "GET", 
        "{make}/speedometer"
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("GET")
        .path("{make}/speedometer")
        .build();
  VehicleResponse speed = vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  speed = vehicle.request(
        "GET", 
        "{make}/speedometer"
  )
  ```
</RequestExample>

## Response

<ResponseField name="speed" default="km/h" type="number">
  The current speed of the vehicle.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
    "speed": 84.32
  }
  ```
</ResponseExample>


# Steering Heater
Source: https://smartcar.com/docs/api-reference/tesla/get-steering-heater

GET https://api.smartcar.com/v2.0/vehicles/{id}/{make}/climate/steering_wheel
Returns the current state of a vehicle's steering wheel heater system.

<Snippet file="api-reference/note-bse-tesla.mdx" />

## Permission

`read_climate`

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/climate/steering_wheel" \
  -H "Authorization: Bearer {token}" \
  -X "GET"
  ```

  ```python Python theme={null}
  steering_wheel = vehicle.request(
        "GET", 
        "{make}/climate/steering_wheel"
  )
  ```

  ```js Node theme={null}
  const steeringWheel = await vehicle.request(
        "GET", 
        "{make}/climate/steering_wheel"
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("GET")
        .path("{make}/climate/steering_wheel")
        .build();
  VehicleResponse steeringWheel = vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  steering_wheel = vehicle.request(
        "GET", 
        "{make}/climate/steering_wheel"
  )
  ```
</RequestExample>

## Response

<ResponseField name="status" type="enum">
  The current state of the steering wheel heater system. `UNAVAILABLE` indicates the vehicle is not equipped with a steering wheel heater.
</ResponseField>

<ResponseExample>
  ```json Example Response theme={null}
  {
    "status": "ON",
  }
  ```
</ResponseExample>


# User Access
Source: https://smartcar.com/docs/api-reference/tesla/get-user-access

GET https://api.smartcar.com/v2.0/vehicles/{id}/{make}/user/access
Returns the account type and permissions for the connected Tesla account.

<Snippet file="api-reference/note-bse-tesla.mdx" />

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/user/access" \
  -H "Authorization: Bearer {token}" \
  -X "GET"
  ```

  ```python Python theme={null}
  access = vehicle.request(
        "GET", 
        "{make}/user/access"
  )
  ```

  ```js Node theme={null}
  const access = await vehicle.request(
        "GET", 
        "{make}/user/access"
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("GET")
        .path("{make}/user/access")
        .build();
  VehicleResponse access =vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  access = vehicle.request(
        "GET", 
        "{make}/user/access"
  )
  ```
</RequestExample>

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

## Response

<ResponseField name="accessType" type="string | null">
  Returns the type of Tesla account connected. Can be either `OWNER` or `DRIVER`. Please see our [Tesla FAQs](/help/oem-integrations/tesla/faqs) for details on the differences between account types.
</ResponseField>

<ResponseField name="permissions" type="[string] | null">
  Returns a list of permissions granted by the user with their Tesla account. Please see [this page](/help/oem-integrations/tesla/developers#permission-mappings) on the mapping from Smartcar permissions to Tesla's.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
    "accessType": "OWNER",
    "permissions" : ["vehicle_cmds", "vehicle_device_data"]
  }
  ```
</ResponseExample>

## Notes

* If you're receiving a [SERVER:INTERNAL](/errors/api-errors/server-errors#internal) error please have the user reconnect their vehicle.


# User Info
Source: https://smartcar.com/docs/api-reference/tesla/get-user-info

GET https://api.smartcar.com/v2.0/vehicles/{id}/{make}/user/info
Returns the email associated with the connected Tesla account.

<Snippet file="api-reference/note-bse-tesla.mdx" />

## Permission

`read_user_profile`

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/user/info" \
  -H "Authorization: Bearer {token}" \
  -X "GET"
  ```

  ```python Python theme={null}
  info = vehicle.request(
        "GET", 
        "{make}/user/info"
  )
  ```

  ```js Node theme={null}
  const info = await vehicle.request(
        "GET", 
        "{make}/user/info"
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("GET")
        .path("{make}/user/info")
        .build();
  VehicleResponse info =vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  info = vehicle.request(
        "GET", 
        "{make}/user/info"
  )
  ```
</RequestExample>

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

## Response

<ResponseField name="email" type="string | null">
  The email associated with the connected Tesla account.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
      {
          "email" : "api@smartcar.com"
      }
  ```
</ResponseExample>


# Vehicle Status
Source: https://smartcar.com/docs/api-reference/tesla/get-vehicle-status

GET https://api.smartcar.com/v2.0/vehicles/{id}/{make}/status
Returns the status for the vehicle.

<Snippet file="api-reference/note-bse-tesla.mdx" />

## Permission

`read_extended_vehicle_info`

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/status" \
  -H "Authorization: Bearer {token}" \
  -X "GET"
  ```

  ```python Python theme={null}
  status = vehicle.request(
        "GET", 
        "{make}/status"
  )
  ```

  ```js Node theme={null}
  const status = await vehicle.request(
        "GET", 
        "{make}/status"
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("GET")
        .path("{make}/status")
        .build();
  VehicleResponse status = vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  status = vehicle.request(
        "GET", 
        "{make}/status"
  )
  ```
</RequestExample>

## Response

<ResponseField name="status" type="string">
  The current status of the vehicle. If the vehicle is asleep, this request will not wake the vehicle.
</ResponseField>

<ResponseField name="inService" type="bool">
  Indicates if the vehicle is in service mode.
</ResponseField>

<ResponseField name="gear" type="string">
  Indicates the current gear shift position.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
  "status": "ASLEEP",
  "inService": true,
  "gear": "DRIVE"
  }
  ```
</ResponseExample>


# Virtual Key Status
Source: https://smartcar.com/docs/api-reference/tesla/get-virtual-key-status

GET https://api.smartcar.com/v2.0/vehicles/{id}/{make}/virtual_key
Indicates if a vehicle has the appropriate virtual key installed. See [Tesla - What's New](https://smartcar.com/docs/help/oem-integrations/tesla/whats-new#if-your-application-issues-commands) for more details on Tesla's virtual key requirements.

<Snippet file="api-reference/note-bse-tesla.mdx" />

## Permission

`read_vehicle_info`

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/virtual_key" \
  -H "Authorization: Bearer {token}" \
  -X "GET"
  ```

  ```python Python theme={null}
  virtual_key = vehicle.request(
        "GET", 
        "{make}/virtual_key"
  )
  ```

  ```js Node theme={null}
  const virtualKey = await vehicle.request(
        "GET", 
        "{make}/virtual_key"
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("GET")
        .path("{make}/virtual_key")
        .build();
  VehicleResponse virtualKey = vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  virtual_key = vehicle.request(
        "GET", 
        "{make}/virtual_key"
  )
  ```
</RequestExample>

## Response

<ResponseField name="isPaired" type="boolean">
  Returns `true` if the vehicle has the appropriate Virtual Key installed. See [Tesla - What's New](/help/oem-integrations/tesla/whats-new#if-your-application-issues-commands) for more details on Tesla's virtual key requirements.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
      "isPaired": true
  }
  ```
</ResponseExample>

## Notes

* This endpoint will throw a [COMPATIBILITY:PLATFORM\_NOT\_CAPABLE](/errors/api-errors/compatibility-errors#platform-not-capable) error if a vehicle is connected to your application via Tesla's legacy integration.
* This endpoint will throw a [CONNECTED\_SERVICES\_ACCOUNT:VEHICLE\_MISSING](/errors/api-errors/compatibility-errors#vehicle-missing) error if the Tesla account connected to Smartcar is **not** the Owner of the vehicle. See our [FAQs](/help/oem-integrations/tesla/faqs#can-owner-and-driver-accounts-authorize-access-with-smartcar-through-connect) for more information on Owner and Driver account types.


# Cabin Climate
Source: https://smartcar.com/docs/api-reference/tesla/set-cabin

POST https://api.smartcar.com/v2.0/vehicles/{id}/{make}/climate/cabin
Set the temperature and control the cabin climate system for a vehicle.

<Snippet file="api-reference/note-bse-tesla.mdx" />

## Permission

`control_climate`

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

**Body**

<ParamField body="action" type="string" required>
  Indicate whether to start or stop the cabin climate control system, or set the temperature.
  If starting or stopping the system, `temperature` is optional and will use the vehicle's current setting by default.

  <Expandable title="status">
    <ResponseField name="START" type="string" />

    <ResponseField name="STOP" type="string" />

    <ResponseField name="SET" type="string">
      Use `SET` to set the `temperature` without changing the climate systems status.
    </ResponseField>
  </Expandable>
</ParamField>

<ParamField body="temperature" type="string">
  Indicate what temperature to set (in Celsius by default or in Fahrenheit using the sc-unit-system).
  If the provided temperature is out of the bounds allowed by the vehicle's climate control system,
  the request will fail with the upper and lower limits in the error response message.
</ParamField>

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/climate/cabin" \
  -H "Authorization: Bearer {token}" \
  -X "POST" \
  -H "Content-Type: application/json" \
  -d '{"action": "SET", "temperature": 20}'
  ```

  ```python Python theme={null}
  set_climate_cabin = vehicle.request(
    "POST", 
    "{make}/climate/cabin", 
    {
      "action": "SET", 
      "temperature": 18
    }
  )

  ```

  ```js Node theme={null}
  const vehicleStopCabin = vehicle.request(
    "POST", 
    "{make}/climate/cabin", 
    {"action": "STOP"}
  );

  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("POST")
        .path("{make}/climate/cabin")
        .addBodyParameter("action", "START")
        .build();
  VehicleResponse startClimateCabin = vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  setChargeScheduleByLocation = vehicle.request(
    "POST", 
    "{make}/climate/cabin", 
    {"action" : "START"}
  )
  ```
</RequestExample>

## Response

<ResponseField name="status" type="string">
  If the request is successful, Smartcar will return `"success"` (HTTP 200 status) containing the current state of the climate cabin system.
</ResponseField>

<ResponseField name="temperature" type="number">
  The target temperature setting of the vehicle when the climate system is on (in Celsius by default or in Fahrenheit using the sc-unit-system).
</ResponseField>

<ResponseExample>
  ```json Example Response theme={null}
  {
    "status": "ON",
    "temperature": 24
  }
  ```
</ResponseExample>


# Amperage
Source: https://smartcar.com/docs/api-reference/tesla/set-charge-ammeter

POST https://api.smartcar.com/v2.0/vehicles/{id}/{make}/charge/ammeter
Set the amperage drawn by the vehicle from the EVSE for the current charging session. If the vehicle is not plugged in, this endpoint results in a vehicle state error.

<Snippet file="api-reference/note-bse-tesla.mdx" />

## Permission

`control_charge`

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

**Body**

<ParamField body="amperage" type="number" required>
  The target amperage to be drawn by the vehicle from the charging point (in amperes). If the value passed is greater than what is supported by the charger, it will be set to the maximum.
</ParamField>

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/charge/ammeter" \
  -H "Authorization: Bearer {token}" \
  -X "POST" \
  -H "Content-Type: application/json" \
  -d '{"amperage": 48}'
  ```

  ```python Python theme={null}
  ammeter = vehicle.request(
    "POST", 
    "{make}/charge/ammeter", 
    {"amperage": 48}
  )
  ```

  ```js Node theme={null}
  const ammeter = vehicle.request(
    "POST", 
    "{make}/charge/ammeter", 
    {"amperage": 48}
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("POST")
        .path("{make}/charge/ammeter")
        .addBodyParameter("amperage": 48)
        .build();
  VehicleResponse ammeter = vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  ammeter = vehicle.request(
    "POST", 
    "{make}/charge/ammeter", 
    {"amperage": 48}
  )
  ```
</RequestExample>

## Response

<ResponseField name="message" type="string">
  If the request is successful, Smartcar will return “success” (HTTP 200 status). If the amperage passed was greater than what is supported by the charger, it will be set to the maximum which will be shown here.
</ResponseField>

<ResponseField name="status" type="string">
  If the request is successful, Smartcar will return a message (HTTP 200 status) containing the amperage set to be drawn from the vehicle.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
    "message": "Successfully sent the following amperage: 48",
    "status": "success"
  }
  ```
</ResponseExample>


# Charge Schedule
Source: https://smartcar.com/docs/api-reference/tesla/set-charge-schedule

POST https://api.smartcar.com/v2.0/vehicles/{id}/{make}/charge/schedule
Sets the charging schedule for a vehicle.

<Snippet file="api-reference/note-bse-tesla.mdx" />

## Permission

`control_charge`

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

**Body**

<ParamField body="type" type="string" required>
  The type of schedule you want to set.

  <Expandable title="type" defaultOpen="true">
    <ResponseField name="START_TIME">
      When plugged in, the vehicle will delay starting a charging session until this time in `HH:mm`.
    </ResponseField>

    <ResponseField name="DEPARTURE_TIME">
      When plugged in, the vehicle may delay starting a charging session as long as it can reach its
      [charge limit](/api-reference/evs/get-charge-limit) by this time in `HH:mm`.
    </ResponseField>
  </Expandable>
</ParamField>

<ParamField body="enable" type="boolean" required>
  Enables or disables the specified charging schedule.
</ParamField>

<ParamField body="time" type="string" required>
  The time for the provided schedule type in HH:mm.
</ParamField>

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/charge/schedule" \
  -H "Authorization: Bearer {token}" \
  -X "POST" \
  -H "Content-Type: application/json" \
  -d '{"type": "START_TIME", "enable": true, "time": "23:30"}'
  ```

  ```python Python theme={null}
  chargeSchedule = vehicle.request(
    "POST", 
    "{make}/charge/schedule",
    {"type": "START_TIME", "enable": true, "time": "23:30"}
  )
  ```

  ```js Node theme={null}
  const chargeSchedule = vehicle.request(
    "POST", 
    "{make}/charge/schedule",
    {"type": "START_TIME", "enable": true, "time": "23:30"}
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("POST")
        .path("{make}/charge/schedule")
        .addBodyParameter("type", "START_TIME")
        .addBodyParameter("enable", "true")
        .addBodyParameter("time", "23:30")
        .build();
  ChargeSchedule chargeSchedule = vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  chargeSchedule = vehicle.request(
    "POST", 
    "{make}/charge/schedule",
    {"type": "START_TIME", "enable": true, "time": "23:30"}
  )
  ```
</RequestExample>

## Response

<ResponseField name="departureTime" type="object">
  The departure time configuration for the charging schedule.

  <Expandable title="departureTime">
    <ResponseField name="enabled" type="boolean">
      Indicates whether this schedule type is enabled or disabled.
      Only one of `departureTime` or `departureTime` can be enabled at a time.
    </ResponseField>

    <ResponseField name="time" type="string | null">
      When plugged in, the vehicle **may** delay starting a charging session as long as it can reach its
      [charge limit](/api-reference/evs/get-charge-limit) by this time in HH:mm.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="startTime" type="object">
  The start time configuration for the charging schedule.

  <Expandable title="startTime">
    <ResponseField name="enabled" type="boolean">
      Indicates whether this schedule type is enabled or disabled.
      Only one of `departureTime` or `departureTime` can be enabled at a time.
    </ResponseField>

    <ResponseField name="time" type="string | null">
      When plugged in, the vehicle will delay starting a charging session until this time in HH:mm.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseExample>
  ```json Example Response theme={null}
  {
    "departureTime": {
      "enabled": false,
      "time": null
    },
    "startTime": {
      "enabled": true,
      "time": "18:30"
    }
  }
  ```
</ResponseExample>


# Defroster
Source: https://smartcar.com/docs/api-reference/tesla/set-defroster

POST https://api.smartcar.com/v2.0/vehicles/{id}/{make}/climate/defroster
Start or stop the front and rear defroster for a vehicle.

<Snippet file="api-reference/note-bse-tesla.mdx" />

## Permission

`control_climate`

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

**Body**

<ParamField body="action" type="string" required>
  Indicate whether to start or stop defrosting the vehicle.
  Options: `START` or `STOP`
</ParamField>

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/climate/defroster" \
  -H "Authorization: Bearer {token}" \
  -X "POST" \
  -H "Content-Type: application/json" \
  -d '{"action" : "STOP"}'
  ```

  ```python Python theme={null}
  defroster = vehicle.request(
    "POST", 
    "{make}/climate/defroster", 
    {"action" : "STOP"}
  )
  ```

  ```js Node theme={null}
  const defroster = vehicle.request(
    "POST", 
    "{make}/climate/defroster", 
    {"action" : "STOP"}
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("POST")
        .path("{make}/climate/defroster")
        .addBodyParameter("action" : "STOP")
        .build();
  VehicleResponse defroster = vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  defroster = vehicle.request(
    "POST", 
    "{make}/climate/defroster", 
    {"action" : "STOP"}
  )
  ```
</RequestExample>

## Response

<ResponseField name="status" type="string">
  If the request is successful, Smartcar will return `status` containing the action sent to the
  climate defroster system of the vehicle.
</ResponseField>

<ResponseExample>
  ```json Example Response   theme={null}
  {
    "status": "START"
  }
  ```
</ResponseExample>


# Set PIN to Drive
Source: https://smartcar.com/docs/api-reference/tesla/set-pin-to-drive

POST https://api.smartcar.com/v2.0/vehicles/{id}/{make}/pin
Enables this feature on the vehicle and sets the PIN needed in order to drive it.

<Snippet file="api-reference/note-bse-tesla.mdx" />

## Permission

`control_pin`

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

**Body**

<ParamField body="pin" type="string" required>
  A four digit numeric PIN
</ParamField>

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/pin" \
  -H "Authorization: Bearer {token}" \
  -X "POST" \
  -H "Content-Type: application/json" \
  -d '{"pin" : "1234"}'
  ```

  ```python Python theme={null}
  pin = vehicle.request(
    "POST", 
    "{make}/pin", 
    {"pin" : "1234"}
  )
  ```

  ```js Node theme={null}
  const pin = vehicle.request(
    "POST", 
    "{make}/pin", 
    {"pin" : "1234"}
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("POST")
        .path("{make}/pin")
        .addBodyParameter("pin" : "1234")
        .build();
  VehicleResponse pin =  vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  pin =  vehicle.request(
    "POST", 
    "{make}/pin", 
    {"pin" : "1234"}
  )
  ```
</RequestExample>

## Response

<ResponseField name="status" type="string">
  If the request is successful, Smartcar will return “success”.
</ResponseField>

<ResponseField name="message" type="string">
  If the request is successful, Smartcar will return a message.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
      {
          "message": "Successfully sent request to vehicle",
          "status": "success"
      }   
  ```
</ResponseExample>

## Notes

* Calling this endpoint will override an existing PIN on the vehicle.
* Call `DELETE` [PIN to Drive](/api-reference/tesla/clear-pin-to-drive) in order to enable this feature and set the PIN
* Currently both owner and driver account types can set a PIN for the vehicle and enable the feature via the API.
* Only account owners can disable this feature from the Tesla app.


# Steering Heater
Source: https://smartcar.com/docs/api-reference/tesla/set-steering-heater

POST https://api.smartcar.com/v2.0/vehicles/{id}/{make}/climate/steering_wheel
Start or stop heating a vehicle's steering wheel.

<Snippet file="api-reference/note-bse-tesla.mdx" />

## Permission

`control_climate`

## Request

**Path**

<Snippet file="api-reference/path-bse.mdx" />

**Body**

<ParamField body="action" type="string" required>
  Indicate whether to start or stop heating the vehicle's steering wheel.
  Options: `START` or `STOP`
</ParamField>

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/{make}/climate/steering_wheel" \
  -H "Authorization: Bearer {token}" \
  -X "POST" \
  -H "Content-Type: application/json" \
  -d '{"action" : "STOP"}'
  ```

  ```python Python theme={null}
  steering_wheel = vehicle.request(
    "POST", 
    "{make}/climate/steering_wheel", 
    {"action" : "STOP"}
  )
  ```

  ```js Node theme={null}
  const steeringWheel = vehicle.request(
    "POST", 
    "{make}/climate/steering_wheel", 
    {"action" : "STOP"}
  );
  ```

  ```java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
        .method("POST")
        .path("{make}/climate/steering_wheel")
        .addBodyParameter("action" : "STOP")
        .build();
  VehicleResponse steeringWheel =  vehicle.request(request);
  ```

  ```ruby Ruby theme={null}
  steering_wheel =  vehicle.request(
    "POST", 
    "{make}/climate/steering_wheel", 
    {"action" : "STOP"}
  )
  ```
</RequestExample>

## Response

<ResponseField name="status" type="string">
  If the request is successful, Smartcar will return status containing the action sent to the vehicle.
  `UNAVAILABLE` indicates the vehicle is not equipped with a steering wheel heater.
</ResponseField>

<ResponseExample>
  ```json Example Response theme={null}
  {
    "status": "START",
  }
  ```
</ResponseExample>


# User
Source: https://smartcar.com/docs/api-reference/user

GET https://api.smartcar.com/v2.0/user
Returns the ID of the vehicle owner who granted access to your application.

<Note>
  This endpoint is under a different path while we complete the transition to v3.0. You can safely continue using this endpoint, but please be aware that it may be deprecated in the future.
</Note>

This should be used as the static unique identifier for storing the access token and refresh token pair in your database.
Note: A single user can own multiple vehicles, and multiple users can own the same vehicle.

<Info>
  When using Single Select for Connect, a single user with multiple vehicles
  will have a 1:1 (`access_token`:`vehicle_id`) mapping.
</Info>

<RequestExample>
  <Snippet file="api-reference/core-sdk-methods/user.mdx" />
</RequestExample>

## Response

<ResponseField name="id" type="string">
  A user ID (UUID v4).
</ResponseField>

<ResponseExample>
  ```json Example Response theme={null}
  {
      "id": "e0514ef4-5226-11e8-8c13-8f6e8f02e27e"
  }   
  ```
</ResponseExample>


# User Vehicles
Source: https://smartcar.com/docs/api-reference/user-vehicles

GET https://api.smartcar.com/v2.0/vehicles
Returns a paged list of all vehicles connected to the application for the current authorized `user`.

<Note>
  This endpoint is under a different path while we complete the transition to v3.0. You can safely continue using this endpoint, but please be aware that it may be deprecated in the future.
</Note>

## Request

**Query**

<ParamField query="limit" type="integer" default="10">
  The number of vehicles to return per page. `Max: 50`
</ParamField>

<ParamField query="offset" type="integer">
  The index to start the `vehicles` list at.
</ParamField>

<RequestExample>
  <Snippet file="api-reference/core-sdk-methods/all-vehicles.mdx" />
</RequestExample>

## Response

<ResponseField name="paging" type="Object">
  Metadata about the current list of elements.

  <Expandable>
    <ResponseField name="count" type="integer">
      The total number of elements for the entire query (not just the given page).
    </ResponseField>

    <ResponseField name="offset" type="integer">
      The current start index of the returned list of elements.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="vehicles" type="[string]">
  An array of vehicle IDs.
</ResponseField>

<ResponseExample>
  ```json Example Response theme={null}
  {
      "paging": {
          "count": 25,
          "offset": 10
      },
      "vehicles": [
          "36ab27d0-fd9d-4455-823a-ce30af709ffc"
      ]
  }
  ```
</ResponseExample>


# Vehicles API v2.0 Overview
Source: https://smartcar.com/docs/api-reference/v2-overview

Overview of the Smartcar Vehicles API v2.0 and deprecation notice.

<Warning>
  The Vehicles API v2.0 will be deprecated by **Q3 of 2026**. We recommend migrating to the [latest version](/api-reference/vehicles-api-intro) as soon as possible to ensure continued support and access to new features.
</Warning>

<Note>
  2.0 is still the only supported version for sending remote commands. If you need to send commands, please continue using v2.0 until commands are supported in the latest version later this year.
</Note>

The Smartcar Vehicles API v2.0 is the previous version of our core API for accessing standardized vehicle data and current version for sending remote commands. It allows developers to:

* Retrieve real-time vehicle signals (e.g., battery level, odometer, fuel, tire pressure)
* Send remote commands (lock/unlock, start/stop charging, etc.)

All requests to v2.0 require an OAuth2 access token, which is obtained by having the vehicle owner authorize your app via [Smartcar Connect](/connect/what-is-connect).

## Base URL

```
https://api.smartcar.com/v2.0
```

For this API, the latency response times may vary per vehicle make and model. For more information, see [OEM Latency](/help/oem-latency).


# Vehicles API Overview
Source: https://smartcar.com/docs/api-reference/vehicles-api-intro

The Vehicles API is Smartcar’s core API for accessing standardized vehicle data and sending remote commands to connected vehicles. It enables you to build applications that interact with a wide range of makes and models through a single, unified interface.

## What You Can Do

* Retrieve last known vehicle signals (e.g., battery level, odometer, fuel, tire pressure)
* Access vehicle attributes (make, model, year, VIN, etc.)
* Send remote commands (lock/unlock, start/stop charging, etc.)

The Vehicles API is designed primarily for exploration and non-frequent data retrieval. This API is not designed for continuous polling or real-time monitoring. Data is typically updated once every 24 hours unless the vehicle is actively subscribed to a webhook, which enables more frequent updates. For most use cases, you should avoid polling the Vehicles API at high frequency leverage [webhooks](/integrations/webhooks/overview) instead.

## Authentication

All requests require an OAuth2 access token, which is obtained by having the vehicle owner authorize your app via [Smartcar Connect](/connect/what-is-connect).

* Learn how to get an access token in our [Getting Started guide](/getting-started/how-to/get-an-access-token).
* Learn more about the [Auth Token Exchange](/api-reference/authorization/auth-code-exchange) process.

## Base URL

```
https://vehicle.api.smartcar.com/v3
```

## Key Resources

* [Signal Schema](/api-reference/signals/schema)
* [Permissions](/api-reference/permissions)
* [Error Codes](/api-reference/api-errors)

## Example Use Cases

* Fleet management and telematics
* Insurance and mileage tracking
* EV charging and energy management
* Car sharing and rental platforms

<Info>
  For a step-by-step guide to integrating with the Vehicles API, see [Getting Started](/getting-started/introduction).
</Info>


# Subscribe
Source: https://smartcar.com/docs/api-reference/webhooks/subscribe-webhook

POST https://api.smartcar.com/v2.0/vehicles/{id}/webhooks/{webhook_id}
Subscribe a vehicle to a webhook.

## Request

**Path**

<Snippet file="api-reference/path-vehicle-id.mdx" />

<ParamField path="webhook_id" type="string" initialValue="9b6ae692-60cc-4b3e-89d8-71e7549cf805" required>
  The webhook id you are subscribing the vehicle to. This can be found in Dashboard under Webhooks.
</ParamField>

<Snippet file="code-group-subscribe.mdx" />

<RequestExample>
  <Snippet file="api-reference/core-sdk-methods/subscribe-webhook.mdx" />
</RequestExample>

## Response

<ResponseField name="vehicleId" type="string">
  The [vehicle id](/api-reference/all-vehicles) of the vehicle you are making a request to.
</ResponseField>

<ResponseField name="webhookId" type="string">
  The webhook id you are subscribing the vehicle to.
</ResponseField>

<ResponseExample>
  ```json ResponseExample theme={null}
  {
      "vehicleId": "dc6ea99e-57d1-4e41-b129-27e7eb58713e",
      "webhookId": "9b6ae692-60cc-4b3e-89d8-71e7549cf805"
  }   
  ```
</ResponseExample>


# Unsubscribe
Source: https://smartcar.com/docs/api-reference/webhooks/unsubscribe-webhook

DELETE https://api.smartcar.com/v2.0/vehicles/{id}/webhooks/{webhook_id}
Unsubscribe a vehicle from a webhook.

## Request

**Header**

<ParamField header="Authorization" type="string" initialValue="Bearer {application_management_token}" required>
  In the format `Bearer {application_management_token}`. You can find your `application_management_token` under
  your Application Configuration in Dashboard.
</ParamField>

**Path**

<Snippet file="api-reference/path-vehicle-id.mdx" />

<ParamField path="webhook_id" type="string" initialValue="9b6ae692-60cc-4b3e-89d8-71e7549cf805" required>
  The [webhook id](/api-reference/management/get-vehicle-connections) you are unsubscribing the vehicle from.
</ParamField>

<RequestExample>
  <Snippet file="api-reference/core-sdk-methods/unsubscribe-webhook.mdx" />
</RequestExample>

## Response

<ResponseField name="status" type="string">
  Status of the request.
</ResponseField>

<ResponseExample>
  ```json Example Response theme={null}
  {
      "status": "success"
  }
  ```
</ResponseExample>


# 2022 Releases
Source: https://smartcar.com/docs/changelog/2022



## January 5, 2022

Smartcar is now compatible with Mercedes-Benz vehicles in the United States.

## February 23, 2022

The EV Battery and EV Charging status and control endpoints are now available for Lexus and Toyota vehicles in Canada and the United States.

## February 21, 2022

The Tire Pressure endpoint is now available for Lexus and Toyota vehicles in Canada and the United States.

## February 14, 2022

Smartcar is now compatible with Chrysler, Dodge, Jeep, and RAM vehicles in Canada.

## February 2, 2022

Brand-specific endpoints are now available for Cadillac, Chevrolet, and Tesla. A full list of the available endpoints is available in the API Reference.

<CodeGroup>
  ```Node Node theme={null}
  const amperage = vehicle.request('GET', 'tesla/charge/ammeter');
  ```

  ```Python Python theme={null}
  amperage = vehicle.request("GET", "tesla/charge/ammeter")
  ```

  ```Java Java theme={null}
  SmartcarVehicleRequest request = new SmartcarVehicleRequest.Builder()
    .method("GET")
    .path("tesla/charge/ammeter")
    .build();
  VehicleResponse amperage = vehicle.request(request);
  ```

  ```Ruby Ruby theme={null}
  amperage = vehicle.request("GET", "tesla/charge/ammeter")
  ```
</CodeGroup>

## March 7, 2022

Smartcar is now compatible with MINI vehicles in Canada, the United States, and our supported European countries.

## April 13, 2022

Smartcar's webhooks now have beta support for sending events in response to events that are generated by the vehicle itself. The initial release supports the following events on Ford, Tesla, and Toyota vehicles in Canada, the United States, and our supported European countries:

* `CHARGING_STARTED`
* `CHARGING_STOPPED`
* `CHARGING_COMPLETED`
  Webhook events sent in response to vehicle events can be distinguished from schedule events based on the `eventName` property of the POST body. For example, the POST body for event based webhooks will have the following structure:

```json  theme={null}
{
  "version": "2.0",
  "webhookId": "uuid",
  "eventName": "eventBased",
  "mode": "test|live",
  "payload": {
    "eventId": "uuid",
    "vehicleId": "uuid",
    "eventType": "CHARGING_STARTED|CHARGING_STOPPED|CHARGING_COMPLETED",
    "eventTime": "ISO8601 Datetime"
  }
}
```

## May 9, 2022

Smartcar is now compatible with Kia vehicles in our supported European countries.

## May 5, 2022

The API now returns more detailed errors for the following:

`UPSTREAM:RATE_LIMIT` - a request fails due to a vehicle rate limit.
`VEHICLE_STATE:NOT_CHARGING` - a vehicle is not charging (only applies to endpoints that return details about a specific charging session e.g. Charging Completion Time).

## June 29, 2022

Smartcar is now compatible with Peugeot and Opel vehicles in our supported European countries.

## June 22, 2022

The Tire Pressure endpoint is now available for BMW, MINI, and Tesla vehicles in Canada, the United States, and our supported European countries.

## June 15, 2022

The API now returns a more detailed VEHICLE\_STATE error whenever a charge request fails due to charger issues or charging schedules. Click the following link to learn more:

VEHICLE\_STATE:CHARGE\_FAULT

## June 8, 2022

Smartcar is now compatible with Nissan vehicles in our supported European countries.

## July 20, 2022

Smartcar is now compatible with Citroën, DS, and Vauxhall vehicles in our supported European countries.

## July 6, 2022

The following brand-specific endpoints are now available for Tesla vehicles in Canada, the United States, and our supported European countries:

* GET `/tesla/compass`
* GET `/tesla/speedometer`

## August 24, 2022

Smartcar is now compatible with Rivian vehicles in the United States.

## August 3, 2022

Smartcar is now compatible with Škoda vehicles in our supported European countries.
The EV Charging control endpoint is now available for Hyundai vehicles in the United States.
The EV Battery Capacity endpoint is now available in our supported European countries.

## September 22, 2022

The following brand-specific endpoint is now available for Tesla vehicles in Canada, the United States, and our supported European countries:

* `POST /tesla/charge/ammeter`

## November 30, 2022

Smartcar is now compatible with Kia vehicles in Canada and the United States.

## December 29, 2022

The Location endpoint is now available for Volkswagen ID series vehicles in our supported European countries.


# 2023 Releases
Source: https://smartcar.com/docs/changelog/2023



## January 6, 2023

Smartcar API v1.0 has been sunset and is no longer supported. If you are currently using v1.0 for API requests, webhooks, errors, or compatibility, we recommend switching to v2.0 as soon as possible.

## March 16, 2023

The API now returns a new code for the RATE\_LIMIT error type if your application tries to make a request to a vehicle too frequently. Click the following link to learn more:

[RATE\_LIMIT:VEHICLE](https://smartcar.com/docs/errors/v2.0/rate-limit/#vehicle)

## March 14, 2023

Smartcar has revamped the Connect flow UI and backend to improve error handling and optimize user conversion rates. Our updates fall into 3 categories: improving brand selection, expanding login methods, and establishing new error codes specific to Connect. These include:

1. Allowing a user to search for:

a. Brand aliases in Brand Select such as VW for Volkswagen

b. Unavailable brands that we plan to introduce in the future, which will display a message highlighting future compatibility with the chosen brand.

2. Expanding login method coverage to include phone numbers for certain brands. We now allow users to log in using email or phone number for the Connect flow starting with Kia and Mercedes-Benz. Stay tuned to our changelog for more brand updates.
3. Providing clearer errors for the Connect flow:

a. no\_vehicles for when the user does not have any vehicles tied to their account and they click to go back to the application

b. configuration\_error for when exiting Connect back to your app through an error page (see below).

<Frame caption="Error Page">
  <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/march14-2023-error-page.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=ae2372638a269dd28e74f1d126548799" data-og-width="457" width="457" data-og-height="590" height="590" data-path="images/changelog/march14-2023-error-page.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/march14-2023-error-page.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=83d51461fa699a42f6e4f02dff613130 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/march14-2023-error-page.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=b009c9870001e0965c93445a272b056d 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/march14-2023-error-page.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=eeb9f79b5fd21addea1c5684dd11add8 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/march14-2023-error-page.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=ee5a92bc1b84aace59c4cbcd723f6d01 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/march14-2023-error-page.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=626fdc0abc2e350585e4c56077eca495 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/march14-2023-error-page.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=1bde0288d4f9eb5afb9189dd7145c0d3 2500w" />
</Frame>

c. server\_error which is thrown if there is not another Connect error specified.

More documentation on error handling can be found [here](https://smartcar.com/docs/integration-guide/test-your-integration/test-errors/#1-connect-errors).

## March 6, 2023

The disconnect endpoint now supports the use of management API token (MAT) for authorization purposes. Documentation can be found [here](https://smartcar.com/docs/api#delete-disconnect)

## May 10, 2023

Smartcar is now compatible with Infiniti vehicles in the United States.

## June 7, 2023

Smartcar is now compatible with Hyundai vehicles in Canada.

## June 5, 2023

Test mode supports the following email format with any password to generate an account with multiple vehicles:

`<number>-vehicles@smartcar.com`

## July 26, 2023

The following brand-specific endpoints are now available for Tesla vehicles in Canada, the United States, and our supported European countries:

* GET `/tesla/charge/records`
* GET `/tesla/charge/records/billing`

## July 19, 2023

Smartcar is now compatible with Mercedes-Benz vehicles in our supported European countries.

## July 12, 2023

The following brand-specific endpoints are now available for Tesla vehicles in Canada, the United States, and our supported European countries:

* GET `/tesla/charge/schedule`
* POST ` /tesla/charge/schedule`
* GET `/tesla/climate/cabin`
* POST ` /tesla/climate/cabin`
* GET `/tesla/climate/defroster`
* POST ` /tesla/climate/defroster`
* GET `/tesla/climate/steering_wheel`
* POST ` /tesla/climate/steering_wheel`

## August 22, 2023

The following brand-specific endpoints are now available for Nissan vehicles in the United States:

* GET /nissan/charge/schedule
* PUT /nissan/charge/schedule

## August 17, 2023

The following endpoints are now available to manage vehicle connections:

* GET Vehicle Connections
* DELETE Vehicle Connections

## August 9, 2023

<img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/charge_schedule.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=84fe1287c6901131cc9b5be2369fab44" data-og-width="3200" width="3200" data-og-height="1800" height="1800" data-path="images/changelog/charge_schedule.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/charge_schedule.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=db24065792681b059578b879a6ce5475 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/charge_schedule.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=fc0f3debdb57efc07871c4e0a83bc00a 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/charge_schedule.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=9b64889d60f65e0571660f1a5383878e 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/charge_schedule.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=3bcefd1fabb57ab00a9016ae8c9c9223 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/charge_schedule.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=fa88255cae6d302decbc46d5fdd19688 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/charge_schedule.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=916f3a628b5fb7169bd5dd48a015b507 2500w" />

The following brand-specific endpoints are now available for Ford and Lincoln vehicles in Canada, the United States, and our supported European countries:

* GET ford/charge/schedule\_by\_location
* PUT ford/charge/schedule\_by\_location
* GET lincoln/charge/schedule\_by\_location
* PUT lincoln/charge/schedule\_by\_location

## September 21, 2023

Introducing Vehicle Management! With this initial release you're able to see and manage
vehicles connected to your applications from within the [Smartcar Dashboard](https://dashboard.smartcar.com/login).

<Frame type="simple">
  <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/vehicleMgmtDashboard.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=9af2e0a52603a89815ca66762c172a29" data-og-width="2880" width="2880" data-og-height="1590" height="1590" data-path="images/changelog/vehicleMgmtDashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/vehicleMgmtDashboard.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=0a4f5306ac471006a3c8acd13d8d8ae4 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/vehicleMgmtDashboard.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=bfd42655ed067a7d6c1ebad25a15ec5b 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/vehicleMgmtDashboard.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=aefd65730da65fac88542cbb2cdb3afa 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/vehicleMgmtDashboard.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=d670ee8d20bc843fa501b1e33d4cd46a 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/vehicleMgmtDashboard.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=e880098c3dac9893f7760030a0d1949f 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/vehicleMgmtDashboard.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=b02e357b72e685c8ab80b064a3d32574 2500w" />
</Frame>

<br />

<br />

<sub>
  <sup>
    Logos and brand names are for identification purposes only and do not
    indicate endorsement of or affiliation with Smartcar.
  </sup>
</sub>

## September 19, 2023

[Charge Records](/api-reference/bmw/get-charge-records) is now available as a make specific endpoint for BMW and MINI in Canada, the United States, and our supported European countries.

## September 06, 2023

<img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/lock_status.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=e1db9270f152efe9c9401f6345919fca" data-og-width="3200" width="3200" data-og-height="1800" height="1800" data-path="images/changelog/lock_status.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/lock_status.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=94f90977ffab5f5d744613336b548b5f 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/lock_status.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=5a5c37a05bedbc700a86537f5b8ab604 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/lock_status.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=ca739afdc85621318780e1ed55628487 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/lock_status.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=0282c82752a1a70d026683b23346f742 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/lock_status.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=12ce5a902cf98ece664c9a54f0dc80c0 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/lock_status.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=8a5e789d425ad00eb10922777e9fe36d 2500w" />

Lock Status is now available as a Core endpoint and supported by the following makes:

* Tesla (Global)
* Ford (Global)
* Kia (Global)
* Jaguar (Global)
* Land Rover (Global)
* BMW (Global)
* MINI (Global)
* Lincoln (US)
* Toyota (US)
* Lexus (US)

In addition to the lock status of the vehicle, Smartcar will also return the open status of doors, sunroof, windows, based on what the vehicle supports.

## October 19, 2023

<Frame type="simple">
  <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/charge_limit_bmw_mini.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=cfb931328327300571d2dd064d833813" data-og-width="2400" width="2400" data-og-height="1255" height="1255" data-path="images/changelog/charge_limit_bmw_mini.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/charge_limit_bmw_mini.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=1d9ebfa2358c9e1b81beadf5caae7d41 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/charge_limit_bmw_mini.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=0e4c96b811a31137183d507a6b3fbbef 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/charge_limit_bmw_mini.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=c80539aa79b733cba4787a6a2ebe0afa 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/charge_limit_bmw_mini.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=4e259b64c8c3a9132831d4aece06a4f0 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/charge_limit_bmw_mini.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=32c9c7bf05d1a47e29aa7c564167131a 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/charge_limit_bmw_mini.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=ca84cdb684b804986c448e20f03f6f2b 2500w" />
</Frame>

BMW and MINI EVs are now compatible with the following endpoints globally:

* [Get Charge Limit](/api-reference/evs/get-charge-limit)
* [Set Charge Limit](/api-reference/evs/set-charge-limit)

## October 5, 2023

<Frame type="simple">
  <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/hyundai_eu.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=5a9d595bbc4eaaeff8d6e2733f98e0a9" data-og-width="3200" width="3200" data-og-height="1800" height="1800" data-path="images/changelog/hyundai_eu.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/hyundai_eu.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=17ed7688f6b5fced05389e7e8f2c6a76 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/hyundai_eu.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=33089cb00b419552da9b17722da36dca 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/hyundai_eu.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=f4160b04b74a2458414afa61d2a4d9cc 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/hyundai_eu.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=b548db74cdaa631ea6aed4e15f9ac123 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/hyundai_eu.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=67eaf023ac227bb424de3735c03bd3a4 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/hyundai_eu.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=bec7471818e296717b95d8846e99bc8b 2500w" />
</Frame>

Smartcar is now compatible with Hyundai in supported European countries.

## October 3, 2023

<Frame type="simple">
  <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/mazda_porsche_eu.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=22f330b90eaa9977895c8eae44298b65" data-og-width="2400" width="2400" data-og-height="1255" height="1255" data-path="images/changelog/mazda_porsche_eu.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/mazda_porsche_eu.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=e6801f1bef849d125388ec3fb8858436 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/mazda_porsche_eu.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=91f52ac8aaaad1907d79069658304293 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/mazda_porsche_eu.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=9c412cc84faa03ea488420c11f23a586 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/mazda_porsche_eu.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=e8a37b2fb0b7735a997ee11c68c01149 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/mazda_porsche_eu.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=79602a6b576766121d219c3787d972d9 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/mazda_porsche_eu.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=cd6a9044ccd528599534f6d8bd37bead 2500w" />
</Frame>

Smartcar is now compatible with Mazda and Porsche in supported European countries.

## November 15, 2023

<Frame type="simple">
  <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/cupra_eu.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=7c96b0fbea7a2310f07099d158b00ca7" data-og-width="2932" width="2932" data-og-height="1572" height="1572" data-path="images/changelog/cupra_eu.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/cupra_eu.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=7678b5586145211bdbc7f4c07e1c33d4 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/cupra_eu.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=707a1cd95c85447a51146bb173edfc99 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/cupra_eu.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=28d2d3fd9b897d5cc22047c87f5a3672 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/cupra_eu.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=93236c72c5a26e4f61d62ef9b35a08f0 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/cupra_eu.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=4c65f0120cd8d7d2cdecf3f6e95d6fba 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/cupra_eu.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=203cd9fd852ac6f6d7d7ce56e966733a 2500w" />
</Frame>

Smartcar is now compatible with CUPRA in supported European countries.


# 2024 Releases
Source: https://smartcar.com/docs/changelog/2024



<Update label="December 20, 2024">
  ## Fetched At Header

  A new [SC-Feched-At](https://smartcar.com/docs/api-reference/headers) header is now available. This new header highlights when Smartcar fetched the returned data from an OEM whereas `sc-data-age` indicates when the returned data was recorded by the vehicle.
</Update>

<Update label="December 20, 2024">
  ## Connect Playground

  <Frame type="simple">
    <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/connect-playground.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=1f9592758b704c3ce99badf046a43700" data-og-width="3318" width="3318" data-og-height="2086" height="2086" data-path="images/changelog/connect-playground.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/connect-playground.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=3143ae2cab977bd90f7034b0a5ee4b13 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/connect-playground.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=03390e8f93bdab3f73fe3254d2a5d51f 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/connect-playground.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=34debb120b7f94083517d8c10275b011 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/connect-playground.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=bc0ee77976e46eee3a531700023ca9c3 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/connect-playground.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=620c13bcabef1a421e4eafdcdb0fb983 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/connect-playground.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=c3be25a0e958aaec89f75807ec1c3cee 2500w" />
  </Frame>

  The [Connect Playground](https://smartcar.com/docs/getting-started/dashboard/playground) is available, making it easier than ever to create your Connect URL and start requesting vehicle consent.
</Update>

<Update label="December 18, 2024">
  ## Diagnostic Webhook

  A new [Diagnostic Webhook](https://smartcar.com/docs/getting-started/tutorials/webhooks-diagnostic) is available in beta. This webhook delivers either [Diagnostic Trouble Code](https://smartcar.com/docs/api-reference/get-dtcs) events or [System Status](https://smartcar.com/docs/api-reference/get-system-status) changes.
</Update>

<Update label="December 3, 2024">
  ## Diagnostic Trouble Codes

  A new [Diagnostic Trouble Code](https://smartcar.com/docs/api-reference/get-dtcs) endpoint is available in beta. This endpoint returns a list of active Diagnostic Trouble Codes (DTCs) and the timestamp they last became active.
</Update>

<Update label="November 5, 2024">
  ## Ford authentication update

  Ford's authentication process has been updated to require the use of SDKs. Our [Connect SDKs](https://smartcar.com/docs/connect/connect-sdks) have been updated to redirect to Ford's site to handle the authentication process when the user logs in.
</Update>

<Update label="November 1, 2024">
  ## System Status endpoint now in Beta

  A new [System Status](https://smartcar.com/docs/api-reference/get-system-status) endpoint is available in beta. This endpoint returns a list of vehicle components and their health state for FCA and GM makes.
</Update>

<Update label="October 10, 2024">
  ## Webhooks subscription status

  The Smartcar Dashboard now indicates which webhooks a vehicle is  subscribed to. From the Vehicles table, click into the three dot menu to view vehicle details. From here, navigate to the new Webhooks tab!
</Update>

<Update label="September 25, 2024">
  ## Dynamic Webhooks now in Beta

  [Dynamic Webhooks](/getting-started/tutorials/webhooks-dynamic) are now in beta for Enterprise customers! Please request access from the Webhooks tab on the Smartcar Dashboard!
</Update>

<Update label="September 30, 2024">
  ## Multi-Factor Authentication in Dashboard

  [Multi-Factor Authentication](/getting-started/dashboard/dashboard-mfa) is available to offer an additional layer of security for the Smartcar Dashboard.
</Update>

<Update label="August 19, 2024">
  ## Support for MG in Europe

  Support for the following endpoints are now available for the MG brand in Europe:

  * [VIN](/api-reference/get-vin)
  * [Odometer](/api-reference/get-odometer)
  * [Lock Status](/api-reference/get-lock-status)
  * [Lock/Unlock](/api-reference/control-lock-unlock)
  * [Tire Pressure](/api-reference/get-tire-pressure)
  * [GET Charge Limit](/api-reference/evs/get-charge-limit)
  * [POST Charge Limit](/api-reference/evs/set-charge-limit)
  * [Battery Level](/api-reference/evs/get-battery-level)
  * [Battery Capacity](/api-reference/evs/get-battery-capacity)
</Update>

<Update label="August 9, 2024">
  ## Support for Honda, Subaru, Acura, and more!

  Smartcar is now compatible with the **Honda Prologue**, **Subaru Solterra** and the **Acura ZDX** in supported regions.

  ### Additional Releases

  The following brands now support [Control Charge](/api-reference/evs/control-charge), [Battery Level](/api-reference/evs/get-battery-level), [Battery Capacity](/api-reference/evs/get-battery-capacity) and [Charge Status](/api-reference/evs/get-charge-status):

  * Jeep, Fiat and Alfa Romeo (US, Canada and Europe)
  * Chevrolet, Cadillac and GMC (US and Canada)
  * RAM and Dodge (US and Canada)
  * Porsche (US and Europe)
  * Mazda (US and Europe)
  * Renault (Europe)
  * Nissan (Europe)
</Update>

<Update label="August 6, 2024">
  ## Smartcar is now compatible with Dacia in Europe.

  Support for the following endpoints are now available for the MG brand in Europe:

  * [Vehicle Info](/api-reference/get-vehicle-info)
  * [Location](/api-reference/get-location)
  * [Control Charge](/api-reference/evs/control-charge)
  * [State of Charge](/api-reference/evs/get-battery-level)
  * [Charging Status](/api-reference/evs/get-charge-status)
</Update>

<Update label="July 31, 2024">
  ## Connect Insights is now available!

  <Frame type="simple">
    <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/connect-insights.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=1065079feb7f9f26d3f9ed9717a4d7a4" data-og-width="1896" width="1896" data-og-height="1075" height="1075" data-path="images/changelog/connect-insights.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/connect-insights.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=e2552e78e18415d6df5ba41698f50f5f 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/connect-insights.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=559ed4eb67ed2bbba45b2315750fd1e4 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/connect-insights.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=900aa1f85e0fe92baad1e593cb2bca21 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/connect-insights.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=659e2add70ffcec5a3b7818c20394012 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/connect-insights.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=cc9b62e94097e80dedbb8965ceb2406c 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/connect-insights.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=df300b0e7a4a0e57007ae80ea66c31f5 2500w" />
  </Frame>

  * Each Connect flow launched for the previous two weeks is available in the Smartcar Dashboard with a variety of ways to search for specific Connect launches.
  * Enterprise customers have access to funnel analysis so they can understand their conversion rates in the Connect flow.
</Update>

<Update label="July 30, 2024">
  ## Test & Simulated modes are now one

  Test and Simulated mode have been combined into a singular mode; Simulated.

  If a simulated vehicle is enabled, we will return data following the selected trip. If the simulated vehicle doesn't support the requested endpoint, randomized data will be returned.

  If no simulated vehicle is enabled for, we will return data as if a simulated vehicle with "Day Commute" was selected. If the simuday commute doesn't support the requested endpoint, randomized data will be returned.
</Update>

<Update label="July 25, 2024">
  ## Support for Google authentication in Dashboard

  The Smartcar Dashboard now supports Google authentication.
</Update>

<Update label="July 3, 2024">
  ## User information for Tesla

  The following endpoints are now available for Tesla:

  * [Get User Info](/api-reference/tesla/get-user-info)
  * [Get User access](/api-reference/tesla/get-user-access)
</Update>

<Update label="June 24, 2024">
  ## Customize brands in Connect

  <Frame type="simple">
    <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/dynamic-brand-filtering.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=cf5f22e5466c95420867714705607c20" data-og-width="2932" width="2932" data-og-height="1572" height="1572" data-path="images/changelog/dynamic-brand-filtering.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/dynamic-brand-filtering.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=5a0154892639d64cb73638ec73fe4db1 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/dynamic-brand-filtering.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=7f86b7a190e9be12b6f9162473d4134a 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/dynamic-brand-filtering.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=b169a91a7d658ac36d346b8080757722 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/dynamic-brand-filtering.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=33814872babfa92b4b0cd7f70f86274f 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/dynamic-brand-filtering.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=6cb51ce5137c25b00c1de9bbcb7d20cb 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/dynamic-brand-filtering.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=5f05873c3feaf100aa0a8d1ab7c156ed 2500w" />
  </Frame>

  You can now customize which bands show up in Connect from the [Dashboard](https://dashboard.smartcar.com/). Easily manage which brands your users can connect to based on engine type or endpoint.
</Update>

<Update label="June 20, 2024">
  ## Get charge endpoint for Audi

  The following Brand Specific Endpoint is now available for Audi:

  * [Get Charge Status](/api-reference/audi/get-charge)
</Update>

<Update label="June 5, 2024">
  ## Additional endpoints for Audi

  The following endpoints are now available for Audi:

  * [Get Charge Limit](/api-reference/evs/get-charge-limit)
  * [Set Charge Limit](/api-reference/evs/set-charge-limit)
  * [Control Charge](/api-reference/evs/control-charge)
  * [Lock Status](/api-reference/get-lock-status)
</Update>

<Update label="May 10, 2024">
  ## Service history

  The following endpoint is now available for Ford, Lincoln, Toyota, Lexus, Mazda and Volkswagen (US) vehicles:

  * [GET /service/history](/api-reference/get-service-records)
</Update>

<Update label="May 8, 2024">
  ## Tesla alerts

  The following make specific endpoint is now available for Tesla across all supported regions:

  * [GET /tesla/alerts](/api-reference/tesla/get-alerts)
</Update>

<Update label="April 25, 2024">
  ## Tesla charge battery and suggested user messages

  <Frame type="simple">
    <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/tesla-charge-battery.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=8dfa7704a994b4904d59ca788ad3c66c" data-og-width="2932" width="2932" data-og-height="1572" height="1572" data-path="images/changelog/tesla-charge-battery.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/tesla-charge-battery.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=d7c8e7007afcbb9aebe34e1e50051670 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/tesla-charge-battery.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=3f7a4d79f887e47f2bf9fc2c304b0aad 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/tesla-charge-battery.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=9120f80df46b039c299cf088e322da62 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/tesla-charge-battery.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=d9347caf589812805b1030f88b0769d9 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/tesla-charge-battery.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=03dc40f51e98b1e55e3a47aec88180df 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/tesla-charge-battery.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=f7c5a1a39d9477922ee20a82405b30fb 2500w" />
  </Frame>

  The following make specific endpoints are now available for Tesla across all supported regions:

  * [GET /tesla/charge](/api-reference/tesla/get-charge)
  * [GET /tesla/battery](/api-reference/tesla/get-battery)

  ### Additional Releases

  Suggested user messages are now included as part of API error responses for you to easily surface resolution steps to vehicle owners. See our [error documentation](/api-reference/api-errors) for more details.
</Update>

<Update label="April 9, 2024">
  ## Country management for Smartcar Connect

  <Frame type="simple">
    <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/country-management.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=11757f1b4cc5145df6c08af7b0a21c67" data-og-width="2932" width="2932" data-og-height="1572" height="1572" data-path="images/changelog/country-management.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/country-management.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=2df99c5b631a2d61065b8f976e041759 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/country-management.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=d7b5ed24ce0762197f37b8c89ad1ffce 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/country-management.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=e64c23acbe09fa40cb184a4fbbaccae4 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/country-management.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=bf457fba200fc21eaf6b6c7ce21d7f00 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/country-management.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=d163c4ce0d88dec820ccadf17352e027 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/country-management.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=049fead1c0930daa984c4e09e3a97d76 2500w" />
  </Frame>

  Country Management is now available for Connect! Easily manage what countries are enabled for your application on Dashboard.

  ### Additional Releases

  The `user` parameter is now available when [building the Connect URL](/connect/redirect-to-connect) to pass a unique identifier for a vehicle owner to track and aggregate analytics across their Connect sessions for your application.
</Update>

<Update label="March 6, 2024">
  ## Organization access for teams

  <Frame type="simple">
    <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/moo.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=71e3545126a0bf4bdaa9f7f1a4b80d02" data-og-width="2932" width="2932" data-og-height="1572" height="1572" data-path="images/changelog/moo.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/moo.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=a14a5206517af13a66101ac86680efe4 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/moo.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=1188be412d1bda8217b043e14e27490b 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/moo.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=1f99c2344af296c4f37903fc4d2b970a 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/moo.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=b1ccd7f90a5a0ad8cc476929d1aed5ed 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/moo.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=f7bb757ebca96ab9ff7de5c6d1bef3d9 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/moo.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=2e45877f32ebcb819ba45cc41ef78966 2500w" />
  </Frame>

  Organization access for Teams is now available on Dashboard. Check out our docs page on [Teams](/getting-started/dashboard/teams) for details.

  ### Additional Releases

  The following endpoint is now available for Tesla vehicles globally:

  * [Virtual Key Status](/api-reference/tesla/get-virtual-key-status)
</Update>

<Update label="February 14, 2024">
  ## Subaru US

  <Frame type="simple">
    <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/subaru-us.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=d9f922b4ca6cbe05ac27249f373c5742" data-og-width="3200" width="3200" data-og-height="1800" height="1800" data-path="images/changelog/subaru-us.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/subaru-us.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=28a5d4b52742c8df1635bd4dee8fecaf 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/subaru-us.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=0368c8cf42aaff6a479fe7cf8e6a7b7c 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/subaru-us.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=fcd496da399e39766e8757ae2e12ab5b 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/subaru-us.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=c795382d489288b2ef6c430b0ca196b0 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/subaru-us.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=b0d3df43fbdbed181c269abbd784920d 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/subaru-us.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=e94b4bffc0bf91a88530f283e1173370 2500w" />
  </Frame>

  Smartcar is now compatible with Subaru in the US.

  ### Additional Releases

  The following endpoints are now available for Tesla vehicles globally:

  * [Control Charge Port](/api-reference/tesla/control-charge-port)
  * [Control Frunk](/api-reference/tesla/control-frunk)
  * [Control Trunk](/api-reference/tesla/control-trunk)
</Update>

<Update label="February 8, 2024">
  ## Fuel endpoint for European brands

  <Frame type="simple">
    <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/eu-fuel.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=42a58cd7e3dfccd0d8b8e3ff57166d47" data-og-width="3200" width="3200" data-og-height="1801" height="1801" data-path="images/changelog/eu-fuel.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/eu-fuel.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=c5779195ef6da9a3a815bd904c31dfc7 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/eu-fuel.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=0e3f875e935f95ee630d9139ed9eb9e0 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/eu-fuel.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=7fe12c3a63dd7428b5325262cbedbac2 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/eu-fuel.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=7197eb5a8a6f6e55b98fb734668f6312 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/eu-fuel.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=8032ac715ac27deb8f3c40cb5dcce8c7 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/eu-fuel.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=9d571258929645b870951f826d2070ce 2500w" />
  </Frame>

  The [GET /fuel](/api-reference/get-fuel-tank) endpoint is now available for the following brands in supported European countries:

  | <div style={{ width:150 }} /> | <div style={{ width:150 }} /> | <div style={{ width:150 }} /> | <div style={{ width:150 }} /> |
  | ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
  | Audi                          | Hyundai                       | Mercedes-Benz                 | Skoda                         |
  | BMW                           | Jaguar                        | MINI                          | Vauxhall                      |
  | Citroen                       | Kia                           | Opel                          | Volkswagen                    |
  | DS                            | Land Rover                    | Peugeot                       | Volvo                         |
  | Ford                          | Mazda                         | Renault                       |                               |
</Update>


# Latest Releases
Source: https://smartcar.com/docs/changelog/latest

Learn about Smartcar's latest product updates and improvements

[Subscribe to changelog updates](https://sta26.share.hsforms.com/2CCbdweFdSOeE5B58UvjVlw) and receive email notifications for new releases and updates.

<Update label="November 19th, 2025">
  ## Improved Webhook Logs in Dashboard

  We've significantly improved the webhook logging experience in the Smartcar Dashboard, making it easier to monitor and debug webhook deliveries.

  **What's New:**

  * **Delivery-focused logging**: Each log row now represents a single webhook delivery, providing a clearer view of your webhook activity
  * **Detailed inspection**: Click "View logs" on any delivery to inspect the signal or endpoint items included in that delivery and their individual statuses
  * **Faster performance**: Reduced latency in both Webhook Logs and the webhook deliveries over time chart for a more responsive experience

  **Where to Find It:**
  You can view your webhook logs in two locations:

  * **Logs > Webhooks** in the main navigation
  * **Vehicles > \[Selected vehicle] > Webhooks** for vehicle-specific logs

  **Get started**: Head to the [Smartcar Dashboard](https://dashboard.smartcar.com/logs?tab=webhooks) to explore the improved webhook logs.
</Update>

<Update label="November 18th, 2025">
  ## Python SDK and Node SDK Updated to Support Version 3 of the Vehicles API

  The [Python SDK](https://github.com/smartcar/python-sdk) and [Node SDK](https://github.com/smartcar/node-sdk) have been updated to support [Version 3 of the Vehicles API](/api-reference/vehicles-api-intro).

  Both SDKs now include three new methods:

  * `get_vehicle` - Retrieve vehicle information
  * `get_signal` - Get a specific signal for a vehicle
  * `get_signals` - Get all available signals for a vehicle

  These new methods provide easier access to vehicle data through the latest API version, enabling developers to work with Smartcar's expanded signal catalog and improved data delivery capabilities.

  **Get started**: Update to the latest SDK version and explore the new methods in the [Python SDK](https://github.com/smartcar/python-sdk) and [Node SDK](https://github.com/smartcar/node-sdk) documentation.
</Update>

<Update label="November 12th, 2025">
  ## Polestar and BYD are now available on Smartcar!

  <Frame>
        <img src="https://mintcdn.com/smartcar-docs/emzQHG3wvjtubP6o/images/changelog/byd-polestar-hero.png?fit=max&auto=format&n=emzQHG3wvjtubP6o&q=85&s=e5ef2ea3f67b7dc0a692aa7fbf5c2be3" alt="" data-og-width="4000" width="4000" data-og-height="2400" height="2400" data-path="images/changelog/byd-polestar-hero.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/emzQHG3wvjtubP6o/images/changelog/byd-polestar-hero.png?w=280&fit=max&auto=format&n=emzQHG3wvjtubP6o&q=85&s=d5525d01ad95038c2704d81263df8570 280w, https://mintcdn.com/smartcar-docs/emzQHG3wvjtubP6o/images/changelog/byd-polestar-hero.png?w=560&fit=max&auto=format&n=emzQHG3wvjtubP6o&q=85&s=dbe61497a58c32af80e52d4242a4c281 560w, https://mintcdn.com/smartcar-docs/emzQHG3wvjtubP6o/images/changelog/byd-polestar-hero.png?w=840&fit=max&auto=format&n=emzQHG3wvjtubP6o&q=85&s=e8f5aa463531ed1decef7f3acc947a1f 840w, https://mintcdn.com/smartcar-docs/emzQHG3wvjtubP6o/images/changelog/byd-polestar-hero.png?w=1100&fit=max&auto=format&n=emzQHG3wvjtubP6o&q=85&s=008cf97c1eb1a226a57f11774d800fde 1100w, https://mintcdn.com/smartcar-docs/emzQHG3wvjtubP6o/images/changelog/byd-polestar-hero.png?w=1650&fit=max&auto=format&n=emzQHG3wvjtubP6o&q=85&s=3b333c105d53f52ec5640bb2b0896bf2 1650w, https://mintcdn.com/smartcar-docs/emzQHG3wvjtubP6o/images/changelog/byd-polestar-hero.png?w=2500&fit=max&auto=format&n=emzQHG3wvjtubP6o&q=85&s=dc62215046c3ede7ecda74c217cbcdbf 2500w" />
  </Frame>

  We're excited to bring compatibility for Polestar and BYD, expanding the number of brands on the platform to 45!

  To enroll vehicles from these brands, make sure you have them enabled for your application in the [Dashboard](https://dashboard.smartcar.com/configuration?tab=oem-brands).

  Once enabled, you can direct vehicle owners to connect their Polestar and BYD vehicles through the Smartcar Connect flow.

  For a list of data points supported for these brands, see the [compatibility matrix](https://smartcar.com/product/compatible-vehicles).

  See important note about [BYD's login requirement](/help/brand-quirks#byd).
</Update>

<Update label="November 12th, 2025">
  ## Upcoming Change to Webhook Payload Structure

  Webhook `VEHICLE_STATE` payloads are being updated to include a `status` value for all signals. Previously, a `status` value was only passed for signals with errors.

  Example Payload:

  ```json  theme={null}
  {
    "code": "location-preciselocation",
    "name": "PreciseLocation",
    "group": "Location",
    "body": {
      "latitude": 37.386051,
      "longitude": -122.083855
    },
    "status": {
      "value": "SUCCESS"
    }
  },
  ```

  This change will go live on November 17, 2025, at 11:00AM Pacific Time. Please ensure your webhook receiver is prepared to handle deliveries in this format.
</Update>

<Update label="November 12th, 2025">
  ## Extended Expiration Times for Vehicle Refresh Tokens

  Starting November 12, 2025, Vehicle Refresh Tokens will expire 10 minutes after they are used to generate a new token set. This is an extension from the previous expiration time of 1 minute.

  For more information about access tokens, see [Refreshing Access Tokens](/api-reference/authorization/refreshing-access-token)
</Update>

<Update label="November 10th, 2025">
  ## Verifying webhooks just got a lot easier!

  <Frame>
        <img src="https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge.png?fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=9106c3a746b703281d6fc2ada9bd6249" alt="" data-og-width="1344" width="1344" data-og-height="1095" height="1095" data-path="images/changelog/webhook-challenge.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge.png?w=280&fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=2af7016d356c723b2c5f2abf8f55e130 280w, https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge.png?w=560&fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=c402b715adfe634727c3db3777518002 560w, https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge.png?w=840&fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=663b8794492a757bc94bb456642ba025 840w, https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge.png?w=1100&fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=c94a590072ee00fe31f2381424ab4866 1100w, https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge.png?w=1650&fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=c36a0f87b244b4a1915d30d9440724c0 1650w, https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge.png?w=2500&fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=f4870c0fed07dab78526f68c81bd989a 2500w" />
  </Frame>

  When you verify a webhook, you’ll see a guided modal with a sample challenge string, copy-ready SDK snippets (Python, Node, Java, Ruby), and inline instructions for hashing the `application_management_token` plus challenge.

  When your server responds with your webhook verification, you'll see the response that Smartcar received compared to the expected hash output.

  <Frame>
        <img src="https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge-calculator.png?fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=12cd5091ce9d0c9f0355569227931374" alt="" data-og-width="1344" width="1344" data-og-height="1095" height="1095" data-path="images/changelog/webhook-challenge-calculator.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge-calculator.png?w=280&fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=01c41a08770277ac722cf56d2207755d 280w, https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge-calculator.png?w=560&fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=eb0f7b5c79d5f1d5001cf2b4e0c1fc94 560w, https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge-calculator.png?w=840&fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=e6a0dedfdd279d20479326bcd0f855e2 840w, https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge-calculator.png?w=1100&fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=a8fe313d141c595525270f50f960da76 1100w, https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge-calculator.png?w=1650&fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=b671a190797c06c85e5fea49b0dab359 1650w, https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge-calculator.png?w=2500&fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=bc0b603ce9b29e082e1c5372681297e3 2500w" />
  </Frame>

  If the verification fails, the new response tab surfaces the HTTP status, challenge string, expected hash output, and the payload Smartcar received so you can immediately compare and retry. This feedback loop removes trial-and-error, shortens onboarding for new teams, and ensures your webhook endpoint is producing the correct `SC-Signature` before you start ingesting production signals.

  **Get started**

  * Head to the [Smartcar Dashboard](https://dashboard.smartcar.com/integrations) and select your webhook integration to launch the verifier.
  * Follow the updated [Payload verification guide](/integrations/webhooks/payload-verification) to reproduce the same HMAC calculation server-side.
  * After verification succeeds, wire up your [webhook receiver tutorial](/getting-started/tutorials/webhook-receiver-recipe) or call the [webhook overview](/integrations/webhooks/overview) docs for deployment best practices.
</Update>

<Update label="November 5th, 2025">
  ## TypeScript Webhook Recipe Now Available

  <Frame>
        <img src="https://mintcdn.com/smartcar-docs/iqgpvOkAmDxDHjKR/images/changelog/webhook-recipe.png?fit=max&auto=format&n=iqgpvOkAmDxDHjKR&q=85&s=f79b6068e67c4abf926be8364ba2c927" alt="" data-og-width="1084" width="1084" data-og-height="478" height="478" data-path="images/changelog/webhook-recipe.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/iqgpvOkAmDxDHjKR/images/changelog/webhook-recipe.png?w=280&fit=max&auto=format&n=iqgpvOkAmDxDHjKR&q=85&s=e7a2254c470e0b0c0ad02bb633e7a46a 280w, https://mintcdn.com/smartcar-docs/iqgpvOkAmDxDHjKR/images/changelog/webhook-recipe.png?w=560&fit=max&auto=format&n=iqgpvOkAmDxDHjKR&q=85&s=f69339b3afb0046da2cfc90373c0c4dc 560w, https://mintcdn.com/smartcar-docs/iqgpvOkAmDxDHjKR/images/changelog/webhook-recipe.png?w=840&fit=max&auto=format&n=iqgpvOkAmDxDHjKR&q=85&s=36992d7750724602a81a7ef810e01749 840w, https://mintcdn.com/smartcar-docs/iqgpvOkAmDxDHjKR/images/changelog/webhook-recipe.png?w=1100&fit=max&auto=format&n=iqgpvOkAmDxDHjKR&q=85&s=e3bf0d348cd7ef1365f650918a3bb25a 1100w, https://mintcdn.com/smartcar-docs/iqgpvOkAmDxDHjKR/images/changelog/webhook-recipe.png?w=1650&fit=max&auto=format&n=iqgpvOkAmDxDHjKR&q=85&s=68708cc3b32099325654da2d395d978a 1650w, https://mintcdn.com/smartcar-docs/iqgpvOkAmDxDHjKR/images/changelog/webhook-recipe.png?w=2500&fit=max&auto=format&n=iqgpvOkAmDxDHjKR&q=85&s=2c572f846670d048baaf62d2b94d0eb2 2500w" />
  </Frame>

  Deploy production-ready webhook receivers in minutes with our new [TypeScript Webhook Recipe](https://github.com/smartcar/typescript-webhook-recipe)! This AWS serverless template provides everything you need to handle Smartcar webhooks at scale:

  * **Complete Infrastructure**: Lambda + API Gateway + SQS with AWS CDK
  * **Built-in Validation**: Automatic webhook verification and payload validation
  * **Error Handling**: Dead letter queues and retry logic for reliability
  * **Production Ready**: CloudWatch monitoring, IAM security, and auto-scaling
  * **Developer Friendly**: TypeScript types and comprehensive documentation

  The recipe eliminates the complexity of building webhook infrastructure from scratch, letting you focus on your business logic. Perfect for new webhook implementations or teams wanting to deploy quickly without infrastructure overhead.

  **Get started**: [Webhook Receiver Recipe Documentation](/getting-started/tutorials/webhook-receiver-recipe) | [GitHub Repository](https://github.com/smartcar/typescript-webhook-recipe)
</Update>

<Update label="September 18th, 2025">
  ## Battery Capacity Selection in the Smartcar Connect Flow

  <Frame style={{ width: '250px', align:'center' }}>
        <img src="https://mintcdn.com/smartcar-docs/JqEHibg7VKARCx7z/images/connect/battery-capacity-selection.png?fit=max&auto=format&n=JqEHibg7VKARCx7z&q=85&s=ae0a84b03f024606bfce72e9c1f4a66b" alt="" data-og-width="388" width="388" data-og-height="842" height="842" data-path="images/connect/battery-capacity-selection.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/JqEHibg7VKARCx7z/images/connect/battery-capacity-selection.png?w=280&fit=max&auto=format&n=JqEHibg7VKARCx7z&q=85&s=0efc0d1d7b90e454505fe7243a4695a9 280w, https://mintcdn.com/smartcar-docs/JqEHibg7VKARCx7z/images/connect/battery-capacity-selection.png?w=560&fit=max&auto=format&n=JqEHibg7VKARCx7z&q=85&s=d8622e19ba50d06c2f9a03b44c426475 560w, https://mintcdn.com/smartcar-docs/JqEHibg7VKARCx7z/images/connect/battery-capacity-selection.png?w=840&fit=max&auto=format&n=JqEHibg7VKARCx7z&q=85&s=1628e58db5cbcb928930c083347fcbc5 840w, https://mintcdn.com/smartcar-docs/JqEHibg7VKARCx7z/images/connect/battery-capacity-selection.png?w=1100&fit=max&auto=format&n=JqEHibg7VKARCx7z&q=85&s=474b6ff769fd376096adcca85a67f05f 1100w, https://mintcdn.com/smartcar-docs/JqEHibg7VKARCx7z/images/connect/battery-capacity-selection.png?w=1650&fit=max&auto=format&n=JqEHibg7VKARCx7z&q=85&s=0940140efeb5fc2101b3119fd83bcb01 1650w, https://mintcdn.com/smartcar-docs/JqEHibg7VKARCx7z/images/connect/battery-capacity-selection.png?w=2500&fit=max&auto=format&n=JqEHibg7VKARCx7z&q=85&s=d246877f0146b9d4241e0280fb33be5d 2500w" />
  </Frame>

  When you request the `read_battery` permission and Smartcar detects multiple possible battery capacity matches for a vehicle, users will now be automatically prompted to select their battery capacity during the Connect flow.

  This streamlined experience eliminates the need for developers to prompt users or source the battery capacity selection from other sources. This step ensures that battery capacity data is available immediately after vehicle connection if Smartcar is not able to identify it.

  Read more about the [User Selected Battery Capacity](/connect/user-selected-batcap).
</Update>

<Update label="September 15th, 2025">
  ## Smartcar Partners with Mercedes-Benz Connectivity Services GmbH!

  <Frame>
        <img src="https://mintcdn.com/smartcar-docs/Bg7Kn_bK3IXZAtXq/images/changelog/mercedes-benz-partnership.png?fit=max&auto=format&n=Bg7Kn_bK3IXZAtXq&q=85&s=2f0a2839bdea0e7a22abb7bdf499d080" alt="" data-og-width="2000" width="2000" data-og-height="1200" height="1200" data-path="images/changelog/mercedes-benz-partnership.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/Bg7Kn_bK3IXZAtXq/images/changelog/mercedes-benz-partnership.png?w=280&fit=max&auto=format&n=Bg7Kn_bK3IXZAtXq&q=85&s=19863b313464c4fc620d30df12c4a9c9 280w, https://mintcdn.com/smartcar-docs/Bg7Kn_bK3IXZAtXq/images/changelog/mercedes-benz-partnership.png?w=560&fit=max&auto=format&n=Bg7Kn_bK3IXZAtXq&q=85&s=8adc584c8118cc3862e4a70e0fdc7d91 560w, https://mintcdn.com/smartcar-docs/Bg7Kn_bK3IXZAtXq/images/changelog/mercedes-benz-partnership.png?w=840&fit=max&auto=format&n=Bg7Kn_bK3IXZAtXq&q=85&s=18ca7624f3954d817a3cd7b51d51a15c 840w, https://mintcdn.com/smartcar-docs/Bg7Kn_bK3IXZAtXq/images/changelog/mercedes-benz-partnership.png?w=1100&fit=max&auto=format&n=Bg7Kn_bK3IXZAtXq&q=85&s=9c4cace159b682759250eafbe4dda527 1100w, https://mintcdn.com/smartcar-docs/Bg7Kn_bK3IXZAtXq/images/changelog/mercedes-benz-partnership.png?w=1650&fit=max&auto=format&n=Bg7Kn_bK3IXZAtXq&q=85&s=e87c7810fbb22b610592ce86c4a8709e 1650w, https://mintcdn.com/smartcar-docs/Bg7Kn_bK3IXZAtXq/images/changelog/mercedes-benz-partnership.png?w=2500&fit=max&auto=format&n=Bg7Kn_bK3IXZAtXq&q=85&s=408823c8d10c25f95d4b0deedd48f7c3 2500w" />
  </Frame>

  We are excited to announce our partnership with Mercedes-Benz Connectivity Services GmbH, expanding seamless access to connected vehicle data for developers and businesses across Europe.

  This integration enables developers to build innovative applications using data from Mercedes-Benz vehicles, including popular models such as the A-Class, C-Class, E-Class, S-Class, GLA, GLC, and more.

  With this partnership, Smartcar customers can leverage secure, reliable, and real-time access to vehicle data for a wide range of use cases, from fleet management to mobility services.

  Read more about this partnership and its impact in our [blog post](https://smartcar.com/blog/smartcar-partners-with-mercedes-benz-connectivity-services-gmbh).
</Update>

<Update label="August 26th, 2025">
  ## Introducing the new Smartcar Platform!

  <Frame>
        <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/data-delivery-announcement.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=22175cab894749206bdc7f3bbd118c56" alt="" data-og-width="2402" width="2402" data-og-height="1184" height="1184" data-path="images/changelog/data-delivery-announcement.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/data-delivery-announcement.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=d6cc8471788593a5626764cc2881cbf4 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/data-delivery-announcement.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=a39af0f2a272dafddd4207bce668ca2f 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/data-delivery-announcement.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=145259f351c51046c8409214ddca69bc 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/data-delivery-announcement.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=84cf82cc8964d47d7809359cf7a7c434 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/data-delivery-announcement.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=90a50fe89f0b8f119233a93dd88ce2e4 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/data-delivery-announcement.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=495ecd701a81e7bd883a2edf05fea531 2500w" />
  </Frame>

  We are excited to announce the launch of the new Smartcar Platform, designed to provide a more reliable and efficient way to access vehicle data. With our new [webhook integration](/integrations/webhooks/overview) and [API](/api-reference/intro), developers can now receive vehicle data at higher frequencies and with improved reliability.

  For all use cases, Smartcar can deliver data as it detects changes based on our new standardized Signal Schema while avoiding unnecessary polling. With over 80 signals available, developers can access a wide range of vehicle data to build innovative applications.

  Getting started with Smartcar is now even easier. [Configure](/getting-started/configure-application) your app, [Connect](/getting-started/connect-vehicles) vehicles, and start receiving data via [webhooks](/integrations/webhooks/overview) in just a few minutes.

  To get started with the new webhooks, check out our [Getting Started guide](/getting-started/introduction) and [Webhook integration overview](/integrations/webhooks/overview).

  These new features are now available to all new customers. Existing customers can reach out to their account manager or contact our support team at [support@smartcar.com](mailto:support@smartcar.com)
</Update>

<Update label="August 6th, 2025">
  ## Smartcar Partners with Ford in Europe!

  <Frame>
        <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/ford-partnership-hero.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=0d8bdcb5a9506b6871a972831f8f2ea9" alt="" data-og-width="4000" width="4000" data-og-height="2400" height="2400" data-path="images/changelog/ford-partnership-hero.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/ford-partnership-hero.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=c95f5ac2fc4be0ae6e976f9ff19b99d9 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/ford-partnership-hero.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=81b7a259276aaa1018ed43c3068ec7d6 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/ford-partnership-hero.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=6fe1ba02a4edb13d5e6d45bfbe8376d6 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/ford-partnership-hero.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=a34b4271c1cbcb43a00857abdd70e9f3 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/ford-partnership-hero.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=93cbb87a39be0a94283a776a836e0e7b 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/ford-partnership-hero.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=b1c4cb8b89e99434d0b80b3474f414e9 2500w" />
  </Frame>

  Smartcar is thrilled to announce our partnership with Ford in Europe, enabling developers to access vehicle data from millions of Ford vehicles across the continent.

  This upcoming integration will give developers seamless access to vehicle data from models including the Mustang Mach‑E®, E‑Transit™, Puma, Fiesta, and Kuga.

  Read more about this exciting partnership in our [blog post](https://smartcar.com/blog/smartcar-partners-with-ford-to-expand-access-to-connected-vehicle-apis?utm_source=docs\&utm_medium=changelog).
</Update>

<Update label="July 9, 2025">
  ## Rivian Commands Now Available!

  <Frame>
        <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/rivian-commands.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=c07a5542bef44eada0f996aa37b5cd71" alt="" data-og-width="2000" width="2000" data-og-height="1200" height="1200" data-path="images/changelog/rivian-commands.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/rivian-commands.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=b7e1528a5bdecde87feec868ef567ffa 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/rivian-commands.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=e874ee657fe65071470b4f5682e9029c 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/rivian-commands.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=332b861fac4a870fd621e4810189b2f6 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/rivian-commands.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=c931d52c272e3d09db38da14b72fd5d7 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/rivian-commands.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=05381fedbebf1706cfe27e567cf2adef 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/rivian-commands.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=3145f275f64ee54ee870e0fff89b6013 2500w" />
  </Frame>

  You can now use the Smartcar API to send commands—such as lock, unlock, and start/stop charge—to Rivian vehicles!

  When requesting command permissions (like `control_security` or `control_charge`), Rivian owners will be prompted to pair their phone with their vehicle. After successful pairing, your application will be able to issue commands to the connected Rivian.

  For step-by-step instructions, see our [Rivian Bluetooth Pairing guide](/connect/other-actions/rivian-bluetooth-pairing).

  > **Note:** Read data permissions (such as `read_location` or `read_charge`) do not require Bluetooth pairing.
  >
  > Smartcar mobile SDKs for iOS and Android are required for Bluetooth pairing.
</Update>

<Update label="June 23, 2025">
  ## Hyundai Lock and Unlock now available!

  <Frame>
        <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/hyundai-lock-unlock.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=365b003efcb521065fb5e8c2bffcc405" alt="" data-og-width="2000" width="2000" data-og-height="1200" height="1200" data-path="images/changelog/hyundai-lock-unlock.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/hyundai-lock-unlock.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=ae688d6acdb297e0f9c8a62e621bbb19 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/hyundai-lock-unlock.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=9811e1c70e06bbcb8cae0494702aa6cc 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/hyundai-lock-unlock.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=643ad4fdbf60a0baacc687701202343d 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/hyundai-lock-unlock.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=b894dc8e9c8b243baf9edabafe3a2f41 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/hyundai-lock-unlock.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=28721498b08fdfc567d952f9b22931d5 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/hyundai-lock-unlock.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=d908456253a214a14d8ba6ecc19db8ff 2500w" />
  </Frame>

  You can now lock and unlock Hyundai vehicles using the same standard Smartcar API. This new feature enables remote control of vehicle doors for supported Hyundai models, making it easier to build secure and convenient experiences for your users.

  For more details on how to use this capability, see our [API reference](/api-reference/control-lock-unlock).

  ## Webhook Logs Now Available in Dashboard

  You can now view logs for your webhooks directly in the Smartcar Dashboard, alongside your API request logs. This update gives you greater visibility into webhook deliveries, making it easier to monitor, debug, and ensure successful integrations.

  To see your webhook logs in action, head over to the [Smartcar Dashboard](https://dashboard.smartcar.com/logs?tab=webhooks).
</Update>

<Update label="June 10, 2025">
  ## New Dashboard Overview Page

  <Frame>
        <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/overview-page.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=fb8a6c0720322cad92144050d38a9e57" alt="" data-og-width="2000" width="2000" data-og-height="1200" height="1200" data-path="images/changelog/overview-page.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/overview-page.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=cae166f5c4c019ddf09ff1d4b07f2f1f 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/overview-page.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=5f9be6c5690e6848193188ba11aaf116 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/overview-page.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=6e3057b0d701384a7c8f1a9f9a0acc34 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/overview-page.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=5758913ff218c5e75f5e4ddc8b6be3ce 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/overview-page.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=1573f58184b866977b041b4732319e60 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/overview-page.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=b73c2dbf3e821e13c28600522548b131 2500w" />
  </Frame>

  Our new Dashboard overview page offers a comprehensive snapshot of your application's performance at a glance. Now, you can quickly visualize:

  * Total vehicle connections
  * New connections in the last 7 days
  * Request trends over time
  * Conversion rates
  * Top five vehicle brands connected to your application

  This update is designed to help you monitor key metrics effortlessly.
</Update>

<Update label="May 20, 2025">
  ## Virtual Keys installation Is Now Supported in Connect

  Smartcar now provides detailed steps for adding and managing Virtual Keys during the connection flow. Virtual Keys are required for third-party applications to issue commands to Tesla vehicles and are the preferred method for accessing data.

  <Frame>
        <img src="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/VirtualKeyPageMobile.png?fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=e504d181b6936f3e0ba17926a2923be2" alt="" data-og-width="2283" width="2283" data-og-height="931" height="931" data-path="images/help-center/oem-integrations/tesla/add-virtual-key/VirtualKeyPageMobile.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/VirtualKeyPageMobile.png?w=280&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=02c5b864bdd1e8c5541ed1a1bfc80549 280w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/VirtualKeyPageMobile.png?w=560&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=a1ca3a12ee41154e396ae4ce1b56af65 560w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/VirtualKeyPageMobile.png?w=840&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=89747ff417caaf5f36b30737aa24bd0a 840w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/VirtualKeyPageMobile.png?w=1100&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=6f5036a32588937a17a0ea6fb0adc4bb 1100w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/VirtualKeyPageMobile.png?w=1650&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=3e4e9358fb3e91fc7e6b1ad8bc7bac0d 1650w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/VirtualKeyPageMobile.png?w=2500&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=b8b9c2e23830523d41d1c9c753d3b309 2500w" />
  </Frame>

  For more details, visit the [Virtual Key documentation](/help/oem-integrations/tesla/virtual-key-tesla).
</Update>

<Update label="May 9, 2025">
  ## atHome signal is now available!

  <Frame>
        <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/athome.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=6fd0f9ec342e5836f7f424b0d84c1551" alt="" data-og-width="1193" width="1193" data-og-height="605" height="605" data-path="images/changelog/athome.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/athome.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=a011b2164337d474b5d280ae97ee291b 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/athome.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=c23ed8efcf27123587ab12e1ce5ac08d 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/athome.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=142571bd4b338cac17e14765929a0cad 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/athome.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=e48de1bbc49d223ed4923582f72371f9 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/athome.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=9d615b05e54d84695fb7f52965ed2788 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/athome.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=2b157e38c55ef34959bd080a5f7198df 2500w" />
  </Frame>

  Smartcar now supports a new vehicle signal `atHome` that returns true or false if a vehicle is at the configured home location. This signal is currently available for Tesla vehicles capable of streaming via [this endpoint](/api-reference/tesla/get-ext-vehicle-info).
</Update>

<Update label="April 21, 2025">
  ## Our New Support Features Are Live!

  <Frame>
        <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/support_center.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=b47b4cecbce18a2f9c9b54f1ed1703e4" alt="" data-og-width="3348" width="3348" data-og-height="1746" height="1746" data-path="images/changelog/support_center.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/support_center.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=09434d78152cf5a4fb5fc8f0544f518a 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/support_center.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=1030ad4e23f917c159899d6dcff3d8a4 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/support_center.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=7b4cc7e8c048371f57c71d267ee22680 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/support_center.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=41df3dd4696763920e8780d3557801f7 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/support_center.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=80d4221ec447492ac02d377f6ee8bcd9 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/support_center.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=0bc42dc428026b00fc53bdf7819ead91 2500w" />
  </Frame>

  We’re excited to share that our new support experience is now available. These updates are designed to make it easier and faster to get the help you need through self-service tools, AI-powered assistance, and improved visibility into your support history.

  **Customer Support Portal** *(Available to paid customers via the Smartcar Dashboard)*

  Your new central hub for all support-related needs:

  * Browse the **Knowledge Base** for helpful articles, guides, and troubleshooting tips
  * Submit new support requests through a user-friendly form
  * View and update **open tickets**, track past communications, and receive timely updates
  * Get help fast with our **AI-powered chat agent**, available 24/7

  **Enhanced Slack Support** *(For eligible plans)*

  Our upgraded Slack support includes:

  * AI-powered answers to common questions directly in your Slack channel
  * Ability to create and track support tickets without leaving Slack
  * One-click access to the Customer Support Portal
  * Real-time updates and faster response workflows

  For more information about what’s included in your current plan, please reach out to your account manager or contact us at [**support@smartcar.com**](mailto:support@smartcar.com).

  For step-by-step instructions on how to use the new features, check out our documentation [here](https://smartcar.com/docs/help/accessing-support-center).
</Update>

<Update label="March 26, 2025">
  ## Support for Single Sign-on (SSO)

  <Frame>
        <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/sso.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=048c472c915140a7f30819b3867f2dc0" alt="" data-og-width="1400" width="1400" data-og-height="1060" height="1060" data-path="images/changelog/sso.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/sso.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=22c8c3065dfae30246b8b7ce849685a9 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/sso.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=b4526a7300ae12b574a813b20ebd1d26 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/sso.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=2b91d146ccb5bbe18bb7cfc31bd43e92 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/sso.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=639e3dfd1732e648b1345fd0dbb186be 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/sso.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=c042b2ae5b902f1af67c3f7cff74d767 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/sso.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=af0ff4a69b4c60aae59f1d010c7375df 2500w" />
  </Frame>

  Single Sign-On (SSO) is now available for teams on an Enterprise plan. To get
  started, reach out to your account manager to have it enabled. For
  implementation details and setup instructions, check out our [SSO
  documentation](/getting-started/dashboard/single-sign-on).
</Update>

<Update label="February 26, 2025">
  ## User Selected Battery Capacity

  <Frame>
        <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/battery-capacity-connect.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=c961d991a12ec7159956c2c019c2c3d3" alt="" data-og-width="1557" width="1557" data-og-height="844" height="844" data-path="images/changelog/battery-capacity-connect.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/battery-capacity-connect.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=e5adb5112b52ea9e44dfec0560a553c0 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/battery-capacity-connect.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=39d36e8ce845e2160e7b4c53f2fc3a8d 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/battery-capacity-connect.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=98e1670947a946171f6317d42ef64395 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/battery-capacity-connect.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=e18cbf7b80707eaaadfc77ae045e96ee 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/battery-capacity-connect.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=abd113f48a42da549583afb78a8cb640 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/battery-capacity-connect.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=548482aa480e985154dbcaef33171082 2500w" />
  </Frame>

  <Frame>
        <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/battery-capacity.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=8c3bb7b334461e7cb0c51541b5f65f14" alt="" data-og-width="1568" width="1568" data-og-height="1209" height="1209" data-path="images/changelog/battery-capacity.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/battery-capacity.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=7c334ae84b82eab6a73957919d7f7d54 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/battery-capacity.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=8b97a7c6bed8fd28ba4ef169345bac29 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/battery-capacity.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=5499cebd357e498dc3ffa1275cddf8d9 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/battery-capacity.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=b95903505b20ef79d8b58326e7e992af 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/battery-capacity.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=8081dbd7c77135f86f12bb622b0c2da1 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/battery-capacity.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=20983c624dcb77f3a2d5d00e8ba06402 2500w" />
  </Frame>

  Developers can now redirect vehicle owners to a Smartcar Connect url where they can select the [battery capacity](/api-reference/get-nominal-capacity) of their vehicle for cases where the battery capacity cannot be accurately determined. This can occur when vehicle owners purchase extension packs, or software upgrades specific to their vehicle. When a user selects an option, Smartcar will return this value with `USER_SELECTED` as the source.
</Update>

<Update label="February 14, 2025">
  ## Diagnostics Webhooks, DTSs, and System Status

  Smartcar now provides Diagnostic Webhooks, DTCs, and System Status vehicle data for an [initial set of brands](https://smartcar.com/product/compatible-vehicles) with more brands added in the future.
</Update>

<Update label="February 6, 2025">
  ## Support for Simplified Chinese

  <Frame>
        <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/simplified-chinese.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=c8d7225d911a5d6582055f33660021b6" alt="" data-og-width="1050" width="1050" data-og-height="1620" height="1620" data-path="images/changelog/simplified-chinese.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/simplified-chinese.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=a8db316e1b5b4548710116205c6c2daf 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/simplified-chinese.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=4cc6ed25b42c4120b3ec8177e4472961 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/simplified-chinese.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=2c16cd2f676e87737aa84219847e30d1 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/simplified-chinese.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=91621b392e156878162b725ffe2db228 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/simplified-chinese.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=a86833cdbd8f53bd6ff079031fe57c1b 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/simplified-chinese.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=5da4895e6c83a1b561563ecd9b68ae9c 2500w" />
  </Frame>

  Vehicle owners can now select Simplified Chinese as they go through the Smartcar Connect flow to connect their cars.
</Update>

<Update label="January 30, 2025">
  ## Tesla Telemetry API

  Smartcar natively supports Tesla's Telemetry API as the default mechanism for retrieving data from Tesla vehicles out of the box and without any configuration from developers. Tesla's Telemetry API is the most efficient and effective way of gathering data from Tesla vehicles. It allows vehicles to stream data directly to Smartcar, eliminating the need to poll Tesla servers. This prevents unnecessary vehicle wakes and battery drain.
</Update>

<Update label="January 10, 2025">
  ## Smartcar MFA

  When a vehicle owner attempts to login to their OEM Connected Services Account and they do not have MFA enabled, Smartcar customers can enable this feature to enforce MFA verification for extra security. If you don't see this option in the Smartcar dashboard, contact [support@smartcar.com](mailto:support@smartcar.com) to get access to this feature.
</Update>

<Update label="January 6, 2025">
  ## New Billing page in Dashboard

  <Frame>
        <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/billing-page.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=a397ed2408731b110969d82626753f8e" alt="" data-og-width="2844" width="2844" data-og-height="2734" height="2734" data-path="images/changelog/billing-page.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/billing-page.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=a28d49467d764e61a30ee3b55d829ca8 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/billing-page.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=4aa6539c0d3a00e7e24e854122c6f97d 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/billing-page.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=fcae21a3d6f8f2b15152ea98081ed751 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/billing-page.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=017dcc3fc88a12b09724d1ca36d4ace5 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/billing-page.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=53a863969b8390b2072e5df30d4e922b 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/changelog/billing-page.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=df3f822c49f8021f089f19bd48a78ade 2500w" />
  </Frame>

  This new page provides more visibility and the ability to update your billing information, view past invoices, and view your plan features and available upgrade options.
</Update>


# Country Selection
Source: https://smartcar.com/docs/connect/advanced-config/country-flag

By default Connect will launch based on the devices location impacting the brands that are available to the user e.g. Renault is only available in Europe.

You can override this behavior by passing a country feature flag in your Connect URL in the form `country:{country_code}`.

Your feature flag should contain the [two-character ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)
of the country that your user is located in.

<Tip>
  Our SDKs provide ways for you to add this as part of the various `authUrlBuilder` or `getAuthUrl` methods.
</Tip>

```plaintext Connect URL w/ country feature flag theme={null}
https://connect.smartcar.com/oauth/authorize?
response_type=code
&client_id=8229df9f-91a0-4ff0-a1ae-a1f38ee24d07
&scope=read_odometer read_vehicle_info
&redirect_uri=https://example.com/home
&flags=country:GB
```

Alternatively, your users can manually change their country and language on Connect's preamble screen:

<Frame caption="Country selector dropdown on the Preamble screen in Connect" type="simple">
  <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/connect/countrySelector.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=6ec90575ab9a84181c4be3ef06a66bfc" data-og-width="786" width="786" data-og-height="1132" height="1132" data-path="images/connect/countrySelector.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/connect/countrySelector.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=f225235b0f894d8b89f5546bbfea87b3 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/connect/countrySelector.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=04a23419bd9c409983c2c5d68095c954 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/connect/countrySelector.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=dad237a120e8b3206c84447fd709280b 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/connect/countrySelector.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=ef748d2898f29a73762bf2183b351306 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/connect/countrySelector.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=76f51cd9c73acae174b740211ddfd99e 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/connect/countrySelector.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=a6846d3072186cd52a0b2a22c104a678 2500w" />
</Frame>


# Connect Flows
Source: https://smartcar.com/docs/connect/advanced-config/flows

Connect can be launched with three different workflows (defult, single select, and single select with VIN). Depending on your use case and what information you  have about the vehicle ahead of a launching Connect, you may be able to leverage one of these flows for a more streamlined Connect experience.

<Tabs>
  <Tab title="Default" defaultOpen="true">
    When you launch Connect, users will be able to select the brand of their vehicle from a list before they enter their credentials and grant access to your application.

    <Frame caption="Default Smartcar Connect Flow">
      <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/default-connect-flow.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=c2cd906b5876221be223249b7ba0c8ef" data-og-width="3782" width="3782" data-og-height="1942" height="1942" data-path="images/default-connect-flow.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/default-connect-flow.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=57674aaf78d5e84ec7acf3a3e987101d 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/default-connect-flow.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=3009ebe305a4b1cbe0559c525f3b8bde 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/default-connect-flow.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=2d05dffc04980fbac98e83da00a09218 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/default-connect-flow.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=4c7f94b577ddffff375afe841fe094b5 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/default-connect-flow.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=dc9a2de37a38d85955d176e3eea6a968 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/default-connect-flow.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=bfc194d9d2adabe6d5b0d2478dbe5954 2500w" />
    </Frame>
  </Tab>

  <Tab title="Authorizing a Single Vehicle">
    In some cases you may only want to connect to a single vehicle, even if there are more than one on your user's connected services account. Smartcar provides two ways for you to do this:

    * Single Select
    * Single Select with VIN

    ### Single Select

    Limits the user's selection on the permissions screen to a single car if there are multiple vehicles on their connected services account. Notice that check-boxes turn into radio buttons, and the call to action wording changes slightly.

    <Frame caption="Grant Screen - Single Select without VIN">
      <img src="https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/single-selection.png?fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=c0ea2b982a0c93a3ea88f57b73e22041" data-og-width="863" width="863" data-og-height="1867" height="1867" data-path="images/single-selection.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/single-selection.png?w=280&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=a3620d3ee18252ab2ca59ff4e87fe53a 280w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/single-selection.png?w=560&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=ebc0df1e6ee5fbb05d56a42e0b326958 560w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/single-selection.png?w=840&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=7976153b366c422d046291d2783b1846 840w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/single-selection.png?w=1100&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=ef5334216cccf2e27d08afee2e632dd2 1100w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/single-selection.png?w=1650&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=bd9266503099f1caba742b83d7c9bb94 1650w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/single-selection.png?w=2500&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=e3e1effe1e6566d0962278db31c4d410 2500w" />
    </Frame>

    To enable Single Select, you can pass `single_select=true` as URL parameter when launching Smartcar Connect.

    ### Single Select with VIN

    In addition, if you know the user’s VIN ahead of time you can pass this over to us in the connect URL. In doing so:

    1. Smartcar  decodes the VIN to get the brand and send the user to the appropriate login form directly
    2. If the owner has more than one vehicle on their connected services account, we’ll only show the VIN that was passed to us on the permission grant screen.

    <Frame caption="Single Select /w VIN: Preamble > Brand’s Login Form > Grant Screen  - no vehicle choice">
      <img src="https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/single-select.png?fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=f27cd7030d595ec7c56f9a3dd537cfbc" data-og-width="2822" width="2822" data-og-height="1946" height="1946" data-path="images/single-select.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/single-select.png?w=280&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=2bed927de3ccb4ffcf2b97bd0451cc0a 280w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/single-select.png?w=560&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=884a0ea1717068601a7a1ce8e8b6d0c0 560w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/single-select.png?w=840&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=c3adb6503c4c610b99c9cae241e5f65f 840w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/single-select.png?w=1100&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=43e2c5bab7ff3861f6aee498b2ae81b7 1100w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/single-select.png?w=1650&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=428c81f882fb76a74c9fbebf816fa50f 1650w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/single-select.png?w=2500&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=34424df262f891adcb7281f89fbfc220 2500w" />
    </Frame>

    To enable Single Select with VIN, you can pass `single_select=true` and `single_select_vin=:vin` as URL parameters when launching Smartcar Connect.
  </Tab>

  <Tab title="Bypassing the Brand Selection Screen">
    ### Brand Select

    Instead of having users go through the brand selector screen, you can pass us a brand in the Connect URL and send the user to the appropriate login form directly.

    <Frame caption="Brand Select">
      <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/brand-select.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=8c25487faed02ad5dfba4e3a853a8ad0" data-og-width="2822" width="2822" data-og-height="1946" height="1946" data-path="images/brand-select.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/brand-select.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=60a46248faa5b363388cedaee53ef617 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/brand-select.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=f5c68e202d9fa45e93cfbc145acad703 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/brand-select.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=6b43c15fd66151bcb7bfbce57bbfb923 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/brand-select.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=c938d1dd783ddd36b1bcee393fd95769 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/brand-select.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=8a255483bf29d22f3aaaea0157d64cf3 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/brand-select.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=3b1a65832e403075d321921f96c928a9 2500w" />
    </Frame>

    To enable Brand Select, you can pass `make` as URL parameter when launching Connect. For example, `make=TESLA`
  </Tab>
</Tabs>


# Modes
Source: https://smartcar.com/docs/connect/advanced-config/modes

Connect can be launched in different modes depending on whether you want to interact with real vehicles or test your integration.

<Tip>
  If no mode is specified, Connect will launch in `live` mode by default.
</Tip>

| Mode      | Description                                                                                                           |
| --------- | --------------------------------------------------------------------------------------------------------------------- |
| live      | Launches Connect in live mode allowing a user to log in with a real connected services account.                       |
| simulated | Launches Connect in simulated mode allowing developers to connect to vehicles created on Dashboard via the Simulator. |


# SDKs for Connect
Source: https://smartcar.com/docs/connect/connect-sdks

Our SDKs make integrating Smartcar fast and easy in different languages and frameworks.

For mobile or single page web apps, you can use one of our frontend SDKs. Please note that our frontend SDKs only handle
integrating Connect into your application. You will still need to use a [backend SDK](/api-reference/api-sdks) to manage tokens and make API requests to vehicles.

<Snippet file="sdks/connect-sdk-card-group.mdx" />

<Note>**Note:** In addition to using a frontend SDK to integrate with Smartcar Connect, a backend SDK is strongly recommended to securely manage tokens, receive data from Smartcar, and make API requests to issue commands to vehicles. The backend SDK facilitates authentication, token exchange, and all communication with Smartcar’s APIs.</Note>

For server-side rendered applications, you can use one of our backend SDKs:

<Snippet file="sdks/api-sdk-card-group.mdx" />

<br />

<Tip>
  Don't see an SDK for your language? No problem!
  As long as you can build a URL and handle http requests, you're good to go.
</Tip>


# Dashboard Configuration
Source: https://smartcar.com/docs/connect/dashboard-config



## Registration

To get started, register your application with Smartcar by navigating to our [dashboard](https://dashboard.smartcar.com/login).

After registration, your application will be assigned a `CLIENT_ID` and a `CLIENT_SECRET`. The `CLIENT_SECRET` must be kept safe and used only in exchanges between your application’s server and Smartcar’s <Tooltip tip="https://connect.smartcar.com">authorization server</Tooltip>.

## Redirect URIs

To authorize with Smartcar, you’ll need to provide one or more redirect URIs. The user will be redirected to the specified URI upon authorization. On redirect, the URI will contain an authorization `code` query parameter that must be exchanged with Smartcar’s authorization server for an `ACCESS_TOKEN`.

The first redirect URI you add to your application is automatically set as the default. If you do not specify a `redirect_uri` in your Connect URL, Smartcar will use this default URI. You can add multiple URIs and set any of them as the default in the Smartcar Dashboard.

The redirect URIs must match one of the following formats:

| Protocol       | Format                                                                                   | Example                                                                        |
| -------------- | ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| HTTP           | a localhost URI with protocol `http://`                                                  | `http://localhost:8000`                                                        |
| HTTPS          | a URI with protocol `https://`                                                           | `https://myapplication.com`                                                    |
| JavaScript SDK | `https://javascript-sdk.smartcar.com/v2/redirect?app_origin={localhost-or-HTTPS-origin}` | `https://javascript-sdk.smartcar.com/v2/redirect?app_origin=https://myapp.com` |
| Custom-scheme  | `sc{clientId}://{hostname-with-optional-path-component-or-TLD}`                          | `sc4a1b01e5-0497-417c-a30e-6df6ba33ba46://callback`                            |

<Note>HTTP is allowed only for testing purposes on localhost</Note>

### Javascript SDK

The JavaScript SDK redirect is used along with the JavaScript SDK library. For more details and examples on the redirect usage, see the [SDK documentation](https://github.com/smartcar/javascript-sdk).

### Custom-scheme

Custom-scheme URIs are used for mobile applications. They must begin with `sc{clientId}` and can have an optional path or TLD. See the OAuth reference on redirect URIs.


# Handle the Response
Source: https://smartcar.com/docs/connect/handle-the-response

Upon successfully accepting the permissions, Smartcar will redirect the user back to your application using the specified `REDIRECT_URI`, along with an authorization code as a query parameter. In the case of an error, we'll provide an error and description as parameters instead.

## Success

<ResponseField name="code">
  An authorization code used to obtain your initial `ACCESS_TOKEN`. The auth `code` expires after **10 minutes**.
</ResponseField>

<Snippet file="response-connect-state.mdx" />

```http Success theme={null}
HTTP/1.1 302 Found
Location: https://example.com/home?
code=90abecb6-e7ab-4b85-864a-e1c8bf67f2ad
&state=0facda3319
```

## Error

For a detailed description of these errors, please see our [errors page](/api-reference/api-errors).

<ResponseField name="error">
  The type of error
</ResponseField>

<ResponseField name="error_description">
  A detailed description of what caused the error
</ResponseField>

<Snippet file="response-connect-state.mdx" />

```http Error theme={null}
HTTP/1.1 302 Found
Location: https://example.com/home?
error=access_denied
&error_description=User+denied+access+to+application.
&state=0facda3319
```

<Info>
  In addition to the error code and description, Smartcar will return the following parameters when a
  user tries to authorize an incompatible vehicle in Connect.
</Info>

<ResponseField name="vin">
  Can be returned for errors where the vehicle is incompatible.
</ResponseField>

<ResponseField name="make">
  The manufacturer of the vehicle.
</ResponseField>

<ResponseField name="model">
  The model of the vehicle.
</ResponseField>

<ResponseField name="year">
  The year of production of the vehicle.
</ResponseField>


# Rivian Bluetooth Pairing
Source: https://smartcar.com/docs/connect/other-actions/rivian-bluetooth-pairing

To support vehicle commands such as lock/unlock or start/stop charge, Rivian requires a mobile device to be paired via Bluetooth with the vehicle.

If permissions for commands are requested in your Connect URL (i.e. `control_security`, `control_charge`), Rivian owners will be prompted to pair their phone to the vehicle to complete the connection. After successful login, users will see a list of vehicles within their Rivian account to pair to. It is important that the mobile phone has Bluetooth enabled at this time.

<Frame caption="Prompting the user to select which Rivian vehicle to connect to">
  <img width="500" src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/connect/rivian-bt-vehicles.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=ab67ad9f1eaf09e8f819bae41e184878" data-og-width="1170" data-og-height="2532" data-path="images/connect/rivian-bt-vehicles.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/connect/rivian-bt-vehicles.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=0ebd0cc2517c7262eada5c3d120e481c 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/connect/rivian-bt-vehicles.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=7c0917e2712f307fcebb78596118402f 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/connect/rivian-bt-vehicles.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=9580d964e0ded9ee928f511e6d034829 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/connect/rivian-bt-vehicles.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=79929c99995f70b236dea4220c83ee05 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/connect/rivian-bt-vehicles.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=92c58c24d3dff873cff536db242f18db 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/connect/rivian-bt-vehicles.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=125d2974195673be2afa68c9bcf71aa8 2500w" />
</Frame>

After selecting the vehicle, the user will be prompted to tap “Set up now” on the Rivian vehicle’s display and follow any on-screen prompts to connect.

<Frame caption="Prompting the user to pair their Rivian vehicle via Bluetooth">
  <img width="500" src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/connect/rivian-bt-display.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=3bbe88f38e27fa53afffce49497c3128" data-og-width="1170" data-og-height="2532" data-path="images/connect/rivian-bt-display.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/connect/rivian-bt-display.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=befb0318a44c14ba29f0610c4c38161d 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/connect/rivian-bt-display.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=1ab0e4a937a381fc0602db496122c41c 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/connect/rivian-bt-display.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=22aebbf10671db0cc7255e78d36a40d7 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/connect/rivian-bt-display.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=6b4cb07916265fd2edbd1b150277eb69 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/connect/rivian-bt-display.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=afa0b9d985c48c69ef33db6f50d493e5 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/connect/rivian-bt-display.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=f4c976d28cc20b1b45eeafe15d427034 2500w" />
</Frame>

Once setup is complete, the application will be able to issue commands to the Rivian vehicle.

<Frame caption="Rivian Bluetooth pairing complete">
  <img width="500" src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/connect/rivian-bt-complete.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=827d7fce67b6225fca9f32104fe3fa41" data-og-width="1170" data-og-height="2532" data-path="images/connect/rivian-bt-complete.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/connect/rivian-bt-complete.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=e1105d614fb4847e64a766855b6dd824 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/connect/rivian-bt-complete.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=b0b3612943edf9c830e86f3ff48cd8fe 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/connect/rivian-bt-complete.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=ecb5e1c23aebd618b309e9e96f59ef3f 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/connect/rivian-bt-complete.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=8d466f07436f7cd81bfc3d92ed8cf694 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/connect/rivian-bt-complete.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=0ed4e36b7699e79a3105fcdb35d59507 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/connect/rivian-bt-complete.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=4eefc7e0c954f8dca77de5f5346266f1 2500w" />
</Frame>

Should Bluetooth be disabled or the Rivian display prompts not followed, the Bluetooth connection will not be established and the vehicle will not be connected to your application.

<Frame caption="Warning users that vehicles that are not paired via Bluetooth will not be connected to the application">
  <img width="500" src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/connect/rivian-bt-not-connected.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=1c25f6c5891bd9b69693804047b534af" data-og-width="1170" data-og-height="2532" data-path="images/connect/rivian-bt-not-connected.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/connect/rivian-bt-not-connected.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=9a94b0c0e44c7988dedc653e8be0189c 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/connect/rivian-bt-not-connected.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=dae7e524cb3b5d2097dc91d1e3499fd1 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/connect/rivian-bt-not-connected.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=b49a9ed5b2ac81d0d8ca4424bca88247 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/connect/rivian-bt-not-connected.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=cf3bd4e1bc983fbfe58ac5984bf0caf9 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/connect/rivian-bt-not-connected.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=7a42ae6508b36d8da78bbea73cb12d40 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/connect/rivian-bt-not-connected.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=8fee16e39c6afcd5e18ee01f9623c201 2500w" />
</Frame>

## Notes

* Rivian vehicles must be paired via Bluetooth to support commands. Data permissions (i.e. `read_location`, `read_charge`) do not require Bluetooth pairing.
* The following commands are supported for Rivian vehicles: lock/unlock, start/stop charge, and set charge limit.
* If a user has multiple Rivian vehicles, they will be prompted to pair each vehicle that they wish to connect to your application.
* At least one vehicle must be paired via Bluetooth to complete the pairing process before the user can continue with the Connect flow and connect their Rivian to your application.
* If there are multiple drivers associated with a Rivian account and both drivers want to connect to your application, each driver must pair their mobile device to the vehicle via Bluetooth.
* There is a limit of four devices that can be paired to a Rivian vehicle at one time. If a user has already paired four devices to their Rivian, they will need to unpair one of the existing devices from the vehicle before they can pair their mobile device and complete the connection to your application.
* Smartcar mobile SDKs for iOS and Android are required to pair the vehicle via Bluetooth.


# Tesla Virtual Keys
Source: https://smartcar.com/docs/connect/other-actions/tesla-virtual-key

To support vehicle commands such as lock/unlock or start/stop charge, and benefit from faster data frequencies, Tesla requires a Virtual Key to be added to the vehicle.

For more information about Virtual Keys, please visit the [Virtual Key page](/help/oem-integrations/tesla/virtual-key-tesla).

### Vehicle Owners adding a Virtual Key

Smartcar Connect will present Tesla vehicle owners a prompt to install the Tesla Virtual Key after granting access and prior to redirecting them back to your application.

<Frame caption="Prompting the user to add a Virtual Key">
  <img width="700" src="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/VirtualKeyPageMobile.png?fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=e504d181b6936f3e0ba17926a2923be2" data-og-width="2283" data-og-height="931" data-path="images/help-center/oem-integrations/tesla/add-virtual-key/VirtualKeyPageMobile.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/VirtualKeyPageMobile.png?w=280&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=02c5b864bdd1e8c5541ed1a1bfc80549 280w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/VirtualKeyPageMobile.png?w=560&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=a1ca3a12ee41154e396ae4ce1b56af65 560w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/VirtualKeyPageMobile.png?w=840&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=89747ff417caaf5f36b30737aa24bd0a 840w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/VirtualKeyPageMobile.png?w=1100&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=6f5036a32588937a17a0ea6fb0adc4bb 1100w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/VirtualKeyPageMobile.png?w=1650&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=3e4e9358fb3e91fc7e6b1ad8bc7bac0d 1650w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/VirtualKeyPageMobile.png?w=2500&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=b8b9c2e23830523d41d1c9c753d3b309 2500w" />
</Frame>

When users open the virtual key link, depending on their device, they will be redirected to the Tesla app or prompted to scan a QR code.

<Tabs>
  <Tab title="Mobile Device">
    On mobile devices, they will be redirected to the Tesla app and prompted to add the Virtual Key

    <Frame caption="Opening the link on a mobile device with the Tesla app installed">
      <img width="600" src="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/mobile.png?fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=1aa3cfa6758a83b3c5384019c8ce9516" data-og-width="4964" data-og-height="4854" data-path="images/help-center/oem-integrations/tesla/add-virtual-key/mobile.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/mobile.png?w=280&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=38179fb64a3f35c9c6412881a41f63a2 280w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/mobile.png?w=560&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=dd132f40eaf0ac8ce3f8c06a4a49937a 560w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/mobile.png?w=840&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=d1f968b7d55de343324b9c34fa1445ae 840w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/mobile.png?w=1100&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=40b9a8fa4ac2c2060da42b5cf08d849b 1100w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/mobile.png?w=1650&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=a01aa61cae09b50959b4f8d03936e056 1650w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/mobile.png?w=2500&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=2978ca715f21ff393c8a6fcd150d6b96 2500w" />
    </Frame>
  </Tab>

  <Tab title="Desktop">
    On Desktop, they will be prompted to scan the QR code which in turn opens up the Tesla app and prompts them to add a Virtual Key

    <Frame caption="Opening the link on a desktop">
      <img width="600" src="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/desktop.png?fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=d23186ba53fe3df10da5569734e35a55" data-og-width="2000" data-og-height="2283" data-path="images/help-center/oem-integrations/tesla/add-virtual-key/desktop.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/desktop.png?w=280&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=1fef759823638e7e4bef332c9ecc2746 280w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/desktop.png?w=560&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=b540a6e8a73a09c2335212f7e76cc83d 560w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/desktop.png?w=840&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=925d9141cba67f54650113d5b89eff78 840w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/desktop.png?w=1100&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=fb91f775461570fbf9babf0d1aa09e3f 1100w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/desktop.png?w=1650&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=072106f529447f5d80c34d216936f07c 1650w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/desktop.png?w=2500&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=c64d864789f7d4e035cc4c50bf2cb7dd 2500w" />
    </Frame>
  </Tab>
</Tabs>

Virtual Key status can be checked at any time from the Tesla infotainment screen under Settings > Locks.

<Frame caption="Check Virtual Key status from your Tesla">
  <img width="600" src="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/infotainment.png?fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=2aa353d17ed5cde11109469fd2e0a798" data-og-width="2720" data-og-height="1802" data-path="images/help-center/oem-integrations/tesla/add-virtual-key/infotainment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/infotainment.png?w=280&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=79989c8784343f6e73094b0e0ebcf348 280w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/infotainment.png?w=560&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=d8b4063d497c846e867109f96ee6afad 560w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/infotainment.png?w=840&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=4df5837d63f70457f4be3a837ad565d9 840w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/infotainment.png?w=1100&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=13e05d49490a3d98848e8045e183fb2c 1100w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/infotainment.png?w=1650&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=b6b2d077092b08c3fb72f852f706d256 1650w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/infotainment.png?w=2500&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=990cf7ae17b09c73129ac1eb6cf934ae 2500w" />
</Frame>

Smartcar will automatically determine which Tesla vehicles require a Virtual Key and prompt users to add it only for those vehicles. If a user has multiple Tesla vehicles, they will be prompted to add a Virtual Key for each vehicle that requires it. At least one vehicle must complete the pairing process before the user can continue with the Connect flow and connect their Tesla to your application.


# Handle the Response
Source: https://smartcar.com/docs/connect/re-auth/handle-response

If the re-auth is successful, the redirect to your application will contain a vehicle ID. In the case of an error, we'll provide an error and description as parameters instead.

## Success

<ResponseField name="vehicle_id">
  Unique identifier for a vehicle on Smartcar’s platform.
</ResponseField>

<Snippet file="response-connect-state.mdx" />

```http Success theme={null}
HTTP/1.1 302 Found
Location: https://example.com/home?
vehicle_id=sc4a1b01e5-0497-417c-a30e-6df6ba33ba46
&state=0facda3319
```

## Error

For a detailed description of these errors, please see our [errors page](/api-reference/api-errors).

<ResponseField name="error">
  The type of error
</ResponseField>

<ResponseField name="error_description">
  A detailed description of what caused the error
</ResponseField>

<Snippet file="response-connect-state.mdx" />

```http Error theme={null}
HTTP/1.1 302 Found
Location: https://example.com/home?
error=access_denied
&error_description=User+denied+access+to+application.
&state=0facda3319
```


# Redirect to Connect
Source: https://smartcar.com/docs/connect/re-auth/redirect-to-connect



There will be times when a user updates credentials to their connected services account. When this happens, the user will need to go through Connect
again to update your authorization through Smartcar.

You can do this with a streamlined Connect flow using a special re-auth URL with the parameters below.

<Tip>
  The [`AUTHENTICATION_FAILED`](/errors/api-errors/connected-services-account-errors#authentication-failed) API error contains a partially constructed re-authentication URL in the `resolution.url` field.
</Tip>

<br />

<ParamField path="client_id" type="string" required>
  The application’s unique identifier.
</ParamField>

<ParamField path="redirect_uri" type="string" required>
  The URI a user will be redirected to after authorization. This value **must** match one of the redirect URIs set in the credentials tab of the dashboard.

  The first redirect URI you add to your application is automatically set as the default. If you do not specify a `redirect_uri` in your Connect URL, Smartcar will use this default URI. You can add multiple URIs and set any of them as the default in the Smartcar Dashboard.
</ParamField>

<ParamField path="response_type" type="string" required>
  This value must be set to `vehicle_id`.
</ParamField>

<ParamField path="vehicle_id" type="string" required>
  The id of the vehicle you are reauthenticating.
</ParamField>

<ParamField path="state" type="string">
  An optional value included as a query parameter in the redirect\_uri back to your application. This value is often used to identify a user and/or prevent cross-site request forgery
</ParamField>

<ParamField query="user" type="string">
  Specify a unique identifier for the vehicle owner to track and aggregate analytics across Connect sessions for each vehicle owner on Dashboard.

  Note: Use the `state` parameter in order to identify the user at your callback URI when receiving an authorization or error code after the user exits the Connect flow.
</ParamField>

<RequestExample>
  ```http Connect URL Example theme={null}
  HTTP/1.1 302 Found
  Location: https://connect.smartcar.com/oauth/reauthenticate?
    response_type=vehicle_id
    &client_id=8229df9f-91a0-4ff0-a1ae-a1f38ee24d07
    &vehicle_id=sc4a1b01e5-0497-417c-a30e-6df6ba33ba46
    &redirect_uri=https://example.com/home
    &state=0facda3319
  ```
</RequestExample>


# Build the Connect URL
Source: https://smartcar.com/docs/connect/redirect-to-connect

Learn how to construct the Smartcar Connect URL to redirect users through the vehicle authorization flow.

<Tip>
  For mobile or single-page web applications you can use one of our [frontend SDKs](/connect/connect-sdks), or for server-side rendered applications you can use one of
  our [backend SDKs](/connect/connect-sdks). Using our SDKs makes it much easier to generate the Connect URL with the proper parameters.
</Tip>

You can configure default permissions for your application in the "Vehicle Access" tab of your application's Configuration page in the [Smartcar Dashboard](https://dashboard.smartcar.com). These settings will determine what permissions are requested during the Connect flow. Any `scope` parameters you specify in the Connect URL will override these dashboard settings.

<Frame>
  <img src="https://mintcdn.com/smartcar-docs/Nbq9w5qPmZOA1Bge/images/dashboard/dashboard-configuration-vehicle-access.png?fit=max&auto=format&n=Nbq9w5qPmZOA1Bge&q=85&s=c3ab83997ea333267fd1aec7b88a810c" alt="Smartcar Dashboard Configuration Page For Vehicle Access" data-og-width="3262" width="3262" data-og-height="2862" height="2862" data-path="images/dashboard/dashboard-configuration-vehicle-access.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/Nbq9w5qPmZOA1Bge/images/dashboard/dashboard-configuration-vehicle-access.png?w=280&fit=max&auto=format&n=Nbq9w5qPmZOA1Bge&q=85&s=3d8870830dcf057fff8d3672df828ef1 280w, https://mintcdn.com/smartcar-docs/Nbq9w5qPmZOA1Bge/images/dashboard/dashboard-configuration-vehicle-access.png?w=560&fit=max&auto=format&n=Nbq9w5qPmZOA1Bge&q=85&s=a86cf3d20ce33a1158ee56690fe4928b 560w, https://mintcdn.com/smartcar-docs/Nbq9w5qPmZOA1Bge/images/dashboard/dashboard-configuration-vehicle-access.png?w=840&fit=max&auto=format&n=Nbq9w5qPmZOA1Bge&q=85&s=ea4e0ca901f954a6da88b3b2c7b597ab 840w, https://mintcdn.com/smartcar-docs/Nbq9w5qPmZOA1Bge/images/dashboard/dashboard-configuration-vehicle-access.png?w=1100&fit=max&auto=format&n=Nbq9w5qPmZOA1Bge&q=85&s=05f4036f1c0d196b0eb9678a7290fdcd 1100w, https://mintcdn.com/smartcar-docs/Nbq9w5qPmZOA1Bge/images/dashboard/dashboard-configuration-vehicle-access.png?w=1650&fit=max&auto=format&n=Nbq9w5qPmZOA1Bge&q=85&s=721cd3aedc861ecdf8d1b09b4a7eed77 1650w, https://mintcdn.com/smartcar-docs/Nbq9w5qPmZOA1Bge/images/dashboard/dashboard-configuration-vehicle-access.png?w=2500&fit=max&auto=format&n=Nbq9w5qPmZOA1Bge&q=85&s=00ce2c131ae17ee2b88a11c29be84b4d 2500w" />
</Frame>

Once you have configured your application, you can get a pre-built Connect URL by clicking the "Share Connect Link" button at the top right in the Smartcar Dashboard.

<Frame>
  <img src="https://mintcdn.com/smartcar-docs/Nbq9w5qPmZOA1Bge/images/dashboard/dashboard-configuration-share-url.png?fit=max&auto=format&n=Nbq9w5qPmZOA1Bge&q=85&s=5f71af4ad3cb76b586b6ba666c660198" alt="Getting the Connect URL" data-og-width="3252" width="3252" data-og-height="2866" height="2866" data-path="images/dashboard/dashboard-configuration-share-url.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/Nbq9w5qPmZOA1Bge/images/dashboard/dashboard-configuration-share-url.png?w=280&fit=max&auto=format&n=Nbq9w5qPmZOA1Bge&q=85&s=72e7def16513decc7e10f5b21fbd0aa7 280w, https://mintcdn.com/smartcar-docs/Nbq9w5qPmZOA1Bge/images/dashboard/dashboard-configuration-share-url.png?w=560&fit=max&auto=format&n=Nbq9w5qPmZOA1Bge&q=85&s=dac1384e77024c8671458b60ffa67177 560w, https://mintcdn.com/smartcar-docs/Nbq9w5qPmZOA1Bge/images/dashboard/dashboard-configuration-share-url.png?w=840&fit=max&auto=format&n=Nbq9w5qPmZOA1Bge&q=85&s=cece5089bd8aa0df4889c873ae2282d3 840w, https://mintcdn.com/smartcar-docs/Nbq9w5qPmZOA1Bge/images/dashboard/dashboard-configuration-share-url.png?w=1100&fit=max&auto=format&n=Nbq9w5qPmZOA1Bge&q=85&s=6c6213a99dd98c9fd8c3d738529daa83 1100w, https://mintcdn.com/smartcar-docs/Nbq9w5qPmZOA1Bge/images/dashboard/dashboard-configuration-share-url.png?w=1650&fit=max&auto=format&n=Nbq9w5qPmZOA1Bge&q=85&s=48256139733206414edd33c82d0e1143 1650w, https://mintcdn.com/smartcar-docs/Nbq9w5qPmZOA1Bge/images/dashboard/dashboard-configuration-share-url.png?w=2500&fit=max&auto=format&n=Nbq9w5qPmZOA1Bge&q=85&s=ccedd24bce536e69a4c5b1d50afba9d4 2500w" />
</Frame>

To build the Connect URL manually by overriding your dashboard settings, pass the following parameters:

<Warning>
  Any parameters you specify in the Connect URL will override your dashboard settings.
</Warning>

<ParamField query="client_id" type="string" required>
  The application’s unique identifier. This is available on the credentials tab of the dashboard
</ParamField>

<ParamField query="redirect_uri" type="string" required>
  The URI a user will be redirected to after authorization. This value must match one of the redirect URIs set in the credentials tab of the dashboard.

  The first redirect URI you add to your application is automatically set as the default. If you do not specify a `redirect_uri` in your Connect URL, Smartcar will use this default URI. You can add multiple URIs and set any of them as the default in the Smartcar Dashboard.
</ParamField>

<ParamField query="response_type" type="string" required>
  This value must be set to `code` during the initial authentication. OAuth2 outlines multiple authorization types. Smartcar Connect utilizes the “Authorization Code” flow.

  To reauthenticate a user after they have already connected a vehicle, you can set this value to the `vehicle_id` of a previously connected vehicle.
</ParamField>

<ParamField query="scope" type="[permissions]" required>
  A space-separated list of permissions that your application is requesting access to. The valid permission names can be found in the permissions section. A permission is optional by default. It can be made required by adding the required: prefix to the permission name, e.g. required:read\_odometer.

  If you don't specify a `scope` parameter, Smartcar will use the permissions configured in the "Vehicle Access" tab of your application's Configuration page in the Dashboard. Any `scope` parameters passed in the Connect URL will override those dashboard settings.
</ParamField>

<ParamField query="state" type="string">
  An optional value included as a query parameter in the `REDIRECT_URI` back to your application. This value is often used to identify a user and/or prevent cross-site request forgery
</ParamField>

<ParamField query="approval_prompt" default="auto" type="string">
  An optional value that sets the behavior of the approval dialog displayed to the user.
  Defaults to `auto` and will only display the approval dialog if the user has not previously approved the scope.
  Set this to `force` to ensure the approval dialog is always shown to the user even if they have previously approved the same scope.
</ParamField>

<ParamField query="mode" default="live" type="ENUM">
  <Expandable title="modes" defaultOpen="true">
    <ResponseField name="simulated" type="string">
      Simulated mode lets you make requests to a vehicle created using the Vehicle Simulator to receive realistic responses from specific makes, models, years, and various states of the vehicle.

      Should the selected simulator not support the desired endpoint randomized data will be returned instead.
    </ResponseField>

    <ResponseField name="live" type="string">
      Live mode should be used when connecting to a real vehicle.
    </ResponseField>
  </Expandable>
</ParamField>

<ParamField query="make" type="string">
  Allows users to bypass the Brand Selector screen. Valid `makes` can be found in the [makes](/api-reference/makes) section on API reference.
  The `single_select_vin` parameter takes precedence over this parameter.
</ParamField>

<ParamField query="single_select" type="bool" default="false">
  Sets the vehicle selection behavior of the grant dialog. If set to true, then the user is only allowed to select a single vehicle. Please refer to the Single Select section for more information.

  This parameter is only available in the Custom Plan.
</ParamField>

<ParamField query="single_select_vin" type="string">
  Sets the behavior of the permissions screen in Smartcar Connect.
  When using `single_select_vin`, you need to pass in the VIN (Vehicle Identification Number) of a specific vehicle into the `single_select_vin` parameter.
  Additionally, you need to set the `single_select` parameter to `true`.
  Smartcar Connect will then let the user authorize **only the vehicle with that specific VIN**.
  The `single_select_vin` parameter takes precedence over the `make` parameter.
  Please refer to the Single Select section for more information.

  This parameter is only available in the Custom Plan.
</ParamField>

<ParamField query="flags" type="[flags]">
  A space separated list of feature flags in the form `{flag}:{value}`.

  <Expandable title="flags">
    <ResponseField name="country" type="ENUM">
      The two-character ISO country code of the country that your user is located in. You can set the default country for Connect on Dashboard

      If no flag is passed or set as default on Dashboard, Smartcar will use the devices IP to set an appropriate country.

      This flag determines what brands are listed on the Brand Selector screen in Connect e.g. Renault is available in Europe, but not the US.
    </ResponseField>
  </Expandable>
</ParamField>

<ParamField query="user" type="string">
  Specify a unique identifier for the vehicle owner to track and aggregate analytics across Connect sessions for each vehicle owner on Dashboard.

  Note: Use the `state` parameter in order to identify the user at your callback URI when receiving an authorization or error code after the user exits the Connect flow.
</ParamField>

<RequestExample>
  ```http Example Connect URL theme={null}
  HTTP/1.1 302 Found
  Location: https://connect.smartcar.com/oauth/authorize?
  response_type=code
  &client_id=8229df9f-91a0-4ff0-a1ae-a1f38ee24d07
  &scope=read_odometer read_vehicle_info read_location
  &redirect_uri=https://example.com/home
  &state=0facda3319
  ```
</RequestExample>


# User Selected Battery Capacity
Source: https://smartcar.com/docs/connect/user-selected-batcap

This flow can be launched using the URL provided by the [battery capacity](/docs/api-reference/get-nominal-capacity) endpoint.

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


# What is Connect?
Source: https://smartcar.com/docs/connect/what-is-connect



Smartcar Connect is the fastest and most transparent way to collect user consent. Before you can make API requests to a car, your customer needs to link the vehicle to your app. It’s a simple process for your users to enroll their vehicles:

1. Select the car brand
2. Sign in
3. Give consent

<Frame caption="Default Smartcar Connect Flow">
  <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/default-connect-flow.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=c2cd906b5876221be223249b7ba0c8ef" data-og-width="3782" width="3782" data-og-height="1942" height="1942" data-path="images/default-connect-flow.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/default-connect-flow.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=57674aaf78d5e84ec7acf3a3e987101d 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/default-connect-flow.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=3009ebe305a4b1cbe0559c525f3b8bde 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/default-connect-flow.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=2d05dffc04980fbac98e83da00a09218 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/default-connect-flow.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=4c7f94b577ddffff375afe841fe094b5 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/default-connect-flow.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=dc9a2de37a38d85955d176e3eea6a968 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/default-connect-flow.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=bfc194d9d2adabe6d5b0d2478dbe5954 2500w" />
</Frame>

From your app, you'll [redirect your users to Connect](/connect/redirect-to-connect), and [handle the response](/connect/handle-the-response) once the user completes or exits the Connect flow. You'll receive a `code` that you'll use to [exchange](/api-reference/authorization/auth-code-exchange) for an access token to start making requests to their vehicle(s).

We have designed Connect in compliance with the OAuth2 authorization protocol, safely handling all user information.

Connect comes with robust configurations to fit your needs and frontend [SDKs](/connect/connect-sdks) for faster integration.


# Authentication Errors
Source: https://smartcar.com/docs/errors/api-errors/authentication-errors

Thrown when there is an issue with your authorization header.

# `NULL`

The authorization header is missing or malformed, or it contains invalid or expired authentication credentials (e.g. access token, client ID, client secret). Please check for missing parameters, spelling and casing mistakes, and other syntax issues.

```json  theme={null}
{
  "type": "AUTHENTICATION",
  "code": null,
  "description": "The authorization header is missing or malformed, or it contains invalid or expired authentication credentials. Please check for missing parameters, spelling and casing mistakes, and other syntax issues.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/authentication-errors",
  "statusCode": 401,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null } 
}
```

### Suggested Resolution

You can resolve this error by referring to our API reference and ensuring that you pass all the parameters as specified. If you are certain that your request is well-formed, please try refreshing your access token.

### Troubleshooting Steps

Refer to our API reference and ensure that you use the correct authentication mechanism for your request

* Check constants like Bearer and Basic for spelling mistakes.
* If you make a request to a vehicle endpoint, verify that your access token grants you access to the correct vehicle. You can do so by making a request to the /vehicles endpoint and ensuring that the correct vehicle ID is included in the returned response.
* If you have refreshed your access token, make sure that it persists and that you use your new token to make your request.


# Billing Errors
Source: https://smartcar.com/docs/errors/api-errors/billing-errors

Thrown when limits have been reached based on your plan, or if the feature is not available.

# `VEHICLE_LIMIT`

You’ve reached the limit of vehicles in your plan. Please upgrade to unlock access to more vehicles.

```json VEHICLE_LIMIT theme={null}
{
  "type": "BILLING",
  "code": "VEHICLE_LIMIT",
  "description": "You’ve reached the limit of vehicles in your plan. Please upgrade to unlock access to more vehicles.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/billing-errors#vehicle-limit",
  "statusCode": 430,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": "CONTACT_SUPPORT" }
}
```

### Troubleshooting Steps

To resolve this error, please [contact us](mailto:support@smartcar.com) to upgrade your plan and increase your vehicle limit.
Please note that you won’t be able to make requests to additional vehicles until the end of the current billing period or until you have upgraded your plan.

# `INVALID_PLAN`

The feature you are trying to use is not included in your current pricing plan. Please visit our pricing page to learn more about our plans and features.

```json INVALID_PLAN theme={null}
{
  "type": "BILLING",
  "code": "INVALID_PLAN",
  "description": "The feature you are trying to use is not included in your current pricing plan. Please visit our pricing page to learn more about our plans and features.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/billing-errors#invalid-plan",
  "statusCode": 430,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": "CONTACT_SUPPORT" } 
}
```

### Troubleshooting Steps

If you have checked our pricing page and believe that the feature you are trying to use is included in your plan,
please [contact us](mailto:support@smartcar.com) and we’ll be happy to assist you.

# `VEHICLE_REQUEST_LIMIT`

You have exceeded the number of API requests that are allowed for **this** vehicle in the current billing period.
Please log in to the [Smartcar dashboard](https://dashboard.smartcar.com/login) and visit the Billing tab to learn more.

```json VEHICLE_REQUEST_LIMIT theme={null}
{
  "type": "BILLING",
  "code": "VEHICLE_REQUEST_LIMIT",
  "description": "You have exceeded the number of API requests that are allowed for this vehicle in the current billing period. Please log into the Smartcar dashboard and visit the Billing tab to learn more.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/billing-errors#vehicle-request-limit",
  "statusCode": 430,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": "CONTACT_SUPPORT" } 
}
```

### Troubleshooting Steps

To resolve this error, please [contact us](mailto:support@smartcar.com) to upgrade your plan and increase your vehicle limit.
Please note that you won’t be able to make additional requests to this vehicle until the end of the current billing period or until you have upgraded your plan.

# `ACCOUNT_SUSPENDED`

Your Smartcar account is past due and has been suspended.
Please reach out to our finance team to resolve this issue.

```json ACCOUNT_SUSPENDED theme={null}
{
  "type": "BILLING",
  "code": "ACCOUNT_SUSPENDED",
  "description": "Your Smartcar account is past due and has been suspended. Please reach out to our finance team to resolve this issue.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/billing-errors#account-suspended",
  "statusCode": 430,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20882a",
  "resolution": { "type": "FINANCE" } 
}
```

### Troubleshooting Steps

To resolve this error, please [contact us](mailto:finance@smartcar.com) to pay past due invoices.
Please note that you won’t be able to make any requests until you have resolved this issue.


# Compatibility Errors
Source: https://smartcar.com/docs/errors/api-errors/compatibility-errors

Thrown when Smartcar does not support a make, or feature for a vehicle.

# `MAKE_NOT_COMPATIBLE`

Smartcar is not yet compatible with this vehicle’s make in the country you specified.

```json  theme={null}
{
  "type": "COMPATIBILITY",
  "code": "MAKE_NOT_COMPATIBLE",
  "description": "Smartcar is not yet compatible with this vehicle’s make in the country you specified.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/compatibility-errors#make-not-compatible",
  "statusCode": 501,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null } 
}
```

**Suggested User Messaging**<br />
`<your app name>` is not yet able to connect to your car brand.

<br />

# `PLATFORM_NOT_CAPABLE`

You're connected to the vehicle using an OEM integration that does not support this endpoint. This can be a result of the OEM migrating to a newer API or requiring vehicle owners to migrate to a new application they have released.

```json  theme={null}
{
  "type": "COMPATIBILITY",
  "code": "PLATFORM_NOT_CAPABLE",
  "description": "You're connected to the vehicle using an OEM integration that does not support this endpoint.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/compatibility-errors#platform-not-capable",
  "statusCode": 501,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": "REAUTHENTICATE" } 
}
```

**Troubleshooting Steps**<br />
For Tesla vehicles please have the owner re-authenticate using the latest Tesla authorization flow.

<br />

# `SMARTCAR_NOT_CAPABLE`

Smartcar does not yet support this feature for this vehicle.

```json  theme={null}
{
  "type": "COMPATIBILITY",
  "code": "SMARTCAR_NOT_CAPABLE",
  "description": "Smartcar does not yet support this feature for this vehicle.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/compatibility-errors#smartcar-not-capable",
  "statusCode": 501,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null } 
}
```

**Troubleshooting Steps**<br />
Please check that the vehicles make and engine type support the feature you are trying to use.

Please contact us to learn when this feature will become available.
If you have a vehicle that supports this feature and would like to help out, check out Smartcar’s Research Fleet.

<br />

# `VEHICLE_NOT_CAPABLE`

This error occurs when a physical limitation makes the vehicle incapable of performing your request
(e.g. battery electric vehicles are incapable of responding to read fuel requests).

```json  theme={null}
{
  "type": "COMPATIBILITY",
  "code": "VEHICLE_NOT_CAPABLE",
  "description": "The vehicle is incapable of performing your request.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/compatibility-errors#vehicle-not-capable",
  "statusCode": 501,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null } 
}
```

**Suggested User Messaging**<br />
Your car is unable to perform this request.

<br />


# Connected Services Account Errors
Source: https://smartcar.com/docs/errors/api-errors/connected-services-account-errors

Thrown when there are issues with the user's connected service account.

# `ACCOUNT_ISSUE`

Action needed in the user’s connected services account. The user needs to log in and complete an outstanding task in their connected services account.

Examples:

* The user needs to accept the connected services app’s Terms of Service.
* The user has created but not yet fully activated their connected services account.
* If you've received this error while testing with Vehicle Simulator, it likely means a simulation has not been started for the vehicle. Visit the Simulator tab in the Smartcar Dashboard to start a simulation for the vehicle.

```json  theme={null}
{
  "type": "CONNECTED_SERVICES_ACCOUNT",
  "code": "ACCOUNT_ISSUE",
  "description": "Action needed in the user’s connected services account. Please prompt the user to log into their connected services account and complete any outstanding tasks.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/connected-services-account-errors#account-issue",
  "statusCode": 400,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null },
  "suggestedUserMessage": "Action required in your connected services account. Please log into your connected services app or web portal and complete any outstanding tasks (e.g. finish activating your account or accept the Terms of Service)." 
}
```

### Suggested resolution

The user can resolve this error by logging into their connected services account and completing any outstanding tasks.

### Troubleshooting steps

* Prompt the user to log into their connected services account using the app or web portal.
* Prompt the user to try triggering an action on their car, e.g. locking the doors or flashing the lights.
* At this point, the app should prompt the user to complete their outstanding task.

### Suggested user message

> Action required in your connected services account. Please log into your connected services app or web portal and complete any outstanding tasks (e.g. finish activating your account or accept the Terms of Service).

***

# `AUTHENTICATION_FAILED`

Smartcar was unable to authenticate with the user’s connected services account. This error usually occurs when the user has updated their connected
services account credentials and not yet re-authenticated in Smartcar Connect. The user should re-authenticate using Smartcar Connect.

```json  theme={null}
{
  "type": "CONNECTED_SERVICES_ACCOUNT",
  "code": "AUTHENTICATION_FAILED",
  "description": "Smartcar was unable to authenticate with the user’s connected services account. Please prompt the user to re-authenticate using Smartcar Connect.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/connected-services-account-errors#authentication-failed",
  "statusCode": 400,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": {
    "type": "REAUTHENTICATE",
    "url": "https://connect.smartcar.com/oauth/reauthenticate?response_type=vehicle_id&client_id=8229df9f-91a0-4ff0-a1ae-a1f38ee24d07&vehicle_id=sc4a1b01e5-0497-417c-a30e-6df6ba33ba46"
  },
  "suggestedUserMessage": "Your car got disconnected from <app name>. Please use this link to re-connect your car: <link to Smartcar Connect>."
}
```

### Suggested resolution

Please provide the user with a link to Smartcar Connect Re-authentication and prompt them to re-connect their vehicle.
The resolution field contains a partially constructed URL for Smartcar Connect Re-authentication, please see the API reference for more detail.

### Suggested user message

> Your car got disconnected from \<app name>. Please use this link to re-connect your car: \<link to Smartcar Connect>.

***

# `NO_VEHICLES`

No vehicles found in the user’s connected services account. The user might not yet have added their vehicle to their account, or they might not yet have activated connected services for the vehicle.

```json  theme={null}
{
  "type": "CONNECTED_SERVICES_ACCOUNT",
  "code": "NO_VEHICLES",
  "description": "No vehicles found in the user’s connected services account. Please prompt the user to add their vehicle to their connected services account and re-authenticate using Smartcar Connect.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/connected-services-account-errors#no-vehicles",
  "statusCode": 400,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null }, 
  "suggestedUserMessage": "Your car got disconnected from <app name>. Please use this link to re-connect your car: <link to Smartcar Connect>."
}
```

### Suggested resolution

Please provide the user with a link to Smartcar Connect Re-authentication and prompt them to re-connect their vehicle.
The resolution field contains a partially constructed URL for Smartcar Connect Re-authentication, please see the API reference for more detail.

### Troubleshooting Steps

* Prompt the user to log into their connected services account using the app or web portal.
* Prompt the user to check whether there are any vehicles listed in their account.
* If there are no vehicles listed, prompt the user to add their vehicle.
* If there are one or more vehicles listed, this means that none of the vehicles have had their connected services activated. Prompt the user to activate connected services for at least one vehicle.
* Provide the user with a link to Smartcar Connect and prompt them to re-connect their vehicle.

### Suggested user message

> Your car got disconnected from \<app name>. Please use this link to re-connect your car: \<link to Smartcar Connect>.

***

# `PERMISSION`

This error occurs when a vehicle owner had initially granted Smartcar access to their OEM account, but has since revoked it via the OEM's management portal.

```json  theme={null}
{
  "type": "CONNECTED_SERVICES_ACCOUNT",
  "code": "PERMISSION",
  "description": "The vehicle owner has revoked Smartcar’s access to their OEM account.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/connected-services-account-errors#permission",
  "statusCode": 400,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": {
	  "type" : "REAUTHENTICATE"
  }
}
```

### Suggested resolution

For Tesla Owners:

* Prompt the vehicle owner to go through the Connect flow again or use our [reauthentication flow](/help/oem-integrations/tesla/developers#stand-alone-flow) to streamline the process.

***

# `SUBSCRIPTION`

The vehicle’s connected services subscription is inactive or does not support the requested API endpoint.

```json  theme={null}
{
  "type": "CONNECTED_SERVICES_ACCOUNT",
  "code": "SUBSCRIPTION",
  "description": "The vehicle’s connected services subscription is inactive or does not support the requested API endpoint.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/connected-services-account-errors#subscription",
  "statusCode": 400,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null },
  "suggestedUserMessage": "Your car’s connected services subscription has either expired or it doesn’t support the necessary features to connect to <app name>. Please activate your subscription or contact us to upgrade your subscription."
}
```

### Suggested resolution

The user can resolve this error by logging into their connected services account and either (re-)activating their subscription or purchasing the required subscription package.

### Troubleshooting Steps

If you don’t know which subscription package the user needs to purchase, please contact our team for help.

### Suggested user message

> Your car’s connected services subscription has either expired or it doesn’t support the necessary features to connect to \<app name>. Please activate your subscription or contact us to upgrade your subscription.

***

# `VEHICLE_MISSING`

This vehicle is no longer associated with the user’s connected services account. The user might have removed it from their account.
The user needs to log into their connected services account and either re-add the vehicle or re-activate its subscription.

If you've received this error while testing with Vehicle Simulator, it likely means the simulated vehicle has not been found in your application. Visit the Simulator tab in the Smartcar Dashboard to create a simulated vehicle to test with.

```json  theme={null}
{
  "type": "CONNECTED_SERVICES_ACCOUNT",
  "code": "VEHICLE_MISSING",
  "description": "This vehicle is no longer associated with the user’s connected services account. Please prompt the user to re-add the vehicle to their account.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/connected-services-account-errors#vehicle-missing",
  "statusCode": 400,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null },
  "suggestedUserMessage": "Your car’s connected services subscription has either expired or it doesn’t support the necessary features to connect to <app name>. Please activate your subscription or contact us to upgrade your subscription."
}
```

### Suggested resolution

The user can resolve this issue by logging into their connected services account and either re-adding the vehicle or re-activating its subscription.

If the user wishes to disconnect their vehicle from your app, please make a request to our Disconnect endpoint and refrain from making API requests to this vehicle in the future.

### Troubleshooting Steps

* Prompt the user to log into their connected services account using the app or web portal.
* Prompt the user to check whether the vehicle is listed under their account.
* If the vehicle is not listed, prompt the user to add the vehicle to their account.
* If the vehicle is listed, prompt the user to activate the vehicle’s connected services subscription.

### Suggested user message

> This car is no longer associated with your connected services account. Please log into your account and re-add this car.

***

# `VIRTUAL_KEY_REQUIRED`

The vehicle owner has granted your application access to the vehicle through Smartcar. However, additional steps are needed on the owners part in order to perform this specific request.

```json  theme={null}
{
  "type": "CONNECTED_SERVICES_ACCOUNT",
  "code": "VIRTUAL_KEY_REQUIRED",
  "description": "The vehicle owner needs to grant additional access to Smartcar in order to perform this request.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/connected-services-account-errors#virtual-key-required",
  "statusCode": 400,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": {
	  "type" : "ACTION_REQUIRED",
	  "url" : "https://www.tesla.com/_ak/smartcar.com"
  }
  "suggestedUserMessage": "In order to perform this request you’ll need to add a Third-Party Virtual key to your vehicle. Please open this link on the phone with your Tesla App to complete this step."
}
```

### Suggested resolution

For Tesla Owners:

* The vehicle owner needs to add Smartcar’s Third-Party Virtual Key. As of late 2023, Tesla is starting to require virtual keys for Third-Party applications to perform commands.
* In order to issue commands, please prompt the vehicle owner to add Smartcar’s Third-Party virtual key: [https://www.tesla.com/\_ak/smartcar.com](https://www.tesla.com/_ak/smartcar.com)

### Troubleshooting steps

* Please direct the vehicle owner to add Smartcar’s [Third-Party Virtual Key (tesla.com)](https://www.tesla.com/_ak/smartcar.com) in order to allow your application to issue commands to the vehicle.

### Suggested user message

> In order to perform this request you’ll need to add a Third-Party Virtual key to your vehicle. Please open [this](https://www.tesla.com/_ak/smartcar.com) link on the phone with your Tesla App to complete this step.


# Permission Errors
Source: https://smartcar.com/docs/errors/api-errors/permission-errors

Thrown when Smartcar does not support a make or feature for a vehicle.

# `NULL`

Your application has insufficient permissions to access the requested resource. Please prompt the user to re-authenticate using Smartcar Connect.

If you receive this error while testing with Vehicle Simulator, it is likely because the simulated vehicle has not yet been connected to your application, or your application doesn't have access to the requested permission.
Visit the Simulator documentation to learn how to connect the vehicle to your application.

```json  theme={null}
{
  "type": "PERMISSION",
  "code": null,
  "description": "Your application has insufficient permissions to access the requested resource. Please prompt the user to re-authenticate using Smartcar Connect.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/permission-errors#null",
  "statusCode": 403,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": "REAUTHENTICATE" }  
}
```

### Suggested Resolution

You can resolve this error by ensuring that the scope parameter contains all the permissions that your application requires and prompting the user to re-authenticate using Smartcar Connect.

### Troubleshooting Steps

* Ensure that the scope parameter contains all the permissions that your application requires.
* Ensure that you spell all permission names in the scope parameter correctly.
* Prompt the user to re-authenticate using Smartcar Connect.


# Rate Limit Errors
Source: https://smartcar.com/docs/errors/api-errors/rate-limit-errors

Thrown when there is an issue with the frequency of your requests.

# `SMARTCAR_API`

Your application has exceeded its rate limit. Please retry your request in a few minutes.

```json  theme={null}
{
  "type": "RATE_LIMIT",
  "code": "SMARTCAR_API",
  "description": "Your application has exceeded its rate limit. Please retry your request in a few minutes.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/rate-limit-errors#smartcar-api",
  "statusCode": 429,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": "RETRY_LATER" },
  "suggestedUserMessage": "Your vehicle is temporarily unable to connect to <app name>. Please be patient while we’re working to resolve this issue."
}
```

### Suggested resolution

You can resolve this error by refraining from making API requests for a certain period of time.
If your application automatically retries requests for certain errors, please disable automatic retries or implement a backoff period to retry certain requests less frequently.

### Troubleshooting steps

If you believe that you received this error by mistake and your application didn’t actually exceed its rate limit, please contact us and we’ll be happy to assist you.

### Suggested user message

> Your car is temporarily unable to connect to \<app name>. Please be patient while we’re working to resolve this issue.

***

# `VEHICLE`

You have reached the throttling rate limit for this vehicle. Please see the `retry-after` header (seconds) for when to retry the request.

This limit is in place to prevent excessive vehicle requests that could:

* Lead to 12v battery drain.
* Trigger UPSTREAM:RATE\_LIMIT errors that prevent you from making requests for a longer period of time.

```json  theme={null}
{
  "type": "RATE_LIMIT",
  "code": "VEHICLE",
  "description": "You have reached the throttling rate limit for this vehicle. Please see the retry-after header for when to retry the request.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/rate-limit-errors#vehicle",
  "statusCode": 429,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": "RETRY_LATER" },
  "suggestedUserMessage": "Your vehicle is temporarily unable to connect to <app name>. Please be patient while we’re working to resolve this issue."
 
}
```

### Suggested resolution

You can resolve this error by refraining from making API requests. Please see the retry-after header for when to try again. If your application automatically retries requests for certain errors, please disable them for this one.

### Suggested user message

> Your car is temporarily unable to connect to \<app name>. Please be patient while we’re working to resolve this issue.

***


# Resource Not Found
Source: https://smartcar.com/docs/errors/api-errors/resource-not-found-errors

Thrown when the incorrect API version is used or when the endpoint URL is incorrect.

# `PATH`

The requested resource does not exist. Please check the URL and try again.

```json  theme={null}
{
  "type": "RESOURCE_NOT_FOUND",
  "code": "PATH",
  "description": "The requested resource does not exist. Please check the URL and try again.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/resource-errors#pathh",
  "statusCode": 404,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null },
  "suggestedUserMessage": "Your vehicle is temporarily unable to connect to <app name>. Please be patient while we’re working to resolve this issue."
}
```

### Suggested Resolution

You can resolve this error by referring to our API reference and ensuring that you use the correct URL for your request.

### Troubleshooting Steps

* Ensure that you spell all static parts of the URL correctly.
* Ensure that you use the correct URL path parameters (e.g. vehicle ID).
* Ensure that you use the correct HTTP method.

***

# `VERSION`

The requested resource does not exist. Your request either does not specify a version number or it specifies a version number that is not supported by this resource.

```json  theme={null}
{
  "type": "RESOURCE_NOT_FOUND",
  "code": "VERSION",
  "description": "The requested resource does not exist. Please check your specified version number and try again.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/resource-errors#version",
  "statusCode": 404,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null },
  "suggestedUserMessage": "Your vehicle is temporarily unable to connect to <app name>. Please be patient while we’re working to resolve this issue."
}
```

### Suggested Resolution

You can resolve this error by referring to our API reference and ensuring that you specify v2.0 in the URL path (e.g. `https://api.smartcar.com/v2.0/vehicles`). Version 1 has been sunset and is no longer supported.


# Server Errors
Source: https://smartcar.com/docs/errors/api-errors/server-errors

Thrown when Smartcar runs into an unexpected issue and was unable to process the request.

# `INTERNAL`

An internal Smartcar error has occurred. Our team has been notified and is working to resolve this issue.

```json  theme={null}
{
  "type": "SERVER",
  "code": "INTERNAL",
  "description": "An internal Smartcar error has occurred. Our team has been notified and is working to resolve this issue.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/server-errors#internal",
  "statusCode": 500,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": "RETRY_LATER" },
  "suggestedUserMessage": "Your car is temporarily unable to connect to <app name>. Please be patient while we’re working to resolve this issue." 
}
```

### Suggested Resolution

Please contact us to learn more about the error and our steps to resolve it.

### Suggested User Message

> Your car is temporarily unable to connect to \<app name>. Please be patient while we’re working to resolve this issue.

***

# `RECORD_NOT_FOUND`

Smartcar is unable to locate a battery capacity record for this vehicle. Depending on the make of the vehicle, battery capacity may depend on upstream sources to fulfil a request if it is not directly provided by the OEM.

If you’re seeing this error then the OEM doesn’t provide all the data we aim to provide in our response and we were unable to locate this information from other sources.

```json  theme={null}
{
  "type": "SERVER",
  "code": "RECORD_NOT_FOUND",
  "description": "Smartcar was unable to locate a battery capacity record for this vehicle.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/server-errors#record-not-found",
  "statusCode": 500,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": "CONTACT_SUPPORT" },
  "suggestedUserMessage": "Your car is temporarily unable to connect to <app name>. Please be patient while we’re working to resolve this issue." 
}
```

### Suggested Resolution

Please reach out to support to see if we are able to update capacity data for the vehicle.

### Suggested User Message

> Your car is temporarily unable to connect to \<app name>. Please be patient while we’re working to resolve this issue.

***

# `MULTIPLE_RECORDS_FOUND`

Smartcar is unable to locate a battery capacity record for this vehicle. Depending on the make of the vehicle, battery capacity may depend on upstream sources to fulfil a request if it is not directly provided by the OEM.

If you’re seeing this error then the OEM doesn’t provide all the data we aim to provide in our response and we were unable to find a specific match. Please see the error response `detail` field for possible matches.

```json  theme={null}
{
	"statusCode": 500,
	"type": "SERVER",
	"code": "MULTIPLE_RECORDS_FOUND",
	"description": "Smartcar found multiple battery capacity records for this vehicle.",
	"docURL": "https://smartcar.com/docs/errors/api-errors/server-errors#multiple-records-found",
	"resolution": {
		"type": "CONTACT_SUPPORT"
	},
	"suggestedUserMessage": "Your car is temporarily unable to connect to <app name>. Please be patient while we’re working to resolve this issue.",
	"detail": [
		{
			"capacities": [83.9, 83.9, 70.2]
		}
	],
	"requestId": "9c8dd6fa-f9d7-4d18-9fdd-2255f6cd8613"
}
```

### Suggested Resolution

For battery capacity errors please check the detail field of the error response for a list of possible options and reach out support if you need us to update the capacity value for a specific vehicle.

### Suggested User Message

> Your car is temporarily unable to connect to \<app name>. Please be patient while we’re working to resolve this issue.


# Upstream Errors
Source: https://smartcar.com/docs/errors/api-errors/upstream-errors

Thrown when the OEM servers or vehicle failed to process the request.

<Info>
  <b>Check Smartcar Reliability & Status</b><br />
  For upt-to-date information on Smartcar's platform and brand reliability, visit our:

  <ul>
    <li><a href="https://brandreliability.smartcar.com/" target="_blank" rel="noopener">Brand Reliability page</a></li>
    <li><a href="https://status.smartcar.com/" target="_blank" rel="noopener">Platform Status page</a></li>
  </ul>
</Info>

# `INVALID_DATA`

One of Smartcar’s upstream sources provided data that is malformed, invalid, or logically invalid (e.g. 65535 psi for tire pressure).

```json  theme={null}
{
  "type": "UPSTREAM",
  "code": "INVALID_DATA",
  "description": "Smartcar received invalid data from an upstream source. Please retry your request at a later time.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/upstream-errors#invalid-data",
  "statusCode": 502,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": "RETRY_LATER" },
  "suggestedUserMessage": "Your car is temporarily unable to connect to <app name>. Please be patient while we’re working to resolve this issue." 
}
```

### Suggested resolution

You can resolve this error by retrying your request at a later time.

### Suggested user message

> Your car is temporarily unable to connect to \<app name>. Please be patient while we’re working to resolve this issue.

***

# `KNOWN_ISSUE`

Smartcar received an error from an upstream source. This error usually occurs when an upstream source experiences an error that we have previously investigated and categorized as a known issue.

```json  theme={null}
{
  "type": "UPSTREAM",
  "code": "KNOWN_ISSUE",
  "description": "Smartcar received an error from an upstream source. Please retry your request at a later time.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/upstream-errors#known-issue",
  "statusCode": 502,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": "RETRY_LATER" },
  "suggestedUserMessage": "Your car is temporarily unable to connect to <app name>. Please be patient while we’re working to resolve this issue." 
}
```

### Suggested resolution

You can resolve this error by retrying your request at a later time.

### Suggested user message

> Your car is temporarily unable to connect to \<app name>. Please be patient while we’re working to resolve this issue.

***

# `NO_RESPONSE`

One of Smartcar’s upstream sources failed to respond. This error usually occurs when one of Smartcar’s upstream sources is experiencing issues and is currently unavailable.
This error can also occur when a specific vehicle in located in an area with weak cellular reception and fails to respond to your request in a timely manner.

```json  theme={null}
{
  "type": "UPSTREAM",
  "code": "NO_RESPONSE",
  "description": "One of Smartcar’s upstream sources failed to respond. Please retry your request at a later time.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/upstream-errors#no-response",
  "statusCode": 502,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": "RETRY_LATER" },
  "suggestedUserMessage": "Your car is temporarily unable to connect to <app name>. Please be patient while we’re working to resolve this issue."
}
```

### Suggested resolution

You can resolve this error by retrying your request at a later time.

### Suggested user message

> Your car is temporarily unable to connect to \<app name>. Please be patient while we’re working to resolve this issue.

***

# `RATE_LIMIT`

Your application’s requests have exceeded this vehicle’s rate limit.

```json  theme={null}
{
  "type": "UPSTREAM",
  "code": "NO_RESPONSE",
  "description": "One of Smartcar’s upstream sources failed to respond. Please retry your request at a later time.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/upstream-errors#rate-limit",
  "statusCode": 502,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": "RETRY_LATER" },
  "suggestedUserMessage": "Your car is temporarily unable to connect to <app name>. Please be patient while we’re working to resolve this issue."
}
```

### Suggested resolution

You can resolve this error by refraining from making API requests to this specific vehicle for a period of time.
If your application automatically retries requests, please disable automatic retries or implement a backoff period to retry less frequently.

### Suggested user message

> Your car is temporarily unable to connect to \<app name>. Please be patient while we’re working to resolve this issue.

***

# `UNKNOWN_ISSUE`

Smartcar received an unknown error from an upstream source. This error usually occurs when one of Smartcar’s upstream sources experiences an error that we have not yet investigated or mitigated.

There are several reasons why we might not have investigated this error yet:

* The feature or vehicle make is still in beta.
* This error does not occur very frequently.
* This is the first time we have received this error.

```json  theme={null}
{
  "type": "UPSTREAM",
  "code": "UNKNOWN_ISSUE",
  "description": "Smartcar received an unknown error from an upstream source. Please retry your request at a later time and contact us if the issue persists.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/upstream-errors#unknown-issue",
  "statusCode": 502,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": "RETRY_LATER" },
  "suggestedUserMessage": "Your car is temporarily unable to connect to <app name>. Please be patient while we’re working to resolve this issue."
}
```

### Suggested resolution

Given the broad range of situations that can cause this error, you might or might not be able to resolve this error by retrying your request at a later time.
If you retry your request and the issue persists, please contact us to help you mitigate this error.

### Suggested user message

> Your car is temporarily unable to connect to \<app name>. Please be patient while we’re working to resolve this issue.

***


# Validation Errors
Source: https://smartcar.com/docs/errors/api-errors/validation-errors

Thrown if there is an issue with the format of the request or body.

# `NULL`

Request invalid or malformed. Please check for missing parameters, spelling and casing mistakes, and other syntax issues.

```json  theme={null}
{
  "type": "VALIDATION",
  "code": null,
  "description": "Request invalid or malformed. Please check for missing parameters, spelling and casing mistakes, and other syntax issues.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/validation-errors#null",
  "statusCode": 400,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null },
  "suggestedUserMessage": "Your car is temporarily unable to connect to <app name>. Please be patient while we’re working to resolve this issue."
}
```

### Suggested resolution

You can resolve this error by referring to our API reference and ensuring that you pass all the parameters as specified.

### Troubleshooting Steps

* Ensure that you spell and case all parameters correctly.

* Ensure that your request has the correct content-type (i.e. application/json or application/x-www-form-urlencoded).

* Ensure that your request has the correct URL and HTTP method.

### Suggested user message

> Your car is temporarily unable to connect to \<app name>. Please be patient while we’re working to resolve this issue.

***

# `PARAMETER`

Your request is formatted correctly, but one or more of the provided parameters is incorrect.

```json  theme={null}
{
  "type": "VALIDATION",
  "code": null,
  "description": "Your request is formatted correctly, but one or more of the provided parameters is incorrect.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/validation-errors#parameter",
  "statusCode": 400,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null },
  "suggestedUserMessage": "Your car is temporarily unable to connect to <app name>. Please be patient while we’re working to resolve this issue." 
}
```

### Suggested resolution

You can resolve this error by referring to our API reference and ensuring that you pass all the parameters as specified.

For Ford or Lincoln vehicles:

* Please check the coordinates provided for setting a charge schedule are associated with a saved charging location for this vehicle.

### Suggested user message

> Your car is temporarily unable to connect to \<app name>. Please be patient while we’re working to resolve this issue.


# Vehicle State Errors
Source: https://smartcar.com/docs/errors/api-errors/vehicle-state-errors

Thrown when a request fails due to the state of a vehicle or logically cannot be completed e.g. you can't start a vehicle charging if it's not plugged in.

# `ASLEEP`

The vehicle is in a sleep state and temporarily unable to perform your request. Either the vehicle has been inactive for a certain period of time (time periods vary between makes and models) or the user has manually triggered the vehicle’s sleep state.

```json  theme={null}
{
  "type": "VEHICLE_STATE",
  "code": "ASLEEP",
  "description": "The vehicle is in a sleep state and temporarily unable to perform your request.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/vehicle-state-errors#asleep",
  "statusCode": 409,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null },
  "suggestedUserMessage": "Your vehicle is in a sleep state. This request was not sent to preserve battery life. "
}
```

### Suggested resolution

The vehicle is in a sleep state and temporarily unable to perform your request.

### Troubleshooting Steps

* Prompt the user to start the vehicle’s engine (required) and to drive the vehicle for a short distance (optional).
* Wait for a few minutes and retry your request.
* Ensure that the vehicle’s 12-volt battery is sufficiently charged.

### Suggested user message

> Your car is temporarily unable to connect to \<app name>. To re-establish the connection, please start your car and take it for a short drive.

***

# `CHARGING_IN_PROGRESS`

The vehicle is currently charging and unable to perform your request. This error usually occurs when you make a request to the start charge endpoint while the vehicle is already charging.

```json  theme={null}
{
  "type": "VEHICLE_STATE",
  "code": "CHARGING_IN_PROGRESS",
  "description": "The vehicle is currently charging and unable to perform your request.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/vehicle-state-errors#charging-in-progress",
  "statusCode": 409,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null },
  "suggestedUserMessage": "Your vehicle is already charging."
}
```

### Suggested resolution

You usually don’t need to resolve this error. If you believe that this error should not have occurred, please follow the troubleshooting steps below.

### Troubleshooting Steps

* Prompt the user to stop charging their vehicle and/or unplug the charger.
* Wait for a few minutes and retry your request.

### Suggested user message

> Your car is already charging.

***

# `CHARGING_PLUG_CONNECTED`

The vehicle is connected to an EV charger and unable to perform your request.

```json  theme={null}
{
  "type": "VEHICLE_STATE",
  "code": "CHARGING_PLUG_CONNECTED",
  "description": "The vehicle is connected to an EV charger and unable to perform your request.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/vehicle-state-errors#charging-plug-connected",
  "statusCode": 409,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null },
  "suggestedUserMessage": "We’re unable to issue the command because the vehicle is currently plugged in."
}
```

### Suggested resolution

The user can resolve this error by unplugging the vehicle.

### Suggested user message

> We're unable to issue the command because the vehicle is currently plugged in. Please ensure that you have unplugged the vehicle from an EV charger.

***

# `CHARGING_PLUG_NOT_CONNECTED`

The vehicle is not connected to an EV charger and unable to perform your request. This error usually occurs when you make a request to the start charge endpoint
but the vehicle’s charge port does not have an EV charger plugged into it.

If testing an electric vehicle with Vehicle Simulator, you will receive this error when attempting a start or stop charge request while the vehicle is in a parked
or driving state (not charging).

```json  theme={null}
{
  "type": "VEHICLE_STATE",
  "code": "CHARGING_PLUG_NOT_CONNECTED",
  "description": "The vehicle is not connected to an EV charger and unable to perform your request.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/vehicle-state-errors#charging-plug-not-connected",
  "statusCode": 409,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null },
  "suggestedUserMessage": "Your vehicle is not plugged in."
}
```

### Suggested resolution

The user can resolve this error by plugging an EV charger into the vehicle’s charge port.

### Troubleshooting Steps

* Prompt the user to plug an EV charger into the vehicle’s charge port.
* If this doesn’t resolve the issue, prompt the user to ensure that the EV charger is connected to a working power source, that it isn’t faulty, and that it is compatible with the user’s vehicle. For example, prompt the user to try out other EV chargers and to check the vehicle’s owner manual for a list of compatible chargers.

### Suggested user message

> Your car isn’t able to start charging. Please ensure that you have plugged an EV charger into your car’s charge port.

***

# `DOOR_OPEN`

The vehicle could not perform your request because one or more of its doors are open. This error usually occurs when you make a request to the lock endpoint while one or more of the vehicle’s doors stand open.

```json  theme={null}
{
  "type": "VEHICLE_STATE",
  "code": "DOOR_OPEN",
  "description": "The vehicle could not perform your request because one or more of its doors are open.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/vehicle-state-errors#door-open",
  "statusCode": 409,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null },
  "suggestedUserMessage": "Your vehicle was unable to lock. Please ensure that all doors and the trunk are fully closed."
}
```

### Suggested resolution

The user can resolve this error by fully closing all of the vehicle’s doors and the trunk.

### Troubleshooting Steps

* Prompt the user to ensure that there is nothing preventing the doors from fully closing and/or locking properly.
* Prompt the user to ensure that the vehicle’s trunk is fully closed.

### Suggested user message

> Your car was unable to lock. Please ensure that all doors and the trunk are fully closed.

***

# `FULLY_CHARGED`

The vehicle is unable to perform your request because its EV battery is fully charged. This error usually occurs when you make a request to the start charge endpoint while the vehicle is already fully charged.

```json  theme={null}
{
  "type": "VEHICLE_STATE",
  "code": "FULLY_CHARGED",
  "description": "The vehicle is unable to perform your request because its EV battery is fully charged.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/vehicle-state-errors#fully-charged",
  "statusCode": 409,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null },
  "suggestedUserMessage": "Your vehicle is already fully charged."
}
```

### Suggested user message

> Your car is already fully charged.

***

# `NOT_CHARGING`

The vehicle is unable to perform your request because it is not currently charging. This error usually occurs when you request information about a vehicle’s charge session while the battery is not charging.

```json  theme={null}
{
  "type": "VEHICLE_STATE",
  "code": "NOT_CHARGING",
  "description": "The vehicle is unable to perform your request because it is not currently charging.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/vehicle-state-errors#not-charging",
  "statusCode": 409,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null },
  "suggestedUserMessage": "Please ensure that you have plugged an EV charger into your car’s charge port and the vehicle is charging."
}
```

### Suggested resolution

You can resolve this error by having the user start a charge session or by sending a start charge request if the vehicle supports that capability.

### Troubleshooting Steps

* Prompt the user to start charging their vehicle.
* Wait for a few minutes and retry your request.

### Suggested user message

> Please ensure that you have plugged an EV charger into your car’s charge port and the vehicle is charging.

***

# `CHARGE_FAULT`

The vehicle is connected to an EV charger but cannot perform the request because:

* the charger is not providing any current
* there is a conflict with another charging schedule

```json  theme={null}
{
  "type": "VEHICLE_STATE",
  "code": "CHARGE_FAULT",
  "description": "The vehicle is connected to an EV charger but cannot perform the request because 1) the charger is not providing any current, or 2) there is a conflict with another charging schedule.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/vehicle-state-errors#charge-fault",
  "statusCode": 409,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null },
  "suggestedUserMessage": "Your vehicle is unable to start or stop charging because of a conflict with the vehicle's charging schedule."
}
```

### Suggested resolution

The user can resolve this error by:

* Disabling any schedules that control when the charger can supply current and charge the vehicle.
* Ensuring that the charging cable is securely connected to the vehicle.
* Disabling any charge schedules on the vehicle’s infotainment system or connected service application.
* Disabling any departure timers on the vehicle’s infotainment system or connected service application.
* Removing the vehicle from other charge scheduling services.

### Troubleshooting Steps

* Prompt the user to start charging their vehicle.
* Wait for a few minutes and retry your request.

### Suggested user message

> Your car is unable to start or stop charging because of a conflict with your vehicle’s charging schedule. Please check that:
>
> * You have disabled any schedules that control when your charger is able to supply current to and charge the vehicle.
> * The charging cable is securely connected to your vehicle.
> * You have disabled any charge schedules on your vehicle’s infotainment system or connected service application.
> * You have disabled any departure timers on your vehicle’s infotainment system or connected service application.
> * Your vehicle is not connected to any other charge scheduling services.

***

# `HOOD_OPEN`

The vehicle is unable to perform your request because its hood is open. This error usually occurs when you make a request to the lock endpoint while the vehicle’s hood stands open.

```json  theme={null}
{
  "type": "VEHICLE_STATE",
  "code": "HOOD_OPEN",
  "description": "The vehicle is unable to perform your request because its hood is open.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/vehicle-state-errors#hood-open",
  "statusCode": 409,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null },
  "suggestedUserMessage": "Your vehicle was unable to lock. Please ensure that the vehicle's hood is fully closed."
}
```

### Suggested resolution

The user can resolve this error by ensuring that the vehicle’s hood is fully closed.

### Suggested user message

> Your car was unable to lock. Please ensure that your car’s hood is fully closed.

***

# `IGNITION_ON`

The vehicle was unable to perform your request because its engine is running. Depending on the vehicle’s make and model, this error can occur for a variety of API endpoints.

```json  theme={null}
{
  "type": "VEHICLE_STATE",
  "code": "IGNITION_ON",
  "description": "The vehicle was unable to perform your request because its engine is running.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/vehicle-state-errors#ignition-on",
  "statusCode": 409,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null },
  "suggestedUserMessage": "Your vehicle is currently running."
}
```

### Suggested resolution

The user can resolve this error by turning off their vehicle. You can also resolve this error by retrying your request at a later time.

### Suggested user message

> Your car is temporarily unable to connect to \<app name> because its engine is running. To re-establish the connection, please turn off your car’s engine.

***

# `IN_MOTION`

The vehicle is currently in motion and unable to perform your request. Depending on the vehicle’s make and model, this error can occur for a variety of API endpoints. The lock/unlock endpoint is a common example.

If testing with Vehicle Simulator, you will receive this error when attempting a lock/unlock request while the vehicle is in a driving state along the simulation.

```json  theme={null}
{
  "type": "VEHICLE_STATE",
  "code": "IN_MOTION",
  "description": "The vehicle is currently in motion and unable to perform your request.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/vehicle-state-errors#in-motion",
  "statusCode": 409,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null },
  "suggestedUserMessage": "Your vehicle is unable to perform the request while in motion."
}
```

### Suggested resolution

The user can resolve this error by parking their car and turning off the engine. You can also resolve this error by retrying your request at a later time.

### Suggested user message

> Your car is in motion and temporarily unable to connect to \<app name>. To re-establish the connection, please park your car and turn off its engine.

***

# `REMOTE_ACCESS_DISABLED`

The vehicle is unable to perform your request because the user has disabled remote access for connected services.

```json  theme={null}
{
  "type": "VEHICLE_STATE",
  "code": "REMOTE_ACCESS_DISABLED",
  "description": "The vehicle is unable to perform your request because the user has disabled remote access for connected services.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/vehicle-state-errors#remote-access-disabled",
  "statusCode": 409,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null },
  "suggestedUserMessage": "Your vehicle is unable to perform the request as remote access is disabled or unavailable."
}
```

### Suggested resolution

The user can resolve this error by re-enabling remote access inside their vehicle. If the user is unsure how to enable remote access for connected services, prompt them to refer to their vehicle’s owner manual for more details.

### Suggested user message

> Your car is temporarily unable to connect to \<app name>. To re-establish the connection, please make sure that remote access for connected services is enabled inside your car. Please refer to your car’s owner manual for more details.

***

# `TRUNK_OPEN`

The vehicle is unable to perform your request because its trunk is open. This error usually occurs when you make a request to the lock endpoint while the vehicle’s trunk and/or front trunk are open.

```json  theme={null}
{
  "type": "VEHICLE_STATE",
  "code": "TRUNK_OPEN",
  "description": "The vehicle is unable to perform your request because its trunk is open.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/vehicle-state-errors#trunk-open",
  "statusCode": 409,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null },
  "suggestedUserMessage": "Your vehicle was unable to open the trunk because it is already open."
}
```

### Suggested resolution

The user can resolve this error by closing the vehicle’s trunk and/or front trunk.

### Suggested user message

> Your car was unable to lock. Please ensure that your car’s trunk (and front trunk) is closed.

***

# `UNKNOWN`

The vehicle was unable to perform your request due to an unknown issue. This error occurs when the vehicle is in a state that makes it unable to perform your request, and we are unable to determine which state the vehicle is in.

If testing an electric vehicle with Vehicle Simulator, you will receive this error when attempting a stop charge request while the vehicle is in a charging state.

```json  theme={null}
{
  "type": "VEHICLE_STATE",
  "code": "UNKNOWN",
  "description": "The vehicle was unable to perform your request due to an unknown issue.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/vehicle-state-errors#unknown",
  "statusCode": 409,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": "RETRY_LATER" },
  "suggestedUserMessage": "Your vehicle is temporarily unable to connect due to an unknown issue. Please be patient while we’re working to resolve this issue."
}
```

### Suggested resolution

Please retry your request at a later time.

### Suggested user message

> Your car is temporarily unable to connect to \<app name>. Please be patient while we’re working to resolve this issue.

***

# `UNREACHABLE`

The vehicle was unable to perform your request because it is currently unreachable. This error usually occurs when the vehicle is in a location with poor cellular reception (e.g. a parking garage or underground parking).

If testing with Vehicle Simulator, you will receive this error when attempting a lock/unlock or start/stop charge request while the simulation is paused or completed.

```json  theme={null}
{
  "type": "VEHICLE_STATE",
  "code": "UNREACHABLE",
  "description": "The vehicle was unable to perform your request because it is currently unreachable.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/vehicle-state-errors#unreachable",
  "statusCode": 409,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null },
  "suggestedUserMessage": "Your vehicle is currently unreachable. Ensure the vehicle has adequate mobile coverage."
}
```

### Suggested resolution

The user can resolve this error by moving the vehicle to a location with better cellular reception. You can also resolve this error by retrying your request at a later time.

### Suggested user message

> Your car is temporarily unable to connect to \<app name>. To re-establish the connection, please move your car to a location with a better cell phone signal.

***

# `VEHICLE_OFFLINE_FOR_SERVICE`

The vehicle was unable to perform your request because it is currently in service mode. Service mode temporarily limits or disables the vehicle’s remote capabilities.

```json  theme={null}
{
  "type": "VEHICLE_STATE",
  "code": "VEHICLE_OFFLINE_FOR_SERVICE",
  "description": "The vehicle was unable to perform your request because it is currently in service mode.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/vehicle-state-errors#vehicle-offline-for-service",
  "statusCode": 409,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null },
  "suggestedUserMessage": "Your vehicle is in service mode and temporarily unable to perform this task."
}
```

### Suggested resolution

Please retry your request at a later time.

### Suggested user message

> Your car is in service mode and temporarily unable to connect to \<app name>. Please try again later.

***

# `LOW_BATTERY`

The vehicle was unable to perform your request because the 12v or high voltage battery is too low.

```json  theme={null}
{
  "type": "VEHICLE_STATE",
  "code": "LOW_BATTERY",
  "description": "The vehicle was unable to perform your request because the 12v or high voltage battery is too low.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/vehicle-state-errors#low-battery",
  "statusCode": 409,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": "RETRY_LATER" },
  "suggestedUserMessage": "Your vehicle battery is too low to perform this task."
}
```

### Suggested resolution

Please retry your request at a later time.

* For EVs ensure that the battery is topped up to at least 60% SoC.
* Ensure that the vehicle’s 12-volt battery is sufficiently charged. Taking the vehicle on a short drive can help.

### Suggested user message

> \<app name> was unable to connect to your car because its battery is too low. Please ensure the battery is charged and try again later.

***


# Access Denied
Source: https://smartcar.com/docs/errors/connect-errors/access-denied

This error occurs when a user denies your application access to the requested scope of permissions.

| Parameter           | Required | Description                        |
| ------------------- | -------- | ---------------------------------- |
| `error`             | `true`   | `access_denied`                    |
| `error_description` | `true`   | User denied access to application. |

```http Example redirect uri theme={null}
HTTP/1.1 302 Found
Location: https://example.com/home
?error=access_denied
&error_description=User+denied+access+to+application
```

## Testing

To test this error, launch Smartcar Connect in test mode and select “Deny access” on the permissions screen.

<Frame caption="Access Denied">
  <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/access_denied.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=b45ddc2c280b865a3771507961d5ca39" data-og-width="1275" width="1275" data-og-height="773" height="773" data-path="images/api-reference/access_denied.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/access_denied.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=b97ec8e6693eabba309af544dda4c7de 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/access_denied.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=77c637f8151eda1513b07e61b78f5eab 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/access_denied.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=5580026d6dc60cba5a07ad7226232387 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/access_denied.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=df87b9ccfe523517f78519dc0deaa9d6 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/access_denied.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=897b2604624fc2b93a72870dd10a1f31 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/access_denied.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=3f1c8bdcd7945574102fbda9d1d58507 2500w" />
</Frame>

We recommend handling this error by re-prompting the user to authorize their vehicle and adding a message like in the example below.

<Frame caption="Access Denied Message">
  <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/access_denied_message.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=844e2501b98ecbb86634f85e969e9499" data-og-width="1275" width="1275" data-og-height="775" height="775" data-path="images/api-reference/access_denied_message.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/access_denied_message.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=e61896e9355dd35847c69b49d7625d68 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/access_denied_message.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=5eb24ca7748ca2ffdb7b6a5cfaccd480 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/access_denied_message.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=84e88aba94b6b918e11af0112ba4a2e3 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/access_denied_message.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=bca717e762619039ea2c9144b85242f2 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/access_denied_message.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=ef18bbc6c88ec00f2bccbc6a47cb1691 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/access_denied_message.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=1ac814add89245e26defb2a4337b9996 2500w" />
</Frame>


# Configuration
Source: https://smartcar.com/docs/errors/connect-errors/configuration-error

This error occurs when the user has encountered an Error page in Connect and has chosen to return to your application.

| Parameter           | Required | Description                                                       |
| ------------------- | -------- | ----------------------------------------------------------------- |
| `error`             | `true`   | `configuration_error`                                             |
| `error_description` | `true`   | There has been an error in the configuration of your application. |
| `status_code`       | `true`   | The status code of the error encountered in Connect               |
| `error_message`     | `true`   | The error message seen by the user                                |

```http Example redirect uri theme={null}
HTTP/1.1 302 Found
Location: https://example.com/callback
?error=configuration_error
&error_description=There%20has%20been%20an%20error%20in%20the%20configuration%20of%20your%20application.&status_code=400
&error_message=You%20have%20entered%20a%20test%20mode%20VIN.%20Please%20enter%20a%20VIN%20that%20belongs%20to%20a%20real%20vehicle.
```

On redirect, Connect will return the status code and message of the error that they encountered. This will be triggered if:

* A user tried to directly navigate to a page that is past their current step in Connect (ie. going directly from the Preamble screen to the Permission Grants screen by directly going to connect.smartcar.com/grant).
* A user is trying to use Single Select in live mode with a test mode VIN or with a simulated VIN in a non-simulated mode.
* A user is trying to use Single Select with an invalid mock VIN.
* A validation error occurs when trying to check compatibility by VIN.

These cases will trigger the following error and give the user the ability to “Exit” Connect.

<Frame caption="Error Page">
  <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/error_page.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=69b4a1e91f6223798b03ed57e696f9e8" data-og-width="457" width="457" data-og-height="590" height="590" data-path="images/api-reference/error_page.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/error_page.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=2f208da34113d1c7b21406c00c7555c3 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/error_page.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=f93e888a88c515ed8f83b69754db53e2 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/error_page.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=1afc3e47c727f6526a9bf22bdaf56e10 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/error_page.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=fac59069a414dfd5d4f87795f08c138e 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/error_page.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=12945d56509b0cb91d6d51609f60be57 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/error_page.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=f6fcac1b5d72e1e32ed4281b7c645187 2500w" />
</Frame>


# Invalid Subscription
Source: https://smartcar.com/docs/errors/connect-errors/invalid-subscription

This error occurs when a user’s vehicle is compatible but their connected services subscription is inactive because either it has expired or it has never been activated.

| Parameter          | Required | Description                                                  |   |
| ------------------ | -------- | ------------------------------------------------------------ | - |
| error              | true     | invalid\_subscription                                        |   |
| error\_description | true     | User does not have an active connected vehicle subscription. |   |

```http Example redirect uri theme={null}
HTTP/1.1 302 Found
Location: https://example.com/callback
?error=invalid_subscription
&error_description=User%20does%20not%20have%20an%20active%20connected%20vehicle%20subscription
```

Smartcar will direct the user to the connected services website to (re-)activate their subscription. However, a user may choose to return back to your application instead, like in the example below.

<Frame caption="No Subscription">
  <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/no_subscription.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=afd7635f3f21192d982b66bbe823f217" data-og-width="1275" width="1275" data-og-height="774" height="774" data-path="images/api-reference/no_subscription.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/no_subscription.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=e1a56a41389ab618dc64d3df3494d360 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/no_subscription.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=830d21e11f453eaec9fcd3f7f8fa0666 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/no_subscription.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=626c6922cf2c384cf8d9b81f9fed33ae 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/no_subscription.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=66532b981cf306ba4f55387aeb11095b 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/no_subscription.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=1e9c50d30adffc8a5a02409b30b32756 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/no_subscription.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=28ae13b73828f13f9b6ae7060e795dd9 2500w" />
</Frame>

## Testing

To test this error, launch Smartcar Connect in test mode and log in with the email [smartcar@invalid-subscription.com](mailto:smartcar@invalid-subscription.com) and any password. If you use Single Select, please see the table below for a simulated VIN.

| Email                                                                         | VIN               |
| ----------------------------------------------------------------------------- | ----------------- |
| [smartcar@invalid-subscription.com](mailto:smartcar@invalid-subscription.com) | 0SCAUDI0155C49A95 |

In the event of an `AUTHENTICATION_FAILED`, the user will need to be prompted to re-connect their vehicle. Smartcar Connect Re-authentication makes the process of re-authenticating a user much more seamless. In addition, the `AUTHENTICATION_FAILED` error provides a partially constructed URL for the re-authentication flow inside the resolution object.


# No Vehicles
Source: https://smartcar.com/docs/errors/connect-errors/no-vehicles

This error occurs when a vehicle owner has a connected services account, but there are no vehicles associated with the account.

| Parameter          | Required | Description                                                  |   |
| ------------------ | -------- | ------------------------------------------------------------ | - |
| error              | true     | no\_vehicles                                                 |   |
| error\_description | true     | User does not have an active connected vehicle subscription. |   |

```http Example redirect uri theme={null}
HTTP/1.1 302 Found
Location: https://example.com/callback
?error=no_vehicles&error_description=No%20vehicles%20found.%20Please%20add%20vehicles%20to%20your%20account%20and%20try%20again.
```

The error is triggered when a user logs into their connected services account and is shown to have no vehicles listed like in the example below for BMW.

<Frame caption="No Vehicle Error">
  <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/no_vehicle_error.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=903fa8967ececee46d63b6f1c6aac5e0" data-og-width="455" width="455" data-og-height="478" height="478" data-path="images/api-reference/no_vehicle_error.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/no_vehicle_error.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=a96f4ec8480911f6e7d7027eb49b6d87 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/no_vehicle_error.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=ee814a28e518096eee6fcde00cded710 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/no_vehicle_error.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=998aadc98e9937aad55104a36b43af3b 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/no_vehicle_error.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=9d7cdaaadbac395ee86c112b98465a1d 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/no_vehicle_error.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=c938e037f052aee494e360ac3f2c3bb4 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/no_vehicle_error.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=d5df8eda25c97ae8c89e8d931ff5a00c 2500w" />
</Frame>

The user has the option to add vehicles or return to your application.


# OEM Login Cancelled
Source: https://smartcar.com/docs/errors/connect-errors/oem-login-cancelled

This error occurs when a user went to authorize directly with the OEM but exited the flow for some reason.

| Parameter           | Required | Description                                          |
| ------------------- | -------- | ---------------------------------------------------- |
| `error`             | `true`   | `oem_cancelled_login`                                |
| `error_description` | `true`   | The user did not complete authorization with the OEM |

```http Example redirect uri theme={null}
HTTP/1.1 302 Found
Location: https://example.com/callback
?error=oem_cancelled_login
&the%20user%20did%20not%20complete%20authorization%20with%20the%20OEM
```

<Frame caption="OEM Login Cancelled">
  <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/oem-cancelled.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=809144a9de87c60d807cf552236babe0" data-og-width="1322" width="1322" data-og-height="1121" height="1121" data-path="images/errors/connect-errors/oem-cancelled.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/oem-cancelled.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=365a81c051c9bc890a80f803fae14d48 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/oem-cancelled.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=2ac28f3a48cdefcf6415c375ceaa2f9d 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/oem-cancelled.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=c2cb8000dd88ea6342d1ad83d9084c63 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/oem-cancelled.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=e1e21a85d978104ec6045741ea779acd 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/oem-cancelled.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=2f8500289efa26329c16d1c64aee9d4f 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/oem-cancelled.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=642123a43b235fe9a5862255bc5a2b2b 2500w" />
</Frame>


# User returned to application
Source: https://smartcar.com/docs/errors/connect-errors/returned-to-application

This error occurs when a user leaves the Connect flow after hitting **Back to application** before granting your application access to their vehicle.

| Parameter           | Required | Description                                                     |
| ------------------- | -------- | --------------------------------------------------------------- |
| `error`             | `true`   | `user_manually_returned_to_application`                         |
| `error_description` | `true`   | The user exited Connect before granting your application access |

There are cases where a user may wish to exit Connect before granting your application access to their vehicle. In these cases, if the user hits **Back to application** instead of closing out the window, Smartcar will return this error to your callback URI. Below are places in the Connect flow users can return to your application.

<Tabs>
  <Tab title="Missing Permissions">
    <Frame caption="Vehicle Incompatible">
      <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/r2a-additional-permissions.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=caf4655b12fd4622a2388b729cef6062" data-og-width="750" width="750" data-og-height="1334" height="1334" data-path="images/errors/connect-errors/r2a-additional-permissions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/r2a-additional-permissions.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=7cf587cf7e0c1b2cba08681729975d9e 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/r2a-additional-permissions.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=b94ebb2859f7703254342641165a2d7c 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/r2a-additional-permissions.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=13387fa92a3ac36533ddaab14c3af732 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/r2a-additional-permissions.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=902b6cccab69e580117ea816dcb6d204 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/r2a-additional-permissions.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=58179df631724a774f59bc7b98dbb47c 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/r2a-additional-permissions.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=7c40443504cd03750b11751769993a57 2500w" />
    </Frame>
  </Tab>

  <Tab title="MFA Entry">
    <Frame caption="Vehicle Incompatible">
      <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/r2a-mfa-entry.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=24d212a190bb5054eab9c1e83b45de2a" data-og-width="750" width="750" data-og-height="1334" height="1334" data-path="images/errors/connect-errors/r2a-mfa-entry.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/r2a-mfa-entry.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=4323baa7ecf4a9fa7e5971757b3e5dee 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/r2a-mfa-entry.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=ff92419e74ba4365700a712145ae1eac 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/r2a-mfa-entry.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=12451d2285e032eba9906d29562ef065 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/r2a-mfa-entry.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=ebb517ebff6f72c834d4a4e238aa36b6 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/r2a-mfa-entry.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=18561fd163d8e8d3358b966139d99ca4 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/r2a-mfa-entry.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=74115eb37105c0e0ab92e9e08a1d9666 2500w" />
    </Frame>
  </Tab>

  <Tab title="PIN Entry">
    <Frame caption="Vehicle Incompatible">
      <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/r2a-pin-entry.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=e746980cc79f0b5c73184434ff772f0f" data-og-width="750" width="750" data-og-height="1334" height="1334" data-path="images/errors/connect-errors/r2a-pin-entry.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/r2a-pin-entry.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=ffea845ea4f7aa0c0790939bd2335c21 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/r2a-pin-entry.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=66528ca361146aa98f3178ab2b9edf65 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/r2a-pin-entry.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=30d5044e008af730f9de6961af43f6eb 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/r2a-pin-entry.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=d71c7eb73761877c3c13b9343620d98f 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/r2a-pin-entry.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=19679505e4bb06522befd9e37e76a502 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/r2a-pin-entry.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=f2c2ce4edec0b6c34d14575bab4d0d18 2500w" />
    </Frame>
  </Tab>
</Tabs>


# Server
Source: https://smartcar.com/docs/errors/connect-errors/server-error

If there is a server error, the user will return to your application.

| Parameter          | Required | Description                                |
| ------------------ | -------- | ------------------------------------------ |
| error              | true     | server\_error                              |
| error\_description | true     | Unexpected server error. Please try again. |

```http Example redirect uri theme={null}
HTTP/1.1 302 Found
Location: https://example.com/callback
?error=configuration_error
&error_description=There%20has%20been%20an%20error%20in%20the%20configuration%20of%20your%20application.&status_code=400
&error_message=You%20have%20entered%20a%20test%20mode%20VIN.%20Please%20enter%20a%20VIN%20that%20belongs%20to%20a%20real%20vehicle.
```

<Note>
  We only show the “Exit” button if a redirect URI is available. If there is a failure before the validation of the redirect URI,  we are unable to include the “Exit” button on the Error page. In those cases, we would not be able to report the `status_code` and `error_message` back to the developer, but they will still be available on screen in the Error page.
</Note>

<Frame caption="Server Error">
  <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/server-error.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=94b0f9f1020d0dcd1156754de31c4231" data-og-width="2000" width="2000" data-og-height="1602" height="1602" data-path="images/errors/connect-errors/server-error.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/server-error.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=9d225822dd6024c1cac4ada2250c45d9 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/server-error.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=d929cb64c48fecfae38c9f35ef9132d9 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/server-error.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=874e0804fd145ee9fb5cffc370cd0afd 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/server-error.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=6ca984de7807d5d6f2a225f1640375d6 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/server-error.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=5d3c20c1d070c54d543058fd4797951b 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/server-error.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=04f572a9df9d09c7c47979dc06bee0f0 2500w" />
</Frame>


# Vehicle Incompatible
Source: https://smartcar.com/docs/errors/connect-errors/vehicle-incompatible

This error occurs when a user tries to authorize an incompatible vehicle in Smartcar Connect.

| Parameter           | Required | Description                           |
| ------------------- | -------- | ------------------------------------- |
| `error`             | `true`   | `vehicle_incompatible`                |
| `error_description` | `true`   | The user’s vehicle is not compatible. |
| `make`              | `false`  | The manufacturer of the vehicle.      |
| `vin`               | `false`  | The VIN of the vehicle.               |

In order to be compatible, a vehicle must:

* Have the hardware required for internet connectivity
* Belong to the makes and models Smartcar is compatible with
* Be capable of the required permissions that your application is requesting access to
* If the user’s vehicle is incompatible, Smartcar will let the user know and offer them to share their vehicle’s VIN, make, model, and year with your application.

This error is triggered when a user selects an unspported make, or selects "I don't see my brand..." and then hits "Back to application"

<Frame caption="Vehicle Incompatible">
  <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/vehicle-incompatible.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=0490adb032508a9965758ab02c26cd29" data-og-width="2643" width="2643" data-og-height="1472" height="1472" data-path="images/errors/connect-errors/vehicle-incompatible.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/vehicle-incompatible.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=4d6f086ca74d32d88ccd37991392679c 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/vehicle-incompatible.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=0ce9294c9716e4f64008d1c22305b363 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/vehicle-incompatible.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=e082e76f4139fbbe58199d68373f3a4d 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/vehicle-incompatible.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=8bdde4128b6703822e6614c214ccd8e1 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/vehicle-incompatible.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=97adb5491804bc5589800448937d8491 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/vehicle-incompatible.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=c90da19a6ad6ceebe5bdad7963ff051c 2500w" />
</Frame>

We recommend that your application provides a flow for incompatible vehicles like in the example below.

<Frame caption="Vehicle Incompatible">
  <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/vehicle_incompatible.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=004f2159102e0d0c756b2eeeff08fcec" data-og-width="1275" width="1275" data-og-height="774" height="774" data-path="images/api-reference/vehicle_incompatible.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/vehicle_incompatible.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=1d42a9b16af715d5479263ebef9d3806 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/vehicle_incompatible.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=c43ba0468743922e945d8a0dc5579b1b 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/vehicle_incompatible.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=362847a86983a35cb81c0228987893eb 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/vehicle_incompatible.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=61f4dc4a21af5f1a7d73ec095e95c28f 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/vehicle_incompatible.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=3ba9a62f4c6e9c36c9d2fcde981d6225 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/api-reference/vehicle_incompatible.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=1aa0e0fa04a5f90a5c3af5fafb7badd2 2500w" />
</Frame>

<br />

<Info>
  Note: This error will never occur if your application uses the Compatibility API. The Compatibility API verifies the compatibility of a vehicle before the user enters Smartcar Connect.
</Info>

To test this error, launch Smartcar Connect in test mode and log in with the email [smartcar@vehicle-incompatible.com](mailto:smartcar@vehicle-incompatible.com) and any password.

If you use Single Select, please see the table below for a simulated VIN.

| Email                                                                         | VIN               |
| ----------------------------------------------------------------------------- | ----------------- |
| [smartcar@vehicle-incompatible.com](mailto:smartcar@vehicle-incompatible.com) | 0SCAUDI012FE3B132 |


# Testing Errors
Source: https://smartcar.com/docs/errors/testing-errors

By launching Connect in [simulated mode](/docs/connect/advanced-config/modes), you're able to test your application against certain errors.

## Testing Connect Errors

You can use the following emails to test a subset of Connect errors:

| Error                  | Email                                                                         | VIN               |
| ---------------------- | ----------------------------------------------------------------------------- | ----------------- |
| `invalid_subscription` | [smartcar@invalid-subscription.com](mailto:smartcar@invalid-subscription.com) | 0SCAUDI0155C49A95 |
| `vehicle_incompatible` | [smartcar@vehicle-incompatible.com](mailto:smartcar@vehicle-incompatible.com) | 0SCAUDI012FE3B132 |

Visit the [Connect Errors](/api-reference/api-errors#connect-errors) page for more details.

## Testing API Errors

You can use use the following emails to test these API error types:

* `COMPATIBILITY`
* `CONNECTED_SERVICES_ACCOUNT`
* `UPSTREAM`
* `VEHICLE_STATE`

| Type                         | Code                          | Email                                                                                                                                    | VIN               |
| ---------------------------- | ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| `COMPATIBILITY`              | `MAKE_NOT_COMPATIBLE`         | [COMPATIBILITY.MAKE\_NOT\_COMPATIBLE@smartcar.com](mailto:COMPATIBILITY.MAKE_NOT_COMPATIBLE@smartcar.com)                                | 0SCLR000270BE6600 |
| `COMPATIBILITY`              | `SMARTCAR_NOT_CAPABLE`        | [COMPATIBILITY.SMARTCAR\_NOT\_CAPABLE@smartcar.com](mailto:COMPATIBILITY.SMARTCAR_NOT_CAPABLE@smartcar.com)                              | 0SCLR0002DC18F57F |
| `COMPATIBILITY`              | `VEHICLE_NOT_CAPABLE`         | [COMPATIBILITY.VEHICLE\_NOT\_CAPABLE@smartcar.com](mailto:COMPATIBILITY.VEHICLE_NOT_CAPABLE@smartcar.com)                                | 0SCLR00024C7CDF7A |
| `CONNECTED_SERVICES_ACCOUNT` | `ACCOUNT_ISSUE`               | [CONNECTED\_SERVICES\_ACCOUNT.ACCOUNT\_ISSUE@smartcar.com](mailto:CONNECTED_SERVICES_ACCOUNT.ACCOUNT_ISSUE@smartcar.com)                 | 0SCLR00026BAAA136 |
| `CONNECTED_SERVICES_ACCOUNT` | `AUTHENTICATION_FAILED`       | [CONNECTED\_SERVICES\_ACCOUNT.AUTHENTICATION\_FAILED@smartcar.com](mailto:CONNECTED_SERVICES_ACCOUNT.AUTHENTICATION_FAILED@smartcar.com) | 0SCLR00021D803C7B |
| `CONNECTED_SERVICES_ACCOUNT` | `NO_VEHICLES`                 | [CONNECTED\_SERVICES\_ACCOUNT.NO\_VEHICLES@smartcar.com](mailto:CONNECTED_SERVICES_ACCOUNT.NO_VEHICLES@smartcar.com)                     | 0SCLR00027671837B |
| `CONNECTED_SERVICES_ACCOUNT` | `SUBSCRIPTION`                | [CONNECTED\_SERVICES\_ACCOUNT.SUBSCRIPTION@smartcar.com](mailto:CONNECTED_SERVICES_ACCOUNT.SUBSCRIPTION@smartcar.com)                    | 0SCLR0002B9BAF29F |
| `CONNECTED_SERVICES_ACCOUNT` | `VEHICLE_MISSING`             | [CONNECTED\_SERVICES\_ACCOUNT.VEHICLE\_MISSING@smartcar.com](mailto:CONNECTED_SERVICES_ACCOUNT.VEHICLE_MISSING@smartcar.com)             | 0SCLR00024E29EEBD |
| `UPSTREAM`                   | `INVALID_DATA`                | [UPSTREAM.INVALID\_DATA@smartcar.com](mailto:UPSTREAM.INVALID_DATA@smartcar.com)                                                         | 0SCLR000298A0A649 |
| `UPSTREAM`                   | `KNOWN_ISSUE`                 | [UPSTREAM.KNOWN\_ISSUE@smartcar.com](mailto:UPSTREAM.KNOWN_ISSUE@smartcar.com)                                                           | 0SCLR0002A8760B72 |
| `UPSTREAM`                   | `NO_RESPONSE`                 | [UPSTREAM.NO\_RESPONSE@smartcar.com](mailto:UPSTREAM.NO_RESPONSE@smartcar.com)                                                           | 0SCLR0002C23E43AB |
| `UPSTREAM`                   | `UNKNOWN_ISSUE`               | [UPSTREAM.UNKNOWN\_ISSUE@smartcar.com](mailto:UPSTREAM.UNKNOWN_ISSUE@smartcar.com)                                                       | 0SCLR0002D4878901 |
| `VEHICLE_STATE`              | `ASLEEP`                      | [VEHICLE\_STATE.ASLEEP@smartcar.com](mailto:VEHICLE_STATE.ASLEEP@smartcar.com)                                                           | 0SCLR0002E8896323 |
| `VEHICLE_STATE`              | `CHARGING_IN_PROGRESS`        | [VEHICLE\_STATE.CHARGING\_IN\_PROGRESS@smartcar.com](mailto:VEHICLE_STATE.CHARGING_IN_PROGRESS@smartcar.com)                             | 0SCLR000221F1E672 |
| `VEHICLE_STATE`              | `CHARGING_PLUG_NOT_CONNECTED` | [VEHICLE\_STATE.CHARGING\_PLUG\_NOT\_CONNECTED@smartcar.com](mailto:VEHICLE_STATE.CHARGING_PLUG_NOT_CONNECTED@smartcar.com)              | 0SCLR0002CBFC7C21 |
| `VEHICLE_STATE`              | `DOOR_OPEN`                   | [VEHICLE\_STATE.DOOR\_OPEN@smartcar.com](mailto:VEHICLE_STATE.DOOR_OPEN@smartcar.com)                                                    | 0SCLR0002F8BD90B8 |
| `VEHICLE_STATE`              | `FULLY_CHARGED`               | [VEHICLE\_STATE.FULLY\_CHARGED@smartcar.com](mailto:VEHICLE_STATE.FULLY_CHARGED@smartcar.com)                                            | 0SCLR00029CD9D894 |
| `VEHICLE_STATE`              | `HOOD_OPEN`                   | [VEHICLE\_STATE.HOOD\_OPEN@smartcar.com](mailto:VEHICLE_STATE.HOOD_OPEN@smartcar.com)                                                    | 0SCLR000219CD4A2C |
| `VEHICLE_STATE`              | `IGNITION_ON`                 | [VEHICLE\_STATE.IGNITION\_ON@smartcar.com](mailto:VEHICLE_STATE.IGNITION_ON@smartcar.com)                                                | 0SCLR00021D49E58A |
| `VEHICLE_STATE`              | `IN_MOTION`                   | [VEHICLE\_STATE.IN\_MOTION@smartcar.com](mailto:VEHICLE_STATE.IN_MOTION@smartcar.com)                                                    | 0SCLR00024F6EE640 |
| `VEHICLE_STATE`              | `REMOTE_ACCESS_DISABLED`      | [VEHICLE\_STATE.REMOTE\_ACCESS\_DISABLED@smartcar.com](mailto:VEHICLE_STATE.REMOTE_ACCESS_DISABLED@smartcar.com)                         | 0SCLR0002588A5CC1 |
| `VEHICLE_STATE`              | `TRUNK_OPEN`                  | [VEHICLE\_STATE.TRUNK\_OPEN@smartcar.com](mailto:VEHICLE_STATE.TRUNK_OPEN@smartcar.com)                                                  | 0SCLR00023C607FDB |
| `VEHICLE_STATE`              | `UNKNOWN`                     | [VEHICLE\_STATE.UNKNOWN@smartcar.com](mailto:VEHICLE_STATE.UNKNOWN@smartcar.com)                                                         | 0SCLR0002E6CC0314 |
| `VEHICLE_STATE`              | `UNREACHABLE`                 | [VEHICLE\_STATE.UNREACHABLE@smartcar.com](mailto:VEHICLE_STATE.UNREACHABLE@smartcar.com)                                                 | 0SCLR000247EBF067 |
| `VEHICLE_STATE`              | `VEHICLE_OFFLINE_FOR_SERVICE` | [VEHICLE\_STATE.VEHICLE\_OFFLINE\_FOR\_SERVICE@smartcar.com](mailto:VEHICLE_STATE.VEHICLE_OFFLINE_FOR_SERVICE@smartcar.com)              | 0SCLR0002AF1D71A1 |


# Configure Your Application
Source: https://smartcar.com/docs/getting-started/configure-application

Learn how to configure your Smartcar application, including setting up permissions and redirect URIs.

Once you have registered your application in the [Smartcar Dashboard](https://dashboard.smartcar.com), you can configure it to suit your business needs.

## Application Configuration Overview

Your application configuration includes several key components:

* **Application Name & Description**: A clear name and description help users understand what your application does.
* **Redirect URI**: The URL to which users will be redirected after they authorize your application. This must match the redirect URI you use in your OAuth flow.
* **Privacy Policy URL**: A link to your application's privacy policy that will be presented to users during the authorization process.
* **Vehicle Data**: Select the specific vehicle data signals your application will request access to. This determines the permissions your application will need from users.

<Frame type="simple" caption="Application Configuration in Smartcar Dashboard">
  <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/getting-started/configuration.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=1e185b87daf43476f157255e3d01d714" alt="Application Configuration in Smartcar Dashboard" data-og-width="3422" width="3422" data-og-height="2080" height="2080" data-path="images/getting-started/configuration.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/getting-started/configuration.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=b7e0f56bf5e4040cf7e14b8f279141f2 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/getting-started/configuration.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=41183a9075c8de0340879e45445d4e08 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/getting-started/configuration.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=30f892047d9e0dcb29066682c9b8dda0 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/getting-started/configuration.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=8ef45d394f3f6febea7b86371f798714 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/getting-started/configuration.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=1be78284f76fc78879548bb884c6ef37 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/getting-started/configuration.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=2dcbfdb4c6f031019de0fe3d2804b690 2500w" />
</Frame>

#### What’s Next?

* [Connect your first vehicle](/getting-started/connect-vehicles).
* [Build your first integration](/getting-started/integration-overview).


# Connect Vehicles
Source: https://smartcar.com/docs/getting-started/connect-vehicles

Learn how to connect vehicles to your Smartcar application using Smartcar Connect.

Smartcar Connect is the starting point for connecting vehicles to your application. It uses Smartcar's patented and secure [OAuth 2.0](https://oauth.net/2/) flow to let vehicle owners grant your app access to their car data and control features.

### Prerequisites

Before you begin, make sure you have [configured](/getting-started/configure-application) your Smartcar application in the [Smartcar Dashboard](https://dashboard.smartcar.com/configuration). You will need:

* Your application's `Client ID` and `Client Secret`
* A valid `redirect_uri` for your application
* The vehicle data you want to access (e.g., odometer, location, etc.)

<Steps>
  <Step title="Step 1: Launch Smartcar Connect">
    Direct your users to the Smartcar Connect URL. This can be done using the Smartcar SDK for your platform (web, iOS, or Android) or copying the URL from the [Smartcar Dashboard](https://dashboard.smartcar.com/configuration). The user will:

    * Select their vehicle brand
    * Log in with their connected services account
    * Review and approve the requested permissions
  </Step>

  <Step title="Step 2: Handle the Redirect and Get the Authorization Code">
    After the user authorizes access, Smartcar will redirect them back to your application using the default `redirect_uri` you provided in your app configuration. The redirect will include an authorization `code` as a query parameter.
  </Step>

  <Step title="Step 3: Exchange the Code for an Access Token">
    Your backend exchanges the authorization code for an access token and refresh token by making a request to [Smartcar’s token endpoint](/api-reference/authorization/auth-code-exchange). You’ll need your app’s `client_id`, `client_secret`, and the same `redirect_uri`.

    ```
    POST https://auth.smartcar.com/oauth/token
    Content-Type: application/x-www-form-urlencoded

    client_id=YOUR_CLIENT_ID&client_secret=YOUR_CLIENT_SECRET&grant_type=authorization_code&code=AUTH_CODE&redirect_uri=YOUR_REDIRECT_URI
    ```

    The response will include an `access_token` and a `refresh_token`.
  </Step>

  <Step title="Step 4: Store Tokens">
    Store the `access_token` and `refresh_token` securely in your application's database. These tokens are sensitive credentials that allow access to vehicle data and actions, so:

    * Use encrypted storage or a secrets manager whenever possible.
    * Never log tokens or expose them in client-side code.
    * Associate tokens with the correct user and vehicle in your database for easy lookup and management. Here is a [recommended architecture structure](/getting-started/how-to/architecture-design).
    * The `access_token` expires after two hours. You will need to use the `refresh_token` to obtain new access tokens when needed. The `refresh_token` expires after 60 days. If the `refresh_token` expires, the user will need to reauthorize your application.
  </Step>
</Steps>

## What’s Next

* [Build your first integration](/getting-started/integration-overview).
* [See more about Smartcar Connect](/connect/what-is-connect)
* [Explore available API endpoints](/api-reference)
* [Learn about permissions and scopes](/api-reference/permissions)


# Connect Insights
Source: https://smartcar.com/docs/getting-started/dashboard/connect-insights

Connect Insights allows you to visualize your Connect conversion rate and identify where individual users are running into issues during onboarding.

## Conversion Rate

For Enterprise customers, the **Conversion Rate** gives you high-level insight into how users are progressing through the Connect Flow over the last two weeks.

<Frame type="glass">
  <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/getting-started/dashboard/connect-insights-overview.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=f6d7dc245b0c40d2f5c2356475b4e022" data-og-width="1896" width="1896" data-og-height="1075" height="1075" data-path="images/getting-started/dashboard/connect-insights-overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/getting-started/dashboard/connect-insights-overview.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=0bc007baadefdd7c893e321575f8d25a 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/getting-started/dashboard/connect-insights-overview.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=51dd8f0d7e986fbc182ff0ee6b731e7b 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/getting-started/dashboard/connect-insights-overview.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=cd0e5cb80f6b5fae7ff4e81eefa7ddd6 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/getting-started/dashboard/connect-insights-overview.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=fc2999a826f89db5b21a46385c661e42 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/getting-started/dashboard/connect-insights-overview.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=692325a1ce05d3f5a629d54532590ed9 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/getting-started/dashboard/connect-insights-overview.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=3e2c624c887b8c9b880c5ffad45745ea 2500w" />
</Frame>

## Session Details

Clicking into an event in the **Sessions Feed** will pull up more detailed
information for that specific user's session, allowing you to see where they
dropped off and highlighting issues they may have run into.

If you need to dial into a specific time frame or individual user, you can use
filters such as Date, VIN, User or Session ID to do so.

<Frame type="glass">
  <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/getting-started/dashboard/connect-insights-session-detail.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=8f1c0afc8667c7ac5776c335a7753bb7" data-og-width="1671" width="1671" data-og-height="1215" height="1215" data-path="images/getting-started/dashboard/connect-insights-session-detail.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/getting-started/dashboard/connect-insights-session-detail.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=ec07dd4f99c3dcff228f4c4ab5136789 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/getting-started/dashboard/connect-insights-session-detail.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=173e2f391e117eeb8c0536985cca4133 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/getting-started/dashboard/connect-insights-session-detail.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=34768e288d1205a64a01d4c8a606bc13 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/getting-started/dashboard/connect-insights-session-detail.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=ced290399495b78fed4b932eebefb82b 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/getting-started/dashboard/connect-insights-session-detail.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=c0bd3b1f4f8fb4780ae5e16a5b30cef3 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/getting-started/dashboard/connect-insights-session-detail.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=3617d56cbec305aa633e91e19472ace4 2500w" />
</Frame>


# Dashboard Multi-Factor Authentication (MFA)
Source: https://smartcar.com/docs/getting-started/dashboard/dashboard-mfa



## Configuring Multi-Factor Authentication

From the settings gear, you can access User Security, which supports Multi-Factor Authentication (MFA). Enable MFA and scan with your preferred authenticator app such as Google Authenticator or 1Password.

Once enabled, each following login will require the use of your authenticator app to provide a unique code for login.

MFA can be disabled for your user at any time, though the authenticator app will be required to disable MFA.

<Frame type="glass">
  <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/dashboard-mfa.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=903d348d71d6fc30a76492b71e66d195" data-og-width="2048" width="2048" data-og-height="1270" height="1270" data-path="images/dashboard/dashboard-mfa.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/dashboard-mfa.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=1a40c671a66aa4d67bbf8532795c9e97 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/dashboard-mfa.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=815955e746107f16840c7c3bdc0ee487 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/dashboard-mfa.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=6a889a352e445a9a8029e9a7f26876a4 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/dashboard-mfa.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=ebc7499534c660cc33d2edb558bd1bd0 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/dashboard-mfa.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=cf7849557374a6a12961e4fa995568a2 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/dashboard-mfa.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=12b40417f3a7973c81cc561876f085f8 2500w" />
</Frame>


# Dashboard Overview
Source: https://smartcar.com/docs/getting-started/dashboard/overview

All you need to know about the Smartcar Dashboard

You can sign up for a Smartcar account [here](https://dashboard.smartcar.com/signup).
The Smartcar Dashboard allows you to manage your application configurations, connected vehicles, billing settings, team members, simulated vehicles, and webhooks.

<Frame type="glass">
  <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/dashboard-overview.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=f380311605e31b538adacf58dfdb9f95" data-og-width="3932" width="3932" data-og-height="2942" height="2942" data-path="images/dashboard/dashboard-overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/dashboard-overview.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=4afce001caa3c39d53bdfcdb5085365b 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/dashboard-overview.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=a48ab2dd052d0908b91d59462dbe489f 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/dashboard-overview.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=611c2b7a30c5510cac73b70219b168c1 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/dashboard-overview.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=7586040a9ac2211af976f33807b272b4 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/dashboard-overview.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=314a6dffcb11862194350a82110a0fe8 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/dashboard-overview.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=24ab45e7a9dded04bb020814b0890d37 2500w" />
</Frame>


# Vehicle Simulator
Source: https://smartcar.com/docs/getting-started/dashboard/simulator



Before launching your integration, we recommend using Smartcar’s Vehicle Simulator to test your application on a simulated vehicle. With the Simulator, you can choose the vehicle's region, make, model and year as well as the vehicle state to test with. Watch your simulated vehicle travel in real-time from the Smartcar Dashboard as you test API requests from your application with realistic vehicle data responses.

<Frame type="glass">
  <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/dashboard-simulator.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=ac953b25a4604fd3e765bd72ef96d843" data-og-width="3338" width="3338" data-og-height="2946" height="2946" data-path="images/dashboard/dashboard-simulator.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/dashboard-simulator.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=b81561e32e5ebbf09f0b2d29326abb4b 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/dashboard-simulator.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=0d95d85d8c60a837bbd95c2d324627be 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/dashboard-simulator.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=218e21b0ae5d62da0afb3c0bb64c5c6e 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/dashboard-simulator.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=341e6abb99c9895fbc154489816d0a57 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/dashboard-simulator.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=a9a91ae839225fbc9418a560117ffd25 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/dashboard-simulator.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=31f3dc853ae247090ccb482060282746 2500w" />
</Frame>

## 1. Create a simulated vehicle

#### Create a simulated vehicle

Begin by logging into the Smartcar Dashboard and navigating to the Simulator tab. Choose your region and select a Smartcar-compatible vehicle using the Make, Model, and Year dropdowns. Or, use the VIN search feature to create a simulated vehicle of the same Make, Model and Year as the VIN entered, as long as the vehicle is compatible with Smartcar. Please note the VIN search is only available for US-based VINs at this time.

#### Review the vehicle capabilities

Confirm the vehicle's supported capabilities includes those you wish to test.

#### Select a vehicle state

Select from one of three available vehicle states for your simulated vehicle. The states vary in duration from 8 to 24 hours and include driving, charging, and parked vehicle states for a wide range of test scenarios.

## 2. Connect your app to the simulated vehicle

Once you've selected a vehicle and state, you are ready to connect the simulated vehicle to your application for testing.

Grab the simulated vehicle credentials
On the simulation screen, you will find a Connect Credentials button that will open a modal containing the simulated vehicle's credentials. You will need these to connect your app and vehicle using Smartcar Connect.

#### Launch Smartcar Connect in simulated mode

When launching Smartcar Connect, pass in the query parameter mode=simulated to enable simulated mode and ensure you can connect to your newly created simulated vehicle. Smartcar's SDKs provide a convenient option to facilitate this:

<CodeGroup>
  ```js Node theme={null}
  const client = new smartcar.AuthClient({
    clientId: CLIENT_ID,
    clientSecret: CLIENT_SECRET,
    redirectUri: REDIRECT_URI,
    mode: "simulated",
  });
  ```

  ```python Python theme={null}
  client = smartcar.AuthClient(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    mode="simulated"
  )
  ```

  ```java Java theme={null}
  AuthClient authClient = new AuthClient.Builder()
    .clientId(CLIENT_ID)
    .clientSecret(CLIENT_SECRET)
    .redirectUri(REDIRECT_URI)
    .mode("simulated")
    .build();
  ```

  ```ruby Ruby theme={null}
  client = Smartcar::AuthClient.new({
    client_id: CLIENT_ID,
    client_secret: CLIENT_SECRET,
    redirect_uri: REDIRECT_URI,
    mode: "simulated"
  })
  ```
</CodeGroup>

#### Log into a connected services account

After launching Smartcar Connect, select the brand that matches your simulated vehicle and enter the credentials pulled from the Smartcar Dashboard simulation screen on the brand login page. You will then be prompted to grant access to your selected permissions.

Upon completing the Smartcar Connect flow, return to the Smartcar Dashboard. It may take up to a minute to reflect that your vehicle is now connected. Once connected, the vehicle ID will appear next to the vehicle's VIN near the top of the simulation screen.

## 3. Start the simulation and begin testing

Once the vehicle is connected to your application, you are ready to start the simulation and begin making API requests to the simulated vehicle.

### Start the simulation

In the Smartcar Dashboard on the simulation screen for your selected simulated vehicle, start the simulation by pressing the Play button. You have the option to pause, resume or restart the simulation at any time. Additional controls you have over the simulation:

#### Control the simulation speed

You can control the simulation's speed in case you would like to test the vehicle at various stages at a faster or slower pace.

#### Change the simulation stage

Once the simulation has started, you can jump to any stage of the simulation in the event you would like to test the vehicle in a particular state.

#### Set the API response latency

Control the response latency of any API requests you make to the simulated vehicle.

`Ideal` - API responses are returned immediately upon request.

`Realistic` - API responses are delayed a certain amount of time based on average API response latency statistics that Smartcar has gathered for each supported brand.

A breakdown of estimated response latencies can be viewed by clicking on the ‘View latencies’ link directly underneath the Request Latency dropdown in the Dashboard. Please note latency estimates may not be available for all brands. In these cases, the Realistic setting will return immediate responses -- same as Ideal.

#### Change the vehicle state

You can select a different vehicle state for your simulated vehicle at any time. Select the Edit icon in the `Trip type` card on the simulation screen.

### Send an API request to the simulated vehicle

The Smartcar API will return realistic data matching the current state of the simulated vehicle as displayed on the simulation screen. Note that if you've selected Realistic API response latency, the data returned to your application may appear somewhat delayed.


# Single Sign-on (SSO)
Source: https://smartcar.com/docs/getting-started/dashboard/single-sign-on

Smartcar offers SSO through your identity provider (IdP) for Enterprise customers.

## About SSO with Smartcar

Our Dashboard supports SSO integrations with popular identity providers
including:

* Okta
* Microsoft Azure AD
* Google Workspace
* OneLogin
* Ping Identity
* ADFS
* Custom SAML 2.0 providers

To set up SSO for your organization's Dashboard accounts, you'll need to:

1. Be an Owner for an existing Team on an Enterprise plan
2. Verify your domain
3. Configure your identity provider

The following section will guide you through each step of this process.

## Setting up SSO

On Dashboard navigate to **Team settings > Security** and select **Enable SSO**

<Frame>
    <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/enable-sso.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=25cb9f378d60084f216d0c8341d0d846" alt="" data-og-width="1417" width="1417" data-og-height="517" height="517" data-path="images/dashboard/sso/enable-sso.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/enable-sso.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=b877b06d48922a99f9bb92b3e8f4efc4 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/enable-sso.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=e61a60c77fa33f873a1db2e3fe57ed81 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/enable-sso.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=d59d2cd95e627bfacab7173d91d4c67b 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/enable-sso.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=cecb3e19007e9f33df5e7b8b8ac4b6fe 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/enable-sso.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=524b58a248c8701af8283b5a9ce92d3d 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/enable-sso.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=6d9aa3c05e1d6e9612691b8055f40528 2500w" />
</Frame>

You’ll be redirected to start the SSO configuration process.

<Frame>
    <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/verify-domain-1.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=d2163f376519a4a27ccedd07910091e1" alt="" data-og-width="1061" width="1061" data-og-height="705" height="705" data-path="images/dashboard/sso/verify-domain-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/verify-domain-1.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=83581ff2b0559a69d2b2b2ab370549a8 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/verify-domain-1.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=e2510c784e807c1b340da2bbc082e786 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/verify-domain-1.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=16b463970552e8d9a47a8e1d1dc833d6 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/verify-domain-1.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=f4d3c7240ae3d77080f6de659b6fcf6c 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/verify-domain-1.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=4ec6364f91acfd734dda45554a3e0408 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/verify-domain-1.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=7d74cc03530fd081ee1738ff37bcbc77 2500w" />
</Frame>

Depending on your DNS provider, you'll receive instructions on how to verify your domain.

<Frame>
    <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/verify-domain-2.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=8a522104b3e4c392add44c7b7670a8b5" alt="" data-og-width="516" width="516" data-og-height="1016" height="1016" data-path="images/dashboard/sso/verify-domain-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/verify-domain-2.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=fb506b211830b3657f537a6416f0e911 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/verify-domain-2.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=f0c5752093458dea14d516858189d9f9 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/verify-domain-2.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=f348dc19bd86c34cca8fe03ee909c346 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/verify-domain-2.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=11cc2649d63e9031eaa1658b494ffb88 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/verify-domain-2.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=ce55ea6c6cbbe1c0734ff7588b02d610 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/verify-domain-2.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=3c389d53c4e0fe9484667d5b49549482 2500w" />
</Frame>

Once your domain is verified, you’ll be able to select your Identity Provider
(IdP).

<Frame>
    <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/select-idp.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=cc58d3e1c79ea46ba0ac7d0879cc2f8c" alt="" data-og-width="1145" width="1145" data-og-height="486" height="486" data-path="images/dashboard/sso/select-idp.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/select-idp.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=d729fbaa9b48bdb3d6aefef2bfa9b34e 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/select-idp.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=fd53922bfdccd7ea2b2c61b697890790 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/select-idp.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=c850e9b64b9a01bc5e8c765912d0229f 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/select-idp.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=e3e368a3b8a496a0ee7adc2ee1138d33 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/select-idp.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=86c92b78a1966b299f3c221dc1cbacf5 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/select-idp.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=a1c9ed66aff7e8378e11d1a6cd34a925 2500w" />
</Frame>

You'll be provided a guide on how to get set up based on your IdP.

<Frame>
    <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/config-idp.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=5b175cde2bc4e00277c17b3d63a84e53" alt="" data-og-width="1058" width="1058" data-og-height="588" height="588" data-path="images/dashboard/sso/config-idp.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/config-idp.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=c0b1bea8be73031103dfbc8429d135bd 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/config-idp.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=daac4db2d45418bb324ef5fca7447e4c 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/config-idp.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=8c7331c3ed3011fb2e8d77d8b0a865cf 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/config-idp.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=0047a406d29b6bf7bfb09a7cbf3b73de 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/config-idp.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=1bf560fd843ac8b5867d8df632b6929f 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/config-idp.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=050664254b62d1b1db1b7096e2b2729c 2500w" />
</Frame>

Once you’ve got everything configured, you’ll be prompted to test SSO.

<Frame>
    <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/test-sso.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=2dc072fb8b8c9b3dd933091bb0ffa8a7" alt="" data-og-width="1058" width="1058" data-og-height="366" height="366" data-path="images/dashboard/sso/test-sso.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/test-sso.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=7464494f6b5eed426690448ff4b5caaa 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/test-sso.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=0decc9519c098999c40340a8f81f4b69 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/test-sso.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=ce699b5e204863e02f7c98467880a90b 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/test-sso.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=8d5a5db32d3a5a91b8d5674031b5e7ec 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/test-sso.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=6e1b36599829f751db351b712de0eefc 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/test-sso.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=b5958057a9435dfc4e4f3c2d1c015716 2500w" />
</Frame>

<br />

<Tip>
  If you exit the flow at any time before finalizing your configuration, you
  can jump back in from Dashboard.
</Tip>

<Frame>
    <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/sso-config-pending.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=4e8f44f02059878dce36912a5dde0519" alt="" data-og-width="1076" width="1076" data-og-height="626" height="626" data-path="images/dashboard/sso/sso-config-pending.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/sso-config-pending.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=dbb3f3e5dee8f79067f30b60a5ff7c84 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/sso-config-pending.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=a858f0b128121c9d4d3c374b2dcd15de 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/sso-config-pending.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=25b14426cafd0b438a88fa6e4e5bee0c 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/sso-config-pending.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=9faf2ed7404f98a270ec2ee18bf09c64 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/sso-config-pending.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=959f81303a64f4921223f039cc8c39f5 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/sso-config-pending.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=c19d9c97584ed8e2b21a212be243a86f 2500w" />
</Frame>

## Disabling SSO

If you have SSO configured, the Team Owner can disable it from **Team
settings > Security**.

<Warning>
  Disabling SSO will require you to go through the whole setup process
  again.
</Warning>

## Inviting team members with SSO enabled

Once enabled, you’ll need to add members to your team through your identity
provider. Invites via the Dashboard will be disabled while SSO is enabled.

<Frame>
    <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/invite-with-sso.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=cd408514ef3a7e8e46a7b2368e02901e" alt="" data-og-width="875" width="875" data-og-height="285" height="285" data-path="images/dashboard/sso/invite-with-sso.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/invite-with-sso.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=7a938fc9e64e07750d4c5d03a4fc5068 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/invite-with-sso.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=4cdf56ef26632ba9b9ea5d9143cba134 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/invite-with-sso.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=e156364b2a42d2c7823c960113c18db8 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/invite-with-sso.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=50dcc0576cb4ea96daa32a42fa793cc1 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/invite-with-sso.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=296d66de91680940b072231d77454b16 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/sso/invite-with-sso.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=891f8b7fc43e673b75638f3e352c52b0 2500w" />
</Frame>

When a newly added member has signed in via SSO, they will have the Viewer role
by default. Other team members with the appropriate role can promote these
members as needed.

<Note>
  If a user creates a Dashboard account with their email prior to being added
  to your IdP, they will be added to their own Team initially. When they are
  added to your IdP they will be able to switch Teams in Dashboard.
</Note>

## A note on aliased emails

If members of your team have Dashboard accounts using email aliases prior to
enabling SSO e.g. [rover+thebest@dog.com](mailto:rover+thebest@dog.com), once SSO is enabled for your Team and
they’re added to your IdP, their login will be tied to their non-aliased email
address e.g. [rover@dog.com](mailto:rover@dog.com).

SSO is only available on the **Enterprise** plan, please reach out to your Account Manager for more details.


# Team Settings
Source: https://smartcar.com/docs/getting-started/dashboard/teams

Your Smartcar Team is the central hub for managing your applications, vehicles, members, security settings, and billing information.

Your Smartcar Team allows you to collaborate with other members and manage your applications in one place.

## Members

You can add team members to your Smartcar account on any plan for free.
Team members can be added to your Smartcar account by navigating to the **Settings** tab in the Dashboard and selecting **Members** under the **Team** section.

<Frame type="glass">
  <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/dashboard-team-members.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=f42b136eb32b09de7725c31dc6db3dd7" data-og-width="3336" width="3336" data-og-height="2946" height="2946" data-path="images/dashboard/dashboard-team-members.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/dashboard-team-members.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=00d5f360352218de3998c5d80f36600d 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/dashboard-team-members.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=8f34d0dc11cad80da78f66ab3dc50bdc 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/dashboard-team-members.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=9306ba1870873a143d3a0507cb7a88f6 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/dashboard-team-members.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=99e9b2e2501cc574273a8439d3194785 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/dashboard-team-members.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=5286298f00b6bd075b0c79084bdb4bf4 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/dashboard/dashboard-team-members.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=11950d938d85453f8248d852a424a402 2500w" />
</Frame>

## Roles and Permissions

Team members can be added on any plan. Specific roles are available on our [Enterprise plan](https://smartcar.com/pricing).

| <div style={{ width:200 }} /> | Owner <div style={{ width:100 }} /> | Admin <div style={{ width:100 }} /> | Editor <div style={{ width:100 }} /> | Viewer <div style={{ width:100 }} /> |
| ----------------------------- | ----------------------------------- | ----------------------------------- | ------------------------------------ | ------------------------------------ |
| Manage billing                | ✅                                   |                                     |                                      |                                      |
| View billing                  | ✅                                   |                                     |                                      |                                      |
| Delete applications           | ✅                                   |                                     |                                      |                                      |
| Modify team settings          | ✅                                   |                                     |                                      |                                      |
| Remove team members           | ✅                                   | ✅                                   |                                      |                                      |
| Modify team members           | ✅                                   | ✅                                   |                                      |                                      |
| Create applications           | ✅                                   | ✅                                   |                                      |                                      |
| Modify applications           | ✅                                   | ✅                                   | ✅                                    |                                      |
| View applications             | ✅                                   | ✅                                   | ✅                                    | ✅                                    |
| View team members             | ✅                                   | ✅                                   | ✅                                    | ✅                                    |

<Tip>
  Editors and Viewers can be limited to specific applications.
</Tip>

## Roles

### Owner

Owners have full control and access to the team. They're able to add and remove members, create and modify applications, edit billing information and more.

A team **can** have multiple Owners, but **must** have at least one.

### Admin

Admins have similar access to Owners but can't edit or view billing information.

### Editor

Editors have similar access to Admins but are limited to specific applications. They're unable to manage team members, view the team's billing information, create applications, or delete applications they're allowed to access.

### Viewer

Viewers have similar permissions to Editors but only have read-only access to applications they've been invited to.


# How to Design Your Backend Architecture for Smartcar
Source: https://smartcar.com/docs/getting-started/how-to/architecture-design

Learn how to design your backend to integrate your application with Smartcar.

Designing your backend architecture for Smartcar integration ensures secure storage of credentials, reliable webhook handling, and a scalable implementation. This guide walks you through the essential database tables and backend endpoints you’ll need.

## What You'll Achieve

* Set up database tables to store vehicles, users, and tokens
* Create backend endpoints to handle OAuth and webhooks
* Understand the data flow between Smartcar and your backend

<Steps>
  <Step title="Step 1: Plan Your Database Tables">
    You’ll need tables to track users, vehicles, and Smartcar tokens. Here’s a recommended schema:

    | Table             | Purpose                                                                   | Key Fields                                                                                                                                   |
    | ----------------- | ------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
    | `users`           | You probably already have this table to store your app's users            | `id`, `email`, `name`, etc.                                                                                                                  |
    | `smartcar_tokens` | Stores Smartcar access and refresh tokens pairs with user and vehicle IDs | `id`, `your_app_user_id`, `smartcar_vehicle_id`, `smartcar_access_token`, `smartcar_refresh_token`, `expires_at`, `created_at`, `updated_at` |
    | `vehicles`        | Stores connected vehicle information                                      | `id`, `smartcar_user_id`, `your_app_user_id`, `make`, `model`, `year`, `created_at`, `updated_at`                                            |
    | `vehicle_data`    | Stores data about your vehicles (i.e. odometer readings, location, etc.)  | `id`, `smartcar_vehicle_id`, `created_at`, `data_type`, `data_value`                                                                         |
    | `webhook_logs`    | Log incoming webhook events (optional)                                    | `id`, `smartcar_vehicle_id`, `event_type`, `payload`, `received_at`                                                                          |

    <Note>
      Always encrypt tokens at rest and never expose them to the client.
    </Note>
  </Step>

  <Step title="Step 2: Implement OAuth Code Exchange Endpoint">
    Create a backend endpoint to handle the OAuth redirect from Smartcar and exchange the authorization code for tokens.

    **Example: `/api/smartcar/callback`**

    1. Receive the `code` and `state` query parameters from Smartcar.
    2. Exchange the code for tokens using Smartcar’s token endpoint.
    3. Store the tokens in your `tokens` table, linked to the user and vehicle.

    ```javascript  theme={null}
    POST https://auth.smartcar.com/oauth/token
    Content-Type: application/x-www-form-urlencoded

    client_id=YOUR_CLIENT_ID&client_secret=YOUR_CLIENT_SECRET&grant_type=authorization_code&code=AUTH_CODE&redirect_uri=YOUR_REDIRECT_URI
    ```
  </Step>

  <Step title="Step 3: Create a Webhook Receiver Endpoint">
    Set up an endpoint to receive webhook POST requests from Smartcar.

    **Example: `/api/webhooks/smartcar`**

    * Validate the webhook signature (see [Smartcar webhook docs](/integrations/webhooks)).
    * Parse the event payload and update your database as needed.
    * Log the event in `webhook_logs` for auditing and debugging.

    <Info>
      Want a production-ready AWS implementation? Use the <a href="/getting-started/tutorials/webhook-receiver-recipe">Webhook Receiver Recipe</a>. It includes everything you need to get up and running so you can focus on business logic instead of infrastructure.
    </Info>

    ```javascript  theme={null}
    // Example Express.js handler
    app.post('/api/webhooks/smartcar', async (req, res) => {
      try {
        // 1. Validate webhook signature
        const isValid = await validateWebhookSignature(req);
        if (!isValid) {
          return res.status(401).send('Invalid signature');
        }

        // 2. Parse event and update database
        const event = req.body;
        await processWebhookEvent(event);

        // 3. Respond with 200 OK
        res.status(200).send('Received');
      } catch (error) {
        console.error('Error processing webhook:', error);
        res.status(500).send('Error processing webhook');
      }
    });
    ```
  </Step>

  <Step title="Step 4: Secure Your Endpoints">
    * Restrict access to OAuth and webhook endpoints.
    * Use HTTPS for all traffic.
    * Never expose access or refresh tokens to the frontend.
  </Step>
</Steps>

***

## What’s Next

* [Set up Smartcar Connect](/getting-started/connect-vehicles)
* [Configure your webhook integration](/getting-started/integration-overview)


# How to Configure Permissions for Vehicle Data Collection
Source: https://smartcar.com/docs/getting-started/how-to/configure-permissions

Step-by-step guide to selecting signals, commands, and attributes in the Smartcar Dashboard and requesting the right permissions from vehicle owners.

To retrieve vehicle data through Smartcar, you must configure your application to request the correct permissions from vehicle owners. This guide walks you through the process using the Smartcar Dashboard.

<Steps>
  <Step title="Open the Configuration Page in the Dashboard">
    Go to the [Smartcar Dashboard](https://dashboard.smartcar.com/configuration) and select your application. Navigate to the <b>Configuration</b> section and choose the <b>Vehicle access</b> tab.
  </Step>

  <Step title="Select Signals, Commands, and Attributes">
    Under the <b>Signals</b>, <b>Commands</b>, and <b>Attributes</b> tabs, select the specific vehicle data points and actions your application needs. Each selection corresponds to a permission that the vehicle owner must approve.

    <Frame type="simple" caption="Application Configuration in Smartcar Dashboard">
      <img src="https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/how-to/vehicle-access.png?fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=8dbd5a5cbf7561ce6890e8b74d2e3af1" alt="Smartcar Dashboard configuration page showing signal selection and Connect Preview." data-og-width="5014" width="5014" data-og-height="2966" height="2966" data-path="images/how-to/vehicle-access.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/how-to/vehicle-access.png?w=280&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=cddfd1c093f18c5addf4747182e51a93 280w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/how-to/vehicle-access.png?w=560&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=ea20d97a8cd21ed0f9b792cdcafb7655 560w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/how-to/vehicle-access.png?w=840&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=8e81876d3862241affee92b987706cea 840w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/how-to/vehicle-access.png?w=1100&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=31c470447fe2ebdf68c75dd3d160a1fd 1100w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/how-to/vehicle-access.png?w=1650&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=ca57dad41510fe85b7c5407384adfac0 1650w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/how-to/vehicle-access.png?w=2500&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=a95f7e18664d6b9d3592652f3c662607 2500w" />
    </Frame>

    <ul>
      <li><b>Signals:</b> Dynamic vehicle data (e.g., battery level, odometer, location).</li>
      <li><b>Commands:</b> Actions your app can perform (e.g., lock/unlock, start charging).</li>
      <li><b>Attributes:</b> Static vehicle info (e.g., make, model, year).</li>
    </ul>

    <Note>
      Only select the permissions your application truly needs. This improves user trust and increases the likelihood of successful connections.
    </Note>
  </Step>

  <Step title="Preview the Owner Experience">
    As you select signals, commands, and attributes, the <b>Connect Preview</b> on the right updates to show what the vehicle owner will see when connecting their vehicle. This preview lists the permissions your app is requesting and the vehicles that will be connected.
  </Step>

  <Step title="Publish Your Configuration">
    Once you are satisfied with your selections, click <b>Publish</b> to save your configuration. Your application will now request these permissions from vehicle owners during the Smartcar Connect flow.
  </Step>
</Steps>

## Dynamic Permissions

If your application needs to access different permissions based on user actions or vehicle types, you can leverage the `scope` parameter in the Smartcar Connect URL to dynamically request permissions at runtime. This allows you to tailor the permissions based on the specific vehicle or user context.
Keep in mind that any permissions you pass via the `scope` parameter will override the permissions configured in the Smartcar Dashboard for that specific connection.

### Notes

* If you need to change permissions later, you can return to this configuration page and update your selections. Vehicle owners will need to reauthorize your application to grant any new permissions.
* The permissions you select here will determine the data and actions available to your application. Make sure to choose only what is necessary for your use case.

***

## What’s Next

* [How to Connect Vehicles](/getting-started/connect-vehicles)
* [How to Manage API Tokens](/getting-started/how-to/manage-api-tokens)
* [API Reference: Permissions](/api-reference/permissions)


# How to Detect and Process Charging Sessions with Webhooks
Source: https://smartcar.com/docs/getting-started/how-to/detect-charging-session

Learn how to use Smartcar webhooks to detect when a vehicle starts and ends charging, and how to process charging session data.

Smartcar webhooks make it easy to detect and process vehicle charging sessions in real time. This guide explains how to configure your webhook, handle charging events, and process charging session data in your backend.

<Steps>
  <Step title="Configure Your Webhook for Charging Events">
    In the [Smartcar Dashboard](https://dashboard.smartcar.com/integrations), create or edit a webhook integration. Under <b>Triggers</b>, select the following events:

    <ul>
      <li>Charge.IsCharging</li>
      <li>Charge.IsChargingCableConnected</li>
    </ul>

    These signals will act as triggers for detecting when a vehicle starts and stops charging and when it is plugged in or unplugged. Whenever these signals change, Smartcar will send a webhook event to your configured endpoint.
    Next, you'll configure your **data**. This is the information you want to receive in your webhook payload every time you receive a webhook event. Triggers are included by default, but you can also add additional signals to the data payload, such as:

    <ul>
      <li>Charge.StateOfCharge (included as a trigger)</li>
      <li>Charge.ChargingCurrent (included as a trigger)</li>
      <li>Charge.ActiveLimit</li>
      <li>Charge.Amperage</li>
      <li>Charge.Voltage</li>
      <li>Charge.Wattage</li>
      <li>Charge.EnergyAdded</li>
      <li>Charge.TimeToComplete</li>
      <li>TractionBattery.Range</li>
      <li>TractionBattery.NominalCapacity</li>
      <li>Location.PreciseLocation</li>
    </ul>

    These data signals will be delivered for every webhook event, allowing you to track the state of charge and other relevant metrics while the vehicle is charging.
    Next, provide your webhook URL where Smartcar will send the events. Make sure your endpoint is publicly accessible and can handle POST requests. You can choose to auto enroll all your vehicles to this webhook or manually subscribe vehicles later (you can do this from the Dashboard). For this guide, select "don't subscribe any vehicles".
    Now it is time to save and verify your webhook.
  </Step>

  <Step title="Validate Webhook Events">
    Smartcar will send a verification request to your endpoint, which you must respond to with a 200 OK status code to complete the setup (see [Webhook Verification guide](/integrations/webhooks/callback-verification)).
    Once verified, you will start to receive vehicle data for the vehicles you have subscribed to this webhook. For this guide, we chose not to auto subscribe vehicles, so let's head over to the [Smartcar Dashboard](https://dashboard.smartcar.com/vehicles) to manually subscribe a vehicle to your webhook.
    Select a vehicle from your list of connected vehicles and click on the three dots action menu to the right of the row and click subscribe. Select your newly created webhook from the options and click subscribe.

    <Frame type="simple" caption="Subscribe a vehicle to a webhook in the Smartcar Dashboard">
      <img src="https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/how-to/subscribe-vehicles-from-dashboard.png?fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=5bd20bb10e660b3297ef2de1dbf4c022" alt="Smartcar Dashboard showing how to subscribe a vehicle to a webhook." data-og-width="3298" width="3298" data-og-height="2048" height="2048" data-path="images/how-to/subscribe-vehicles-from-dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/how-to/subscribe-vehicles-from-dashboard.png?w=280&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=051e639fdee31c606c0980f8f304b8ff 280w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/how-to/subscribe-vehicles-from-dashboard.png?w=560&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=f4cbba0bde2464efdc3cf1c78ad78bdf 560w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/how-to/subscribe-vehicles-from-dashboard.png?w=840&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=782a6977e48b8e3ba1c8e40cd7cc5433 840w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/how-to/subscribe-vehicles-from-dashboard.png?w=1100&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=953979e3045a081ab1b20c6f792e0b14 1100w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/how-to/subscribe-vehicles-from-dashboard.png?w=1650&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=aa7e740e2f42c98206dd735f89a48286 1650w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/how-to/subscribe-vehicles-from-dashboard.png?w=2500&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=7655f451c559dd4ca247423a4f9884d4 2500w" />
    </Frame>
  </Step>
</Steps>

At this point, your webhook is fully configured to receive charging events from the subscribed vehicle. Now let's handle the incoming webhook events in your backend.

Every webhook will include an `eventId` and an `eventType` field. The `eventType` will indicate the type of event that occurred, such as `VEHICLE_STATE` or `VEHICLE_ERROR`.
Your handler should gracefully handle both event types. For `VEHICLE_STATE` events, you will receive the updated vehicle data. For `VEHICLE_ERROR` events, you may want to log the error.
For `VEHICLE_STATE` events, you will receive the data in a `data` property of the payload. There will also be an array of signals under a `triggers` property that caused the event to be sent. Lastly, you will also receive a `meta` property with additional context about the event, such as the webhook ID, name, delivery ID, delivery timestamp, etc.

### How to track charging sessions

When a vehicle starts charging, you will receive a webhook event with the `eventType` of `VEHICLE_STATE` and the `Charge.IsCharging` signal set to `true`. When the vehicle stops charging, you will receive another event with `Charge.IsCharging` set to `false`. You can use these events to track the start and end of each charging session.

Example event payload:

```json  theme={null}
{
  "eventId": "a7738a15-7ee2-40b3-9815-823d146230cd",
  "eventType": "VEHICLE_STATE",
  "data": {
    "user": {
      "id": "deee49b6-d638-4be4-82dc-121ea613eed9"
    },
    "vehicle": {
      "id": "829e30ab-5a13-40b5-9f8a-8538af86ed95",
      "make": "Tesla",
      "model": "Model 3",
      "year": 2020
    },
    "signals": [
      {
        "code": "charge-ischarging",
        "name": "IsCharging",
        "group": "Charge",
        "body": {
          "value": true
        },
        "status": {
          "value": "SUCCESS"
        },
        "meta": {
          "oemUpdatedAt": 1754365413366,
          "retrievedAt": 1754365413366
        }
      }
    ],
    "triggers": [
      {
        "type": "SIGNAL_UPDATED",
        "signal": {
          "code": "charge-ischarging",
          "name": "IsCharging",
          "group": "Charge"
        }
      }
    ],
    "meta": {
      "webhookId": "f1c2d3e4-5678-90ab-cdef-1234567890ab",
      "webhookName": "My Charging Webhook",
      "deliveryId": "b1c2d3e4-5678-90ab-cdef-1234567890ab",
      "deliveryTimestamp": "2024-08-04T17:00:00Z",
      "mode": "LIVE",
      "signalCount": 1
    }
  }
}
```

Tip: Always validate the webhook signature to ensure the request is from Smartcar.

***

## What’s Next

* [How to Configure Permissions](/getting-started/how-to/configure-permissions)
* [How to Manage API Tokens](/getting-started/how-to/manage-api-tokens)
* [API Reference: Webhooks](/api-reference/webhooks/subscribe-webhook)


# How to Get an API Access Token
Source: https://smartcar.com/docs/getting-started/how-to/get-an-access-token

Learn how to obtain your first Smartcar API access token by exchanging an authorization code.

To make requests to the Smartcar API, you first need to obtain an access token. This guide walks you through the process of getting the authorization code and exchanging it for an access token for the first time.

<Steps>
  <Step title="1. Launch Smartcar Connect">
    Direct your user to the Smartcar Connect URL. The user will:

    * Select their vehicle brand
    * Log in with their connected services account
    * Approve the requested permissions

    After successful authorization, Smartcar will redirect the user to your application's `redirect_uri` with an authorization `code` as a query parameter.
  </Step>

  <Step title="2. Handle the Redirect and Extract the Code">
    Your application should listen for requests to the `redirect_uri`. When Smartcar redirects the user, extract the `code` parameter from the query string.
    <b>Example redirect:</b>

    ```
    https://your-app.com/callback?code=AUTH_CODE&state=STATE
    ```
  </Step>

  <Step title="3. Exchange the Code for an Access Token">
    Use the authorization code to request an access token and refresh token from [Smartcar’s OAuth token endpoint](/api-reference/authorization/auth-code-exchange).

    Here is an example using the Smartcar Node.js SDK:

    ```javascript  theme={null}
    const smartcar = require('smartcar'); //Smartcar backend Node SDK

    smartcar.OAuth.getToken({
      client_id: 'YOUR_CLIENT_ID',
      client_secret: 'YOUR_CLIENT_SECRET',
      grant_type: 'authorization_code',
      code: 'AUTH_CODE', //extracted from the URL query parameter
      redirect_uri: 'YOUR_REDIRECT_URI'
    });
    ```

    The response will include an `access_token`, an `expires_in` field, and a `refresh_token`. Store these securely in your backend database.
    The `access_token` expires after two hours, and the `refresh_token` expires after 60 days.
  </Step>
</Steps>

***

## What’s Next

* [How to Manage API Tokens](/getting-started/how-to/manage-api-tokens)
* [Refreshing API Access Tokens](/api-reference/authorization/refreshing-access-token)


# How to Manage API Access Tokens and Refresh Tokens
Source: https://smartcar.com/docs/getting-started/how-to/manage-api-tokens

Best practices for securely storing, refreshing, and rotating Smartcar API tokens.

This guide explains how to store, refresh, and rotate tokens using the Smartcar API.

<Info>
  <b>API Access Token vs. Application Management Token</b><br />

  <ul>
    <li><b>API Access Token:</b> Used to access vehicle data and issue commands on behalf of a vehicle owner. These tokens are obtained through the OAuth flow after a user connects their vehicle and are required for all Smartcar API requests involving vehicle data.</li>
    <li><b>Application Management Token:</b> Used to manage your Smartcar application itself (e.g., configuring webhooks or managing your vehicles). This token is found in the Smartcar Dashboard and is <b>not</b> used for accessing vehicle data or making API requests on behalf of users.</li>
  </ul>

  <b>Always use the correct token type for your use case:</b> API access tokens for vehicle data, and management tokens for application configuration.
</Info>

<Steps>
  <Step title="Store Tokens Securely">
    * Store both the `access_token` and `refresh_token` in your backend database, never in client-side code.
    * Encrypt tokens at rest and restrict access to only necessary backend services.
    * Associate tokens with the correct user and vehicle for easy lookup and management.
  </Step>

  <Step title="Use the Access Token for API Requests">
    * Use the `access_token` as a Bearer token in the `Authorization` header for all API requests.

    ```javascript  theme={null}
    GET https://vehicle.api.smartcar.com/v3/vehicles/{vehicleId}
    Authorization: Bearer ACCESS_TOKEN
    ```

    * If the access token is valid, the API will return the requested data.
  </Step>

  <Step title="Detect Expired Access Tokens">
    * If an API request returns a 401 Unauthorized error, the access token may have expired.
    * In this case, use the refresh token to obtain a new access token.
  </Step>

  <Step title="Refresh the Access Token">
    * Make a POST request to the Smartcar OAuth token endpoint with `grant_type=refresh_token`.

    ```javascript  theme={null}
    POST https://auth.smartcar.com/oauth/token?client_id=YOUR_CLIENT_ID&client_secret=YOUR_CLIENT_SECRET&grant_type=refresh_token&refresh_token=YOUR_REFRESH_TOKEN
    Content-Type: application/x-www-form-urlencoded
    ```

    * Store the new `access_token` and `refresh_token` in your database, replacing the old values.
  </Step>

  <Step title="Rotate and Revoke Tokens">
    * Always update both tokens after a refresh to maintain security.
  </Step>
</Steps>

***

## Additional Resources

* [Smartcar API Reference](/api-reference)
* [How to Design Your Backend](/getting-started/how-to/architecture-design)


# Integrate with Smartcar To Receive Vehicle Data
Source: https://smartcar.com/docs/getting-started/integration-overview

Welcome to the integration phase of your Smartcar journey! After configuring your application and connecting vehicles, the next crucial step is to integrate your systems with Smartcar to receive vehicle data.

## The architecture that's right for you

<Info>
  Webhooks are the recommended way to receive real-time vehicle data from Smartcar. You can still use the REST API for retrieving data and issuing commands, but webhooks are the most scalable and reliable option for most use cases.
</Info>

## Webhooks

[Webhooks](/integrations/webhooks/overview) are the most efficient way to receive real-time vehicle data. Smartcar sends you a payload whenever a vehicle event occurs, such as a change in battery level or location. This allows you to build applications that respond instantly to vehicle changes without polling an API.

**Quick Start**: Deploy a production-ready webhook receiver in minutes with our [Webhook Receiver Recipe](/getting-started/tutorials/webhook-receiver-recipe) - a complete AWS serverless solution.

Get started with Webhooks [here](/integrations/webhooks/overview).

## REST APIs

If you prefer to retrieve data on demand, you can use the Smartcar [Vehicles API](/api-reference/vehicles-api-intro). This allows you to query vehicle data at any time, but it may not be as efficient for real-time applications. The Vehicles API provides endpoints for accessing signals, issuing commands, and retrieving vehicle attributes.

The Vehicles API is designed primarily for exploration and non-frequent data retrieval. This API is not designed for continuous polling or real-time monitoring. Data is typically updated once every 24 hours unless the vehicle is actively subscribed to a webhook, which enables more frequent updates. For most use cases, you should avoid polling the Vehicles API at high frequency leverage [webhooks](/integrations/webhooks/overview) instead.

## CSVs (coming soon)

This integration will help you receive vehicle data in a CSV file where you can integrate analyze using your existing tools and workflows.

With CSV integrations, you will be able to:

* Receive vehicle data from Smartcar at a specified cadence (e.g., weekly, monthly)
* Choose the data fields you want to include in the CSV export (e.g., vehicle info, location, odometer, battery level)
* Have CSV files automatically delivered to your preferred destination, such as an SFTP server, cloud storage bucket, etc.
* Easily import Smartcar data into your analytics, reporting, or business intelligence tools

This solution is ideal for customers who need scheduled, automated data exports for compliance, reporting, or integration with legacy systems.

<Note>
  CSV integration is coming soon! If you are interested in early access or have specific requirements, please reach out to <a href="mailto:support@smartcar.com">[support@smartcar.com](mailto:support@smartcar.com)</a>.
</Note>


# Getting Started with Smartcar
Source: https://smartcar.com/docs/getting-started/introduction

Welcome to Smartcar's Developer Documentation! Here, you'll learn how to integrate your application with over 40 OEM brands, securely connect to vehicles, and receive the dynamic vehicle data you need, delivered directly to your systems.

<CardGroup cols={3}>
  <Card title="Start a tutorial" icon="play" href="/getting-started/tutorials/ios" icontype="duotone">Learn how to configure your first application and connect a vehicle in under 10 minutes.</Card>
  <Card title="Read How-To Guides" href="/getting-started/how-to/configure-permissions" icon="graduation-cap" icontype="duotone">Solve common implementation challenges with step-by-step instructions.</Card>

  <Card title="Connecting Vehicles" href="/getting-started/connect-vehicles" icon="mobile" icontype="duotone">
    Learn how to use our patented consent management authorization flow, to connect vehicles to your application.
  </Card>

  <Card title="Help Center" href="/help/what-is-smartcar" icon="life-ring" icontype="duotone">
    Visit our Help Center for FAQs, troubleshooting tips, and to contact support.
  </Card>

  <Card title="Integrations" href="/getting-started/integration-overview" icon="square-terminal" icontype="duotone">Dive deep into our Smartcar integrations and learn how to connect with various services.</Card>
  <Card title="Browse our SDKs" href="/connect/connect-sdks" icon="computer" icontype="duotone">Connect with other developers, share ideas, and get help.</Card>
</CardGroup>

Learn how to connect your app to Smartcar so you can access vehicle data like odometer, location, battery level, issue vehicle commands, and more. In this guide, you’ll register your app, walk through the Smartcar Connect flow, and configure a webhook to receive data.

By the end of this guide, you’ll have a working setup with access to a vehicle’s data through Smartcar’s platform.

## Prerequisites

Before you begin, you’ll need:

* A [Smartcar Account](https://dashboard.smartcar.com)
* Your Application ID and Secret (found in the [Smartcar Dashboard](https://dashboard.smartcar.com/configuration))
* An application with a redirect URI (e.g. a local development server or staging environment)

<Steps>
  <Step title="Step 1: Register & Configure Your Application">
    1. Log in or sign up via the [Smartcar Dashboard](https://dashboard.smartcar.com)
    2. Fill in your app name, description, and redirect URI in the configuration page of the dashboard.
    3. Copy your `Client ID` and `Client Secret` in a safe location. These credentials identify your app during the authorization process. **Do not commit your client secret to version control**.
    4. Select the data you want to access from vehicles by choosing the data signals (e.g. `odometer`, `location`, etc.).

    The necessary permissions will be derived from these signals and presented to your users.
  </Step>

  <Step title="Step 2: Start Connecting Vehicles via Smartcar Connect">
    [Smartcar Connect](/connect) is an OAuth 2.0 consent flow that lets your users link their vehicles securely.

    The vehicle access tab in the Smartcar Dashboard will generate a Connect URL for you. You can also generate the URL programmatically using one of our SDKs.

    ```javascript  theme={null}

    const link = new Smartcar.AuthClient({ //Smartcar frontend SDK
      clientId: 'YOUR_CLIENT_ID',
      redirectUri: 'YOUR_REDIRECT_URI',
      scope: ['read_vehicle_info', 'read_odometer'], // add other scopes as needed
      mode: 'live', // use 'simulated' for testing with simulated vehicles
    });

    window.location.href = link.getAuthUrl();
    ```

    This will take your user to the Smartcar Connect screen to authorize access.
  </Step>

  <Step title="Step 3: Exchange Authorization Code for Access Tokens">
    After the user grants access, Smartcar redirects back to your app with an authorization code. This is where the redirect URI you configured earlier comes into play.

    Use this code in your backend to exchange for access and refresh tokens:

    ```javascript  theme={null}
    const smartcar = require('smartcar'); //Smartcar backend SDK

    const client = new smartcar.AuthClient({
      clientId: 'YOUR_CLIENT_ID',
      clientSecret: 'YOUR_CLIENT_SECRET',
      redirectUri: 'YOUR_REDIRECT_URI',
      mode: 'live', //use 'simulated' for testing with simulated vehicles
    });

    const access = await client.exchangeCode('AUTHORIZATION_CODE_FROM_QUERY');

    ```

    You’ll receive:

    * `accessToken`: used to make API calls
    * `refreshToken`: used to obtain new access tokens
  </Step>

  <Step title="Step 4: Configure an Integration To Receive Vehicle Data">
    Our recommended method is to use webhooks, allowing you to choose triggers (e.g. location changes, battery state of charge changes) and the data to be sent upon those triggers.

    **Quick Start**: Deploy a production-ready webhook receiver in minutes with our [Webhook Receiver Recipe](/getting-started/tutorials/webhook-receiver-recipe) - a complete AWS serverless solution.
  </Step>
</Steps>

#### What’s Next?

* [Learn how to configure your application](/getting-started/configure-application).
* [Connect your first vehicle](/getting-started/connect-vehicles).
* [Build your first integration](/getting-started/integration-overview).

Need help? Visit our Support Portal or contact us at [support@smartcar.com](mailto:support@smartcar.com).

Let’s get building!


# Android Tutorial
Source: https://smartcar.com/docs/getting-started/tutorials/android

In this tutorial, we will use the Android SDK to integrate Connect into your application.

<Warning>
  Our frontend SDKs handle getting an authorization code representing a vehicle owner's consent for your application to interact with their vehicle
  for the requested permissions. In order to make requests to a vehicle, please use one of our [backend SDKs](/api-reference/api-sdks).

  For security, token exchanges and requests to vehicles **should not** be made client side.
</Warning>

# Overview

<Frame type="simple">
  <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/android/overview.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=e55ce733a1529f22994defa49ca2ca8c" data-og-width="850" width="850" data-og-height="510" height="510" data-path="images/android/overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/android/overview.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=8ded54ca1d073b539d48542e44032e6b 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/android/overview.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=7a3b55192cd87e42e5b5e0cc51ef81f0 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/android/overview.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=050ddfb32ff8eafb4a907ee1601a653a 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/android/overview.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=1e8414af0bb59139f78d4ff54072a129 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/android/overview.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=97d5a32bc895768e53ba94f9139c751a 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/android/overview.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=202b2b7d1ff4c26cbc91677a30d692ea 2500w" />
</Frame>

<br />

1. The Mobile Application launches a `Chrome Custom Tab` with Smartcar Connect to request access to a user’s vehicle.
   On Connect, the user logs in with their vehicle credentials and grants the Application access to their vehicle.
2. The `Chrome Tab` is redirected to a specified `REDIRECT_URI` along with an authorization `code`.
   This will be the custom scheme set on the application. The Smartcar Android receives the authorization `code` in a view listening
   for the specified custom scheme URI, and passes it to the Mobile Application.
3. The Mobile Application sends the received authorization `code` to the Application’s backend service.
4. The Application sends a request to the Smartcar API. This request contains the authorization code along with the Application’s
   `CLIENT_ID` and `CLIENT_SECRET`.
5. In response, Smartcar returns an `ACCESS_TOKEN` and a `REFRESH_TOKEN`.
6. Using the `ACCESS_TOKEN`, the Application can now send requests to the Smartcar API. It can access protected resources and send commands
   to and from the user’s vehicle via the backend service.

# Prerequisites

* [Sign up](https://dashboard.smartcar.com/signup) for a Smartcar account.
* Make a note of your `CLIENT_ID` and `CLIENT_SECRET` from the **Configuration** section on the Dashboard.
* Add a custom scheme redirect URI to your application configuration.
* Add the `app_server` redirect URI from [Setup step 2.](/getting-started/tutorials/android#setup) to your application configuration.

<Note>
  For Android, we require the custom URI scheme to be in the format of `sc` + `clientId` + `://` + `hostname`.
  For now, you can just set it to `sc` + `clientId` + `://exchange`.

  Please see our [Connect Docs](/connect/dashboard-config#redirect-uris) for more information.
</Note>

# Setup

1. Clone our repo and install the required dependencies:
   ```bash  theme={null}
   $git clone https://github.com/smartcar/getting-started-android-sdk.git
   ```
   <Note>
     Do not “checkout from version control” with the Getting Started repo in Android Studio, as it will not open the proper module.
   </Note>

2. Open `getting-started-android-sdk/tutorial` in Android Studio as an existing project and build from existing sources.
   Android Studio should automatically import the required dependencies and build gradle. We're setting `app_server` to `http://10.0.2.2:8000`
   to pass the authorization `code` from the [Handle the Response](/getting-started/tutorials/android#handle-the-response) step later on in the tutorial to our backend.
   ```xml strings.xml theme={null}
   <string name="smartcar_auth_scheme">sc[yourClientId]</string>
   <string name="client_id">[yourClientId]</string>
   <string name="app_server">http://10.0.2.2:8000</string>
   ```

# Build your Connect URL

1. Instantiate a `smartcarAuth` object in the `onCreate` function of the `MainActivity`.
   ```java MainActivity.java theme={null}
   // TODO: Authorization Step 1a: Initialize the Smartcar object
   private static String CLIENT_ID;
   private static String REDIRECT_URI;
   private static String[] SCOPE;
   private SmartcarAuth smartcarAuth;

   protected void onCreate(Bundle savedInstanceState) {
       ...
       
       // TODO: Authorization Step 1b: Initialize the Smartcar object
       CLIENT_ID = getString(R.string.client_id);
       REDIRECT_URI = getString(R.string.smartcar_auth_scheme) + "://" + getString(R.string.smartcar_auth_host);
       SCOPE = new String[]{"required:read_vehicle_info"};
       
       smartcarAuth = new SmartcarAuth(
           CLIENT_ID,
           REDIRECT_URI,
           SCOPE,
           true,
           new SmartcarCallback() {
               // TODO: Authorization Step 3b: Receive an authorization code
           }
       );
   }
   ```

<Info>
  The Android SDK does not support `simulated` mode at this time - only `test` and `live`.
  Feel free to set `testMode` to `false` where you instantiate your `SmartcarAuth` object to
  connect to a real vehicle.
</Info>

2. The Android application will launch a Chrome Tab with Smartcar Connect to request access to a user’s vehicle.
   On Connect, the user logs in with the username and password for their vehicle’s connected services account and grants the application access to their vehicle.

   To launch Connect, we can use the `addClickHandler` function that our `smartcarAuth` object has access to.

   ```java MainActivity.java theme={null}
   // TODO: Authorization Step 2: Launch Connect
   smartcarAuth.addClickHandler(appContext, connectButton);
   ```

# Registering your Custom Scheme

Once a user has authorized the application to access their vehicle, the user is redirected to the `REDIRECT_URI` with an authorization `code` as a query parameter.

Android applications use custom URI schemes to intercept calls and launch the relevant application. This is defined within the `AndroidManifest`.

```xml AndroidManifest.xml theme={null}
<!-- TODO: Authorization Step 3a: Receive an authorization code -->
<activity android:name="com.smartcar.sdk.SmartcarCodeReceiver">
    <intent-filter>
        <action android:name="android.intent.action.VIEW" />
        <category android:name="android.intent.category.DEFAULT" />
        <category android:name="android.intent.category.BROWSABLE" />
        <data
            android:host="@string/smartcar_auth_host"
            android:scheme="@string/smartcar_auth_scheme" />
    </intent-filter>
</activity>
```

# Handle the response

Using the Android SDK, the application can receive the code in the `SmartcarCallback` object passed into the `SmartcarAuth` object.

```java MainActivity.java theme={null}
smartcarAuth = new SmartcarAuth(
    CLIENT_ID,
    REDIRECT_URI,
    SCOPE,
    true,
    new SmartcarCallback() {
        // TODO: Authorization Step 3b: Receive an authorization code
        @Override
        public void handleResponse(final SmartcarResponse smartcarResponse) {
            Log.i("MainActivity", smartcarResponse.getCode());

            // TODO: Request Step 1: Obtain an access token

            //TODO: Request Step 2: Get vehicle information
        }
    }
);
```

# Launching Connect

Build your application in Android Studio and click on the **Connect your vehicle** button.

<Info>
  This tutorial configures Connect to launch in `test` mode by default.
  In `test` mode, any `username` and `password` is valid for each brand.
</Info>

Smartcar showcases all the permissions your application is asking for - `read_vehicle_info` in this case.
Once you have logged in and accepted the permissions, you should see your authorization `code` printed to your console.

# Getting your first access token

After receiving the authorization `code`, your iOS application must exchange it for an `ACCESS_TOKEN`. To do so, we can send
the code to a backend service. Let’s assume our backend service contains an endpoint `/exchange` that receives an authorization `code` as a query parameter and exchanges it for an `ACCESS_TOKEN`.

```swift ViewController.swift theme={null}
// TODO: Obtain an access token
public void handleResponse(final SmartcarResponse smartcarResponse) {
    Log.i("MainActivity", smartcarResponse.getCode());

    final OkHttpClient client = new OkHttpClient();

    // TODO: Request Step 1: Obtain and access token

    // Request can not run on the Main Thread
    // Main Thread is used for UI and therefore can not be blocked
    new Thread(new Runnable() {
        @Override
        public void run() {
    
            // send request to exchange the auth code for the access token
            Request exchangeRequest = new Request.Builder()
                .url(getString(R.string.app_server) + "/exchange?code=" + smartcarResponse.getCode())
                .build();
        
            try {
                client.newCall(exchangeRequest).execute();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }).start();
}
```

<Warning>
  Notice that our backend service **does not** return the `ACCESS_TOKEN`.
  This is by design. For security, our frontend should never have access
  to the `ACCESS_TOKEN` and should always be stored in the backend.
</Warning>

# Getting data from a vehicle

Once the backend has the `ACCESS_TOKEN`, it can send requests to a vehicle using the Smartcar API. The Android app will
have to send a request to the backend service which in turn sends a request to Smartcar. We have to do this because
our frontend **does not** have the `ACCESS_TOKEN`.

Assuming our backend has a `/vehicle` endpoint that returns the information of a user’s vehicle, we can make this query in
our `completion callback` and start another `activity` to show the returned vehicle attributes.

```java MainActivity.java theme={null}
public void handleResponse(final SmartcarResponse smartcarResponse) {
    ...
    
    // TODO: Request Step 2: Get vehicle information

    // send request to retrieve the vehicle info
    Request infoRequest = new Request.Builder()
        .url(getString(R.string.app_server) + "/vehicle")
        .build();
    
    try {
        Response response = client.newCall(infoRequest).execute();
    
        String jsonBody = response.body().string();
        JSONObject JObject = new JSONObject(jsonBody);
    
        String make = JObject.getString("make");
        String model = JObject.getString("model");
        String year = JObject.getString("year");
    
        Intent intent = new Intent(appContext, DisplayInfoActivity.class);
        intent.putExtra("INFO", make + " " + model + " " + year);
        startActivity(intent);
    } catch (IOException e) {
        e.printStackTrace();
    } catch (JSONException e) {
        e.printStackTrace();
    }
}
```

# Setting up your backend

Now that our frontend is complete, we will need to create a backend service that contains the logic for the `/exchange` and `/vehicle` endpoints.
You can use any of our backend SDKs below to set up the service starting from the **Obtaining an Access Token** step.

<Note>
  When setting up the environment variables for your  backend SDK, make sure to set `REDIRECT_URI` to the custom scheme
  used for this tutorial i.e. `sc + "clientId" + ://exchange`.
</Note>

<CardGroup cols={4}>
  <Card title="Java" icon="java" href="/getting-started/how-to/architecture-design" icontype="duotone" />

  <Card title="Node.js" href="/getting-started/how-to/architecture-design" icon="node-js" icontype="duotone" />

  <Card title="Python" icon="python" href="/getting-started/how-to/architecture-design" icontype="duotone" />

  <Card title="Ruby" href="/getting-started/how-to/architecture-design" icon="gem" icontype="duotone" />
</CardGroup>


# Backend SDK Tutorials
Source: https://smartcar.com/docs/getting-started/tutorials/backend

In this tutorial, we will go over how to integrate Connect into your application and make requests to a vehicle using our backend SDKs.

# Overview

<Frame type="simple">
  <img src="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/backend-sdks/overview.png?fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=c14eeafc1d4ff0ae02482d59c66d451e" data-og-width="850" width="850" data-og-height="491" height="491" data-path="images/backend-sdks/overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/backend-sdks/overview.png?w=280&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=a750458073489eac8055cdb934501cff 280w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/backend-sdks/overview.png?w=560&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=07bb6214d5299d1307fac596f1f9ed62 560w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/backend-sdks/overview.png?w=840&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=92e3e33f2a10f43968b4b54283aaf562 840w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/backend-sdks/overview.png?w=1100&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=d6e7165c1893d87298c28e6c66fef71d 1100w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/backend-sdks/overview.png?w=1650&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=6804f3ac4768b14e517fb07c3448ca6a 1650w, https://mintcdn.com/smartcar-docs/NtuX9OSBHLxFwWIa/images/backend-sdks/overview.png?w=2500&fit=max&auto=format&n=NtuX9OSBHLxFwWIa&q=85&s=bacb0ca36a1b1a5f5c91a6ef0bfb06cc 2500w" />
</Frame>

<br />

1. The Application redirects the user to Smartcar Connect to request access to the user’s vehicle. In Connect,
   the user logs in with their vehicle credentials and grants the Application access to their vehicle.
2. The user’s browser is redirected to a specified `REDIRECT_URI`. The Application Server, which is listening
   at the `REDIRECT_URI`, will retrieve the authorization code from query parameters sent to the `REDIRECT_URI`.
3. The Application sends a request to the Smartcar API. This request contains the authorization `code` along with
   the Application’s `CLIENT_ID` and `CLIENT_SECRET`.
4. In response, Smartcar returns an `ACCESS_TOKEN` and a `REFRESH_TOKEN`.
5. Using the `ACCESS_TOKEN`, the Application can now send requests to the Smartcar API. It can access protected resources and send commands
   to and from the user’s vehicle via the backend service.

# Prerequisites

* [Sign up](https://dashboard.smartcar.com/signup) for a Smartcar account.
* Make a note of your `CLIENT_ID` and `CLIENT_SECRET` from the **Configuration** section on the Dashboard.
* Add the following `REDIRECT_URI` to your application configuration: `http://localhost:8000/exchange`

# Setup

1. Clone the repo for the SDK you want to use and install the required dependencies:
   <CodeGroup>
     ```bash Node theme={null}
     $ git clone https://github.com/smartcar/getting-started-express.git
     $ cd getting-started-express/tutorial
     $ npm install
     ```

     ```bash Python theme={null}
     $ git clone https://github.com/smartcar/getting-started-python-sdk.git
     $ cd getting-started-python-sdk/tutorial
     $ pip install -r requirements.txt
     ```

     ```bash Java theme={null}
     $ git clone https://github.com/smartcar/getting-started-java-sdk.git
     $ cd getting-started-java-sdk/tutorial
     $ gradlew build
     ```

     ```bash Ruby theme={null}
     $ git clone https://github.com/smartcar/getting-started-ruby-sdk.git
     $ cd getting-started-ruby-sdk/tutorial
     $ bundle install
     $ ruby app.rb
     ```
   </CodeGroup>
2. You will also have to set the following environment variables

<Warning>
  If you've used one of our frontend SDKs to integrate connect, you'll want to set the
  `SMARTCAR_REDIRECT_URI` environment variable to the URI you used for that application.
</Warning>

```bash  theme={null}
$export SMARTCAR_CLIENT_ID=<your-client-id>
$export SMARTCAR_CLIENT_SECRET=<your-client-secret>
$export SMARTCAR_REDIRECT_URI=http://localhost:8000/exchange
```

<Note>
  If you are using Windows, ensure you are appropriately setting environment variables for your shell.
  Please refer to [this post](https://stackoverflow.com/questions/9249830/how-can-i-set-node-env-production-on-windows/9250168#9250168) which details how to set environment variables on Windows.
</Note>

<br />

# Build your Connect URL

1. Instantiate a `Smartcar` object in the constructor of the App component.
   <CodeGroup>
     ```js index.js theme={null}
     const client = new smartcar.AuthClient({
         mode: 'simulated',
     });
     ```

     ```python main.py theme={null}
     client = smartcar.AuthClient(mode='simulated')
     ```

     ```java Main.java theme={null}
     String mode = "simulated";

     AuthClient client = new AuthClient.Builder()
     .mode(mode)
     .build();
     ```

     ```ruby index.rb theme={null}
     @@client = Smartcar::AuthClient.new({
         mode: 'simulated',
     })
     ```
   </CodeGroup>

<Info>
  Feel free to set `mode` to `simulated` or `live` where you instantiate your `Smartcar` object to
  connect to a simulated or real vehicle.
</Info>

2. A Server-side rendered application will redirect to Smartcar Connect to request access to a user’s vehicle.
   On Connect, the user logs in with the username and password for their vehicle’s connected services account
   and grants the application access to their vehicle.

   To launch Connect, we need to redirect the user to the appropriate URL. We can make use of the `AUTHORIZATION_URL`
   function in our Smartcar object and redirect the user to the URL to launch the Connect flow.

   <CodeGroup>
     ```js index.js theme={null}
     app.get('/login', function(req, res) {
         const scope = ['read_vehicle_info'];
         const authUrl = client.getAuthUrl(scope);

         res.render('home', {
             url: authUrl,
         });
     });
     ```

     ```python main.py theme={null}
     @app.route('/login', methods=['GET'])
     def login():
         scope = ['read_vehicle_info']
         auth_url = client.get_auth_url(scope)
         return redirect(auth_url)        
     ```

     ```java Main.java theme={null}
     get("/login", (req, res) -> {
         // TODO: Authorization Step 2: Launch Smartcar authentication dialog
         String[] scope = {"read_odometer"};
         String link = client.authUrlBuilder(scope).build();
         res.redirect(link);
         return null;
     });
     ```

     ```ruby index.rb theme={null}
     get "/login" do
         redirect @@client.get_auth_url(['required:read_vehicle_info'])
     end
     ```
   </CodeGroup>

<br />

# Handle the response

Once a user has authorized the application to access their vehicle, the user is redirected to the `REDIRECT_URI`
with an authorization `code` as a query parameter. In the previous section, we had set our `REDIRECT_URI` as `localhost:8000/exchange`.
Now, our server can be set up as follows to receive the authorization `code`.

<CodeGroup>
  ```js index.js theme={null}
  app.get('/exchange', function(req, res) {
  const code = req.query.code;

  console.log(code);

  res.sendStatus(200);
  });
  ```

  ```python main.py theme={null}
  @app.route('/exchange', methods=['GET'])
  def exchange():
      code = request.args.get('code')
      
      print(code)
      
      return '', 200      
  ```

  ```java Main.java theme={null}
  get("/exchange", (req, res) -> {
      String code = req.queryMap("code").value();

      System.out.println(code);

      return "";
  });
  ```

  ```ruby index.rb theme={null}
  get "/exchange" do
      code = params[:code]

      puts code

      "OK"
  end
  ```
</CodeGroup>

<br />

# Launching Connect

Let’s try authenticating a vehicle! Restart your server, open up your browser and go to `http://localhost:8000/login`

<CodeGroup>
  ```bash Node theme={null}
  $node index.js
  ```

  ```bash Python theme={null}
  $python main.py
  ```

  ```bash Java theme={null}
  $./gradlew run
  ```

  ```bash Ruby theme={null}
  $bundle exec ruby app.rb
  ```
</CodeGroup>

<br />

<Info>
  This tutorial configures Connect to launch in `test` mode by default.
  In `test` mode, any `username` and `password` is valid for each brand.
</Info>

Smartcar showcases all the permissions your application is asking for - `read_vehicle_info` in this case.
Once you have logged in and accepted the permissions, you should see your authorization `code` printed to your console.

<br />

# Getting your first access token

<Note>
  If you've used one of our frontend SDKs to integrate Connect, this is where you'll need to fetch your access token.
</Note>

In the previous section, we retrieved an authorization `code`. The application must exchange the code for an `ACCESS_TOKEN` to make a request.
After receiving the ACCESS\_TOKEN, the user can be redirected to the `/vehicle` route.

<CodeGroup>
  ```js index.js theme={null}
  // Global variable to save our access_token
  let access;

  app.get('/exchange', async function(req, res) {
      const code = req.query.code;
      
      // Access our global variable and store our access tokens.
      // In a production app you'll want to store this in some 
      // kind of persistent storage
      access = await client.exchangeCode(code);
      res.redirect('/vehicle');
  });
  ```

  ```python main.py theme={null}
  # Global variable to save our access_token
  access = None

  @app.route('/exchange', methods=['GET'])
  def exchange():
      code = request.args.get('code')

      # Access our global variable and store our access tokens.
      # In a production app you'll want to store this in some
      # kind of persistent storage
      global access

      access = client.exchange_code(code)
      return redirect('/vehicle')      
  ```

  ```java Main.java theme={null}
  // Global variable to save our access_token
  private static String access;

  public static void main(String[] args) {

      get("/exchange", (req, res) -> {
          String code = req.queryMap("code").value();

          Auth auth = client.exchangeCode(code);
          
          // Access our global variable and store our access tokens.
          // In a production app you'll want to store this in some kind of persistent storage
          access = auth.getAccessToken();
          
          res.redirect("/vehicle");
          return null;
      })
  }
  ```

  ```ruby index.rb theme={null}
  # Global variable to store the token
  @@token = ''

  get "/exchange" do
      code = params[:code]
      # Access our global variable and store our access tokens.
      # In a production app you'll want to store this in 
      # some kind of persistent storage
      @@token = @@client.exchange_code(code)[:access_token]
      redirect '/vehicle'
  end
  ```
</CodeGroup>

<br />

# Getting data from a vehicle

1. Once the backend service or server-side application has the `ACCESS_TOKEN`, it can send requests to a vehicle using the Smartcar API.
   First we'll need to fetch the `vehicle_id`s associated with the `ACCESS_TOKEN`, then fetch vehicle attributes for one of them. After
   receiving the `vehicle_attributes` object, we can render it in a simple table on the page.
   <CodeGroup>
     ```js index.js theme={null}
     app.get('/vehicle', async function(req, res) {
         // Get the smartcar vehicleIds associated with the access_token
         const { vehicles } = await smartcar.getVehicles(access.accessToken);
         
         // Instantiate the first vehicle in the vehicle id list
         const vehicle = new smartcar.Vehicle(vehicles[0], access.accessToken);

         // Make a request to Smartcar API
         const attributes = await vehicle.attributes();
         res.render('vehicle', {
             info: attributes, 
         });
     });
     ```

     ```python main.py theme={null}
     @app.route('/vehicle', methods=['GET'])
     def get_vehicle():
         # Access our global variable to retrieve our access tokens
         global access
         
         # Get the smartcar vehicleIds associated with the access_token
         vehicles = smartcar.get_vehicles(access.access_token)
         vehicle_ids = vehicles.vehicles
         
         # Instantiate the first vehicle in the vehicle id list
         vehicle = smartcar.Vehicle(vehicle_ids[0], access.access_token)

         # Make a request to Smartcar API
         attributes = vehicle.attributes()
         return jsonify({
             "make": attributes.make,
             "model": attributes.model,
             "year": attributes.year    
         })
         '''
         {
             "make": "TESLA",
             "model": "Model S",
             "year": 2014
         }
         '''
     ```

     ```java Main.java theme={null}
     get("/vehicle", (req, res) -> {

         // Get the smartcar vehicleIds associated with the access_token
         VehicleIds vehiclesResponse = Smartcar.getVehicles(access);
         String[] vehicleIds = vehiclesResponse.getVehicleIds();
         
         // Instantiate the first vehicle in the vehicle id list
         Vehicle vehicle = new Vehicle(vehicleIds[0], access);

         // Make a request to Smartcar API
         VehicleAttributes attributes = vehicle.attributes();
         System.out.println(gson.toJson(attributes));
         
         // {
         //     "id": "36ab27d0-fd9d-4455-823a-ce30af709ffc",
         //     "make": "TESLA",
         //     "model": "Model S",
         //     "year": 2014
         // }
         
         res.type("application/json");
         return gson.toJson(attributes);
     })
     ```

     ```ruby index.rb theme={null}
     get "/vehicle" do
         code = params[:code]

         # Get the smartcar vehicleIds associated with the access_token
         vehicles =  Smartcar::Vehicle.get_vehicle(token: @@token)
         vehicle_ids = vehicles.vehicles
         
         # Instantiate the first vehicle in the vehicle id list
         vehicle = Smartcar::Vehicle.new(token: @@token, id: vehicle_ids.first)  
         
         # Get the vehicle_attributes object for vehicle
         vehicle_attributes = vehicle.attributes
         vehicle_attributes.slice(*%I(id make model year)).to_json
     end
     ```
   </CodeGroup>

2. Restart your sever and head back to `http://localhost:8000/login` to go through Connect and make your first API request!
   <CodeGroup>
     ```bash Node theme={null}
     $node index.js
     ```

     ```bash Python theme={null}
     $python main.py
     ```

     ```bash Java theme={null}
     $./gradlew run
     ```

     ```bash Ruby theme={null}
     $bundle exec ruby app.rb
     ```
   </CodeGroup>


# iOS Tutorial
Source: https://smartcar.com/docs/getting-started/tutorials/ios

In this tutorial, we will use the iOS SDK to integrate Connect into your application.

<Warning>
  Our frontend SDKs handle getting an authorization code representing a vehicle owner's consent for your application to interact with their vehicle
  for the requested permissions. In order to make requests to a vehicle, please use one of our [backend SDKs](/api-reference/api-sdks).

  For security, token exchanges and requests to vehicles **should not** be made client side.
</Warning>

<br />

# Overview

<Frame type="simple">
  <img src="https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/ios/overview.png?fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=45bac644e60e25a9e5a92a550e398f37" data-og-width="850" width="850" data-og-height="510" height="510" data-path="images/ios/overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/ios/overview.png?w=280&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=a61885111dee58865db17980113e5035 280w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/ios/overview.png?w=560&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=b8651a42e98db8d2eab1c451f37f6995 560w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/ios/overview.png?w=840&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=bdc2acc2ab6a04e66c4717359d4aa74b 840w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/ios/overview.png?w=1100&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=ac8a17905c843637daf985634c01cf76 1100w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/ios/overview.png?w=1650&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=cf6a43d011422f21f72e89fc7422fcef 1650w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/ios/overview.png?w=2500&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=2e1b4272ed0a314b03128f615747b033 2500w" />
</Frame>

<br />

1. The Mobile Application launches a `SafariView` with Smartcar Connect to request access to a user’s vehicle.
   On Connect, the user logs in with their vehicle credentials and grants the Application access to their vehicle.
2. The `SafariView` is redirected to a specified `REDIRECT_URI` along with an authorization `code`.
   This will be the custom scheme set on the application. The Smartcar iOS SDK receives the authorization `code` in a view listening
   for the specified custom scheme URI, and passes it to the Mobile Application.
3. The Mobile Application sends the received authorization `code` to the Application’s back-end service.
4. The Application sends a request to the Smartcar API. This request contains the authorization code along with the Application’s
   `CLIENT_ID` and `CLIENT_SECRET`.
5. In response, Smartcar returns an `ACCESS_TOKEN` and a `REFRESH_TOKEN`.
6. Using the `ACCESS_TOKEN`, the Application can now send requests to the Smartcar API. It can access protected resources and send commands
   to and from the user’s vehicle via the backend service.

# Prerequisites

* [Sign up](https://dashboard.smartcar.com/signup) for a Smartcar account.
* Make a note of your `CLIENT_ID` and `CLIENT_SECRET` from the **Configuration** section on the Dashboard.
* Add a custom scheme redirect URI to your application configuration.
* Add the `appServer` redirect URI from [step 2](/getting-started/tutorials/ios/#setup) below to your application configuration.

<Note>
  For iOS, we require the custom URI scheme to be in the format of `sc` + `clientId` + `://` + `hostname`.
  For now, you can just set it to `sc` + `clientId` + `://exchange`.

  Please see our [Connect Docs](/connect/dashboard-config#redirect-uris) for more information.
</Note>

# Setup

1. Clone our repo and install the required dependencies:
   ```bash  theme={null}
   $git clone https://github.com/smartcar/getting-started-ios-sdk.git
   $cd getting-started-ios-sdk/tutorial
   $pod install
   $open getting-started-ios-sdk.xcworkspace
   ```
2. Set the following constants in `Constants.swift`. We're setting `appServer` to `http://localhost:8000` to pass the authorization `code` from
   the [Handle the Response](/getting-started/tutorials/ios#handle-the-response) step later on in the tutorial to our backend.
   ```swift Constants.swift theme={null}
   struct Constants {
       static let clientId = "<your-client-id>";
       static let appServer = "http://localhost:8000";
   }
   ```

# Build your Connect URL

Instantiate a `SmartcarAuth` object in the `viewdidLoad` function of the `ViewController`.
The iOS application will launch a `WebView` with Connect to request access to a user’s vehicle.
On Connect, the user logs in with the username and password for their vehicle’s connected services account
and grants the application access to their vehicle.

To launch Connect, we can use the `launchAuthFlow` function that our `SmartcarAuth` object has access to. We can place
this within the `connectPressed` action function.

```swift ViewController.swift theme={null}
let appDelegate = UIApplication.shared.delegate as! AppDelegate

func completionHandler(code: String?, state: String?, virtualKeyUrl: String?, err: AuthorizationError?,) -> Void {
// Receive authorization code
}

appDelegate.smartcar = SmartcarAuth(
  clientId: "afb0b7d3-807f-4c61-9b04-352e91fe3134",
  redirectUri: "scafb0b7d3-807f-4c61-9b04-352e91fe3134://exchange",
  scope: ["read_vin", "read_vehicle_info", "read_odometer"],
  mode: SCMode.simulated, //use SCMode.live to connect to a real vehicles
  completionHandler: completionHandler
)
let smartcar = appDelegate.smartcar

// Generate a Connect URL
let authUrl = smartcar.authUrlBuilder().build()

// Pass in the generated Connect URL and a UIViewController
smartcar.launchAuthFlow(url: authUrl, viewController: viewController)
```

<br />

# Registering your Custom Scheme

Once a user has authorized the application to access their vehicle, the user is redirected to the `REDIRECT_URI` with an authorization code as a query parameter.

iOS applications use custom URI schemes to intercept calls and launch the relevant application. This is defined within the `Info.plist`.

1. Open up `Info.plist` and click on the grey arrow next to **URL types**.
2. Next, click on the grey arrow next to the `Item 0` dictionary and `URL Schemes` array.
3. Finally, set your `Item 0` string to the redirect URI you set up in the [Prerequisites](/getting-started/tutorials/ios#prerequisites) section (i.e. 'sc' + clientId).

<Frame>
  <img src="https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/ios/info-plist.png?fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=f44c4b8181efc5f04fd5032a3b22829d" data-og-width="866" width="866" data-og-height="464" height="464" data-path="images/ios/info-plist.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/ios/info-plist.png?w=280&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=811be6c402b564aff3ee32bd8ed317b7 280w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/ios/info-plist.png?w=560&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=77760fa09f368baac7206da5867b6275 560w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/ios/info-plist.png?w=840&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=92e4e79d535d84f17f8b7c324bfac253 840w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/ios/info-plist.png?w=1100&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=b33b563596db365cddb46d19c2e87494 1100w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/ios/info-plist.png?w=1650&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=09fc68c33c02682e8f352e03b658e193 1650w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/ios/info-plist.png?w=2500&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=71e3a80d7430a15c99788daf2ed85b53 2500w" />
</Frame>

<br />

# Handle the response

1. The iOS application will now receive the request in the `application:(_:open:options:)` function within the AppDelegate.
   ```swift AppDelegate.swift theme={null}
   func application(_ application: UIApplication, open url: URL, options: [UIApplicationOpenURLOptionsKey : Any] = [:]) -> Bool {
       {/* TODO: Authorization Step 3a: Receive the authorization code */}
       window!.rootViewController?.presentedViewController?.dismiss(animated: true , completion: nil)
       smartcar!.handleCallback(with: url)
       
       return true
   }
   ```
2. Using the iOS SDK, the application can receive the code in the `completion callback` passed into the `SmartcarAuth` object.
   ```swift AppDelegate.swift theme={null}
   func completion(err: Error?, code: String?, state: String?) -> Any {
       {/* TODO: Authorization Step 3b: Receive the authorization code */}
       print(code!);
       {/* prints out the authorization code */}
   }
   ```

# Launching Connect

Build your application in XCode and click on the **Connect your vehicle** button.

<Info>
  This tutorial configures Connect to launch in `test` mode by default.
  In `test` mode, any `username` and `password` is valid for each brand.
</Info>

Smartcar showcases all the permissions your application is asking for - `read_vehicle_info` in this case.
Once you have logged in and accepted the permissions, you should see your authorization `code` printed to your console.

# Getting your first Access Token

After receiving the authorization `code`, your iOS application must exchange it for an `ACCESS_TOKEN`. To do so, we can send
the code to a backend service. Let’s assume our backend service contains an endpoint `/exchange` that receives an authorization `code` as a query parameter and exchanges it for an `ACCESS_TOKEN`.

```swift ViewController.swift theme={null}
// TODO: Obtain an access token
Alamofire.request("\(Constants.appServer)/exchange?code=\(code!)", method: .get)
    .responseJSON {_ in}
```

<Warning>
  Notice that our backend service **does not** return the `ACCESS_TOKEN`.
  This is by design. For security, our frontend should never have access
  to the `ACCESS_TOKEN` and should always be stored in the backend.
</Warning>

# Getting data from a vehicle

Once the backend has the `ACCESS_TOKEN`, it can send requests to a vehicle using the Smartcar API. The iOS app will
have to send a request to the backend service which in turn sends a request to Smartcar. We have to do this because
our frontend **does not** have the `ACCESS_TOKEN`.

Assuming our backend has a `/vehicle` endpoint that returns the information of a user’s vehicle, we can make this query in
our `completion callback` and segue into another `view` to show the returned  vehicle attributes

```swift ViewController.swift theme={null}
func completion(err: Error?, code: String?, state: String?) -> Any {

    // send request to exchange auth code for access token
    Alamofire.request("\(Constants.appServer)/exchange?code=\(code!)", method: .get).responseJSON {_ in

        // TODO: Request Step 2: Get vehicle information
        // send request to retrieve the vehicle info
        Alamofire.request("\(Constants.appServer)/vehicle", method: .get).responseJSON { response in
            print(response.result.value!)
            
            if let result = response.result.value {
                let JSON = result as! NSDictionary
                
                let make = JSON.object(forKey: "make")!  as! String
                let model = JSON.object(forKey: "model")!  as! String
                let year = String(JSON.object(forKey: "year")!  as! Int)
                
                let vehicle = "\(year) \(make) \(model)"
                self.vehicleText = vehicle
                
                self.performSegue(withIdentifier: "displayVehicleInfo", sender: self)
            }
        }
    }
    
    return ""
}
```

# Setting up your backend

Now that our frontend is complete, we will need to create a backend service that contains the logic for the `/exchange` and `/vehicle` endpoints.
You can use any of our backend SDKs below to set up the service starting from the **Obtaining an Access Token** step.

<Note>
  When setting up the environment variables for your  backend SDK, make sure to set `REDIRECT_URI` to the custom scheme
  used for this tutorial i.e. `sc + "clientId" + ://exchange`.
</Note>

<CardGroup cols={4}>
  <Card title="Java" icon="java" href="/getting-started/tutorials/backend#getting-your-first-access-token" icontype="duotone" />

  <Card title="Node.js" href="/getting-started/tutorials/backend#getting-your-first-access-token" icon="node-js" icontype="duotone" />

  <Card title="Python" icon="python" href="/getting-started/tutorials/backend#getting-your-first-access-token" icontype="duotone" />

  <Card title="Ruby" href="/getting-started/tutorials/backend#getting-your-first-access-token" icon="gem" icontype="duotone" />
</CardGroup>


# React Tutorial
Source: https://smartcar.com/docs/getting-started/tutorials/react

In this tutorial, we will use the JavaScript SDK to integrate Connect into your application.

<Warning>
  Our frontend SDKs handle getting an authorization code representing a vehicle owner's consent for your application to interact with their vehicle
  for the requested permissions. In order to make requests to a vehicle, please use one of our [backend SDKs](/api-reference/api-sdks).

  For security, token exchanges and requests to vehicles **should not** be made client side.
</Warning>

<br />

# Overview

<Frame type="simple">
  <img src="https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/react/overview.png?fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=a030ac9d073b3f69e52e9831b0e41bea" data-og-width="850" width="850" data-og-height="510" height="510" data-path="images/react/overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/react/overview.png?w=280&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=c46752e77889db204b1930062db34936 280w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/react/overview.png?w=560&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=c1d3d7adcbc35bc127407083157060bc 560w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/react/overview.png?w=840&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=6d9ee3d46aee7f0663736122763c1dba 840w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/react/overview.png?w=1100&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=60875fcb463a344e1015b1ec771ae261 1100w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/react/overview.png?w=1650&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=f2e679d7bbf21c310786a5897d70504f 1650w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/react/overview.png?w=2500&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=ed5d7cecf987432ab8992b387ab6d6eb 2500w" />
</Frame>

<br />

1. The Single-Page Application launches a pop-up window with Smartcar Connect to request access to a user’s vehicle.
   It does so by using the Smartcar JavaScript SDK. On Connect, the user logs in with the username and password for
   their vehicle’s connected services account and grants the Application access to their vehicle.
2. The user’s browser is redirected to a specified Smartcar-hosted `REDIRECT_URI` - the Smartcar JavaScript SDK redirect page.
3. The Smartcar JavaScript SDK redirect page will receive an authorization `code` as a query parameter. The redirect page will then
   send the code to the Single-Page Application’s `onComplete` callback using the `postMessage` web API. **This step is handled entirely
   by the JavaScript SDK.**
4. The Single-Page Application sends the received authorization `code` to the Application’s backend service.
5. The Application sends a request to the Smartcar API. This request contains the authorization code along with the Application’s
   `CLIENT_ID` and `CLIENT_SECRET`.
6. In response, Smartcar returns an `ACCESS_TOKEN` and a `REFRESH_TOKEN`.
7. Using the `ACCESS_TOKEN`, the Application can now send requests to the Smartcar API. It can access protected resources and send commands
   to and from the user’s vehicle via the backend service.

# Prerequisites

* [Sign up](https://dashboard.smartcar.com/signup) for a Smartcar account.
* Make a note of your `CLIENT_ID` and `CLIENT_SECRET` from the **Configuration** section on the Dashboard.
* Add the special JavaScript SDK redirect URI to your application configuration.
* Add the `REACT_APP_SERVER` redirect URI from [Setup step 2.](/getting-started/tutorials/react#setup) to your application configuration.

<Note>
  To use the JavaScript SDK, we require the special redirect URI to provide a simpler flow to retrieve authorization codes.
  For this tutorial you can use the following:

  `https://javascript-sdk.smartcar.com/v2/redirect?app_origin=http://localhost:3000`
</Note>

# Setup

1. Clone our repo and install the required dependencies:
   ```bash  theme={null}
   $git clone https://github.com/smartcar/getting-started-javascript-sdk-react.git
   $cd getting-started-javascript-sdk-react/tutorial
   $npm install
   ```
2. Set the following environment variables. We will be setting up a server later for our React front-end to communicate with.
   For now, let’s assume our server is listening on `http://localhost:8000`.
   ```bash  theme={null}
   $export REACT_APP_CLIENT_ID=<your-client-id>
   $export REACT_APP_REDIRECT_URI= https://javascript-sdk.smartcar.com/v2/redirect?app_origin=http://localhost:3000
   $export REACT_APP_SERVER=http://localhost:8000
   ```

<Note>
  Note: If you are using Windows, ensure you are appropriately setting environment variables for your shell.
  Please refer to this post which details how to set environment variables on Windows.
</Note>

# Build your Connect URL

1. Instantiate a `Smartcar` object in the `constructor` of the App component.
   ```js App.jsx theme={null}
   constructor(props) {
   ...
   // TODO: Authorization Step 1: Initialize the Smartcar object
   this.smartcar = new Smartcar({
       clientId: process.env.REACT_APP_CLIENT_ID,
       redirectUri: process.env.REACT_APP_REDIRECT_URI,
       scope: ['required:read_vehicle_info'],
       mode: 'test',
       onComplete: this.onComplete,
   });
   }
   ```

<Snippet file="tutorials/info-mode-callout.mdx" />

2. A single-page application will launch a pop-up window with Smartcar Connect to request access to a user’s vehicle.
   On Connect, the user logs in with the username and password for their vehicle’s connected services account and grants
   the application access to their vehicle.

   To launch Connect, we can use the `openDialog` function that our `Smartcar` object has access to. We can place this is
   an `onClick` handler of an HTML button.

   ```js App.jsx theme={null}
   authorize() {
       // TODO: Authorization Step 2a: Launch Connect
       this.smartcar.openDialog({forcePrompt: true});
   }

   render() {
       // TODO: Authorization Step 2b: Render the Connect component
       return <Connect onClick={this.authorize} />;
   }
   ```

# Handle the response

1. Once a user has authorized the application to access their vehicle, the user is redirected to the `redirect_uri` with an
   authorization code as a query parameter and the pop-up dialog is closed. Using the JavaScript SDK, the frontend can
   receive this `code` in the `onComplete` callback passed into the `Smartcar` object.
   ```js App.jsx theme={null}
   onComplete(err, code, status) {
       //TODO: Authorization Step 3: Receive the authorization code
       console.log(code);
       //prints out the authorization code
   };
   ```

# Launching Connect

Restart your server, open up your browser and go to `http://localhost:3000/login`. You should be reciderect to Smartcar Connect.

<Info>
  This tutorial configures Connect to launch in `test` mode by default.
  In `test` mode, any `username` and `password` is valid for each brand.
</Info>

Smartcar showcases all the permissions your application is asking for - `read_vehicle_info` in this case.
Once you have logged in and accepted the permissions, you should see your authorization `code` printed to your console.

# Getting your first access token

After receiving the authorization code, the React application must exchange it for an `ACCESS_TOKEN`. To do so, we can send
the code to the backend service which we will implement in a bit. Until then, let’s assume our backend service contains
an endpoint `/exchange` that receives an authorization code as a query parameter and exchanges it for an `ACCESS_TOKEN`.

We can add this logic in our `onComplete` callback

```js App.jsx theme={null}
onComplete(err, code, status) {
  // TODO: Request Step 1: Obtain an access token
  return axios
    .get(`${process.env.REACT_APP_SERVER}/exchange?code=${code}`);
}

```

# Getting data from a vehicle

Once the back-end has the `ACCESS_TOKEN`, it can send requests to a vehicle using the Smartcar API. The React app will
have to send a request to the backend service which in turn sends a request to Smartcar. We have to do this because
our frontend does not have the `ACCESS_TOKEN`.

Assuming our backend has a `/vehicle` endpoint that returns the information of a user’s vehicle, we can make this query in
our `completion callback` and and set the state of the React app with the returned vehicle attributes.

```js App.jsx theme={null}
onComplete(err, code, status) {
  // TODO: Request Step 2a: Get vehicle information
  return axios
    .get(`${process.env.REACT_APP_SERVER}/exchange?code=${code}`)
    .then(_ => {
      return axios.get(`${process.env.REACT_APP_SERVER}/vehicle`);
    })
    .then(res => {
      this.setState({vehicle: res.data});
    });
}

```

Now that we have the vehicle attributes, we can render a simple Vehicle component that shows the vehicle attributes in a table.

```js App.jsx theme={null}
render() {
  // TODO: Request Step 2b: Get vehicle information
  return Object.keys(this.state.vehicle).length !== 0 ? (
    <Vehicle info={this.state.vehicle} />
  ) : (
    <Connect onClick={this.authorize} />
  );
}
```

# Setting up your backend

Now that our frontend is complete, we will need to create a backend service that contains the logic for the `/exchange` and `/vehicle` endpoints.
You can use any of our backend SDKs below to set up the service starting from the **Obtaining an access token** step.

<Note>
  When setting up the environment variables for your  backend SDK, make sure to set `REDIRECT_URI` to the custom scheme
  used for this tutorial i.e. `https://javascript-sdk.smartcar.com/v2/redirect?app_origin=http://localhost:3000`.
</Note>

<CardGroup cols={4}>
  <Card title="Java" icon="java" href="/getting-started/how-to/architecture-design" icontype="duotone" />

  <Card title="Node.js" href="/getting-started/how-to/architecture-design" icon="node-js" icontype="duotone" />

  <Card title="Python" icon="python" href="/getting-started/how-to/architecture-design" icontype="duotone" />

  <Card title="Ruby" href="/getting-started/how-to/architecture-design" icon="gem" icontype="duotone" />
</CardGroup>


# Webhook Receiver Recipe
Source: https://smartcar.com/docs/getting-started/tutorials/webhook-receiver-recipe

Deploy a production-ready AWS serverless webhook receiver in minutes using our complete TypeScript template with built-in validation, error handling, and scalability.

<Info>
  **Quick Start**: Deploy a complete webhook receiver to AWS in under 10 minutes with our battle-tested TypeScript recipe. Perfect for production workloads and new webhook implementations.
</Info>

## Overview

The Webhook Receiver Recipe is a production-ready, AWS-based webhook receiver template that helps developers quickly implement robust webhook handling for Smartcar integrations. This TypeScript recipe provides a deployable starting point that makes adding custom business logic easy, eliminating much of the complexity of building webhook infrastructure from scratch.

* **Repository**: [smartcar/typescript-webhook-recipe](https://github.com/smartcar/typescript-webhook-recipe)
* **Deployment Target**: AWS (Lambda + API Gateway + SQS)
* **Language**: TypeScript/Node.js v22+
* **Infrastructure**: AWS CDK (Infrastructure as Code)

## What You Get

### Complete Serverless Architecture

* **API Gateway**: Public HTTPS endpoint for webhook delivery
* **Lambda Functions**: Serverless processing with automatic scaling
* **SQS Queues**: Asynchronous message processing with built-in retry logic
* **Dead Letter Queues**: Error handling and failed message recovery
* **CloudWatch**: Comprehensive logging and monitoring

### Production-Ready Features

* **Webhook Verification**: Automatic payload signature validation
* **Error Handling**: Graceful failure handling with retries
* **Scalability**: Automatic scaling to handle traffic spikes
* **Security**: IAM roles with least-privilege access
* **Monitoring**: Built-in CloudWatch logging
* **Type Safety**: Full TypeScript support with Smartcar types

### Infrastructure as Code

* Complete AWS CDK setup for repeatable deployments
* Environment-specific configurations (dev, staging, production)
* Easy customization and extension

## When to Use This Recipe

**Perfect for:**

* New webhook receiver implementations
* Teams using AWS as your cloud provider
* Production workloads requiring reliability and scale
* Teams wanting to deploy quickly without infrastructure complexity
* TypeScript/Node.js projects

## Architecture Overview

The recipe provides a complete serverless webhook receiver infrastructure on AWS. The diagram below shows the data flow from Smartcar webhooks through your deployment:

```mermaid  theme={null}
graph TD
    A[Smartcar Webhooks] -->|HTTPS POST| B[API Gateway]
    B --> C[Receiver Lambda]
    C -->|Validate & Queue| D[SQS Queue]
    D --> E[Processor Lambda]
    E -->|Process Signals| F[Your Business Logic]
    E -->|Failed Processing| G[Dead Letter Queue]
    G --> H[Manual Review/Retry]
    
    style A fill:#FFB84D,stroke:#E69500,stroke-width:2px,color:#000
    style B fill:#FF9900,stroke:#CC7A00,stroke-width:2px,color:#000
    style C fill:#FF9900,stroke:#CC7A00,stroke-width:2px,color:#000
    style D fill:#FF9900,stroke:#CC7A00,stroke-width:2px,color:#000
    style E fill:#FF9900,stroke:#CC7A00,stroke-width:2px,color:#000
    style F fill:#d3d3d3,stroke:#666,stroke-width:2px,color:#000
    style G fill:#FF9900,stroke:#CC7A00,stroke-width:2px,color:#000
    style H fill:#d3d3d3,stroke:#666,stroke-width:2px,color:#000
```

<Note>
  **Orange components** are provided by the recipe and deployed automatically. **Gray components** represent external systems where your custom business logic would live.
</Note>

### Key Components

1. **Receiver Lambda**: Validates incoming webhooks and queues them for processing
2. **SQS Queue**: Decouples receiving from processing for reliability
3. **Processor Lambda**: Processes webhook payloads and executes business logic
4. **Dead Letter Queue**: Captures failed messages for investigation
5. **CloudWatch**: Monitoring, logging, and alerting

## Quick Start

### Prerequisites

* AWS Account with CLI configured
* Node.js v22+ installed
* Git
* **Smartcar Application** configured in the [Dashboard](https://dashboard.smartcar.com/)
  * You'll need your **Application Management Token** (found in Dashboard → Configuration)
  * Learn how to [configure your application](/getting-started/configure-application)

### Deployment Steps

<Steps>
  <Step title="Clone the Repository">
    ```bash  theme={null}
    git clone https://github.com/smartcar/typescript-webhook-recipe.git
    cd typescript-webhook-recipe
    ```
  </Step>

  <Step title="Build the Project">
    ```bash  theme={null}
    make build
    ```
  </Step>

  <Step title="Deploy to AWS">
    The recipe uses AWS CDK for infrastructure deployment. First, create a secret to store your Application Management Token, then deploy the stack.

    ```bash  theme={null}
    # Step 1: Create the secret for your Application Management Token
    make create-secret appName=your-app-name amt=your_smartcar_application_management_token

    # Step 2: Deploy the infrastructure
    make deploy appName=your-app-name

    # Note the ApiEndpointUrl from the output
    # Example: https://abc123.execute-api.us-east-1.amazonaws.com/prod/
    ```

    <Note>
      Use the same `appName` value for both commands. This name will be used to identify your CloudFormation stack and associated resources.
    </Note>

    For detailed deployment instructions including environment-specific configuration, see the [GitHub repository README](https://github.com/smartcar/typescript-webhook-recipe#usage).
  </Step>

  <Step title="Configure Webhook in Dashboard">
    Now that your receiver is deployed, configure the webhook integration in Smartcar Dashboard:

    1. Go to your [Smartcar Dashboard](https://dashboard.smartcar.com/integrations)
    2. Click **+ Add Integration** and select **Webhooks**
    3. Configure your webhook:
       * **Webhook URL**: Use the deployed URL from the previous step
       * **Trigger**: Choose when to send webhooks (e.g., "State of charge changes")
       * **Signals**: Select the vehicle data you want to receive (e.g., battery level, location, odometer)
    4. Click **Save** - Smartcar will automatically verify your endpoint

    <Note>
      The recipe automatically handles webhook verification. If verification fails, check CloudWatch logs for errors.
    </Note>

    For detailed webhook configuration guidance, see [Webhooks Setup](/integrations/webhooks/overview).
  </Step>

  <Step title="Subscribe Vehicles (Optional)">
    Depending on your webhook configuration, you may need to manually subscribe vehicles:

    * **Auto-subscribe enabled**: New vehicle connections will automatically start sending webhook data
    * **Manual subscription**: Use the [Subscribe endpoint](/api-reference/webhooks/subscribe-webhook) or Dashboard to subscribe specific vehicles

    Learn more about [subscribing vehicles to webhooks](/integrations/webhooks/overview#subscribing-vehicles-to-a-webhook).
  </Step>
</Steps>

<Note>
  The deployment typically takes 2-3 minutes. The recipe will output your webhook URL and other important configuration details upon completion.
</Note>

## Customizing Your Webhook Processor

The recipe includes a sample processor that logs webhook data. To implement your business logic:

<CodeGroup>
  ```typescript src/lambdas/sqs/index.ts theme={null}
  import { Logger } from '@aws-lambda-powertools/logger';
  import { getSignalByCode, Signals, type TractionBatteryStateOfCharge } from "@smartcar/signals";
  import type { WebhookDataPayload } from '@smartcar/webhooks';
  import { parseEnvelope } from '@smartcar/webhooks';
  import { Context, SQSEvent, SQSHandler } from 'aws-lambda';

  const logger = new Logger();

  export const processor: SQSHandler = async (
    event: SQSEvent,
    context: Context
  ) => {
    const batchItemFailures: { itemIdentifier: string }[] = [];

    for (const record of event.Records) {
      try {
        const eventBody: WebhookDataPayload = parseEnvelope(record.body);
        const signals: Signals = eventBody.data.signals as Signals;
        const { errors } = eventBody.data;

        // Example: Process signals data
        if (signals && signals.length > 0) {
          const stateOfChargeSignal: TractionBatteryStateOfCharge | undefined = 
            getSignalByCode<TractionBatteryStateOfCharge>(signals, 'tractionbattery-stateofcharge');
          
          if (stateOfChargeSignal) {
            logger.info('State of Charge Signal', stateOfChargeSignal.body);
            
            // Replace with your business logic
            if (stateOfChargeSignal.body.value < 50) {
              logger.info('Battery below 50% - get charged!');
            }
          }
        }
        
        // Handle errors in webhook payload
        if (errors && errors.length > 0) {
          logger.warn('Errors in webhook payload', { errors });
        }
      } catch (err) {
        logger.error('Error during processing', { error: err, record });
        batchItemFailures.push({ itemIdentifier: record.messageId });
      }
    }

    return { batchItemFailures };
  };
  ```

  ```typescript External API Integration theme={null}
  // Example: Send data to external service
  async function sendToExternalAPI(payload: WebhookPayload) {
    const response = await fetch('https://your-api.com/webhook-data', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${process.env.API_TOKEN}`
      },
      body: JSON.stringify(payload)
    });
    
    if (!response.ok) {
      throw new Error(`API call failed: ${response.statusText}`);
    }
  }
  ```
</CodeGroup>

## Configuration Options

The recipe uses AWS CDK for infrastructure configuration. You can customize various aspects by modifying the CDK stack configuration in `lib/webhook-receiver-stack.ts`.

### Common Configuration Options

Use these CDK properties (not environment variables) to tune the stack. Their camelCase names match the props in `lib/webhook-receiver-stack.ts`.

| Configuration       | Description                             | Example                                                                                                                                              |
| ------------------- | --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `logLevel`          | Logging verbosity for Lambda functions  | [See example](https://github.com/smartcar/typescript-webhook-recipe/blob/61485696ed459ee21ed5aa9d967373f5ecee651f/lib/webhook-receiver-stack.ts#L46) |
| `memorySize`        | Lambda function memory allocation in MB | [See example](https://github.com/smartcar/typescript-webhook-recipe/blob/61485696ed459ee21ed5aa9d967373f5ecee651f/lib/webhook-receiver-stack.ts#L41) |
| `visibilityTimeout` | SQS message visibility timeout          | [See example](https://github.com/smartcar/typescript-webhook-recipe/blob/61485696ed459ee21ed5aa9d967373f5ecee651f/lib/webhook-receiver-stack.ts#L29) |
| `maxReceiveCount`   | Max retries before dead letter queue    | [See example](https://github.com/smartcar/typescript-webhook-recipe/blob/61485696ed459ee21ed5aa9d967373f5ecee651f/lib/webhook-receiver-stack.ts#L30) |

For environment-specific configurations (dev, staging, production), you'll define these in your CDK code rather than using environment variables. This allows you to manage infrastructure differences across environments programmatically.

See the [GitHub repository](https://github.com/smartcar/typescript-webhook-recipe) for detailed configuration examples.

## Monitoring and Troubleshooting

### CloudWatch Logging

The recipe includes built-in CloudWatch logging for debugging and monitoring. You can:

* View Lambda execution logs
* Track webhook deliveries and failures
* Monitor SQS queue metrics

<Note>
  CloudWatch alarms are not included by default. You can add custom alarms on top of CloudWatch metrics based on your monitoring needs.
</Note>

### Common Issues

<AccordionGroup>
  <Accordion title="Webhook verification failing">
    * Check that your Smartcar Application Management Token is correct
    * Verify the webhook URL matches your deployed endpoint
    * Check CloudWatch logs for verification errors
  </Accordion>

  <Accordion title="Messages stuck in dead letter queue">
    * Review CloudWatch logs for processing errors
    * Check if external services (databases, APIs) are accessible
    * Verify IAM permissions for Lambda functions
  </Accordion>

  <Accordion title="High latency or timeouts">
    * Consider increasing Lambda memory allocation in CDK configuration
    * Optimize external API calls and database queries
    * Check for cold start issues in Lambda functions
  </Accordion>
</AccordionGroup>

### Debugging Commands

```bash  theme={null}
# Monitor queue depths
aws sqs get-queue-attributes --queue-url <queue-url> --attribute-names ApproximateNumberOfMessages

# Redrive messages from dead letter queue
aws sqs receive-message --queue-url <dlq-url> --max-number-of-messages 10
```

## Next Steps

After deploying your webhook receiver:

1. **Test Your Integration**: Use the [Smartcar Dashboard](https://dashboard.smartcar.com/) to test webhook delivery
2. **Monitor Performance**: Set up CloudWatch alarms for error rates and queue depths
3. **Scale as Needed**: Adjust Lambda memory and SQS settings based on usage patterns
4. **Add Features**: Extend the processor logic for your specific use cases

## Support and Contributing

* **Issues**: Report bugs or request features in the [GitHub repository](https://github.com/smartcar/typescript-webhook-recipe/issues)
* **Discussions**: Ask questions in [GitHub Discussions](https://github.com/smartcar/typescript-webhook-recipe/discussions)
* **Documentation**: Full setup and customization details in the [repository README](https://github.com/smartcar/typescript-webhook-recipe#readme)

***

<CardGroup cols={2}>
  <Card title="Repository" icon="github" href="https://github.com/smartcar/typescript-webhook-recipe">
    View the complete source code and documentation
  </Card>

  <Card title="Webhook Responses" icon="webhook" href="/integrations/webhooks/responses">
    Understand webhook payload structures
  </Card>
</CardGroup>


# Testing with Postman
Source: https://smartcar.com/docs/getting-started/using-vs-with-postman

In this tutorial we'll go over how to use Vehicle Simulator to test out Smartcar using Postman.

## What is Postman?

Postman is a collaboration platform for API development. Postman's features simplify each step of building an API and streamline collaboration so you can create better APIs - faster.
You’ll need a few things to start making API calls with Smartcar and Postman:

* [A Postman Account](https://identity.getpostman.com/signup?continue=https%3A%2F%2Fgo.postman.co%2Fbuild)
* [Smartcar’s Postman Collection](https://www.postman.com/smartcar/smartcar-api/collection/qk7g8v2/smartcar-api-v3?action=share\&creator=33621094)
* [A Smartcar Developer Account](https://dashboard.smartcar.com/signup)

## Configuring the Connect flow in Postman

1. Install the latest [Postman app](https://www.postman.com/downloads/) and log in
2. Import the [Smartcar collection](https://www.postman.com/smartcar/smartcar-api/collection/qk7g8v2/smartcar-api-v3?action=share\&creator=33621094) into your local Postman workspace. Hit Import.
3. Click Link, paste in [the link](https://www.postman.com/smartcar/smartcar-api/collection/qk7g8v2/smartcar-api-v3?action=share\&creator=33621094) to the collection and hit Continue.
4. On the next screen, hit Import.

<Tabs>
  <Tab title="Step 1">
    <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/postman.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=eff974c27c35429e996cc03ac0537ca3" data-og-width="1909" width="1909" data-og-height="735" height="735" data-path="images/help-center/guide-postman/postman.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/postman.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=016888b9f5f7351d6c23031258011ffd 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/postman.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=3fddd8da5d08c02b7b506e691dd0b9dd 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/postman.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=3c70e7485b08c3c9d26bd6c7e2c7dc8a 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/postman.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=44de4f15cf082a01142835380edfa632 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/postman.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=c8fc1eb62d30bf5d77e41f43d6ec7785 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/postman.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=a8bf82c0dfe360db42977824304c19be 2500w" />
  </Tab>

  <Tab title="Step 2">
    <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/import1.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=0d6ca63f2c0ec0531d6f43013d898d46" data-og-width="2000" width="2000" data-og-height="781" height="781" data-path="images/help-center/guide-postman/import1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/import1.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=75cc5f5c6efea65b11aa05ad9bccaaec 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/import1.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=e408a3428f00acb334b0e8c828fd7b77 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/import1.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=bfd2d6e8c679444d0f4b669971476c06 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/import1.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=3f2f46f58bebc16f68bcadbab4c05e45 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/import1.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=83754ca3236b6ea69edc473b9ebdbb73 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/import1.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=218117c1cff0ac9877f08284d5fa861d 2500w" />
  </Tab>

  <Tab title="Step 3">
    <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/import2.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=ab103641bc93ed9d009e611042a87ddd" data-og-width="2000" width="2000" data-og-height="2034" height="2034" data-path="images/help-center/guide-postman/import2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/import2.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=1bf38338e70dd967e6fa08b1a42d1be4 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/import2.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=70c3f7ddec9d28f7d9a88a07e2441c64 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/import2.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=f151fa36c5b84d324f88e62ecc108bbe 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/import2.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=6aec86aa154618901f62892be022faa7 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/import2.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=f64bfdc2333313b74a8f68fc104bd4d0 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/import2.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=49a5bb764929570322d1d7d6b3b14b86 2500w" />
  </Tab>

  <Tab title="Step 4">
    <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/import3.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=ca91ea1a83ddcd32189f05e142917e3e" data-og-width="2000" width="2000" data-og-height="3103" height="3103" data-path="images/help-center/guide-postman/import3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/import3.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=11a42a3cadbc26df42e96c5fee19f1b3 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/import3.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=b9b8e8c1c6120d82fdc3586f9c66e5a5 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/import3.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=d1f18a835ad80f2669bdcfb9f6480667 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/import3.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=ba8d70342d7d97385599b04d5c67bc77 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/import3.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=6f96f78fcdcc2bece341c64ef878edae 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/import3.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=b8dd3242dd2775d1a41b509344ae763c 2500w" />
  </Tab>
</Tabs>

## Smartcar Application Configuration

If you haven’t already signed up for a Smartcar Developer account, you can do so from this [**signup link**](https://dashboard.smartcar.com/signup).

* Grab your **Client ID** and **Client Secret** from the Configuration page after you sign in, and copy them to someplace secure. You’ll need those tokens a little later in this setup.
* Under the Credentials tab for your application, you’ll need to add the following Redirect URIs. This will ensure that Smartcar Connect exits successfully with both Postman’s Native and Web clients.

```
https://oauth.pstmn.io/v1/browser-callback 
http://localhost:8000/exchange
```

<Frame type="simple">
  <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/appConfig.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=227ee48bcdd4a1994049717c996deaa4" data-og-width="2000" width="2000" data-og-height="1306" height="1306" data-path="images/help-center/guide-postman/appConfig.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/appConfig.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=22525c94a1167dc50c0b7c29f521b75d 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/appConfig.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=35f84af32748222af74a57f5b8b56a1d 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/appConfig.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=7aef027c29db70ca3ba0a8ee7e878626 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/appConfig.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=0efa259095c171610dbabf66573d46e2 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/appConfig.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=d9bcc2b805c2374762e3e4340d0880e0 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/appConfig.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=0fb808d66c484339ccf916af71d3a1e3 2500w" />
</Frame>

Through the Connect flow, you’re able to get consent from vehicle owners to connect their vehicle to your application. Postman provides an easy way to manage oAuth 2.0 flows under the Authorization tab of a Collection. Set up the Configuration Options for either a live or simulated vehicle.

<Frame type="simple">
  <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/authorization.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=44585e961f665d2d259993a8ddd4319e" data-og-width="2000" width="2000" data-og-height="2428" height="2428" data-path="images/help-center/guide-postman/authorization.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/authorization.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=46aa2f12046829bd12721516223962fc 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/authorization.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=e1564439120f97729c09dfdbb991f128 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/authorization.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=c2a4277fff801a484e5119578b772632 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/authorization.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=64c4d2591f0c61bd44dc7652bed92312 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/authorization.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=817af5d94ee6ab342b4429d45d645300 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/authorization.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=8a9fc062932e0fc9d38577d3ecd1ec4f 2500w" />
</Frame>

**Live Vehicle**

| Parameter        | Description                                                                                                       |
| ---------------- | ----------------------------------------------------------------------------------------------------------------- |
| Auth URL         | `https://connect.smartcar.com/oauth/authorize?approval_prompt=force`                                              |
| Access Token URL | `https://auth.smartcar.com/oauth/token`                                                                           |
| Client ID        | `client_id` from your Dashboard                                                                                   |
| Client Secret    | `client_secret` from your Dashboard                                                                               |
| Scope            | A space-separated list of [permissions](/api-reference/permissions) that your application is requesting access to |

**Simulated Vehicle**

| Parameter        | Description                                                                                                       |
| ---------------- | ----------------------------------------------------------------------------------------------------------------- |
| Auth URL         | `https://connect.smartcar.com/oauth/authorize?approval_prompt=force&mode=simulated`                               |
| Access Token URL | `https://auth.smartcar.com/oauth/token`                                                                           |
| Client ID        | `client_id` from your Dashboard                                                                                   |
| Client Secret    | `client_secret` from your Dashboard                                                                               |
| Scope            | A space-separated list of [permissions](/api-reference/permissions) that your application is requesting access to |

## Setting up a Simulated Vehicle

Under the Simulator tab on Dashboard, hit Add Vehicle. Note that you may already have a pre-created simulated vehicle available, if so skip to **Connecting to a vehicle** below.

<Frame type="simple">
  <img src="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim1.png?fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=ac48f25d23f26724ac3c3a030a98db67" data-og-width="1601" width="1601" data-og-height="633" height="633" data-path="images/help-center/guide-postman/sim1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim1.png?w=280&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=81b228e533bb030731f804c8e5dc79f8 280w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim1.png?w=560&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=684fa9b64b213b5a14070d9805907e60 560w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim1.png?w=840&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=cf9129e663aabc81e830c5483165b9a5 840w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim1.png?w=1100&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=1aa6264af9bbe9cc36d80b3cdb691d6f 1100w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim1.png?w=1650&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=1cbf429bcd1da5b1191df8a90aadec27 1650w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim1.png?w=2500&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=ad28310d044fb17262ac42b120855908 2500w" />
</Frame>

Select a region and MMY for your vehicle, then hit Search by MMY

<Frame type="simple">
  <img src="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim2.png?fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=d4185d0baab4608387e4bcb418395156" data-og-width="1691" width="1691" data-og-height="1120" height="1120" data-path="images/help-center/guide-postman/sim2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim2.png?w=280&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=3e8c4290600c6fac71158aed12b6311c 280w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim2.png?w=560&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=4b1c85eda9dffee5d77ba0f3e5df0f71 560w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim2.png?w=840&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=573ff038bcc73c80a01e07e46a07374e 840w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim2.png?w=1100&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=1347a9538d405c40efc0b8ae939ba73e 1100w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim2.png?w=1650&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=a69b34c3beea29e4800ee2663adeaf20 1650w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim2.png?w=2500&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=e40af5e2b60a6d1bbd4a36d9bd7c0577 2500w" />
</Frame>

After selecting Use Vehicle, you’ll want to select a state for the vehicle. After that, you’ll get a set of credentials to use in the Connect flow.

<Frame type="simple">
  <img src="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim3.png?fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=a80ce27d74bf60db8c576a22a73dfe50" data-og-width="1691" width="1691" data-og-height="920" height="920" data-path="images/help-center/guide-postman/sim3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim3.png?w=280&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=5871a63b04a29e9813c2224b6decf078 280w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim3.png?w=560&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=0d6de51615abdd7657c0aee6bbf0df47 560w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim3.png?w=840&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=0689689c1f14cb2e861731807feafc16 840w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim3.png?w=1100&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=5cbd492e16eb56d47a7c6015d2feb54b 1100w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim3.png?w=1650&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=efbc736170c9e3aa4272d65d019747de 1650w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim3.png?w=2500&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=bc5bccd272f3cc5b79e64abacf157dd8 2500w" />
</Frame>

<Frame type="simple">
  <img src="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim4.png?fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=234f54c381002a8dc4bbb988d9678d23" data-og-width="1929" width="1929" data-og-height="849" height="849" data-path="images/help-center/guide-postman/sim4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim4.png?w=280&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=ea1b8471e9682dd3b1a08502dd887fb5 280w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim4.png?w=560&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=e511753f8e9c7b299bc7424aeb654ce9 560w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim4.png?w=840&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=27e78a8cec0bdfb038b737a8e0842ad0 840w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim4.png?w=1100&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=1812b6b804ee240ad2396dacc0c65bb4 1100w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim4.png?w=1650&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=0409c59399c2063de53898838018eaf8 1650w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim4.png?w=2500&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=da731b53ecdeeb4ef690b58e66cf17a7 2500w" />
</Frame>

Before proceeding to the next step, you’ll want to start the simulation in the Smartcar Dashboard.

<Frame type="simple">
  <img src="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim5.png?fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=62c9900a88d6027f0ef2c623aaf59729" data-og-width="1468" width="1468" data-og-height="646" height="646" data-path="images/help-center/guide-postman/sim5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim5.png?w=280&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=255690782e946ed2eb4b29788cca8f65 280w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim5.png?w=560&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=a28d37c35bc257f50c5da645efc968ae 560w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim5.png?w=840&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=e612df7a4fce464843c5cf89dcc4a51c 840w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim5.png?w=1100&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=b8f37558d09cacbc68e9fab162f46bf4 1100w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim5.png?w=1650&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=2b83b12949a032b4fa074e0533c3518e 1650w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/sim5.png?w=2500&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=0a3a3318474af0d9f8a964f97f862e39 2500w" />
</Frame>

## Connecting to a vehicle

If configured correctly, when you click **Get New Access Token** in Postman, you should see the first screen of the Connect flow.

<Tip>
  Before hitting Continue, make sure to select a country from the dropdown appropriate to the region you selected for your simulated vehicle.
</Tip>

<Frame type="simple">
  <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/connect1.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=4eac302ec3adec5e4bd844218b1e8c02" data-og-width="2000" width="2000" data-og-height="2490" height="2490" data-path="images/help-center/guide-postman/connect1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/connect1.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=b33c86b9a49200aca03b0b2268d56b30 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/connect1.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=851cfdcc84cca6418304adc05ba75bb6 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/connect1.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=818c4993a577ac3d44da91d638faaf00 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/connect1.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=1dcb7d05948fd0a2c6fcd28b65377804 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/connect1.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=89a567a8b88bcf023347fbad04fa4f65 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/connect1.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=54f5cb846fd240db594de5887e8b6c05 2500w" />
</Frame>

Continue through the Connect flow, select the brand of your simulated vehicle and enter in the credentials you were issued for your simulated vehicle.
After accepting the permissions you’ll be met with the following screen:

<Frame type="simple">
  <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/connect2.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=b3fda47b60fb4b1d049769362b24b9fa" data-og-width="2000" width="2000" data-og-height="1171" height="1171" data-path="images/help-center/guide-postman/connect2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/connect2.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=bf14c4a7fa472feed32bf1653a186d0a 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/connect2.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=f629985aa1b2096126648869f6ef10ff 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/connect2.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=14afb459a27975f25c8b75f93d9fbaa4 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/connect2.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=12638020d51f7f48c974e9a1432486ef 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/connect2.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=ba92c7b42557535ece0de00caf6cbb05 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/connect2.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=f9af66b4ba70192c5b3317caa2cc4ad1 2500w" />
</Frame>

Hit Use Token. You should see Access Token under Current Token populate with the access\_token from the popup. Using this access\_token you can make API requests to Smartcar's API.

<Frame type="simple">
  <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/connect3.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=71eef9cb9f7fffbe7015cb6110b6daa7" data-og-width="2000" width="2000" data-og-height="774" height="774" data-path="images/help-center/guide-postman/connect3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/connect3.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=228f2abc0f83ae37967465df1e0c118f 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/connect3.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=14c08260ce21d05fe6c79ecdcde6c0b5 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/connect3.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=603e838cee16606a98763739e3d8671a 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/connect3.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=ce42d6b65d2fd760ee1e5006536ce3d2 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/connect3.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=37d944156781e88428fd65712a838156 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/connect3.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=9db774eaa2fa873059031b38b629e69b 2500w" />
</Frame>

<br />

<Warning>
  Access tokens are only valid for two hours. If you want to make API requests after it has expired, you'll need to generate a
  new one by stepping through the Connect Flow again, or through a [token refresh](/api-reference/authorization/token-refresh).
</Warning>

## Making an API request

<Tip>
  Thanks to Postman, requests in the collection will inherit the `access_token` from the OAuth 2.0 Authorization flow we went through in the steps above.
</Tip>

In order to make API requests, we’ll need to first get a Smartcar `vehicle Id`. A `vehicle Id` is a unique identifier for a vehicle on Smartcar’s platform.

This can be done with the `All Vehicles` request. Making this request will assign the `vehicle Id` to the `{{vehicle_id}}` variable for other requests in the Collection.

<Frame type="simple">
  <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/req1.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=1182006af59ffca20f826b396d7876c5" data-og-width="2000" width="2000" data-og-height="1186" height="1186" data-path="images/help-center/guide-postman/req1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/req1.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=e95dac20eef0635b4e16ca565d4d5922 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/req1.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=1b4ed61974c72f06e6b5be4789dba84a 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/req1.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=9d5aeae2a0334cfcca8bfbd8d1f6e1d1 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/req1.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=a1d5f5a2c76f7f52c52fc25d5af49f82 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/req1.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=ebb64246814d3f35781c3beb5dd08094 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/req1.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=091082c4b9e2057866598684824a1b65 2500w" />
</Frame>

<br />

Now that you've got a vehicle Id, you can make a request to other endpoints. Hitting Vehicle Info, we can see the MMY of the vehicle.

<Frame type="simple">
  <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/req2.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=c9b1d9dd016d9ef9674a84a368648db6" data-og-width="2000" width="2000" data-og-height="1105" height="1105" data-path="images/help-center/guide-postman/req2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/req2.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=80472e786a7f26a6d730ad761ed69d5d 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/req2.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=c96f5f6aad6b8db7f8955d7107c6fa61 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/req2.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=efa987df738bf5c5219f16dd288181e8 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/req2.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=4cc1084b30ed7130b2c28594072f0038 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/req2.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=876da9b854b51b8144042e2c007050f1 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/req2.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=5fd20e450288ea503841316a82260332 2500w" />
</Frame>

<br />

Checking `EV Battery Level`, we can see the response matches the vehicle state on the simulator

<Frame type="simple">
  <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/req3.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=7230503ce005f2bde54dddfd00c5b58c" data-og-width="2000" width="2000" data-og-height="1036" height="1036" data-path="images/help-center/guide-postman/req3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/req3.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=e4b83819e252f452039d0c963953d541 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/req3.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=6add9acb8b6f8a19ef1a75629eac75c1 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/req3.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=309bdf161ba4d9ae74452493a1dbcec9 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/req3.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=8241ba78505dbb0ee4c81aa4514e6e86 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/req3.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=9b65f4395bf55177a09c69c9637a1ac5 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/help-center/guide-postman/req3.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=e7af67311b0bb31397e6d4e7b369ed3d 2500w" />
</Frame>

<br />

<Frame type="simple">
  <img src="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/req4.png?fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=5798556122aea8b0f4e20aa60d816b7e" data-og-width="2000" width="2000" data-og-height="1580" height="1580" data-path="images/help-center/guide-postman/req4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/req4.png?w=280&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=9a501a8002cb2d23f52a9619349a6fec 280w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/req4.png?w=560&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=1b9fd83b56957a7d55c5a20f119a4023 560w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/req4.png?w=840&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=7e8e19baf5e09e99e58bf528e8c6f2a2 840w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/req4.png?w=1100&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=91ef1aed95e552fdeffccea38c4c82c1 1100w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/req4.png?w=1650&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=f0b411f53e83c5c7977de54cc874ec42 1650w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/guide-postman/req4.png?w=2500&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=ce529293fd334a85251146348945de84 2500w" />
</Frame>

<br />

## Troubleshooting

<AccordionGroup>
  <Accordion title="I’m getting an Invalid Credentials error in the Connect flow">
    * Check that you’re launching Connect in simulated mode
    * If you’re still running into an error make sure you’ve selected a country that matches the region you selected for your simulated vehicle.
  </Accordion>

  <Accordion title="I’m getting a 403 - Permission error on API requests">
    * Check that the vehicle you’ve created supports the endpoint. Select View Estimated Latencies to see a list of endpoints supported for the vehicle.
    * If you’re still running into the error, check that you’ve requested the appropriate permission in the scope parameter of the Connect URL.

    <Tip>
      You can always check the `/permissions` endpoint to see what endpoints you have access to.
    </Tip>
  </Accordion>
</AccordionGroup>


# Accessing the Smartcar Support Center
Source: https://smartcar.com/docs/help/accessing-support-center

The Smartcar Support Center provides helpful resources including a knowledge base, ticket submission form, AI chat assistant, and a ticket center to manage your requests.

<Note>This feature is available on paid plans.</Note>

You can access the Support Center in two ways:

### Option 1: Visit the Support Center directly

Go to [support.smartcar.com](https://support.smartcar.com). You’ll be redirected to the Smartcar Dashboard to log in with your Dashboard credentials.

### Option 2: From the Smartcar Dashboard

1. Log in at [dashboard.smartcar.com](https://dashboard.smartcar.com).
2. Click the **Help** icon in the bottom-left corner, or the **Help Hub** icon in the bottom-right. <img src="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/support-center/help-hub.png?fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=5b38c0162e8814262623c6be79ce7490" alt="Help Hub" data-og-width="3360" width="3360" data-og-height="1846" height="1846" data-path="images/help-center/support-center/help-hub.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/support-center/help-hub.png?w=280&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=b059cadbb30bb8967f52c423cdfc37f7 280w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/support-center/help-hub.png?w=560&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=38c81769d3aded28a62a6468859904ae 560w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/support-center/help-hub.png?w=840&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=8b6cfba7fd2863f593ac1ce602550905 840w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/support-center/help-hub.png?w=1100&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=894be9202604164d85c3b986ab935418 1100w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/support-center/help-hub.png?w=1650&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=b14cbeb8d0bb577737bfe7689f06f02f 1650w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/support-center/help-hub.png?w=2500&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=470e63f058c63faa1ca624143e01dc91 2500w" />
3. Select the **Support Center** option to be redirected to the full Support Center. <img src="https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/help-center/support-center/support-center-button.png?fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=55b92545b9f29533a420cb8c28bbe23c" alt="Support Center Button" data-og-width="466" width="466" data-og-height="786" height="786" data-path="images/help-center/support-center/support-center-button.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/help-center/support-center/support-center-button.png?w=280&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=9f739f26b776a019428b99fda9422e14 280w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/help-center/support-center/support-center-button.png?w=560&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=badc29dd1597ebc701c3d52f1236a244 560w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/help-center/support-center/support-center-button.png?w=840&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=88fcab31d69334a3f9f45623ad8eacd0 840w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/help-center/support-center/support-center-button.png?w=1100&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=840b47ed2c930d927532f7b3293a5e3d 1100w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/help-center/support-center/support-center-button.png?w=1650&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=a0e1e09f307b6da24c61e0ff60dbd767 1650w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/help-center/support-center/support-center-button.png?w=2500&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=7845362581a401997b75f616768c9f69 2500w" />


# Smartcar Usage Limits
Source: https://smartcar.com/docs/help/api-limits

Learn about limits you may encounter when using Smartcar.

## Overview

There are several types of limits that govern your use of Smartcar. The nature of telematics requires us to carefully manage vehicle connections and traffic to ensure the stability of our platform and those of our upstream providers.

There are two major types of limits - **Billing Limits** and **Operational Rate Limits**.

# Billing Limits

### [BILLING : VEHICLE\_REQUEST\_LIMIT](/errors/api-errors/billing-errors#vehicle-request-limit)

Your Smartcar plan specifies a maximum number of API calls you are permitted to make to each single vehicle in a given month. If you exceed this limit, you will receive the `VEHICLE_REQUEST_LIMIT` error.

For example: you have been allocated 500 API calls per vehicle per month, but you made the 501<sup>st</sup> call to a single vehicle during the billing period.

**This limit can be changed.** If you require more calls per vehicle per month, contact [support@smartcar.com](mailto:support@smartcar.com) or your Account Manager and we can work with you to understand your options.

### [BILLING : VEHICLE\_LIMIT](/errors/api-errors/billing-errors#vehicle-request-limit)

Your Smartcar plan specifies a maximum number of vehicles that you may have connected at any one time. This limit applies to vehicle connections, and is separate from the limit regarding the number of API calls to those vehicles. If you receive this error, you have exceeded your maximum number of connected vehicles.

**This limit can be changed.** Reach out to [support@smartcar.com](mailto:support@smartcar.com) or your Account Manager to discuss your options.

# Operational Rate Limits

### [RATE\_LIMIT : SMARTCAR\_API](/errors/api-errors/rate-limit-errors#smartcar-api)

Smartcar limits the total number of requests a single application can make over a given period of time to ensure platform stability for all customers. The Smartcar API Limit is defined as a "bucket" of requests that refills at a constant rate over time.

The default Smartcar API Limit is a **bucket of 120 requests that refills at a rate of 2 requests per minute.**

If you receive a `RATE_LIMIT:SMARTCAR_API` response, your application has exceeded this limit. You should implement an exponential backoff strategy when retrying requests.

**This limit can be changed.** Reach out to [support@smartcar.com](mailto:support@smartcar.com) or your Account Manager to discuss your options.

### [RATE\_LIMIT : VEHICLE](/errors/api-errors/rate-limit-errors#vehicle)

Sending telematics requests to a vehicle causes it to wake up from its sleep state and consume energy and data resources. Excessive requests to a single vehicle can result in:

* EV battery drain
* 12 volt battery drain
* `UPSTREAM:RATE_LIMIT` errors that prevent you from making requests for a longer period of time

Smartcar enforces a per-vehicle rate limit that governs the rate of requests to a single vehicle and mitigates these potential issues. These limits can differ based on the vehicle manufacturer and a number of other factors, and are set by Smartcar to ensure consistent and timely data can be retrieved from vehicles.

**This limit cannot be changed.** If you receive this response, refer to the `retry-after` header (returned as seconds) for when to retry the request.

### [UPSTREAM : RATE\_LIMIT](/errors/api-errors/upstream-errors#rate-limit)

Vehicle manufacturers sometimes impose rate limits on requests to vehicles. The Smartcar Vehicle Rate Limit will generally prevent those limits from being reached, but outside requests from other providers may cause the upstream limit to be exceeded. If the OEM upstream rate limit is exceeded, you will receive `UPSTREAM:RATE_LIMIT` from the Smartcar API for the affected vehicle until the limit is reset.

**This limit cannot be changed.** Smartcar cannot control rate limits imposed by our upstream providers. If you consistently receive this response for a single vehicle, reach out to [support@smartcar.com](mailto:support@smartcar.com) and we can investigate.


# Assist AI features in Slack
Source: https://smartcar.com/docs/help/assist-ai-slack

As part of our Enterprise Slack support offering, Smartcar includes access on select Enterprise plans to an AI-powered assistant that can help you get answers quickly, submit tickets, and navigate support resources—all without leaving your Slack workspace.

## 1. Ask a Question

In your dedicated Slack support channel, send a message with your question. The AI Agent will attempt to answer it based on Smartcar’s support documentation and past support interactions. <img src="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/support-center/ask-a-question.png?fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=bcb149aff43bca356b9714f2760c6e00" alt="Ask a Question" data-og-width="484" width="484" data-og-height="686" height="686" data-path="images/help-center/support-center/ask-a-question.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/support-center/ask-a-question.png?w=280&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=985d5e75b4b7ac088fb41c4fe953981c 280w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/support-center/ask-a-question.png?w=560&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=d2a94093bef1bb846b9c8be47c180629 560w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/support-center/ask-a-question.png?w=840&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=7af3235d68f17dd9391d8daeda88515b 840w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/support-center/ask-a-question.png?w=1100&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=f00040c1e3e691068b7bd3acd3925c74 1100w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/support-center/ask-a-question.png?w=1650&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=246667428285e80fa50976cbaf57ebf3 1650w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/support-center/ask-a-question.png?w=2500&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=8f1fc2a6276ec130bb89e8f673feec4d 2500w" />

## 2. Submit a Support Ticket

If your question requires deeper support, simply click **"Create a Ticket"** at the bottom of the AI-generated response within the Slack channel. This will open a form to submit a formal, trackable support request. <img src="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/support-center/slack-create-a-ticket.png?fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=fa67c071dac4080ff8ecb41cca82fd9b" alt="Create a Ticket" data-og-width="742" width="742" data-og-height="686" height="686" data-path="images/help-center/support-center/slack-create-a-ticket.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/support-center/slack-create-a-ticket.png?w=280&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=d0e4daa02485bef86485d67194fd7415 280w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/support-center/slack-create-a-ticket.png?w=560&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=558ab55e94a1961d013da2955aab56d3 560w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/support-center/slack-create-a-ticket.png?w=840&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=b98d375c269b23ee7281f80a077e7c88 840w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/support-center/slack-create-a-ticket.png?w=1100&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=f8c83255eb74bd5d6d02f14ef1a05934 1100w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/support-center/slack-create-a-ticket.png?w=1650&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=40233b951d9422cbfa9daa055fd3745e 1650w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/support-center/slack-create-a-ticket.png?w=2500&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=82343f5a2589d30d219aaeb8226204c9 2500w" /> <img src="https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/help-center/support-center/slack-create-a-ticket2.png?fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=0a6dbe0e28716ccaab5617fc228363b3" alt="Ticket Form" data-og-width="535" width="535" data-og-height="550" height="550" data-path="images/help-center/support-center/slack-create-a-ticket2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/help-center/support-center/slack-create-a-ticket2.png?w=280&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=56333728b2fdb4fb7f8125a915d1d635 280w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/help-center/support-center/slack-create-a-ticket2.png?w=560&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=93eca671b85569fffa0cbd5df5b4ae59 560w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/help-center/support-center/slack-create-a-ticket2.png?w=840&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=a95096ba02c62cd08eadfdea7b09a361 840w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/help-center/support-center/slack-create-a-ticket2.png?w=1100&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=0736cedd6937c620e7aeabe44d694271 1100w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/help-center/support-center/slack-create-a-ticket2.png?w=1650&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=f96b8796852eca5c371a48bcfa1afc05 1650w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/help-center/support-center/slack-create-a-ticket2.png?w=2500&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=6160f1cdf12aac6e3ba2a5e0d8fd319b 2500w" />

## 3. View Open Tickets

To check the status of an existing ticket, navigate to the Slack thread where the ticket was created and click the **"View Ticket Info"** icon. This will display the current status and details of your support request. <img src="https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/help-center/support-center/view-ticket-info.png?fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=3d26b2403a32f6706f7a513836753010" alt="View Open Ticket" data-og-width="1036" width="1036" data-og-height="1006" height="1006" data-path="images/help-center/support-center/view-ticket-info.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/help-center/support-center/view-ticket-info.png?w=280&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=a29da77d07d2c7d7920b11f0273f6270 280w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/help-center/support-center/view-ticket-info.png?w=560&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=523dc88b41028896536d71568475be8b 560w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/help-center/support-center/view-ticket-info.png?w=840&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=91f7f89c5b9f1a6b475b063ff7c294ac 840w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/help-center/support-center/view-ticket-info.png?w=1100&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=1c4058743fc7380361bc1ca0f35cbdc2 1100w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/help-center/support-center/view-ticket-info.png?w=1650&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=f304a97991bfd1e83cfe2c0219692a74 1650w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/help-center/support-center/view-ticket-info.png?w=2500&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=01625842882f7f5be2d4cfad94819565 2500w" />

## 4. Navigate to the Support Center

Need more detailed help? You can access your ticket by clicking the **ticket ID** that appears after submitting a request using the **"Create a Ticket"** option. Alternatively, from the **"View Ticket Info"** window, you can click the **ticket number** to be redirected to the Smartcar Developer Dashboard. If you're already logged into an active session, you'll be taken directly to the ticket details within the Support Center. Otherwise, you'll be prompted to log in first.

In the Support Center, you can:

* Browse our documentation
* Submit new support requests
* View and update your existing tickets

For step-by-step instructions on how to log into the Smartcar Support Center, please see the following article: [Accessing the Smartcar Support Center](/help/accessing-support-center)


# Beta
Source: https://smartcar.com/docs/help/beta

Understand Smartcar's approach to features in beta.

Beta is an option that allows developers to test and integrate new Smartcar features before they are fully released. Beta refers to a phase where certain features are made available for testing and feedback prior to general availability. These features are functional but may still be under development or refinement.

## Benefits of Beta Features

Participating in beta allows developers to get a head start on integrating new features, a chance to influence the feature in development through feedback and help Smartcar ensure your app’s needs are met.

## Considerations for features in Beta

When working with beta features, keep in mind that features may change before final release. As such, extra caution is advised when using these features in production environments.

## How to Participate

If you would like to get involved in testing a beta features, contact your Account Manager or our Support team at [support@smartcar.com](mailto:support@smartcar.com) for guidance.


# Brand Quirks
Source: https://smartcar.com/docs/help/brand-quirks

Brand specific quirks to keep in mind while building out your application.

## Acura

### Ignition On

Depending on model year, certain Acura vehicles do not return data when the ignition/engine is on.

### Sleep State

Most Acuras will go into a sleep state after about a week of inactivity,

## Audi

### Primary Key User

In order to have access to all vehicle functionality the account that connects to Smartcar will need to be flagged as a Key User by Audi.

## BMW/MINI

### CONNECTED\_SERVICES\_ACCOUNT - SUBSCRIPTION errors

Smartcar API will throw a CONNECTED\_SERVICES\_ACCOUNT - SUBSCRIPTION when the data we receive from the vehicle is older than a month as this normally indicates a subscription issue.

## BYD

### Concurrent login requirement

BYD accounts can only maintain one active session at a time. Vehicle owners should sign in with a dedicated BYD login for Smartcar that is separate from the credentials used in the BYD mobile app. If the same account signs into the OEM app after connecting through Smartcar, the Smartcar session will be revoked and require re-authentication.

If customers reach out about being logged out of their BYD mobile app, we recommend instructing users to create a secondary BYD account exclusively for your app.

## Ford/Lincoln

### Authentication

Connecting Ford and Lincoln vehicles requires the use of one of our mobile SDKs. We currently offer SDKs for iOS, Android, and Flutter. Smartcar's Connect SDKs will redirect to Ford’s site to handle the authentication process when the user logs in.

**Authentication via non-mobile platforms such as web browsers is not supported at this time**. See [Connect SDKs](/connect/connect-sdks) for our latest SDKs.

## GM (Buick, Chevrolet, Cadillac, GMC)

### VEHICLE\_STATE - ASLEEP errors

After 3-4 days of no activity, GM vehicles will enter a deep sleep state at which point they will no longer respond to API requests to preserve their 12v battery. In order to get data from the vehicle again, the car will need to go through an ignition cycle.

### UPSTREAM - RATE\_LIMIT errors

In order to avoid hitting UPSTREAM - RATE\_LIMIT errors use batch requests and ping no more than once every 30 minutes. Use of the OEM app also counts towards the rate limit.

## Hyundai/Kia

### Telemetry Update Behavior

#### Pre-2025 Models (Gen 2 Navigation)

Hyundai/Kia vehicles have event-based logic that sends telemetry updates based on state changes such as:

* Every 10% of SoC while charging
* 5 minutes after ignition off
* Vehicle doors are left unlocked for 5 minutes
* After a command successfully completes
* Whenever charging stops

#### 2025+ Models (Gen 3 / CCnC Navigation)

Newer Hyundai/Kia models update more frequently, as often as every five minutes, including while the vehicle is driving.

## Nissan

### “Vehicle has been found” MyNISSAN notifications

Vehicle owners may receive a notification from the MyNISSAN app stating “Success! We found the location of your vehicle. Check the map for the location of your YYYY Model.” every time the location endpoint is hit.

The app appears to have an option to edit notifications, but as of Feb 2024 they are not available in the app. Notifications may need to be turned off at the iOS/Android level by the vehicle owner.

## PSA Group (Citroen, DS, Opel, Peugeot, Vauxhall)

### Requesting control\_charge permissions

If you request control\_charge permissions for PSA EVs, upon login owners will be presented with a PIN and MFA screen in Connect upon submitting their credentials. They will need to have set this up on their OEMs application in order to grant your application this permission.

## Rivian

### MFA

If MFA is enabled the vehicle owner will need to re-authorize via Connect about every 2 weeks.

## Tesla

### Remote Access

It may take a few hours or up to a full day for the REMOTE\_ACCESS\_DISABLED errors to subside after remote access is enabled.

### Charge Billing Records

In order to retrieve charge billing records, the main Tesla account must connect the vehicle, as driver profiles do not have access to this data.

### Virtual Key

Tesla now requires virtual keys for 3rd-party applications in order to issue commands for the following models:

* All Cybertrucks, Model 3 and Model Y
* 2021+ Model S and X

Please see [Virtual Keys](oem-integrations/tesla/virtual-key-tesla) for more information.

## Volkswagen

### Control charge limits

Volkswagen only allows 15 charge commands (start/stop charge) before the vehicle needs to be driven again in order to start responding to start/stop requests.

### CONNECTED\_SERVICES\_ACCOUNT errors on lock/unlock commands

In addition to verifying the VW account with the activation code, some cars will need to undergo the VW Ident Process before you can access remote lock/unlock functionality. This involves contacting the dealership to verify your ownership of the vehicle.

### Missing Subscription (European VWs)

Upon purchasing (or activating the free trial), VW needs to review the request. You will get an email confirmation once they've cleared everything on their side.

### Primary Driver Status

In order to fully interact with Smartcar, the credentials need to be flagged as the primary driver. You'll need to tap the "become primary driver" flow in the VW app. Depending on the model, this may require you to be in the car to interact with the infotainment system.

A vehicle owner can verify whether or not they are the primary driver by following the steps below:

1. Open the VW mobile app tap the profile icon in the bottom right
2. Go to **Vehicle Management**
3. If there’s an **Additional Users** section, tap their name to see whether it says **Primary User** or **Additional User**

## Volvo

### Lock/unlock commands

Volvo is an outlier regarding how unlock requests are processed. After initiating the request, after about 10 seconds you'll need to open the trunk (boot) to successfully complete the request. You'll know the car is ready to unlock the trunk as the hazard lights will flash. We recommend adding a notification for Volvos as part of the request loading animation to inform the user of this process.

### Phone number username

Smartcar Connect currently checks for an email format, as such phone number usernames cannot be used. The owner will need to add their email to their Volvo account via the web portal.

### Compatibility

Some models are not compatible because the device needs to be physically in the vehicle during authentication, which Connect doesn’t support at the moment:

* 2021+: XC40 Recharge
* 2022+: S90, S90 Recharge, V90, V90 Recharge, V90 Cross Country, XC60, XC60 Recharge, C40 Recharge
* 2023+: All models with the exception of the XC40

Even if the vehicle has been connected to and shows up in the Volvo app, if they go through Connect the account will present as if there are no vehicles on the account.


# Brand Subscription Information
Source: https://smartcar.com/docs/help/brand-subscriptions

Below you can find the connected service name for each brand as well as any specific subscription packages needed to connect to the vehicle via Smartcar.

| Make                        | Region                      | Connected Service                           | Package                                           | Subscription Cost                                                                                             |
| --------------------------- | --------------------------- | ------------------------------------------- | ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| Acura                       | US, Canada                  | ACURALINK                                   | Remote                                            | 3 year free trial (2023 and Newer Models), 6 month free trial (2022 and Older Models). \$110/year thereafter. |
| Alfa Romeo                  | US, Europe                  | My Alfa Connect                             | My Car and My Remote                              | 3 - 5 years included.                                                                                         |
| Audi                        | US                          | myAudi                                      | CARE                                              | -                                                                                                             |
|                             | Europe, Canada              | Audi Connect                                | Remote                                            | Free for three years after delivery of a new vehicle. \~£120/year thereafter.                                 |
| BMW                         | All                         | BMW Connected                               | -                                                 | Free trial varies with model year. \~\$120/year thereafter.                                                   |
| Buick                       | US, Canada                  | OnStar                                      | Remote Access                                     | Free trial varies with model year. \$14.99/month for standalone Remote Access package.                        |
| BYD                         | Europe                      | BYD (Connected Services)                    | -                                                 | -                                                                                                             |
| Cadillac                    | US, Canada                  | OnStar                                      | Remote Access                                     | Free trial varies with model year. \$14.99/month for standalone Remote Access package.                        |
| Chevrolet                   | US, Canada                  | OnStar                                      | Remote Access                                     | Free trial varies with model year. \$14.99/month for standalone Remote Access package.                        |
| Chrysler                    | US, Canada                  | Uconnect                                    | Sirius XM Guardian (Remote Package)               | 1 year free trial. \$12.99/month for the Remote Package thereafter.                                           |
| Citroën                     | Europe                      | My Citroën                                  | ë-remote services needed for remote commands      | -                                                                                                             |
| CUPRA                       | Europe                      | CUPRA CONNECT                               | Remote Access Services                            | 3 years free for the Born model, 1 year free for others. Price varies with region.                            |
| Dacia                       | Europe                      | My Dacia                                    | -                                                 |                                                                                                               |
| Dodge                       | US, Canada                  | Uconnect                                    | Sirius XM Guardian (Remote Package)               | 1 year free trial. \$12.99/month for the Remote Package thereafter.                                           |
| DS                          | Europe                      | MyDS                                        | E-TENSE Remote                                    | -                                                                                                             |
| Fiat                        | Europe                      | FIAT                                        | My Car and My Remote                              | 6 month free trial.                                                                                           |
|                             | US                          | FIAT Connect                                | Assistance Package                                | 3 month free trial with select vehicles. \$14.99/month.                                                       |
| Ford                        | All                         | FordPass                                    | -                                                 | -                                                                                                             |
| GMC                         | US, Canada                  | OnStar                                      | Remote Access                                     | Free trial varies with model year. \$14.99/month for standalone Remote Access package.                        |
| Honda                       | US                          | HondaLink                                   | EV Access for EV Data. Remote Access for Commands | EV Access 8 year trial. \$14.99/month for standalone Remote Access package.                                   |
| Hyundai                     | All                         | Hyundai BlueLink                            | -                                                 | 3 year free trial for new vehicles. \$9.90/month per package thereafter.                                      |
|                             | US                          | Hyundai BlueLink (2023 IONIQ 6 & all 2024+) | BlueLink+                                         | -                                                                                                             |
| Infiniti                    | US                          | MyINFINITI                                  | -                                                 | 1 year free trial. \$12.99/month thereafter.                                                                  |
| Jaguar                      | All                         | Jaguar InControl                            | -                                                 | 3 year free trial. \~\$100/year thereafter.                                                                   |
| Jeep                        | US, Canada                  | Uconnect                                    | Sirius XM Guardian (Remote Package)               | 1 year free trial. \$12.99/month for the Remote Package thereafter.                                           |
|                             | US, Canada                  | Jeep Connect                                | Sirius XM Guardian (Remote Package)               | 1 year free trial. \$12.99/month for the Remote Package thereafter.                                           |
| Kia                         | US, Canada                  | Kia Access                                  | Plus                                              | 1 year free trial. \$149/year thereafter.                                                                     |
|                             | Europe                      | Kia Connect                                 | -                                                 | 7 year free trial starting on sale to the first owner.                                                        |
| Land Rover                  | All                         | Land Rover InControl                        | -                                                 | 3 year free trial. \~\$100/year thereafter.                                                                   |
| Lexus                       | US, Canada                  | Lexus Enform                                | REMOTE                                            | Free trial up to 3 years, varies with model year. \$80/year thereafter.                                       |
| Lincoln                     | US                          | Lincoln Way                                 | -                                                 | -                                                                                                             |
| Mazda                       | US, Europe                  | MyMazda                                     | -                                                 | 3 year free trial. \$10/month thereafter.                                                                     |
| Mercedes                    | All                         | MeConnect                                   | -                                                 | 1 year free trial. \~\$15/year there after.                                                                   |
| Mini                        | All                         | Mini Connected                              | -                                                 | Free trial varies with model year. \~\$120/year thereafter.                                                   |
| Nissan                      | US                          | NissanConnect Services                      | - Convenience   - Select (EV data)                | Free trial varies with model year. $9.99 - $  21.98/month thereafter.                                         |
|                             | Europe                      | NissanConnect                               | -                                                 | Free trial varies with model year. \~£1.99/month thereafter.                                                  |
| Opel                        | Europe                      | myOpel                                      | e-Remote services needed for remote commands      | -                                                                                                             |
| Peugeot                     | Europe                      | MYPEUGEOT                                   | E-REMOTE CONTROL needed for remote commands       | -                                                                                                             |
| Polestar                    | All                         | Polestar                                    | -                                                 | Included (no separate paid Remote package required).                                                          |
| Porsche                     | US, Europe                  | My Porsche                                  |                                                   | 1 year free trial after initial purchase. \$299/year there after.                                             |
| RAM                         | US, Canada                  | Uconnect                                    | Sirius XM Guardian (Remote Package)               | 1 year free trial. \$12.99/month for the Remote Package thereafter.                                           |
|                             | US, Canada                  | Ram Connect                                 | Sirius XM Guardian (Remote Package)               | 1 year free trial. \$12.99/month for the Remote Package thereafter.                                           |
| Renault                     | Europe                      | My Renault                                  | -                                                 | -                                                                                                             |
| Rivian                      | US                          | Rivian                                      | -                                                 | -                                                                                                             |
| Skoda                       | Europe                      | MySKODA                                     | Care Connect                                      | \~£36/year.                                                                                                   |
| Subaru (excluding Solterra) | US                          | MySubaru                                    | STARLINK Security Plus                            | 6-month free trial. \$4.95/month thereafter.                                                                  |
| Subaru Solterra             | US                          | Solterra Connect                            | Remote Connect                                    | One-year trial included, \$8/month after trial.                                                               |
| Tesla                       | All                         | Tesla                                       | -                                                 | -                                                                                                             |
| Toyota                      | US, Canada                  | Toyota Connected Services                   | Remote Connect                                    | 1 year free trial. \$80/year thereafter.                                                                      |
| Vauxhall                    | Europe                      | myVauxhall                                  | e-Remote services needed for remote commands      | -                                                                                                             |
| Volkswagen                  | US                          | Car-Net                                     | Remote Access                                     | -                                                                                                             |
|                             | Europe (non-ID) 2018 - 2022 | Car-Net                                     | -                                                 | -                                                                                                             |
|                             | Europe (non-ID) ≤ 2023      | We Connect                                  | -                                                 | -                                                                                                             |
|                             | Europe (non-ID) 2024+       | VW Connect                                  | -                                                 | -                                                                                                             |
|                             | Europe (ID) Firmware \<3    | We Connect Start                            | -                                                 | -                                                                                                             |
|                             | Europe (ID) Firmware v3+    | We Connect ID                               | -                                                 | -                                                                                                             |
| Volvo                       | All                         | Volvo Cars                                  | -                                                 | Free trial varies with model year. \~\$200/year thereafter.                                                   |

## Notes

### Audi

* Owners will need to ensure they're the Primary or Key user for the vehicle connected to their account in order to access all Smartcar functionality.

### Ford and Lincoln

* Owners that use a username to login to their connected services app will need to migrate to using their email address under account settings in their Ford Pass or Lincoln Way portal.

### Onstar

* Chevy Bolts MY 2020+ come with the **EV Mobile Command** service included for 5 years with the purchase of a new vehicle. Location data is not included in the package. Bolt owners will need to also subscribe to **Remote Access** to be able to get access to location data.
* For all other OnStar accounts, we require the modern **Remote Access** plan as our base subscription. This plan comes with the **Vehicle Status** feature set, which is what enables our remote access to data from cars.
  More information can be found [in this PDF](https://my.chevrolet.com/content/dam/gmownercenter/gmna/dynamic/onstar/comparePlans/nbm/OC_Compare-Plans-Chevy.pdf).
* There are certain legacy OnStar accounts floating around with similar names. A good check on whether a customer has the correct plan or not is the ability to view vehicle information like fuel level, EV battery level, odometer, or tire pressure from within their vehicle’s mobile app.

### Nissan US

* Convenience features are included as part of the Premium package.

### Toyota

* The Remote Connect subscription is tied to the audio package purchased with the vehicle. Compatible audio package availability is determined based on the trim of the vehicle model and varies model year to model year.
  Toyota provides PDFs for Remote Connect availability [here](https://www.toyota.com/connected-services/#:~:text=Learn%20about%20your%20Connected%20Services).

### Uconnect

* For all Uconnect accounts, we require the ability to interact with vehicle information through the UConnect portal
* A Uconnect account may have access to Mopar, but not all Mopar accounts have access to UConnect. If a user can see information in Mopar but not UConnect, they’ll need to reach out to UConnect support to set up the right UConnect plan for their vehicle.
* 2021+ Jeeps have their own connected service - Jeep Connect
* 2022+ Rams have their own connected service - Ram Connect
* 2022+ Jeep Wagoneers have their own connected service - Wagoneer Connect
* Canada has limited support listed [here](https://www.driveuconnect.ca/en/sirius-xm-guardian-vehicles)

### Volkswagen ID Series

* Model year 2021 and certain 2022 Volkswagen ID vehicles require an upgrade to vehicle software version 3 which will allow you to get location and odometer data. This is a requirement for both US and European vehicles.

### Volvo

The following models are not currently compatible with Smartcar:

* 2021+ : XC40 Recharge
* 2022+ : S90, S90 Recharge, V90, V90 Recharge, V90 Cross Country, XC60, XC60 Recharge
* 2023+ : All models with the exception of the XC40


# Compatible Vehicles
Source: https://smartcar.com/docs/help/compatibility





# Connect your car
Source: https://smartcar.com/docs/help/connect-your-car





# Diagnostic Systems
Source: https://smartcar.com/docs/help/diagnostic-systems

To support our System Status endpoint, reference the below list of unified systems.

The [System Status](https://smartcar.com/docs/api-reference/get-system-status) endpoint returns a list of systems reported by any given vehicle, as well as their current state which may be "OK" or "ALERT".

## System IDs

|                                   |                                                           |
| --------------------------------- | --------------------------------------------------------- |
| `SYSTEM_ABS`                      | Antilock Braking Systems                                  |
| `SYSTEM_ACTIVE_SAFETY`            | Active Safety Systems                                     |
| `SYSTEM_AIRBAG`                   | Airbag Systems                                            |
| `SYSTEM_BRAKE_FLUID`              | Brake Fluid Level                                         |
| `SYSTEM_DRIVER_ASSISTANCE`        | Driver Assistance Systems                                 |
| `SYSTEM_EMISSIONS`                | Emissions Systems                                         |
| `SYSTEM_ABS`                      | Antilock Braking Systems                                  |
| `SYSTEM_ENGINE`                   | Engine Systems                                            |
| `SYSTEM_EV_BATTERY_CONDITIONING`  | EV Battery Conditioning Systems                           |
| `SYSTEM_EV_CHARGING`              | EV Charging Systems                                       |
| `SYSTEM_EV_DRIVE_UNIT`            | EV Drive Unit Systems                                     |
| `SYSTEM_EV_HV_BATTERY`            | EV High-Voltage Battery Systems                           |
| `SYSTEM_LIGHTING`                 | Lighting Systems                                          |
| `SYSTEM_MIL`                      | Malfunction Indiciator Lamp Systems (Check Engine Lights) |
| `SYSTEM_OIL_LIFE`                 | Oil Life Systems                                          |
| `SYSTEM_OIL_PRESSURE`             | Oil Pressure Systems                                      |
| `SYSTEM_OIL_TEMPERATURE`          | Oil Temperature Systems                                   |
| `SYSTEM_TELEMATICS`               | Telematics Systems                                        |
| `SYSTEM_TIRE_PRESSURE`            | Tire Pressure Systems                                     |
| `SYSTEM_TIRE_PRESSURE_MONITORING` | Tire Pressure MonitoringSystems                           |
| `SYSTEM_TRANSMISSION`             | Transmission Systems                                      |
| `SYSTEM_WASHER_FLUID`             | Washer Fluid Systems                                      |
| `SYSTEM_WATER_IN_FUEL`            | Water in Fuel Detection Systems                           |


# Frequently Asked Questions (FAQs)
Source: https://smartcar.com/docs/help/faqs



Below you'll find answers to some of the most frequently asked questions about Smartcar.

<AccordionGroup>
  <Accordion title="Does Smartcar make apps?">
    Smartcar does not build applications ourselves. Rather, we provide the building blocks that our customers need in order to build applications for a variety of use cases.
  </Accordion>

  <Accordion title="Do I need a connected services account?">
    Yes. For instance, if you own a VW, you will need to have Car-Net activated in the US or WeConnect in Europe. You can read more about connected service subscriptions [here](/help/brand-subscriptions).
  </Accordion>

  <Accordion title="What countries does Smartcar work in?">
    Take a look at our [Global Compatibility page](https://smartcar.com/global/) for the latest information on where Smartcar works.

    Smartcar is always expanding and working hard to ensure supported countries are stable and reliable. If your country is not currently supported, but you think we'll be a good fit for your use case, [schedule a demo](https://smartcar.com/demo/) and let's see how we can help you!
  </Accordion>

  <Accordion title="Which languages does Smartcar support?">
    [Smartcar Connect](/connect/what-is-connect) is available in English, Danish, German, Spanish (Spain), Spanish (Latin America), French, Italian, Dutch, Norwegian, and Swedish providing vehicle owners a native experience as they onboard vehicles to your platform.
  </Accordion>

  <Accordion title="How fresh is my data?">
    Smartcar will always try to pull the latest data point from any given vehicle. Each API response includes an [sc-data-age header](https://smartcar.com/docs/api#response-headers) that will contain the timestamp of when that data was last saved.

    Although each OEM saves data at different times, the data age header should not be older than the last time the vehicle was used.
  </Accordion>

  <Accordion title="How many cars is Smartcar compatible with?">
    <Tip>
      For a list of compatible vehicles, visit [our website](https://smartcar.com/product/compatible-vehicles/).
    </Tip>

    Smartcar is compatible with **161 million vehicles** across the US, Canada and Europe.

    **United States** <br />
    Smartcar is compatible with **29 car brands** in the United States.

    **Europe** <br />
    Smartcar is compatible with **19 car brands** in Europe.

    **Canada** <br />
    Smartcar is compatible with **21 car brands** in Canada.
  </Accordion>

  <Accordion title="Why isn't my car supported?">
    **If your make isn't supported...**

    We work hard to ensure that supported brands are stable and reliable, which takes time. If you don't see your make on our [compatibility page](https://smartcar.com/product/compatible-vehicles/) but you would like it to be, reach out to [support@smartcar.com](mailto:support@smartcar.com) to see how you can help speed up the process!

    **If we support your make, but not your model...**

    We might just need to do some additional testing. Sign up to our [research fleet](https://smartcar.com/research-fleet) and we'll reach out to see what we can do for you!

    **If we support your make, model, but not your year...**

    The majority of automakers only started adding internet connectivity to their cars around 2014. If you're able to access your car through a smartphone application and believe it should be supported, reach out to us and we'll be happy to take a look.
  </Accordion>

  <Accordion title="Smartcar versus Aftermarket Hardware">
    While on-board diagnostics dongles are versatile and useful for tracking and diagnostics of many kinds, they are far from ideal when it comes to mileage verification.
    They can be inaccurate, inconvenient, expensive and unreliable.Smartcar is only one example of a pure software alternative that uses API technology to offer the perfect
    mileage verification solution to auto insurance companies. Compared with traditional OBD-II devices, our API is accurate, cost efficient and tamper-resistant.

    You can read more about why using our API is a great choice on our [blog](https://smartcar.com/blog/obd-mileage-verification/).
  </Accordion>

  <Accordion title="Why do I see requests that resulted in a 460 status code with different error codes and error types on the Smartcar Dashboard?">
    In the event that we recieve a response from the OEM after the connection is closed, we will show the error code and error type we would have responded with on the Dashboard if the connection had been kept open.
  </Accordion>
</AccordionGroup>


# Submit a Feature Request
Source: https://smartcar.com/docs/help/feature-request



## Help Us Improve Smartcar!

Your feedback shapes our future. Have an idea or improvement you’d love to see? Submit your suggestions using the form below, and let us know how we can better serve your needs.

If you have trouble seeing the form below, please visit [this link](https://smartcarapi.notion.site/215f1477e9d380538219cb34866b8540?pvs=105) to submit your feature request.

<iframe src="https://smartcarapi.notion.site/ebd/215f1477e9d380538219cb34866b8540" width="100%" height="900" frameborder="0" allowfullscreen />


# Data Freshness Frequencies
Source: https://smartcar.com/docs/help/frequencies

Smartcar's goal is to provide as close to real-time data as possible based on available technologies and capabilities from OEMs. Although real-time is not yet available across all OEMs outside of commercial fleets, Smartcar continues to improve these frequencies as platforms and technologies evolve.

<Note>
  The values below indicate a range of how quickly you can expect to see fresh data and not how frequent you can receive data from Smartcar. i.e. You may request/receive odometer every three minutes from Smartcar, but its value won't change until it is refreshed by the OEM.
</Note>

**Data Frequency**: This indicates the frequency at which you receive vehicle data updates that Smartcar delivers to you via webhooks. This frequency can vary based on the vehicle make, the data type (such as location, odometer, or battery), and how frequently the vehicle is driven. In general, you can expect updates to arrive anywhere from every few minutes to once every few hours. While our slowest data rates for all OEMs is an hour, for many vehicles (including the fastest), when the vehicle is idle or "asleep", no updates will be provided since no change has occurred.

Smartcar automatically adjusts polling frequency based on vehicle status to balance timely updates with efficient resource use. While we aim to provide near real-time data when possible, exact timing depends on factors outside of Smartcar's control, such as OEM behavior and vehicle connectivity.

| Make          | Region     | Data Frequency Range (in min) |
| ------------- | ---------- | ----------------------------- |
| ACURA         | US, Canada | 30-60                         |
| ALFA ROMEO    | Global     | 5-10                          |
| AUDI          | Global     | 3-5                           |
| BMW           | Global     | 5-10                          |
| BUICK         | US, Canada | 30-45                         |
| BYD           | Europe     | 1-3                           |
| CADILLAC      | US, Canada | 30-45                         |
| CHEVROLET     | US, Canada | 30-45                         |
| CHRYSLER      | Global     | 5-10                          |
| CITROEN       | Europe     | 5-10                          |
| CUPRA         | Europe     | 5-10                          |
| DACIA         | Europe     | 30-60                         |
| DODGE         | Global     | 5-10                          |
| DS            | Europe     | 5-10                          |
| FIAT          | Global     | 5-10                          |
| FORD          | Global     | 5-10                          |
| GMC           | US, Canada | 30-45                         |
| HONDA         | US, Canada | 15-30                         |
| HYUNDAI       | Global     | 5                             |
| INFINITI      | US         | 5-10                          |
| JAGUAR        | Global     | 15-30                         |
| JEEP          | Global     | 5-10                          |
| KIA           | Global     | 5                             |
| LAND ROVER    | Global     | 15-30                         |
| LEXUS         | US         | 5-10                          |
| LINCOLN       | Global     | 5-10                          |
| MAZDA         | Global     | 5-10                          |
| MERCEDES BENZ | Global     | 5-10                          |
| MG            | Europe     | 30-60                         |
| MINI          | Global     | 30-60                         |
| NISSAN        | Europe     | 5-10                          |
| NISSAN        | US         | 5-10                          |
| OPEL          | Europe     | 5-10                          |
| PEUGEOT       | Europe     | 5-10                          |
| POLESTAR      | Global     | 1-3                           |
| PORSCHE       | Europe     | 30-60                         |
| RAM           | Global     | 5-10                          |
| RENAULT       | Europe     | 30-60                         |
| RIVIAN        | Global     | 3-5                           |
| SKODA         | Europe     | 5                             |
| SUBARU        | US         | 5-10                          |
| TESLA\*       | Global     | 1 sec - 5 min                 |
| TOYOTA        | US         | 30-60                         |
| VAUXHALL      | Europe     | 5-10                          |
| VOLKSWAGEN    | Europe     | 5-10                          |
| VOLKSWAGEN\*  | US         | 1-3                           |
| VOLVO         | Global     | 1-3                           |

## Notes

### \* Tesla

<Info>
  For Tesla vehicles capable of streaming, 3 minutes is the average of how often the data is refreshed. Depending on the data point and how often it changes, you may see data refreshed faster. For vehicles that do not support streaming, Smartcar fetches data from the vehicle every 5 minutes when the vehicle is awake.
</Info>

### \* Volkswagen US

<Info>
  For Volkswagen vehicles in the US, 3 minutes is the average of how often the data is refreshed. For EVs, you may see data refreshed faster when the vehicle is plugged in.
</Info>

{/*| -----------------------| */}

{/*| -                      | */}

{/*| 3 (US/CA/EUR)          | */}

{/*| 1 (US), 1 (CA)         | */}

{/*| 3 (US), 3 (CA)         | */}

{/*| 3 (EUR)                | */}

{/*| 3 (US), 3 (CA)         | */}

{/*| -                      | */}

{/*| 1 (CA)                 | */}

{/*| 1 (CA)                 | */}

{/*| 1 (US/CA/EUR)          | */}

{/*| 1 (US), 1 (CA), 3 (EUR)| */}

{/*| 1 (US), 2 (CA)         | */}

{/*| 3 (US/CA/EUR)          | */}

{/*| -                      | */}

{/*| 1 (EUR)                | */}

{/*| 3 (EUR)                | */}

{/*| 1 (US/EUR)             | */}

{/*| 1 (EUR)                | */}

{/*| 1 (EUR)                | */}

{/*| 1 (US/CA), 2 (EUR)     | */}

{/*| 1 (EUR)                | */}

{/*| 3 (US)                 | */}


# How to Submit a Ticket in the Support Center
Source: https://smartcar.com/docs/help/how-to-submit-ticket

Learn how to submit a support ticket through the Smartcar Support Center, including step-by-step instructions and eligibility details based on your plan.

<Info>
  For information on how to access the Smartcar Support Center, please visit the following article: [Accessing the Smartcar Support Center](/help/accessing-support-center)
</Info>

***

### **How to Submit a Support Ticket**

**1. Select "Submit a Ticket"**\
Once in the Support Center, click **"Submit a Ticket"** at the top right corner of the page to begin creating your ticket. <img src="https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/help-center/support-center/submit-ticket.png?fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=80b169e08bb58f9b98eb858abdabbe30" alt="Submit a Ticket" data-og-width="3360" width="3360" data-og-height="1754" height="1754" data-path="images/help-center/support-center/submit-ticket.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/help-center/support-center/submit-ticket.png?w=280&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=447743ab5894ecbcc7a691f6a02c538e 280w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/help-center/support-center/submit-ticket.png?w=560&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=a234ad51d9abf62b96308b378a642e0f 560w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/help-center/support-center/submit-ticket.png?w=840&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=b07bdcd9188832735d025b10c9e52833 840w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/help-center/support-center/submit-ticket.png?w=1100&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=c8d77b19e5419baf6465ee29feab2151 1100w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/help-center/support-center/submit-ticket.png?w=1650&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=966d80af826b07cc2cb35e1fa7a67b6b 1650w, https://mintcdn.com/smartcar-docs/YqcNJdgEDgXpXtEG/images/help-center/support-center/submit-ticket.png?w=2500&fit=max&auto=format&n=YqcNJdgEDgXpXtEG&q=85&s=6777b10fc2f6136d4876d52420763a32 2500w" />

**2. Fill Out the Ticket Form**\
Provide details such as:

* Subject
* Description
  * Please include as much relevant context as possible such as Session IDs, Vehicle IDs, screenshots, etc.
* The Smartcar Component affected
* The issue type

<img src="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/support-center/create-a-new-ticket.png?fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=91d72b48965a5dbc6ba89c9eaa20df7d" alt="Fill Out the Ticket Form" data-og-width="3360" width="3360" data-og-height="1851" height="1851" data-path="images/help-center/support-center/create-a-new-ticket.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/support-center/create-a-new-ticket.png?w=280&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=6be2c00b8ed5d86d260a5c0d89349a33 280w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/support-center/create-a-new-ticket.png?w=560&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=224d7fcbcfce41b744c2dcb4b094d7f7 560w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/support-center/create-a-new-ticket.png?w=840&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=ca9b47c013f32ceb7b1427e0717ca341 840w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/support-center/create-a-new-ticket.png?w=1100&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=5f07ff2df7da774391869c57a987c045 1100w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/support-center/create-a-new-ticket.png?w=1650&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=aee3698e259e2619b9100aaf856a9b30 1650w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/support-center/create-a-new-ticket.png?w=2500&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=6bf8db2c4cee5561f5d83c41cea60cc4 2500w" />

**3. Submit Your Ticket**\
Click **Submit**, and your request will be sent to our Support team.

**4. Track Your Request**\
You can view and track the status of your tickets under **"My Tickets"** in the Support Center. <img src="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/support-center/my-tickets.png?fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=ba91b60781ce83ffeb732c109c10600c" alt="Track Your Requests" data-og-width="3360" width="3360" data-og-height="1850" height="1850" data-path="images/help-center/support-center/my-tickets.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/support-center/my-tickets.png?w=280&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=d5e6291982ac3aef0e6430ee313562c7 280w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/support-center/my-tickets.png?w=560&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=afa2ad9de8ec84aae221a1ed506349cf 560w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/support-center/my-tickets.png?w=840&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=2170ca7fcae9c35f42bcfdc3bb56503a 840w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/support-center/my-tickets.png?w=1100&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=04cdb4cad3eb6c947aa7f110998ff15f 1100w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/support-center/my-tickets.png?w=1650&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=918b19887aedea46cc0bb71854551a08 1650w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/support-center/my-tickets.png?w=2500&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=44e47e3dae7bcf140fb48a7de7bd004a 2500w" />

**5. Update or Close a Request**\
Select the ticket you'd like to update or close from the **"My Tickets"** view. Once you're on the ticket page:

* Click **"Reply"** at the bottom left to add more information or request a status update.
* Click **"Close Ticket"** at the bottom right to mark the request as **Closed - Resolved** if you no longer need assistance. <img src="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/support-center/reply-and-close.png?fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=2ec0302e9189c360db7dea39d15f8287" alt="Update or Close a Request" data-og-width="3360" width="3360" data-og-height="1859" height="1859" data-path="images/help-center/support-center/reply-and-close.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/support-center/reply-and-close.png?w=280&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=ff9169c4a3410875abb4acc7f4c5fcd7 280w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/support-center/reply-and-close.png?w=560&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=2b4ef90007dd220da9360fd3af67213e 560w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/support-center/reply-and-close.png?w=840&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=4a3486a5aa552943652cbfb4d037dc67 840w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/support-center/reply-and-close.png?w=1100&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=21438da0ac095598efb5e901c460e871 1100w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/support-center/reply-and-close.png?w=1650&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=771450347e6ea23f9cf2cde87283c885 1650w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/support-center/reply-and-close.png?w=2500&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=ac89be098828a60df6792b324ee22030 2500w" />

***

### **Who can submit tickets?**

Ticket submission is available to users on **Build** and **Custom** **Enterprise** plans.

**Free plan users** can access the Docs Center and AI Agent within the Dashboard for assistance but do not have access to submit tickets.


# mySmartcar
Source: https://smartcar.com/docs/help/my-smartcar

With [mySmartcar](https://my.smartcar.com/login), you can see which apps are connected to your vehicle and manage their permissions anytime.

## Log in

Log into [mySmartcar](https://my.smartcar.com/login) by providing your preferred email address. A 6-digit code will be sent to you by email, which will grant access to mySmartcar.

<Frame>
  <img src="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/mysmartcar/mysmartcar-login.png?fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=227273a3bb7f9a2c390eb06b3ab548b5" data-og-width="985" width="985" data-og-height="496" height="496" data-path="images/help-center/mysmartcar/mysmartcar-login.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/mysmartcar/mysmartcar-login.png?w=280&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=6a382bad851389e0e5d52c0f6a652017 280w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/mysmartcar/mysmartcar-login.png?w=560&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=4030bec5be6df02b7758591a9775d50d 560w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/mysmartcar/mysmartcar-login.png?w=840&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=565663eacc142a09b97f93168f610b3a 840w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/mysmartcar/mysmartcar-login.png?w=1100&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=682444bc1e46cbf115183960dbfd1e38 1100w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/mysmartcar/mysmartcar-login.png?w=1650&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=339b2c3bc7759fcbbcdf6087a6f0a97c 1650w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/mysmartcar/mysmartcar-login.png?w=2500&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=156b1d3c1985ccb2b1466e35caa886d3 2500w" />
</Frame>

## Connect your OEM account

Now press "Connect your Car" and follow the on-screen prompts to pair your Connected Services account with mySmartcar.

<Frame>
  <img src="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/mysmartcar/mysmartcar-connect.png?fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=b9a3adeac57cf04d9b38fdaf7ba9a0a1" data-og-width="960" width="960" data-og-height="408" height="408" data-path="images/help-center/mysmartcar/mysmartcar-connect.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/mysmartcar/mysmartcar-connect.png?w=280&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=fabbde0f3e5262e96846d13cf7718b59 280w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/mysmartcar/mysmartcar-connect.png?w=560&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=ce79a7ad6983535d58ce0ce8b28dd09d 560w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/mysmartcar/mysmartcar-connect.png?w=840&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=f6b1d84fcb5ee9ce6c39e88661d6ffef 840w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/mysmartcar/mysmartcar-connect.png?w=1100&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=6abfc559006e7d01f40cc2884ac83d63 1100w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/mysmartcar/mysmartcar-connect.png?w=1650&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=d237c513da5d10c8bfa5775da6614c2b 1650w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/mysmartcar/mysmartcar-connect.png?w=2500&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=be665141c28af479380b3123a0172b96 2500w" />
</Frame>

## Review and manages connected apps

Once your OEM account is connected, Smartcar will provide a list of each application connected via Smartcar to your Connected Services account. Here you can see when the app was first granted access and the permissions requested.

Should you wish to disconnect an application, click "Revoke Access" and confirm to remove access to your vehicle's data for that application.

<Frame>
  <img src="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/mysmartcar/mysmartcar-review.png?fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=2caae71bb4f9a047c4d424438b2aec7d" data-og-width="1646" width="1646" data-og-height="962" height="962" data-path="images/help-center/mysmartcar/mysmartcar-review.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/mysmartcar/mysmartcar-review.png?w=280&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=49fd2a90cf1b58e6926c6686d8baaf25 280w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/mysmartcar/mysmartcar-review.png?w=560&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=03c2c7741f7761fab5a5c59afecc645e 560w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/mysmartcar/mysmartcar-review.png?w=840&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=1b0460a5c2635a68656050edac45ae82 840w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/mysmartcar/mysmartcar-review.png?w=1100&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=af9f17be8d7b835d0db22c034cab13e5 1100w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/mysmartcar/mysmartcar-review.png?w=1650&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=6ee2ea68420049576ee3c3f48e88d9f2 1650w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/mysmartcar/mysmartcar-review.png?w=2500&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=c74e2f3618181c58b625e816b0d16e29 2500w" />
</Frame>


# Tesla Permission Info
Source: https://smartcar.com/docs/help/oem-integrations/tesla/developers

This page has information regarding Smartcar's upgraded Tesla integration.

## Updating access with Tesla

You can use either of the following URLs to prompt users for more Tesla
permissions in the event you need additional access from the
vehicle owner due to:

* A [PERMISSION](/errors/api-errors/permission-errors) error from API

* A [CONNECTED\_SERVICES\_ACCOUNT:PERMISSION](/errors/api-errors/connected-services-account-errors#permission) error from API

* Needing access to an endpoint out of scope for your existing permissions

If one or more of the Smartcar scopes you pass map to a new Tesla permission(s)
for the account, the user will be prompted to update access after they log in
with Tesla.

<Tabs>
  <Tab title="Authorize">
    <Info>
      This flow sends a new authorization code to your callback URI in order to fetch a new access and refresh token.
    </Info>

    ```
        https://connect.smartcar.com/oauth/{path}?
        response_type=code
        &make=TESLA
        &client_id=8229df9f-91a0-4ff0-a1ae-a1f38ee24d07
        &scope=read_odometer control_security
        &redirect_uri=https://example.com
    ```

    | name            | type            | required | description                                                                                                                                                                                                                                                                                                            |
    | --------------- | --------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | `response_type` | `string`        | true     | This should be set to `code`.                                                                                                                                                                                                                                                                                          |
    | `make`          | `string`        | true     | Specifies the brand to update access to. Currently, the only make available for this flow is `TESLA`.                                                                                                                                                                                                                  |
    | `client_id`     | `string`        | true     | The application’s unique identifier. This is available on the credentials tab of the Smartcar Dashboard.                                                                                                                                                                                                               |
    | `scope`         | `[permissions]` | true     | A space-separated list of permissions that your application is requesting access to. The valid permission names can be found in the [permissions](/api-reference/permissions) section. When reauthenticating, the user will be required to grant the corresponding OEM permissions before being able to exit the flow. |
    | `redirect_uri`  | `string`        | true     | Required if using the `/authorize` route for Smartcar to return an authorization code.                                                                                                                                                                                                                                 |
  </Tab>

  <Tab title="Reauthenticate">
    <Info>
      This flow **will not** send back an authorization code to fetch a new
      refresh and access token, or redirect the user back to your application.
      Continue to use the access and refresh tokens you have on file for
      associated vehicles.
    </Info>

    ```
        https://connect.smartcar.com/oauth/reauthenticate?
        response_type=vehicle_id
        &make=TESLA
        &client_id=8229df9f-91a0-4ff0-a1ae-a1f38ee24d07
        &scope=read_odometer control_security
    ```

    | name            | type            | required | description                                                                                                                                                                                                                                                                                                            |
    | --------------- | --------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | `response_type` | `string`        | true     | This should be set to `vehicle_id` .                                                                                                                                                                                                                                                                                   |
    | `make`          | `string`        | true     | Specifies the brand to revoke access to. Currently, the only make available for this flow is `TESLA`.                                                                                                                                                                                                                  |
    | `client_id`     | `string`        | true     | The application’s unique identifier. This is available on the credentials tab of the Smartcar Dashboard.                                                                                                                                                                                                               |
    | `scope`         | `[permissions]` | true     | A space-separated list of permissions that your application is requesting access to. The valid permission names can be found in the [permissions](/api-reference/permissions) section. When reauthenticating, the user will be required to grant the corresponding OEM permissions before being able to exit the flow. |
  </Tab>
</Tabs>

## Requiring Tesla Permissions

To ensure users select the necessary permissions with Tesla before
being able to connect their vehicle via Smartcar, please append the `required:`
prefix to Smartcar scopes in your Connect URL e.g. `required:read_location`.

As a result if they do not select the necessary permissions with Tesla, they will see the
following screen and be prompted to return to Tesla to update their permissions.

<Frame>
  <img src="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/tesla-missing-permissions.png?fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=3c3de6736086f806218fd439716cee9a" data-og-width="1308" width="1308" data-og-height="1923" height="1923" data-path="images/help-center/oem-integrations/tesla/tesla-missing-permissions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/tesla-missing-permissions.png?w=280&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=5fb01d16d7c34e696a86a443ba50c30d 280w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/tesla-missing-permissions.png?w=560&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=e0def47b1a2240586d2225c01b04f848 560w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/tesla-missing-permissions.png?w=840&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=4fe026ad6d521f59d29ad46b60c35796 840w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/tesla-missing-permissions.png?w=1100&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=41aaba09ac860b141dba082845659333 1100w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/tesla-missing-permissions.png?w=1650&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=400fde9714c485477336556f605b94d9 1650w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/tesla-missing-permissions.png?w=2500&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=22465ccd5c736ce89d9e51aeff01f4d6 2500w" />
</Frame>

## Permission Mappings

Tesla provides a limited set of permissions. To ensure vehicle data is shared only with explicit consent, Smartcar has mapped Tesla’s permissions into its existing more granular options. For example, granting access to “vehicle commands” in a Tesla account allows an application to start or stop charging, lock or unlock doors, enable or disable Sentry Mode, and more. Smartcar separates these permissions so that applications must request access to control charging separately from access to vehicle security, control navigation, etc. Smartcar does not use or share vehicle data beyond the permissions listed in this table. An application with the ability to control the charge status of a vehicle, does not have access to control other aspects of the car unless explictly requested and granted by a vehicle owner.

| Smartcar Permission          | Tesla Permission                                    |
| ---------------------------- | --------------------------------------------------- |
| `control_charge`             | Vehicle Charge Management (vehicle\_charging\_cmds) |
| `control_climate`            | Vehicle Commands (vehicle\_cmds)                    |
| `control_navigation`         | Vehicle Commands (vehicle\_cmds)                    |
| `control_pin`                | Vehicle Commands (vehicle\_cmds)                    |
| `control_security`           | Vehicle Commands (vehicle\_cmds)                    |
| `control_trunk`              | Vehicle Commands (vehicle\_cmds)                    |
| `read_battery`               | Vehicle Information (vehicle\_device\_data)         |
| `read_charge_records`        | Vehicle Charge Management (vehicle\_charging\_cmds) |
| `read_charge`                | Vehicle Information (vehicle\_device\_data)         |
| `read_climate`               | Vehicle Information (vehicle\_device\_data)         |
| `read_compass`               | Vehicle Information (vehicle\_device\_data)         |
| `read_engine_oil`            | Vehicle Information (vehicle\_device\_data)         |
| `read_extended_vehicle_info` | Vehicle Information (vehicle\_device\_data)         |
| `read_fuel`                  | Vehicle Information (vehicle\_device\_data)         |
| `read_location`              | Vehicle Location (vehicle\_location)                |
| `read_odometer`              | Vehicle Information (vehicle\_device\_data)         |
| `read_security`              | Vehicle Information (vehicle\_device\_data)         |
| `read_speedometer`           | Vehicle Information (vehicle\_device\_data)         |
| `read_thermometer`           | Vehicle Information (vehicle\_device\_data)         |
| `read_tires`                 | Vehicle Information (vehicle\_device\_data)         |
| `read_user_profile`          | Profile Information (user\_data)                    |
| `read_vehicle_info`          | Vehicle Information (vehicle\_device\_data)         |
| `read_vin`                   | Vehicle Information (vehicle\_device\_data)         |


# Tesla FAQs
Source: https://smartcar.com/docs/help/oem-integrations/tesla/faqs

FAQs on our new Tesla integration. For an overview of the changes see [this page](https://smartcar.com/docs/help/oem-integrations/tesla/whats-new).

#### What happens if I connect to one of my applications with the legacy flow and another with the new flow?

As long as you have access to the same set of permissions on Tesla’s side and have added our virtual key there will not be any conflicts while the legacy API is active.

#### If my users have more than one Tesla on their account, will they need to add the virtual key to all of their vehicles?

Yes. You will need to add our virtual key to each vehicle on the Tesla account.

#### What happens if I issue a command but Smartcar’s virtual key hasn’t been added to the vehicle?

We will throw a `CONNECTED_SERVICES_ACCOUNT:VIRTUAL_KEY_REQUIRED` error.

## Do all vehicles need a virtual key?

2020 and earlier Model S and X **will not** require a virtual key to keep
working at this time. Smartcar will poll these vehicles in the background every
5 minutes for data. These requests **will not** wake the vehicle.

#### What happens if a user does not add a virtual key for vehicles that support streaming?

If a vehicle is streaming capable and does not yet have a virtual key installed,
requests to the vehicle will be limited to 1 request every 8 hours for data. These requests **will
not** wake the vehicle.

#### What happens if I issue a command but the owner has revoked access through their Tesla portal?

We will throw a `CONNECTED_SERVICES_ACCOUNT:PERMISSION` error.

#### What happens if a user doesn’t select the correct permissions on Tesla’s side?

Connect maps Tesla’s permissions to Smartcar’s and only grants your application access to the ones requested. If we do not get the corresponding permission from Tesla, we will not grant your application access and throw the `PERMISSION:NULL` error as per usual when you make an API request.

Your users will need to [revoke access](/help/oem-integrations/tesla/faqs#how-can-my-users-update-their-permissions-with-tesla) through the Tesla portal, then step through the flow again in order to fix this.

#### How can I tell which cars have gone through the new flow?

The [Migration Status](/api-reference/tesla/get-migration-status) make specific endpoint indicates if a vehicle still needs to be migrated to Tesla's new API.

#### Can owner and driver accounts authorize access with Smartcar through Connect?

Yes. Either account type can go through the Connect flow. As long as the Tesla account is attached to the vehicle, you can make requests to it.

#### Does the user need to be next to vehicle when adding a virtual key?

Owner accounts can add a virtual key remotely. Driver accounts need to be in
bluetooth range in order to add a virtual key.

#### Can driver accounts add a virtual key?

Yes. However, driver accounts can only pair virtual keys via bluetooth. They
cannot add a virtual key remotely.

#### Why are my users are seeing a location sharing notification on their navigation unit?

With the [recent changes to data
access](/help/oem-integrations/tesla/whats-new), vehicles will transmit their
live location if your application has requested access to location data. This
notification was put in place by Tesla to ensure transparency for owners about
what data is being shared and with whom.

The domain displayed will match the Virtual Key for your application.

<img src="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/tesla-location-notification.png?fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=199d257346ee46c2e486a370e0b190f8" data-og-width="909" width="909" data-og-height="927" height="927" data-path="images/help-center/oem-integrations/tesla/tesla-location-notification.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/tesla-location-notification.png?w=280&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=653ace5fd5561326713a909ee559e175 280w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/tesla-location-notification.png?w=560&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=ee3d64ac5d81cf5af33dfe1a715c45b8 560w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/tesla-location-notification.png?w=840&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=429ff9f5e78ecc2cffccea9526ea8168 840w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/tesla-location-notification.png?w=1100&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=c76c4c2f2f2583b698a8465cdfc1aff8 1100w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/tesla-location-notification.png?w=1650&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=0d4096a7631690de964f7ec430a64dc6 1650w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/tesla-location-notification.png?w=2500&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=8d16ada3c12e5ce2afb22757d10a0452 2500w" />

#### How can my users update their permissions with Tesla?

Please [this guide](/help/oem-integrations/tesla/developers#updating-access-with-tesla) for details on how to do facilitate this for your users.


# Virtual Keys
Source: https://smartcar.com/docs/help/oem-integrations/tesla/virtual-key-tesla

This page has information regarding the use of Virtual Keys for Tesla vehicles.

## What is a Virtual Key?

A Virtual Key is a digital access method required by Tesla for third-party
applications to issue commands to Tesla vehicles and the preferred method for accessing data.
Please see [this
section](/help/oem-integrations/tesla/developers#adding-a-virtual-key)
for more information.

### Adding the Virtual Key

Smartcar handles this step on your behalf in the Connect flow. You can get started with the default Smartcar Virtual Key with no configurations required.

If you're on an **Enterprise** plan, please reach out to your Account Manager or
Solutions Architect for information on setting up a custom Virtual Key with your own brand name.

## Where can I find my Virtual Key?

Although Smartcar handles this step on your behalf, the Virtual Key URL for your application is sent back along with the authorization code after a user completes the Connect flow. You can redirect users to this URL if they need to add the Virtual Key again.

### Vehicle Owners adding a Virtual Key

Smartcar Connect will present Tesla vehicle owners a prompt to install the Tesla Virtual Key after granting access and prior to redirecting them back to your application.

<Frame caption="Prompting the user to add a Virtual Key">
  <img width="700" src="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/VirtualKeyPageMobile.png?fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=e504d181b6936f3e0ba17926a2923be2" data-og-width="2283" data-og-height="931" data-path="images/help-center/oem-integrations/tesla/add-virtual-key/VirtualKeyPageMobile.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/VirtualKeyPageMobile.png?w=280&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=02c5b864bdd1e8c5541ed1a1bfc80549 280w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/VirtualKeyPageMobile.png?w=560&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=a1ca3a12ee41154e396ae4ce1b56af65 560w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/VirtualKeyPageMobile.png?w=840&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=89747ff417caaf5f36b30737aa24bd0a 840w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/VirtualKeyPageMobile.png?w=1100&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=6f5036a32588937a17a0ea6fb0adc4bb 1100w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/VirtualKeyPageMobile.png?w=1650&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=3e4e9358fb3e91fc7e6b1ad8bc7bac0d 1650w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/VirtualKeyPageMobile.png?w=2500&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=b8b9c2e23830523d41d1c9c753d3b309 2500w" />
</Frame>

The Virtual Key is a URL in the form:

<Tabs>
  <Tab title="Free or Build Plans">
    ```
    https://www.tesla.com/_ak/smartcar.com
    ```
  </Tab>

  <Tab title="Enterprise Plan">
    ```
    https://www.tesla.com/_ak/{{custom_subdomain}}.app.car
    ```
  </Tab>
</Tabs>

After prompting your users to open the link, depending on their device, they will be redirected to the Tesla app or prompted to scan a QR code.

<Tip>
  Adding a Virtual Key will need to be done after a user has granted your application access to their Tesla account in the Connect flow.

  Please see our [FAQs](/help/oem-integrations/tesla/faqs#can-owner-and-driver-accounts-authorize-access-with-smartcar-through-connect) for details on adding a virtual key for accounts with multiple vehicles and different account types.
</Tip>

<Tabs>
  <Tab title="Mobile Device">
    On mobile devices, they will be redirected to the Tesla app and prompted to add the Virtual Key

    <Frame caption="Opening the link on a mobile device with the Tesla app installed">
      <img width="600" src="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/mobile.png?fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=1aa3cfa6758a83b3c5384019c8ce9516" data-og-width="4964" data-og-height="4854" data-path="images/help-center/oem-integrations/tesla/add-virtual-key/mobile.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/mobile.png?w=280&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=38179fb64a3f35c9c6412881a41f63a2 280w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/mobile.png?w=560&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=dd132f40eaf0ac8ce3f8c06a4a49937a 560w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/mobile.png?w=840&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=d1f968b7d55de343324b9c34fa1445ae 840w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/mobile.png?w=1100&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=40b9a8fa4ac2c2060da42b5cf08d849b 1100w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/mobile.png?w=1650&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=a01aa61cae09b50959b4f8d03936e056 1650w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/mobile.png?w=2500&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=2978ca715f21ff393c8a6fcd150d6b96 2500w" />
    </Frame>
  </Tab>

  <Tab title="Desktop">
    On Desktop, they will be prompted to scan the QR code which in turn opens up the Tesla app and prompts them to add a Virtual Key

    <Frame caption="Opening the link on a desktop">
      <img width="600" src="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/desktop.png?fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=d23186ba53fe3df10da5569734e35a55" data-og-width="2000" data-og-height="2283" data-path="images/help-center/oem-integrations/tesla/add-virtual-key/desktop.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/desktop.png?w=280&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=1fef759823638e7e4bef332c9ecc2746 280w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/desktop.png?w=560&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=b540a6e8a73a09c2335212f7e76cc83d 560w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/desktop.png?w=840&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=925d9141cba67f54650113d5b89eff78 840w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/desktop.png?w=1100&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=fb91f775461570fbf9babf0d1aa09e3f 1100w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/desktop.png?w=1650&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=072106f529447f5d80c34d216936f07c 1650w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/desktop.png?w=2500&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=c64d864789f7d4e035cc4c50bf2cb7dd 2500w" />
    </Frame>
  </Tab>
</Tabs>

Virtual Key status can be checked at any time from the Tesla infotainment screen under Settings, Locks.

<Frame caption="Check Virtual Key status from your Tesla">
  <img width="600" src="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/infotainment.png?fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=2aa353d17ed5cde11109469fd2e0a798" data-og-width="2720" data-og-height="1802" data-path="images/help-center/oem-integrations/tesla/add-virtual-key/infotainment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/infotainment.png?w=280&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=79989c8784343f6e73094b0e0ebcf348 280w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/infotainment.png?w=560&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=d8b4063d497c846e867109f96ee6afad 560w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/infotainment.png?w=840&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=4df5837d63f70457f4be3a837ad565d9 840w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/infotainment.png?w=1100&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=13e05d49490a3d98848e8045e183fb2c 1100w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/infotainment.png?w=1650&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=b6b2d077092b08c3fb72f852f706d256 1650w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/infotainment.png?w=2500&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=990cf7ae17b09c73129ac1eb6cf934ae 2500w" />
</Frame>

## Do all vehicles need a virtual key?

2020 and earlier Model S and X **will not** require a virtual key at this time. Data for these vehicles is refreshed every
5 minutes while the vehicle is awake.

## What if a streaming capable vehicle does not have a virtual key installed?

If a vehicle is streaming capable and does not yet have a virtual key installed,
requests to the vehicle will be limited to 1 request every 8 hours for data. These requests **will
not** wake the vehicle.


# Important Updates
Source: https://smartcar.com/docs/help/oem-integrations/tesla/whats-new

Upcoming changes to data access and permissions in 2025

## May 20, 2025

Smartcar now handles adding Virtual Keys for Tesla vehicles on your behalf in the Connect flow. Virtual Keys are required for third-party applications to issue commands to Tesla vehicles and are the preferred method for accessing data.

<Frame type="simple">
  <img src="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/VirtualKeyPageMobile.png?fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=e504d181b6936f3e0ba17926a2923be2" data-og-width="2283" width="2283" data-og-height="931" height="931" data-path="images/help-center/oem-integrations/tesla/add-virtual-key/VirtualKeyPageMobile.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/VirtualKeyPageMobile.png?w=280&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=02c5b864bdd1e8c5541ed1a1bfc80549 280w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/VirtualKeyPageMobile.png?w=560&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=a1ca3a12ee41154e396ae4ce1b56af65 560w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/VirtualKeyPageMobile.png?w=840&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=89747ff417caaf5f36b30737aa24bd0a 840w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/VirtualKeyPageMobile.png?w=1100&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=6f5036a32588937a17a0ea6fb0adc4bb 1100w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/VirtualKeyPageMobile.png?w=1650&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=3e4e9358fb3e91fc7e6b1ad8bc7bac0d 1650w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/VirtualKeyPageMobile.png?w=2500&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=b8b9c2e23830523d41d1c9c753d3b309 2500w" />
</Frame>

For more details, visit the [Virtual Key documentation](/help/oem-integrations/tesla/virtual-key-tesla).

## January 10, 2025

Starting in March 2025, Tesla will require a new permission to access live
location data for its vehicles. Due to this change, you have two options:

**If your application needs live location data:**<br />
Users will need to reauthenticate and grant explicit access to the Vehicle
Location permission to continue receiving location data beyond March 2025, if
they haven’t already done so. This permission was previously included as part of
the Vehicle Information permission.

**If your application only needs to know whether the vehicle is at home:**<br />
A new boolean value will be available soon, and it will not require
reauthentication. Vehicle owners can set their home location in the Tesla
application.

### Why is this change occurring?

Tesla now provides users more granular data access control, and requires vehicle
owners to explicitly consent to sharing location data with 3rd parties like
Smartcar. This ultimately gives drivers more control and awareness of how and
what data they decide to share.

### Next steps if you need live location data

**1. Check existing permissions** <br />
Use the [User Access](/api-reference/tesla/get-user-access) endpoint to verify whether a vehicle has already
been granted the required permission on Tesla's side.

**2. Update Smartcar Connect scopes**<br />
To ensure vehicle owners grant the new permission, append `required:` to your
scopes in the Smartcar Connect URL (for example, `required:read_location`). For
detailed instructions, please refer to [this guide](/help/oem-integrations/tesla/developers#requiring-tesla-permissions).

**3. Prompt users to reauthenticate**<br />
If needed, guide users to reauthenticate their Tesla vehicles using the methods outlined
[here](/help/oem-integrations/tesla/developers#updating-access-with-tesla).

<br />

<Warning>
  If the Vehicle Location permission isn’t granted by March 2025, you may
  encounter a `PERMISSION` error. As a result, your
  application will no longer receive live location data from affected Tesla
  vehicles until they reauthenticate.
</Warning>

## December 19, 2024

Starting **January 21, 2025**, a Virtual Key will be required to maintain access to
Tesla vehicle data. Failure to make the necessary changes could result in a
disruption to your service after this date. Below, we’ve outlined the steps you
need to take to prepare, depending on your situation.

### For new developers

If you're on an **Enterprise** plan, please reach out to your Account Manager or
Solutions Architect for information on setting up your own Virtual Key.

**Free** and **Build** customers can get started with the default Virtual Key.

### For existing developers

<AccordionGroup>
  <Accordion title="I'm using an app.car subdomain that Smartcar has created for me">
    **What’s changing?**

    Telsa is changing the way data can be accessed by 3rd party applications.

    **What do you need to do?**

    To ensure continuous data access, please have your users add your Virtual Key to
    their vehicles if they haven’t already.  They can follow [this
    guide](https://smartcar.com/docs/help/oem-integrations/tesla/developers#adding-a-virtual-key)
    for more information. If you already prompt users to add a Virtual Key as your
    application issues commands - no additional work is needed, please continue to
    do so.

    **What is a Virtual Key?**

    A virtual key is a digital access method required by Tesla for third-party
    applications to receive vehicle data and issue commands to Tesla vehicles.
    Please see [this
    guide](https://smartcar.com/docs/help/oem-integrations/tesla/developers#adding-a-virtual-key)
    for more information.

    **Where can I find my Virtual Key?**

    The Virtual Key URL for your application will be sent back along with the
    authorization code after a user completes the Connect flow.
    Alternatively, you can reach out to Support or your Account Manager and they'll be able to provide
    it to you.

    **What happens if my users do not add my Virtual Key?**

    Starting January 21, 2025 you will not be able to get data from Tesla vehicles
    you are connected to and will receive a `virtual_key_required` error instead
    ([docs](https://smartcar.com/docs/errors/api-errors/connected-services-account-errors#virtual-key-required)).

    **What about vehicles that do not support Virtual Keys?**

    2020 and earlier Model S and X **will not** require a Virtual Key to keep
    working at this time. However, you may not always receive the latest data from
    the vehicle when you make an API request to Smartcar.

    **Will my users need to reauthenticate?**

    No. They simply need to add the Virtual Key to their vehicle.
  </Accordion>

  <Accordion title="I'm using Smartcar's default Tesla application">
    **What’s changing?**

    Tesla is changing the way data can be accessed by 3rd party applications.

    **What do you need to do?**

    To ensure continuous data access, please have your users add your Virtual Key to their vehicles if they haven’t already.  They can
    follow [this
    guide](https://smartcar.com/docs/help/oem-integrations/tesla/developers#adding-a-virtual-key)
    for more information. If you already prompt users to add a Virtual Key as your
    application issues commands - no additional work is needed, please continue to
    do so.

    **What is a Virtual Key?**

    A virtual key is a digital access method required by Tesla for third-party
    applications to receive vehicle data and issue commands to Tesla vehicles.
    Please see [this
    guide](https://smartcar.com/docs/help/oem-integrations/tesla/developers#adding-a-virtual-key)
    for more information.

    **Where can I find my Virtual Key?**

    The Virtual Key URL for your application will be sent back along with the
    authorization code after a user completes the Connect flow. The Virtual Key URL
    is:
    [`https://www.tesla.com/_ak/smartcar.com`](https://www.tesla.com/_ak/smartcar.com)

    **What happens if my users do not add my Virtual Key?**

    Starting January 21, 2025 you will not be able to get data from Tesla vehicles
    you are connected to and will receive a `virtual_key_required` error instead
    ([docs](https://smartcar.com/docs/errors/api-errors/connected-services-account-errors#virtual-key-required)).

    **What about vehicles that do not support Virtual Keys?**

    2020 and earlier Model S and X **will not** require a Virtual Key to keep
    working at this time. However, you may not always receive the latest data from
    the vehicle when you make an API request to Smartcar.

    **Will my users need to reauthenticate?**

    No. They simply need to add the Virtual Key to their vehicle.
  </Accordion>
</AccordionGroup>


# Important Updates
Source: https://smartcar.com/docs/help/oem-integrations/vw/whats-new

Updates regarding the Volkswagen Smartcar Integration.

## May 28th, 2025

Smartcar is excited to announce a new and improved integration with Volkswagen Group of America. is a testament to our mission of unlocking seamless mobility experiences for everyone.

Starting today, VW vehicle owners connecting their cars in the US to Smartcar powered applications will be redirected to Volkswagen's login page for authentication, vehicle selection, and acceptance of VW's terms as part of the Smartcar Connect flow. This change does not affect existing VW vehicle connections.

<Frame type="simple">
  <img src="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/vw/volkswagen-flow.png?fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=976adb1821a643171f8a68e9af0f0c86" data-og-width="7012" width="7012" data-og-height="2890" height="2890" data-path="images/help-center/oem-integrations/vw/volkswagen-flow.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/vw/volkswagen-flow.png?w=280&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=2f62a21896b840f025044dc86fe33b7d 280w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/vw/volkswagen-flow.png?w=560&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=647d65fc63468783658289479aa8e322 560w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/vw/volkswagen-flow.png?w=840&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=95476326cd0b25cab695f6873f1ccef8 840w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/vw/volkswagen-flow.png?w=1100&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=93ad2518f328c515780046171d3cd5fe 1100w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/vw/volkswagen-flow.png?w=1650&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=82b518db41b0d47858ee88ca3ac3c1e9 1650w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/vw/volkswagen-flow.png?w=2500&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=2164aae0e8343df53f439a102e079ac5 2500w" />
</Frame>

Vehicle owners will receive an email from Volkswagen notifying them of new services being added to their account.

<Frame type="simple">
  <img src="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/vw/vw-connection-email.png?fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=a3ccfe86772ab239d029d4a63dffd42f" data-og-width="1510" width="1510" data-og-height="2398" height="2398" data-path="images/help-center/oem-integrations/vw/vw-connection-email.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/vw/vw-connection-email.png?w=280&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=8de5053cb43d1127ebcc07bb0fe424d9 280w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/vw/vw-connection-email.png?w=560&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=d1ee88e895403822b9ddf45d0b34e369 560w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/vw/vw-connection-email.png?w=840&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=f5ae1fb1b4fb76760162ec9df9214f56 840w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/vw/vw-connection-email.png?w=1100&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=d09464cf2a21c9312c0476c863de60f4 1100w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/vw/vw-connection-email.png?w=1650&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=52953f511c9920d6a1c45bcd89dd3d5a 1650w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/vw/vw-connection-email.png?w=2500&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=9a03ffa0a21c4ed361dfab197dbb492f 2500w" />
</Frame>

Vehicle owners can revoke access to Smartcar powered applications at any time through the myVW Mobile App or by logginginto their account online.

### Notes

* This change is only applicable to VW vehicles in the US. Volkswagen vehicles in Europe will continue to use the existing Smartcar integration.
* Car Net does not allow secondary driver accounts to authorize access to any third-party applications including Smartcar. Only the primary account holder can authorize access to any third-party applications.
* For Volkswagen vehicles in the US, 3 minutes is the average of how often the data is refreshed.


# Reliability
Source: https://smartcar.com/docs/help/reliability-and-freshness

When making requests to vehicles, there is variation in how often data is updated and how many requests it can process in a given period. The tables below indicate the performance for each of Smartcar supported brands in each region.

**Data Reliability**<br />
This ranking represents how reliably the vehicle or OEM processes data requests. A rank of 1 indicates the highest reliability.

**Command Reliability**<br />
This ranking measures the effectiveness with which the vehicle or OEM handles command requests. A score of 1 reflects the most reliable command execution. N/A means there is not enough data to provide a score.

***

## United States

| <div style={{ width:200 }}>Brand</div> | <div style={{ width:130 }}>Data Reliability</div> | <div style={{ width:140 }}>Command Reliability</div> |
| -------------------------------------- | ------------------------------------------------- | ---------------------------------------------------- |
| ACURA                                  | 1                                                 | 1                                                    |
| ALFA ROMEO                             | 1                                                 | 1                                                    |
| AUDI                                   | 1                                                 | 2                                                    |
| BMW                                    | 1                                                 | 2                                                    |
| BUICK                                  | 1                                                 | 1                                                    |
| CADILLAC                               | 1                                                 | 2                                                    |
| CHEVROLET                              | 1                                                 | 3                                                    |
| CHRYSLER                               | 1                                                 | 2                                                    |
| DODGE                                  | 1                                                 | 2                                                    |
| FIAT                                   | 1                                                 | N/A                                                  |
| FORD                                   | 1                                                 | 3                                                    |
| GMC                                    | 1                                                 | 2                                                    |
| HONDA                                  | 1                                                 | 2                                                    |
| HYUNDAI                                | 1                                                 | 2                                                    |
| INFINITI                               | 3                                                 | N/A                                                  |
| JAGUAR                                 | 1                                                 | 3                                                    |
| JEEP                                   | 1                                                 | 2                                                    |
| KIA                                    | 1                                                 | 3                                                    |
| LAND ROVER                             | 1                                                 | 3                                                    |
| LEXUS                                  | 1                                                 | 3                                                    |
| LINCOLN                                | 1                                                 | 3                                                    |
| MAZDA                                  | 1                                                 | 2                                                    |
| MERCEDES BENZ                          | 1                                                 | 1                                                    |
| MINI                                   | 1                                                 | 1                                                    |
| NISSAN                                 | 1                                                 | 2                                                    |
| PORSCHE                                | 1                                                 | 3                                                    |
| POLESTAR                               | 1                                                 | N/A                                                  |
| RAM                                    | 2                                                 | 1                                                    |
| RIVIAN                                 | 1                                                 | 1                                                    |
| TESLA                                  | 1                                                 | 1                                                    |
| TOYOTA                                 | 1                                                 | 3                                                    |
| VOLKSWAGEN                             | 1                                                 | 2                                                    |
| VOLVO                                  | 1                                                 | N/A                                                  |

## Canada

| <div style={{ width:200 }}>Brand</div> | <div style={{ width:130 }}>Data Reliability</div> | <div style={{ width:140 }}>Command Reliability</div> |
| -------------------------------------- | ------------------------------------------------- | ---------------------------------------------------- |
| ACURA                                  | 1                                                 | N/A                                                  |
| AUDI                                   | 1                                                 | 1                                                    |
| BMW                                    | 1                                                 | 1                                                    |
| BUICK                                  | 1                                                 | N/A                                                  |
| CADILLAC                               | 1                                                 | 2                                                    |
| CHEVROLET                              | 1                                                 | 2                                                    |
| DODGE                                  | 1                                                 | 1                                                    |
| FIAT                                   | 1                                                 | N/A                                                  |
| FORD                                   | 1                                                 | N/A                                                  |
| GMC                                    | 1                                                 | 1                                                    |
| HONDA                                  | 1                                                 | N/A                                                  |
| HYUNDAI                                | 2                                                 | 1                                                    |
| JAGUAR                                 | 1                                                 | 3                                                    |
| JEEP                                   | 1                                                 | 3                                                    |
| KIA                                    | 1                                                 | 1                                                    |
| LEXUS                                  | 1                                                 | 3                                                    |
| MINI                                   | 2                                                 | 1                                                    |
| RAM                                    | 1                                                 | 1                                                    |
| TESLA                                  | 1                                                 | 1                                                    |
| TOYOTA                                 | 1                                                 | 3                                                    |
| VOLVO                                  | 1                                                 | N/A                                                  |

## Europe

| <div style={{ width:200 }}>Brand</div> | <div style={{ width:130 }}>Data Reliability</div> | <div style={{ width:140 }}>Command Reliability</div> |
| -------------------------------------- | ------------------------------------------------- | ---------------------------------------------------- |
| ALFA ROMEO                             | 1                                                 | N/A                                                  |
| AUDI                                   | 1                                                 | 1                                                    |
| BMW                                    | 1                                                 | 1                                                    |
| BYD                                    | 1                                                 | N/A                                                  |
| CITROEN                                | 1                                                 | 1                                                    |
| CUPRA                                  | 1                                                 | 1                                                    |
| DACIA                                  | 1                                                 | 1                                                    |
| DS                                     | 1                                                 | N/A                                                  |
| FIAT                                   | 1                                                 | 1                                                    |
| FORD                                   | 2                                                 | 3                                                    |
| HYUNDAI                                | 1                                                 | 2                                                    |
| JAGUAR                                 | 1                                                 | 3                                                    |
| JEEP                                   | 1                                                 | N/A                                                  |
| KIA                                    | 1                                                 | 1                                                    |
| LAND ROVER                             | 1                                                 | N/A                                                  |
| MAZDA                                  | 1                                                 | 1                                                    |
| MERCEDES BENZ                          | 1                                                 | 1                                                    |
| MG                                     | 1                                                 | 1                                                    |
| MINI                                   | 1                                                 | 1                                                    |
| NISSAN                                 | 1                                                 | 3                                                    |
| OPEL                                   | 1                                                 | 1                                                    |
| PEUGEOT                                | 1                                                 | 1                                                    |
| PORSCHE                                | 1                                                 | 3                                                    |
| POLESTAR                               | 1                                                 | N/A                                                  |
| RENAULT                                | 1                                                 | 1                                                    |
| SKODA                                  | 1                                                 | 1                                                    |
| TESLA                                  | 1                                                 | 2                                                    |
| VAUXHALL                               | 1                                                 | N/A                                                  |
| VOLKSWAGEN                             | 1                                                 | 2                                                    |
| VOLVO                                  | 1                                                 | 1                                                    |

Last Updated: November 12, 2025


# Join the Research Fleet
Source: https://smartcar.com/docs/help/research-fleet



Smartcar is the easiest way to integrate apps with cars, funded by [a16z](https://a16z.com/), [NEA](https://www.nea.com/) and [Energize Capital](https://www.energizecap.com/).\
We enable companies like [Uber](https://smartcar.com/blog/uber), [Lyft](https://smartcar.com/blog/lyft), [Emulate](https://smartcar.com/blog/emulate), [Bluewave](https://smartcar.com/blog/bluwave-ai), [Neowatt](https://smartcar.com/blog/revenue-for-energy-retailers), and [more](https://smartcar.com/customers) to monitor a car's battery state of charge, verify mileage, manage EV charging, and much more.

We are always expanding to new makes and models of cars and we'd love your help!

## What are we asking for?

Building and maintaining our APIs is a complex endeavor. Smartcar operates a research fleet of vehicles across brands, models, and geographies to ensure we can provide the best product possible. **This is where you come in**. We'd like your help with understanding real-world vehicle behaviors with your car and improve the quality of our platform. Understanding things like:

* Does your car’s odometer update in real-time?
* What's the amount of fuel/battery your car has remaining?
* What data and remote actions are available for your specific car's brand, model, year?

## Perks of being part of the Research Fleet

* 💰 You will receive \$250 for the 6 months that your car is part of the fleet
* 🧥 Smartcar swag
* 🙋 Assistance setting up your car's connected services

## Sign up

<iframe src="https://form.typeform.com/to/a8XPIn9W?utm_source=docs.smartcar.com&utm_medium=form-embed&utm_campaign=research-fleet" width="700" height="700" allow="fullscreen" />

## FAQs

<AccordionGroup>
  <Accordion title="How and when will I get paid?">
    The Smartcar team will schedule a check to be sent to your preferred address if your car is verified to be eligible for the Smartcar Research Fleet.
  </Accordion>

  <Accordion title="What exactly will Smartcar do with my car?">
    Smartcar will use your vehicle to retrieve and verify key data points such as your odometer and fuel tank/battery level. The team will inform you of all data and actions they will retrieve from your vehicle and the schedule at which they will be performing the verification. No action will be perfomed remotely without your permission.
  </Accordion>

  <Accordion title="How can I opt-out of the program?">
    You may opt-out at any point without any explanation. We simply ask that you give us a heads up that you no longer wish to participate by reaching out to [support@smartcar.com](mailto:support@smartcar.com).
  </Accordion>
</AccordionGroup>


# Vehicle Simulator
Source: https://smartcar.com/docs/help/vehicle-simulator

Learn about what to expect from Vehicle Simulator and how it compares to Live mode.

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


# What is a Connected Car?
Source: https://smartcar.com/docs/help/what-is-a-connected-car

Learn about how to build applications that connect to millions of vehicles around the world.

Connected cars are vehicles that have in-built cellular modems. Most vehicles manufactured after 2015 have been shipping with this connectivity, or "embedded telematics." This essentially makes cars "smart" allowing them to communicate with the Internet. Take a look at this blog post for an in depth primer.


# What is Smartcar?
Source: https://smartcar.com/docs/help/what-is-smartcar

Learn about how to build applications that connect to millions of vehicles around the world.

The Smartcar platform allows mobility businesses to easily connect with their customers’ cars. Whether you need to track a vehicle’s location,
verify its mileage, share a virtual key, start charging an EV, monitor a car’s fuel tank level, inspect the tire pressure, or check the engine
oil life, Smartcar lets you do so with a single API request.

Take a look at the video below for a quick overview of how Smartcar works.

<Frame type="simple">
  <iframe width="800" height="450" src="https://www.youtube.com/embed/P-7CP70r-8U" />
</Frame>


# Callback URI Verification
Source: https://smartcar.com/docs/integrations/webhooks/callback-verification

Verify your newly-created webhook.

<Info>
  This page covers the verification step **when first setting up a webhook** on Dashboard. Please see our [payload verification](/integrations/webhooks/payload-verification) section for information on how to verify webhook payloads from vehicles.
</Info>

When you first set up a webhook in the Smartcar Dashboard, Smartcar will post a challenge request to ensure we're sending payloads to the correct place. This is a **one time** event and will be in the following format:

<CodeGroup>
  ```json Version 4.0 (NEW) theme={null}
  {
    "eventId": "52f6e0bb-1369-45da-a61c-9e67d092d6db",
    "eventType": "VERIFY",
    "data": {
      "challenge": "<random-string>"
    },
    "meta": {
      "version": "4.0",
      "webhookId": "5a8e5e38-1e12-4011-a36d-56f120053f9e",
      "webhookName": "Example Webhook",
      "deliveryId": "5d569643-3a47-4cd1-a3ec-db5fc1f6f03b",
      "deliveredAt": "2025-07-31T19:38:42.332Z"
    }
  }
  ```

  ```json Version 2.0 theme={null}
  {
    "version": "2.0",
    "webhookId": "<uuid>",
    "eventName": "verify",
    "payload": { 
      "challenge": "<random-string>" 
    }
  }
  ```
</CodeGroup>

Upon receiving the request, your server will need respond to the challenge by hashing `payload.challenge` with your `application_management_token` to create a `SHA-256` based `HMAC`.

<Tip>
  Our [backend SDKs](/api-reference/api-sdks) have helper methods to generate the `HMAC`.
</Tip>

<CodeGroup>
  ```python Python theme={null}
      hmac = smartcar.hash_challenge(
              application_management_token, 
              payload.challenge
          )
  ```

  ```js Node theme={null}
      let hmac = smartcar.hashChallenge(
          application_management_token, 
          payload.challenge
      ); 
  ```

  ```java Java theme={null}
  String hmac =  Smartcar.hashChallenge(
              application_management_token, 
              payload.challenge
          );
  ```

  ```ruby Ruby theme={null}
      hmac = Smartcar.hash_challenge(
          application_management_token, 
          payload.challenge
      )
  ```
</CodeGroup>

Return the hex-encoded hash as the value for `challenge` in your response body with a `200` status code, and the `Content-Type` header set to `application/json`.

```json verificationResponse.body theme={null}
{
  "challenge" : "{HMAC}"
}
```

## Verify webhook challenges inside the Dashboard

Use the Smartcar Dashboard to understand exactly what Smartcar expects before you enable webhooks in production. The **Verify webhook** modal shows a sample challenge string plus language-specific snippets so you can implement the same HMAC signature in your code.

<Frame>
    <img src="https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge.png?fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=9106c3a746b703281d6fc2ada9bd6249" alt="" data-og-width="1344" width="1344" data-og-height="1095" height="1095" data-path="images/changelog/webhook-challenge.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge.png?w=280&fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=2af7016d356c723b2c5f2abf8f55e130 280w, https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge.png?w=560&fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=c402b715adfe634727c3db3777518002 560w, https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge.png?w=840&fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=663b8794492a757bc94bb456642ba025 840w, https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge.png?w=1100&fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=c94a590072ee00fe31f2381424ab4866 1100w, https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge.png?w=1650&fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=c36a0f87b244b4a1915d30d9440724c0 1650w, https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge.png?w=2500&fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=f4870c0fed07dab78526f68c81bd989a 2500w" />
</Frame>

<Steps>
  <Step title="Implement the signature in your handler">
    Copy the challenge string from the modal and use the embedded snippets (Python, Node, Java, or Ruby) as references while you code the signature logic on your server. Run your handler locally or in staging so it is ready to answer Smartcar’s challenge.
  </Step>

  <Step title="Trigger Smartcar’s verification call">
    Once your server is ready, click **Verify this webhook**. Smartcar sends the challenge payload to your callback URL, and your code responds with the signature it just produced.
  </Step>

  <Step title="Compare expected vs actual responses">
    The Response tab displays the HTTP status, the challenge Smartcar sent, the signature Smartcar expected, and the body your server returned. Use this side-by-side view to confirm success or adjust your implementation before retrying.
  </Step>
</Steps>

<Frame>
    <img src="https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge-calculator.png?fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=12cd5091ce9d0c9f0355569227931374" alt="" data-og-width="1344" width="1344" data-og-height="1095" height="1095" data-path="images/changelog/webhook-challenge-calculator.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge-calculator.png?w=280&fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=01c41a08770277ac722cf56d2207755d 280w, https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge-calculator.png?w=560&fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=eb0f7b5c79d5f1d5001cf2b4e0c1fc94 560w, https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge-calculator.png?w=840&fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=e6a0dedfdd279d20479326bcd0f855e2 840w, https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge-calculator.png?w=1100&fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=a8fe313d141c595525270f50f960da76 1100w, https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge-calculator.png?w=1650&fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=b671a190797c06c85e5fea49b0dab359 1650w, https://mintcdn.com/smartcar-docs/92ufkjISfFm8Rd1q/images/changelog/webhook-challenge-calculator.png?w=2500&fit=max&auto=format&n=92ufkjISfFm8Rd1q&q=85&s=bc0b603ce9b29e082e1c5372681297e3 2500w" />
</Frame>


# Webhooks Setup
Source: https://smartcar.com/docs/integrations/webhooks/overview

Receive a seamless data stream from your vehicles via webhooks with optimized vehicle updates, ensuring you always have the most current information available for all of your vehicles.

Integrating with Smartcar is now easier than ever. We've combined all previous version of webhooks into a much more powerful single webhook offering to get your integration up and running quickly.

<Info>
  Webhooks are the recommended way to receive real-time vehicle data from Smartcar. You can still use the REST API for retrieving data and issuing commands, but webhooks are the most scalable and reliable option for most use cases.
</Info>

## Quick Start Options

### Option 1: Use Our Webhook Receiver Recipe (Recommended)

Deploy a production-ready webhook receiver to AWS in minutes using our [Webhook Receiver Recipe →](/getting-started/tutorials/webhook-receiver-recipe).

This easy to deploy recipe is a complete AWS serverless webhook receiver with built-in validation, error handling, and scalability.

### Option 2: Build From Scratch

Follow our step-by-step guide to build your own webhook receiver.

**Perfect for**: Custom architectures, learning webhook concepts, non-AWS deployments

[Continue with manual setup ↓](#configuring-a-webhook-integration)

***

## Webhook Recipes & Templates

To help you get started quickly, we provide production-ready webhook receiver templates:

### Webhook Receiver Recipe

A complete AWS serverless webhook receiver with built-in validation, error handling, and scalability.

* **Best for**: New implementations, AWS environments, TypeScript projects
* **Deployment**: AWS Lambda + API Gateway + SQS
* **Repository**: [smartcar/typescript-webhook-recipe](https://github.com/smartcar/typescript-webhook-recipe)
* **Documentation**: [Webhook Receiver Recipe →](/getting-started/tutorials/webhook-receiver-recipe)

*More recipes coming soon for Python, Go, and other cloud platforms.*

***

## Configuring a Webhook Integration

Head over to the [Smartcar Dashboard](https://dashboard.smartcar.com/integrations) to set up your webhook integration. There are three main steps to set up a webhook in Smartcar:

<Frame type="simple" caption="Integrations in Smartcar Dashboard">
  <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/getting-started/integration.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=d3af48b5bc08ad44ee8570b8687ddb8d" alt="Application Configuration in Smartcar Dashboard" data-og-width="3420" width="3420" data-og-height="2080" height="2080" data-path="images/getting-started/integration.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/getting-started/integration.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=3c570d45ab5e11c646ae694f07f4782e 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/getting-started/integration.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=4385dc02cfe9a0f737a08afa6cb1a248 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/getting-started/integration.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=3c0d60e6c8328c7c511070c8491eab7e 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/getting-started/integration.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=95eecd2c084428179e4acfae1040f730 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/getting-started/integration.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=1e5d939db4bba88fa2af6c391bf3729a 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/getting-started/integration.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=3b99e85bc4f6c2b4b1159c28d2a7779b 2500w" />
</Frame>

<Steps>
  <Step title="Select an Integration Type">
    From the integrations page, start by creating a new integration and choosing webhook. For most use cases, Webhooks are the recommended option.
  </Step>

  <Step title="Choose a Trigger">
    Define <b>when</b> Smartcar should send you a webhook. This is the vehicle event or condition that causes data to be delivered.

    <br />

    <b>Example triggers:</b>

    <ul>
      <li>Vehicle's battery percentage changes</li>
      <li>Vehicle is plugged in or unplugged</li>
      <li>Airbags deploy</li>
      <li>Odometer changes as the vehicle drives</li>
      <li>Doors or windows open</li>
      <li>Vehicle location changes as it drives</li>
    </ul>
  </Step>

  <Step title="Select the Data (Signals)">
    After choosing a trigger, specify <b>what</b> vehicle data ("signals") should be included in the webhook payload.<br />
    Your selection directly maps to the permissions that the vehicle owner granted your application during the connection process. Smartcar offers over 20 specific <a href="https://smartcar.com/docs/api-reference/permissions">permissions</a> for granular control.
  </Step>

  <Step title="Provide a callback URI & verify your webhook">
    Enter the destination URL where Smartcar should send the data. This should be your application's endpoint to receive webhook payloads.

    Read more about [verifying your webhook](/integrations/webhooks/callback-verification) or use our [Webhook Receiver Recipe](/getting-started/tutorials/webhook-receiver-recipe) for an out-of-the box solution.

    Read more about [receiving webhooks.](/integrations/webhooks/webhook-receiver)

    Your callback URI should handle the `"eventType" : "VERIFY"` received in the request payload and respond with a `200` status code and a `{"challenge": "{HMAC}"}`. Please see [this guide](/integrations/webhooks/callback-verification) on how to
    verify your callback URI.
  </Step>
</Steps>

## Subscribing Vehicles to a Webhook

Once the user grants access to your application, you can chose between automatically subscribing all vehicles to your webhook or by manually subscribing specific vehicles.

Automatically subscribing vehicles can be done by selecting the option in the Dashboard when creating your webhook. When this option is selected, all vehicles that are connected to your application will be automatically subscribed to your webhook. New connections will also be automatically subscribed and start sending data right away.

If you do not select the option to autosubscribe vehicles, you may also manually subscribe vehicles to webhoooks by issuing requests to the [subscribe](/api-reference/webhooks/subscribe-webhook) and [unsubscribe](/api-reference/webhooks/unsubscribe-webhook) with the corresponding
webhook ID or from the Smartcar Dashboard.

<Frame type="simple" caption="Webhook Subscription in Smartcar Dashboard">
  <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/getting-started/dashboard/subscribe-from-dashboard.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=0df1e27487ad5b8116a99e2dd3f80b5c" alt="Webhook Subscription in Smartcar Dashboard" data-og-width="3972" width="3972" data-og-height="1932" height="1932" data-path="images/getting-started/dashboard/subscribe-from-dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/getting-started/dashboard/subscribe-from-dashboard.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=c7ebca922726f37bef95869e227f2c3a 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/getting-started/dashboard/subscribe-from-dashboard.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=5a4ff5c39f80690cd8f50f23ab53117b 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/getting-started/dashboard/subscribe-from-dashboard.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=dac53494978cba5d47ed149813c952f9 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/getting-started/dashboard/subscribe-from-dashboard.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=5e7d7cd58f719877acb1e8778e02a48a 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/getting-started/dashboard/subscribe-from-dashboard.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=fcdf42ce2444e6d8afcdd5223bb93488 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/getting-started/dashboard/subscribe-from-dashboard.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=6687ae24a2eda0e30025de3dcc867301 2500w" />
</Frame>

In both scenarios, data will be sent only after your webhook has been verified.

When a vehicle is first subscribed to a webhook, Smartcar will send an initial
payload that attempts to get all the signals you're subscribed to for that vehicle.

Smartcar will only send subsequent data when it matches the conditions specified in your webhook creation steps. For example, when any of the signals you specified change in value.

<Info>
  The first payload may only contain partial data if there were issues
  retrieving data from the vehicle initially. Connection or compatibility
  issues will be reported to your error callback URI as described below.
</Info>

## FAQS

<AccordionGroup>
  <Accordion title="What data can I access from a vehicle?">
    All the data you'd expect from vehicles through the Smartcar API - standardized and accessible through Webhooks. Please refer to the list of supported [signals](/api-reference/signals/schema) for specific data points and signal names.
  </Accordion>

  <Accordion title="What does the webhook payload look like">
    Please refer to these [responses](/integrations/webhooks/responses) for success and errors.
  </Accordion>

  <Accordion title="How often will I get data?">
    Data update frequency will depend on the brand. Exact frequencies for each brand can be found
    [here](/help/frequencies). Please note that Smartcar will only send data if it has
    changed.
  </Accordion>

  <Accordion title="Will I be billed for using webhooks during beta?">
    During beta, developers will not be billed for using these webhooks.
  </Accordion>

  <Accordion title="How do I know if a vehicle supports a signal?">
    Please refer to [Vehicle compatibility issues](/integrations/webhooks/responses#vehicle-connection-or-compatibility-issues).
  </Accordion>

  <Accordion title="Do I need a different URL for errors?">
    No. You may use the same callback URI for both errors and data. In
    order to distinguish between the types of payloads, please refer to the
    `type` field.
  </Accordion>

  <Accordion title="Are Webhooks available on all plans?">
    Yes. As of Summer of 2025, Smartcar now makes Webhooks available on all plans for ease of integration. Read more about it [here](https://smartcar.com/docs/changelog/latest#august-26th%2C-2025)
  </Accordion>
</AccordionGroup>

***

Ready to get started? Check out our [Getting Started guides](/getting-started/) or [tutorials](/getting-started/tutorials/) to connect your first vehicle and set up your integration.


# Payload Verification
Source: https://smartcar.com/docs/integrations/webhooks/payload-verification

Verify webhook payloads from vehicles to ensure data integrity and security.

<Info>
  This page covers verification of payloads from vehicles.
  Please see our [callback verification](/integrations/webhooks/callback-verification) section for
  information on how to initially verify your callback uri.
</Info>

Verify webhook payloads against the `SC-Signature` header and a `SHA-256` based `HMAC` generated by hashing
your `application_management_token` and the body.

<Tip>
  Our [backend SDKs](/api-reference/api-sdks) have helper methods that return `true` if the payload is good.
</Tip>

<CodeGroup>
  ```python Python theme={null}
      Smartcar.verify_payload(
          {application_management_token},
          {SC-Signature}, 
          {webhook_body}
      )
  ```

  ```js Node theme={null}
      smartcar.verifyPayload(
          {application_management_token},
          {SC-Signature}, 
          {webhook_body}
      );
  ```

  ```java Java theme={null}
      Smartcar.verifyPayload(
          {application_management_token},
          {SC-Signature}, 
          {webhook_body}
      );
  ```

  ```ruby Ruby theme={null}
      Smartcar.verify_payload(
          {application_management_token},
          {SC-Signature}, 
          {webhook_body}
      )
  ```
</CodeGroup>


# Webhook Response Payloads
Source: https://smartcar.com/docs/integrations/webhooks/responses

Receive a seamless data stream from your vehicles via webhooks with optimized vehicle updates, ensuring you always have the most current information available for all of your vehicles.

## Vehicle State

When a vehicle is first subscribed to a webhook, Smartcar will send an initial payload that attempts to get all the signals you're subscribed to for that vehicle with a `VEHICLE_STATE` type. Subsequent events will contain a payload with the same event type but only the relevant signals based on your webhook configuration. (i.e, when a signal changes, on a schedule, etc.)

Vehicle state payloads will contain the following object types for the `triggers` array:

* `SIGNAL_UPDATED`: indicates that a signal value has changed since the last payload was sent. The `signal` object will contain the `code` of the signal that was updated.
* `FIRST_DELIVERY`: indicates that this is the first payload sent for this vehicle. This trigger will only be present in the initial payload sent when a vehicle is first subscribed to a webhook, unsubscribed and then resubscribed to your webhook, or if your application is not responding with a 200 status code, we will attempt to deliver this webhook again.

If you request a signal as part of your webhook payload data that the vehicle is not capable of, Smartcar will still include it in the `VEHICLE_STATE` payload, but the signal will contain an error object instead of data as shown in the example below.

```json  theme={null}
{
    "eventId": "5a537912-9ad3-424b-ba33-65a1704567e9",
    "eventType": "VEHICLE_STATE",
    "data": {
        "user": {
            "id": "93b3ea96-ca37-43a9-9073-f4334712dbc7"
        },
        "vehicle": {
            "id": "123e4567-e89b-12d3-a456-426614174000",
            "make": "Test Make",
            "model": "Test Model",
            "year": 2020
        },
        "signals": [
            {
                "code": "location-preciselocation",
                "name": "PreciseLocation",
                "group": "Location",
                "body": {
                    "latitude": 37.7749,
                    "longitude": -122.4194
                },
                "status": {
                  "value": "SUCCESS"
                },
                "meta": {
                  "retrievedAt": 1758668712404,
                  "oemUpdatedAt": 1758668712404
                }
            },
            {
              "code": "location-isathome",
              "name": "IsAtHome",
              "group": "Location",
              "status": {
                "error": {
                  "code": "VEHICLE_NOT_CAPABLE",
                  "type": "COMPATIBILITY"
                },
                "value": "ERROR"
              }
            },
            {
                "code": "tractionbattery-stateofcharge",
                "name": "StateOfCharge",
                "group": "TractionBattery",
                "body": {
                    "unit": "percent",
                    "value": 75
                },
                "status": {
                  "value": "SUCCESS"
                },
                "meta": {
                  "retrievedAt": 1758668712404,
                  "oemUpdatedAt": 1758668712404
                }
            }
        ]
    },
    "triggers": [
        {
            "type": "SIGNAL_UPDATED",
            "signal": {
                "name": "StateOfCharge",
                "group": "TractionBattery",
                "code": "tractionbattery-stateofcharge"
            }
        }
    ],
    "meta": {
        "version": "4.0",
        "deliveryId": "48b25f8f-9fea-42e1-9085-81043682cbb8",
        "deliveredAt": 1761896351529,
        "webhookId": "123e4567-e89b-12d3-a456-426614174000",
        "webhookName": "My First Webhook",
        "signalCount": 3,
        "mode": "LIVE"
    }
}
```

For each signal, you will have a `meta` object that contains the following fields:

* `retrievedAt`: The timestamp (in milliseconds since epoch) of when the data was retrieved from the vehicle by Smartcar.
* `oemUpdatedAt`: The timestamp (in milliseconds since epoch) of when the data was last recorder by the vehicle.

You'll also see a `code` with the unique signal code that can be used to retrieve that signal from the API by calling the [`GET` Signal endpoint](/api-reference/get-signal).
The `name` and `group` fields correspond to the signal's name and group respectively as defined in the [Signal Schema](/api-reference/signals/schema).

## Vehicle connection or compatibility issues

There may be times when Smartcar is unable to get vehicle data because there is
an issue with our connection to the vehicle that requires vehicle owner
interaction, or because the subscribed vehicle does not support some of the signals you have configured.

Smartcar will allow you to subscribe any vehicle to your webhook. When processing
the initial payload, we will report compatibility issues to your error callback
URI. For example, if a vehicle is not capable of the `nickname` signal we would
send data for other signals as normal, but send the following payload for the `nickname` signal instead.

When either of these happens, we'll send a `VEHICLE_ERROR` payload to your vehicle error callback URI. If you don't specify a callback URI for errors, Smartcar will send them to the same vehicle data callback URI.

For a list of possible errors, please refer to the [API Errors](/errors/api-errors) section.

```json  theme={null}
{
    "eventId": "5a537912-9ad3-424b-ba33-65a1704567e9",
    "eventType": "VEHICLE_ERROR",
    "data": {
        "user": {
            "id": "93b3ea96-ca37-43a9-9073-f4334719iok7"
        },
        "errors": [
            {
                "type": "COMPATIBILITY",
                "code": "VEHICLE_NOT_CAPABLE",
                "state": "ERROR",
                "description": "The vehicle is incapable of performing your request.",
                "suggestedUserMessage": "Your car is unable to perform this request.",
                "docURL": "https://smartcar.com/docs/errors/api-errors/compatibility-errors#vehicle-not-capable",
                "resolution": {
                    "type": "CONTACT_SUPPORT"
                },
                "signals": [
                  {
                    "code": "location-preciselocation",
                    "name": "PreciseLocation",
                    "group": "Location"
                  },
                  {
                    "code": "tractionbattery-stateofcharge",
                    "name": "StateOfCharge",
                    "group": "TractionBattery"
                  }
                ]
            }
        ],
        "vehicle": {
            "id": "123e4567-e89b-12d3-a456-426614174000",
            "make": "TESLA",
            "model": "Model 3",
            "year": 2020
        }
    },
    "meta": {
        "version": "4.0",
        "deliveryId": "48b25f8f-9fea-42e1-9085-81043682cbb8",
        "deliveredAt": 1761896351529,
        "webhookId": "123e4567-e89b-12d3-a456-426614174000",
        "webhookName": "Bad Webhook",
        "mode": "LIVE"
    }
}
```

While a vehicle is in one of these states, you may be unable to receive data from the
vehicle until the owner has taken the necessary steps to re-establish
the connection.

Upon resolution of the issue, Smartcar will send another payload to your error callback URI with `state`
set to `RESOLVED`. If you don't specify a callback URI for errors, Smartcar will send them to the same vehicle data callback URI.


# Building a Webhook Receiver
Source: https://smartcar.com/docs/integrations/webhooks/webhook-receiver

Webhook payloads are sent from Smartcar to your receiving server. Your receiver must respond properly to ensure payloads are delivered without delay.

<Info>
  **Looking for a quick start?** Our [Webhook Receiver Recipe](/getting-started/tutorials/webhook-receiver-recipe) provides a production-ready AWS serverless webhook receiver that you can deploy in minutes. Perfect for new implementations!
</Info>

## How Webhooks are Sent

Webhook payloads are sent as HTTP requests to the `Vehicle data callback URI` you defined when you set up the webhook.

The HTTP request body consists of a JSON payload. Webhook payloads will be one of `VEHICLE_STATE` or `VEHICLE_ERROR` as defined in [Response Payloads](/integrations/webhooks/responses).

Optionally, you may configure a separate `Vehicle error callback URI` for `VEHICLE_ERROR` payloads. If this is not defined, all payloads will be sent to the primary URI.

## Verifying Your Receiver Endpoint

Before you can receive vehicle data, Smartcar will send a verification payload to your `Vehicle data callback URI` to validate that your receiver is reachable and responding appropriately.

Please see [Callback URI Verification](/integrations/webhooks/callback-verification) for details on how to correctly respond to this request.

## Responding to Webhook Deliveries

Smartcar expects your webhook receiver to return an HTTP `200` response within 15 seconds of each delivery. Any other status code, or responses that exceed this 15-second timeout, are treated as errors and the delivery will be marked unsuccessful.

Smartcar will attempt to re-deliver unsuccessful requests up to three times, with exponential backoff. If a timely `200` response code is not received for all attempts, the payload is dropped. Future deliveries will still be attempted as long as the webhook is active.

<Info>
  As a best practice, you should decouple webhook receiving and payload processing. If your receiver does not respond because of a processing issue, Smartcar will consider the payload undelivered and will send it again. Persist the payload first, then run any signal processing logic as a separate step.
</Info>

## Verifying Payloads

We recommend that you verify the payloads you receive to ensure they are legitimate and complete. Smartcar cryptographically signs each payload using a signature that can only be decoded with your Application Management Token. See [Payload verification](/integrations/webhooks/payload-verification) for details.

## Networking Considerations

* Webhook receivers must be accessible from the public internet so Smartcar can resolve your receiver URI.
* Receiver URIs must use HTTPS with a valid SSL certificate.
* Internal corporate network addresses or custom SSL certificates are not supported.
* Smartcar sends webhook payloads from public IPv4 addresses, which may change over time. Be careful when defining firewall rules.

## Webhook Best Practices

<AccordionGroup>
  <Accordion title="1. Decouple Receiving from Processing">
    The recipe uses SQS to separate webhook receipt from processing. This ensures:

    * Fast response times (\< 200ms) from your server to Smartcar
    * No timeouts from long-running business logic
    * Reliable delivery even during processing failures
  </Accordion>

  <Accordion title="2. Validate Webhook Signatures">
    Every webhook is cryptographically verified using HMAC-SHA256:

    * Confirms payloads come from Smartcar
    * Prevents replay attacks and tampering
    * Rejects invalid requests before processing
  </Accordion>

  <Accordion title="3. Implement Retry Logic">
    Built-in retry mechanisms handle transient failures:

    * Automatic retries for failed processing (up to 3 times)
    * 30-second visibility timeout between retries
    * Dead letter queue for manual investigation of persistent failures
  </Accordion>

  <Accordion title="4. Return 200 Quickly">
    The receiver lambda responds within milliseconds:

    * Acknowledges receipt immediately
    * Prevents Smartcar from retrying unnecessarily
    * Queues payload for asynchronous processing
  </Accordion>

  <Accordion title="5. Monitor and Alert">
    CloudWatch integration provides observability:

    * Track delivery success rates
    * Monitor queue depths and processing times
    * Alert on error rate thresholds
    * Debug issues with comprehensive logging
  </Accordion>

  <Accordion title="6. Scale Automatically">
    Serverless architecture handles traffic variability:

    * Lambda auto-scales with webhook volume
    * No capacity planning required
    * Pay only for actual usage
    * Handles traffic spikes seamlessly
  </Accordion>

  <Accordion title="7. Secure with Least Privilege">
    IAM policies enforce security best practices:

    * Each Lambda has minimal required permissions
    * No hardcoded credentials
    * AWS manages encryption at rest and in transit
    * Secrets stored securely in AWS Secrets Manager
  </Accordion>
</AccordionGroup>

## Recommended Webhook Receiver Pattern

This pattern is provides a complete serverless webhook receiver infrastructure on AWS. The diagram below shows the data flow from Smartcar webhooks through your deployment:

```mermaid  theme={null}
graph TD
    A[Smartcar Webhooks] -->|HTTPS POST| B[API Gateway]
    B --> C[Receiver Serverless Function]
    C -->|Validate & Queue| D[Queue]
    D --> E[Processor Serverless Function]
    E -->|Process Signals| F[Your Business Logic]
    E -->|Failed Processing| G[Dead Letter Queue]
    G --> H[Manual Review/Retry]
    
    style A fill:#FFB84D,stroke:#E69500,stroke-width:2px,color:#000
    style B fill:#FF9900,stroke:#CC7A00,stroke-width:2px,color:#000
    style C fill:#FF9900,stroke:#CC7A00,stroke-width:2px,color:#000
    style D fill:#FF9900,stroke:#CC7A00,stroke-width:2px,color:#000
    style E fill:#FF9900,stroke:#CC7A00,stroke-width:2px,color:#000
    style F fill:#d3d3d3,stroke:#666,stroke-width:2px,color:#000
    style G fill:#FF9900,stroke:#CC7A00,stroke-width:2px,color:#000
    style H fill:#d3d3d3,stroke:#666,stroke-width:2px,color:#000
```

<Note>
  **Orange components** are provided by the recipe and deployed automatically. **Gray components** represent external systems where your custom business logic would live.
</Note>


