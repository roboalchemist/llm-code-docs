# Source: https://docs.datadoghq.com/security/default_rules/8r2-zyy-shg.md

---
title: Containers on the default network bridge should restrict network traffic
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Containers on the default network
  bridge should restrict network traffic
---

# Containers on the default network bridge should restrict network traffic
Classification:complianceFramework:cis-dockerControl:2.1 
## Description{% #description %}

By default, all network traffic is allowed between containers on the same host on the default network bridge. You can restrict all inter-container communication and link specific containers together that require communication. Or, you can create a custom network and only join containers that need to communicate to that custom network.

## Rationale{% #rationale %}

By default, unrestricted network traffic is enabled between all containers on the same host on the default network bridge. Each container has the potential of reading all packets across the container network on the same host. This might lead to an unintended and unwanted disclosure of information to other containers. Hence, restrict inter-container communication on the default network bridge.

## Audit{% #audit %}

Verify that the default network bridge has been configured to restrict inter-container communication by running:

```
docker network ls --quiet | xargs docker network inspect --format '{{ .Name }}: {{ .Options }}' 
```

Check that it returns `com.docker.network.bridge.enable_icc:false` for the default network bridge.

## Remediation{% #remediation %}

Edit the Docker daemon configuration file to ensure that inter-container communication is disabled:

```
"icc": false
```

Alternatively, run the Docker daemon directly and pass `--icc=false` as an argument:

```
dockerd --icc=false 
```

Follow the Docker documentation and create a custom network, and only join containers that need to communicate to that custom network. The `--icc` parameter only applies to the default docker bridge. If you use a custom network, adopt the segmenting networks approach instead.

## Impact{% #impact %}

Inter-container communication is disabled on the default network bridge. If any communication between containers on the same host is desired, it needs to be explicitly defined using container linking or custom networks.

## Default value{% #default-value %}

By default, all inter-container communication is allowed on the default network bridge.

## References{% #references %}

1. [https://docs.docker.com/engine/userguide/networking/](https://docs.docker.com/engine/userguide/networking/)
1. [https://docs.docker.com/engine/userguide/networking/default_network/container-communication/#communication-between-containers](https://docs.docker.com/engine/userguide/networking/default_network/container-communication/#communication-between-containers)

## CIS controls{% #cis-controls %}

None
