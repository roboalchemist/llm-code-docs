# Source: https://docs.confluent.io/cloud/current/clusters/terraform-provider.md

<a id="confluent-terraform-provider"></a>

# Create a Kafka Cluster on Confluent Cloud from a Template Using Terraform

## What is Terraform?

[HashiCorp Terraform](https://developer.hashicorp.com/terraform/docs)
is an open source infrastructure-as-code tool that lets you build, change,
and version your cloud data infrastructure in a safe, efficient way. You
program Terraform with human-readable configuration files that you can
version, reuse, share, and deploy in your CI/CD pipelines.

<!-- WARNING: THIS IS A SHARED FILE AND THE SOURCE IS LOCATED IN DOCS-COMMON. DO NOT ADD TO ANY OTHER REPO. -->

## Resources you can manage

- [Confluent](#confluent-terraform-provider-resources-confluent)
- [Connect](#confluent-terraform-provider-resources-connect)
- [Confluent Cloud for Apache FlinkÂ®](#confluent-terraform-provider-resources-flink)
- [Apache KafkaÂ®](#confluent-terraform-provider-resources-kafka)
- [ksqlDB](#confluent-terraform-provider-resources-ksqldb)
- [Metadata](#confluent-terraform-provider-resources-metadata)
- [Network](#confluent-terraform-provider-resources-network)
- [Schema management and Stream Governance](#confluent-terraform-provider-resources-schema)

<a id="confluent-terraform-provider-why-terraform-and-kafka"></a>

## Why Terraform and Kafka?

Use the [Confluent Terraform provider](https://registry.terraform.io/providers/confluentinc/confluent/latest)
to deploy and manage Confluent Cloud infrastructure. The Confluent Terraform
provider automates the workflow for managing environments, Apache KafkaÂ® clusters,
Kafka topics, and other resources in Confluent Cloud.

These are some of the benefits you get with the Confluent Terraform provider:

- **Human Readable Configuration:** Define infrastructure resources declaratively
  in human-readable configuration files.
- **Manage Critical Confluent Cloud Resources:** Manage API keys, environments,
  Kafka clusters, topics, ACLs, RBAC, Private Networking, and more.
- **Consistent Deployability:** Provision and manage your infrastructure safely
  and efficiently throughout its lifecycle. Package reusable modules to provision
  multi-cloud resources.
- **Multi-Cloud With Ease:** Deploy Confluent Cloud seamlessly across cloud providers.
- **Scale Quickly:** Provision complex and dependent infrastructure quickly.
- **Industry Standard:** Enable industry standard GitOps and infrastructure-as-code
  practices.

<a id="confluent-terraform-provider-tutorial"></a>

## Confluent Terraform tutorial

The following tutorials show how to get started with the Confluent Terraform
provider:

- [Sample Project for Confluent Terraform Provider](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/guides/sample-project)
- [Applying Data Pipeline Principles in Practice: Exploring the Kafka Summit Keynote Demo](https://www.confluent.io/blog/data-pipeline-principles-use-cases-examples/)

<a id="confluent-terraform-provider-using"></a>

## Using the Confluent Terraform provider

The following example shows a simple Terraform configuration file that
provisions a Confluent Cloud environment, a basic Kafka cluster, and a service
account.

```terraform
# Configure the Confluent Provider
terraform {
  required_providers {
    confluent = {
      source  = "confluentinc/confluent"
      version = "2.63.0"
    }
  }
}

provider "confluent" {
  cloud_api_key    = var.confluent_cloud_api_key    # optionally use CONFLUENT_CLOUD_API_KEY env var
  cloud_api_secret = var.confluent_cloud_api_secret # optionally use CONFLUENT_CLOUD_API_SECRET env var
}

resource "confluent_environment" "development" {
  display_name = "Development"

  lifecycle {
    prevent_destroy = true
  }
}

resource "confluent_kafka_cluster" "basic" {
  display_name = "basic_kafka_cluster"
  availability = "SINGLE_ZONE"
  cloud        = "AWS"
  region       = "us-east-2"
  basic {}

  environment {
    id = confluent_environment.development.id
  }

  lifecycle {
    prevent_destroy = true
  }
}

resource "confluent_service_account" "app-manager" {
  display_name = "app-manager"
  description  = "Service account to manage Kafka cluster"
}

# Create more resources ...
```

You must provide appropriate Confluent Cloud and Kafka cluster credentials to use
the provider.

For more information about the resources that you can interact with, see the
[Confluent Terraform Provider documentation](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs)
in the Terraform registry.

<a id="confluent-terraform-provider-sample-project"></a>

### Sample project

For realistic examples that create multiple Confluent Cloud resources, see the
[Sample Project for Confluent Terraform Provider](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/guides/sample-project).
The sample project shows configurations that provision Confluent Cloud resources like
these:

- Basic, Standard, Enterprise, Dedicated, and Freight Kafka clusters
- PrivateLink connections
- RBAC and ACLs for access control
- Source and sink connectors
- VPC Peering connections

<a id="confluent-terraform-provider-source-code"></a>

## Source code

- For the provider source code, see the
  [Confluent Terraform Provider repository on GitHub](https://github.com/confluentinc/terraform-provider-confluent).
- For sample configuration files, see the [examples](https://github.com/confluentinc/terraform-provider-confluent/tree/master/examples/configurations) directory in the source repo.

<a id="confluent-terraform-provider-resource-importer"></a>

## Resource Importer

The [Resource Importer](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/guides/resource-importer)
enables importing your existing Confluent Cloud resources to Terraform Configuration
(`main.tf`) and Terraform State (`terraform.tfstate`) files.

<a id="confluent-terraform-provider-resources"></a>

## Resources you can manage

You can provision the following Confluent Cloud resources and get data from these data
sources in your Terraform configuration files.

<a id="confluent-terraform-provider-resources-confluent"></a>

### Confluent

<!-- string replacements for the table -->

| Resource                                                                                                                                              | Data Source                                                                                                                                              |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Confluent Invitation](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_invitation)                     | [Confluent Invitation](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_invitation)                     |
| [Confluent Provider Integration](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_provider_integration) | [Confluent Provider Integration](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_provider_integration) |
| â                                                                                                                                                     | [Confluent Endpoint](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_endpoint)                         |
| â                                                                                                                                                     | [Confluent Gateways](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_gateways)                         |

<a id="confluent-terraform-provider-resources-connect"></a>

### Connect

<!-- string replacements for the table -->

| Resource                                                                                                                                                   | Data Source                                                                                                                            |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| [Connect Artifact](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_connect_artifact)                        | [Connect Artifact](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_connect_artifact) |
| [Connector](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_connector)                                      | â                                                                                                                                      |
| [Connector Plugin](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_plugin)                                  | â                                                                                                                                      |
| [Connector Plugin Version](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_custom_connector_plugin_version) | â                                                                                                                                      |

<a id="confluent-terraform-provider-resources-flink"></a>

### Flink

<!-- string replacements for the table -->

| Resource                                                                                                                                | Data Source                                                                                                                                |
|-----------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| [Flink Artifact](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_flink_artifact)         | [Flink Artifact](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_flink_artifact)         |
| [Flink Compute Pool](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_flink_compute_pool) | [Flink Compute Pool](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_flink_compute_pool) |
| [Flink Connection](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_flink_connection)     | [Flink Connection](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_flink_connection)     |
| [Flink Statement](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_flink_statement)       | â                                                                                                                                          |
| â                                                                                                                                       | [Flink Region](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_flink_region)             |

<a id="confluent-terraform-provider-resources-kafka"></a>

### Kafka cluster

<!-- string replacements for the table -->

| Resource                                                                                                                                                     | Data Source                                                                                                                                |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| [Cluster Link](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_cluster_link)                                  | [Cluster Link](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_cluster_link)             |
| [Connector](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_connector)                                        | â                                                                                                                                          |
| [Dedicated Kafka Cluster Configuration](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_kafka_cluster_config) | â                                                                                                                                          |
| [Kafka Client Quota](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_kafka_client_quota)                      | [Kafka Client Quota](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_kafka_client_quota) |
| [Kafka Cluster](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_kafka_cluster)                                | [Kafka Cluster](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_kafka_cluster)           |
| â                                                                                                                                                            | [Kafka Clusters](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_kafka_clusters)         |
| [Kafka Mirror Topic](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_kafka_mirror_topic)                      | â                                                                                                                                          |
| [Kafka Topic](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_kafka_topic)                                    | [Kafka Topic](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_kafka_topic)               |

<a id="confluent-terraform-provider-resources-ksqldb"></a>

### ksqlDB

<!-- string replacements for the table -->

| Resource                                                                                                                      | Data Source                                                                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| [ksqlDB Cluster](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_ksql_cluster) | [ksqlDB Cluster](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_ksql_cluster) |

<a id="confluent-terraform-provider-resources-metadata"></a>

### Metadata

<!-- string replacements for the table -->

| Resource                                                                                                                                              | Data Source                                                                                                                                              |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Business Metadata](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_business_metadata)                 | [Business Metadata](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_business_metadata)                 |
| [Business Metadata Binding](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_business_metadata_binding) | [Business Metadata Binding](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_business_metadata_binding) |
| [Tag](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_tag)                                             | [Tag](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_tag)                                             |
| [Tag Binding](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_tag)                                     | [Tag Binding](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_tag_binding)                             |

<a id="confluent-terraform-provider-resources-network"></a>

### Network

<!-- string replacements for the table -->

| Resource                                                                                                                                                                | Data Source                                                                                                                                                                |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Access Point](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_access_point)                                             | [Access Point](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_access_point)                                             |
| [Certificate Authority](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_certificate_authority)                           | [Certificate Authority](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_certificate_authority)                           |
| [Certificate Pool](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_certificate_pool)                                     | [Certificate Pool](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_certificate_pool)                                     |
| [DNS Record](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_dns_record)                                                 | [DNS Record](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_dns_record)                                                 |
| â                                                                                                                                                                       | [IP Addresses (Preview)](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_ip_addresses)                                   |
| [DNS Forwarder](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_dns_forwarder)                                           | â                                                                                                                                                                          |
| [Gateway](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_gateway)                                                       | [Gateway](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_gateway)                                                       |
| [IP Filter](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_ip_filter)                                                   | [IP Filter](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_ip_filter)                                                   |
| [IP Group](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_ip_group)                                                     | [IP Group](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_ip_group)                                                     |
| [Network](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_network)                                                       | [Network](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_network)                                                       |
| [Network Link Endpoint](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_network_link_endpoint)                           | [Network Link Endpoint](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_network_link_endpoint)                           |
| [Network Link Service](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_network_link_service)                             | [Network Link Service](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_network_link_service)                             |
| [Peering](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_peering)                                                       | [Peering](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_peering)                                                       |
| [Private Link Access](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_private_link_access)                               | [Private Link Access](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_private_link_access)                               |
| [Private Link Attachment](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_private_link_attachment)                       | [Private Link Attachment](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_private_link_attachment)                       |
| [Private Link Attachment Connection](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_private_link_attachment_connection) | [Private Link Attachment Connection](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_private_link_attachment_connection) |
| [Transit Gateway Attachment](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_transit_gateway_attachment)                 | [Transit Gateway Attachment](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_transit_gateway_attachment)                 |

<a id="confluent-terraform-provider-resources-schema"></a>

### Schema management and Stream Governance

<!-- string replacements for the table -->

| Resource                                                                                                                                                        | Data Source                                                                                                                                                        |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Catalog Entity Attributes](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_catalog_entity_attributes)           | â                                                                                                                                                                  |
| [Schema](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_schema)                                                 | [Schema](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_schema)                                                 |
| â                                                                                                                                                               | [Schemas](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_schemas)                                               |
| [Schema Exporter](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_schema_exporter)                               | â                                                                                                                                                                  |
| â                                                                                                                                                               | [Schema Registry Cluster](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_schema_registry_cluster)               |
| â                                                                                                                                                               | [Schema Registry Clusters](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_schema_registry_clusters)             |
| [Schema Registry Cluster Config](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_schema_registry_cluster_config) | [Schema Registry Cluster Config](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_schema_registry_cluster_config) |
| [Schema Registry Cluster Mode](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_schema_registry_cluster_mode)     | [Schema Registry Cluster Mode](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_schema_registry_cluster_mode)     |
| [Schema Registry DEK](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_schema_registry_dek)                       | [Schema Registry DEK](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_schema_registry_dek)                       |
| [Schema Registry KEK](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_schema_registry_kek)                       | [Schema Registry KEK](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_schema_registry_kek)                       |
| [Subject Config](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_subject_config)                                 | [Subject Config](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_subject_config)                                 |
| [Subject Mode](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_subject_mode)                                     | [Subject Mode](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_subject_mode)                                     |

<a id="confluent-terraform-provider-resources-security"></a>

### Security, access control, and identity

<!-- string replacements for the table -->

| Resource                                                                                                                              | Data Source                                                                                                                              |
|---------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| [API key](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_api_key)                     | â                                                                                                                                        |
| [BYOK key](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_byok_key)                   | [BYOK key](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_byok_key)                   |
| [Environment](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_environment)             | [Environment](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_environment)             |
| â                                                                                                                                     | [Environments](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_environments)           |
| [Group Mapping](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_group_mapping)         | [Group Mapping](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_group_mapping)         |
| [Identity Pool](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_identity_pool)         | [Identity Pool](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_identity_pool)         |
| [Identity Provider](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_identity_provider) | [Identity Provider](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_identity_provider) |
| [Kafka ACL](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_kafka_acl)                 | â                                                                                                                                        |
| â                                                                                                                                     | [Organization](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_organization)           |
| [Role Binding](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_role_binding)           | [Role Binding](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_role_binding)           |
| [Service Account](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_service_account)     | [Service Account](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_service_account)     |
| â                                                                                                                                     | [User](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_user)                           |
| â                                                                                                                                     | [Users](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_users)                         |

<a id="confluent-terraform-provider-resources-tableflow"></a>

### Tableflow

<!-- string replacements for the table -->

| Resource                                                                                                                                  | Data Source                                                                                                                                  |
|-------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| [Tableflow Topic](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_tableflow_topic)         | [Tableflow Topic](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_tableflow_topic)         |
| [Catalog Integration](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/resources/confluent_catalog_integration) | [Catalog Integration](https://registry.terraform.io/providers/confluentinc/confluent/latest/docs/data-sources/confluent_catalog_integration) |

## Related content

- [Video: Getting started with the Confluent Terraform Provider](https://www.youtube.com/watch?v=ofSQ4j9u6W4)
- [Terraform CLI Documentation](https://www.terraform.io/cli)
- [Create a Kafka Cluster on Confluent Cloud from a Template Using Pulumi](pulumi-provider.md#confluent-pulumi-provider)
- [Kafka Cluster Types in Confluent Cloud](cluster-types.md#cloud-cluster-types)
