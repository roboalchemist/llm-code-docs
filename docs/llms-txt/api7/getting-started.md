# Source: https://docs.api7.ai/enterprise/api-portal/getting-started.md

# Source: https://docs.api7.ai/cloud/getting-started.md

# Source: https://docs.api7.ai/apisix/getting-started.md

# Source: https://docs.api7.ai/cloud/getting-started.md

# Source: https://docs.api7.ai/apisix/getting-started.md

# Get APISIX

Apache APISIX is a dynamic, real-time, and high-performance API Gateway. It is a [top-level project](https://projects.apache.org/project.html?apisix) of the Apache Software Foundation.

You can use APISIX API Gateway as a traffic entrance to process all business data. It offers features including dynamic routing, dynamic upstream, dynamic certificates, A/B testing, canary release, blue-green deployment, limit rate, defense against malicious attacks, metrics, monitoring alarms, service observability, service governance, and more.

This tutorial covers one installation method for you to quickly get started with APISIX:

* Start APISIX in Docker with a quickstart script.

## Prerequisite(s)[â](#prerequisites "Direct link to Prerequisite(s)")

* Docker

- Install [Docker](https://docs.docker.com/get-docker/) to be used in the quickstart script to create containerized **etcd** and **APISIX**.
- Install [cURL](https://curl.se/) to be used in the quickstart script and to send requests to APISIX for verification.

## Get APISIX[â](#get-apisix "Direct link to Get APISIX")

* Docker

caution

To provide a better experience in this tutorial, the requirement of [Admin API key](https://docs.api7.ai/apisix/production/security/admin-api-key.md) is switched off by default. Please turn on the API key requirement of Admin API in the production environment.

Start APISIX in Docker with the quickstart script:

```
curl -sL "https://run.api7.ai/apisix/quickstart" | sh
```

The script starts two Docker containers, `apisix-quickstart` and `etcd-quickstart` in the `apisix-quickstart-net` Docker network, where etcd is used to store APISIX configurations.

You should see the following message once APISIX is ready:

```
â APISIX is ready!
```

## Verify Installation[â](#verify-installation "Direct link to Verify Installation")

* Docker

Send a request to see if APISIX is running:

```
curl -sI "http://127.0.0.1:9080" | grep Server
```

If everything is ok, you should see the APISIX version:

```
Server: APISIX/3.15.0
```

APISIX is now installed and running.

## Next Steps[â](#next-steps "Direct link to Next Steps")

Follow the rest of the getting started tutorials to learn and compare different ways of configuring APISIX, including using:

* Admin API
* [API Declarative CLI (ADC)](https://docs.api7.ai/apisix/reference/adc.md)
* [APISIX Model Context Protocol (APISIX-MCP)](https://docs.api7.ai/apisix/reference/apisix-mcp.md)

If you would like to declaratively configure APISIX with ADC, or use natural language through LLM models to configure APISIX with APISIX-MCP, please visit their docs for installation and setup before visiting the other tutorials.

Note that the APISIX instance started with the quickstart script is not optimized for production. For production installation, please see the [production installation options](https://docs.api7.ai/apisix/install/docker/.md) for more information.
