# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.elasticsearch_domain.dataset.md

---
title: Elasticsearch Domain
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Elasticsearch Domain
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.elasticsearch_domain.dataset/index.html
---

# Elasticsearch Domain

This table represents the Elasticsearch Domain resource from Amazon Web Services.

```
aws.elasticsearch_domain
```

## Fields

| Title                           | ID   | Type   | Data Type                                                                                                                                                                                                                                                                              | Description |
| ------------------------------- | ---- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                            | core | string |
| access_policies                 | core | string | IAM access policy as a JSON-formatted string.                                                                                                                                                                                                                                          |
| account_id                      | core | string |
| advanced_options                | core | hstore | Specifies the status of the <code>AdvancedOptions</code>                                                                                                                                                                                                                               |
| advanced_security_options       | core | json   | The current status of the Elasticsearch domain's advanced security options.                                                                                                                                                                                                            |
| arn                             | core | string | The Amazon resource name (ARN) of an Elasticsearch domain. See <a href="http://docs.aws.amazon.com/IAM/latest/UserGuide/index.html?Using_Identifiers.html" target="_blank">Identifiers for IAM Entities</a> in <i>Using AWS Identity and Access Management</i> for more information.   |
| auto_tune_options               | core | json   | The current status of the Elasticsearch domain's Auto-Tune options.                                                                                                                                                                                                                    |
| change_progress_details         | core | json   | Specifies change details of the domain configuration change.                                                                                                                                                                                                                           |
| cognito_options                 | core | json   | The <code>CognitoOptions</code> for the specified domain. For more information, see <a href="http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-cognito-auth.html" target="_blank">Amazon Cognito Authentication for Kibana</a>.                                |
| created                         | core | bool   | The domain creation status. <code>True</code> if the creation of an Elasticsearch domain is complete. <code>False</code> if domain creation is still in progress.                                                                                                                      |
| deleted                         | core | bool   | The domain deletion status. <code>True</code> if a delete request has been received for the domain but resource cleanup is still in progress. <code>False</code> if the domain has not been deleted. Once domain deletion is complete, the status of the domain is no longer returned. |
| domain_endpoint_options         | core | json   | The current status of the Elasticsearch domain's endpoint options.                                                                                                                                                                                                                     |
| domain_id                       | core | string | The unique identifier for the specified Elasticsearch domain.                                                                                                                                                                                                                          |
| domain_name                     | core | string | The name of an Elasticsearch domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).                                   |
| domain_processing_status        | core | string | The status of any changes that are currently in progress for the domain.                                                                                                                                                                                                               |
| ebs_options                     | core | json   | The <code>EBSOptions</code> for the specified domain. See <a href="http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-ebs" target="_blank">Configuring EBS-based Storage</a> for more information.           |
| elasticsearch_cluster_config    | core | json   | The type and number of instances in the domain cluster.                                                                                                                                                                                                                                |
| elasticsearch_version           | core | string |
| encryption_at_rest_options      | core | json   | Specifies the status of the <code>EncryptionAtRestOptions</code>.                                                                                                                                                                                                                      |
| endpoint                        | core | string | The Elasticsearch domain endpoint that you use to submit index and search requests.                                                                                                                                                                                                    |
| endpoints                       | core | hstore | Map containing the Elasticsearch domain endpoints used to submit index and search requests. Example <code>key, value</code>: <code>'vpc','vpc-endpoint-h2dsd34efgyghrtguk5gt6j2foh4.us-east-1.es.amazonaws.com'</code>.                                                                |
| log_publishing_options          | core | string | Log publishing options for the given domain.                                                                                                                                                                                                                                           |
| modifying_properties            | core | json   | Information about the domain properties that are currently being modified.                                                                                                                                                                                                             |
| node_to_node_encryption_options | core | json   | Specifies the status of the <code>NodeToNodeEncryptionOptions</code>.                                                                                                                                                                                                                  |
| policies                        | core | json   |
| processing                      | core | bool   | The status of the Elasticsearch domain configuration. <code>True</code> if Amazon Elasticsearch Service is processing configuration changes. <code>False</code> if the configuration is active.                                                                                        |
| service_software_options        | core | json   | The current status of the Elasticsearch domain's service software.                                                                                                                                                                                                                     |
| snapshot_options                | core | json   | Specifies the status of the <code>SnapshotOptions</code>                                                                                                                                                                                                                               |
| tags                            | core | hstore |
| upgrade_processing              | core | bool   | The status of an Elasticsearch domain version upgrade. <code>True</code> if Amazon Elasticsearch Service is undergoing a version upgrade. <code>False</code> if the configuration is active.                                                                                           |
| vpc_options                     | core | json   | The <code>VPCOptions</code> for the specified domain. For more information, see <a href="http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html" target="_blank">VPC Endpoints for Amazon Elasticsearch Service Domains</a>.                               |
