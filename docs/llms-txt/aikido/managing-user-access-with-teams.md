# Source: https://help.aikido.dev/getting-started/manage-teams-and-applications/managing-user-access-with-teams.md

# Managing User Access with Teams

## Introduction <a href="#introduction" id="introduction"></a>

Aikido lets you create teams, connect multiple repositories and clouds, and manage access using RBAC (Role-Based Access Control) for better security. This article focuses on Managing of User Access. If you are looking to use Teams to group your resources into Projects or Apps, please [**click here**](https://help.aikido.dev/getting-started/manage-teams-and-applications/manage-and-view-your-apps-and-projects-via-our-teams-feature).

## Use Cases <a href="#use-cases" id="use-cases"></a>

* **Selective Access Control:** Assign repository access exclusively to designated team members.
* **Filter Repositories Quickly:** In companies with multiple teams, each team may have access to the entire codebase, but their primary responsibilities are often limited to specific repositories or projects. By creating teams in Aikido, team members **can have a focused overview** of only the repositories relevant to their tasks.\
  ​

  ![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-4bb2f109bd2129819846da01466f592e79b2c0e0%2Fmanaging-user-access-with-teams_e47c7d0e-a0e8-40db-9c28-dd5ab925c8c5.png?alt=media)
* **Better overview when using a monorepo split.** You can assign team members to specific directories of your monorepo, improving their overview. More information on splitting monorepositories can be found [here](https://help.aikido.dev/en/articles/9026666-splitting-up-your-monorepo-per-directory).

## How To Create Teams <a href="#how-to-create-teams" id="how-to-create-teams"></a>

**Step 1:** Navigate to **Settings -> Teams**\
​

![Team dashboard showing user "mdschuym" with 4 active repositories and 1 member.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-0b18ccf8b33376a81bcb2be0b155c8ea75bf054a%2Fmanaging-user-access-with-teams_eb9c5cc9-fe18-4fda-8040-d68dc275f186.png?alt=media)

**Step 2:** Click **Create Team** and give your team a name

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-2df987cb28febd5270a9e0f37b72b13d15f2eaee%2Fmanaging-user-access-with-teams_2713e19f-5433-435b-b10b-9f1aa409950e.png?alt=media)

**Step 3:** **Add team members** to the newly created team.

![User management interface showing available users and team assignment options.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-360a0c5347426b99a212daa1a65be6b91a03be63%2Fmanaging-user-access-with-teams_59d4a227-bdc5-4880-a1de-4fcb3da51294.png?alt=media)

**Step 4:** Define the **team's responsibilities** by adding **resources via the responsibility tab.** You can add different resources such as clouds, repositories, containers, domains and zen apps.

> If you want to link specific domains to a team, you can set this up by linking your domains to a repo or container. It will automatically inherit access permissions.

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FuyEJzLnw6eQHoLdBUAiw%2FScreenshot%202025-12-15%20at%2016.21.52.png?alt=media\&token=ce29fb76-f6bc-4401-a7e3-e81bd279ef20)

**Step 5.** Go back to your feed and filter on a specific team. You should only see issues that are related to those repositories and clouds that were attached to the team.

## Syncing with GitHub, Bitbucket or Azure DevOps <a href="#syncing-with-github-bitbucket-or-azure-devops" id="syncing-with-github-bitbucket-or-azure-devops"></a>

If you have **existing teams** set up in GitHub, Bitbucket or Azure DevOps, Aikido will import them and maintain synchronization on a nightly basis. This ensures that any changes in team structures or access rights managed in GitHub/Bitbucket are accurately reflected in Aikido. Any new teams that are created in GitHub will appear in Aikido. The same applies to when you remove a team in GitHub: Aikido will pick this up and remove the team too. Any repos that are part of the team, will be synced too.

{% hint style="info" %}
It's important to note that in this scenario, GitHub/Bitbucket/Azure DevOps acts as the source of truth for access rights, and all management should be conducted within those platforms. This also means that **no extra users can be added to scm-linked teams** inside Aikid&#x6F;**.**
{% endhint %}

Aikido makes it clear which teams have been imported from your SCM.

![Team roles and users overview with DevOps group imported from GitHub.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-7f3ddad0a51238cf01f2b9d4ccf619c5ac7995bf%2Fmanaging-user-access-with-teams_0ab4ee09-6b7d-48ee-a435-b20c98ff18d6.png?alt=media)

## Syncing with Backstage.io <a href="#syncing-with-backstageio" id="syncing-with-backstageio"></a>

Aikido integrates seamlessly with repositories containing `catalog-info.yaml` files for [Backstage.io](https://backstage.io). This allows for the automatic importing of teams, taking into account the path of where the file is located.

{% hint style="info" %}
Please note: This feature needs to be enabled by Aikido manually. Please reach out to support to enable this.
{% endhint %}

#### How It Works <a href="#how-it-works" id="how-it-works"></a>

1. Aikido scans repositories for `catalog-info.yaml` files.
2. Aikido looks for the `spec->owner` field in the file and imports this as team.
3. Aikido records the exact path of each `catalog-info.yaml` file, ensuring the team is responsible for those specific paths (and repositories).

## Syncing with Port.io <a href="#syncing-with-backstageio" id="syncing-with-backstageio"></a>

Aikido integrates seamlessly with repositories containing `port.yaml` files for [Port.io](https://port.io). This allows for the automatic importing of teams, taking into account the path of where the file is located.

#### How It Works <a href="#how-it-works" id="how-it-works"></a>

1. Aikido scans repositories for `port.yaml` files.
2. Aikido looks for the `team` field in the file and imports this as team.
3. Aikido records the exact path of each `port.yaml` file, ensuring the team is responsible for those specific paths (and repositories).

## How to select your team in UI <a href="#how-to-select-your-team-in-ui" id="how-to-select-your-team-in-ui"></a>

**Aikido's Feed** features a **team filter** at the top of the page. This filter allows users to tailor the feed to display only the issues relevant to selected teams. This filter can be used on basically every page in Aikido (feed, reports, settings etc).

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-61296e08665b9c3e6e29330ab62bf16a1916b53d%2Fmanaging-user-access-with-teams_1c6dccbd-d42b-46d0-afb8-741ac1a85163.png?alt=media)
