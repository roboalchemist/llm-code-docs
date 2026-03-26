# Source: https://docs.api7.ai/hub/key-auth.md

# Source: https://docs.api7.ai/cloud/guides/traffic-management/authentication/key-auth.md

# Use Key Auth to Protect Your APIs

You may want to protect your [routes](https://docs.api7.ai/cloud/concepts/route.md) or [services](https://docs.api7.ai/cloud/concepts/service.md) by using API authentication. With the requirement of authentication, API7 Cloud will only forward API requests with valid authentication credentials. Other requests (without credentials or with a wrong one) will be rejected and get a `401 Unauthorized` response.

Key Auth is an API authentication method that asks the API clients to provide a valid key or token as the identifier. The key (or the token) will be shared by the API clients and the API provider or the API Gateway.

This guide will introduce using Key Auth to protect your APIs on API7 Cloud. You can also safeguard services as long as you configure the Authentication plugin on the Service (instead of a specific route).

important

API7 Cloud uses the [Consumer](https://docs.api7.ai/cloud/concepts/consumer.md) concept to implement fine-grained API authentication, so please learn what is Consumer before you go ahead.

## Prepare the Environment[â](#prepare-the-environment "Direct link to Prepare the Environment")

### Deploy Apache APISIX[â](#deploy-apache-apisix "Direct link to Deploy Apache APISIX")

Please refer to [How to Deploy Apache APISIX](https://docs.api7.ai/cloud/guides/product/how-to-deploy-apache-apisix.md) to learn how to deploy Apache APISIX and connect it to API7 Cloud. In this guide, we'll deploy an Apache APISIX instance on Docker.

### Create Service and Route[â](#create-service-and-route "Direct link to Create Service and Route")

We'll create a service with the following details in this guide.

1. The service name is `key-auth-app`.
2. The path prefix is `/v1`.
3. The HTTP Host is `auth.httpbin.org`.
4. The upstream URL is `https://httpbin.org`.

Besides, we'll create a route inside the `key-auth-app` service.

1. The route name is `json`.
2. The path is `/json` (exact match).
3. Accepted HTTP method is `GET`.

tip

If you don't know how to configure a service and route, please refer to the [Getting Started](https://docs.api7.ai/cloud/getting-started/.md) guides first

## Configure Authentication Plugin on the Route[â](#configure-authentication-plugin-on-the-route "Direct link to Configure Authentication Plugin on the Route")

You need to enable the Authentication plugin on the `json` route as per the steps below:

1. Enter the `json` route details page.
2. Click on **Add Plugin** and select the Authentication plugin.
3. Choose Key Auth as the authentication method and fill out the form.

![Authentication Plugin Key Auth](https://static.api7.ai/2022/12/30/add-authentication-plugin-key-auth.png)

You can customize the HTTP request header name to carry the key. The default value is `apikey`. In this case, we set the header name to `Authorization`.

tip

The checkbox `Strip Credentials` controls if Apache APISIX should remove the authentication credentials before forwarding the requests to the backend. By default, it will be reserved.

Now let's try to access this route.

```
curl http://127.0.0.1:9080/v1/json -H 'Host: key-auth.httpbin.org' -i
```

```
HTTP/1.1 401 Unauthorized
Date: Wed, 08 Jun 2022 08:38:07 GMT
Content-Type: text/plain; charset=utf-8
Transfer-Encoding: chunked
Connection: keep-alive
Server: APISIX/2.15.0

{"message":"Missing API key found in request"}
```

Since we don't take any credentials, Apache APISIX will reject the request.

## Configure Key Auth Plugin on Consumer[â](#configure-key-auth-plugin-on-consumer "Direct link to Configure Key Auth Plugin on Consumer")

Now let's create a Consumer and enable the Authentication plugin.

1. The Consumer's name is `alex`.
2. Enable the Authentication plugin and choose Key Auth as the authentication method.
3. Fill in the string `ec8e8fa78d4e271b368d` as the API key.

## Test the Authentication[â](#test-the-authentication "Direct link to Test the Authentication")

Let's send a request with the API key.

```
curl http://127.0.0.1:9080/v1/json -H 'Host: auth.httpbin.org' -i -H 'Authorization: ec8e8fa78d4e271b368d'
```

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 429
Connection: keep-alive
Date: Wed, 08 Jun 2022 08:47:22 GMT
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true
Server: APISIX/2.15.0

{
  "slideshow": {
    "author": "Yours Truly",
    "date": "date of publication",
    "slides": [
      {
        "title": "Wake up to WonderWidgets!",
        "type": "all"
      },
      {
        "items": [
          "Why <em>WonderWidgets</em> are great",
          "Who <em>buys</em> WonderWidgets"
        ],
        "title": "Overview",
        "type": "all"
      }
    ],
    "title": "Sample Slide Show"
  }
}
```

After taking the correct API key, the request is forwarded to the backend.

If we take the wrong API key, the API request will also be rejected by Apache APISIX.

```
curl http://127.0.0.1:9080/v1/json -H 'Host: auth.httpbin.org' -i -H 'Authorization: bad-api-key'
```

```
HTTP/1.1 401 Unauthorized
Date: Wed, 08 Jun 2022 08:49:36 GMT
Content-Type: text/plain; charset=utf-8
Transfer-Encoding: chunked
Connection: keep-alive
Server: APISIX/2.15.0

{"message":"Invalid API key in request"}
```

## What's Next[â](#whats-next "Direct link to What's Next")

* [Authentication Plugin Reference](https://docs.api7.ai/cloud/references/plugins/traffic-management/authentication.md)
* [Apache APISIX Key Auth Plugin](https://apisix.apache.org/docs/apisix/next/plugins/key-auth/)
