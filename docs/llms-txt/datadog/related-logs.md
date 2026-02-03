# Source: https://docs.datadoghq.com/security/cloud_security_management/guide/related-logs.md

---
title: View a misconfiguration's related logs
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Cloud Security > Cloud Security Guides > View a
  misconfiguration's related logs
---

# View a misconfiguration's related logs

Datadog Cloud Security's Related Logs feature allows you to quickly identify cloud audit logs that relate to a specific cloud resource. When investigating a misconfiguration, this can help you understand:

- Who created the resource
- Who last modified the resource

## Supported cloud providers{% #supported-cloud-providers %}

Related Logs supports the following:

- AWS CloudTrail logs

**Note**: CloudTrail events do not follow a standardized schema that supports a generic Logs query. Related Logs uses an internal mapping service to match resource attributes to CloudTrail event fields, allowing Datadog to generate the full query needed to identify related CloudTrail activity.

- Azure Activity Logs

## Prerequisites{% #prerequisites %}

### AWS{% #aws %}

Set up [CloudTrail logs](https://docs.datadoghq.com/security/cloud_security_management/setup/cloudtrail_logs/).

Related Logs supports the following AWS resources:

- aws_acm
- aws_cloudfront_distribution
- aws_ebs_snapshot
- aws_ec2_instance
- aws_ecs_service
- aws_ecr_repository
- aws_iam_account
- aws_iam_group
- aws_iam_policy
- aws_iam_role
- aws_iam_user
- aws_lambda_function
- aws_opensearch_domain
- aws_rds_instance
- aws_s3_bucket
- aws_security_group
- aws_sns_topic
- aws_sqs_queue
- aws_subnet
- aws_vpc



To request additional resource types, fill out the [feedback form](https://forms.gle/AqZg9jqBusDf62h87).

### Azure{% #azure %}

Set up [Azure Activity Logs](https://docs.datadoghq.com/logs/guide/azure-automated-log-forwarding/).

## View related logs{% #view-related-logs %}

1. On the **Findings** page, in the [Misconfigurations explorer](https://app.datadoghq.com/security/compliance), open a misconfiguration for a supported resource type.
1. Click the **Related Logs** tab. Datadog queries your cloud logs for events related to the cloud resource.

### Search through a larger time frame{% #search-through-a-larger-time-frame %}

By default, Related Logs searches the last two weeks of related cloud logs. To extend the search to a larger time frame:

1. While viewing a misconfiguration's related logs, click **View All Related Logs**. The search used to populate the list opens in Log Explorer.
1. In the upper-right corner, change the timeframe of the search.

**Note**: Related Logs only display cloud logs within your retention period. To store logs for an extended period of time in a cost-effective manner, Datadog recommends using [Flex Logs](https://docs.datadoghq.com/logs/log_configuration/flex_logs/).

### Search through Flex Logs{% #search-through-flex-logs %}

If your organization uses Flex Logs, toggle **Include Flex logs** in the **Related Logs** tab to display related audit logs stored as Flex Logs.

## Sample generated queries{% #sample-generated-queries %}

Related Logs generates structured Logs queries based on the selected cloud resource. The following examples illustrate typical queries.

### AWS CloudTrail{% #aws-cloudtrail %}

This query finds CloudTrail activity related to a specific EC2 instance:

```plaintext
source:cloudtrail @recipientAccountId:172597598159 @awsRegion:us-east-1 @readOnly:false -status:error (@eventSource:ec2.amazonaws.com AND (@requestParameters.instanceId:"i-0d52853076ed2a357" OR @requestParameters.instancesSet.items.instanceId:"i-0d52853076ed2a357" OR @responseElements.instancesSet.items.instanceId:"i-0d52853076ed2a357" OR @requestParameters.resourcesSet.items.resourceId:"i-0d52853076ed2a357" OR @responseElements.ReplaceIamInstanceProfileAssociationResponse.iamInstanceProfileAssociation.instanceId:"i-0d52853076ed2a357" OR @responseElements.CreateFleetResponse.fleetInstanceSet.item.instanceIds.item:"i-0d52853076ed2a357" OR @requestParameters.CreateReplaceRootVolumeTaskRequest.InstanceId:"i-0d52853076ed2a357" OR @requestParameters.ModifyInstanceMetadataOptionsRequest.InstanceId:"i-0d52853076ed2a357" OR @serviceEventDetails.instanceIdSet:"i-0d52853076ed2a357" OR @requestParameters.AssociateIamInstanceProfileRequest.InstanceId:"i-0d52853076ed2a357" OR @requestParameters.CreateSnapshotsRequest.InstanceSpecification.InstanceId:"i-0d52853076ed2a357"))
```

### Azure Activity Logs{% #azure-activity-logs %}

This query finds Azure Activity events for a specific storage account:

```plaintext
source:azure.* @properties.eventCategory:Administrative @resourceId:(/SUBSCRIPTIONS/FA6CC2AC-1395-5913-1944-F16F8F47EB4D/RESOURCEGROUPS/DEV-RG/PROVIDERS/MICROSOFT.STORAGE/STORAGEACCOUNTS/DEMOSTGACCOUNT OR /SUBSCRIPTIONS/FA6CC2AC-1395-5913-1944-F16F8F47EB4D/RESOURCEGROUPS/DEV-RG/PROVIDERS/MICROSOFT.STORAGE/STORAGEACCOUNTS/DEMOSTGACCOUNT/*) 
```
