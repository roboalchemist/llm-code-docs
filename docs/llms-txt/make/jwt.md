# Source: https://developers.make.com/custom-apps-documentation/app-components/connections/jwt.md

# JWT

There's no dedicated JWT connection type because the JWT is a special format of the Authorization header. See the [basic connection](https://developers.make.com/custom-apps-documentation/app-components/connections/basic-connection) section for more information.

## Generating a JWT

To generate the token, use the following code:

{% tabs %}
{% tab title="Code example" %}

```json
{
  "url": "https://mock.api/connect",
  "temp": {
    "jwt": {
      "iss": "https://iam.the.issu.er",
      "iat": "{{timestamp}}",
      "exp": "{{timestamp + 30000}}",
      "scope": ["rest_webservices"],
      "aud": "https://iam.the.audien.ce/services/rest/auth/oauth2/v1/token"
      },
    "options": {
      "header": {
        "kid": "{{parameters.clientId}}"
	}
      }
    },
    "headers": {
      "authorization": "Bearer {{jwt(temp.jwt, parameters.clientSecret, 'HS512', temp.options)}}"
    }
}
```

{% hint style="info" %}
The options argument refers to the same options object as in the [npm library](https://www.npmjs.com/package/jsonwebtoken).
{% endhint %}
{% endtab %}
{% endtabs %}

In this example, you can build a JWT payload inside the `temp` variable called `jwt`.

Inside the Authorization header, call the IML function named `jwt`. The `jwt` function accepts four parameters:

1. The **payload** to be signed.
2. The **secret** to sign the payload.
3. The **algorithm**. The supported algorithms are `HS256`, `HS384`, `HS512`, and `RS256`. The default value is `HS256`. This parameter is optional.
4. A **custom header** to customize the JWT authorization header. This parameter is optional.

This function will output a JWT token which you can use in the Authorization header.
