# Source: https://docs.sonarsource.com/sonarqube-server/10.6/project-administration/maintaining-the-branches-of-your-project.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/project-administration/maintaining-the-branches-of-your-project.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/project-administration/maintaining-the-branches-of-your-project.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/project-administration/maintaining-the-branches-of-your-project.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/project-administration/maintaining-the-branches-of-your-project.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/project-administration/maintaining-the-branches-of-your-project.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/project-administration/maintaining-the-branches-of-your-project.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/project-administration/maintaining-the-branches-of-your-project.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/project-administration/maintaining-project/maintaining-the-branches-of-your-project.md

# Source: https://docs.sonarsource.com/sonarqube-server/project-administration/maintaining-project/maintaining-the-branches-of-your-project.md

# Maintaining project branches

### Renaming the main branch <a href="#rename-main-branch" id="rename-main-branch"></a>

Your main branch can be renamed from the project settings at **Project Settings** > **Branches and Pull Requests**. This is used mainly to maintain branch history when upgrading from SonarQube Community Build to a SonarQube Server commercial edition (see section below).

### Choosing a new main branch <a href="#new-main-branch" id="new-main-branch"></a>

You can choose a different, existing branch to become the new main branch of a project. To do this:

1. Go to **Project Settings** > **Branches & Pull Requests**.
2. On the list of branches, click on the Actions cog button for the branch you want to make your main branch and click **Set as main branch**.

Changing the main branch of your project will trigger [reindexing](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/maintenance/reindexing "mention") and may impact the level of information that is available for your project until reindexing is complete.

#### Impacts of choosing a new main branch <a href="#impacts-of-choosing-a-new-main-branch" id="impacts-of-choosing-a-new-main-branch"></a>

Choosing a new main branch has an effect on:

* **New code:** When some of a project’s branches use the main branch as a reference branch, changing the main branch does not update the new code settings. All branches continue to point to the previous main branch. If you want your reference branch to point to the new main branch, you must update the new code settings manually.
* **Applications:** The main branch of an application always references the main branch of a project, and changing the main branch of the project changes the main branch of the application. When a project’s main branch changes, the application is automatically scheduled for recomputation (see [managing-applications](https://docs.sonarsource.com/sonarqube-server/project-administration/managing-applications "mention")). After you change the main branch of a project, it can take a few minutes to propagate to the application.
* **Portfolios:** Portfolios are different from applications, as they can either reference the main branch of a project or a project’s branch specifically.
  * In the first case, if you change the project’s main branch, the portfolio starts referencing the new main branch of the project. The recomputation mechanics are the same as for applications.
  * In the second case, changing the project’s main branch does not change the portfolio, as the portfolio is referencing a specific branch.
* **Branch analysis:**
  * **Impacts on CI setup:** It is possible to analyze a branch without passing an explicit branch name (`sonar.branch.name`). In this case, the analysis automatically points to the main branch of the project. If you change the main branch, you could unintentionally have analyses from the old main branch go to the new branch. To avoid this, ensure the branch analysis is always pointing to a specific branch.
  * **Impacts on analysis processing:** If you change the main branch during a busy load of background tasks, it may impact certain background tasks that process analysis reports. This could lead to an inconsistent state. The solution is to re-analyze the project. This will put everything back into a consistent state.

### Deleting a branch <a href="#delete-branch" id="delete-branch"></a>

You can delete a branch in the **Branches** tab at **Project Settings** > **Branches and Pull Requests**.

### Managing inactive branches <a href="#manage-inactive-branches" id="manage-inactive-branches"></a>

Projects and branches that are not scanned for more than a configured number of consecutive days are considered inactive, and SonarQube Server automatically deletes their cached data to free space in the database. If a project has several branches, only the cache of its inactive branches is deleted.

You can configure at the global and project levels, branches to be kept from the automatic deletion when inactive.

{% hint style="info" %}
The main branch is always protected from automatic deletion, even if it’s inactive. This can’t be changed.
{% endhint %}

To configure the number of days after which an inactive branch is deleted:

* In **Administration** > **General Settings** > **Housekeeping**, set the **Number of days before deleting inactive branches.**

### Keeping specific branches from automatic deletion (permanent branches) <a href="#keep-specific-branches-from-deletion" id="keep-specific-branches-from-deletion"></a>

You can use naming patterns to protect specific branches, such as release branches, from automatic deletion. To do this, add one or several patterns under:

* At global level\*\*: Administration\*\* > **General Settings** > **Housekeeping** > **Branches** > **Branches to keep when inactive**
* At project level, from the page of the specific project: **Project settings** > **General Settings** > **Housekeeping** > **Branches** > **Branches to keep when inactive.**

When a branch is created with a name that follows one of these patterns, it will be kept indefinitely. For example, adding the pattern release/.\* would keep any branches named release/6.0, release/7, and so on.

{% hint style="info" %}
Patterns aren’t retroactive and won’t apply to branches that have already been created. They only apply to branches created after the pattern is set. You can protect an existing branch at the project level. See the following section.
{% endhint %}

You can protect a specific branch from the automatic deletion as follows:

* From the **Branches** page: in **Project Settings** > **Branches and Pull Requests** check **Keep when inactive**.

### Maintaining branch history when upgrading to a commercial edition <a href="#upgrade-to-commercial-edition" id="upgrade-to-commercial-edition"></a>

When upgrading to a current commercial edition version, automatic branch and pull request configuration creates branches based on their names in your code repository. If the name of your main branch in SonarQube Server doesn’t match the branch’s name in your code repository (this may be the case if you didn’t import the repository but created your project manually in SonarQube Server), the history of your main branch won’t be taken on by the branch you analyze.

**Before running analysis**, you can keep your branch history by renaming the main branch in SonarQube Server with the name of the branch in your code repository at **Project Settings** > **Branches and Pull Requests**.

For example, if your main branch is named `main` in SonarQube Server but `develop` in your code repository, rename your main branch to `develop` in SonarQube Server.
