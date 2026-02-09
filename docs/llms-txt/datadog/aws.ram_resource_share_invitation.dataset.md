# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ram_resource_share_invitation.dataset.md

---
title: Resource Access Manager Resource Share Invitation
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Resource Access Manager Resource
  Share Invitation
---

# Resource Access Manager Resource Share Invitation

A Resource Access Manager Resource Share Invitation in AWS represents an invitation sent to an AWS account or organization to join a resource share. It allows the recipient to accept or reject access to shared resources such as subnets, transit gateways, or license configurations. This resource tracks the status of the invitation and ensures secure cross-account or cross-organization sharing without requiring resource duplication.

```
aws.ram_resource_share_invitation
```

## Fields

| Title                         | ID   | Type       | Data Type                                                                                                      | Description |
| ----------------------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                          | core | string     |
| account_id                    | core | string     |
| invitation_timestamp          | core | timestamp  | The date and time when the invitation was sent.                                                                |
| receiver_account_id           | core | string     | The ID of the Amazon Web Services account that received the invitation.                                        |
| receiver_arn                  | core | string     | The Amazon Resource Name (ARN) of the IAM user or role that received the invitation.                           |
| resource_share_arn            | core | string     | The Amazon Resource Name (ARN) of the resource share                                                           |
| resource_share_associations   | core | json       | To view the resources associated with a pending resource share invitation, use ListPendingInvitationResources. |
| resource_share_invitation_arn | core | string     | The Amazon Resource Name (ARN) of the invitation.                                                              |
| resource_share_name           | core | string     | The name of the resource share.                                                                                |
| sender_account_id             | core | string     | The ID of the Amazon Web Services account that sent the invitation.                                            |
| status                        | core | string     | The current status of the invitation.                                                                          |
| tags                          | core | hstore_csv |
