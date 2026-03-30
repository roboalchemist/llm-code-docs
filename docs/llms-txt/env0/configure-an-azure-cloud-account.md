# Source: https://docs.envzero.com/guides/cloud-compass/cloud-compass/configure-an-azure-cloud-account.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configure an Azure Cloud Account

> Connect your Azure subscription to env zero Cloud Compass using activity logs and Log Analytics

## Configure a Cloud Account

<img src="https://mintcdn.com/envzero-b61043c8/DEMw5onAg75H1sCr/images/guides/cloud-compass/cloud-compass/eab87935ae549248283cdc93a2c6b339ca4e267b39929cf7b41b084368d683d6-image.png?fit=max&auto=format&n=DEMw5onAg75H1sCr&q=85&s=b0f94b2f581709c5849e39c684e80f52" alt="" width="2132" height="1190" data-path="images/guides/cloud-compass/cloud-compass/eab87935ae549248283cdc93a2c6b339ca4e267b39929cf7b41b084368d683d6-image.png" />

## Requirements

### Export Activity Logs to an Azure Log Activity Workspace

* Open the Azure Console and login to the relevant tenant

* Go to the *Activity Log* service

* Follow [Azure official procedure](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/activity-log?tabs=powershell#send-to-log-analytics-workspace) to send the activity logs to a Log Analytics Workspace

* env zero reads and uses the *Administrative* logs only:

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/DEMw5onAg75H1sCr/images/guides/cloud-compass/cloud-compass/ce2e715b63d1cd05d8293f31dc78283280816b65524179ba214366aab83db42e-image.png?fit=max&auto=format&n=DEMw5onAg75H1sCr&q=85&s=983bf496f90e4a77686b0f436299d021" alt="Interface screenshot showing configuration options" width="1104" height="474" data-path="images/guides/cloud-compass/cloud-compass/ce2e715b63d1cd05d8293f31dc78283280816b65524179ba214366aab83db42e-image.png" />
</Frame>

### Grant permissions to env zero via OIDC

* Open the Azure Console and login to the relevant tenant
* Go to the *Microsoft Entra ID* service
* Follow [this procedure](/guides/integrations/oidc-integrations/oidc-with-azure/#azure-ad-app--federated-credential) to configure a proper *App registration*
* After the App registration is created, Go to the *Log Analytics Workspaces* service
* Select the relevant Log Analytics Workspace, and select *Access Control (IAM)* from the left pane menu

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/DEMw5onAg75H1sCr/images/guides/cloud-compass/cloud-compass/8f6d9c134d66017ba5849eabf46c7ab4d907d67752d4f90c65e0c8d9effafef2-image.png?fit=max&auto=format&n=DEMw5onAg75H1sCr&q=85&s=70b67ad69b71ab0ce11ec57abb47ec00" alt="Interface screenshot showing configuration options" width="915" height="628" data-path="images/guides/cloud-compass/cloud-compass/8f6d9c134d66017ba5849eabf46c7ab4d907d67752d4f90c65e0c8d9effafef2-image.png" />
</Frame>

* Click *+ Add* and select *Add role assignment*
* Add the **Log Analytics Reader** permission to the relevant App registration

To enrich the data and provide better insights into the account, the **Application.Read.All** permission is required. This permission enables the app to retrieve Azure AD application details, helping map app IDs to human-readable names for better account understanding.

#### Adding the Permission in Azure Portal

1. Go to **Azure Active Directory** in the Azure portal.
2. Select your app under **App registrations**.
3. Navigate to **API permissions**, click **Add a permission**, select **Microsoft Graph**, choose **Application permissions**, and add **Application.Read.All**.
4. Click **Grant admin consent for \<Tenant Name>** under **Configured permissions**. You must have a role like Global Administrator to perform this action.

#### Adding the Permission with Azure CLI

You can also use the Azure CLI for this:

1. Add the permission:

   ```bash  theme={null}
   az ad app permission add --id <APP_ID> --api 00000003-0000-0000-c000-000000000000 --api-permissions 311a71cc-e848-46a1-bdf8-97ff7156d8e6=Role
   ```

2. Grant admin consent:

   ```bash  theme={null}
   az ad app permission grant --id <APP_ID> --api 00000003-0000-0000-c000-000000000000
   ```

Built with [Mintlify](https://mintlify.com).
