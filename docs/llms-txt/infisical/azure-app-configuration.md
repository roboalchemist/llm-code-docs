# Source: https://infisical.com/docs/integrations/secret-syncs/azure-app-configuration.md

# Source: https://infisical.com/docs/integrations/cloud/azure-app-configuration.md

# Source: https://infisical.com/docs/integrations/app-connections/azure-app-configuration.md

# Source: https://infisical.com/docs/integrations/secret-syncs/azure-app-configuration.md

# Source: https://infisical.com/docs/integrations/cloud/azure-app-configuration.md

# Source: https://infisical.com/docs/integrations/app-connections/azure-app-configuration.md

# Azure App Configuration Connection

> Learn how to configure a Azure App Configuration Connection for Infisical.

Infisical currently only supports two methods for connecting to Azure, which are OAuth and Client Secrets.

<Accordion title="Self-Hosted Instance">
  Using the Azure App Configuration connection on a self-hosted instance of Infisical requires configuring an application in Azure
  and registering your instance with it.

  **Prerequisites:**

  * Set up Azure and have an existing App Configuration instance.

  <Steps>
    <Step title="Create an application in Azure">
      Navigate to Azure Active Directory > App registrations to create a new application.

      <Info>
        Azure Active Directory is now Microsoft Entra ID.
      </Info>

      <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/azure-app-configuration/config-aad.png" alt="Azure app config" />
      <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/azure-app-configuration/config-new-app.png" alt="Azure app config" />

      Create the application. As part of the form, set the **Redirect URI** to `https://your-domain.com/organization/app-connections/azure/oauth/callback`.

      <Tip>
        The domain you defined in the Redirect URI should be equivalent to the `SITE_URL` configured in your Infisical instance.
      </Tip>

            <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/azure/register-callback.png" alt="Azure app config" />
    </Step>

    <Step title="Assign API permissions to the application">
      For the Azure Connection to work with App Configuration, you need to assign multiple permissions to the application.

      #### Azure App Configuration permissions

      Set the API permissions of the Azure application to include the following Azure App Configuration permissions: `KeyValue.Delete`, `KeyValue.Read`, and `KeyValue.Write`.
      <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/azure-app-configuration/app-api-permissions.png" alt="Azure app config" />
    </Step>

    <Step title="Add your application credentials to Infisical">
      Obtain the **Application (Client) ID** in Overview and generate a **Client Secret** in Certificate & secrets for your Azure application.

      <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/azure-app-configuration/config-credentials-1.png" alt="Azure app config" />
      <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/azure-app-configuration/config-credentials-2.png" alt="Azure app config" />
      <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/azure-app-configuration/config-credentials-3.png" alt="Azure app config" />

      Back in your Infisical instance, add two new environment variables for the credentials of your Azure application.

      * `INF_APP_CONNECTION_AZURE_APP_CONFIGURATION_CLIENT_ID`: The **Application (Client) ID** of your Azure application.
      * `INF_APP_CONNECTION_AZURE_APP_CONFIGURATION_CLIENT_SECRET`: The **Client Secret** of your Azure application.

      Once added, restart your Infisical instance and use the Azure App Configuration connection.
    </Step>
  </Steps>
</Accordion>

<Accordion title="Client Secret Authentication">
  To use client secret authentication, ensure your Azure Service Principal has the required permissions and is connected to the Azure App Configuration resources you want to use.

  **Prerequisites:**

  * Set up Azure and have an existing App Configuration instance.
  * The service principal must be connected to your target Azure App Configuration resource(s)

  <Steps>
    <Step title="Assign API permissions to the service principal">
      Configure the required API permissions for your App Registration to interact with Azure App Configuration:

      #### Azure App Configuration permissions

      Set the API permissions of your Azure service principal to include the following Azure App Configuration permissions: `KeyValue.Delete`, `KeyValue.Read`, and `KeyValue.Write`.

            <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/azure-app-configuration/app-api-permissions.png" alt="Azure app config" />
    </Step>
  </Steps>
</Accordion>

## Setup Azure Connection in Infisical

<Steps>
  <Step title="Navigate to App Connections">
    Navigate to the **App Connections** page in the desired project. <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/general/add-connection.png" alt="App Connections
    Tab" />
  </Step>

  <Step title="Add Connection">
    Select the **Azure Connection** option from the connection options modal. <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/azure/app-configuration/select-connection.png" alt="Select Azure Connection" />
  </Step>

  <Step title="Create Connection">
    <Tabs>
      <Tab title="OAuth">
        <Step title="Authorize Connection">
          You can optionally authenticate against a specific tenant by providing the Azure Tenant or Directory ID.

          Now select the **OAuth** method and click **Connect to Azure**.

                    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/azure/app-configuration/create-oauth-method.png" alt="Connect via Azure OAUth" />
        </Step>

        <Step title="Grant Access">
          You will then be redirected to Azure to grant Infisical access to your Azure account. Once granted,
          you will redirect you back to Infisical's App Connections page. <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/azure/grant-access.png" alt="Azure App Configuration
          Authorization" />
        </Step>
      </Tab>

      <Tab title="Client Secret">
        <Step title="Create Connection">
          Fill in the **Tenant ID**, **Client ID** and **Client Secret** fields with the Directory (Tenant) ID, Application (Client) ID and Client Secret you obtained in the previous step.

                    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/azure/app-configuration/create-client-secrets-method.png" alt="Connect via Azure OAUth" />
        </Step>
      </Tab>
    </Tabs>
  </Step>

  <Step title="Connection Created">
    Your **Azure App Configuration Connection** is now available for use. <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/app-connections/azure/app-configuration/oauth-connection.png" alt="Assume Role AWS Connection" />
  </Step>
</Steps>
