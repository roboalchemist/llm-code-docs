# Source: https://northflank.com/docs/v1/application/collaborate/create-a-team.md

# Create a team

Your team contains your account settings, integrations, and projects.

![A team dashboard in the Northflank application](https://assets.northflank.com/documentation/v1/application/collaborate/create-a-team/team-dashboard.png)

To create a new team select team from the create new menu, or create team from your account dashboard. Enter a team name, select a billing plan, and enter a contact email. You can also invite people to the new team via email.

> [!note] Organisations
> You can also create and manage teams with  [an organisation](/docs/collaborate/manage-an-organisation). This allows you to manage users and access across teams, and integrate your user directory and other enterprise features.

Your team name must be unique and will be used to refer to resources in your team projects, and used to generate Northflank DNS entries for your deployment's [public ports](https://northflank.com/docs/v1/application/network/configure-ports#public-ports). Your team email address will receive important notifications and billing information.

After verifying your team email you can link a Git account, configure integrations and settings, and create a new project.

Any resources consumed by your team will be billed to the team, and only the payment method linked to the team account will be charged.

> [!note] 
> [Click here](https://app.northflank.com/s/account/teams/new) to create a new team.

![Creating a team in the Northflank application](https://assets.northflank.com/documentation/v1/application/collaborate/create-a-team/create-team.png)

## Invite members to your team

You can invite members to your team from the members page under your team's account settings.

You can invite one or more users to join your team by their email address. If they do not already have a Northflank account they will be prompted to create one, but they do not need to add payment information to use the team account.

You can set roles for invited users, and modify them on the members page afterwards. If a user has not yet accepted their invitation to join the team they will appear in the invited members section.

## Manage team security

### Role-based access control

You can limit the access team members have to resources and actions by configuring and assigning [RBAC roles](https://northflank.com/docs/v1/application/secure/use-role-based-access-control). Roles can be created on the RBAC roles page, and assigned when editing the role, or from the team members page.

### API access

To allow team members to create API tokens to access team resources, you must first create an [API token role](https://northflank.com/docs/v1/application/secure/grant-api-access). Team members can then create API tokens for their accounts using these roles, and you can specify which team members have access to an API role.

### Multifactor Authentication

You can enable require MFA to enforce multifactor authentication for your team members. Team members will be prompted to [set up an authenticator application for their Northflank account](https://northflank.com/docs/v1/application/secure/single-sign-on-multi-factor-authentication#multi-factor-authentication) before they can access Northflank, and they will need to enter their one-time passcode on every log in attempt.

You can also set a maximum login session duration in hours, which will automatically log team members out and require them to re-authenticate after the time period.

## Transfer ownership of a team

The team owner has full permissions in a team and cannot be removed by other members, even if they have [permissions to manage team members](https://northflank.com/docs/v1/application/secure/use-role-based-access-control). The owner also cannot leave the team without transferring ownership to another member.

To change ownership of a team the current owner must navigate to the members page and transfer  ownership to another member.

## Next steps

- [Link your Git account: Integrate your Git accounts with Northflank to start building and deploying your code.](/v1/application/getting-started/link-your-git-account)
- [Create a project: Create a project to contain your services, persistent data, secrets, and more.](/v1/application/getting-started/create-a-project)
- [Add a card: Add a credit or debit card to your user or team account, and select the card to charge.](/v1/application/billing/add-a-card)
- [Configure role-based access control: Grant granular permissions and manage users with roles for teams and organisations.](/v1/application/secure/use-role-based-access-control)
- [Grant API access: Create API roles to grant access to the Northflank API, with granular permissions.](/v1/application/secure/grant-api-access)
- [Manage your organisation on Northflank: Manage users, security, billing, and multiple teams with a Northflank organisation.](/v1/application/collaborate/manage-an-organisation)
