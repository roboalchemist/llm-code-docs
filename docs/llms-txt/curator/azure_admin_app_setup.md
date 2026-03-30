# Source: https://docs.curator.interworks.com/creating_integrations/power_bi_connection/azure_admin_app_setup.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Azure Admin Registered App Setup

> Step-by-step guide to set up Azure application registration for Power BI's Admin API integration with Curator.

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

<PowerBIConnectionSteps currentStep="azure_admin_app_setup" />

## Creating a registered app for the admin API within the Azure Portal

This will be a very similar process to creating the non-admin registered app in the previous step, but this registered app will
be used for authentication to the read-only Power BI **Admin API** for Curator to be able to check permissions, etc. on behalf of
Power BI users.

1. Log in to the [Azure Portal](https://portal.azure.com);
2. Search for “App Registrations” to start the process.  You may also find them inside the *Microsoft Entra ID* > *Manage* > *App Registrations*.
3. Click the button to register a new application.
4. Add a distinct and descriptive name. It's suggested to clarify that this is for the Admin API (e.g. "Curator Power BI Admin API App").
   * You should skip the "Redirect URI" step for this registered app as it will not be used.
     <Note>Make sure to create this app registration under the same Azure tenant as the non-admin registered app created previously.</Note>
5. Once the app is registered, make note of the following details from the “Overview” page as you will need them when
   setting up the configuration on Curator:
   * Application (client) ID - This will be used as the **Admin Client ID** in Curator.
   * Directory (tenant) ID - This should be the same as the tenant ID used for the registered app.

## API Permissions

<Warning>Do **not** add any API permissions to this registered app.  It does not need permissions assigned in order to access
the read-only admin APIs, and in fact adding them will actually prevent it from being able to access those APIs.</Warning>

## Create a Client Secret

1. While still viewing the admin registered app, click on *Manage* > *Certificates & secrets* in the left navigation.
2. Click the button to add a new client secret.  This will be used as the **Admin Client Secret** in Curator.
3. Fill in the description and adjust the expiration date as desired, and click the save button.
4. Copy the client secret **value** and document it in a secure place.
   <Info>You will not be able to retrieve the value again once you leave this screen.</Info>
   <Warning>Do not confuse this with the *Secret ID*.  Curator must have the secret *value* to authenticate.</Warning>
