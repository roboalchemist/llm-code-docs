# Source: https://dagshub.com/docs/integration_guide/connect_a_git_server_to_dagshub/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTggMTJoOHYySDh6bTIgOEg2VjRoN3Y1aDV2My4xbDItMlY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNHptLTItMmg0LjFsLjktLjlWMTZIOHptMTIuMi01Yy4xIDAgLjMuMS40LjJsMS4zIDEuM2MuMi4yLjIuNiAwIC44bC0xIDEtMi4xLTIuMSAxLTFjLjEtLjEuMi0uMi40LS4ybTAgMy45TDE0LjEgMjNIMTJ2LTIuMWw2LjEtNi4xeiIgLz48L3N2Zz4=)](https://dagshub.com/DagsHub-Official/dagshub-docs/src/main/docs/integration_guide/connect_a_git_server_to_dagshub.md "Edit this page")

# Mirror or Migrate a Git Server to DagsHub[¶](#mirror-or-migrate-a-git-server-to-dagshub "Permanent link")

If you have a project hosted on a Git provider (GitLab, BitBucket, etc.) and want to enjoy the added value DagsHub offers, you can easily mirror or migrate the project to DagsHub and enjoy the best of both worlds!

**Note:** *We have a tighter integration for Git servers hosted on GitHub. To learn more about it, please see the [GitHub Integration](../github/) docs.*

## How DagsHub Mirror / Migrate git servers?[¶](#how-dagshub-mirror-migrate-git-servers "Permanent link")

### Mirror a Git server[¶](#mirror-a-git-server "Permanent link")

When mirroring a remote Git server to DagsHub, behind the scenes, it clones all the commits and branches to the new DagsHub repository and displays them there. The original Git server stays the default Git remote while adding the unique DagsHub remotes (storage, experiment tracking, etc.) as an integral part of the project.

[![Mirror Remote](../assets/git_server/mirror-remote.png)](../assets/git_server/mirror-remote.png)\
~Mirrored\ repository\ remotes~

The repository will be automatically synced every 24 hours or triggered manually by clicking on the sync button next to the project name. Behind the scenes, DagsHub pulls all the changes from the remote Git server and displays them.

[![Sync button](../assets/git_server/mirror-sync.png)](../assets/git_server/mirror-sync.png)\
~Sync\ button~

### Mirror and Migrate Git servers[¶](#mirror-and-migrate-git-servers "Permanent link")

The migration process is identical to the connection but assumes you want to move the project\'s development entirely to DagsHub. Therefore, it will create a new Git remote server for the project and clone all the files from the original Git server to it. How to use it?

## How to mirror a Git server to DagsHub?[¶](#how-to-mirror-a-git-server-to-dagshub "Permanent link")

- Click the **Create +** button and choose the **+ New Repository** option.

[![Import a repository](../assets/git_server/connect-1a.png)](../assets/git_server/connect-1a.png)\
~Mirror\ a\ repo~

- Select the **Import Repository** card.

[![Import repository](../assets/git_server/connect-1b.png)](../assets/git_server/connect-1b.png)\
~Mirror\ a\ repo~

- Choose the **Other** option on the Connection menu.

[![Other repository](../assets/git_server/connect-2.png)](../assets/git_server/connect-2.png)\
~Mirror\ a\ repo~

- Fill in the connection information:

[![Connect a repo](../assets/git_server/connect-3.png)](../assets/git_server/connect-3.png)\
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

## How to migrate a Git server to DagsHub?[¶](#how-to-migrate-a-git-server-to-dagshub "Permanent link")

Follow the same steps as above, but select **Migrate** under *Connectivity Mode*.

[![Migrate a repo](../assets/git_server/migrate-3.png)](../assets/git_server/migrate-3.png)\
~Migrate\ a\ repo~

Was this page helpful?

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxME0xMCA5LjVjMCAuOC0uNyAxLjUtMS41IDEuNVM3IDEwLjMgNyA5LjUgNy43IDggOC41IDhzMS41LjcgMS41IDEuNW03IDBjMCAuOC0uNyAxLjUtMS41IDEuNVMxNCAxMC4zIDE0IDkuNSAxNC43IDggMTUuNSA4czEuNS43IDEuNSAxLjVtLTUgNy43M2MtMS43NSAwLTMuMjktLjczLTQuMTktMS44MUw5LjIzIDE0Yy40NS43MiAxLjUyIDEuMjMgMi43NyAxLjIzczIuMzItLjUxIDIuNzctMS4yM2wxLjQyIDEuNDJjLS45IDEuMDgtMi40NCAxLjgxLTQuMTkgMS44MSIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxMG0tNi41LTRjLjggMCAxLjUuNyAxLjUgMS41cy0uNyAxLjUtMS41IDEuNS0xLjUtLjctMS41LTEuNS43LTEuNSAxLjUtMS41TTEwIDkuNWMwIC44LS43IDEuNS0xLjUgMS41UzcgMTAuMyA3IDkuNSA3LjcgOCA4LjUgOHMxLjUuNyAxLjUgMS41bTIgNC41YzEuNzUgMCAzLjI5LjcyIDQuMTkgMS44MWwtMS40MiAxLjQyQzE0LjMyIDE2LjUgMTMuMjUgMTYgMTIgMTZzLTIuMzIuNS0yLjc3IDEuMjNsLTEuNDItMS40MkM4LjcxIDE0LjcyIDEwLjI1IDE0IDEyIDE0IiAvPjwvc3ZnPg==)

Thanks for your feedback!

Thanks for your feedback! Help us improve this page by creating an [issue in our Docs repo](https://dagshub.com/DAGsHub-Official/dagshub-docs/issues).