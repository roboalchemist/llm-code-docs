# Source: https://docs.datadoghq.com/actions/app_builder/access_and_auth.md

---
title: Access and Authentication
description: Access and authentication for App builder
breadcrumbs: Docs > App Builder > Access and Authentication
---

# Access and Authentication

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

A few tools control access and authentication for apps and their components.

## App execution identity{% #app-execution-identity %}

A published app runs using the Datadog user identity of its author, or a service account associated with the app. The author is listed both in the **All Apps** view and in **App Properties**.

In edit mode, an app runs as the current editor.

### Use a service account{% #use-a-service-account %}

A service account can be associated with an app and act as the identity of the app when it runs. A service account can:

- resolve the connections defined in the app queries at runtime
- provide an identity for app executions
- provide an identity for app [audit trails](https://docs.datadoghq.com/account_management/audit_trail/#overview)

To create a service account for an app, you must have either the Datadog admin role, or a custom role with the **Service Account Write** permission. The service account you create adopts your role and permissions. For more information on service accounts and permissions, see [Service accounts](https://docs.datadoghq.com/account_management/org_settings/service_accounts#permissions) or [Role based access control](https://docs.datadoghq.com/account_management/rbac/?tab=datadogapplication#role-based-access-control).

#### Configure your app to run as a service account{% #configure-your-app-to-run-as-a-service-account %}

1. Click the cog (**Settings**) icon.
1. Click **Manage app identity**.
1. Select **Run as Service Account**.
1. Select a role for your service account user or select an existing service account.
1. Click **Save** to save the service account and apply the changes.

When you run an app, the service account user resolves the connections defined in the app queries. Therefore, the service account user needs the `connections_resolve` permission. The Datadog Admin Role and the Datadog Standard Role include the `connections_resolve` permission.

#### View service account details{% #view-service-account-details %}

1. Click the cog (**Settings**) icon.
1. Select **Manage app identity**.
1. Click on your service account next to *Run As*.

#### Remove a service account associated with an app{% #remove-a-service-account-associated-with-an-app %}

1. Click the cog (**Settings**) icon.
1. Select **Manage app identity**.
1. Click **Remove service account**.

## Action credentials{% #action-credentials %}

Because app [actions](https://app.datadoghq.com/actions/action-catalog/) connect with external software systems, you may need to authenticate your Datadog account to a corresponding integration. An app can run successfully only if every action that requires authentication can verify the identity of your Datadog account.

Actions can be authenticated in the following ways:

- Credentials and permissions configured in the integration tile
- Connection credentials

By default, viewers of a published app do not need access to the app's connections. Instead, actions use the identity of the app's author. This simplifies sharing and improves security by preventing apps from performing sensitive operations using the identity of arbitrary viewers. For more information on configuring credentials, see [Connections](https://docs.datadoghq.com/actions/connections/). App Builder shares the Action Catalog and the connection credentials for each integration with [Datadog Workflow Automation](https://docs.datadoghq.com/actions/workflows/).

## App permissions{% #app-permissions %}

By default:

- While the app is in draft, the author of an app is the only user who has access to the app.
- After the app is published, the author maintains **Editor** access, while the rest of the author's Datadog organization receives **Viewer** access to the app.

You can expand access to a draft of published app using access control.

### Permissions and access control{% #permissions-and-access-control %}

Use [role-based access control (RBAC)](https://docs.datadoghq.com/account_management/rbac/?tab=datadogapplication#role-based-access-control) to control access to your apps and connections.

The coarse permissions that apply to apps include the following:

{% dl %}

{% dt %}
Apps View
{% /dt %}

{% dd %}
View and run apps. Datadog Standard and Admin roles have view access to App Builder by default.
{% /dd %}

{% dt %}
Apps Write
{% /dt %}

{% dd %}
Create and edit new and existing apps. Datadog Standard and Admin roles have write access to App Builder by default.
{% /dd %}

{% dt %}
Connections Read
{% /dt %}

{% dd %}
List and view available connections. Datadog Read Only, Standard, and Admin roles have read access to connections by default.
{% /dd %}

{% /dl %}

### Restrict access to a specific connection{% #restrict-access-to-a-specific-connection %}

Set permissions on individual connections to restrict their use or limit modifications. App Builder provides the following permissions for each connection:

{% dl %}

{% dt %}
Viewer
{% /dt %}

{% dd %}
View the connection
{% /dd %}

{% dt %}
Resolver
{% /dt %}

{% dd %}
Resolve and view the connection
{% /dd %}

{% dt %}
Editor
{% /dt %}

{% dd %}
Edit, resolve, and view the connection
{% /dd %}

{% /dl %}

By default, only the author of the connection receives **Editor** access. The author can choose to grant access to additional users, roles, or teams.

**Note**: Permission to resolve a connection includes permission to get the connection object assigned to a step and retrieve the secret associated with it.

Use the following steps to modify the permissions on a specific connection:

1. Navigate to the [App Builder page](https://app.datadoghq.com/app-builder/).
1. Click the **Connections** tab. A list of connections appears.
1. Hover over the connection that you would like to set granular permissions on. **Edit**, **Permissions**, and **Delete** icons appear on the right.
1. Click the padlock (**Permissions**) icon.
1. Select **Restrict Access**.
1. Select a role from the dropdown menu and click **Add**. The role you selected populates into the bottom of the dialog box.
1. Next to the role name, select the desired permission from the dropdown menu.
1. If you would like to remove access from a role, click the trash can icon to the right of the role name.
1. Click **Save**.

### Restrict access to a specific app{% #restrict-access-to-a-specific-app %}

Set permissions on each app to restrict modifications to the app. By default:

- The author of an app is the only user who has access to the app.
- After the app is published, the author maintains **Editor** access, while the rest of the author's Datadog organization receives **Viewer** access to the app.

App Builder provides the following permissions for each app:

{% dl %}

{% dt %}
Viewer
{% /dt %}

{% dd %}
Run and view the app
{% /dd %}

{% dt %}
Contributor
{% /dt %}

{% dd %}
Edit, run, and view the app
{% /dd %}

{% dt %}
Editor
{% /dt %}

{% dd %}
Edit, run, view, publish, and delete the app.
{% /dd %}

{% /dl %}

To restrict access to the app, perform the following steps in the app canvas:

1. Navigate to the detailed editing view for the app you want to restrict access to.
1. In the app editor, click on the cog (**Settings**) icon.
1. Select **Permissions** from the dropdown.
1. Select **Restrict Access**.
1. Select a role from the dropdown menu. Click **Add**. The role you selected populates into the bottom of the dialog box.
1. Next to the role name, select your desired permission from the dropdown menu.
1. If you would like to remove access from a role, click the trash can icon to the right of the role name.
1. Click **Save**.

Do you have questions or feedback? Join the **#app-builder** channel on the [Datadog Community Slack](https://chat.datadoghq.com/).
