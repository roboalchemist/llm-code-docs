# Source: https://docs.datadoghq.com/actions/connections.md

---
title: Connections
description: Connections for actions
breadcrumbs: Docs > Connections
---

# Connections

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

Because actions connect with external software systems, you may need to authenticate your Datadog account to the corresponding integration. An app or workflow can run successfully only if every action that requires authentication can verify the identity of your Datadog account. When granting permissions to Datadog, ensure that you're following security best practice and only granting the permissions necessary for an app or workflow to run.

Actions can be authenticated in two ways:

- Credentials and permissions configured in the integration tile
- Connection credentials

## Integration tile credentials{% #integration-tile-credentials %}

Credentials and account authentication that you set up in the following Datadog integration tiles automatically propagate to the corresponding actions in workflows or apps:

- GitHub
- Jira
- Microsoft Teams
- Opsgenie
- PagerDuty
- Slack
- Statuspage

Configure the integration tiles by following instructions in [Datadog Integrations](https://docs.datadoghq.com/integrations/).

If the integration you need to set up is not listed above, set up connection credentials.

## Connection credentials{% #connection-credentials %}

Connections extend your installed integrations to give you control over workflow step authentication. Use connection credentials to authenticate a [generic action](https://docs.datadoghq.com/service_management/workflows/actions/) or any action for which the integration tile does not offer authentication. For a list of integrations that use the integration tile for authentication, see the Integration tile credentials section. Connection credentials are only available for use within the Workflow Automation and App Builder products.

Connections support the following example use cases:

- The integration you need is not available as a built-in connection.
- You wish to authenticate a custom action. For instance, you need to use the HTTP action with your own service.
- The permissions needed are not supported by the integration, such as write permissions on AWS.
- You want granular access control, for example restricting user access to certain workflows.

### Connection security considerations{% #connection-security-considerations %}

Before you create a connection, think about the permissions needed to fulfill the required task and grant the connection only the necessary permissions to fulfill that task. In addition, the connection should be restricted to only the people who need to use it.

Where possible, use granular connections for different workflows or apps. For example, if you have a workflow that writes to an Amazon S3 bucket, and an app that terminates Amazon EC2 instances, do not use the same connection for both. Instead, create two respective connections, each corresponding to an IAM role with limited scope.

## Work with connections{% #work-with-connections %}

### View connections{% #view-connections %}

1. From the [Workflow Automation page](https://app.datadoghq.com/workflow) or the [App Builder page](https://app.datadoghq.com/app-builder/), click the **Connections** tab. The connections list opens.
1. Click on a single line to view connection details.

### Create a connection{% #create-a-connection %}

Establishing a connection requires the following information:

- What to connect to (for example, product name, URL)
- How to authenticate (for example, API key, username/password, oauth)

To create a connection:

1. From the [Workflow Automation page](https://app.datadoghq.com/workflow) or the [App Builder page](https://app.datadoghq.com/app-builder/), click the **Connections** tab. The connections list opens.
1. Click the **New Connection** button in the upper right. The **New Connection** dialog box appears.
1. Click on an icon to choose an integration schema.
1. Fill in the appropriate fields.Important alert (level: info): If you want to add the connection to a connection group in the future, add one or more Identifier Tags.
1. Click **Create**.

Alternatively, add a connection from a workflow or app page:

{% tab title="Workflow Automation" %}

1. Navigate to the [Workflow Automation list](https://app.datadoghq.com/workflow).
1. Select the workflow containing the action to which you need to add a credential. The workflow builder appears.
1. In the workflow visualization, click the action to which you need to add a credential. The right side panel populates with the action details.
1. Under the **Configure** tab, look for the **Connection** dropdown and click the **+** icon.
1. In the **New Connection** dialog box, name the connection and enter the required authentication details.
1. Click **Save**.

{% /tab %}

{% tab title="App Builder" %}

1. Navigate to the [App Builder app list](https://app.datadoghq.com/app-builder).
1. Select the app containing the action you need to add a credential to. The app canvas appears.
1. Click **Edit** in the upper right.
1. Under **Data** on the left-hand side, click the action to which you need to add a credential. The left side panel populates with the action details.
1. Look for the **Connection** dropdown and click the **+** icon.
1. In the **New Connection** dialog box, name the connection and enter the required authentication details.
1. Click **Save**.

{% /tab %}

The example below shows the **New Connection** dialog box for the OpenAI connection. Each connection requires different authentication information. The OpenAI connection requires a valid Connection Name and API Token.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/new-connection-2.6163cdeab0f54d3d983bb6caa2e08f5c.png?auto=format"
   alt="The New Connection dialog box for the OpenAI connection" /%}

### Edit a connection{% #edit-a-connection %}

1. From the [Workflow Automation page](https://app.datadoghq.com/workflow) or the [App Builder page](https://app.datadoghq.com/app-builder/), click the **Connections** tab. The connections list opens.
1. Hover over the connection you would like to edit. **Edit**, **Permissions**, and **Delete** icons appear on the right.
1. Click the pencil (**Edit**) icon. A dialog box appears.
1. Update the fields you would like to change.
1. Click **Save**.

### Delete a connection{% #delete-a-connection %}

1. Navigate to the [connections list](https://app.datadoghq.com/workflow/connections).
1. Hover over the connection you would like to delete. **Edit**, **Permissions**, and **Delete** icons appear on the right.
1. Click the trash can (**Delete**) icon. "Are you sure?" text appears.
1. Select **Delete**.

### Restrict connection use{% #restrict-connection-use %}

To learn how to restrict connection use, see Access and Authentication for [Workflow Automation](https://docs.datadoghq.com/actions/workflows/access_and_auth/#restrict-access-on-a-specific-connection) or [App Builder](https://docs.datadoghq.com/actions/app_builder/access_and_auth/#restrict-access-to-a-specific-connection).

## HTTP connection{% #http-connection %}

To connect to an arbitrary service, use the HTTP connection type. For authentication options and setup instructions, see the [HTTP action](https://docs.datadoghq.com/actions/connections/http/).

## Connection identifier tags{% #connection-identifier-tags %}

You can add identifier tags to connections. The tagging rules for connections are based on [Datadog tags](https://docs.datadoghq.com/getting_started/tagging/), with the following additional requirements:

- Identifier tags must follow the format `tag:value`, and additional colons are not allowed. For example, the identifier tags `env:staging:east` and `env` are invalid formats for connection tags.
- Identifier tags must start with a letter, after which they can contain:
  - Alphanumerics
  - Underscores
  - Minuses
  - Slashes
  - Exactly one colon
- `default` is a reserved value for connection identifier tags. It can't be used as a stand-alone tag key or as a tag value. For example, `default:yes` and `aws:default` are invalid for connection tags.

## Connection groups{% #connection-groups %}

You can create groups of connections so that your workflows and apps can authenticate into the correct account or accounts based on the given inputs. Connections can be grouped together only if they share the same integration (for example, you cannot group GCP and AWS connections within the same group).

You define the members of a connection group using a connection's *Identifier Tags*. For example, you can create a connection group consisting of AWS accounts that have the `account_id` tag.

Each connection in the group must have a set of unique identifier tags so that a workflow can dynamically select the correct connection at runtime. For example:

- `connectionA {account_id:123456789}` and `connectionB {account_id:987654321}` can be grouped together.
- `connectionA {account_id:123456789}` and `connectionC {account_id:123456789}` can't be grouped, because the group would contain duplicate tag values.

### Create a connection group{% #create-a-connection-group %}

{% alert level="info" %}
You can only add connections to a group if you have [Resolver permission](https://docs.datadoghq.com/actions/workflows/access_and_auth/#restrict-access-on-a-specific-connection) for them.
{% /alert %}

To create a connection group:

1. Navigate to the [connections list](https://app.datadoghq.com/workflow/connections).
1. On the left, click **Groups**.
1. Click **+ New Group**, then select an integration.
1. Enter a group name, then enter a set of up to three **Identifier Tags** that the connections you want to include in your group all have.
1. Under **Confirm Group**, use the checkboxes to select the specific members of your group.
1. Click **Next, Confirm Access**, then choose your desired access level for the group.
1. Click **Create**.

### Use a connection group{% #use-a-connection-group %}

To use a connection group:

1. In your workflow or app, select an action that requires a connection.
1. In the **Connection** field, in the drop-down, select the desired connection group under **Groups**.
1. Fill in the desired values for the connection group **Identifiers**. For example, if your connection group is defined using the `env` Identifier Tag, and you have two environments, `prod` and `staging`, you could use either of those values (or an expression that evaluates to one of those values).
1. Fill in any other required step values, then click **Save**.

**Note**: You can only use connections within a group if you have [Resolver permission](https://docs.datadoghq.com/actions/workflows/access_and_auth/#restrict-access-on-a-specific-connection) for those connections. If a workflow or app tries to use a connection you don't have Resolver permission for, it fails with a `403 Forbidden` error. To fix this issue, you can:

- Configure the workflow or app so that it can't point to a connection that doesn't have a Resolver permission.
- Remove the connection that doesn't have a Resolver permission from the connection group.Important alert (level: warning): If you are using a connection group for multiple workflows or multiple apps, removing a connection that another workflow relies on causes that workflow to fail.

### Update a connection group{% #update-a-connection-group %}

If you have edit access to a connection group, you can update the following attributes:

- Group name
- Identifier Tags (these can never be empty, but they can be completely replaced)
- Connections (a group can be empty)

### Delete a connection group{% #delete-a-connection-group %}

To delete a connection group:

1. Hover over the group you want to delete and click the **delete (trash can)** icon.
1. Click **Delete**.

{% alert level="danger" %}
Deleting a connection group impacts any workflows and apps that are using that group.
{% /alert %}

## Further reading{% #further-reading %}

- [Getting Started with Workflow Automation](https://docs.datadoghq.com/getting_started/workflow_automation/)
- [App Builder documentation](https://docs.datadoghq.com/service_management/app_builder/)

Do you have questions or feedback? Join the **#workflows** or **#app-builder** channel on the [Datadog Community Slack](https://chat.datadoghq.com/).
