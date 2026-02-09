# Source: https://infisical.com/docs/integrations/secret-syncs/databricks.md

# Source: https://infisical.com/docs/integrations/app-connections/databricks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Databricks Connection

> Learn how to configure a Databricks Connection for Infisical.

Infisical supports the use of [service principals](https://docs.databricks.com/en/admin/users-groups/service-principals.html) to connect with your Databricks workspaces.

## Configure a Service Principal for Infisical

<Steps>
  <Step title="Databricks Workspace Settings">
    Navigate to your Databricks Workspace **Settings** via the dropdown in the top right.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/databricks/workspace-settings.png" alt="Workspace Settings Page" />
  </Step>

  <Step title="Manage Service Principals">
    Under the **Identity & Access** tab, click the **Manage** button in the **Service Principals** section.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/databricks/manage-service-principals.png" alt="Manage Service Principals" />
  </Step>

  <Step title="Service Principal Management">
    Click the **Add Service Principal** button.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/databricks/add-service-principal.png" alt="Add Service Principal" />
  </Step>

  <Step title="Add Service Principal">
    Select the **Add New** option and create a service principal for Infisical.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/databricks/create-service-principal.png" alt="Create Service Principal" />
  </Step>

  <Step title="Generate Service Principal Secret">
    Click on your new service principal, select the **Secrets** tab and click the **Generate Secret** button.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/databricks/service-principal-secrets.png" alt="Generate Secret" />
  </Step>

  <Step title="Service Principal Secret">
    Copy your service principal **Secret** and **Client ID** for use in the following steps.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/databricks/service-principal-ids.png" alt="Generate Secret" />
  </Step>
</Steps>

<Accordion title="Configure Permissions for Secret Rotation">
  <Steps>
    <Step title="Add Service Principal to Admin Group">
      Navigate to **Settings** > **Identity & Access** > **Groups** and select the admin group (typically named "admins" or "workspace-admins").

            <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/databricks/admin-group.png" alt="Admin Group" />

      Click **Add** and select the service principal you created for Infisical to add it to the admin group.

      <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/databricks/add-to-admin-group.png" alt="Add to Admin Group" />
      <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/databricks/add-to-admin-group-form.png" alt="Add to Admin Group Modal" />
    </Step>

    <Step title="Grant Manage Permission for Target Service Principals">
      For each service principal whose secrets you want to rotate, navigate to **Settings** > **Identity & Access** > **Service Principals** and select the target service principal.

            <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/databricks/select-target-service-principal.png" alt="Select Target Service Principal" />
    </Step>

    <Step title="Open Permissions Tab">
      Click on the **Permissions** tab for the selected service principal. And then click the **Grant access** button to open the permission modal

            <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/databricks/permissions-tab.png" alt="Permissions Tab" />
    </Step>

    <Step title="Grant Manage Permission to Infisical Service Principal">
      In the **User, Group or Service Principal** field, select the service principal you created for Infisical. In the **Permission** field, select **Manage** to allow the Infisical service principal to manage credentials and secrets for this service principal. Click **Save** to apply the permissions. Repeat these steps for each service principal whose secrets you want to rotate.

            <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/databricks/assign-manage-permission.png" alt="Assign Manage Permission" />
    </Step>
  </Steps>
</Accordion>

## Setup Databricks Connection in Infisical

<Steps>
  <Step title="Navigate to App Connections">
    Navigate to the **Integrations** tab in the desired project, then select **App Connections**. <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/general/add-connection.png" alt="App Connections
    Tab" />
  </Step>

  <Step title="Add Connection">
    Select the **Databricks Connection** option from the connection options modal.
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/databricks/select-databricks-connection.png" alt="Select Databricks
    Connection" />
  </Step>

  <Step title="Authorize Connection">
    Select the **Service Principal** method, add your **workspace URL** and **service principal credentials**, then click **Connect to
    Databricks**. <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/databricks/create-databricks-service-principal-method.png" alt="Connect via Databricks
    service principal" />
  </Step>

  <Step title="Connection Created">
    Your **Databricks Connection** is now available for use. <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/databricks/databricks-service-principal-connection.png" alt="Databricks Service Principal
    Connection" />
  </Step>
</Steps>
