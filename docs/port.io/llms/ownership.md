# Source: https://docs.port.io/sso-rbac/ownership.md

# Manage ownership in Port

Ownership in Port defines who is responsible for specific entities in your internal developer portal â such as services, repositories, or incidents.

Managing ownership correctly ensures clear accountability, smoother collaboration, and accurate reporting.<br /><!-- -->Ownership in Port is represented through relationships between **users**, **teams**, and **catalog entities**.

This page outlines how to manage ownership in Port, from syncing users and teams to assigning them to catalog entities, and visualizing the data.

## How does it work?[â](#how-does-it-work "Direct link to How does it work?")

When creating a Port account, some default blueprints are created for you. Two of them are the `User` and `Team` blueprints, which are used to represent your users and teams.

Using these blueprints, we can define ownership of resources in the software catalog to specific users or teams.

Defining ownership in Port is composed of several steps:

1. [Sync Users](#sync-users) - the first step in managing ownership is syncing your users from 3rd party tools into Port, and connecting to the relevant Port user. This allows you to have a single component in your portal that represents your user across your entire ecosystem.

2. [Sync Teams](#sync-teams) - just like users, teams from 3rd party tools can be synced into Port, and connected to the relevant Port teams.

3. [Assign Users to Teams](#assign-users-to-teams) - once Port users and teams are synced and connected to each other, users can get visibility into the resources owned by their team/s.

4. [Assign Teams to Catalog Entities](#assign-teams-to-catalog-entities) - define ownership of resources in your catalog to Port teams.<br /><!-- -->For example, a GitHub repository can be owned by the `frontend` team.

5. [Assign Users to Catalog Entities](#assign-users-to-catalog-entities) - define ownership of resources in your catalog to Port users.<br /><!-- -->For example, a PagerDuty incident can be owned by the current `on-call` user.

## Sync users[â](#sync-users "Direct link to Sync users")

Users can be synced into Port either manually or automatically, depending on your integrations.

**Note** that when using an SSO provider, users and teams are synced automatically.

### Automatically[â](#automatically "Direct link to Automatically")

* **Built-in integrations**: Update the integration mapping to connect the Port user to the integration user:

  * GitHub
  * GitLab
  * Azure DevOps
  * Jira

  ```
  - kind: user
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: .login
          title: .login
          blueprint: '"_user"'
          relations:
            git_hub_user: .login
  ```

  ```
  - kind: group-with-members
    selector:
      query: 'true'
      includeBotMembers: 'true'
      includeInheritedMembers: 'true'
    port:
      itemsToParse: .__members
      entity:
        mappings:
          identifier: .item.username
          title: .item.name
          blueprint: '"_user"'
          relations:
            gitlab_user: .item.username
  ```

  ```
  - kind: user
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: '.id'
          title: '.user.displayName'
          blueprint: '"_user"'
          relations:
            azure_devops_user: '.id'
  ```

  ```
  - kind: user
    selector:
      query: 'true'
    port:
      entity:
        mappings:
          identifier: .accountId
          title: .displayName
          blueprint: '"_user"'
          relations:
            jira_user: .accountId
  ```

* **Custom integrations**: We can create a simple automation to link new Port users to the matching integration user upon creation:

  * [Slack](https://docs.port.io/guides/all/map-slack-users-to-port-accounts/#sync-slack-users-when-a-new-port-user-is-added)
  * [ServiceNow](https://docs.port.io/guides/all/map-servicenow-users-to-port-accounts/#sync-servicenow-users-when-a-new-port-user-is-added)
  * [HiBob](https://docs.port.io/guides/all/map-hibob-users-to-port-accounts/#sync-hibob-users-when-a-new-port-user-is-added)

### Manually[â](#manually "Direct link to Manually")

* [**Self-service Action (SSA)**]() â [Register your user](https://app.getport.io/self-serve?action=_onboard_your_user) An out-of-the-box self service action used to register the logged-in user in Port, connecting it to the relevant 3rd party user/s.

* **Register a new user**<br /><!-- -->This can be done from the [Users catalog page](https://app.getport.io/_users):<br /><!-- -->Click on the `+ User` button, then click on `Register existing user`.

  This is useful for inviting a new user and defining their relations to 3rd party users in a single step.

* **Edit an existing user entity**<br /><!-- -->This can also be done from the [Users catalog page](https://app.getport.io/_users):<br /><!-- -->Click on the `...` button, then click on `Edit`.

  Ideal when updating a user with new data â for example, connecting it to a Slack user.

**Custom integrations**:<br /><!-- -->3rd party tools for which Port does not have a built-in integration can be synced manually using the following guides:

* [Slack](https://docs.port.io/guides/all/map-slack-users-to-port-accounts/)
* [ServiceNow](https://docs.port.io/guides/all/map-servicenow-users-to-port-accounts/)
* [HiBob](https://docs.port.io/guides/all/map-hibob-users-to-port-accounts/)

## Sync teams[â](#sync-teams "Direct link to Sync teams")

Teams can also be synced into Port either manually or automatically, depending on your integrations and conventions.

**Note** that when using an SSO provider, teams are synced automatically.

### Automatically[â](#automatically-1 "Direct link to Automatically")

* **Built-in integrations**:

  Using the integration mapping, we can define how to create/update teams in Port.

  For example, the following mapping can be used to create/update teams using GitHub:

  ```
  - kind: team
    selector:
      query: 'true'
    port:
      entity:
      mappings:
        identifier: .id | tostring
        title: .name
        blueprint: '"_team"'
        relations:
          git_hub_team: .id | tostring
  ```

  In this example, if the team already exists in Port, it will be connected to the GitHub team with the same identifier.<br /><!-- -->If it does not exist, it will be created and connected to the GitHub team with the same identifier.

### Manually[â](#manually-1 "Direct link to Manually")

* **Register a new team**<br /><!-- -->This can be done from the [Teams catalog page](https://app.getport.io/_teams):<br /><!-- -->Click on the `+ Team` button.

  This is useful for creating a new team and defining its relations to 3rd party teams in a single step.

* **Edit an existing team entity**<br /><!-- -->This can also be done from the [Teams catalog page](https://app.getport.io/_teams):<br /><!-- -->Click on the `...` button, then click on `Edit`.

  Ideal when updating a team with new data â for example, connecting it to a Sentry team.

## Assign users to teams[â](#assign-users-to-teams "Direct link to Assign users to teams")

In many cases, ownership is assigned to a team and not a specific user. By default, Port allows you to assign one or more owning teams to each entity in your catalog.

As a user, it's important to see all of the resources owned by you or your team/s. Therefore, the next step is to ensure that all Port users are assigned to the relevant team/s.

### Automatically[â](#automatically-2 "Direct link to Automatically")

* When using SSO, users and teams are created and connected automatically.

* When using Entra ID, you can use this [integration tool](https://github.com/port-experimental/entra-id-provisioner) to sync users and teams into Port.

* When using Gitlab or ADO integrations, you can connect Port team to Port user when fetching the integration's teams.

  For example, the following mapping connects a team in Port to a user in Port based on the GitLab association (assuming the GitLab group is already mapped to the Port team):

  ```
  - kind: group-with-members
    selector:
      query: 'true'
      includeBotMembers: 'true'
      includeInheritedMembers: 'true'
    port:
      itemsToParse: .__members
      entity:
        mappings:
          identifier: .item.email
          title: .item.name
          team: .full_path
          blueprint: '"_user"'
  ```

### Manually[â](#manually-2 "Direct link to Manually")

* [**Self-service action (SSA)**]() â [Add team members](https://app.getport.io/self-serve?action=_onboard_existing_team)<br /><!-- -->An out-of-the-box self service action used to add users to an existing team.

* **Edit a user entity**<br /><!-- -->This can be done from the [Users catalog page](https://app.getport.io/_users):<br /><!-- -->Click on the `...` button, then click on `Edit`.

* When creating/inviting a new user from the UI, you can assign them to teams as part of the creation process.

## Assign teams to catalog entities[â](#assign-teams-to-catalog-entities "Direct link to Assign teams to catalog entities")

### Automatically[â](#automatically-3 "Direct link to Automatically")

* If using GitHub, you can use the [team-mapper](https://github.com/port-experimental/repo-team-mapper) script to map repositories to teams based on commit history.

* If an entity has an property or relation that contains the integration team identifier (e.g., GitHub repository â `github-teams`), update the mapping so that the `github-teams` value will automatically be set in `owning teams`.

  ```
  - kind: repository
    selector:
      query: 'true'
      teams: true
    port:
      entity:
        mappings:
          identifier: .full_name
          title: .name
          blueprint: '"githubRepository"'
          properties:
            readme: file://README.md
            url: .html_url
            defaultBranch: .default_branch
            $team: '[.teams[].id | tostring]'
          relations:
            githubTeams: '[.teams[].id | tostring]'
  ```

  Note that this assumes Port team identifiers match GitHub team identifiers.

### Manually[â](#manually-3 "Direct link to Manually")

* [**Self-service action (SSA)**]() â [Own services](https://app.getport.io/self-serve?action=set_ownership)<br /><!-- -->An out-of-the-box self service action used to assign ownership of one or more services to a specific team.

* **Edit an entity**<br /><!-- -->This can be done from the entity's relevant catalog page:<br /><!-- -->Click on the `...` button, then click on `Edit`, and change the `Owning teams` field.

* When creating a new entity, assign its owning team(s) as part of the creation process.

## Assign users to catalog entities[â](#assign-users-to-catalog-entities "Direct link to Assign users to catalog entities")

In some cases, ownership needs to be assigned to a specific user and not a team. For example, a PagerDuty incident may be owned by the current on-call user, or a GitHub Pull Request may be owned by the creator.

### Automatically[â](#automatically-4 "Direct link to Automatically")

In many Port integrations, blueprints can have out-of-the-box relations to the **3rd party user blueprint**, with a default mapping configuration that automatically sets the value of this relation.

Additionally, some blueprints have out-of-the-box relations to the **Port user blueprint**, with a default mapping configuration that automatically sets the value of this relation as well.

Here are some common examples:

* The `GitHub Pull Request` blueprint has a default relation ("git\_hub\_creator") to the **GitHub user** that created the PR.<br /><!-- -->Additionally, it has a default relation ("creator") to the **Port user** associated with the GitHub user that created the PR.

* The `Jira Issue` blueprint has a default relation ("reporter") to the **Port user** that reported the issue.

* The `PagerDuty Incident` blueprint has a default relation ("assignee") to the **Port user** that is assigned to the incident.

### Manually[â](#manually-4 "Direct link to Manually")

* **Edit an entity**
  <br />
  <!-- -->
  If a blueprint has a relation to the Port user blueprint, you can edit the entity from its catalog page and change the value of this relation:
  <br />
  <!-- -->
  Click on the `...` button, then click on `Edit`, and change the relation value.

## Visualize user & team data[â](#visualize-user--team-data "Direct link to Visualize user & team data")

Now that we have set up ownership in our catalog, let's see how we can visualize it in useful ways.

### Default pages & filters[â](#default-pages--filters "Direct link to Default pages & filters")

* By default, the following pages are available in your catalog:

  * **User entity page**: View all Port users and their related 3rd-party users and the Port teams they belong to.

  * **Team entity page**: View all Port teams and their related 3rd-party teams.

* In any table or chart, you can use the `My Teams` or `My` filters to show only entities that belong to your teams or are owned by you.

### User management dashboard[â](#user-management-dashboard "Direct link to User management dashboard")

Now let's create a dedicated dashboard to manage users and ownership of entities in your catalog.<br /><!-- -->This dashboard will allow you to:

* View which users are assigned to which team/s.
* View which users from 3rd-party tools are connected to which Port user/s.
* View which teams from 3rd-party tools are connected to which Port team/s.
* View which services are owned by which team/s.
* Execute several [**self-service actions**]() to onboard users to teams, register new users, and assign ownership of services to teams.

### Create a dashboard[â](#create-a-dashboard "Direct link to Create a dashboard")

1. Navigate to the [Catalog](https://app.getport.io/organization/catalog) page of your portal.

2. Click on the **`+ New`** button in the left sidebar.

3. Select **New dashboard**.

4. Name the dashboard **Ownership Management**.

5. Input `Manage and onboard your users and teams` under **Description**.

6. Select the `Users` icon.

7. Click `Create`.

We now have a blank dashboard where we can start adding widgets to visualize ownership insights.

#### Add widgets[â](#add-widgets "Direct link to Add widgets")

In the new dashboard, create the following widgets:

**Users assignment (click to expand)**

1. Click `+ Widget` and select **Table**.

2. Title: `Users assignment`.

3. Choose **User** as the **Blueprint**.

4. Click `Save`.

5. Click on the **`...`** button in the top right corner of the table and select **Customize table**.

6. Define the visible columns to include the user title, team, and third parties associated user.

7. Click on the **save icon** in the top right corner of the widget to save the customized table.

![](/img/software-catalog/pages/usersAssignmentWidget.png)

***

<br />

**Users with no teams (click to expand)**

1. Click **`+ Widget`** and select **Pie chart**.

2. Title: `Users with no teams`.

3. Choose the **User** blueprint.

4. Under `Breakdown by property`, select the **Ownership - Has Team** property

5. Click **Save**.

![](/img/software-catalog/pages/usersWithNoTeamsWidget.png)

***

<br />

**Teams assignment (click to expand)**

1. Click **`+ Widget`** and select **Table**.

2. Title: `Teams assignment`.

3. Choose the **Team** blueprint.

4. Click **Save**.

5. Click on the **`...`** button in the top right corner of the table and select **Customize table**.

6. Define the visible columns to include the team's title, and third parties associated teams.

7. Click on the **save icon** in the top right corner of the widget to save the customized table.

![](/img/software-catalog/pages/teamsAssignmentWidget.png)

***

<br />

**Services ownership (click to expand)**

1. Click **`+ Widget`** and select **Table**.

2. Title the widget **Services ownership**.

3. Choose the **Service** blueprint

4. Click **Save** to add the widget to the dashboard.

5. Click on the **`...`** button in the top right corner of the table and select **Customize table**.

6. Define the visible columns to include the service title and the owning teams.

7. Click on the **save icon** in the top right corner of the widget to save the customized table.

![](/img/software-catalog/pages/servicesOwnershipWidget.png)

***

<br />

**Ownership management actions (click to expand)**

1. Click **`+ Widget`** and select **Action Card**.

2. Under `Actions`, select all the Ownership management actions we created:

   * **Add team members**
   * **Register your user**
   * **Own services**

3. Title: `Ownership management`.

4. Click **Save**.

![](/img/software-catalog/pages/ownershipSSAWidget.png)
