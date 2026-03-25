# Source: https://docs.envzero.com/guides/admin-guide/user-role-and-team-management/role-assignment.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Assigning Roles

> Assign roles to users and teams at organization, project, and environment levels in env zero

Roles can be assigned at three levels: organization, project, and environment.

## Assigning Organization Roles

Organization roles can be assigned to both individual users and teams, and apply across the entire organization (including all projects and environments).

### Assigning Organization Roles to Users

<Steps>
  <Step title="Navigate to Organization Settings">
    Go to **Organization Settings** > **Users** tab.
  </Step>

  <Step title="Select User Role">
    Locate the user in the table and click the **Role** dropdown for that user.
  </Step>

  <Step title="Choose Role">
    Select from the available roles in the dropdown:

    * Default roles: [Organization User](/guides/admin-guide/user-role-and-team-management/default-roles#organization-user), [Organization Admin](/guides/admin-guide/user-role-and-team-management/default-roles#organization-admin)
    * Custom roles: Any custom roles created for your organization

    <Info>
      **Role Dropdown Organization**: Default roles are listed first, followed by a separator, then custom roles in alphabetical order.
    </Info>
  </Step>

  <Step title="Save Changes">
    Click **SAVE** to apply the changes.
  </Step>
</Steps>

<img src="https://mintcdn.com/envzero-b61043c8/ngeLWWxxE3C57X-b/images/guides/admin-guide/user-role-and-team-management/org-user-role-assignment.png?fit=max&auto=format&n=ngeLWWxxE3C57X-b&q=85&s=41a5e370ce84125bae9cefe83e52ea7f" alt="Organization User Role Assignment" width="1721" height="877" data-path="images/guides/admin-guide/user-role-and-team-management/org-user-role-assignment.png" />

### Assigning Organization Roles to Teams

<Steps>
  <Step title="Navigate to Organization Settings">
    Go to **Organization Settings** > **Teams** tab.
  </Step>

  <Step title="Select Team Role">
    Locate the team in the table and click the **Role** dropdown for that team.
  </Step>

  <Step title="Choose Role">
    Select from the available roles:

    * Default roles: [Organization User](/guides/admin-guide/user-role-and-team-management/default-roles#organization-user), [Organization Admin](/guides/admin-guide/user-role-and-team-management/default-roles#organization-admin)
    * Custom roles: Any custom roles created for your organization
  </Step>

  <Step title="Save Changes">
    Click **SAVE** to apply the changes.
  </Step>
</Steps>

<img src="https://mintcdn.com/envzero-b61043c8/ngeLWWxxE3C57X-b/images/guides/admin-guide/user-role-and-team-management/org-team-role-assignment.png?fit=max&auto=format&n=ngeLWWxxE3C57X-b&q=85&s=5cdf07db3bb6d5f2c152d21faa139c2c" alt="Organization Team Role Assignment" width="1719" height="697" data-path="images/guides/admin-guide/user-role-and-team-management/org-team-role-assignment.png" />

## Assigning Project Roles

Project roles can be assigned to both users and teams and apply to a specific project, all its sub-projects, and all environments within them.

### Assigning Project Roles to Users

<Steps>
  <Step title="Navigate to Project Settings">
    Go to **Project Settings** > **Users** tab.
  </Step>

  <Step title="Select User">
    Locate the user in the table and check the checkbox in the **Assign** column.
  </Step>

  <Step title="Choose Role">
    Click the **Role** dropdown that appears and select from the available roles:

    * Default roles: [Project Viewer](/guides/admin-guide/user-role-and-team-management/default-roles#project-viewer), [Project Planner](/guides/admin-guide/user-role-and-team-management/default-roles#project-planner), [Project Deployer](/guides/admin-guide/user-role-and-team-management/default-roles#project-deployer), [Project Admin](/guides/admin-guide/user-role-and-team-management/default-roles#project-admin)
    * Custom roles: Any custom roles created for your organization
  </Step>

  <Step title="Save Changes">
    Click **SAVE** to apply the changes.
  </Step>
</Steps>

<img src="https://mintcdn.com/envzero-b61043c8/ngeLWWxxE3C57X-b/images/guides/admin-guide/user-role-and-team-management/project-user-role-assignment.png?fit=max&auto=format&n=ngeLWWxxE3C57X-b&q=85&s=bbe906f67c685f1f6384928e7a8e449f" alt="Project User Role Assignment" width="1730" height="719" data-path="images/guides/admin-guide/user-role-and-team-management/project-user-role-assignment.png" />

<Info>
  **Important:** You must first select the user using the checkbox in the **Assign** column before you can choose their role.
</Info>

### Assigning Project Roles to Teams

<Steps>
  <Step title="Navigate to Project Settings">
    Go to **Project Settings** > **Teams** tab.
  </Step>

  <Step title="Select Team">
    Locate the team in the table and check the checkbox in the **Assign** column.
  </Step>

  <Step title="Choose Role">
    Click the **Role** dropdown that appears and select from the available roles:

    * Default roles: [Project Viewer](/guides/admin-guide/user-role-and-team-management/default-roles#project-viewer), [Project Planner](/guides/admin-guide/user-role-and-team-management/default-roles#project-planner), [Project Deployer](/guides/admin-guide/user-role-and-team-management/default-roles#project-deployer), [Project Admin](/guides/admin-guide/user-role-and-team-management/default-roles#project-admin)
    * Custom roles: Any custom roles created for your organization
  </Step>

  <Step title="Save Changes">
    Click **SAVE** to apply the changes.
  </Step>
</Steps>

<img src="https://mintcdn.com/envzero-b61043c8/ngeLWWxxE3C57X-b/images/guides/admin-guide/user-role-and-team-management/project-team-role-assignment.png?fit=max&auto=format&n=ngeLWWxxE3C57X-b&q=85&s=ec02ca89493ea887caca7fc9a38a94e9" alt="Project Team Role Assignment" width="1718" height="758" data-path="images/guides/admin-guide/user-role-and-team-management/project-team-role-assignment.png" />

<Info>
  **Important:** You must first select the team using the checkbox in the **Assign** column before you can choose their role.
</Info>

## Assigning Environment Roles

Environment roles can be assigned to both users and teams and apply only to a specific environment.

<Note>
  **Team Role Assignment Limitation**

  Default roles cannot be assigned to teams at the environment level. Teams can only be assigned custom roles at the environment level.
</Note>

### Assigning Environment Roles to Users

<Steps>
  <Step title="Navigate to Environment">
    Go to the **Environment** page and click the **ACCESS** tab.
  </Step>

  <Step title="Select User">
    In the **Manage Users** card, locate the user in the table and check the checkbox in the **Assign** column.
  </Step>

  <Step title="Choose Role">
    Click the **Role** dropdown that appears and select from the available roles:

    * Default roles: [Environment Viewer](/guides/admin-guide/user-role-and-team-management/default-roles#environment-viewer), [Environment Planner](/guides/admin-guide/user-role-and-team-management/default-roles#environment-planner), [Environment Deployer](/guides/admin-guide/user-role-and-team-management/default-roles#environment-deployer), [Environment Admin](/guides/admin-guide/user-role-and-team-management/default-roles#environment-admin)
    * Custom roles: Any custom roles created for your organization
  </Step>

  <Step title="Save Changes">
    Click **SAVE** to apply the changes.
  </Step>
</Steps>

<img src="https://mintcdn.com/envzero-b61043c8/ngeLWWxxE3C57X-b/images/guides/admin-guide/user-role-and-team-management/environment-user-role-assignment.png?fit=max&auto=format&n=ngeLWWxxE3C57X-b&q=85&s=5b1e0419a9a1f5dc59cb25c69dfd042f" alt="Environment User Role Assignment" width="1741" height="903" data-path="images/guides/admin-guide/user-role-and-team-management/environment-user-role-assignment.png" />

<Info>
  **Important:** You must first select the user using the checkbox in the **Assign** column before you can choose their role.
</Info>

### Assigning Environment Roles to Teams

<Steps>
  <Step title="Navigate to Environment">
    Go to the **Environment** page and click the **ACCESS** tab.
  </Step>

  <Step title="Select Team">
    In the **Manage Teams** card, locate the team in the table and check the checkbox in the **Assign** column.
  </Step>

  <Step title="Choose Role">
    Click the **Role** dropdown that appears and select a custom role.
  </Step>

  <Step title="Save Changes">
    Click **SAVE** to apply the changes.
  </Step>
</Steps>

<img src="https://mintcdn.com/envzero-b61043c8/ngeLWWxxE3C57X-b/images/guides/admin-guide/user-role-and-team-management/environment-team-role-assignment.png?fit=max&auto=format&n=ngeLWWxxE3C57X-b&q=85&s=f22e61c29027979427f8732a1f5de458" alt="Environment Team Role Assignment" width="1733" height="1034" data-path="images/guides/admin-guide/user-role-and-team-management/environment-team-role-assignment.png" />

<Note>
  **Default Role Limitation**

  Default roles ([Environment Viewer](/guides/admin-guide/user-role-and-team-management/default-roles#environment-viewer), [Environment Planner](/guides/admin-guide/user-role-and-team-management/default-roles#environment-planner), [Environment Deployer](/guides/admin-guide/user-role-and-team-management/default-roles#environment-deployer), [Environment Admin](/guides/admin-guide/user-role-and-team-management/default-roles#environment-admin)) cannot be assigned to teams at the environment level. Only custom roles are available for team assignments.
</Note>

<Info>
  **Important:** You must first select the team using the checkbox in the **Assign** column before you can choose their role.
</Info>

## Next Steps

<CardGroup cols={2}>
  <Card title="Manage Users" icon="user" href="/guides/admin-guide/user-role-and-team-management/user-management">
    Learn how to invite and manage users in your organization
  </Card>

  <Card title="Manage Teams" icon="users" href="/guides/admin-guide/user-role-and-team-management/teams">
    Learn how to create and manage teams to simplify permission management
  </Card>

  <Card title="Default Roles" icon="shield-check" href="/guides/admin-guide/user-role-and-team-management/default-roles">
    Review the built-in default roles and their permissions
  </Card>

  <Card title="Custom Roles" icon="settings" href="/guides/admin-guide/user-role-and-team-management/custom-roles">
    Create custom roles before assigning them
  </Card>
</CardGroup>

Built with [Mintlify](https://mintlify.com).
