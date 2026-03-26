# Source: https://docs.api7.ai/apisix/reference/api-standalone-usage.md

# API-Driven Standalone Mode Usage

[API-driven standalone mode](https://docs.api7.ai/apisix/production/deployment-modes.md#api-driven) is a recent addition to APISIXâs standalone deployment model. In this mode, routing rules are stored entirely in memory rather than in a configuration file. All updates must be performed through the dedicated standalone Admin API. Each update replaces the full configuration and takes effect immediately through a hot update, without requiring a gateway restart.

caution

This feature is designed specifically for the APISIX Ingress Controller and is primarily intended for integration with ADC. APISIX provides an official, end-to-end, stateless Ingress Controller implementation. Do not use this feature directly unless you fully understand its internal workings and behavior.

This document provides a few examples for using APISIX in API-driven standalone mode. To learn more about the available configuration options, see the [Admin API reference](https://docs.api7.ai/apisix/reference/admin-api/.md) (but do not use these endpoints). These configuration options can be translated into JSON or YAML for use in API-driven standalone mode.

## Examples[â](#examples "Direct link to Examples")

In API-driven standalone mode, you will be working with the `/apisix/admin/configs` API, instead of the traditional mode Admin API endpoints. The API accepts both JSON and YAML inputs.

The standalone mode Admin API has the same security requirements as the traditional mode Admin API configured in the `config.yaml`, including API key, (m)TLS, CORS, and IP allowlist.

### Get All Configurations[â](#get-all-configurations "Direct link to Get All Configurations")

To get all configurations:

```
curl "http://127.0.0.1:9180/apisix/admin/configs" -H "X-API-KEY: ${ADMIN_API_KEY}"
```

If you have no resource configured, you should see the following response:

```
{
  "consumer_groups_conf_version": 0,
  "secrets_conf_version": 0,
  "global_rules_conf_version": 0,
  "upstreams_conf_version": 0,
  "ssls_conf_version": 0,
  "protos_conf_version": 0,
  "plugin_metadata_conf_version": 0,
  "routes_conf_version": 0,
  "services_conf_version": 0,
  "plugin_configs_conf_version": 0,
  "consumers_conf_version": 0
}
```

### Create a Resource[â](#create-a-resource "Direct link to Create a Resource")

For instance, to create a route:

```
curl -i -X PUT "http://127.0.0.1:9180/apisix/admin/configs" \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '
    {
      "routes": [
        {
          "id": "getting-started-ip",
          "uri": "/ip",
          "upstream": {
            "type": "roundrobin",
            "nodes": {
              "httpbin.org:80": 1
            }
          }
        }
      ]
    }'
```

Alternatively, you can also use the YAML input:

```
curl -X PUT "http://127.0.0.1:9180/apisix/admin/configs" \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -H "Content-Type: application/yaml" \
  --data-binary @- <<EOF
routes:
  - id: getting-started-ip
    uri: /ip
    upstream:
      type: roundrobin
      nodes:
        "httpbin.org:80": 1
EOF
```

You should receive an `HTTP/1.1 202 Accepted` response.

Now when you review the change by [getting all configurations](#get-all-configurations), you should see the `*_conf_version` has automatically increased by 1.

### Update a Resource[â](#update-a-resource "Direct link to Update a Resource")

In the API-driven mode, there are two version trackers APISIX uses to manage updates:

* `*_conf_version`: Configuration version of a resource type.
* `modifiedIndex`: Modified index of a resource in a resource type.

For instance, routes with the same `routes_conf_version` can have different `modifiedIndex`.

The update rules of `*_conf_version` and `modifiedIndex` are evaluated in the following logic:

<!-- -->

Suppose you send an update of a route with an upstream as such:

```
curl -X PUT "http://127.0.0.1:9180/apisix/admin/configs" \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '
    {
      "routes_conf_version": 2000,
      "routes": [
        {
          "modifiedIndex": 1,
          "id": "ip",
          "uri": "/ip",
          "upstream_id": "u1"
        }
      ],
      "upstreams_conf_version": 2000,
      "upstreams": [
        {
          "modifiedIndex": 1,
          "id": "u1",
          "nodes": {
            "127.0.0.1:1980": 1,
            "127.0.0.1:2980": 1
          },
          "type": "roundrobin"
        }
      ]
    }'
```

When [getting all configurations](#get-all-configurations), you should see a response similar to the following:

```
{
  "upstreams": [
    {
      "id": "u1",
      "type": "roundrobin",
      "modifiedIndex": 1,
      "nodes": {
        "127.0.0.1:2980": 1,
        "127.0.0.1:1980": 1
      }
    }
  ],
  "ssls_conf_version": 2,
  "upstreams_conf_version": 2000,
  "routes": [
    {
      "id": "ip",
      "upstream_id": "u1",
      "modifiedIndex": 1,
      "uri": "/ip"
    }
  ],
  "protos_conf_version": 2,
  "consumers_conf_version": 2,
  "services_conf_version": 2,
  "plugin_configs_conf_version": 2,
  "plugin_metadata_conf_version": 2,
  "consumer_groups_conf_version": 2,
  "secrets_conf_version": 2,
  "global_rules_conf_version": 2,
  "routes_conf_version": 2000
}
```

Now if you increase the `upstreams_conf_version`, update `modifiedIndex` and node address of the upstream, update the route URI while keeping `routes_conf_version` unchanged:

```
curl -X PUT "http://127.0.0.1:9180/apisix/admin/configs" \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '
    {
      "routes_conf_version": 2000,
      "routes": [
        {
          "modifiedIndex": 1,
          "id": "ip",
          "uri": "/new-ip",
          "upstream_id": "u1"
        }
      ],
      "upstreams_conf_version": 2001,
      "upstreams": [
        {
          "modifiedIndex": 5,
          "id": "u1",
          "nodes": {
            "127.0.0.1:1980": 1,
            "127.0.0.1:3980": 1
          },
          "type": "roundrobin"
        }
      ]
    }'
```

When [getting all configurations](#get-all-configurations), you should see a response similar to the following, while route configuration is unchanged and upstream has been updated:

```
{
  "upstreams": [
    {
      "id": "u1",
      "type": "roundrobin",
      "modifiedIndex": 5,
      "nodes": {
        "127.0.0.1:3980": 1,
        "127.0.0.1:1980": 1
      }
    }
  ],
  "services_conf_version": 3,
  "plugin_configs_conf_version": 3,
  "plugin_metadata_conf_version": 3,
  "consumer_groups_conf_version": 3,
  "secrets_conf_version": 3,
  "routes": [
    {
      "id": "ip",
      "uri": "/ip",
      "modifiedIndex": 1,
      "upstream_id": "u1"
    }
  ],
  "upstreams_conf_version": 2001,
  "routes_conf_version": 2000,
  "consumers_conf_version": 3,
  "ssls_conf_version": 3,
  "global_rules_conf_version": 3,
  "protos_conf_version": 3
}
```

### Clear All Resources[â](#clear-all-resources "Direct link to Clear All Resources")

To clear all resources:

```
curl -X PUT "http://127.0.0.1:9180/apisix/admin/configs" \
  -H "X-API-KEY: ${ADMIN_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{}'
```

Note that this operation does not reset the `*_conf_version`. They will continue to increment.
