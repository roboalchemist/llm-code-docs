# Source: https://docs.port.io/getting-started/set-up-service-catalog.md

# Set up your service catalog

Now that your tools are connected to your portal, you can start creating your service catalog and add some users and teams to your organization.

This page will explain some basic concepts and describe the process of onboarding assets to your portal.

## Service catalog[â](#service-catalog "Direct link to Service catalog")

Every Port account comes with a set of default [blueprints]().<br /><!-- -->Three of these blueprints are designed to help you create a rich and dynamic service catalog:

1. [`_service`](/getting-started/default-components.md#-service)
2. [`_workload`](/getting-started/default-components.md#-workload)
3. [`_environment`](/getting-started/default-components.md#-environment)

To manually onboard `services`, `workloads` and `environments`, go to the relevant page in the [Service catalog](https://app.getport.io/services) page, and click on the `+` button in the top right corner (for example, `+ Service` in the `Services` page).

This will create entities, with rich context from the tools you've integrated.

*For example:*<br /><!-- -->Say you've integrated `GitHub`, `Jira`, and `Pagerduty`.<br /><!-- -->When onboarding a service via the `+ Service` button, you will be able to select the relevant `GitHub repository`, `Jira project`, and `Pagerduty service` related to that service.

This will create a single `service` entity, with relations to the relevant entities you selected, serving as a single component to track & manage the service.

## Users & teams[â](#users--teams "Direct link to Users & teams")

Two other default blueprints are designed to help you manage users, teams, and ownership in your portal:

1. [`_user`](/getting-started/default-components.md#-user)
2. [`_team`](/getting-started/default-components.md#-team)

To manually onboard users and teams, go to the relvant page in the [Organization catalog](https://app.getport.io/users), and click on the `+` button in the top right corner (for example, `+ User` in the `Users` page).

This will create entities, with rich context from the tools you've integrated.

#### Register your user[â](#register-your-user "Direct link to Register your user")

First, in the [users](https://app.getport.io/users) page, choose `Register your user`.<br /><!-- -->This will create a `user` entity with context of your user accounts in other tools you've integrated.

Now that you've registered your user, some components in your portal will be populated with data.

For example, the table named `Track your open pull requests` in the [Plan my day](https://app.getport.io/plan_my_day) page is configured to display `pull request` entities that were opened by the logged in user (in this case, you).<br /><!-- -->This table should now be populated with PRs from your Git provider.

#### Register teams[â](#register-teams "Direct link to Register teams")

In the [teams](https://app.getport.io/teams) page, choose `Register a new team` and select your user as a member.<br /><!-- -->This will create a `team` entity and add your user to it.<br /><!-- -->Now that your user is a member of a team, widgets in the [My team](https://app.getport.io/my_team) page will be populated with data.

#### Register more users[â](#register-more-users "Direct link to Register more users")

To see what components in your portal look like with more than one user, register additional users to add them to your Port organization.

If you want to create users without inviting them to the portal just yet, make sure the `Invite to Port` toggle is disabled when creating the user.

User & team management

The `user` and `team` blueprints are powerful components that can be leveraged for many use cases, such as **ownership definition**, **RBAC definition**, **dynamic visualization**, and more.

Read more about them in the [User & team management](/sso-rbac/users-and-teams/manage-users-teams.md) page.

## How the service catalog works[â](#how-the-service-catalog-works "Direct link to How the service catalog works")

As you may have seen, installing an integration will create one or more [blueprints](), some of which may have a [relation]() to other blueprints.

For example, when installing the `PagerDuty` integration, the `pagerdutyIncident` blueprint has a relation to the `pagerdutyService` blueprint.

Additionally, some of the blueprints will have a [relation]() to one of the default blueprints (e.g. `service`).

In the `PagerDuty` example, the `pagerdutyIncident` blueprint has a relation to the `service` blueprint.

This results in a rich `service` component, as these relations give it context from other components in your data model.<br /><!-- -->You can then use this service component to achieve many use cases, such as:

* Calculate "Mean time to recovery" for a `service` by adding an aggregation property to it, that will sum the `timeToRecovery` property of all `pagerdutyIncident` entities related to it.

* Calculate total monthly incident count for a `service` by adding an aggregation property to it, that will sum the number of related `pagerdutyIncident` entities.

* Create visualizations to track incidents, e.g. a chart that shows the number of incidents per service, a table that shows all incidents per service/team, and more.

### Relation mapping[â](#relation-mapping "Direct link to Relation mapping")

To connect integration entities and default component entities, (like the `pagerdutyIncident`->`service` relation), we use a rule to find the relevant `service` entity for each `pagerdutyIncident` entity.

Read more about relation mapping [here](/build-your-software-catalog/customize-integrations/configure-mapping.md#mapping-relations-using-search-queries).

For example, here is part of the default mapping for the `PagerDuty` integration.<br /><!-- -->Note the rule that is used under the `service` relation, which will find the relevant `service` entity for each `pagerdutyIncident` entity:

```
kind: incidents
selector:
    ...
port:
  entity:
    mappings:
      ...
      relations:
        pagerdutyService: .service.id
        service:
          combinator: '"and"'
          rules:
            - property: '"pagerdutyServiceId"'
              operator: '"="'
              value: .service.id
```

You can use this method to connect additional components to default components in your data model.

## Next step - automatic discovery[â](#next-step---automatic-discovery "Direct link to Next step - automatic discovery")

Proceed to the [next step](/getting-started/set-up-automatic-discovery.md) to learn how to manage your catalog automatically, creating and updating components based on changes in data from your tools.
