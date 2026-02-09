# Source: https://www.promptfoo.dev/docs/enterprise/service-accounts/

# Service Accounts

Service accounts allow you to create API keys for programmatic access to Promptfoo Enterprise. These are useful for CI/CD pipelines and automated testing.

> **Note**
>
> Only global system admins can create and assign service accounts.

To create a service account:

1. Navigate to your Organization Settings page
2. Click on the "Users" tab and then select "Create Service Account"

![Create Service Account screen](/img/enterprise-docs/create-service-account.png)

3. Enter a name for your service account and save the API key in a secure location.

![Service Account API key](/img/enterprise-docs/service-account-api-key.png)

> **Warning**
>
> Make sure to copy your API key when it's first created. For security reasons, you won't be able to view it again after closing the dialog.

4. Determine if you want to assign the API key with global admin privileges. This will provision the API key with access to everything that can be done in the organization settings page, such as managing teams, roles, users, and webhooks.
5. Assign the API key to a team by navigating to the "Teams" tab and selecting the team you want to assign the API key to in the "Service Accounts" section. Service account API keys will not have programmatic access to Promptfoo Enterprise unless assigned to a team and role.

![Assign Service Account to team](/img/enterprise-docs/assign-service-account.png)

6. Select the predefined role for the service account for that team.

## See Also

- [Managing Roles and Teams](/docs/enterprise/teams/)
- [Authentication](/docs/enterprise/authentication/)