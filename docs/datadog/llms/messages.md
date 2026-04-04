# Source: https://docs.datadoghq.com/data_streams/messages.md

---
title: Messages
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Data Streams Monitoring > Messages
---

# Messages

Messages feature allows identifying the root cause of poison pill messages and to better understand data streams by inspecting message content. It allows viewing Kafka messages at specific partitions and offsets.

{% alert level="info" %}
Messages is in Preview. Contact your Customer Success Manager for access.
{% /alert %}

## Supported data formats{% #supported-data-formats %}

Avro, Protobuf, and JSON are supported.

## Prerequisites{% #prerequisites %}

### Kafka Consumer integration{% #kafka-consumer-integration %}

[Kafka Consumer](https://docs.datadoghq.com/integrations/kafka-consumer) integration needs to be set up on any consumer consuming from the topic you want to retrieve messages from. If a topic has more than one consumer group, setting up the integration on one of these consumer groups is enough to use the feature.

#### Validation{% #validation %}

Ensure that the Kafka Consumer check is running correctly by following [these instructions](https://docs.datadoghq.com/integrations/kafka-consumer/?tab=host#validation)

### Agent version{% #agent-version %}

Ensure the agent version you are running is 7.70 or later.

#### Validation{% #validation-1 %}

1. [Run the Agent's status subcommand](https://docs.datadoghq.com/agent/configuration/agent-commands/#agent-information) and check the agent version.
1. In Datadog, under [integrations, View agents](https://app.datadoghq.com/fleet), find the agent running the Kafka Consumer integration, and check its version.

### Remote configuration{% #remote-configuration %}

Ensure [remote configuration](https://docs.datadoghq.com/agent/remote_config) is set up for the agent running the Kafka Consumer integration.

#### Validation{% #validation-2 %}

1. In Datadog, under [Remote Configuration](https://app.datadoghq.com/organization-settings/remote-config), check that remote configuration is enabled at the organization level.
1. In Datadog, under [Remote Configuration](https://app.datadoghq.com/organization-settings/remote-config), check that the agent running the Kafka Consumer integration has remote configuration enabled, and is using an API key with remote configuration enabled.

## Required permissions{% #required-permissions %}

You must have the `Data Streams Monitoring Capture Messages` permission, and these logs permissions that are part of the Datadog Standard role:

- `Logs Read Index Data`
- `Logs Read Data`
- `Logs Live Tail`

You can verify your current permissions on your [Profile page](https://app.datadoghq.com/personal-settings/profile). To enable permissions, edit an existing role or create a new one on the [Roles page](https://app.datadoghq.com/organization-settings/roles). If you do not have permission to modify roles, contact your organization's administrator.

### 1. Create a new role

1. Navigate to the [Roles page](https://app.datadoghq.com/organization-settings/roles) in Datadog.
1. Click **+ New Role** in the top-right corner.Important alert (level: info): If you see "Read Only" instead of the "+ New Role button", you don't have permission to create roles. Contact your Datadog administrator for assistance.
1. Enter a descriptive name for your new role (for example, "Data Streams Messages Access").
1. In the **Search Permissions** field, type `Data Streams Monitoring Capture Messages`.
1. Select the permission from the search results to enable it for this role.
1. Click **Save**.
1. Confirm your role was created successfully by searching for it in the roles list.

### 2. Assign the role to users

1. Go to the [Users page](https://app.datadoghq.com/organization-settings/users) in Datadog.
1. Find and click on the user you want to assign the role to.
1. In the user details panel, click **Edit** next to their name.Important alert (level: info): If you don't see an "Edit" button, you need administrator privileges to modify user roles. Contact your Datadog administrator.
1. In the modal that opens, locate the **Roles** section.
1. Add your newly created role to the user.
1. Click **Save**.
1. Look for a "User updated" confirmation message to verify the change was successful.
