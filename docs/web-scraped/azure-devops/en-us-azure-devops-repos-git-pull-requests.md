# Source: https://learn.microsoft.com/en-us/azure/devops/repos/git/pull-requests?view=azure-devops

Title: Create a pull request to review and merge code - Azure Repos

URL Source: https://learn.microsoft.com/en-us/azure/devops/repos/git/pull-requests?view=azure-devops

Markdown Content:
**Azure DevOps Services | Azure DevOps Server | Azure DevOps Server 2022**

**Visual Studio 2019 | Visual Studio 2022**

Create pull requests (PRs) to change, review, and merge code in a [Git repository](https://learn.microsoft.com/en-us/azure/devops/repos/git/creatingrepo?view=azure-devops). You can create PRs from branches in the upstream repository or from branches in your [fork](https://learn.microsoft.com/en-us/azure/devops/repos/git/forks?view=azure-devops) of the repository. Your team can [review the PRs](https://learn.microsoft.com/en-us/azure/devops/repos/git/review-pull-requests?view=azure-devops) and give feedback on changes. Reviewers can step through the proposed changes, leave comments, and vote to approve or reject the PRs. Depending on [branch policies](https://learn.microsoft.com/en-us/azure/devops/repos/git/branch-policies?view=azure-devops) and other requirements, your PR might need to meet various criteria before you can [complete the PR](https://learn.microsoft.com/en-us/azure/devops/repos/git/complete-pull-requests?view=azure-devops) and merge the changes into the target branch.

For PR guidelines and management considerations, see [About pull requests](https://learn.microsoft.com/en-us/azure/devops/repos/git/about-pull-requests?view=azure-devops).

| Category | Requirements |
| --- | --- |
| **Access levels** | - View or review PRs: At least **Basic access**. For public projects, users **Stakeholder access** have full access to Azure Repos. |
| **Permissions** | - Contribute to a PR: Member of the **Readers** security group or corresponding permissions. - Create and complete a PR: Member of the **Contributors** security group or corresponding permissions. |
| **Services** | [Repos enabled](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/set-services?view=azure-devops). |
| **Tools** | [Azure DevOps CLI](https://learn.microsoft.com/en-us/azure/devops/cli/?view=azure-devops). |

| Category | Requirements |
| --- | --- |
| **Access levels** | - View or review PRs: At least **Basic access**. |
| **Permissions** | - Contribute to a PR: Member of the **Readers** security group or corresponding permissions. - Create and complete a PR: Member of the **Contributors** security group or corresponding permissions. |
| **Services** | [Repos enabled](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/set-services?view=azure-devops). |

For more information about permissions and access, see [Default Git repository and branch permissions](https://learn.microsoft.com/en-us/azure/devops/organizations/security/default-git-permissions?view=azure-devops) and [About access levels](https://learn.microsoft.com/en-us/azure/devops/organizations/security/access-levels?view=azure-devops).

You can create a new PR from the Azure DevOps project website, from Visual Studio, or from the Azure DevOps CLI.

*   [Browser](https://learn.microsoft.com/en-us/azure/devops/repos/git/pull-requests?view=azure-devops#tabpanel_1_browser)
*   [Visual Studio](https://learn.microsoft.com/en-us/azure/devops/repos/git/pull-requests?view=azure-devops#tabpanel_1_visual-studio)
*   [Azure DevOps CLI](https://learn.microsoft.com/en-us/azure/devops/repos/git/pull-requests?view=azure-devops#tabpanel_1_azure-devops-cli)

From the Azure DevOps project website, you can create a new PR from:

*   [The Pull requests page](https://learn.microsoft.com/en-us/azure/devops/repos/git/pull-requests?view=azure-devops#from-the-pull-requests-page).
*   [A feature branch pushed to your repo](https://learn.microsoft.com/en-us/azure/devops/repos/git/pull-requests?view=azure-devops#from-a-pushed-branch).
*   [An existing PR, by using cherry-pick](https://learn.microsoft.com/en-us/azure/devops/repos/git/pull-requests?view=azure-devops#add-updates-with-cherry-pick).
*   [The Development control in a linked Azure Boards work item](https://learn.microsoft.com/en-us/azure/devops/repos/git/pull-requests?view=azure-devops#from-a-linked-work-item).

You can create PRs for any branch from your project's **Pull requests** page on the web.

1.   On the **Repos**>**Pull requests** page, select **New pull request** at upper right.

![Image 1: Screenshot of the New pull request button.](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/pull-requests/new-pr-button.png?view=azure-devops)

2.   Select the branch with the changes and the branch you want to merge the changes into, such as the main branch.

![Image 2: Screenshot of source and target branches for a P R in Azure Repos.](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/pull-requests/pr-branch-targets.png?view=azure-devops)

3.   [Enter your PR details](https://learn.microsoft.com/en-us/azure/devops/repos/git/pull-requests?view=azure-devops#finish) and create the PR.

After you push or update a feature branch, Azure Repos displays a prompt to create a PR.

*   On the **Pull requests** page:

![Image 3: Screenshot that shows the prompt to create a P R on the Pull Requests tab in Azure Repos.](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/pull-requests/create-pr-from-push-new-nav.png?view=azure-devops)

*   On the **Files** page:

![Image 4: Screenshot that shows the prompt to create a P R on the Files tab in Azure Repos.](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/pull-requests/create-pr-from-push-files-tab-new-nav.png?view=azure-devops)

Select **Create a pull request** to go to a page where you can [enter your PR details](https://learn.microsoft.com/en-us/azure/devops/repos/git/pull-requests?view=azure-devops#finish) and create the PR.

You can create a PR directly from an Azure Boards work item linked to the branch.

1.   In Azure Boards, from **Backlogs** or **Queries** in the **Work** view, open a work item linked to the branch.

2.   In the **Development** area of the work item, select **Create a pull request**.

![Image 5: Screenshot of creating a PR from the Development area of a work item with a linked branch.](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/pull-requests/create-pr-from-work-item.png?view=azure-devops)

The link takes you to a page where you can [enter your PR details](https://learn.microsoft.com/en-us/azure/devops/repos/git/pull-requests?view=azure-devops#finish) and create the PR.

You can copy commits from one branch to another by using cherry-pick. Unlike a merge or rebase, cherry-pick only brings the changes from the commits you select, instead of all the changes in a branch.

To cherry-pick changes from a completed PR, select **Cherry-pick** on the PR's **Overview** page. To copy changes from an active PR, select **Cherry-pick** from the PR's **More options** menu. This action creates a new branch with the copied changes. You can then create a new PR from the new branch. For detailed instructions, see [Copy changes with cherry-pick](https://learn.microsoft.com/en-us/azure/devops/repos/git/cherry-pick?view=azure-devops).

Before the first time you save a PR, you can switch the source and target branches of the PR by selecting the **Switch source and target branches** icon next to the branch names. Once the PR is active, this icon goes away, but you can still [change the target branch](https://learn.microsoft.com/en-us/azure/devops/repos/git/pull-requests?view=azure-devops#change-the-target-branch-of-a-pull-request) of the PR.

![Image 6: Screenshot of the switch source and target branches icon.](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/pull-requests/switch-branches.png?view=azure-devops)

A pull request template is a file containing Markdown text that populates the PR description when you create a PR. Good PR descriptions tell PR reviewers what to expect, and can help track tasks like adding unit tests and updating documentation. Your team can create a default PR template that adds text to all new PR descriptions in the repo. Also, you can select from branch-specific templates or other templates your team defines. For more information about creating and using PR templates, see [Improve pull request descriptions using templates](https://learn.microsoft.com/en-us/azure/devops/repos/git/pull-request-templates?view=azure-devops).

If your repo has a default template, all PRs in the repo have the default template's description text at creation. To add other templates, select **Add a template** and then choose a template from the dropdown list. You can edit the template text in your description, remove it, or add other text.

![Image 7: Screenshot showing Add a template when creating a P R.](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/pull-requests/use-template.png?view=azure-devops)

If your PR isn't ready for review, you can create a draft PR to indicate work in progress. When the PR is ready for review, you can publish it, and begin or resume the full review process.

Draft PRs have the following differences from published PRs:

*   Build validation policies don't run automatically. You can queue build validations manually by selecting the more options menu in the PR.

*   Voting is disabled while in draft mode.

*   Required reviewers aren't automatically added. Notifications are sent only to reviewers that you explicitly add to the draft PR.

*   Draft PRs display in the PR list with a **Draft** badge.

![Image 8: Screenshot showing a draft P R in the P R list.](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/pull-requests/draft-pull-request-badge.png?view=azure-devops)

*   [Browser](https://learn.microsoft.com/en-us/azure/devops/repos/git/pull-requests?view=azure-devops#tabpanel_2_browser)
*   [Visual Studio](https://learn.microsoft.com/en-us/azure/devops/repos/git/pull-requests?view=azure-devops#tabpanel_2_visual-studio)
*   [Azure DevOps CLI](https://learn.microsoft.com/en-us/azure/devops/repos/git/pull-requests?view=azure-devops#tabpanel_2_azure-devops-cli)

To create a draft PR, select the arrow next to **Create** and select **Create as draft** when creating the PR. You don't have to use title prefixes such as `WIP` or `DO NOT MERGE`.

![Image 9: Screenshot showing Create as draft PR.](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/pull-requests/create-draft-pr.png?view=azure-devops)

When you're ready to have the PR reviewed and completed, select **Publish** at upper right in the PR. Publishing a PR assigns required reviewers, evaluates policies, and kicks off voting.

![Image 10: Screenshot showing Publish for a PR.](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/pull-requests/publish-pr.png?view=azure-devops)

To change an existing published PR to a draft, choose **Mark as draft**. Marking a PR as draft removes all existing votes.

![Image 11: Screenshot showing Mark as draft.](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/pull-requests/mark-pr-as-draft.png?view=azure-devops)

*   [Browser](https://learn.microsoft.com/en-us/azure/devops/repos/git/pull-requests?view=azure-devops#tabpanel_3_browser)
*   [Visual Studio](https://learn.microsoft.com/en-us/azure/devops/repos/git/pull-requests?view=azure-devops#tabpanel_3_visual-studio)
*   [Azure DevOps CLI](https://learn.microsoft.com/en-us/azure/devops/repos/git/pull-requests?view=azure-devops#tabpanel_3_azure-devops-cli)

On the **New pull request** page, enter a **Title** and detailed **Description** of your changes, so others can see what problems the changes solve. On a new PR as in existing PRs, you can see the **Files** and **Commits** in your PR on separate tabs. You can add reviewers, link work items, and add tags to the PR.

When you're ready to have your changes reviewed, select **Create** to create the PR.

![Image 12: Screenshot that shows creating a new P R.](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/pull-requests/create-new-pull-request-2020.png?view=azure-devops)

Don't worry if you don't have all of the work items, reviewers, or details ready when you create your PR. You can add or update these items after you create the PR.

Keep the PR title and description up to date so reviewers can understand the changes in the PR.

You can update the title of an existing PR by selecting the current title and updating the text. Select the **Save** icon to save changes, or select the **Undo** icon to discard the changes.

Edit the PR description by selecting the **Edit** icon in the **Description** section.

![Image 13: Screenshot that shows editing the P R title and selecting the description Edit button.](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/pull-requests/pull-request-edit-title-description-2020.png?view=azure-devops)

*   [Browser](https://learn.microsoft.com/en-us/azure/devops/repos/git/pull-requests?view=azure-devops#tabpanel_4_browser)
*   [Visual Studio](https://learn.microsoft.com/en-us/azure/devops/repos/git/pull-requests?view=azure-devops#tabpanel_4_visual-studio)
*   [Azure DevOps CLI](https://learn.microsoft.com/en-us/azure/devops/repos/git/pull-requests?view=azure-devops#tabpanel_4_azure-devops-cli)

You can add reviewers in the **Reviewers** section of a new or existing PR. You can also change optional reviewers to required, change required reviewers to optional, or remove them, unless they're required by policy.

Branch policies can [require a minimum number of reviewers](https://learn.microsoft.com/en-us/azure/devops/repos/git/branch-policies?view=azure-devops#require-a-minimum-number-of-reviewers) or automatically include certain optional or required reviewers in PRs. You can't remove reviewers required by branch policy, but you can change optional reviewers to required or remove them.

To see the branch policy that automatically added a reviewer, right-select **More options** next to the reviewer in the **Reviewers** section of the PR **Overview** page.

![Image 14: Screenshot that shows View policy on a reviewer that's automatically included by branch policy.](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/pull-requests/view-policy.png?view=azure-devops)

If the user or group you want to review your PR isn't a member of your project, [add them to the project](https://learn.microsoft.com/en-us/azure/devops/organizations/security/add-users-team-project?view=azure-devops) before you can add them as reviewers.

To add reviewers to a new PR, do the following steps:

1.   On the **New pull request** page, under **Reviewers**, select **Search users and groups to add as reviewers**.
2.   As you enter a name or email address, a dropdown list shows a list of matching users and groups. Select names from the list to add as optional reviewers.
3.   To add required reviewers, select **Add required reviewers**, and then select **Search to add required reviewers** to search for and select the names.

![Image 15: Screenshot of adding a reviewer to a new P R.](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/pull-requests/add-reviewer.png?view=azure-devops)

To add reviewers to an existing PR, do the following steps:

1.   In the **Reviewers** section of the **Overview** page, select **Add**, and then select **Required reviewer** or **Optional reviewer**.

![Image 16: Pull request overview](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/pull-requests/pull-request-add-reviewer-v2.png?view=azure-devops)

2.   As you enter a name or email address, a list of matching users or groups appears. Select the names to add as reviewers.

![Image 17: Add P R reviewer.](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/pull-requests/pull-request-add-reviewer.png?view=azure-devops)

To change a reviewer between required and optional, or to remove a reviewer, select **More options** (⋮) to the right of the reviewer's name. To view the membership of a group or team designated as a reviewer, select the group's icon.

*   [Browser](https://learn.microsoft.com/en-us/azure/devops/repos/git/pull-requests?view=azure-devops#tabpanel_5_browser)
*   [Visual Studio](https://learn.microsoft.com/en-us/azure/devops/repos/git/pull-requests?view=azure-devops#tabpanel_5_visual-studio)
*   [Azure DevOps CLI](https://learn.microsoft.com/en-us/azure/devops/repos/git/pull-requests?view=azure-devops#tabpanel_5_azure-devops-cli)

To link work items to a new PR, do the following steps:

1.   On the **New pull request** page, under **Work items to link**, select **Search work items by ID or title**.
2.   Start entering a work item ID or title, and select the work item to link from the dropdown list that appears. 
    *   Search by title returns work items filtered by state; all work items with states categorized as **Completed** and **Removed** are excluded.
    *   These work items also get filtered by date and user, showing only items created or updated in the last 30 days. They should be created by, assigned to, or authorized as the current user.

To link work items to an existing PR, do the following steps:

1.   On the PR **Overview** tab, in the **Work items** area, select **+**.

![Image 18: Screenshot that shows selecting the Overview tab and the work items section.](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/pull-requests/pull-request-link-work-items-2020.png?view=azure-devops)

2.   Enter the ID of the work item or search for the work item title. Select the work item from the list that appears.

Remove a work item link by selecting the **x** icon next to the work item. Removing a link only removes the link between the work item and the PR. Links created in the branch or from commits remain in the work item.

Use tags to show important details and help organize PRs. Tags can communicate extra information to reviewers, such as that the PR is still a work in progress, or is a hotfix for an upcoming release.

![Image 19: Screenshot showing P Rs with tags.](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/pull-requests/pull-request-labels.png?view=azure-devops)

To add a tag when creating a PR, type a tag name in the **Tags** section. After you create the PR, you can manage tags in the **Tags** section.

![Image 20: Screenshot that shows the P R Tags section highlighted.](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/pull-requests/pull-request-tags-section.png?view=azure-devops)

You can attach files, including images, to your PR during or after creation. Select the paper clip icon below the **Description** field, or drag and drop files directly into the **Description** field of the PR.

![Image 21: Screenshot that shows attaching files to the P R description during creation.](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/pull-requests/attachment.png?view=azure-devops)

For most teams, nearly all PRs target a default branch, such as `main` or `develop`. If you sometimes need to target a different branch, it's easy to forget to change the target branch when you create the PR. If that happens, you can change the target branch of an active PR:

1.   Select **More actions** at upper-right on the PR **Overview** page, and then select **Change target branch** from the dropdown menu.
2.   In the **Change target branch** pane, select **Choose a target branch**, select the new branch, and then select **Change**.

You can share a pull request by email to notify reviewers and communicate with team members. To share a PR:

1.   Select **More options** on the PR **Overview** page, and then select **Share pull request**.

![Image 22: Screenshot that shows selecting Share pull request on a P R's Overview page.](https://learn.microsoft.com/en-us/azure/devops/repos/git/media/pull-requests/share.png?view=azure-devops)

2.   On the **Share pull request** screen, add recipients by typing their names in the **To:** field and selecting from the user names that appear. You can also remove recipients.

3.   Add an optional message in the **Note (Optional)** field, and then select **Send**. Recipients receive an email requesting their attention and linking to the PR.

Note

When using the built-in email feature, you can only send emails to individual project members' addresses. Adding a team group or security group to the **To:** line isn't supported. If you add an unrecognized email address, you receive a message indicating that one or more recipients don't have permissions to read the mailed pull request.

*   [View pull requests](https://learn.microsoft.com/en-us/azure/devops/repos/git/view-pull-requests?view=azure-devops)
*   [Review pull requests](https://learn.microsoft.com/en-us/azure/devops/repos/git/review-pull-requests?view=azure-devops)
*   [Complete pull requests](https://learn.microsoft.com/en-us/azure/devops/repos/git/complete-pull-requests?view=azure-devops)
*   [Change the default branch](https://learn.microsoft.com/en-us/azure/devops/repos/git/change-default-branch?view=azure-devops)
*   [Copy changes with cherry-pick](https://learn.microsoft.com/en-us/azure/devops/repos/git/cherry-pick?view=azure-devops)
*   [Learn about pull requests and permissions](https://learn.microsoft.com/en-us/azure/devops/repos/git/about-pull-requests?view=azure-devops)
