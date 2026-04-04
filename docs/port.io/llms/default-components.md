# Source: https://docs.port.io/getting-started/default-components.md

# Default components

In addition to the components created in the previous steps, Port will create a few default components for you (even if you did not select any tools).

## Blueprints[â](#blueprints "Direct link to Blueprints")

Several blueprints used to represent common concepts in your organization will be created automatically.

You can view and edit blueprints in the [data model page](https://app.getport.io/settings/data-model) of your portal.

### ![](/img/icons/service.svg) Service[â](#-service "Direct link to -service")

`_service` - a flexible [blueprint]() representing a piece of software that is owned by a team/group in your organization.

This blueprint serves as a single component with rich context about all the resources related to the software, such as:

* **The code itself** - a repository or a specific folder in a monorepo.
* **Incident management** components, such as a PagerDuty service.
* **Code scanning** components, such as Snyk Targets or Sonar Cloud projects.
* **Project management** components, such as Jira projects and issues.
* **Runtime** components, such as workloads.

Services are the core component of R\&D operations within a developer portal, providing each team with a unified view of its services and their status across different domains, such as **security**, **stability**, **access management**, and more.

### ![](/img/icons/environment.svg) Environment[â](#-environment "Direct link to -environment")

`_environment` - represents a deployment environment in your organization.

In addition to this [blueprint](), 3 default [entities]() will be created: `Dev`, `Test` and `Prod`.<br /><!-- -->You can modify the default environments and/or create additional ones.

### ![](/img/icons/workload.svg) Workload[â](#-workload "Direct link to -workload")

`_workload` - represents a `service` running in a specific `environment`, with context of the relevant related components.

For example, a `frontend` service in your organization can have `frontend-prod` and `frontend-test` workloads, each with its own Kubernetes namespace, Sentry project, and owning team.

### ![](/img/guides/icons/User.svg)![](/img/guides/icons/dark/User.svg) User[â](#-user "Direct link to -user")

`_user` - represents a user in your organization.

This blueprint can be related to other "user" blueprints coming from your data sources, such as `github_user`, allowing you to manage a user across multiple tools from a single component.

### ![](/img/guides/icons/Team.svg)![](/img/guides/icons/dark/Team.svg) Team[â](#-team "Direct link to -team")

`_team` - represents a team in your organization.

This blueprint can be related to other "team" blueprints coming from your data sources, such as `github_team`, allowing you to manage a team across multiple tools from a single component.

Users in Port can be assigned to teams, allowing you to implement ownership of components in your portal.
