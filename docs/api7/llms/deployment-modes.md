# Source: https://docs.api7.ai/apisix/production/deployment-modes.md

# Deployment Modes

You can deploy APISIX in three modes:

* [Traditional mode](#traditional-mode)
* [Decoupled mode](#decoupled-mode)
* [Standalone mode](#standalone-mode)

## Traditional Mode[â](#traditional-mode "Direct link to Traditional Mode")

In traditional mode, every APISIX instance runs as both a control plane and data plane. APISIX configurations are stored in etcd. The APISIX instance dynamically routes requests and responses, as well as interacts with etcd to synchronize configurations.

This example shows a sample configuration for deploying APISIX in traditional mode:

config.yaml

```
apisix:
  node_listen:
    - port: 9080
deployment:
  role: traditional
  role_traditional:
    config_provider: etcd
  admin:
    admin_listen:
      port: 9180
    admin_key_required: true
    allow_admin:
      - 127.0.0.0/24
    admin_key:
      -
        name: admin
        key: ${{CUSTOM_API_WRITE_KEY}}
        role: admin
      -
        name: viewer
        key: ${{CUSTOM_API_VIEW_KEY}}
        role: viewer
```

Running APISIX in traditional mode is the simplest way to get APISIX started and can reduce additional configuration management and overhead. However, there are some downsides too. As the responsibilities of data plane and control plane are not separate, deploying APISIX in traditional mode may not meet the production requirements in resiliency and availability.

## Decoupled Mode[â](#decoupled-mode "Direct link to Decoupled Mode")

In decoupled mode, APISIX instances are divided into two roles: data plane and control plane. The data plane is responsible for actual data like requests and responses flowing through the system. The control plane manages and orchestrates the whole system and sets rules and policies on how the data plane handles data.

This example shows a sample configuration for deploying APISIX as a data plane in decoupled mode:

config.yaml

```
deployment:
  role: data_plane
  role_data_plane:
    config_provider: etcd
```

This example shows a sample configuration for deploying APISIX as a control plane in decoupled mode:

config.yaml

```
deployment:
  role: control_plane
  role_control_plane:
    config_provider: etcd
  admin:
    admin_key_required: true
    allow_admin:
      - 127.0.0.0/24
    admin_key:
      -
        name: admin
        key: ${{CUSTOM_API_WRITE_KEY}}
        role: admin
      -
        name: viewer
        key: ${{CUSTOM_API_VIEW_KEY}}
        role: viewer 
```

Running APISIX in decoupled mode brings some benefits:

* **Improve scalability**

  Separation of the data plane and control plane allows both planes to operate independently without depending on one another. This independence enables the data plane to scale easily without impacting the control plane. This scalability ensures that a network architecture can seamlessly accommodate growth and increased data demands.

* **Improve security**

  Since the control plane and the data plane are decoupled, a security breach in one plane cannot be exposed to the other. If a control plane is offline, data planes will run using their last configuration. Additionally, decoupling makes it easier to introduce optimized security mechanisms separately for each plane.

* **Optimize performance**

  Both planes perform distinct functionalities independently. The separation of layers enables each plane to concentrate on optimizing its specific tasks. For instance, the control plane can prioritize efficient routing and decision-making. Meanwhile, the data plane can focus on swift and effective packet forwarding and enhancing network performance.

While decoupling control planes and data planes provides many benefits, it also introduces some challenges and drawbacks.

* **Increase latency**

  While the decoupled planes work independently from one another, they still need to communicate with each other to take instructions and perform their tasks. It can lead to increased latency, especially in distributed architectures, introducing delays for packet transmission through the networks.

* **Increase complexity**

  Decoupling control planes and data planes can also increase additional configuration management and overhead. It requires significant skills and expertise to operate such two separate planes. Finding such expertise can be challenging and costly.

For details about how to get started with APISIX in decoupled mode, see [Install APISIX in decoupled mode using Docker](https://docs.api7.ai/apisix/install/docker/.md#decoupled-mode).

## Standalone Mode[â](#standalone-mode "Direct link to Standalone Mode")

In standalone mode, APISIX operates solely as the data plane. It can either load configurations from [`apisix.yaml`](https://docs.api7.ai/apisix/reference/configuration-files.md#apisixyaml) in file-driven mode or receive configurations through the standalone Admin API, storing them entirely in memory.

### File-Driven[â](#file-driven "Direct link to File-Driven")

This example shows a sample configuration for deploying APISIX in file-driven standalone mode:

config.yaml

```
apisix:
  enable_admin: false
deployment:
  role: data_plane
  role_data_plane:
    config_provider: yaml   # yaml or json
```

The combination of standalone mode and declarative configuration has a number of benefits:

* **Reduce complexity**

  You do not need to install and manage the etcd. In this mode, all APISIX configurations are stored in-memory on the node.

* **Consolidate your APISIX configurations**

  All APISIX configurations are kept in a single source of truths to reduce the possibility of errors and even simplify configuration management.

For details about how to get started with APISIX in file-driven standalone mode, see [Install APISIX in standalone mode using Docker](https://docs.api7.ai/apisix/install/docker/.md#standalone-mode).

For details about how to configure APISIX, see [File-Driven Standalone configurations](https://docs.api7.ai/apisix/reference/file-standalone-configurations.md).

### API-Driven[â](#api-driven "Direct link to API-Driven")

API-driven mode is a recent addition to APISIXâs standalone deployment model. In this mode, routing rules are stored entirely in memory rather than in a configuration file. All updates must be performed through the dedicated standalone Admin API. Each update replaces the full configuration and takes effect immediately through a hot update, without requiring a gateway restart.

caution

This feature is designed specifically for the APISIX Ingress Controller and is primarily intended for integration with ADC. APISIX provides an official, end-to-end, stateless Ingress Controller implementation. Do not use this feature directly unless you fully understand its internal workings and behavior.

This example shows a sample configuration for deploying APISIX in API-driven standalone mode. It sets the APISIX role to `traditional` (to start both the gateway and the API-driven Admin API and use the YAML config provider:

config.yaml

```
deployment:
  role: traditional
  role_traditional:
    config_provider: yaml
```

This disables the local file-based configuration source in favor of the API. When APISIX starts, it awaits configuration updates through the API.

For details about how to work with the standalone Admin API, see [API-Driven Standalone configurations](https://docs.api7.ai/apisix/reference/api-standalone-usage.md).
