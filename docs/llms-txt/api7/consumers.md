# Source: https://docs.api7.ai/enterprise/key-concepts/consumers.md

# Source: https://docs.api7.ai/enterprise/3.2.16.7/key-concepts/consumers.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/key-concepts/consumers.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/key-concepts/consumers.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/key-concepts/consumers.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/key-concepts/consumers.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/key-concepts/consumers.md

# Source: https://docs.api7.ai/enterprise/3.8.x/key-concepts/consumers.md

# Source: https://docs.api7.ai/enterprise/3.7.x/key-concepts/consumers.md

# Source: https://docs.api7.ai/enterprise/3.6.x/key-concepts/consumers.md

# Source: https://docs.api7.ai/enterprise/3.5.x/key-concepts/consumers.md

# Source: https://docs.api7.ai/enterprise/3.4.x/key-concepts/consumers.md

# Source: https://docs.api7.ai/enterprise/3.3.x/key-concepts/consumers.md

# Source: https://docs.api7.ai/apisix/key-concepts/consumers.md

# Source: https://docs.api7.ai/enterprise/3.3.x/key-concepts/consumers.md

# Source: https://docs.api7.ai/apisix/key-concepts/consumers.md

# Consumers

In this document, you will learn the basic concepts of consumers in APISIX and why you need them. You will be introduced to a few relevant concepts, including how to pass consumer information to upstream, consumer access restriction, as well as consumer authentication and authorization.

Explore additional resources at the end of the document for more information on related topics.

## Overview[â](#overview "Direct link to Overview")

In APISIX, a *consumer* object represents a user, application, or host that sends requests to the API gateway and consumes backend services. It is used in conjunction with the authentication system; that is, every consumer is associated with at least one authentication plugin.

Consumer objects come in handy if you have different consumers sending requests to your system, and you need APISIX to perform certain functions, such as rate limiting, based on consumers. These functionalities are provided by APISIX plugins configured in consumers.

The following diagram illustrates an example of APISIX with one [`key-auth`](https://docs.api7.ai/hub/key-auth.md) enabled route and two consumers, John and Jane. John and Jane each authenticates to the route with their [credentials](https://docs.api7.ai/apisix/key-concepts/credentials.md). Only authenticated requests are then allowed to access the upstream resource:

![consumers diagram](https://static.api7.ai/uploads/2024/09/12/nJhSZ7tC_consumers-label-udpated.svg)

The configuration above ensures if a request is sent to APISIX:

* without any key or with a wrong key, the request is rejected.
* with `john-key`, the request is authenticated and forwarded to the upstream service.
* with `jane-key`, the request is authenticated and forwarded to the upstream service. The rate limiting plugin [`limit-count`](https://docs.api7.ai/hub/limit-count.md) on the consumer also takes effect, limiting the number of requests to a maximum of 2 within any 5-second window. If the rate limit threshold is exceeded, the request will be rejected.

Note that when a consumer is successfully authenticated, APISIX adds additional headers, such as `X-Consumer-Username`, `X-Credential-Identifier`, `X-Consumer-Custom-ID`, to the request, before proxying it to the upstream service. The upstream service will be able to differentiate between consumers and implement additional logic as needed. If any of these values is not available, the corresponding header will not be added.

## Passing Consumer Information to Upstream[â](#passing-consumer-information-to-upstream "Direct link to Passing Consumer Information to Upstream")

For certain use cases, such as logging, analytics, and auditing, you might want to pass consumer information to upstream services. Consumer information, by default, is not exposed to upstream; however, you can use `proxy-rewrite` plugin to include the needed information in the header:

```
{
  "plugins":{
    ...,
    "proxy-rewrite":{
      "headers":{
        "set":{
          "X-Consumer-Name":"$consumer_name"
        }
      }
    }
  }
}
```

## Consumer Access Restriction[â](#consumer-access-restriction "Direct link to Consumer Access Restriction")

You can control request access to your API by imposing restrictions based on consumer name, HTTP methods, or other parameters in the `consumer-restriction` plugin.

For example, if you want to blacklist `Jane` from accessing your upstream service without changing any consumers configuration in the example from [overview](#overview), you can update the plugin's configuration in the route to the following:

```
{
  "plugins":{
    "key-auth":{},
    "consumer-restriction":{
      "blacklist":["Jane"]
    }
  }
}
```

Or, if you want to strictly allow `FetchBot`'s access by HTTP GET method, you can update the plugin's configuration (in either the route or the consumer) to the following:

```
{
  "plugins":{
    ...,
    "consumer-restriction":{
      "allowed_by_methods":[
        {
          "user":"FetchBot",
          "methods":["GET"]
        }
      ]
    }
  }
}
```

The [`consumer-restriction`](https://docs.api7.ai/hub/consumer-restriction.md) plugin can also be used with [routes](https://docs.api7.ai/apisix/key-concepts/routes.md), [services](https://docs.api7.ai/apisix/key-concepts/services.md), and [consumer groups](https://docs.api7.ai/apisix/key-concepts/consumer-groups.md).

## Authentication & Authorization[â](#authentication--authorization "Direct link to Authentication & Authorization")

There are two main design patterns for building authentication and authorization in an APISIX-based architecture.

The first and most commonly adopted approach is to authenticate and authorize requests through a third-party [identity provider (IdP)](https://en.wikipedia.org/wiki/Identity_provider), such as [Keycloak](https://www.keycloak.org):

![APISIX integration with an IdP](https://static.api7.ai/uploads/2023/03/16/N8W31TWC_consumers-auth1.svg)

<br />

In some environments, a request might need to go through more than one IdP before it can be forwarded to the upstream service. In such cases, you can configure multiple authentication plugins, each corresponding to an IdP, on one consumer; only when all IdPs have granted access to a request will APISIX show a success response.

With multiple authentication plugins in place, the [plugins order of execution](https://docs.api7.ai/apisix/key-concepts/plugins.md#plugins-execution-order) is determined by the plugin's priority, which can be overridden with [`_meta.priority`](https://docs.api7.ai/apisix/reference/plugin-common-configurations.md#_metapriority).

The second and a more basic approach is to perform authentication and authorization on the API gateway itself, using `key-auth`, `basic-auth`, `jwt-auth`, `hmac-auth` plugins:

![APISIX performs auth without IdP](https://static.api7.ai/uploads/2023/03/16/UGxTDGut_consumers-auth2.svg)

<br />

For details about how to configure authentication and authorization for your specific needs, please refer to the [authentication section](https://docs.api7.ai/apisix/how-to-guide/authentication/implement-basic-auth.md) in How-To Guides.

## Additional Resource(s)[â](#additional-resources "Direct link to Additional Resource(s)")

* Getting Started - [Configure Key Authentication](https://docs.api7.ai/apisix/getting-started/key-authentication.md)
* Admin API - [Consumer](https://docs.api7.ai/apisix/reference/admin-api/.md#tag/Consumer)
* [`consumer-restriction`](https://docs.api7.ai/hub/consumer-restriction.md) plugin
* Key Concepts - [Credentials](https://docs.api7.ai/apisix/key-concepts/credentials.md)
