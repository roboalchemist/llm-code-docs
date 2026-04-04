# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.managedblockchain_invitation.dataset.md

---
title: Managed Blockchain Invitation
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Managed Blockchain Invitation
---

# Managed Blockchain Invitation

An AWS Managed Blockchain Invitation represents an invitation sent to another AWS account to join a blockchain network. It contains details about the invitation, such as the network it belongs to, the status of the invitation, and the account being invited. This resource allows network administrators to manage and track invitations for participants in a blockchain consortium.

```
aws.managedblockchain_invitation
```

## Fields

| Title           | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Description |
| --------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key            | core | string     |
| account_id      | core | string     |
| arn             | core | string     | The Amazon Resource Name (ARN) of the invitation. For more information about ARNs and their format, see Amazon Resource Names (ARNs) in the Amazon Web Services General Reference.                                                                                                                                                                                                                                                                                           |
| creation_date   | core | timestamp  | The date and time that the invitation was created.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| expiration_date | core | timestamp  | The date and time that the invitation expires. This is the CreationDate plus the ProposalDurationInHours that is specified in the ProposalThresholdPolicy. After this date and time, the invitee can no longer create a member and join the network using this InvitationId.                                                                                                                                                                                                 |
| invitation_id   | core | string     | The unique identifier for the invitation.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| network_summary | core | json       | A summary of network configuration properties.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| status          | core | string     | The status of the invitation: PENDING - The invitee hasn't created a member to join the network, and the invitation hasn't yet expired. ACCEPTING - The invitee has begun creating a member, and creation hasn't yet completed. ACCEPTED - The invitee created a member and joined the network using the InvitationID. REJECTED - The invitee rejected the invitation. EXPIRED - The invitee neither created a member nor rejected the invitation before the ExpirationDate. |
| tags            | core | hstore_csv |
