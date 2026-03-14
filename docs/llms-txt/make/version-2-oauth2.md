# Source: https://developers.make.com/custom-apps-development-training/version-2-oauth2.md

# Version 2 (OAuth2)

## Authorization flow

The API version 2 implements the OAuth2 authorization framework, enabling secure authentication and authorization to access its resources. This flow has been developed specifically for the Make Academy Custom Apps Development course, aiming to simulate a real-world authentication and authorization process.

Every developer can integrate Custom App Academy API V2 by obtaining up to one app access that involves registration of their application and obtaining client credentials.

To obtain the necessary client credentials (client ID and secret), you can submit the [form](https://airtable.com/apptuF9ohhm4eho3M/shrXXIuflEJFXaUPP). If you have previously submitted the form for API version 1, you should already have received the credentials to API version 2 via email.

{% hint style="info" %}
To provide a realistic user authorization experience, API version 2 includes a feature where users can select the specific account they want to connect with the application. This mimics the behavior seen in real-world applications.
{% endhint %}

<figure><img src="https://3114796191-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgNTg64InL2Ea6QArLuAq%2Fuploads%2FOWmjRcj7OZYrHYGYLr3A%2Fauthorization_form.png?alt=media&#x26;token=d545f3e3-d0ab-433c-8845-9398f92d3dee" alt="" width="375"><figcaption><p>Selection of the account authorize</p></figcaption></figure>

{% hint style="warning" %}
Each app user (John Doe/Jane Black) can have only one active connection. If you generate a new connection, the existing one will be removed.
{% endhint %}

### Step one: Redirect a user to your app

Redirect the user to `authorize` endpoint. This will prompt the user to allow your application to access the Custom App Academy API on their behalf. You need the user to allow the `connect` scope to successfully authorize access. To obtain the `code` parameter to authorize `token` request, set the `response_type` to `code`.

{% openapi src="<https://3114796191-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgNTg64InL2Ea6QArLuAq%2Fuploads%2F8dbg774IdnlOIMTtyULx%2FTKLOBOUCKOVA-app-academy-v2-1.0.0-swagger.json?alt=media&token=c8f5ec77-3a7f-46d5-99c2-69e52f1b4315>" path="/authorize" method="get" %}
[TKLOBOUCKOVA-app-academy-v2-1.0.0-swagger.json](https://3114796191-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgNTg64InL2Ea6QArLuAq%2Fuploads%2F8dbg774IdnlOIMTtyULx%2FTKLOBOUCKOVA-app-academy-v2-1.0.0-swagger.json?alt=media\&token=c8f5ec77-3a7f-46d5-99c2-69e52f1b4315)
{% endopenapi %}

### Step two: Handle the callback request

Once a user decides to allow or disallow your application access to their account, Custom App Academy will redirect them to the OAuth2 redirect URL that you set when submitting your form.

If there was an error processing the request, the response will contain an `error.message` parameter. If the request was successful, the response will contain `code` parameter.

### Step three: Retrieve an access token and refresh token

Use your application `client_id` and `client_secret` together with `code` from the previous step to issue a request to `token` endpoint. You must use the same redirect URL in the `token` request and `authorization_code` grant type.

A successful request will respond with `access_token`, `expires-in`, `refresh_token` and `refresh_expires_in` parameters. `expires-in` and `refresh_expires_in` values are in minutes.

{% openapi src="<https://3114796191-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgNTg64InL2Ea6QArLuAq%2Fuploads%2F8dbg774IdnlOIMTtyULx%2FTKLOBOUCKOVA-app-academy-v2-1.0.0-swagger.json?alt=media&token=c8f5ec77-3a7f-46d5-99c2-69e52f1b4315>" path="/token" method="post" %}
[TKLOBOUCKOVA-app-academy-v2-1.0.0-swagger.json](https://3114796191-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgNTg64InL2Ea6QArLuAq%2Fuploads%2F8dbg774IdnlOIMTtyULx%2FTKLOBOUCKOVA-app-academy-v2-1.0.0-swagger.json?alt=media\&token=c8f5ec77-3a7f-46d5-99c2-69e52f1b4315)
{% endopenapi %}

### Step four: Make an API request

After obtaining the access token, you can send requests to App Academy API that contain the `authorization` header in this format: `Bearer {access_token}`.

{% openapi src="<https://3114796191-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgNTg64InL2Ea6QArLuAq%2Fuploads%2F8dbg774IdnlOIMTtyULx%2FTKLOBOUCKOVA-app-academy-v2-1.0.0-swagger.json?alt=media&token=c8f5ec77-3a7f-46d5-99c2-69e52f1b4315>" path="/info" method="get" %}
[TKLOBOUCKOVA-app-academy-v2-1.0.0-swagger.json](https://3114796191-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgNTg64InL2Ea6QArLuAq%2Fuploads%2F8dbg774IdnlOIMTtyULx%2FTKLOBOUCKOVA-app-academy-v2-1.0.0-swagger.json?alt=media\&token=c8f5ec77-3a7f-46d5-99c2-69e52f1b4315)
{% endopenapi %}

### Step five: Refresh the access token

The API provides the `expires_in` parameter in the `token` response to determine if the user's access token has expired. If it has, use the `refresh` endpoint to retrieve a new access token and refresh token. `expires-in` and `refresh_expires_in` values are in minutes. To obtain a new access token and refresh token, the refresh token must not be expired!

{% openapi src="<https://3114796191-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgNTg64InL2Ea6QArLuAq%2Fuploads%2F8dbg774IdnlOIMTtyULx%2FTKLOBOUCKOVA-app-academy-v2-1.0.0-swagger.json?alt=media&token=c8f5ec77-3a7f-46d5-99c2-69e52f1b4315>" path="/refresh" method="post" %}
[TKLOBOUCKOVA-app-academy-v2-1.0.0-swagger.json](https://3114796191-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgNTg64InL2Ea6QArLuAq%2Fuploads%2F8dbg774IdnlOIMTtyULx%2FTKLOBOUCKOVA-app-academy-v2-1.0.0-swagger.json?alt=media\&token=c8f5ec77-3a7f-46d5-99c2-69e52f1b4315)
{% endopenapi %}

### Step six: Access invalidation

If the user wants to invalidate the access of your app to Custom App Academy API, use the `invalidate` endpoint.

{% openapi src="<https://3114796191-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgNTg64InL2Ea6QArLuAq%2Fuploads%2F8dbg774IdnlOIMTtyULx%2FTKLOBOUCKOVA-app-academy-v2-1.0.0-swagger.json?alt=media&token=c8f5ec77-3a7f-46d5-99c2-69e52f1b4315>" path="/invalidate" method="get" %}
[TKLOBOUCKOVA-app-academy-v2-1.0.0-swagger.json](https://3114796191-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgNTg64InL2Ea6QArLuAq%2Fuploads%2F8dbg774IdnlOIMTtyULx%2FTKLOBOUCKOVA-app-academy-v2-1.0.0-swagger.json?alt=media\&token=c8f5ec77-3a7f-46d5-99c2-69e52f1b4315)
{% endopenapi %}

## Scopes

API Version 2 provides integration with scopes. Scopes provide a granular level of access control and ensure that users can only access the specific resources they need. The following scopes are supported:

<table><thead><tr><th>Endpoint</th><th>Scope</th><th data-hidden></th></tr></thead><tbody><tr><td>authorize</td><td>connect</td><td></td></tr><tr><td>any GET endpoint*</td><td>read</td><td></td></tr><tr><td>any POST/PUT/PATCH ednpoint</td><td>write</td><td></td></tr><tr><td>any DELETE endpoint</td><td>delete</td><td></td></tr></tbody></table>

\*except for `/info` endpoint.

## Endpoints

In API version 2, all the endpoints available in API version 1 are fully supported. To make API calls in version 2, you need to use the URL for API version 2 as well as to ensure proper authorization and scope management by following the instructions provided above.

{% content-ref url="version-1-api-key" %}
[version-1-api-key](https://developers.make.com/custom-apps-development-training/version-1-api-key)
{% endcontent-ref %}
