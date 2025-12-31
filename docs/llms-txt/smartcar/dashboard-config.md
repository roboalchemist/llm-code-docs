# Source: https://smartcar.com/docs/connect/dashboard-config.md

# Dashboard Configuration

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
