# Source: https://smartcar.com/docs/api-reference/permissions.md

# Permissions

> In order to use an endpoint or webhook, you'll need to request the associated permissions from your user in [Connect](/docs/connect/what-is-connect).

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
