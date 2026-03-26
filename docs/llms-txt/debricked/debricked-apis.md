# Source: https://docs.debricked.com/tools-and-integrations/debricked-apis.md

# OpenText Core SCA APIs

OpenText Core SCA is an API-first service, allowing for all actions inside the UI to be scripted. This allows you to integrate OpenText Core SCA service into your code, CI pipelines, and more.

All users with the role with the API access scope have access to OpenText Core SCA open API. This is also the API used by the [OpenText Core SCA CLI](https://docs.debricked.com/tools-and-integrations/cli/debricked-cli).

### Important API resources <a href="#importantapiresources" id="importantapiresources"></a>

* Base URL for API: <https://debricked.com/api>
* Current version URL: <https://debricked.com/api/1.0>
* [Open API reference/Sandbox](https://debricked.com/api/doc/open)
* [Open API reference/Sandbox, JSON format](https://debricked.com/api/doc/open.json)

### Authentication <a href="#howdoiauthenticate" id="howdoiauthenticate"></a>

The API uses JWT-tokens for authentication.

#### **Generate JWT-Tokens using your username and password**

In order to get a JWT-token you need to provide your username and password to: <https://debricked.com/api/login\\_check>

Using curl, the call would look like this:

```bash
curl https://debricked.com/api/login_check -d _username=YOUR_USERNAME -d _password=YOUR_PASSWORD
```

If successful, the response will contain your token:

```
{"token":"YOUR_VERY_LONG_TOKEN"}
```

*Note*: In case your username and/or password contains special characters, you need to url encode and surround it by quotes to ensure that it works as expected. See example:

```bash
curl https://debricked.com/api/login_check --data-urlencode '_username=email+extra@domain.com' --data-urlencode '_password=password&'

```

#### **Generate JWT-Tokens using a long-lived access token**

If you have added an access token, you can use it to get a short-lived JWT token by sending the access token to:&#x20;

<https://debricked.com/api/login\\_refresh>

Using curl the call would look like this:

```bash
curl https://debricked.com/api/login_refresh -d refresh_token=YOUR_ACCESS_TOKEN
```

### **Using tokens**

{% hint style="info" %}
Keep in mind that the long-lived access token, and the short-lived JWT-token are different tokens! You must always exchange your access token for a JWT-token to use the API.
{% endhint %}

The JWT-token has a lifetime of about an hour. If the JWT-token is invalid (e.g. if it has expired) a 401 status code will be returned. You should therefore implement a way of automatically getting a new token every time you receive a 401 status code from any API call.

When you have your token you need to pass it to the Authorization HTTP header with the value Bearer YOUR\_VERY\_LONG\_TOKEN on each API call.

For example, using curl:

```bash
curl -H 'Authorization: Bearer YOUR_VERY_LONG_TOKEN' https://debricked.com/api/the_api_endpoint
```

### API rate limits <a href="#apiratelimits" id="apiratelimits"></a>

The following rate limits apply:

* No account: 100 requests per hour (only applies for the Open Source Select API)
* Free account: 500 requests per hour per code contributor (up to a maximum of 5 000 requests per hour)
* Premium/Enterprise account: 5000 requests per hour per code contributor

If you require a higher rate limit, please contact the sales team.

### Mastering OpenText Core SCA's CLI and API - webinar recording

Check out our latest training webinar and learn the basics of working with OpenText Core SCA CLI and API:

{% embed url="<https://www.youtube.com/watch?v=3fEOTOwHGbM>" %}
