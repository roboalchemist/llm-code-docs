# Source: https://help.aikido.dev/getting-started/manage-teams-and-applications/manage-and-view-your-apps-and-projects-via-our-teams-feature.md

# Manage and View Your Apps and Projects via Our Teams Feature

## Introduction <a href="#introduction" id="introduction"></a>

Aikido lets you create teams, connect multiple repositories and clouds to have a clear overview of your apps and projects. This project/app view is available throughout the entire Aikido app, going from feed, alerting and reporting. This article focuses on using Teams in order to group resources into Project and Apps. Managing of User Access. If you are looking to manage User Access with teams, please [**click here**](https://help.aikido.dev/getting-started/manage-teams-and-applications/managing-user-access-with-teams).

## Use Cases <a href="#use-cases" id="use-cases"></a>

* **Agency Project Management:** Agencies frequently handle multiple clients, necessitating a structured approach to manage each client's repositories separately. Aikido facilitates this by allowing the creation of teams for each client, making it straightforward to organize and access client-specific repositories. Additionally, this allows for easy generation of client-specific reports.

  ![Dropdown menu for selecting "All teams" or individual client teams.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-fc75651468dd17ae319af297704658fc64a26e34%2Fmanage-and-view-your-apps-and-projects-via-our-teams-feature_a746b534-b6eb-4c21-bbdc-1265ab24b74f.png?alt=media)
* **Specify resources connect to an app:** you can use the team functionality to combine resources that are part of the same app (combination of repos, containers and clouds). This also allows you to view all reports
* **Better overview when using a monorepo split.** You can assign team members to specific directories of your monorepo, improving their overview. More information on splitting monorepositories can be found [here](https://help.aikido.dev/en/articles/9026666-splitting-up-your-monorepo-per-directory).

{% hint style="info" %}
Repo linking is only available for manually created teams (not imported from SCM). Other resources like containers, clouds & Zen apps can be linked to both manually created and SCM-imported teams.
{% endhint %}

## How To Create Teams <a href="#how-to-create-teams" id="how-to-create-teams"></a>

**Step 1:** Navigate to **Settings -> Teams**\
​

![Team dashboard for “mdschuym” showing 4 active repositories and management options.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-0b18ccf8b33376a81bcb2be0b155c8ea75bf054a%2Fmanage-and-view-your-apps-and-projects-via-our-teams-feature_5986952f-2c5a-4fc5-bbab-78742b2d10d0.png?alt=media)

**Step 2:** Click **Create Team** and give your team a name\
​

![Form to create a new team by entering a team name for vulnerability tracking.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-2df987cb28febd5270a9e0f37b72b13d15f2eaee%2Fmanage-and-view-your-apps-and-projects-via-our-teams-feature_86bb94a8-6266-4192-945a-873e275bfc36.png?alt=media)

**Step 3 (optional):** **Add team members** to the newly created team.

![User management interface for assigning people to the "Architects" team.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-360a0c5347426b99a212daa1a65be6b91a03be63%2Fmanage-and-view-your-apps-and-projects-via-our-teams-feature_56480ec4-3c43-4324-a974-31492495dd76.png?alt=media)

**Step 4:** **Link different resources** via the **responsibility tab.** You can add different resources such as repositories, clouds, containers, domains and zen apps. You can add repositories and containers **in bulk** via the [repository](https://app.aikido.dev/settings/integrations/repositories) and [container settings](https://app.aikido.dev/settings/container-image-registry) screen.

> If you want to link specific domains to a team, you can set this up by linking your domains to a repo or container. It will automatically inherit access permissions.

![Interface for linking repositories, cloud, or container resources to the Backend team.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FuyEJzLnw6eQHoLdBUAiw%2FScreenshot%202025-12-15%20at%2016.21.52.png?alt=media\&token=ce29fb76-f6bc-4401-a7e3-e81bd279ef20)

**Step 5.** Go back to your feed and filter on a specific team. You should only see issues that are related to those repositories and clouds that were attached to the team.

## How to select your team in UI <a href="#how-to-select-your-team-in-ui" id="how-to-select-your-team-in-ui"></a>

**Aikido's Feed** features a **team filter** at the top of the page. This filter allows users to tailor the feed to display only the issues relevant to selected teams. This filter can be used on basically every page in Aikido (feed, reports, settings etc).

![Team filter dropdown with stats for solved and newly detected issues this week.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-61296e08665b9c3e6e29330ab62bf16a1916b53d%2Fmanage-and-view-your-apps-and-projects-via-our-teams-feature_4709269e-976a-487e-af63-80160fbc3907.png?alt=media)
