# Source: https://docs.api7.ai/cloud/overview/how-apisix-connects-to-api7-cloud.md

# How does Apache APISIX connect to API7 Cloud

In the [Overview](https://docs.api7.ai/cloud/overview/api7-cloud.md) section, we know the gateway solution of API7 Cloud is [Apache APISIX](https://apisix.apache.org/), API7 Cloud uses [the official Apache APISIX distributions](https://apisix.apache.org/downloads/) as the base, with an extra Lua module to communicate with API7 Cloud.

note

Currently, API7 Cloud only supports `APISIX/2.15.0` and above.

## The Data Flow[â](#the-data-flow "Direct link to The Data Flow")

The data flow between Apache APISIX and API7 Cloud is as follows:

1. Apache APISIX will periodically send [Prometheus](https://prometheus.io/) metrics and stats data (e.g., number of API calls) to API7 Cloud.
2. API7 Cloud will send the configuration changes to Apache APISIX (leverage the Apache APISIX configuration center).

## The Control Flow[â](#the-control-flow "Direct link to The Control Flow")

API7 Cloud only communicates with registered Apache APISIX instances. So before the data flow, Apache APISIX needs to register itself to API7 Cloud. After the initial registration, Apache APISIX will send periodic heartbeat probes (per `10s`) to keep it alive.

## How to check if the Apache APISIX instance is registered[â](#how-to-check-if-the-apache-apisix-instance-is-registered "Direct link to How to check if the Apache APISIX instance is registered")

You can see registered Apache APISIX instances on the API7 Cloud overview page (Gateway Instances section).

![Apache APISIX Status](https://static.api7.ai/uploads/2023/01/13/3IY9aEGa_gateway-instances.png)

tip

Learn [How to Deploy Apache APISIX](https://docs.api7.ai/cloud/guides/product/how-to-deploy-apache-apisix.md) for more details.

## The API7 Cloud Lua Module[â](#the-api7-cloud-lua-module "Direct link to The API7 Cloud Lua Module")

The Data Flow and Control Flow logics are not the standard parts of the open-source Apache APISIX, we implement them in a separate Lua module: [Cloud Lua Module](https://github.com/api7/cloud-scripts/tree/main/assets).

And thanks to the [Lua Module Hook](https://github.com/apache/apisix/blob/master/conf/config-default.yaml#L54) feature, we mount this module easily, without any modifications to the Apache APISIX core.

## The mTLS Support[â](#the-mtls-support "Direct link to The mTLS Support")

No matter the Data Flow or the Control Flow, the Apache APISIX instance can communicate with API7 Cloud securely with the support of [mTLS](https://en.wikipedia.org/wiki/Mutual_authentication). The certificate and private key can be downloaded from API7 Cloud and should configure for the Apache APISIX instance.

## The Cloud CLI[â](#the-cloud-cli "Direct link to The Cloud CLI")

Users don't have to do the above steps (mount the Cloud Lua Module and configure the certificate) manually as we use [Cloud CLI](https://github.com/api7/cloud-cli) to manipulate them. So the above steps are imperceptible to users.

## The Local Configuration Cache[â](#the-local-configuration-cache "Direct link to The Local Configuration Cache")

The Apache APISIX instances can still work normally even if they cannot connect to API7 Cloud. In such a case, they will use the configurations in the memory. But it'll be dangerous to reload instances as after the reload, the configurations inside memory will disappear.

So we use a local configuration cache to store the configurations to the disk, once the Apache APISIX instance watched a new configuration change, it will save the new configurations. When the Apache APISIX instance starts and cannot connect to API7 Cloud successfully, it will load the local configuration cache to the memory.

The local configuration feature is enabled by default, and the cache file is located at `/usr/local/apisix/conf/apisix.data`.

## What's Next[â](#whats-next "Direct link to What's Next")

* [Start using API7 Cloud](https://docs.api7.ai/cloud/getting-started/.md)
* [Learn How to use Cloud CLI to deploy Apache APISIX](https://github.com/api7/cloud-cli#introduction)
