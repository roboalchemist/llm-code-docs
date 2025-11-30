# Source: https://dagshub.com/docs/quick_start/connect_existing_project/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTggMTJoOHYySDh6bTIgOEg2VjRoN3Y1aDV2My4xbDItMlY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNHptLTItMmg0LjFsLjktLjlWMTZIOHptMTIuMi01Yy4xIDAgLjMuMS40LjJsMS4zIDEuM2MuMi4yLjIuNiAwIC44bC0xIDEtMi4xLTIuMSAxLTFjLjEtLjEuMi0uMi40LS4ybTAgMy45TDE0LjEgMjNIMTJ2LTIuMWw2LjEtNi4xeiIgLz48L3N2Zz4=)](https://dagshub.com/DagsHub-Official/dagshub-docs/src/main/docs/quick_start/connect_existing_project.md "Edit this page")

# Connect an existing project to DagsHub[¶](#connect-an-existing-project-to-dagshub "Permanent link")

Hello, and welcome to DagsHub! We\'re happy to have you with us! In this guide, we\'ll walk you through setting up and configuring DagsHub to start building your ML project. The first step is creating a DagsHub repository to host your project. If you don\'t have an existing project and are starting from scratch, check out the guide on [creating a new repository](../create_new_project/).

## Video Tutorial[¶](#video-tutorial "Permanent link")

# An error occurred. 

Unable to execute JavaScript.

## Step-by-Step Guide[¶](#step-by-step-guide "Permanent link")

Whether your project is hosted on GitHub, GitLab, BitBucket, or any other Git provider, this guide will walk you through the process of connecting your project to DagsHub. By connecting your project to DagsHub, you\'ll gain access to data hosting and versioning, experiment tracking, model registry, data annotations, and collaboration capabilities, designed specifically for machine learning projects.

### Connecting projects from GitHub to DagsHub[¶](#connecting-projects-from-github-to-dagshub "Permanent link")

If you have a GitHub project ready to connect, you can get started in less than a minute!

1.  Press the blue **Create +** button on the top right and click **+ New Repository**
2.  Select the **Import Repository** card
3.  Click on the GitHub **Connect** button and authorize in GitHub
4.  Click the **Add/Revoke Access** button and choose to give access to all your repositories or specific ones.
5.  Click the repository you want to connect on DagsHub and click **Connect Repository**.

\

\
~DagsHub\ connect~

\

### Connecting & Migrating projects for GitLab, Bitbucket and Other Git servers to DagsHub[¶](#connecting-migrating-projects-for-gitlab-bitbucket-and-other-git-servers-to-dagshub "Permanent link")

If your project is hosted on GitLab, BitBucket, or any other Git provider you can connect of migrate it to DagsHub. The migration process is identical to the connection but assumes you want to move the project\'s development entirely to DagsHub. Therefore, it will create a new Git remote server for the project and clone all the files from the original Git server to it.

### Connecting your project[¶](#connecting-your-project "Permanent link")

Use this when you need a lasting connection between your project on the other git server and DagsHub, for example when you\'re working with other team members that aren\'t on the ML team.

- Click the **Create +** button and choose the **+ New Repository** option.

[![Import repository](../../integration_guide/assets/git_server/connect-1a.png)](../../integration_guide/assets/git_server/connect-1a.png)

- Select the **Import Repository** card.

[![Import repository](../../integration_guide/assets/git_server/connect-1b.png)](../../integration_guide/assets/git_server/connect-1b.png)\
~Mirror\ a\ repo~

- Choose the **Other** option on the Connection menu.

[![Other repository](../../integration_guide/assets/git_server/connect-2.png)](../../integration_guide/assets/git_server/connect-2.png)\
~Mirror\ a\ repo~

- Fill in the connection information:

[![Connect a repo](../../integration_guide/assets/git_server/connect-3.png)](../../integration_guide/assets/git_server/connect-3.png)\
~Connect\ a\ repo~

1.  The Git server address - can be an HTTP/HTTPS/GIT URL.
2.  If it requires authorization to access the Git server, please add the user name and authentication token (or password) needed to access it.
3.  The new DagsHub repository settings:
    - The repository owner (mandatory) - can be a user or an organization.
    - The repository name (mandatory).
    - Visibility (optional).
    - Description (optional).
4.  Select **Mirror** under *Connectivity Mode*.
5.  Launch the Connection.

### Migrating your project DagsHub?[¶](#migrating-your-project-dagshub "Permanent link")

Use this option if you want to move your project completely to DagsHub and work on it there. This is effectively creates a disconnected copy of the project on DagsHub.

Follow the same steps as above, but select **Migrate** under *Connectivity Mode*.

[![Migrate a repo](../../integration_guide/assets/git_server/migrate-3.png)](../../integration_guide/assets/git_server/migrate-3.png)\
~Migrate\ a\ repo~

If you need to mirror or migrate a Git server not hosted on GitHub, follow this [guide](../../integration_guide/connect_a_git_server_to_dagshub/).

## Next Steps[¶](#next-steps "Permanent link")

Now that you have your project set up, you can continue to [upload your data](../upload_data/), [track experiments](../../use_cases/track_ml_experiments/), or check out some of our other common [use cases](../../use_cases/).

Was this page helpful?

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxME0xMCA5LjVjMCAuOC0uNyAxLjUtMS41IDEuNVM3IDEwLjMgNyA5LjUgNy43IDggOC41IDhzMS41LjcgMS41IDEuNW03IDBjMCAuOC0uNyAxLjUtMS41IDEuNVMxNCAxMC4zIDE0IDkuNSAxNC43IDggMTUuNSA4czEuNS43IDEuNSAxLjVtLTUgNy43M2MtMS43NSAwLTMuMjktLjczLTQuMTktMS44MUw5LjIzIDE0Yy40NS43MiAxLjUyIDEuMjMgMi43NyAxLjIzczIuMzItLjUxIDIuNzctMS4yM2wxLjQyIDEuNDJjLS45IDEuMDgtMi40NCAxLjgxLTQuMTkgMS44MSIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxMG0tNi41LTRjLjggMCAxLjUuNyAxLjUgMS41cy0uNyAxLjUtMS41IDEuNS0xLjUtLjctMS41LTEuNS43LTEuNSAxLjUtMS41TTEwIDkuNWMwIC44LS43IDEuNS0xLjUgMS41UzcgMTAuMyA3IDkuNSA3LjcgOCA4LjUgOHMxLjUuNyAxLjUgMS41bTIgNC41YzEuNzUgMCAzLjI5LjcyIDQuMTkgMS44MWwtMS40MiAxLjQyQzE0LjMyIDE2LjUgMTMuMjUgMTYgMTIgMTZzLTIuMzIuNS0yLjc3IDEuMjNsLTEuNDItMS40MkM4LjcxIDE0LjcyIDEwLjI1IDE0IDEyIDE0IiAvPjwvc3ZnPg==)

Thanks for your feedback!

Thanks for your feedback! Help us improve this page by creating an [issue in our Docs repo](https://dagshub.com/DAGsHub-Official/dagshub-docs/issues).