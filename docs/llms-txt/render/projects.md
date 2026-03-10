# Source: https://render.com/docs/projects.md

# Projects and Environments — Organize your services and set environment-level controls.

Render *projects* enable you to organize your services by application and environment:

[image: Viewing a project environment in the Render Dashboard]

For example, one of your applications might include a static site, a GraphQL backend, and a database. By adding all of these services to the same project, you can find and manage them more quickly.

Each project has one or more *environments* (such as *Production* in the screenshot above). If you run staging and production versions of your app, you can add each version's services to a different environment.

You can also set *[environment-specific controls](#environment-specific-controls):*

- [Define environment variables and secret files](#scoped-configuration) that only services in a single environment can access.
  - Prevent your staging services from inadvertently using a production-specific credential (or vice versa).
- Designate an environment as [protected](#protected-environments) so that only your workspace's admins can make potentially destructive changes to its resources.
- [Block private network traffic](#blocking-cross-environment-traffic) from entering or exiting a specific environment.
  - Prevent your staging services from inadvertently accessing a production database (or vice versa).

## Setup

> *Hobby workspaces can have up to one project with up to two environments.*
>
> To create additional projects or environments, [upgrade your workspace](team-members#change-a-workspaces-plan).

### Create a project

1. In the [Render Dashboard](https://dashboard.render.com), click *New > Project*:

   [image: Navigating to project creation]

   The following form appears:

   [image: Create a project dialog]

2. Provide a name for your new project, along with a name for its first environment.

   - Both of these names are for your own informational purposes. You can change them later.

3. Click *Create a project*.

That's it! You're redirected to the page for your new project.

### Add services to an environment

If an environment in your project is empty, it displays buttons for creating a new service or moving some of your workspace's existing services into the project:

[image: An empty project page in the Render Dashboard]

You can specify a new service's associated project and environment during the creation flow.

You can bulk-move services to an environment by selecting them in your workspace's service list and then clicking *Move*:

[video]

You can also move an individual service by opening its *•••* menu and clicking *Move*.

### Open a project

Your workspace's homepage in the [Render Dashboard](https://dashboard.render.com) lists all projects at the top:

[image: Workspace homepage with projects]

Click a project to open it. Services belonging to a project appear on that project's page, _not_ on your workspace's homepage.

### Modify a project

- To add an environment to a project, click *+ Add environment* at the top right of the project's page.
- To configure an existing environment, click the *•••* menu at the top right of that environment's section on the project's page.
- To rename or delete an entire project, click *Settings* in the left pane of the project's page.

> *Important:*
>
> - Deleting a project deletes _all_ of its associated environments and services.
> - Deleting an environment deletes all of its associated services.

## Blueprint support

[Blueprints](infrastructure-as-code) (Render's infrastructure-as-code model) support creating projects and environments, along with assigning your resources to them:

```yaml
projects:
  - name: my-project
    environments:
      - name: production
        # These resources will belong to the my-project/production environment.
        # Do not duplicate these definitions at the root level.
        services:
          - name: my-web-service
            type: web
            envVars:
              - key: MY_ENV_VAR
                value: my-value
        databases:
          - name: my-database
            type: postgres
            envVars:
              - key: DATABASE_URL
                fromDatabase:
                  name: my-database
                  property: connectionString
        envVarGroups:
          - name: my-env-group
            envVars:
              - key: MY_ENV_VAR
                value: my-value
        # Environment-specific settings
        networking:
          isolation: enabled
        permissions:
          protection: enabled
```

For details, see the [YAML reference](blueprint-spec#projects-and-environments).

## Environment-specific controls

### Scoped configuration

[Environment groups](configure-environment-variables#environment-groups) are a helpful way to share environment variables and/or secret files across multiple services in your workspace.

You can optionally scope an environment group to a single project environment. This helps you share configuration across multiple services in that environment, while also ensuring that services in _other_ environments _can't_ use that environment group.

Move an environment group into a project environment from the group's info page by clicking *Manage > Move group*:

[image: Moving environment group into an environment]

After you move your environment group, it appears on the corresponding project's overview page:

[image: Environment groups on project overview page]

### Protected environments

Workspace members with the [*Admin* role](team-members#member-roles) can designate any project environment as *protected*. This restricts other members from performing potentially destructive actions ([listed below](#restricted-actions)).

#### Steps to configure

1. Go to your project's page in the [Render Dashboard](https://dashboard.render.com) and scroll to the environment you want to configure.
2. Click the *•••* menu at the top right of the environment, then click *All settings*.
3. Scroll down to the *Permissions* section and click *Edit*:

   [image: Editing an environment's permissions in the Render Dashboard]

4. Select *Protected* and click *Save*.

Protected environments display a label and a lock icon on your project's page in the Render Dashboard:

[image: Indicators of a protected environment in the Render Dashboard]

#### Restricted actions

> *Important:* If your protected environment includes resources that are managed via [Blueprints](infrastructure-as-code), non-*Admin* workspace members _can_ still modify those resources by publishing an update to the corresponding `render.yaml` file.

Only *Admin* workspace members can perform the following actions in a protected environment:

*Resource management*

- Deleting any of the environment's resources (services, [environment groups](#scoped-configuration), etc.), or deleting the environment itself
- Creating new resources in the environment
- Moving resources into or out of the environment

*Operational controls*

- Modifying access control IPs for any Render Postgres or Key Value instance in the environment
- Suspending or resuming any service in the environment
- Toggling [maintenance mode](maintenance-mode) for any service in the environment
- Accessing the shell for any service in the environment

*Secret values*

- Viewing or modifying environment variables or secret files for any service or environment group in the environment
- Viewing passwords or connection URLs for any Render Postgres or Key Value instance in the environment

### Blocking cross-environment traffic

By default, all of your Render services in the same region can communicate over their shared private network.

You can configure an environment to _block_ private network traffic from crossing its boundary. If you do, services _within_ the environment can still communicate:

[diagram]

This helps you prevent your staging services from inadvertently accessing a production resource (or vice versa).

> *This setting only affects _private network_ traffic.*
>
> - Web services and static sites in the environment can still receive public internet traffic at their `onrender.com` subdomain, _including_ traffic originating from your services outside the environment.
> - Render Postgres and Key Value instances in the environment can still receive traffic at their external URL from [allowed IPs](postgresql-creating-connecting#restricting-external-access).
> - Workspace members can still access services in the environment over [SSH](ssh).
>   - In a [protected environment](#protected-environments), only *Admin* workspace members can access the shell for services in the environment.

#### Steps to configure

> Toggling this feature does not trigger any deploys or cause any interruptions for your running services.

1. Go to your project's page in the [Render Dashboard](https://dashboard.render.com) and scroll to the environment you want to configure.
2. Click the *•••* menu at the top right of the environment, then toggle *Block cross-environment connections*:

   [image: Blocking cross-environment traffic in the Render Dashboard]

> *Enabling this feature does not terminate any active network connections.*
>
> To ensure that all existing connections are terminated, you can restart your services in the environment.

You're all set! Your environment now blocks private network traffic from crossing its boundary.

### Environment-level IP rules

Enterprise orgs can set inbound IP rules for all services in a particular environment. These rules apply to inbound connections from the public internet.

For details, see [Inbound IP rules](inbound-ip-rules).

## FAQ

###### Does an environment named 'Production' or 'Staging' have special restrictions or capabilities?

*No.* Render does not apply special logic to any environment based on its name. The examples above use "Production" and "Staging" because they're common.

###### Will my service behave differently after I add it to a project?

*Possibly.* If you've configured any [environment-specific controls](#environment-specific-controls) for the service's corresponding environment, those controls apply to the service.

For example, if the service's environment [blocks cross-environment network traffic](#blocking-cross-environment-traffic), the service can no longer communicate over your private network with services outside the environment.

###### Can I use projects and environments with Blueprints (Render's infrastructure-as-code model)?

*Yes.* You can define projects and environments in your `render.yaml` file, then assign new and existing resources to them.

For details, see the [YAML reference](blueprint-spec#projects-and-environments).

###### Are preview environments tied to projects?

*No.* You manage your workspace's [preview environments](preview-environments) with [Blueprints](infrastructure-as-code), not projects. A preview environment can include services that belong to any number of different projects.

###### Can I use the same service name in multiple project environments?

*No.* All of a workspace's services must have unique names—even services that belong to different project environments.


---

##### Appendix: Glossary definitions

###### private network

Your Render services in the same *region* can reach each other without traversing the public internet, enabling faster and safer communication.

Related article: https://render.com/docs/private-network.md