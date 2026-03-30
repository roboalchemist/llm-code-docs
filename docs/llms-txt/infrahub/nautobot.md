# Source: https://docs.infrahub.app/sync/adapters/nautobot.md

# Nautobot adapter

## What is Nautobot?[​](#what-is-nautobot "Direct link to What is Nautobot?")

Nautobot is an open-source network source of truth and automation platform, offering extended customization, plugin support, and enhanced functionality to simplify network documentation and operations.

## Requirements[​](#requirements "Direct link to Requirements")

This Adapter uses [Nautobot SDK](https://pypi.org/project/pynautobot). You will need to install it beforehand.

## Sync directions supported[​](#sync-directions-supported "Direct link to Sync directions supported")

* Nautobot → Infrahub

info

Currently, the Nautobot adapter supports only **one-way synchronization** from Nautobot to Infrahub. Syncing data back into Nautobot is not yet supported.

## Schema[​](#schema "Direct link to Schema")

Our `infrahub` repository contains an **example schema** that serves as a starting point for syncing Nautobot data into Infrahub. This schema follows best practices for Infrahub, **but it does not map the Nautobot data model one-to-one** since Infrahub may have additional use cases.

To reflect the breaking changes introduced in Nautobot v2, there is not one but two schemas. You can explore them to see the difference.

* Nautobot v1
* Nautobot v2

[Schema V1https://github.com/opsmill/infrahub/blob/stable/models/examples/nautobot/nautobot-v1.yml](https://github.com/opsmill/infrahub/blob/stable/models/examples/nautobot/nautobot-v1.yml)

[Schema V2https://github.com/opsmill/infrahub/blob/stable/models/examples/nautobot/nautobot-v2.yml](https://github.com/opsmill/infrahub/blob/stable/models/examples/nautobot/nautobot-v2.yml)

### Installing the example schema[​](#installing-the-example-schema "Direct link to Installing the example schema")

To install the example schema into Infrahub, follow these steps:

* Nautobot v1
* Nautobot v2

```
mkdir nautobot-sync
cd nautobot-sync
curl -o schema.yml https://raw.githubusercontent.com/opsmill/infrahub/refs/heads/stable/models/examples/nautobot/nautobot-v1.yml
infrahubctl schema load schema.yml
```

```
mkdir nautobot-sync
cd nautobot-sync
curl -o schema.yml https://raw.githubusercontent.com/opsmill/infrahub/refs/heads/stable/models/examples/nautobot/nautobot-v2.yml
infrahubctl schema load schema.yml
```

## Configuration[​](#configuration "Direct link to Configuration")

`infrahub-sync` allows defining what gets synchronized from a source to a destination. Included in the examples is a config.yml file that matches the example schema.

* Nautobot v1
* Nautobot v2

[config.ymlhttps://github.com/opsmill/infrahub-sync/blob/main/examples/nautobot-v1\_to\_infrahub/config.yml](https://github.com/opsmill/infrahub-sync/blob/main/examples/nautobot-v1_to_infrahub/config.yml)

[config.ymlhttps://github.com/opsmill/infrahub-sync/blob/main/examples/nautobot-v2\_to\_infrahub/config.yml](https://github.com/opsmill/infrahub-sync/blob/main/examples/nautobot-v2_to_infrahub/config.yml)

To download the example `config.yml`

* Nautobot v1
* Nautobot v2

```
curl https://raw.githubusercontent.com/opsmill/infrahub-sync/refs/heads/main/examples/nautobot-v1_to_infrahub/config.yml > config.yml
```

```
curl https://raw.githubusercontent.com/opsmill/infrahub-sync/refs/heads/main/examples/nautobot-v2_to_infrahub/config.yml > config.yml
```

### Configuration parameters[​](#configuration-parameters "Direct link to Configuration parameters")

To instruct `infrahub-sync` to use the Nautobot adapter, set `nautobot` in the direction 'name', you want to use for Peering Manager.

Below is a snippet from the example config.yml file:

* Source example

```
---
name: from-nautobot
source:
name: nautobot
settings:
    url: "https://<NAUTOBOT-ENDPOINT>"
    token: "<TOKEN>"
    verify_ssl: true # Default value
```

### Schema mapping[​](#schema-mapping "Direct link to Schema mapping")

The configuration file allows mapping Nautobot data to the Infrahub schema, which has been designed to loosely align with the Nautobot data model. Below is an example showing how to:

* Set the destination Infrahub model (`OrganizationGeneric` and `InfraPlatform`)
* Map source data from Nautobot (`dcim.manufacturers`, and `dcim.platforms`)
* Specify field mappings between Nautobot and Infrahub models

As you can see in this example, we can map several paths to the same Infrahub Model.

```
  - name: OrganizationGeneric
    mapping: dcim.manufacturers
    identifiers: ["name"]
    fields:
      - name: name
        mapping: name
      - name: description
        mapping: description
      - name: type
        static: "Manufacturer"

  - name: InfraPlatform
    mapping: dcim.platforms
    identifiers: ["name", "manufacturer"]
    fields:
      - name: name
        mapping: name
      - name: description
        mapping: description
      - name: napalm_driver
        mapping: napalm_driver
      - name: manufacturer
        mapping: manufacturer
        reference: OrganizationGeneric
```

The models available on Nautobot can be find in the `/api/schema/swagger-ui` of your instance.

[Nautobot API Docshttps://demo.nautobot.com/api/docs](https://demo.nautobot.com/api/docs)
