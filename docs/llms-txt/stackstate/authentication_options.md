# Source: https://archivedocs.stackstate.com/5.1/configure/security/authentication/authentication_options.md

# Source: https://archivedocs.stackstate.com/self-hosted-setup/security/authentication/authentication_options.md

# Authentication options

Out of the box, StackState is configured with [file-based authentication](https://archivedocs.stackstate.com/self-hosted-setup/security/authentication/file) with a username and password [configured during installation](https://archivedocs.stackstate.com/install-stackstate/initial_run_guide#default-username-and-password). This authenticates users with a file on the server. However, this isn't a production-ready setup.

For better security StackState can be configured to use exactly one of the following authentication mechanisms (replacing the standard admin user):

* [File based](https://archivedocs.stackstate.com/self-hosted-setup/security/authentication/file)
* [LDAP](https://archivedocs.stackstate.com/self-hosted-setup/security/authentication/ldap)
* [Open ID Connect (OIDC)](https://archivedocs.stackstate.com/self-hosted-setup/security/authentication/oidc)
* [KeyCloak (a specialized version of OIDC)](https://archivedocs.stackstate.com/self-hosted-setup/security/authentication/keycloak)

{% hint style="info" %}
Authentication configuration is part of the Helm chart, any changes will automatically trigger a restart of the pods requiring that.
{% endhint %}

## User roles

When a user has been authenticated permissions for that user are usually assigned based of the roles the user has. The documentation for the specific authentication mechanisms also contain examples on how to map the roles or groups from the external systems to the 4 standard roles of StackState:

* **Guest** - able to see information but make no changes.
* **Kubernetes Troubleshooter** - able to see all information and see and change monitors and metric configuration.
* **Power User** - able to see and change all configuration and install StackPacks.
* **Administrator** - able to see and change content of StackState. For example, see all configuration, install StackPacks, grant and revoke user permissions and upload (new versions of) StackPacks.
* **Platform Administrator** - able to perform management of the StackState platform. For example, change data retention, clear the database, view logs and cache management.

When deciding on the roles to assign your users, it's strongly advised to have only a small group of Platform Administrators and Administrators. For example, only the engineers responsible for installing StackState and doing the initial configuration. Administrator users can manage access to StackState and decide which StackPacks can be used. You can delegate installation of StackPacks and other fine-tuning of the configuration to a larger number of users with the Power User role. Platform Administrator users can clear the database, change data retention settings, view logs and perform other platform management tasks.

It's also possible to add more roles, see the page [Roles (RBAC)](https://archivedocs.stackstate.com/self-hosted-setup/security/rbac/rbac_roles) and the other [RBAC documentation pages](https://archivedocs.stackstate.com/self-hosted-setup/security/rbac)
