# Source: https://learn.microsoft.com/en-us/azure/devops/artifacts/feeds/feed-permissions?view=azure-devops

Title: Manage permissions - Azure Artifacts

URL Source: https://learn.microsoft.com/en-us/azure/devops/artifacts/feeds/feed-permissions?view=azure-devops

Markdown Content:
**Azure DevOps Services | Azure DevOps Server | Azure DevOps Server 2022**

Azure Artifacts enables developers to efficiently manage dependencies by hosting various types of packages in a single feed. With flexible permission settings, you can fine-tune access to your packages, control who can create or administer feeds, and manage how packages are accessed from Azure Pipelines.

With Azure Artifacts settings, you can control who can create and administrer feeds.

1.   Sign in to your Azure DevOps organization, and navigate to your project.

2.   Select **Artifacts**, then select your feed from the dropdown menu.

3.   Select the **Azure Artifacts settings** icon on the right.

4.   Select **Who can create feeds** and **Who can administer feeds**, then select **Save** when you're done.

![Image 1: Screenshot showing how to set up Azure Artifacts settings.](https://learn.microsoft.com/en-us/azure/devops/artifacts/feeds/media/artifact-feed-settings.png?view=azure-devops)

From the Azure Artifacts feed settings, you can manage various aspects of your feed, such as enabling package sharing, configuring retention policies, adding new users or groups, managing view permissions, and setting up or modifying upstream sources. Here's how to add a new user or group to your feed:

1.   Sign in to your Azure DevOps organization, then navigate to your project.

2.   Select **Artifacts**, then select your feed from the dropdown menu.

3.   Select the gear icon on the right to navigate to your **Feed Settings**.

4.   Select **Permissions**, then select **Add users/groups**.

![Image 2: A screenshot displaying how to access feed permissions.](https://learn.microsoft.com/en-us/azure/devops/artifacts/feeds/media/feed-permissions.png?view=azure-devops)

5.   Add the new user(s) or group(s), and assign the appropriate **Role**:

    1.   **Feed Owner**: Can delete packages, allow external package versions, edit feed settings, and manage upstream sources, in addition to contributor permissions.
    2.   **Feed Publisher (Contributor)**: Can publish, promote, or deprecate packages along with collaborator permissions.
    3.   **Feed and Upstream Reader (Collaborator)**: Can save packages from upstream source in addition to reader permissions.
    4.   **Feed Reader**: Can view and download packages from the feed.

6.   Select **Save** when you're done.

Note

By default, the _Project Collection Build Service_ (organization-scoped) and the project-level _Build Service_ (project-scoped) are assigned the **Feed and Upstream Reader (Collaborator)** role.

Note

By default, the _Project Collection Build Service_ is automatically assigned the **Feed and Upstream Reader (Collaborator)** role for newly created collection-scoped feeds.

Azure Artifacts provides a flexible permission model to manage access within feeds. Each role comes with specific privileges that determine what actions a user or group can perform. The table below outlines the key permissions associated with each role:

| Permission | Feed Reader | Feed and Upstream Reader (Collaborator) | Feed Publisher (Contributor) | Feed Owner |
| --- | --- | --- | --- | --- |
| List packages in the feed | ✓ | ✓ | ✓ | ✓ |
| Download/install/restore packages | ✓ | ✓ | ✓ | ✓ |
| Save packages from upstream sources |  | ✓ | ✓ | ✓ |
| Publish packages |  |  | ✓ | ✓ |
| Promote packages to a view |  |  | ✓ | ✓ |
| Deprecate/unlist/yank packages |  |  | ✓ | ✓ |
| Delete/unpublish packages |  |  |  | ✓ |
| Add/remove upstream sources |  |  |  | ✓ |
| Allow external package versions |  |  |  | ✓ |
| Edit feed settings |  |  |  | ✓ |
| Delete a feed |  |  |  | ✓ |

Note

**Project Collection Administrators** and **Azure Artifacts Administrators** are automatically granted the **Feed Owner** role for all feeds in the project.

Feed views in Azure Artifacts enable users to share specific packages while keeping others private. A common use case is sharing a package version that has been tested and validated, while keeping packages still under development restricted.

By default, each feed includes three views: _@Local_, _@Prerelease_, and _@Release_. The latter two are suggested views that can be renamed or deleted as needed. The @Local view is the default and includes all packages published directly to the feed, as well as packages saved from upstream sources.

Important

Users who have access to a specific view are able to access and download packages from the feed through that view even if they don't have direct access to that feed. If you want to completely hide your packages, you must restrict access to both the feed and its views.

1.   Sign in to your Azure DevOps organization, then navigate to your project.

2.   Select **Artifacts**, then select your feed from the dropdown menu.

3.   Select the gear icon to navigate to your **Feed Settings**.

4.   Select **Views**, select the ellipsis button next to your view, then select **Edit** to modify its permission.

5.   To restrict access to your view, change the visibility setting to **specific people**.

Important

Views inherit permissions from the parent feed. If you set a view's visibility to _Specific people_ without specifying any users or groups, the view's permissions will default back to the permissions of the parent feed. 
6.   Select **Save** when you're done. The access permissions column will update to reflect your changes.

![Image 3: A screenshot showing the permissions settings for the @Prerelease view in Azure Artifacts.](https://learn.microsoft.com/en-us/azure/devops/artifacts/feeds/media/edit-views.png?view=azure-devops)

Note

To add a feed from a different organization as an upstream source, the target feed owner must share the target view with **All feeds and people in organizations associated with my Microsoft Entra tenant**. This can be done by navigating to **Feed Settings**>**Views**, selecting the ellipsis next to the specified view, selecting **Edit**, and adjusting the permissions.

To access your feed from your pipeline, the [corresponding build identity](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/access-tokens?view=azure-devops#scoped-build-identities) must have the necessary permissions. The project-level build identity is named `[Project name] Build Service ([Organization name])`, for example `FabrikamFiber Build Service (codesharing-demo)` while the organization-level build identity is named `Project Collection Build Service ([Organization name])`, for example `Project Collection Build Service (codesharing-demo)`. Here's how to add the build identity to your feed's permissions:

1.   Sign in to your Azure DevOps organization, then navigate to your project.

2.   Select **Artifacts**, then select your feed from the dropdown menu.

3.   Select the gear icon ![Image 4: gear icon](https://learn.microsoft.com/en-us/azure/devops/media/icons/gear-icon.png?view=azure-devops) to navigate to **Feed settings**.

4.   Select **Permissions**, then select **Add users/groups**. Add your build identity and assign it the **Feed and Upstream Reader (Collaborator)** role. If your pipeline needs to publish packages to the feed, make sure that both the _Project Collection Build Service_ and your _project's Build Service_ identities have the **Feed Publisher (Contributor)** role.

![Image 5: A screenshot displaying how to add a build identity to the feed permissions.](https://learn.microsoft.com/en-us/azure/devops/artifacts/feeds/media/feed-pipelines-permissions.png?view=azure-devops)

See the examples below to learn how to authenticate and publish packages to your feed with Azure Pipelines.

| Package Type | Article |
| --- | --- |
| NuGet | [Publish NuGet packages with Azure Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/artifacts/nuget?view=azure-devops) |
| Npm | [Publish npm packages with Azure Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/artifacts/npm?view=azure-devops) |
| Maven | [Publish Maven artifacts with Azure Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/artifacts/publish-maven-artifacts?view=azure-devops) |
| Python | [Publish Python packages with Azure Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/artifacts/pypi?view=azure-devops) |
| Cargo | [Publish Cargo packages with Azure Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/artifacts/cargo-pipelines?view=azure-devops) |
| Universal Packages | [Publish Universal Packages with Azure Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/artifacts/universal-packages?view=azure-devops) |

| Package Type | Article |
| --- | --- |
| NuGet | [Publish NuGet packages with Azure Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/artifacts/nuget?view=azure-devops) |
| Npm | [Publish npm packages with Azure Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/artifacts/npm?view=azure-devops) |
| Maven | [Publish Maven artifacts with Azure Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/artifacts/publish-maven-artifacts?view=azure-devops) |
| Python | [Publish Python packages with Azure Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/artifacts/pypi?view=azure-devops) |
| Cargo | [Publish Cargo packages with Azure Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/artifacts/cargo-pipelines?view=azure-devops) |

Note

If your pipeline uses the project-level build identity and needs to access a feed in a different project, you must configure that other project to grant the build identity at least the **Edit project-level information** permission.

*   [Monitor Artifacts storage consumption](https://learn.microsoft.com/en-us/azure/devops/artifacts/artifact-storage?view=azure-devops)

*   [Promote packages and manage feed views](https://learn.microsoft.com/en-us/azure/devops/artifacts/feeds/views?view=azure-devops)

*   [Set up upstream sources](https://learn.microsoft.com/en-us/azure/devops/artifacts/how-to/set-up-upstream-sources?view=azure-devops)
