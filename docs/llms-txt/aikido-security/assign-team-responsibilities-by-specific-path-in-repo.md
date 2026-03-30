# Source: https://help.aikido.dev/getting-started/manage-teams-and-applications/assign-team-responsibilities-by-specific-path-in-repo.md

# Assign Team Responsibilities by Specific Path in Repo

Assigning **specific repo paths** to teams in Aikido can help to streamline issue management in **large monorepos** and enabling **more granular reporting**.

### Use Cases <a href="#use-cases" id="use-cases"></a>

* **Monorepo management:** Assign specific paths to teams instead of the full monorepo. This allows you to filter your feed in a more granular way.
* **Specific reporting:** Allows reports to be generated based on service-level/path-level rather than at the repo level.

### Assigning Specific Paths <a href="#assigning-specific-paths" id="assigning-specific-paths"></a>

**Step 1:** Create a Team and Link Repositories (see [article](https://help.aikido.dev/getting-started/manage-teams-and-applications/managing-user-access-with-teams))

* Create a new team or select an existing one, then link the relevant repositories to this team.

**Step 2:** Click Limit Access By Path in the dropdown menu

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-3a01b2dcc3f32601d77662d9d9d9371cc37f2c40%2Fassign-team-responsibilities-by-specific-path-in-repo_e373539b-fc2c-4566-bd1a-49ea280c5386.png?alt=media)

**Step 3:** Enter the paths within the repo that you want the team to have access to.

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-df71db5c6ffd56f721b37087d38991706c629630%2Fassign-team-responsibilities-by-specific-path-in-repo_fe715668-3cdc-4ff9-8dee-953f92ad64f8.png?alt=media)

**Wildcard support**

`**` means anything in any subdirectory\
`*` means anything in the current directory\
`?` means any single char

**Step 4:** Filter Issues in Feed/Reports

Go to the **Feed** or **Reports** section. Apply a filter based on the team, and you will see only the issues related to the paths assigned to that team.

![Dashboard showing security findings, severity levels, and issue statuses for the "devs" team workspace.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-6aa40746080049d93c39e7df6a862098639abd72%2Fassign-team-responsibilities-by-specific-path-in-repo_12583652-fb59-4830-a140-36996db6ff3d.png?alt=media)
