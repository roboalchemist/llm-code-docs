# Source: https://docs.api7.ai/apisix/getting-started/key-authentication.md

# Key Authentication

An API gateway's primary role is to connect API consumers and providers. For security reasons, it should authenticate and authorize consumers before allowing them to access upstream resources.

![Key Authentication](https://static.api7.ai/uploads/2023/02/08/8mRaK3v1_consumer.png)

APISIX has a flexible plugin extension system and a number of existing plugins for user authentication and authorization. For example:

* [Key Authentication](https://docs.api7.ai/hub/key-auth.md)
* [Basic Authentication](https://docs.api7.ai/hub/basic-auth.md)
* [HMAC](https://docs.api7.ai/hub/hmac-auth.md)
* [JSON Web Token (JWT) Authentication](https://docs.api7.ai/hub/jwt-auth.md)
* [OpenID Connect](https://docs.api7.ai/hub/openid-connect.md)
* [Keycloak Authorization](https://docs.api7.ai/hub/authz-keycloak.md)
* [Casdoor Authorization](https://apisix.apache.org/docs/apisix/plugins/authz-casdoor/)
* [Casbin Authorization](https://apisix.apache.org/docs/apisix/plugins/authz-casbin/)
* [Open Policy Agent (OPA)](https://docs.api7.ai/hub/opa.md)
* [Wolf RBAC](https://apisix.apache.org/docs/apisix/plugins/wolf-rbac/)
* [Central Authentication Service (CAS)](https://apisix.apache.org/docs/apisix/plugins/cas-auth/)
* [LDAP](https://apisix.apache.org/docs/apisix/plugins/ldap-auth/)
* [Forward Authentication](https://docs.api7.ai/hub/forward-auth.md)

In this tutorial, you will create a [consumer](https://docs.api7.ai/apisix/key-concepts/consumers.md), configure its [credential](https://docs.api7.ai/apisix/key-concepts/consumers.md) with [key authentication](https://docs.api7.ai/hub/key-auth.md), and learn how to enable and disable key authentication.

## Key Concepts[â](#key-concepts "Direct link to Key Concepts")

### Consumer[â](#consumer "Direct link to Consumer")

A *consumer* is an application or a developer who consumes the API.

In APISIX, a consumer requires a unique `username` to be created. As part of the key authentication configuration, you would also add one of the authentication plugins from the list above to the consumer's `plugin` field.

### Key Authentication[â](#key-authentication "Direct link to Key Authentication")

Key authentication is a relatively simple but widely used authentication approach. The idea is as follows:

1. Administrator adds an authentication plugin to the route.
2. API consumers attach the key to the query string or headers for authentication when sending requests.

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

1. Complete [Get APISIX](https://docs.api7.ai/apisix/getting-started/.md) to install APISIX in Docker.
2. Complete [Configure Routes](https://docs.api7.ai/apisix/getting-started/configure-routes.md).
3. Install [ADC](https://docs.api7.ai/apisix/reference/adc.md) or [APISIX-MCP](https://docs.api7.ai/apisix/reference/apisix-mcp.md) if you are using these tools.

## Configure Key Authentication[â](#configure-key-authentication "Direct link to Configure Key Authentication")

* Admin API
* ADC
* APISIX-MCP

### Create a Consumer

Create a consumer `tom`:

caution

Please use a complex key in the production environment.

```
curl -i "http://127.0.0.1:9180/apisix/admin/consumers" -X PUT -d '
{
  "username": "tom"
}'
```

You will receive an `HTTP/1.1 201 Created` response if the consumer was created successfully.

### Configure Consumer Credential

Configure the consumer `key-auth` credential for `tom`:

```
curl "http://127.0.0.1:9180/apisix/admin/consumers/tom/credentials" -X PUT -d '
{
  "id": "cred-tom-key-auth",
  "plugins": {
    "key-auth": {
      "key": "secret-key"
    }
  }
}'
```

You will receive an `HTTP/1.1 201 Created` response if the consumer credential was created.

### Enable Authentication

Update the `getting-started-ip` route from [Configure Routes](https://docs.api7.ai/apisix/getting-started/configure-routes.md) to add the `key-auth` plugin:

```
curl -i "http://127.0.0.1:9180/apisix/admin/routes/getting-started-ip" -X PATCH -d '
{
  "plugins": {
    "key-auth": {}
  }
}'
```

You will receive an `HTTP/1.1 200 OK` response if the route was updated successfully.

Create an ADC configuration file containing a consumer and a route:

adc.yaml

```
consumers:
  - username: tom
    credentials:
      - name: tom-key
        type: key-auth
        config:
          key: secret-key
services:
  - name: httpbin Service
    routes:
      - uris:
          - /ip
        name: getting-started-ip
        plugins:
          key-auth: {}
    upstream:
      type: roundrobin
      nodes:
        - host: httpbin.org
          port: 80
          weight: 1
```

Synchronize the configuration to APISIX:

```
adc sync -f adc.yaml
```

Enter the following prompt in your AI client:

```
Create a consumer named tom in APISIX and the key-auth credential for the consumer should be secret-key.
Enable the key-auth plugin on the route getting-started-ip, requiring consumers to provide an API key when accessing that route.
```

You should see a response similar to the following:

```
Created consumer 'tom' with key-auth credential and enabled key-auth plugin on route 'getting-started-ip'. The consumer can now access the route using API key 'secret-key' in either the 'apikey' header or query parameter.
```

## Verify[â](#verify "Direct link to Verify")

You will be verifying if the key authentication is successfully enabled in this section.

* Admin API
* ADC
* APISIX-MCP

### Send a Request without Any Key

Send a request without the `apikey` header.

```
curl -i "http://127.0.0.1:9080/ip"
```

Since the key is not provided, you will receive an unauthorized `HTTP/1.1 401 Unauthorized` response.

### Send a Request with a Wrong Key

Send a request with a wrong key in the `apikey` header.

```
curl -i "http://127.0.0.1:9080/ip" -H 'apikey: wrong-key'
```

Since the key is incorrect, you will receive an `HTTP/1.1 401 Unauthorized` response.

### Send a Request with the Correct Key

Send a request with the correct key in the `apikey` header.

```
curl -i "http://127.0.0.1:9080/ip" -H 'apikey: secret-key'
```

Since the correct key is provided, you will receive an `HTTP/1.1 200 OK` response.

### Send a Request without Any Key

Send a request without the `apikey` header.

```
curl -i "http://127.0.0.1:9080/ip"
```

Since the key is not provided, you will receive an unauthorized `HTTP/1.1 401 Unauthorized` response.

### Send a Request with a Wrong Key

Send a request with a wrong key in the `apikey` header.

```
curl -i "http://127.0.0.1:9080/ip" -H 'apikey: wrong-key'
```

Since the key is incorrect, you will receive an `HTTP/1.1 401 Unauthorized` response.

### Send a Request with the Correct Key

Send a request with the correct key in the `apikey` header.

```
curl -i "http://127.0.0.1:9080/ip" -H 'apikey: secret-key'
```

Since the correct key is provided, you will receive an `HTTP/1.1 200 OK` response.

### Send a Request without Any Key

Enter the following prompt in your AI client:

```
Send a request to the route without any authentication header.
```

You should see a response similar to the following:

```
Unauthenticated request to '/ip' returned 401 as expected
```

### Send a Request with a Wrong Key

Enter the following prompt in your AI client:

```
Send a request to the route with wrong-key.
```

You should see a response similar to the following:

```
Invalid API key returns 401 (wrong credentials)
```

### Send a Request with the Correct Key

Enter the following prompt in your AI client:

```
Send a request to the route with secret-key.
```

You should see a response similar to the following:

```
Valid API key 'secret-key' authenticates successfully (200)
```

## Disable Authentication[â](#disable-authentication "Direct link to Disable Authentication")

Disable the key authentication plugin by setting the `_meta.disable` parameter to `true`.

* Admin API
* ADC
* APISIX-MCP

```
curl "http://127.0.0.1:9180/apisix/admin/routes/getting-started-ip" -X PATCH -d '
{
  "plugins": {
    "key-auth": {
      "_meta": {
        "disable": true
      }
    }
  }
}'
```

Send a request without any key to verify:

```
curl -i "http://127.0.0.1:9080/ip"
```

Since key authentication is disabled, you will receive an `HTTP/1.1 200 OK` response.

adc.yaml

```
consumers:
  - username: tom
    plugins:
      key-auth:
        key: secret-key
services:
  - name: httpbin Service
    routes:
      - uris:
          - /ip
        name: getting-started-ip
        plugins:
          key-auth:
            _meta:
              disable: true
    upstream:
      type: roundrobin
      nodes:
        - host: httpbin.org
          port: 80
          weight: 1
```

Synchronize the configuration to APISIX:

```
adc sync -f adc.yaml
```

Send a request without any key to verify:

```
curl -i "http://127.0.0.1:9080/ip"
```

Since key authentication is disabled, you will receive an `HTTP/1.1 200 OK` response.

Enter the following prompt in your AI client:

```
Disable the key authentication plugin for the route getting-started-ip while keeping its configuration intact.
```

You should see a response similar to the following:

```
Successfully disabled the key-auth plugin for route 'getting-started-ip' while maintaining all other configuration. The route now:

* Still matches requests to URI '/ip'
* Forwards to upstream httpbin.org:80
* No longer requires API key authentication
Retains all other settings including load balancing configuration
```

Send a request without any key in your AI client:

```
Send a request to the route without any key.
```

You should see a response similar to the following:

```
The request to the /ip route without an API key was successful (HTTP 200).
```

## What's Next[â](#whats-next "Direct link to What's Next")

You have learned how to configure key authentication for a route. In the next tutorial, you will learn how to configure rate limiting.
