# Source: https://docs.infrahub.app/sync/adapters/peering-manager.md

# Peering Manager adapter

## What is Peering Manager?[​](#what-is-peering-manager "Direct link to What is Peering Manager?")

Peering Manager lets you effortlessly manage and document your network’s peering sessions and interconnections with pre-configured data models and automation for seamless BGP session management.

## Sync directions supported[​](#sync-directions-supported "Direct link to Sync directions supported")

* Peering Manager → Infrahub
* Infrahub → Peering Manager

## Schema[​](#schema "Direct link to Schema")

Our `infrahub` repository contains an **example schema** that serves as a starting point for syncing Peering Manager data into Infrahub. This schema follows best practices for Infrahub, **but it does not map the Peering Manager data model one-to-one** since Infrahub may have additional use cases.

This example is using the "base" demo schema and use an extension for Peering Manager.

[Base Schemahttps://github.com/opsmill/infrahub/blob/stable/models/base/](https://github.com/opsmill/infrahub/blob/stable/models/base/) [Peering Manager Extensionhttps://github.com/opsmill/infrahub/blob/stable/models/examples/extension\_peering\_manager.yml](https://github.com/opsmill/infrahub/blob/stable/models/examples/extension_peering_manager.yml)

### Installing the example schema[​](#installing-the-example-schema "Direct link to Installing the example schema")

To install the example schema into Infrahub, follow these steps:

```
mkdir peeringmanager-sync
cd peeringmanager-sync

# Fetch the list of YAML file names from the peeringmanager folder
curl -s "https://api.github.com/repos/opsmill/infrahub/contents/models/base?ref=stable" | jq -r '.[].name | select(endswith(".yml"))' | while read file; do
  curl -O "https://raw.githubusercontent.com/opsmill/infrahub/refs/heads/stable/models/base/$file"
done
curl -O "https://raw.githubusercontent.com/opsmill/infrahub/refs/heads/stable/models/examples/extension_peering_manager.yml"

infrahubctl schema load *.yml
```

## Configuration[​](#configuration "Direct link to Configuration")

`infrahub-sync` allows defining what gets synchronized from a source to a destination. Included in the examples there is two `config.yml` files that matches the example schema.

[Source config.ymlhttps://github.com/opsmill/infrahub-sync/blob/main/examples/peering-manager\_to\_infrahub/config.yml](https://github.com/opsmill/infrahub-sync/blob/main/examples/peering-manager_to_infrahub/config.yml) [Destination config.ymlhttps://github.com/opsmill/infrahub-sync/blob/main/examples/infrahub\_to\_peering-manager/config.yml](https://github.com/opsmill/infrahub-sync/blob/main/examples/infrahub_to_peering-manager/config.yml)

To download those examples `config.yml`

peering-manager to infrahub

```
curl https://raw.githubusercontent.com/opsmill/infrahub-sync/refs/heads/main/examples/peering-manager_to_infrahub/config.yml > config.yml
```

infrahub to peering-manager

```
curl https://raw.githubusercontent.com/opsmill/infrahub-sync/refs/heads/main/examples/infrahub_to_peering-manager/config.yml > config.yml
```

### Configuration parameters[​](#configuration-parameters "Direct link to Configuration parameters")

To instruct `infrahub-sync` to use the Peering Manager adapter, set `peeringmanager` in the direction 'name', you want to use for Peering Manager.

The settings dictionary is passed directly to the REST API client for Peering Manager for authentication and connection details.

Below is a snippet from the example config.yml file:

* Source example
* Destination example

```
---
name: from-peering-manager
source:
name: peeringmanager
settings:
    url: "https://<PEERING-MANAGER-ENDPOINT>"
    api_endpoint: "api" # Default value
    auth_method: "token" # Default value
    # auth_method: "token"
    token: "<TOKEN>"
```

```
---
name: to-peering-manager
destination:
name: peeringmanager
settings:
    url: "https://<PEERING-MANAGER-ENDPOINT>"
    api_endpoint: "api" # Default value
    auth_method: "token" # Default value
    # auth_method: "token"
    token: "<TOKEN>"
    verify_ssl: true # Default value
```

info

You can pass `params` for the REST API client, used by Peering Manager adapter, in the settings. For example `limit`

### Schema mapping[​](#schema-mapping "Direct link to Schema mapping")

The configuration file allows mapping tables from PeeringManager into Infrahub models. Below is an example showing how to:

* Set the destination Infrahub model (`InfraBGPCommunity`)
* Map source data from Peering Manager (`peering/communities`)
* Specify field mappings between Peering Manager and Infrahub models

```
  - name: InfraBGPCommunity
    mapping: peering/communities
    identifiers: ["name"]
    fields:
      - name: name
        mapping: slug
      - name: label
        mapping: name
      - name: description
        mapping: description
      - name: value
        mapping: value
      - name: community_type
        mapping: type
```

The models available on Peering Manager can be find in the /api of your instance.

[Peering Manager API Swaggerhttps://demo.peering-manager.net/api/schema/swagger-ui](https://demo.peering-manager.net/api/schema/swagger-ui)

![Peering Manager API Example](/assets/images/peering-manager-api-8c7c5220752c321dbe43bd8aac08f78f.png)
