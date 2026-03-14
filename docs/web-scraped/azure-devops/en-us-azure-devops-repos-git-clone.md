# Source: https://learn.microsoft.com/en-us/azure/devops/repos/git/clone?view=azure-devops

Title: Clone an existing Git repo - Azure Repos

URL Source: https://learn.microsoft.com/en-us/azure/devops/repos/git/clone?view=azure-devops

Markdown Content:
**Azure DevOps Services | Azure DevOps Server | Azure DevOps Server 2022**

**Visual Studio 2019 | Visual Studio 2022**

You can create a local copy of a remote Git repo by cloning it into a local folder on your computer. Cloning a remote repo downloads all [commits](https://learn.microsoft.com/en-us/azure/devops/repos/git/commits?view=azure-devops) on all [branches](https://learn.microsoft.com/en-us/azure/devops/repos/git/create-branch?view=azure-devops) of the repo, unless you use the `--single-branch` clone option. Cloning links each branch in your new local repo with the corresponding branch in the remote repo. That way, when you [push](https://learn.microsoft.com/en-us/azure/devops/repos/git/pushing?view=azure-devops) to share your local branch changes with your team, the corresponding remote branch is updated. Similarly, when you [pull](https://learn.microsoft.com/en-us/azure/devops/repos/git/pulling?view=azure-devops) to update your local branch with changes made by your team, updates from the corresponding remote branch are retrieved. The remote repo can be an **Azure Repos** Git repo, a **GitHub** repo, or other hosted Git repo.

This article provides procedures for the following tasks:

*   Get the clone URL for an **Azure Repos** Git repo
*   Get the clone URL for a **GitHub** repo
*   Clone an **Azure Repos** Git repo
*   Clone a **GitHub** repo
*   Clone any Git repo
*   Open a Visual Studio solution from a cloned repo

For an overview of the Git workflow, see [Azure Repos Git tutorial](https://learn.microsoft.com/en-us/azure/devops/repos/git/gitworkflow?view=azure-devops).

| Category | Requirements |
| --- | --- |
| **Project access** | Member of a [project](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/create-project?view=azure-devops). |
| **Permissions** | - View code in private projects: At least **Basic** access. - Clone or contribute to code in private projects: Member of the **Contributors** security group or corresponding permissions in the project. - Set branch or repository permissions: **Manage permissions** permissions for the branch or repository. - Change default branch: **Edit policies** permissions for the repository. - Import a repository: Member of the **Project Administrators** security group or Git project-level **Create repository** permission set to **Allow**. For more information, see [Set Git repository permissions](https://learn.microsoft.com/en-us/azure/devops/repos/git/set-git-repository-permissions?view=azure-devops). |
| **Services** | [Repos enabled](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/set-services?view=azure-devops). |
| **Tools** | Optional. Use **az repos** commands: [Azure DevOps CLI](https://learn.microsoft.com/en-us/azure/devops/cli/?view=azure-devops). |

Note

In public projects, users with **Stakeholder** access have full access to Azure Repos, including viewing, cloning, and contributing to code.

| Category | Requirements |
| --- | --- |
| **Project access** | Member of a [project](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/create-project?view=azure-devops). |
| **Permissions** | - View code: At least **Basic** access. - Clone or contribute to code: Member of the **Contributors** security group or corresponding permissions in the project. |
| **Services** | [Repos enabled](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/set-services?view=azure-devops). |

Typically, you need to know the clone URL of the remote repo that you want to clone. The clone URL uniquely identifies the remote repo.

Note

When you're signed into an Azure DevOps project, Visual Studio supports searching for and cloning project repos without needing to know the clone URL.

1.   From your web browser, open the team project for your Azure DevOps organization, and then choose **Repos**>**Files** to open the **Files** view.

[![Image 1: Screenshot of the Azure DevOps project page.](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/clone/visual-studio-2019/common/repos-files.png?view=azure-devops)](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/clone/visual-studio-2019/common/repos-files-lrg.png?view=azure-devops#lightbox)

2.   In the **Files** view, choose **Clone** to launch the **Clone Repository** popup.

[![Image 2: Screenshot of the Clone button on the Azure DevOps repo page.](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/clone/visual-studio-2019/common/azure-repo.png?view=azure-devops)](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/clone/visual-studio-2019/common/azure-repo-lrg.png?view=azure-devops#lightbox)

3.   Copy the clone URL from the **Clone Repository** popup.

[![Image 3: Screenshot of the Clone Repository popup on the Azure DevOps project site.](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/clone/visual-studio-2019/common/azure-clone-repo.png?view=azure-devops)](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/clone/visual-studio-2019/common/azure-clone-repo-lrg.png?view=azure-devops#lightbox)

Typically, you need to know the clone URL of the remote repo that you want to clone. The clone URL uniquely identifies the remote repo.

Note

When you're signed into **GitHub**, Visual Studio supports searching for and cloning GitHub repos without needing to know the clone URL.

1.   Open a browser and go to your **GitHub** account, select the **Repositories** tab, and choose the repository to clone.

[![Image 4: Screenshot of the repository page on the GitHub site.](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/clone/visual-studio-2019/common/github-repo.png?view=azure-devops)](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/clone/visual-studio-2019/common/github-repo-lrg.png?view=azure-devops#lightbox)

2.   On the **GitHub** repository page, choose **Code** to launch the **Clone** popup. Copy the clone URL from the **Clone** popup.

[![Image 5: Screenshot of the Clone popup on the GitHub site.](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/clone/visual-studio-2019/common/github-clone-repo.png?view=azure-devops)](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/clone/visual-studio-2019/common/github-clone-repo-lrg.png?view=azure-devops#lightbox)

Tip

**Microsoft Entra ID tokens are the recommended authentication method** for Git operations. The "Generate Git Credentials" button was removed in January 2025 to encourage the use of more secure authentication methods. For all available authentication options, including the preferred Microsoft Entra OAuth tokens, see the [Authentication overview](https://learn.microsoft.com/en-us/azure/devops/repos/git/auth-overview?view=azure-devops).

By signing in as a member of an Azure DevOps project, you can clone private repos that are accessible to you, and public repos. Visual Studio supports search, clone, and sync operations on repos that are accessible through authentication.

Note

You can clone a public **Azure Repos** Git repo without signing in as a member of its parent Azure DevOps project. To clone a public Git repo without signing in, see [Clone any Git repo](https://learn.microsoft.com/en-us/azure/devops/repos/git/clone?view=azure-devops#clone-any-git-repo) and then connect to a project in Azure DevOps.

*   [Visual Studio 2022](https://learn.microsoft.com/en-us/azure/devops/repos/git/clone?view=azure-devops#tabpanel_1_visual-studio-2022)
*   [Visual Studio 2019 - Git menu](https://learn.microsoft.com/en-us/azure/devops/repos/git/clone?view=azure-devops#tabpanel_1_visual-studio-2019-git-menu)
*   [Visual Studio 2019 - Team Explorer](https://learn.microsoft.com/en-us/azure/devops/repos/git/clone?view=azure-devops#tabpanel_1_visual-studio-2019-team-explorer)
*   [Git Command Line](https://learn.microsoft.com/en-us/azure/devops/repos/git/clone?view=azure-devops#tabpanel_1_git-command-line)

Visual Studio 2022 provides a Git version control experience by using the **Git** menu, **Git Changes**, and through context menus in **Solution Explorer**. Visual Studio 2019 version 16.8 also offers the **Team Explorer** Git user interface. For more information, see the **Visual Studio 2019 - Team Explorer** tab.

1.   From the **Git** menu on the menu bar, choose **Clone Repository** to open the **Clone a repository** window.

[![Image 6: Screenshot of the 'Clone Repository' option in the Git menu in Visual Studio.](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/clone/visual-studio-2019/git-experience/clone-repo.png?view=azure-devops)](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/clone/visual-studio-2019/git-experience/clone-repo-lrg.png?view=azure-devops#lightbox)

2.   In the **Clone a repository** window, select **Azure DevOps** under **Browse a repository** to open the **Connect to a Project** window.

[![Image 7: Screenshot of the 'Clone Repository' window in Visual Studio.](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/clone/visual-studio-2019/git-experience/clone-azure-devops-repo.png?view=azure-devops)](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/clone/visual-studio-2019/git-experience/clone-azure-devops-repo-lrg.png?view=azure-devops#lightbox)

3.   In the **Connect to a Project** window, sign in to Azure DevOps and choose the remote repo you want to clone. You can use the search box to filter the list of remote repos. If you don't see the remote repo, select **Add Azure DevOps Server** to add the server that hosts the repo. Verify the local folder path where you want the local clone to be created, and then select **Clone**.

[![Image 8: Screenshot of the 'Connect to a Project' window in Visual Studio 2019.](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/clone/visual-studio-2019/team-explorer/connect-add-server.png?view=azure-devops)](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/clone/visual-studio-2019/team-explorer/connect-add-server-lrg.png?view=azure-devops#lightbox)

After you've cloned a remote Git repo, Visual Studio detects the local clone and adds it to the list of **Local Repositories** in the **Git** menu.

[![Image 9: Screenshot of the 'Local Repositories' option from the Git menu in Visual Studio 2019.](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/clone/visual-studio-2019/common/local-repositories.png?view=azure-devops)](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/clone/visual-studio-2019/common/local-repositories-lrg.png?view=azure-devops#lightbox)

By signing into **GitHub** or using SSH authentication, you can clone private repos that are accessible to you, and public repos. Visual Studio supports search, clone, and sync operations on repos that are accessible through authentication.

Note

You can clone a public **GitHub** repo without signing in to GitHub or otherwise authenticating. To clone a public Git repo without signing in, see [Clone any Git repo](https://learn.microsoft.com/en-us/azure/devops/repos/git/clone?view=azure-devops#clone-any-git-repo).

*   [Visual Studio 2022](https://learn.microsoft.com/en-us/azure/devops/repos/git/clone?view=azure-devops#tabpanel_2_visual-studio-2022)
*   [Visual Studio 2019 - Git menu](https://learn.microsoft.com/en-us/azure/devops/repos/git/clone?view=azure-devops#tabpanel_2_visual-studio-2019-git-menu)
*   [Visual Studio 2019 - Team Explorer](https://learn.microsoft.com/en-us/azure/devops/repos/git/clone?view=azure-devops#tabpanel_2_visual-studio-2019-team-explorer)
*   [Git Command Line](https://learn.microsoft.com/en-us/azure/devops/repos/git/clone?view=azure-devops#tabpanel_2_git-command-line)

1.   From the **Git** menu on the menu bar, choose **Clone Repository** to open the **Clone a repository** window.

[![Image 10: Screenshot of the 'Clone Repository' option in the Git menu in Visual Studio.](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/clone/visual-studio-2019/git-experience/clone-repo.png?view=azure-devops)](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/clone/visual-studio-2019/git-experience/clone-repo-lrg.png?view=azure-devops#lightbox)

2.   In the **Clone a repository** window, select **GitHub** under **Browse a repository** to open the **Open from GitHub** window.

[![Image 11: Screenshot of the GitHub option in the 'Clone Repository' window in Visual Studio.](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/clone/visual-studio-2019/git-experience/clone-github-repo.png?view=azure-devops)](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/clone/visual-studio-2019/git-experience/clone-github-repo-lrg.png?view=azure-devops#lightbox)

3.   In the **Open from GitHub** window, sign in to **GitHub** and choose the remote repo you want to clone. You can use the search box to filter the list of remote repos. Verify the local folder path where you want the local clone to be created, and then choose **Clone**.

[![Image 12: Screenshot of the 'Open from GitHub' window in Visual Studio.](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/clone/visual-studio-2019/git-experience/open-from-github.png?view=azure-devops)](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/clone/visual-studio-2019/git-experience/open-from-github-lrg.png?view=azure-devops#lightbox)

After you've cloned a remote Git repo, Visual Studio detects the local clone and adds it to the list of **Local Repositories** in the **Git** menu.

[![Image 13: Screenshot of the 'Local Repositories' option from the Git menu in Visual Studio 2019.](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/clone/visual-studio-2019/common/local-repositories.png?view=azure-devops)](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/clone/visual-studio-2019/common/local-repositories-lrg.png?view=azure-devops#lightbox)

You can clone any Git repo that's accessible to you by using the clone URL of the repo.

*   [Visual Studio 2022](https://learn.microsoft.com/en-us/azure/devops/repos/git/clone?view=azure-devops#tabpanel_3_visual-studio-2022)
*   [Visual Studio 2019 - Git menu](https://learn.microsoft.com/en-us/azure/devops/repos/git/clone?view=azure-devops#tabpanel_3_visual-studio-2019-git-menu)
*   [Visual Studio 2019 - Team Explorer](https://learn.microsoft.com/en-us/azure/devops/repos/git/clone?view=azure-devops#tabpanel_3_visual-studio-2019-team-explorer)
*   [Git Command Line](https://learn.microsoft.com/en-us/azure/devops/repos/git/clone?view=azure-devops#tabpanel_3_git-command-line)

1.   From the **Git** menu on the menu bar, choose **Clone Repository** to open the **Clone a repository** window.

[![Image 14: Screenshot of the 'Clone Repository' option in the Git menu in Visual Studio.](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/clone/visual-studio-2019/git-experience/clone-repo.png?view=azure-devops)](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/clone/visual-studio-2019/git-experience/clone-repo-lrg.png?view=azure-devops#lightbox)

2.   In the **Clone a repository** window, enter the clone URL of the remote Git repo that you want to clone, verify the local folder path where you want to create the local clone, and then choose **Clone**.

[![Image 15: Screenshot of the 'Clone a repository' window in Visual Studio.](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/clone/visual-studio-2019/git-experience/specify-repo.png?view=azure-devops)](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/clone/visual-studio-2019/git-experience/specify-repo-lrg.png?view=azure-devops#lightbox)

After you've cloned a remote Git repo, Visual Studio detects the local clone and adds it to the list of **Local Repositories** in the **Git** menu.

[![Image 16: Screenshot of the 'Local Repositories' option from the Git menu in Visual Studio 2019.](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/clone/visual-studio-2019/common/local-repositories.png?view=azure-devops)](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/clone/visual-studio-2019/common/local-repositories-lrg.png?view=azure-devops#lightbox)

*   [Visual Studio 2022](https://learn.microsoft.com/en-us/azure/devops/repos/git/clone?view=azure-devops#tabpanel_4_visual-studio-2022)
*   [Visual Studio 2019 - Git menu](https://learn.microsoft.com/en-us/azure/devops/repos/git/clone?view=azure-devops#tabpanel_4_visual-studio-2019-git-menu)
*   [Visual Studio 2019 - Team Explorer](https://learn.microsoft.com/en-us/azure/devops/repos/git/clone?view=azure-devops#tabpanel_4_visual-studio-2019-team-explorer)
*   [Git Command Line](https://learn.microsoft.com/en-us/azure/devops/repos/git/clone?view=azure-devops#tabpanel_4_git-command-line)

1.   Choose the **File > Open > Project/Solution** from the menu bar, and select the solution file to open.

[![Image 17: Screenshot of the Open Solution option in the File menu in Visual Studio.](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/clone/visual-studio-2019/git-experience/open-solution.png?view=azure-devops)](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/clone/visual-studio-2019/git-experience/open-solution-lrg.png?view=azure-devops#lightbox)

2.   The Visual Studio solution that you selected is now open in **Solution Explorer**.

[![Image 18: Screenshot of an open solution in 'Solution Explorer' in Visual Studio.](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/clone/visual-studio-2019/git-experience/open-solution-explorer.png?view=azure-devops)](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/clone/visual-studio-2019/git-experience/open-solution-explorer-lrg.png?view=azure-devops#lightbox)

*   [New to Git repos? Learn more](https://learn.microsoft.com/en-us/devops/develop/git/set-up-a-git-repository)
