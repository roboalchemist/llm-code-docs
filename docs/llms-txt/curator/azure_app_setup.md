# Source: https://docs.curator.interworks.com/creating_integrations/power_bi_connection/azure_app_setup.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Azure Registered App Setup

> Step-by-step guide to set up Azure application registration for non-admin Power BI integration with Curator.

export const PowerBIConnectionSteps = ({currentStep}) => {
  const steps = [{
    number: 1,
    title: 'Azure Registered App Setup',
    path: '/creating_integrations/power_bi_connection/azure_app_setup',
    key: 'azure_app_setup'
  }, {
    number: 2,
    title: 'Azure Admin Registered App Setup',
    path: '/creating_integrations/power_bi_connection/azure_admin_app_setup',
    key: 'azure_admin_app_setup'
  }, {
    number: 3,
    title: 'Power BI Workspace Access',
    path: '/creating_integrations/power_bi_connection/power_bi_workspace_access',
    key: 'power_bi_workspace_access'
  }, {
    number: 4,
    title: 'Curator Connection',
    path: '/creating_integrations/power_bi_connection/curator_connection',
    key: 'curator_connection'
  }];
  return <ol>
      {steps.map(step => <li key={step.key}>
          {step.key === currentStep ? <strong>{step.title}</strong> : <a href={step.path}>{step.title}</a>}
        </li>)}
    </ol>;
};

## Steps

<PowerBIConnectionSteps currentStep="azure_app_setup" />

## Creating a Registered App within the Azure Portal

This registered app will be used for authentication to the Power BI non-admin APIs on behalf of users accessing Power BI content within Curator.

1. Log in to the [Azure Portal](https://portal.azure.com);

2. Search for “App Registrations” to start the process.  You may also find them inside the *Microsoft Entra ID* > *Manage* > *App Registrations*.

3. Click the button to register a new application.

4. Give the app a distinct and descriptive name and provide a redirect URI during this process under the "Web" platform.  The redirect URI should follow
   this format:

   `https://curatorexample.com/powerbi`

   <Warning>
     If the redirect URI is not configured correctly, users will see an error like:

     `AADSTS50011: The redirect URI specified in the request does not match the redirect URIs configured for the application.`

     **To fix this:**

     1. Go to [Azure Portal](https://portal.azure.com)
     2. Find your app registration
     3. Click **Manage** > **Authentication (Preview)** in the left navigation
     4. Add a **Web** redirect URI using your Curator portal's domain with the `/powerbi` suffix (e.g., `https://curatorexample.com/powerbi`)
   </Warning>

5. Once the app is registered, make note of the following details from the “Overview” page as you will need them when
   setting up the configuration on Curator:
   * Application (client) ID
   * Directory (tenant) ID
   * Application ID URI

## API Permissions

Your InterWorks Curator Azure Registered App will need several delegated API permissions.  While still viewing the
registered app, click on *Manage* > *API permissions* in the left navigation.  Add the following permissions as delegated
permissions:

* Microsoft Graph
  * User.Read
* Power BI Service
  * Dashboard.Read.All
  * Dataset.Read.All
  * Report.Read.All
  * Workspace.Read.All

If you intend to use **persistent filters** or other functionality that tracks user state, you'll also need to add:

* Power BI Service
  * UserState.ReadWrite.All

<Note>
  Depending on your level of access, you may need to ask Azure administrators to grant admin consent for these permissions.
</Note>

## Create a Client Secret

1. While still viewing the registered app, click on *Manage* > *Certificates & secrets* in the left navigation.
2. Click the button to add a new client secret.
3. Fill in the description and adjust the expiration date as desired, and click the save button.
4. Copy the client secret **value** and document it in a secure place.
   <Info>You will not be able to retrieve the value again once you leave this screen.</Info>
   <Warning>Do not confuse this with the *Secret ID*.  Curator must have the secret *value* to authenticate.</Warning>
