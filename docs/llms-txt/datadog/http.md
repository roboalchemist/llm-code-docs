# Source: https://docs.datadoghq.com/actions/connections/http.md

---
title: HTTP Requests
description: >-
  Make custom HTTP requests to endpoints with configurable authentication,
  methods, headers, and response handling for workflows and apps.
breadcrumbs: Docs > Connections > HTTP Requests
---

# HTTP Requests

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

Use the **Make request** action to make a custom request to an HTTP endpoint. You can control the request method and its contents, how it is authenticated and processed, and how it should respond to scenarios like expired certificates or redirects. If you need to add Datadog IP address ranges to your allowlist so that the HTTP action works as expected, use the IPs listed in the `webhooks` object. See the [IP Ranges API](https://docs.datadoghq.com/api/latest/ip-ranges/#list-ip-ranges) for details.

To add an HTTP Request:

{% tab title="Workflow Automation" %}

- In a new workflow, click **Add step** and search for `Make request`. Select the **Make request** action to add it to your workflow.
- In an existing workflow, click **+** and search for `Make request`. Select the **Make request** action to add it to your workflow.

Specify the request method and any necessary [authentication](https://docs.datadoghq.com/actions/workflows/access_and_auth/). Read the sections below for further information about the available configuration options. Optionally, the request can wait on conditions that you specify in the **Conditional wait** section, and retry at a given interval if the condition is not satisfied.
{% /tab %}

{% tab title="App Builder" %}

1. In your app, under **Data**, click **+ New** and select **Query**
1. Search for `HTTP`, then select the **Make request** action to add it to your app.

Specify the request method and any necessary [authentication](https://docs.datadoghq.com/actions/app_builder/access_and_auth/). Read the sections below for further information about the available configuration options.
{% /tab %}

## Authentication{% #authentication %}

If you need to authenticate your request, use the action's **Connection** to configure the authentication method. You can either select a preconfigured connection from the dropdown, or create a connection.

### Create an AWS connection{% #create-an-aws-connection %}

1. In the **Connection** section, click the plus icon (**+**).
1. Select **AWS**.
1. Enter a **Connection Name**, **Account ID**, and **AWS Role Name**.
1. Click **Create**.

### Create an Azure connection{% #create-an-azure-connection %}

1. In the **Connection** section, click the plus icon (**+**).
1. Select **Azure**.
1. Enter a **Connection Name**, **Tenant ID**, **Client ID**, and **Client Secret**.
1. Optionally, enter the **Custom Scope** to be requested from Microsoft when acquiring an OAuth 2 access token. A resource's scope is constructed using the identifier URI for the resource and `.default`, separated by a forward slash (`/`). For example, `{identifierURI}/.default`. For more information, see [the Microsoft documentation on .default scope](https://learn.microsoft.com/en-us/azure/active-directory/develop/scopes-oidc#the-default-scope).
1. Click **Create**.

### Create an HTTP token authentication connection{% #create-an-http-token-authentication-connection %}

The Token Auth connection uses a bearer token to authenticate the HTTP request.

1. In the **Connection** section, click the plus icon (**+**).
1. Select **HTTP**.
1. Enter a **Connection Name**.
1. Enter the **Base URL** for authentication.
1. From the **Authentication Type** dropdown, select **Token Auth**.
1. Enter a **Token Name** and **Token Value**. You can enter multiple tokens. To reference your token in a header, parameter, or the request body, use the syntax `{{ secretTokenName }}`.
1. Optionally, add additional **Request Headers**, **URL parameters** and a **Body** to your request.
1. Click **Create**.

### Create an HTTP basic authentication connection{% #create-an-http-basic-authentication-connection %}

The Basic Auth connection uses an authorization header with a username and password to authenticate the HTTP request.

1. In the **Connection** section, click the plus icon (**+**).
1. Select **HTTP**.
1. Enter a **Connection Name**.
1. Enter the **Base URL** for authentication.
1. From the **Authentication Type** dropdown, select **Basic Auth**.
1. Enter a **Username** and **Password**. The required authorization request header is automatically populated using your username and password.
1. Click **Create**.

### Create a 2 Step HTTP authentication connection{% #create-a-2-step-http-authentication-connection %}

The HTTP 2 step connection allows you to make a preliminary request to retrieve an access token with which to authenticate the HTTP request. This is useful for authenticating JSON Web Token (JWT) and OAuth applications.

1. In the **Connection** section, click the plus icon (**+**).
1. Select **HTTP**.
1. Enter a **Connection Name**.
1. Enter the **Base URL** for authentication.
1. From the **Authentication Type** dropdown, select **2 Step Auth**.

{% tab title="Token auth" %}
Configure the preliminary access token query:

1. From the **Secret Type** dropdown, select **Token Auth**.
1. Enter a Token Name and Token Value
1. Enter the **Request URL** and specify the type of request as either **GET** or **POST**.
1. Optionally, add additional **Request Headers**, **URL parameters** and a **Body** to the request.

Get the access token from the response:

1. Under **Variable Path to Access Token**, enter the path to the access token in the response. This is the path through which your access token is returned after making the authentication call. For example, if the access token is returned as the body of the access request, use `body`. If the access token is returned in a property called `token` of the response `body`, use `body.token`. Paths are case sensitive.
1. Optionally, enter a **Refresh Interval**. This is the duration until the access token expires, specified in seconds. When the token expires, the connection automatically requests a new access token. Setting an interval of `0` disables token refresh.

Use your retrieved token to authenticate your connection:

1. Under **Request Detail**, enter **Request Headers**, **URL parameters** and a **Body** to complete your request using the retrieved access token.
1. Click **Create**.

{% /tab %}

{% tab title="Basic auth" %}
Configure the preliminary authentication query:

1. From the **Secret Type** dropdown, select **Basic Auth**.
1. Enter a **Username** and **Password**. The **Request Headers** section is automatically populated using your username and password.

Configure the authentication request:

1. Enter the **Request URL** and specify the type of request as either **GET** or **POST**.
1. Optionally, add additional **Request Headers**, **URL parameters** and a **Body** to the request.

Get the access token from the response:

1. Under **Variable Path to Access Token**, enter the path to the access token in the response. This is the path through which your access token is returned after making the authentication call. For example, if the access token is returned as the body of the access request, use `body`. If the access token is returned in a property called `token` of the response `body`, use `body.token`. Paths are case sensitive.
1. Optionally, enter a **Refresh Interval**. This is the duration until the access token expires, specified in seconds. When the token expires, the connection automatically requests a new access token. Setting an interval of `0` disables token refresh.

Use your retrieved token to authenticate your connection:

1. Under **Request Detail**, enter **Request Headers**, **URL parameters** and a **Body** to complete your request using the retrieved access token.
1. Click **Create**.

{% /tab %}

### Create an HTTP mTLS connection{% #create-an-http-mtls-connection %}

The Mutual TLS (mTLS) Auth connection allows you to use a private key and TLS certificate to authenticate the HTTP request.

{% alert level="info" %}
The client certificate (`.crt`, `.pem`) and private key (`.key`, `.pem`) must use the PEM format.
{% /alert %}

1. In the **Connection** section, click the plus icon (**+**).
1. Select **HTTP**.
1. Enter a **Connection Name**.
1. Enter the **Base URL** for authentication.
1. From the **Authentication Type** dropdown, select **mTLS Auth**.
1. Click **Upload File** to upload your **Private Key**.
1. Click **Upload File** to upload your **Certificate**.
1. Click **Create**.

## Inputs{% #inputs %}

A URL and request method are required for your request. Optionally, you can enter:

- URL parameters
- headers
- the content type
- a request body
- cookies

You can also select whether you want to allow expired certificates, or follow redirects.

### Response options{% #response-options %}

Under **Error on Status**, enter a comma-delineated list of any status codes on which to return an error. Use the **Response Parsing** dropdown to override the default response parsing method inferred from the headers, and **Response Encoding** if the target server specifies the wrong encoding in its response headers.

## Private actions{% #private-actions %}

{% callout %}
##### Join the Preview!

Private Actions are in Preview. Use this form to request access today.

[Request Access](https://www.datadoghq.com/product-preview/private-actions/)
{% /callout %}

You can use a private HTTP action to interact with services hosted on your private network without exposing your services to the public internet. Private actions make use of a private action runner which you install on a host in your network using Docker and pair with a Datadog Connection. For more information, see [Private Actions](https://docs.datadoghq.com/actions/private_actions).

To configure a private HTTP request:

1. Add an HTTP action to your app.

1. In the **Connection** section, click the plus icon (**+**).

1. Select **HTTP**.

1. Enter a **Connection Name**.

1. Enter the **Base URL** for the host in your private network.

1. For **Type**, ensure that **Private Action Runner** is selected.

1. From the **Private Action Runner** dropdown, select your [private action runner](https://docs.datadoghq.com/actions/private_actions).

1. From the **Authentication Type** dropdown, select an Authentication type and fill in the required fields. Private HTTP requests support the following authentication types:

   - No authentication
   - Basic authentication
   - Token authentication

For information on configuring credentials for Token authentication, see [Handling Private Action Credentials](https://docs.datadoghq.com/actions/private_actions/private_action_credentials/?tab=httpsaction#credential-files).

1. Click **Next, Confirm Access** and configure access to the query.

1. Click **Create**.

## Further reading{% #further-reading %}

- [Find out more about connection credentials](https://docs.datadoghq.com/actions/connections/)

Do you have questions or feedback? Join the **#workflows** or **#app-builder** channel on the [Datadog Community Slack](https://chat.datadoghq.com/).
