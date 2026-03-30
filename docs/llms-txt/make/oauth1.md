# Source: https://developers.make.com/custom-apps-documentation/app-components/connections/oauth1.md

# OAuth 1.0

While OAuth 1.0 is supported, it is not commonly used. Unless you are dealing with a legacy platform, we suggest you use a [basic connection](https://developers.make.com/custom-apps-documentation/app-components/connections/basic-connection) or [OAuth 2.0](https://developers.make.com/custom-apps-documentation/app-components/connections/oauth2).

Before you start to configure your OAuth 1.0 connection, create an app on a third-party service. When creating an app, use `https://www.integromat.com/oauth/cb/app-oauth1` as a callback URL.

## Components

### Communication

For more information, see the [communication](https://developers.make.com/custom-apps-documentation/component-blocks/api) documentation.

* `aws` directive is not available
* Communication is extended with `oauth`
* `pagination` directive is not available
* `response.limit` is not available
* `response.iterate` directive is not available
* `response.output` is not available
* `response` is extended with `data`

#### oauth

It is sometimes tedious and difficult to generate an OAuth 1.0 Authorization header. Below are all the properties that you can use to customize the header generation.

<table><thead><tr><th width="212" valign="top">Key</th><th width="148.33333333333331" valign="top">Type</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top"><code>consumer_key</code></td><td valign="top">IML String</td><td valign="top">Your consumer key</td></tr><tr><td valign="top"><code>consumer_secret</code></td><td valign="top">IML String</td><td valign="top">Your consumer secret</td></tr><tr><td valign="top"><code>private_key</code></td><td valign="top">IML String</td><td valign="top">Instead of <code>consumer_secret</code> you can specify a <code>private_key</code> string in PEM format</td></tr><tr><td valign="top"><code>token</code></td><td valign="top">IML String</td><td valign="top">An expression that parses the <code>oauth_token</code> string.</td></tr><tr><td valign="top"><code>token_secret</code></td><td valign="top">IML String</td><td valign="top">An expression that parses the <code>oauth_token_secret</code> string.</td></tr><tr><td valign="top"><code>verifier</code></td><td valign="top">IML String</td><td valign="top">An expression that parses the <code>oauth_verifier</code> string.</td></tr><tr><td valign="top"><code>signature_method</code></td><td valign="top">String</td><td valign="top">Specifies the desired method to use when calculating the signature. Can be either <code>HMAC-SHA1</code>, <code>RSA-SHA1</code>, <code>PLAINTEXT</code>. Default is <code>HMAC-SHA1</code>.</td></tr><tr><td valign="top"><code>transport_method</code></td><td valign="top">String</td><td valign="top">Specifies how OAuth parameters are sent: via query params, header or in a POST body. Can be either <code>query</code>, <code>body</code> or <code>header</code>. Default is <code>header</code></td></tr><tr><td valign="top"><code>body_hash</code></td><td valign="top">IML String</td><td valign="top">To use Request Body Hash, you can either manually generate it, or you can set this directive to <code>true</code> and the body hash will be generated automatically</td></tr></tbody></table>

#### response.data

The `data` directive saves data to the connection so that it can be later accessed from a module through the `connection` variable. It functions similarly to the `temp` directive, except that `data` is persisted to the connection.

{% tabs %}
{% tab title="Code example" %}

```json
{
    "response": {
        "data": {
            "accessToken": "{{body.token}}"
        }
    }
}
```

{% endtab %}

{% tab title="Code example used to access later" %}

```json
{
    "url": "http://example.com",
    "qs": {
        "token": "{{connection.accessToken}}"
    }
}
```

{% hint style="info" %}
This `accessToken` can be later accessed in any module that uses this connection.
{% endhint %}
{% endtab %}
{% endtabs %}

### ​Parameters​ <a href="#parameters" id="parameters"></a>

[Parameters](https://developers.make.com/custom-apps-documentation/block-elements/parameters) the user needs to provide when setting up a new connection.

### Default scope

[Default scope](https://developers.make.com/custom-apps-documentation/component-blocks/scope) for every new connection.

### Scope list

Collection of available [scopes](https://developers.make.com/custom-apps-documentation/component-blocks/scopes).

### ​Common data​ <a href="#common-data" id="common-data"></a>

[Non-user-specific sensitive values](https://developers.make.com/custom-apps-documentation/app-components/connections) like secrets.

## OAuth 1.0 authentication process

The OAuth 1.0 authentication process consists of multiple steps. You can fill in the necessary sections and delete those that are unnecessary.

<table><thead><tr><th width="178.33333333333331" valign="top">Key</th><th width="209" valign="top">Type</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top"><code>oauth</code></td><td valign="top">OAuth 1 parameters specification</td><td valign="top">Allows you to specify special OAuth 1.0 properties to simplify OAuth 1.0 header generation.</td></tr><tr><td valign="top"><code>requestToken</code></td><td valign="top">Request specification</td><td valign="top">Describes a request that retrieves the request token</td></tr><tr><td valign="top"><code>authorize</code></td><td valign="top">Request specification</td><td valign="top">Describes the authorization process.</td></tr><tr><td valign="top"><code>accessToken</code></td><td valign="top">Request specification</td><td valign="top">Describes a request that exchanges credentials and the request token for the access token.</td></tr><tr><td valign="top"><code>info</code></td><td valign="top">Request specification</td><td valign="top">Describes a request that validates a connection. The most common way to validate the connection is to call a method to get user’s information. Most of the APIs have such a method.</td></tr></tbody></table>

When using an OAuth 1.0 connection there is a special object available globally: the `oauth` object. You can use it in the connection specification as well as in module specifications to avoid generating the OAuth 1.0 header yourself. This object is available at the root of the connection specification, in the Base and in the Request Specification.

If the `oauth` object is present in the root of the connection specification, it will be merged with each of the directives described above. If you wish to override some properties of the root object, you can do so in the respective directive by specifying the `oauth` object and overriding the properties.

## Available IML variables

These IML variables are available for you to use everywhere in this module:

<table><thead><tr><th width="170.74072265625" valign="top">Variable</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top"><code>now</code></td><td valign="top">Current date and time</td></tr><tr><td valign="top"><code>environment</code></td><td valign="top">TBD</td></tr><tr><td valign="top"><code>temp</code></td><td valign="top">Contains custom variables created via <code>temp</code> directive.</td></tr><tr><td valign="top"><code>parameters</code></td><td valign="top">Contains the connection’s input parameters.</td></tr><tr><td valign="top"><code>common</code></td><td valign="top">Contains the connection’s common data collection.</td></tr><tr><td valign="top"><code>data</code></td><td valign="top">Contains the connection's data collection.</td></tr><tr><td valign="top"><code>oauth.scope</code></td><td valign="top">Contains an array of scope required to be passed to the OAuth 1.0 authorization process.</td></tr><tr><td valign="top"><code>oauth.redirectUri</code></td><td valign="top">Contains the redirect URL for the OAuth 1.0 authorization process.</td></tr></tbody></table>
