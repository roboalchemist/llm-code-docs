# Source: https://docs.datadoghq.com/security/default_rules/znn-2vq-c2x.md

---
title: Private registry should use TLS encryption for a secure Docker environment
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Private registry should use TLS
  encryption for a secure Docker environment
---

# Private registry should use TLS encryption for a secure Docker environment
Classification:complianceFramework:cis-dockerControl:2.4 
## Description{% #description %}

Docker considers a private registry either secure or insecure. By default, registries are considered secure.

## Rationale{% #rationale %}

A secure registry uses TLS. A copy of the registry's CA certificate is placed on the Docker host in the `/etc/docker/certs.d/<registry-name>/` directory. An insecure registry is one which does not have a valid registry certificate, or one not not using TLS. You should not use insecure registries because they present a risk of traffic interception and modification. Additionally, once a registry has been marked as insecure, commands such as `docker pull`, `docker push`, and `docker search` will not result in an error message, and users may indefinitely be working with this type of insecure registry without ever being notified of the risk of potential compromise.

## Audit{% #audit %}

Find out if any insecure registries are in use by running:

```
docker info --format 'Insecure Registries: {{.RegistryConfig.InsecureRegistryCIDRs}}'
```

## Remediation{% #remediation %}

You should ensure that no insecure registries are in use.

## Impact{% #impact %}

None.

## Default value{% #default-value %}

By default, Docker assumes all registries except local ones are secure.

## References{% #references %}

1. [https://docs.docker.com/registry/insecure/](https://docs.docker.com/registry/insecure/)

## CIS controls{% #cis-controls %}

Version 6.14.2 Encrypt All Sensitive Information Over Less-trusted Networks - All communication of sensitive information over less-trusted networks should be encrypted. Whenever information flows over a network with a lower trust level, the information should be encrypted.

Version 7.14.4 Encrypt All Sensitive Information in Transit - Encrypt all sensitive information in transit.
