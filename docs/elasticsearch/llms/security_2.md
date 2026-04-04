# Source: https://www.elastic.co/docs/deploy-manage/security

﻿---
title: Security
description: An Elastic implementation comprises many moving parts: Elasticsearch nodes forming the cluster, Kibana instances, additional stack components such as...
url: https://www.elastic.co/docs/deploy-manage/security
products:
  - Elastic Cloud Enterprise
  - Elastic Cloud Hosted
  - Elastic Cloud Serverless
  - Elastic Cloud on Kubernetes
  - Elasticsearch
  - Kibana
applies_to:
  - Elastic Cloud Serverless: Generally available
  - Elastic Cloud Hosted: Generally available
  - Elastic Cloud on Kubernetes: Generally available
  - Elastic Cloud Enterprise: Generally available
  - Self-managed Elastic deployments: Generally available
---

# Security
An Elastic implementation comprises many moving parts: Elasticsearch nodes forming the cluster, Kibana instances, additional stack components such as Logstash and Beats, and various clients and integrations, all communicating with your cluster.
To keep your data secured, Elastic offers security features that prevent bad actors from tampering with your data, and encrypt communications to, from, and within your cluster. Regardless of your deployment type, Elastic sets up certain security features for you automatically.
The availability and configurability of security features vary by deployment type. On every page, you'll see deployment type indicators that show which content applies to specific deployment types. Focus on sections tagged with your deployment type and look for subsections specifically addressing your deployment model. You can also review a [comparison table](#comparison-table) showing feature availability and configurability by deployment type.
<note>
  As part of your overall security strategy, you can also do the following:
  - Prevent unauthorized access with [password protection and role-based access control](https://www.elastic.co/docs/deploy-manage/users-roles).
  - Control access to dashboards and other saved objects in your UI using [Spaces](https://www.elastic.co/docs/deploy-manage/manage-spaces).
  - Connect a local cluster to a [remote cluster](https://www.elastic.co/docs/deploy-manage/remote-clusters) to enable [cross-cluster replication](https://www.elastic.co/docs/deploy-manage/tools/cross-cluster-replication) and [cross-cluster search](https://www.elastic.co/docs/explore-analyze/cross-cluster-search).
  - Manage [API keys](https://www.elastic.co/docs/deploy-manage/api-keys) used for programmatic access to Elastic.
</note>


## Managed security in Elastic Cloud

<applies-to>
  - Elastic Cloud Serverless: Generally available
  - Elastic Cloud Hosted: Generally available
</applies-to>

Elastic Cloud has built-in security. For example, HTTPS communications between Elastic Cloud and the internet, as well as inter-node communications, are secured automatically, and cluster data is encrypted at rest.
In both Elastic Cloud Hosted and Elastic Cloud Serverless, you can augment these security features in the following ways:
- Configure [IP filters](https://www.elastic.co/docs/deploy-manage/security/ip-filtering-cloud) to prevent unauthorized access to your deployments and projects.
- [Configure private connectivity and apply VPC filtering](https://www.elastic.co/docs/deploy-manage/security/private-connectivity) to establish a secure connection for your deployments or projects and restrict traffic based on those private connections. Serverless supports AWS PrivateLink only; Elastic Cloud Hosted supports AWS PrivateLink, Azure Private Link, and GCP Private Service Connect.

In Elastic Cloud Hosted, you can also:
- Encrypt your deployment with a [customer-managed encryption key](https://www.elastic.co/docs/deploy-manage/security/encrypt-deployment-with-customer-managed-encryption-key).
- [Secure your settings](https://www.elastic.co/docs/deploy-manage/security/secure-settings) using Elasticsearch and Kibana keystores.
- Use the list of [Elastic Cloud static IPs](https://www.elastic.co/docs/deploy-manage/security/elastic-cloud-static-ips) to allow or restrict communications in your infrastructure.

Elastic Cloud Hosted doesn't support custom SSL certificates, which means that a custom CNAME for an Elastic Cloud Hosted endpoint such as *mycluster.mycompanyname.com* also is not supported.
Refer to [Elastic Cloud security](https://www.elastic.co/cloud/security) for more details about Elastic security and privacy programs.

## Securing your orchestrator

<applies-to>
  - Elastic Cloud on Kubernetes: Generally available
  - Elastic Cloud Enterprise: Generally available
</applies-to>

When running Elastic Stack applications on Elastic Cloud Enterprise or Elastic Cloud on Kubernetes, you must also secure the [orchestration layer](/docs/deploy-manage/deploy#who-manages-the-infrastructure) responsible for deploying and managing your Elastic products.
Learn about securing the following components:
- [An Elastic Cloud Enterprise installation](https://www.elastic.co/docs/deploy-manage/security/secure-your-elastic-cloud-enterprise-installation)
- [An Elastic Cloud on Kubernetes operator](https://www.elastic.co/docs/deploy-manage/security/secure-your-eck-installation)

<tip>
  Elastic secures your [Elastic Cloud](https://www.elastic.co/docs/deploy-manage/deploy/elastic-cloud) orchestrator for you.
</tip>


## Cluster or deployment security features

<applies-to>
  - Elastic Cloud Hosted: Generally available
  - Elastic Cloud on Kubernetes: Generally available
  - Elastic Cloud Enterprise: Generally available
  - Self-managed Elastic deployments: Generally available
</applies-to>

You can configure the following aspects of your Elastic cluster or deployment to maintain and enhance security:

### Initial security setup

Elasticsearch security features unlock key capabilities such as [authentication and authorization](https://www.elastic.co/docs/deploy-manage/users-roles), TLS encryption, and other security-related functionality described in this section. The first step in securing your deployment is to ensure that the Elasticsearch security features are enabled and properly configured.
For self-managed deployments, security features are automatically configured when possible. To learn about the automatic configuration process, the cases where automatic configuration might be skipped, and how to manually configure security, refer to [Set up security in self-managed deployments](https://www.elastic.co/docs/deploy-manage/security/self-setup).
<tip>
  If you want to use your own TLS certificates, then you should manually configure security.
</tip>

Deployments managed by Elastic Cloud on Kubernetes, Elastic Cloud Enterprise, Elastic Cloud Hosted, as well as Elastic Cloud Serverless projects, automatically configure security by default. This includes setting the `elastic` user password, generating TLS certificates, and configuring Kibana to connect to Elasticsearch securely. Disabling security is not supported in these deployment types.

### Communication and network security

- [Manage TLS certificates](https://www.elastic.co/docs/deploy-manage/security/secure-cluster-communications): TLS certificates apply security controls to network communications. Elastic uses TLS certificates to secure communications in two places:
  - **The HTTP layer**: Used for communication between your cluster or deployment and the internet.
- **The transport layer**: Used mainly for inter-node communications, and in certain cases for cluster to cluster communication.
- In self-managed Elasticsearch clusters, you can also [Configure Kibana and Elasticsearch to use mutual TLS](https://www.elastic.co/docs/deploy-manage/security/kibana-es-mutual-tls).
- [Enable cipher suites for stronger encryption](https://www.elastic.co/docs/deploy-manage/security/enabling-cipher-suites-for-stronger-encryption): The TLS and SSL protocols use a cipher suite that determines the strength of encryption used to protect the data. You may want to enable the use of additional cipher suites, so you can use different cipher suites for your TLS communications or communications with authentication providers.
- [Add network security policies](https://www.elastic.co/docs/deploy-manage/security/network-security): Network security allows you to limit how your deployments or projects can be accessed. Add another layer of security to your installation and deployments by restricting inbound traffic to only the sources that you trust. In both Elastic Cloud Hosted deployments and Serverless projects, you can restrict access based on IP addresses or CIDR ranges. You can also secure connectivity through private link services and filter traffic using VPC filters: Elastic Cloud Hosted supports AWS PrivateLink, Azure Private Link, and GCP Private Service Connect; Serverless supports AWS PrivateLink only.
- [Allow or deny Elastic Cloud Hosted IP ranges](https://www.elastic.co/docs/deploy-manage/security/elastic-cloud-static-ips): Elastic Cloud publishes a list of IP addresses used by its Elastic Cloud Hosted services for both incoming and outgoing traffic. Users can use these lists to configure their network firewalls as needed to allow or restrict traffic related to Elastic Cloud Hosted services.


### Data security

- [Secure your settings](https://www.elastic.co/docs/deploy-manage/security/secure-settings): Some of the settings that you configure in Elastic are sensitive, such as passwords, and relying on file system permissions to protect these settings is insufficient. Learn how to configure secure settings in the Elasticsearch keystore or Kibana keystore.
- [Secure saved objects](https://www.elastic.co/docs/deploy-manage/security/secure-saved-objects): Kibana stores entities such as dashboards, visualizations, alerts, actions, and advanced settings as saved objects, which are kept in a dedicated, internal Elasticsearch index. If such an object includes sensitive information, for example a PagerDuty integration key or email server credentials used by the alert action, Kibana encrypts it and makes sure it cannot be accidentally leaked or tampered with. You can configure and rotate the saved object encryption key for additional security.
- [Encrypt data at rest](https://www.elastic.co/docs/deploy-manage/security/data-security): By default, Elastic Cloud already encrypts your Elastic Cloud Hosted deployment data, Serverless project data, and snapshots at rest. If you’re using ECH, then you can reinforce this mechanism by providing your own encryption key, also known as [Bring Your Own Key (BYOK)](https://www.elastic.co/docs/deploy-manage/security/encrypt-deployment-with-customer-managed-encryption-key).
  <note>
  Other deployment types don’t implement encryption at rest out of the box. For self-managed clusters, to implement encryption at rest, the hosts running the cluster must be configured with disk-level encryption, such as `dm-crypt`. In addition, snapshot targets must ensure that data is encrypted at rest as well.Configuring `dm-crypt` or similar technologies is outside the scope of this documentation, and issues related to disk encryption are outside the scope of support.
  </note>


### User session security

[Manage Kibana sessions](https://www.elastic.co/docs/deploy-manage/security/kibana-session-management) to control the timeout and lifespan of logged-in sessions to Kibana, as well as the number of concurrent sessions each user can have.

### Security event audit logging

Audit logging is a powerful feature that helps you monitor and track security-related events within the Elastic Stack. By enabling audit logs, you can gain visibility into authentication attempts, authorization decisions, and other system activity.
Audit logging also provides forensic evidence in the event of an attack, and can be enabled independently for Elasticsearch and Kibana.
[Learn how to enable audit logging](https://www.elastic.co/docs/deploy-manage/security/logging-configuration/security-event-audit-logging).

### Security features by deployment type

Security feature availability varies by deployment type, with each feature having one of the following statuses:

| Status            | Description                                                                   |
|-------------------|-------------------------------------------------------------------------------|
| **Fully managed** | Handled automatically by Elastic with no user configuration needed            |
| **Managed**       | Handled automatically by Elastic, but certain configuration allowed           |
| **Configurable**  | Built-in feature that needs your configuration (like IP filters or passwords) |
| **N/A**           | Not available for this deployment type                                        |

Select your deployment type below to see what's available and how implementation responsibilities are distributed:
<applies-switch>
  <applies-item title="ess:" applies-to="Elastic Cloud Hosted: Generally available">
    | Category          | Security feature                       | Status        | Notes                                                                                                                                               |
    |-------------------|----------------------------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
    | **Communication** | TLS (HTTP layer)                       | Fully managed | Automatically configured by Elastic                                                                                                                 |
    |                   | TLS (Transport layer)                  | Fully managed | Automatically configured by Elastic                                                                                                                 |
    | **Network**       | IP filtering                           | Configurable  | [Configure IP-based access restrictions](https://www.elastic.co/docs/deploy-manage/security/ip-filtering-cloud)                                     |
    |                   | Private connectivity and VPC filtering | Configurable  | [Private connectivity](https://www.elastic.co/docs/deploy-manage/security/private-connectivity)                                                     |
    |                   | Kubernetes network policies            | N/A           |                                                                                                                                                     |
    | **Data**          | Encryption at rest                     | Managed       | You can [bring your own encryption key](https://www.elastic.co/docs/deploy-manage/security/encrypt-deployment-with-customer-managed-encryption-key) |
    |                   | Secure settings                        | Configurable  | [Configure secure settings](https://www.elastic.co/docs/deploy-manage/security/secure-settings)                                                     |
    |                   | Saved object encryption                | Fully managed | Automatically encrypted by Elastic                                                                                                                  |
    | **User session**  | Kibana sessions                        | Configurable  | [Customize session parameters](https://www.elastic.co/docs/deploy-manage/security/kibana-session-management)                                        |
  </applies-item>

  <applies-item title="serverless:" applies-to="Elastic Cloud Serverless: Generally available">
    | Category          | Security feature                       | Status        | Notes                                                                                                                  |
    |-------------------|----------------------------------------|---------------|------------------------------------------------------------------------------------------------------------------------|
    | **Communication** | TLS (HTTP layer)                       | Fully managed | Automatically configured by Elastic                                                                                    |
    |                   | TLS (Transport layer)                  | Fully managed | Automatically configured by Elastic                                                                                    |
    | **Network**       | IP filtering                           | Configurable  | [Configure IP-based access restrictions](https://www.elastic.co/docs/deploy-manage/security/ip-filtering-cloud)        |
    |                   | Private connectivity and VPC filtering | Configurable  | [Private connectivity](https://www.elastic.co/docs/deploy-manage/security/private-connectivity) (AWS PrivateLink only) |
    |                   | Kubernetes network policies            | N/A           |                                                                                                                        |
    | **Data**          | Encryption at rest                     | Fully managed | Automatically encrypted by Elastic                                                                                     |
    |                   | Secure settings                        | N/A           |                                                                                                                        |
    |                   | Saved object encryption                | Fully managed | Automatically encrypted by Elastic                                                                                     |
    | **User session**  | Kibana sessions                        | Fully managed | Automatically configured by Elastic                                                                                    |
  </applies-item>

  <applies-item title="ece:" applies-to="Elastic Cloud Enterprise: Generally available">
    | Category          | Security feature                       | Status        | Notes                                                                                                                                                                      |
    |-------------------|----------------------------------------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | **Communication** | TLS (HTTP layer)                       | Managed       | You can [configure custom certificates](https://www.elastic.co/docs/deploy-manage/security/secure-your-elastic-cloud-enterprise-installation/manage-security-certificates) |
    |                   | TLS (Transport layer)                  | Fully managed | Automatically configured by Elastic                                                                                                                                        |
    | **Network**       | IP filtering                           | Configurable  | [Configure IP-based access restrictions](https://www.elastic.co/docs/deploy-manage/security/ip-filtering-cloud)                                                            |
    |                   | Private connectivity and VPC filtering | N/A           |                                                                                                                                                                            |
    |                   | Kubernetes network policies            | N/A           |                                                                                                                                                                            |
    | **Data**          | Encryption at rest                     | N/A           |                                                                                                                                                                            |
    |                   | Secure settings                        | Configurable  | [Configure secure settings](https://www.elastic.co/docs/deploy-manage/security/secure-settings)                                                                            |
    |                   | Saved object encryption                | Configurable  | [Enable encryption for saved objects](https://www.elastic.co/docs/deploy-manage/security/secure-saved-objects)                                                             |
    | **User session**  | Kibana sessions                        | Configurable  | [Customize session parameters](https://www.elastic.co/docs/deploy-manage/security/kibana-session-management)                                                               |
  </applies-item>

  <applies-item title="eck:" applies-to="Elastic Cloud on Kubernetes: Generally available">
    | Category          | Security feature                       | Status       | Notes                                                                                                           |
    |-------------------|----------------------------------------|--------------|-----------------------------------------------------------------------------------------------------------------|
    | **Communication** | TLS (HTTP layer)                       | Managed      | [Multiple options](https://www.elastic.co/docs/deploy-manage/security/k8s-https-settings) for customization     |
    |                   | TLS (Transport layer)                  | Managed      | [Multiple options](https://www.elastic.co/docs/deploy-manage/security/k8s-transport-settings) for customization |
    | **Network**       | IP filtering                           | Configurable | [Configure IP-based access restrictions](https://www.elastic.co/docs/deploy-manage/security/ip-filtering-basic) |
    |                   | Private connectivity and VPC filtering | N/A          |                                                                                                                 |
    |                   | Kubernetes network policies            | Configurable | [Apply network policies to your Pods](https://www.elastic.co/docs/deploy-manage/security/k8s-network-policies)  |
    | **Data**          | Encryption at rest                     | N/A          |                                                                                                                 |
    |                   | Secure settings                        | Configurable | [Configure secure settings](https://www.elastic.co/docs/deploy-manage/security/k8s-secure-settings)             |
    |                   | Saved object encryption                | Configurable | [Enable encryption for saved objects](https://www.elastic.co/docs/deploy-manage/security/secure-saved-objects)  |
    | **User session**  | Kibana sessions                        | Configurable | [Customize session parameters](https://www.elastic.co/docs/deploy-manage/security/kibana-session-management)    |
  </applies-item>

  <applies-item title="self:" applies-to="Self-managed Elastic deployments: Generally available">
    | Category          | Security feature                       | Status       | Notes                                                                                                                                    |
    |-------------------|----------------------------------------|--------------|------------------------------------------------------------------------------------------------------------------------------------------|
    | **Communication** | TLS (HTTP layer)                       | Configurable | Can be automatically or manually configured. See [Initial security setup](https://www.elastic.co/docs/deploy-manage/security/self-setup) |
    |                   | TLS (Transport layer)                  | Configurable | Can be automatically or manually configured. See [Initial security setup](https://www.elastic.co/docs/deploy-manage/security/self-setup) |
    | **Network**       | IP filtering                           | Configurable | [Configure IP-based access restrictions](https://www.elastic.co/docs/deploy-manage/security/ip-filtering-basic)                          |
    |                   | Private connectivity and VPC filtering | N/A          |                                                                                                                                          |
    |                   | Kubernetes network policies            | N/A          |                                                                                                                                          |
    | **Data**          | Encryption at rest                     | N/A          |                                                                                                                                          |
    |                   | Keystore security                      | Configurable | [Configure secure settings](https://www.elastic.co/docs/deploy-manage/security/secure-settings)                                          |
    |                   | Saved object encryption                | Configurable | [Enable encryption for saved objects](https://www.elastic.co/docs/deploy-manage/security/secure-saved-objects)                           |
    | **User session**  | Kibana sessions                        | Configurable | [Customize session parameters](https://www.elastic.co/docs/deploy-manage/security/kibana-session-management)                             |
  </applies-item>
</applies-switch>


## Securing other Elastic Stack components

The Elasticsearch security features enable you to secure your Elasticsearch cluster. However, for a complete security strategy, you must secure other applications in the Elastic Stack, as well as communications between Elasticsearch and other Elastic Stack components.
[Review security topics for other Elastic Stack components](https://www.elastic.co/docs/deploy-manage/security/secure-clients-integrations).

## Securing clients and integrations

If you use HTTP clients or integrations to communicate with Elasticsearch, then you also need to [secure communications between the clients or integrations and Elasticsearch](https://www.elastic.co/docs/deploy-manage/security/httprest-clients-security).

## Security limitations

There are security limitations that apply to the usage of some Elasticsearch features or resources. Depending on your organization's security requirements, you might want to restrict, adjust, or find workaround or alternatives for some of these features and resources.
[Review Elasticsearch security limitations](https://www.elastic.co/docs/deploy-manage/security/limitations).