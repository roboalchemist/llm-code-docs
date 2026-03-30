# Source: https://docs.infrahub.app/sync/adapters/netbox.md

# NetBox adapter

## What is NetBox?[​](#what-is-netbox "Direct link to What is NetBox?")

NetBox is an open-source infrastructure resource management tool that centralizes and documents your network's devices, IP addresses, circuits, and connections using pre-configured models and automation for streamlined operations.

## Requirements[​](#requirements "Direct link to Requirements")

This Adapter uses [Netbox SDK](https://pypi.org/project/pynetbox). You will need to install it beforehand.

## Sync directions supported[​](#sync-directions-supported "Direct link to Sync directions supported")

* NetBox → Infrahub

info

Currently, the Netbox adapter supports only **one-way synchronization** from Netbox to Infrahub. Syncing data back into Netbox is not yet supported.

## Schema[​](#schema "Direct link to Schema")

Our `infrahub` repository contains an **example schema** that serves as a starting point for syncing Netbox data into Infrahub. This schema follows best practices for Infrahub, **but it does not map the Netbox data model one-to-one** since Infrahub may have additional use cases.

[Schemahttps://github.com/opsmill/infrahub/blob/stable/models/examples/netbox/netbox.yml](https://github.com/opsmill/infrahub/blob/stable/models/examples/netbox/netbox.yml)

### Installing the example schema[​](#installing-the-example-schema "Direct link to Installing the example schema")

To install the example schema into Infrahub, follow these steps:

```
mkdir netbox-sync
cd netbox-sync
curl -o schema.yml https://raw.githubusercontent.com/opsmill/infrahub/refs/heads/stable/models/examples/netbox/netbox.yml
infrahubctl schema load schema.yml
```

## Configuration[​](#configuration "Direct link to Configuration")

`infrahub-sync` allows defining what gets synchronized from a source to a destination. Included in the examples is a config.yml file that matches the example schema.

[config.ymlhttps://github.com/opsmill/infrahub-sync/blob/main/examples/netbox\_to\_infrahub/config.yml](https://github.com/opsmill/infrahub-sync/blob/main/examples/netbox_to_infrahub/config.yml)

To download the example `config.yml`

```
curl https://raw.githubusercontent.com/opsmill/infrahub-sync/refs/heads/main/examples/netbox_to_infrahub/config.yml > config.yml
```

### Configuration parameters[​](#configuration-parameters "Direct link to Configuration parameters")

To instruct `infrahub-sync` to use the Netbox adapter, set `netbox` in the direction 'name', you want to use for Peering Manager.

Below is a snippet from the example config.yml file:

* Source example

```
---
name: from-netbox
source:
name: netbox
settings:
    url: "https://<NETBOX-ENDPOINT>"
    token: "<TOKEN>"
    verify_ssl: true # Default value
```

### Schema mapping[​](#schema-mapping "Direct link to Schema mapping")

The configuration file allows mapping Netbox data to the Infrahub schema, which has been designed to loosely align with the Netbox data model. Below is an example showing how to:

* Set the destination Infrahub model (`BuiltinTag` and `LocationGeneric`)
* Map source data from Netbox (`extras.tags`, `dcim.regions`, and `dcim.sites`)
* Specify field mappings between Netbox and Infrahub models

As you can see in this example, we can map several paths to the same Infrahub Model.

```
  - name: BuiltinTag
    mapping: extras.tags
    identifiers: ["name"]
    fields:
      - name: name
        mapping: name
      - name: description
        mapping: description

  - name: LocationGeneric
    mapping: dcim.regions
    fields:
      - name: name
        mapping: slug
      - name: description
        mapping: name
      - name: type
        static: "Region"
      - name: tags
        mapping: tags
        reference: BuiltinTag

  - name: LocationGeneric
    mapping: dcim.sites
    fields:
      - name: name
        mapping: slug
      - name: description
        mapping: name
      - name: type
        static: "Site"
      - name: tags
        mapping: tags
        reference: BuiltinTag
```

The models available on Netbox can be find in the `/api/schema/swagger-ui` of your instance.

[Netbox API Swaggerhttps://demo.netbox.dev/api/schema/swagger-ui](https://demo.netbox.dev/api/schema/swagger-ui)
