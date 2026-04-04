# Source: https://infisical.com/docs/documentation/platform/workflow-integrations/microsoft-teams-integration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Microsoft Teams Integration

> Learn how to setup the Microsoft Teams integration

This guide will provide step by step instructions on how to configure Microsoft Teams integration for your Infisical projects.

## Setting up Microsoft Teams integration in your projects

<Tabs>
  <Tab title="Infisical Cloud">
    ### Create Microsoft Teams workflow integration

    <Steps>
      <Step title="Install the Infisical Microsoft Teams App in Microsoft Teams tenant">
        Currently, Infisical requires you to install a custom Microsoft Teams app into your Microsoft Teams tenant.

        You can download the Infisical Microsoft Teams app package here:

        * [Infisical Microsoft Teams app package](https://infisical-microsoft-teams-app.s3.us-east-1.amazonaws.com/Infisical.zip)

        <Note>
          **Important for self-hosted users:**

          If you're self-hosting Infisical, you can skip the download step. Instead you should use the app package file you downloaded from the Microsoft Teams Developer Portal when you followed the Self-hosted guide.
        </Note>

        Once you've downloaded the app package, you can install the app in your Microsoft Teams tenant by navigating to the **Apps** > **Upload a custom app** page, and selecting the "Upload an app" button.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/workflow-integrations/microsoft-teams-integration/microsoft-teams-install-app.png" alt="microsoft-teams-install-app" />
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/workflow-integrations/microsoft-teams-integration/microsoft-teams-submit-app.png" alt="microsoft-teams-submit-app" />

        Once the app has been submitted, your Microsoft Teams tenant admin will need to approve the app in the [Microsoft Teams Admin Center](https://admin.teams.microsoft.com/policies/manage-apps).

        <Warning>
          After the app has been approved, it can take a few hours *(up to 24 hours in some cases)* for Microsoft Teams to reflect the new app. During this period, the Infisical app will not be visible in Microsoft Teams, and won't be usable.
        </Warning>

        Once the app has been approved, you will be able to use the Infisical Microsoft Teams integration in your projects.
      </Step>

      <Step title="Add the Infisical Microsoft Teams app to your Microsoft Teams teams">
        Once the app has been approved and installed in your Microsoft Teams tenant, you can add the app to your Microsoft Teams teams.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/workflow-integrations/microsoft-teams-integration/microsoft-teams-add-app.png" alt="microsoft-teams-add-app" />

        Navigate to **Apps** > **Built for your org**, select the "Infisical" app, and press the "Add" button to select the teams and channels you wish to add the app to.

        <Info>
          This can also be done later through the [Microsoft Teams Admin Center](https://admin.teams.microsoft.com/policies/manage-apps), or through the Microsoft Teams client itself by navigating to the individual team's app settings.
        </Info>

        Once the app has been added to the team, you will be able to use the Infisical Microsoft Teams integration in the team.
      </Step>

      <Step title="Navigate to the Workflow Integrations tab in your organization settings">
        After installing the Microsoft Teams app, you are now ready to configure the Microsoft Teams integration within Infisical.

        Navigate to the **Workflow Integrations** tab in your organization settings, and press the "Add" button.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/workflow-integrations/microsoft-teams-integration/infisical-org-overview.png" alt="org-integrations-overview" />
      </Step>

      <Step title="Create a Microsoft Teams workflow integration">
        In order to use the Infisical Microsoft Teams integration, you will need to grant admin consent to the app. Once the consent is granted, the Microsoft Teams workflow integration will be created in your Infisical organization.

        Press the "Add" button and select the "Microsoft Teams" platform option.
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/workflow-integrations/microsoft-teams-integration/infisical-org-add-microsoft-teams-integration.png" alt="add-microsoft-teams-integration" />

        Select the Microsoft Teams integration you wish to configure, and press the "Configure" button.

        Here you will be prompted to enter an alias, tenant ID, and an optional description for your workflow integration.
        The tenant ID is the ID of the Microsoft 365 / Azure AD tenant that you installed the Infisical Microsoft Teams app in, in the previous steps.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/workflow-integrations/microsoft-teams-integration/infisical-org-microsoft-teams-integration-modal.png" alt="configure-microsoft-teams-integration" />

        Press the "Create Microsoft Teams Integration" button, and you'll be navigated to the Azure AD consent page.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/workflow-integrations/microsoft-teams-integration/microsoft-consent-page.png" alt="microsoft-consent-page" />

        <Note>
          Please note that you must be a privileged administrator user of your Microsoft 365 / Azure AD tenant in order to grant admin consent to the app.
        </Note>

        Once you've granted admin consent, you'll be navigated back to the Infisical organization settings, where you can now select the Microsoft Teams integration you just created.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/workflow-integrations/microsoft-teams-integration/microsoft-teams-workflow-integration-created.png" alt="microsoft-teams-workflow-integration-created" />
      </Step>
    </Steps>

    ### Configure project to use Microsoft Teams workflow integration

    <Steps>
      <Step title="Navigate to the Workflow Integrations tab in the project settings">
        To add a new Microsoft Teams workflow integration, navigate to **Project Settings** > **Workflow Integrations** and press the "Add".
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/workflow-integrations/microsoft-teams-integration/infisical-project-settings.png" alt="project-settings-workflow-integrations" />

        Select the "Microsoft Teams" option from the list of available workflow integrations.
      </Step>

      <Step title="Configure the Microsoft Teams workflow integration">
        Your project will send notifications to the connected Microsoft Teams team of the
        selected Microsoft Teams integration when the configured events are triggered.

        Press the "Save" button to save your Microsoft Teams workflow integration.
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/workflow-integrations/microsoft-teams-integration/infisical-project-microsoft-teams-integration-save.png" alt="infisical-project-microsoft-teams-integration-save" />
      </Step>
    </Steps>

    Once you've created the project Microsoft Teams workflow integration, you will now receive Access Requests and Secret Approval Requests notifications in Microsoft Teams according to your configuration.
  </Tab>

  <Tab title="Self-hosted setup">
    ### Configure Azure Resources

    To create a Microsoft Teams bot, you must first create an Azure Bot from the Azure Marketplace, an app registration, and a Microsoft Teams app. The steps below document in detail how to create and configure these resources.

    <Steps>
      <Step title="Create Microsoft Teams app">
        Navigate to the [Microsoft Teams Developer Portal](https://dev.teams.microsoft.com/).

        Once you're on the Microsoft Teams Developer Portal, press the "Create a new app" button on the overview page. Give the bot a name and press the "Add" button.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/workflow-integrations/microsoft-teams-integration/teams-dev-portal-create-app.png" alt="microsoft-dev-portal" />
      </Step>

      <Step title="Create a Microsoft Teams bot">
        After creating the Microsoft Teams app, you'll need to create a Microsoft Teams bot.

        Navigate to the app's bot settings page and click "Create a new bot".

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/workflow-integrations/microsoft-teams-integration/teams-dev-portal-bot-app-feature.png" alt="microsoft-dev-portal-create-bot" />
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/workflow-integrations/microsoft-teams-integration/teams-dev-portal-create-a-new-bot.png" alt="microsoft-dev-portal-create-bot-2" />

        After clicking the "Create a new bot" button, you'll be navigated to the Teams Developer Portal for bot management. Press the "New bot" button, and enter the name of the bot.
        Please keep in mind that the name of the bot can only contain alphanumeric characters, dashes, and underscores.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/workflow-integrations/microsoft-teams-integration/teams-dev-portal-create-bot.png" alt="microsoft-dev-portal-create-bot-3" />
      </Step>

      <Step title="Add a message endpoint to the bot">
        After creating the bot, you'll need to add a message endpoint to the bot. Navigate to the "Configure" tab, and input the following endpoint under "Endpoint address":
        `https://<your-infisical-instance-url>/api/v1/workflow-integrations/microsoft-teams/message-endpoint`
        Replace `<your-infisical-instance-url>` with the URL of your Infisical instance.

        Press the "Save" button to save the changes.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/workflow-integrations/microsoft-teams-integration/teams-dev-portal-add-bot-endpoint.png" alt="microsoft-dev-portal-create-bot-4" />
      </Step>

      <Step title="Find the bot in Azure App Registrations">
        When you create a bot through the Teams Developer Portal, an Azure App Registration is also created.

        Open your [Azure Portal](https://portal.azure.com/) and navigate to the "App Registrations" section to find the newly created app registration.
        The name of the app registration will be the same as the name of the bot you created in the previous step.

        Press the app registration to open the app registration overview page.
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/workflow-integrations/microsoft-teams-integration/azure-app-registrations-bot.png" alt="azure-app-registrations" />
      </Step>

      <Step title="Add API Permissions to the App Registration">
        Navigate to the "API Permissions" section of the app registration, and add the following permissions:

        * `AppCatalog.Read.All`
        * `ChannelSettings.Read.All`
        * `MultiTenantOrganization.Read.All`
        * `Organization.Read.All`
        * `Team.ReadBasic.All`
        * `TeamsAppInstallation.Read.All`

        After adding the API permissions, press the "Grant admin consent" button to grant the permissions.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/workflow-integrations/microsoft-teams-integration/azure-app-registration-api-permissions.png" alt="azure-app-registration-api-permissions" />
      </Step>

      <Step title="Add a new web application to the App Registration">
        Navigate to the "Authentication" section of the App Registration, and press the "Add a platform" button. Select the "Web" platform and enter the following redirect URI:
        `https://<your-infisical-instance-url>/organization/settings/oauth/callback`. Replace `<your-infisical-instance-url>` with the URL of your Infisical instance.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/workflow-integrations/microsoft-teams-integration/azure-app-registration-register-callback.png" alt="azure-app-registration-register-callback" />
      </Step>

      <Step title="Get App Registration Client ID and Client Secret">
        Next we need to get the application client ID and create a new client secret. **Save these values for later, as they're required to configure the Microsoft Teams integration in Infisical.**

        **Get the Application (Client) ID**

        To get the Application (Client) ID, press the "Copy" button next to the "Application (client) ID" field.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/workflow-integrations/microsoft-teams-integration/azure-app-registration-copy-client-id.png" alt="copy-client-id" />

        **Create a new client secret**

        Create a new client secret within the app registration. Navigate to the "Certificates & Secrets" section of the app registration, and press the "New client secret" button.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/workflow-integrations/microsoft-teams-integration/azure-app-registration-create-client-secret.png" alt="create-client-secret" />

        <Warning>
          Remember to rotate your client secret before it expires. Consider setting up a reminder or automated process to replace the secret and update your Infisical configuration before expiration.
        </Warning>
      </Step>

      <Step title="Get the Microsoft Teams App ID">
        Navigate back to the [Microsoft Teams Developer Portal](https://dev.teams.microsoft.com/), and press the "Apps" tab and select the app you created earlier.
        Here you can find the Microsoft Teams App ID in the overview page, which you need to copy and save for later.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/workflow-integrations/microsoft-teams-integration/teams-dev-portal-copy-app-id.png" alt="microsoft-teams-app-id" />
      </Step>

      <Step title="Link the Microsoft Teams App to the bot">
        You need to link the Microsoft Teams App with the bot/app registration you created earlier.
        Inside the [Microsoft Teams Developer Portal](https://dev.teams.microsoft.com/), navigate to the "Bot" tab and select the bot you created earlier. Navigate to the "App Features" section, and press the "Bot" button.

        Under the "What can your bot do?" section, enable `Only send notifications (one-way conversations)`.

        Under the "Select the scopes where people can use your bot" section, select `Personal`, `Team`, and `Group Chat`.

        Finally, press the "Save" button to save the changes.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/workflow-integrations/microsoft-teams-integration/teams-dev-portal-bot-app-feature.png" alt="microsoft-teams-app-features" />
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/workflow-integrations/microsoft-teams-integration/teams-dev-portal-configure-bot.png" alt="microsoft-teams-configure-bot" />
      </Step>

      <Step title="Run an app validation test (Recommended)">
        To ensure that the Microsoft Teams App is working correctly, you can run an app validation test. This step is optional, but recommended to ensure the app is working correctly.

        You should expect to see two errors related to sending welcome messages, because we haven't configured the Microsoft Teams App inside Infisical yet, which is required for proactive messages.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/workflow-integrations/microsoft-teams-integration/teams-dev-portal-app-validation.png" alt="microsoft-teams-app-validation-test" />

        <Note>
          You may see manifest validation errors. Before running an app validation test, you must ensure that your app has all errors resolved, such as having a description and a valid name.
        </Note>

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/workflow-integrations/microsoft-teams-integration/teams-dev-portal-app-validation-result.png" alt="microsoft-teams-app-validation-test-results" />

        <Note>
          If you see two errors for bot welcome messages, you can ignore them. This is expected until you configure the Microsoft Teams App inside Infisical.
        </Note>
      </Step>

      <Step title="Download the App Package">
        Once the Microsoft Teams App is working correctly, you can download the app package by navigating to the "Publish to Store" page, and pressing the "Download app package" button.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/workflow-integrations/microsoft-teams-integration/teams-dev-portal-download-app-package.png" alt="microsoft-teams-download-app-package" />
      </Step>
    </Steps>

    ### Configure Microsoft Teams Bot in Infisical

    After creating the Microsoft Teams App and Bot, you are ready to configure the Microsoft Teams integration in Infisical.
    Please note that you must be an instance admin in order to configure the Microsoft Teams instance-wide settings.

    <Steps>
      <Step title="Navigate to the Integrations tab in your Server Admin Console settings">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/workflow-integrations/microsoft-teams-integration/infisical-server-admin-console-tab.png" alt="server-admin-console-tab" />
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/workflow-integrations/microsoft-teams-integration/infisical-instance-configure-microsoft-teams.png" alt="infisical-instance-configure-microsoft-teams" />

        Enter the values you saved from the earlier steps into the respective fields.

        * **Application (Client) ID**: The Client ID of the App Registration from the previous steps.
        * **Client Secret**: The Client Secret of the App Registration from the previous steps.
        * **Microsoft Teams App ID**: The App ID of the Microsoft Teams App from the previous steps.

        Once completed, press the "Save" button to save your changes.
      </Step>
    </Steps>

    ### Create Microsoft Teams workflow integration

    <Steps>
      <Step title="Install the Infisical Microsoft Teams App in Microsoft Teams tenant">
        Currently, Infisical requires you to install a custom Microsoft Teams app into your Microsoft Teams tenant.

        You can download the Infisical Microsoft Teams app package here:

        * [Infisical Microsoft Teams app package](https://infisical-microsoft-teams-app.s3.us-east-1.amazonaws.com/Infisical.zip)

        <Note>
          **Important for self-hosted users:**

          If you're self-hosting Infisical, you can skip the download step. Instead you should use the app package file you downloaded from the Microsoft Teams Developer Portal when you followed the Self-hosted guide.
        </Note>

        Once you've downloaded the app package, you can install the app in your Microsoft Teams tenant by navigating to the **Apps** > **Upload a custom app** page, and selecting the "Upload an app" button.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/workflow-integrations/microsoft-teams-integration/microsoft-teams-install-app.png" alt="microsoft-teams-install-app" />
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/workflow-integrations/microsoft-teams-integration/microsoft-teams-submit-app.png" alt="microsoft-teams-submit-app" />

        Once the app has been submitted, your Microsoft Teams tenant admin will need to approve the app in the [Microsoft Teams Admin Center](https://admin.teams.microsoft.com/policies/manage-apps).

        <Warning>
          After the app has been approved, it can take a few hours *(up to 24 hours in some cases)* for Microsoft Teams to reflect the new app. During this period, the Infisical app will not be visible in Microsoft Teams, and won't be usable.
        </Warning>

        Once the app has been approved, you will be able to use the Infisical Microsoft Teams integration in your projects.
      </Step>

      <Step title="Add the Infisical Microsoft Teams app to your Microsoft Teams teams">
        Once the app has been approved and installed in your Microsoft Teams tenant, you can add the app to your Microsoft Teams teams.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/workflow-integrations/microsoft-teams-integration/microsoft-teams-add-app.png" alt="microsoft-teams-add-app" />

        Navigate to **Apps** > **Built for your org**, select the "Infisical" app, and press the "Add" button to select the teams and channels you wish to add the app to.

        <Info>
          This can also be done later through the [Microsoft Teams Admin Center](https://admin.teams.microsoft.com/policies/manage-apps), or through the Microsoft Teams client itself by navigating to the individual team's app settings.
        </Info>

        Once the app has been added to the team, you will be able to use the Infisical Microsoft Teams integration in the team.
      </Step>

      <Step title="Navigate to the Workflow Integrations tab in your organization settings">
        After installing the Microsoft Teams app, you are now ready to configure the Microsoft Teams integration within Infisical.

        Navigate to the **Workflow Integrations** tab in your organization settings, and press the "Add" button.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/workflow-integrations/microsoft-teams-integration/infisical-org-overview.png" alt="org-integrations-overview" />
      </Step>

      <Step title="Create a Microsoft Teams workflow integration">
        In order to use the Infisical Microsoft Teams integration, you will need to grant admin consent to the app. Once the consent is granted, the Microsoft Teams workflow integration will be created in your Infisical organization.

        Press the "Add" button and select the "Microsoft Teams" platform option.
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/workflow-integrations/microsoft-teams-integration/infisical-org-add-microsoft-teams-integration.png" alt="add-microsoft-teams-integration" />

        Select the Microsoft Teams integration you wish to configure, and press the "Configure" button.

        Here you will be prompted to enter an alias, tenant ID, and an optional description for your workflow integration.
        The tenant ID is the ID of the Microsoft 365 / Azure AD tenant that you installed the Infisical Microsoft Teams app in, in the previous steps.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/workflow-integrations/microsoft-teams-integration/infisical-org-microsoft-teams-integration-modal.png" alt="configure-microsoft-teams-integration" />

        Press the "Create Microsoft Teams Integration" button, and you'll be navigated to the Azure AD consent page.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/workflow-integrations/microsoft-teams-integration/microsoft-consent-page.png" alt="microsoft-consent-page" />

        <Note>
          Please note that you must be a privileged administrator user of your Microsoft 365 / Azure AD tenant in order to grant admin consent to the app.
        </Note>

        Once you've granted admin consent, you'll be navigated back to the Infisical organization settings, where you can now select the Microsoft Teams integration you just created.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/workflow-integrations/microsoft-teams-integration/microsoft-teams-workflow-integration-created.png" alt="microsoft-teams-workflow-integration-created" />
      </Step>
    </Steps>

    ### Configure project to use Microsoft Teams workflow integration

    <Steps>
      <Step title="Navigate to the Workflow Integrations tab in the project settings">
        To add a new Microsoft Teams workflow integration, navigate to **Project Settings** > **Workflow Integrations** and press the "Add".
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/workflow-integrations/microsoft-teams-integration/infisical-project-settings.png" alt="project-settings-workflow-integrations" />

        Select the "Microsoft Teams" option from the list of available workflow integrations.
      </Step>

      <Step title="Configure the Microsoft Teams workflow integration">
        Your project will send notifications to the connected Microsoft Teams team of the
        selected Microsoft Teams integration when the configured events are triggered.

        Press the "Save" button to save your Microsoft Teams workflow integration.
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/workflow-integrations/microsoft-teams-integration/infisical-project-microsoft-teams-integration-save.png" alt="infisical-project-microsoft-teams-integration-save" />
      </Step>
    </Steps>

    Once you've created the project Microsoft Teams workflow integration, you will now receive Access Requests and Secret Approval Requests notifications in Microsoft Teams according to your configuration.
  </Tab>
</Tabs>

## Troubleshooting

<Accordion title="Notifications are not being sent to Microsoft Teams even though the integration is configured">
  If you recently added the Microsoft Teams app to your tenant, **it may take up to 24 hours for Microsoft Teams to propagate the changes.**
  A common indication of propagation issues is that the workflow integration is shown as "Installed", and you're able to view the teams and channels when configuring the workflow integration on your project, but no notification is being sent.
</Accordion>

<Accordion title="Workflow Integration is stuck on 'Pending' status">
  The workflow integration can get stuck on Pending if you created the workflow integration before the Infisical Microsoft Teams bot was installed in the tenant.
  To resolve this, make sure you have installed the Infisical Microsoft Teams app in your tenant.

  You can manually recheck the installation status by pressing the "Check Installation Status" button in the workflow organization settings.

    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/workflow-integrations/microsoft-teams-integration/microsoft-teams-check-installation-status.png" alt="microsoft-teams-check-installation-status" />
</Accordion>
