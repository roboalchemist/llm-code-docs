# Source: https://docs.curator.interworks.com/creating_integrations/power_bi_connection/power_bi_workspace_access.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Power BI Workspace Access

> Configure workspace permissions for Power BI integration with Curator.

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

<PowerBIConnectionSteps currentStep="power_bi_workspace_access" />

## A Note on Terminology

The terms "registered app", "service principal", and "client" are technically not the same thing, however, for the
purposes of this documentation you can think of them as the same thing.  Similarly, "Power BI" and "Fabric" can also be
considered the same things for the purposes of this documentation. If you already understand the differences, you
probably also understand how to adjust the steps outlined in this documentation to meet your own needs.

## Allow service principals to use Fabric APIs

The registered apps created in the previous steps need to be able to access Power BI APIs in order to query which
workspaces, Dashboard, reports, etc. exist in your environment when publishing content to Curator.

To enable the Power BI APIs:

1. Log in to the [Power BI portal](https://app.powerbi.com) with an account that has access to the admin portal.
2. Navigate to the [admin portal](https://app.powerbi.com/admin-portal) by clicking on the gear icon at the top right.
3. Select "Tenant Settings" on the left if not already selected.
4. Scroll to the "Developer settings" section and expand the "Allow service principals to use Fabric APIs" group.
5. Click the switch to enable.  If desired, restrict access to only specific security groups (make sure the registered
   apps that Curator will be using are included in a security group specified here).
   <Note>Enabling this setting may take \~15 minutes to take effect.</Note>

## Allow service principals to access read-only admin APIs

The admin registered app needs read-only access to the Power BI Admin APIs in order to query permissions, etc. on behalf of
Power BI users.

To enable the read-only admin APIs:

1. Log in to the [Power BI portal](https://app.powerbi.com) with an account that has access to the admin portal.
2. Navigate to the [admin portal](https://app.powerbi.com/admin-portal) by clicking on the gear icon at the top right.
3. Select "Tenant Settings" on the left if not already selected.
4. Scroll to the "Admin API settings" section and expand the "Service principals can access read-only admin APIs" group.
5. Click the switch to enable.  If desired, restrict access to only specific security groups (make sure the admin registered app that Curator will be using is included in a security group specified here).
   <Note>Enabling this setting may take \~15 minutes to take effect.</Note>

## Add Registered Apps to Power BI Workspace(s)

In order for the non-admin and admin registered apps to have access to your Power BI content, they must have
permissions to the Power BI workspace(s) you intend to use with Curator.

To add access to a workspace:

1. Log in to the [Power BI portal](https://app.powerbi.com).
2. In the left navigation, click on “Workspaces”.
3. Hover your mouse over one of the workspaces and click on the 3 dots that appear on the right.  Choose “Workspace access”.
4. Search for the non-admin registered app name and give it the "Admin" permission.  This ensures Curator will
   have access to add any content from Power BI that your Curator admins would like to add.
5. Repeat step 4 for the admin registered app name, also giving it "Admin" permission.
6. (optional) Repeat steps 2-5 for any remaining workspaces that need access.

<Note>
  There are other paths to get to the screens mentioned above, but there have been times when those paths
  don't work correctly. The steps above are the most reliable way to get to the correct screens.
</Note>
