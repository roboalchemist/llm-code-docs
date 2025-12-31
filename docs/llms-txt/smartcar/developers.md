# Source: https://smartcar.com/docs/help/oem-integrations/tesla/developers.md

# Tesla Permission Info

> This page has information regarding Smartcar's upgraded Tesla integration.

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
