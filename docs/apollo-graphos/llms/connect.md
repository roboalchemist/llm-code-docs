# Source: https://www.apollographql.com/docs/graphos/platform/explorer/connect.md

# Connecting and Authenticating with the Explorer

The Explorer automatically attempts to connect to your GraphQL server at the URL specified in its Settings tab.

When you use the Explorer with a [cloud supergraph](https://www.apollographql.com/docs/graphos/routing/cloud#cloud-supergraphs), the endpoint URL is always the URL of your current variant's GraphOS Router.

Depending on your GraphQL server's settings, you might need to configure the Explorer's connection to handle CORS requirements or authentication.

## CORS policies

Requests from the Explorer go straight from your browser to your GraphQL server, so your endpoint sees requests coming from this domain: `https://studio.apollographql.com`

It's common for public endpoints to set [CORS policies](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) that restrict which domains can query them. If your endpoint has CORS protections enabled, you probably need to safelist `https://studio.apollographql.com` in your CORS policy to use the Explorer.

To do so, include the following header(s) in your server's responses:

```bash
Access-Control-Allow-Origin: https://studio.apollographql.com

# Include this only if your server *also* authenticates via cookies.
Access-Control-Allow-Credentials: true
```

If you can't change your CORS policy, you might be able to create a proxy for your endpoint and point the Explorer to the proxy instead. CORS policies are enforced by browsers, and the proxy won't have the same issues communicating with your endpoint.

## Authentication

The Explorer provides features to help you authenticate via [request headers](https://www.apollographql.com/docs/graphos/platform/explorer/connect.md#request-headers), [cookies](https://www.apollographql.com/docs/graphos/platform/explorer/connect.md#cookies), and [scripts](https://www.apollographql.com/docs/graphos/platform/explorer/connect.md#custom-scripts).

If your graph has authentication requirements that aren't covered by these options, please contact [support@apollographql.com](mailto:support@apollographql.com) with questions or feedback.

### Request headers

The bottom panel of the Explorer includes a Headers tab where you can set headers that are included in your operation's HTTP request.

Headers can include the values of [environment variables](https://www.apollographql.com/docs/graphos/platform/explorer/connect.md#environment-variables), which are injected using double curly braces.

For example, a header with the key `Authorization` could have the value `Bearer {{token}}`.

### Cookies

If your server uses cookies to authenticate, you can configure your endpoint to share those cookies with `https://studio.apollographql.com`

To set this up, your [cookie's value must contain `SameSite=None; Secure`](https://www.chromium.org/updates/same-site). Additionally, the following CORS headers must be present in your server's response to Studio:

```bash
Access-Control-Allow-Origin: https://studio.apollographql.com
Access-Control-Allow-Credentials: true
```

Once configured, requests sent from `https://studio.apollographql.com` include the cookies from your domain when you run queries with the Explorer. If you're logged in on your domain, requests from the Explorer will also be logged in. If you log out on your domain and the cookie is removed, requests from the Explorer will be logged out.

#### Cookies for Safari users

Safari `13.1` and later [blocks third-party cookies by default](https://webkit.org/blog/10218/full-third-party-cookie-blocking-and-more/). When using Explorer in Safari, it considers your server's endpoint to be "third-party" to GraphOS Studio. Therefore, Safari users need to open **Settings > Privacy** in Safari and deselect **Prevent cross-site tracking** to send Explorer requests with cookies.

### Environment variables

The Explorer's Settings tab includes a section for defining environment variables. Here, you can provide sensitive information that you can then inject into header values, GraphQL variables, or [scripts](https://www.apollographql.com/docs/graphos/platform/explorer/connect.md#custom-scripts).
This lets you share operations (including their headers) with other team members without exposing this sensitive data.

#### Defining

You define environment variables in the Explorer's Settings tab, like so:

```json
{
  "exampleToken": "tokenValue"
}
```

If you share an operation that uses environment variables with your team members, your values for those environment variables are not shared, and other users can provide their own values.

#### Injecting

You can inject your Explorer environment variables into any of the following:

* [HTTP header values](https://www.apollographql.com/docs/graphos/platform/explorer/connect.md#header-values)
* [GraphQL variable values](https://www.apollographql.com/docs/graphos/platform/explorer/connect.md#graphql-variables)
* [Custom scripts](https://www.apollographql.com/docs/graphos/platform/explorer/connect.md#custom-scripts)

##### Header values

Inject an environment variable into an HTTP header value by surrounding the variable's name with double curly braces. For example, a header with the key `Authorization` could have the value `Bearer {{token}}`.

##### GraphQL variables

Inject an environment variable into a GraphQL variable value by surrounding the variable's name with double curly braces, like so:

```json
{
  "token": "{{token}}"
}
```

##### Custom scripts

If you create a [preflight or operation script](https://www.apollographql.com/docs/graphos/platform/explorer/scripting), that script can access an environment variable's value like so:

```js
const secretToken = explorer.environment.get('token');
```

Check out the Explorer [scripting docs](https://www.apollographql.com/docs/graphos/platform/explorer/scripting) to learn how you can use preflight scripts for authentication purposes.
