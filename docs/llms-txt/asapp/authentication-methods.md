# Source: https://docs.asapp.com/generativeagent/configuring/connect-apis/authentication-methods.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Authentication Methods

> Learn how to configure Authentication methods for API connections.

APIs require authentication to control access to their endpoints. GenerativeAgent's API connections support the following authentication methods:

* Basic Authentication (username/password)
* Custom Header Authentication (API keys)
* OAuth 2.0 (Authorization Code and Client Credentials flows)

If your APIs require an authentication flow that is not supported by the default authentication methods, we can create a [custom authentication method](#custom-authentication-methods) for you.

## Create an Authentication Method

To Create an Authentication Method:

<Steps>
  <Step title="Navigate to API Integration Hub > Authentication Methods">
    <Note> You may also create an Authentication Method when specifying the API Connection's API Source.</Note>
  </Step>

  <Step title="Click 'Create Authentication Method'" />

  <Step title="Configure the Authentication Method">
    * Provide a name and description
    * Select the Authentication Type matching your API's requirements
    * Configure the type-specific settings detailed in sections below
    * Save the Authentication Method
  </Step>

  <Step title="Add to API Connection">
    In the API Connection's API Source tab, select this Authentication Method for Sandbox or Production environments.
  </Step>
</Steps>

## Basic Authentication

[Basic authentication](https://en.wikipedia.org/wiki/Basic_access_authentication) requires:

* Username
* Password

## Custom Header

Custom headers add authentication data to API requests via HTTP headers. Common implementations include API keys and bearer tokens.

To configure a custom header, you need to:

1. Optionally enable client authentication:
   * Enable if you need to reference values from the client in a header.
   * Set the client data validity duration.
   * Reference client data using `{Auth.*}`
2. Header configuration:
   * Header Name (e.g., "Authorization", "X-API-Key")
   * Header Value (static value or dynamic client data)
     * e.g. `{Auth.client_token}`

## OAuth

OAuth 2.0 provides delegated authorization flows. GenerativeAgent supports:

<Tabs>
  <Tab title="Authorization Code">
    Required configuration:

    * Authorization Code reference

      This is the location within the [client data](#client-authentication-data) that contains the authorization code.

      `{Auth.authorization_code}`
    * Client ID
    * Client secret
    * Token Request URL
    * Redirect URI

      You can use a variable from the client data for the redirect URI. `{Auth.redirect_uri}`
    * How the client authentication data is passed
      * Basic Auth, or
      * Request Body
    * One or more headers to be added to the request.
      * Header Name
      * Header Value

        Use `{OAuth.access_token}` for the generated access token.

        You can also reference the client data in the header values, using the variable: `{Auth.[auth_data_key]}`.
  </Tab>

  <Tab title="Client Credentials">
    Required configuration:

    * Client ID
    * Client secret
    * Token Request URL
    * How the client authentication data is passed
      * Basic Auth, or
      * Request Body
    * One or more headers to be added to the request.
      * Header Name
      * Header Value

        Use `{OAuth.access_token}` for the generated access token.

        You can also reference the client data in the header values, using the variable: `{Auth.[auth_data_key]}`.
  </Tab>
</Tabs>

## Client Authentication Data

Some authentication flows require dynamic data from the client:

* OAuth authorization codes
* User-specific API keys
* Custom tokens

You provide client authentication data through:

<Tabs>
  <Tab title="Standalone GenerativeAgent">
    If you are using GenerativeAgent independently of ASAPP Messaging, this Auth data is passed via the [`/authenticate`](/apis/conversations/authenticate-a-user-in-a-conversation) endpoint.
  </Tab>

  <Tab title="ASAPP Messaging">
    If you are using GenerativeAgent as part of ASAPP Messaging, this Auth data is passed via the [SDKs](/agent-desk/integrations) depending on the chat channel you are using.
  </Tab>
</Tabs>

### Client Authentication Session

Any authentication method that requires client data will store the auth data for the session.

If the underlying API returns a `401`, the system will require new client authentication data for the session. GenerativeAgent communicates this in the event stream as an [`authenticationRequested`](/generativeagent/integrate/handling-events#user-authentication-required) event.

## Custom Authentication Methods

If your API requires an authentication flow not supported by our default methods, we can work with you to create a custom solution.

Contact your ASAPP account team to discuss your custom authentication requirements. We'll work with you to build and implement the solution.

### Using Custom Authentication Methods

Custom authentication methods work the same way as standard methods:

* They appear in your authentication method list
* You can select them when configuring API connections
* They support both sandbox and production environments

<Note>
  Custom authentication methods are read-only configurations. To modify an existing custom authentication method, please work with your ASAPP account team.
</Note>
