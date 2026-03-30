# Source: https://northflank.com/docs/v1/application/secure/security-on-northflank.md

# Security on Northflank

Northflank has many security features to ensure that your services can run and communicate securely, that your data remains safe, and allow you to grant granular permissions to access and modify your projects, services, and teams via the Northflank API.

These features are only effective combined with best practices. Below are common areas of concern for security, and the relevant Northflank features you can use to reduce risk.

## Account security

You can enable single sign-on to authenticate to Northflank using another service. It is recommended that you add multi-factor authentication to your Northflank account. Teams can enforce members to use multi-factor authentication, and organisations can use directory sync to manage members and their permissions.

- [Sign-on security: Log-in using single sign-on authentication, and add multi-factor authentication to your account.](/v1/application/secure/single-sign-on-multi-factor-authentication)
- [Manage team security: Enforce multi-factor authentication and configure RBAC and API access for your team members.](/v1/application/collaborate/create-a-team#manage-team-security)
- [Manage your organisation on Northflank: Manage users, security, billing, and multiple teams with a Northflank organisation.](/v1/application/collaborate/manage-an-organisation)

## Access control

When working in teams or organisations, it is important to only grant the permissions and access strictly necessary for the job, whether that's a team member or external application. Create roles with granular permissions for team members and API tokens.

- [Configure role-based access control: Grant granular permissions and manage users with roles for teams and organisations.](/v1/application/secure/use-role-based-access-control)
- [Grant API access: Create API roles to grant access to the Northflank API, with granular permissions.](/v1/application/secure/grant-api-access)
- [Generate API tokens: Generate an API token to access your team and project.](/v1/application/secure/grant-api-access#generate-an-api-token)

## Secret management

Secrets should remain encrypted and restricted. Northflank can securely store secrets in services, secret groups, and argument overrides for templates. Secret values should never be committed to a repository or saved in a template body.

- [Inject secrets: Set build arguments and inject runtime variables into running deployments.](/v1/application/secure/inject-secrets)
- [Manage groups of secrets: Create and manage groups of secrets that can be inherited throughout an entire project or by specific services and jobs.](/v1/application/secure/manage-secret-groups)
- [Upload a secret file: Add secret files that will be mounted in your container.](/v1/application/secure/upload-secret-files)
- [Link connection details to group: Use your database in your application by linking it to a secret group.](/v1/application/databases-and-persistence/connect-database-secrets-to-workloads)

## Network security

Restrict access by basic authentication or IP policy, or securely forward services without exposing them to the internet.

- [Configure basic authentication: Require users to enter a username and password to access your site.](/v1/application/network/add-security-policies-for-ports#require-credentials)
- [Set IP policies: Allow or deny access to services based on IP addresses.](/v1/application/network/add-security-policies-for-ports#set-ip-policies)
- [Forward deployments and databases: Forward deployments and databases to your local machine for development.](/v1/api/forwarding)
