# Source: https://docs.curator.interworks.com/creating_integrations/power_bi_connection/curator_connection.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Curator Connection

> Final setup steps to create and configure the Power BI connection within Curator backend.

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

export const BackendNavPath = ({levelOne, levelTwo, levelThree, tab, section}) => {
  const levels = [levelOne, levelTwo, levelThree].filter(Boolean);
  const lastLevel = levels.length ? levels[levels.length - 1] : '';
  return <span>
      In the <a href="/setup/installation/linux_installation">backend of Curator</a> using the left-hand navigation,
      navigate to the
      {levelOne && <strong>{" " + levelOne}</strong>}
      {levelOne && levelTwo && " > "}
      {levelTwo && <strong>{levelTwo}</strong>}
      {levelTwo && levelThree && " > "}
      {levelThree && <strong>{levelThree}</strong>} page.
      {(tab || section) && <>
          {" "}On the {lastLevel} page
          {tab && <> click the <strong>{tab}</strong> tab</>}
          {tab && section && " and"}
          {section && <> expand the <strong>{section}</strong> section</>}.
        </>}
    </span>;
};

## Steps

<PowerBIConnectionSteps currentStep="curator_connection" />

## Creating Curator Connection to Power BI

Note: You will need details from your non-admin registered app and your admin registered app.  See steps 1-3 above if you have not configured those yet.

If your Curator license allows you to connect to Power BI, you can connect to it by following this process:

1. <BackendNavPath levelOne="Integrations" levelTwo="Connections" />
2. Click the button at the top to create a new connection.
3. From here, fill out the details under the *Power BI Connection* section, then click save.  The first 3 fields need to be
   filled in, but the 2 admin fields are highly recommended because they will lead to a better overall experience.

   * **Client ID**: "Application (client) ID" from the non-admin registered app (see [Azure App Setup](/creating_integrations/power_bi_connection/azure_app_setup)).
   * **Tenant ID**: "Directory (tenant) ID" from the non-admin registered app (see [Azure App Setup](/creating_integrations/power_bi_connection/azure_app_setup)).
   * **Client Secret**: "Client secret" value (again, not the client secret ID) from the non-admin registered app (see [Azure App Setup](/creating_integrations/power_bi_connection/azure_app_setup)).
   * **Admin Client ID**: "Application (client) ID" from the *admin* registered app (see [Azure Admin App Setup](/creating_integrations/power_bi_connection/azure_admin_app_setup)).
   * **Admin Client Secret**: "Client secret" value (again, not the client secret ID) from the *admin* registered app (see [Azure Admin App Setup](/creating_integrations/power_bi_connection/azure_admin_app_setup)).
4. Refresh the page after saving and you should see a Power BI section show up in the left navigation.

### Validate a successful connection

* The admin registered app connection was successful if the dropdowns in the backend under **Power BI** > **Reports** >
  **Create** a new report populate.
* The non-admin registered app connection was successful if reports load in the frontend.  Be sure to log out of the frontend and log back in fresh.

If you run into any issues, you can refer to the [Troubleshooting Power BI Access](./troubleshooting_power_bi_access) documentation for help.
