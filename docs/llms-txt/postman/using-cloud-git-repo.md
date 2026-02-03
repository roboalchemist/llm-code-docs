# Connect to a cloud-hosted Git repository in the Postman API Builder

You can connect your API to a cloud-hosted Git repository to sync your API definition and collections between Postman and the repository. Postman supports connecting to [GitHub](https://github.com/), [Bitbucket](https://bitbucket.org/), [GitLab SaaS](https://about.gitlab.com/), or [Azure DevOps](https://azure.microsoft.com/en-us/products/devops/) repositories.

After connecting, you can push and pull changes between Postman and branches in the remote repository. When it’s time to release, you can publish an API version to make your changes available to consumers.

The steps below are for connecting to the cloud-hosted versions of GitHub, Bitbucket, GitLab SaaS, or Azure DevOps. If you need to connect to an on-premises repository, go to [Connect to an on-premises Git repository](/docs/design-apis/api-builder/versioning-an-api/using-on-prem-git-repo/).

## Using a cloud-hosted repository overview

You can connect an API in Postman to your cloud-hosted Git repository. This enables you to sync changes between the repository and Postman.

Keep in mind the following when connecting to a cloud-hosted Git repository:

* **The user account used for authentication requires full access to repositories.** To contribute to the API, each user must authenticate with their own account.
* **For GitHub connections, there's a limit of ten auth tokens per user per application imposed by GitHub.** If you create more than ten connections with the same user, tokens beyond this limit will be revoked in the order that they were created. Teams can use other Postman accounts to create more than ten integrations.
* **For Azure DevOps connections, make sure to enable third-party application access for your organization.** If you don’t enable third-party access, Postman won’t be able to connect to your repository. In Azure DevOps, go to your [organization settings](https://docs.microsoft.com/en-us/azure/devops/organizations/accounts/change-application-access-policies?view=azure-devops), select **Policies**, and turn on the toggle next to **Third-party application access via OAuth**.
* **You can connect one or more APIs to a remote repository.** You can keep your APIs separate in the repository using files or branches. Learn more about [connecting more than one API to the same repository](/docs/design-apis/api-builder/versioning-an-api/connecting-multiple-apis/).
* **You can create a new collection from a GitHub repository.** You can create a new collection from a GitHub repository by selecting the repository and clicking **Create Collection**.

## Connecting to a cloud-hosted repository

You can connect your API to a GitHub, Bitbucket, GitLab SaaS, or Azure DevOps repository hosted in the cloud.

1. Click **APIs** in the sidebar and select an API.
2. Under **Connect repository**, click **Connect** and select the type of repository you want to connect to (GitHub, Bitbucket, GitLab SaaS, or Azure DevOps).
3. A browser tab opens asking you to sign in to your repository. Follow the onscreen instructions. When you’re finished, close the browser tab and return to Postman.
4. On the **Connect your repository** page, select the **Organization** or **Workspace** and the **Repository** where the API will be stored. (For GitLab, enter the **Group** and **Project** for your API.)
5. Select the **Initial branch** for the API. Any changes you make in Postman are stored in the initial active branch. (You can switch to another branch to make it the active branch at any time.)
6. (Optional) Select an **API schema file** to add to your API. If you’re working on a [multi-file API definition](/docs/design-apis/api-builder/develop-apis/defining-an-api/#work-with-multi-file-api-definitions), make sure to select the [root definition file](/docs/design-apis/api-builder/develop-apis/defining-an-api/#about-root-files) in your repository. The root file is the base file that references other files in the API definition. If you leave this field blank, no definition files are added to your API. You can [manually add a definition file](/docs/design-apis/api-builder/develop-apis/defining-an-api/#add-an-api-definition-from-a-connected-repository) from your repository later.
7. Select a **Collection directory** where the collections linked to your API will be stored in the repository. If you leave this field blank, a `postman/collections` directory is created in the root of the repository.
8. Click **Connect Repository**.

The root definition file you selected is added to your API. For OpenAPI 2.0 and 3.0 APIs, Postman scans for any dependent files referenced in the root definition file and automatically adds them to your API. You can also [manually add more definition files](/docs/design-apis/api-builder/develop-apis/defining-an-api/#add-files-from-a-connected-repository) from your repository as needed.

Postman stores your authorized accounts so you can use them to connect to other repositories and services. Learn more about [managing connected accounts for remote repositories](#managing-connected-accounts-for-remote-repositories).

![Image 1: Connecting to a cloud-hosted repo](https://assets.postman.com/postman-docs/v10/api-builder-remote-repo-v10-18a.jpg)

## Managing connected accounts for remote repositories

After you connect an API to a remote repository, other editors of the API must authenticate to be able to contribute to the API. Postman will prompt editors to authenticate the next time they open the API.

Postman stores the accounts you’ve authorized with. After connecting to one repository, you can connect to other repositories that use the same Git provider without having to reauthenticate.

To manage services you’ve authorized with, click ![Image 2: Setting icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-setting-stroke.svg#icon) **Settings** in the header, click **Settings**, and select the **Connected accounts** tab. Learn more about [managing connected accounts](/docs/getting-started/installation/settings/#connected-accounts).

## Disconnecting a cloud-hosted repository

After you disconnect a remote repository, you can no longer sync changes between Postman and the repository.

1. Click **APIs** in the sidebar and select an API.
2. Click ![Image 3: Branch icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-branch-stroke.svg#icon) **Source Control** in the right sidebar.
3. In the **Source Control** pane, click ![Image 4: Options icon](https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon) and select **Disconnect repository**.
4. Enter the name of the API to confirm, then click **Disconnect**.

## Next steps

After you’ve connected a remote repository to your API, you can:

* Work with branches, push and pull changes, and resolve conflicts. Learn more about [managing changes using Git](/docs/design-apis/api-builder/versioning-an-api/managing-git-changes/).
* Publish an API version to a workspace or your team’s Private API Network. Learn more about [publishing an API version](/docs/design-apis/api-builder/versioning-an-api/api-versions/).

---

## Connect to a cloud-hosted Git repository in the Postman API Builder

You can connect your API to a cloud-hosted Git repository to sync your API definition and collections between Postman and the repository. Postman supports connecting to [GitHub](https://github.com/), [Bitbucket](https://bitbucket.org/), [GitLab SaaS](https://about.gitlab.com/), or [Azure DevOps](https://azure.microsoft.com/en-us/products/devops/) repositories.

After connecting, you can push and pull changes between Postman and branches in the remote repository. When it’s time to release, you can publish an API version to make your changes available to consumers.

The steps below are for connecting to the cloud-hosted versions of GitHub, Bitbucket, GitLab SaaS, or Azure DevOps. If you need to connect to an on-premises repository, go to [Connect to an on-premises Git repository](/docs/design-apis/api-builder/versioning-an-api/using-on-prem-git-repo/).

## Using a cloud-hosted repository overview

You can connect an API in Postman to your cloud-hosted Git repository. This enables you to sync changes between the repository and Postman.

Keep in mind the following when connecting to a cloud-hosted Git repository:

* **The user account used for authentication requires full access to repositories.** To contribute to the API, each user must authenticate with their own account.
* **For GitHub connections, there's a limit of ten auth tokens per user per application imposed by GitHub.** If you create more than ten connections with the same user, tokens beyond this limit will be revoked in the order that they were created. Teams can use other Postman accounts to create more than ten integrations.
* **For Azure DevOps connections, make sure to enable third-party application access for your organization.** If you don’t enable third-party access, Postman won’t be able to connect to your repository. In Azure DevOps, go to your [organization settings](https://docs.microsoft.com/en-us/azure/devops/organizations/accounts/change-application-access-policies?view=azure-devops), select **Policies**, and turn on the toggle next to **Third-party application access via OAuth**.
* **You can connect one or more APIs to a remote repository.** You can keep your APIs separate in the repository using files or branches. Learn more about [connecting more than one API to the same repository](/docs/design-apis/api-builder/versioning-an-api/connecting-multiple-apis/).
* **You can create a new collection from a GitHub repository.** You can create a new collection from a GitHub repository by selecting the repository and clicking **Create Collection**.

## Connecting to a cloud-hosted repository

You can connect your API to a GitHub, Bitbucket, GitLab SaaS, or Azure DevOps repository hosted in the cloud.

1. Click **APIs** in the sidebar and select an API.
2. Under **Connect repository**, click **Connect** and select the type of repository you want to connect to (GitHub, Bitbucket, GitLab SaaS, or Azure DevOps).
3. A browser tab opens asking you to sign in to your repository. Follow the onscreen instructions. When you’re finished, close the browser tab and return to Postman.
4. On the **Connect your repository** page, select the **Organization** or **Workspace** and the **Repository** where the API will be stored. (For GitLab, enter the **Group** and **Project** for your API.)
5. Select the **Initial branch** for the API. Any changes you make in Postman are stored in the initial active branch. (You can switch to another branch to make it the active branch at any time.)
6. (Optional) Select an **API schema file** to add to your API. If you’re working on a [multi-file API definition](/docs/design-apis/api-builder/develop-apis/defining-an-api/#work-with-multi-file-api-definitions), make sure to select the [root definition file](/docs/design-apis/api-builder/develop-apis/defining-an-api/#about-root-files) in your repository. The root file is the base file that references other files in the API definition. If you leave this field blank, no definition files are added to your API. You can [manually add a definition file](/docs/design-apis/api-builder/develop-apis/defining-an-api/#add-an-api-definition-from-a-connected-repository) from your repository later.
7. Select a **Collection directory** where the collections linked to your API will be stored in the repository. If you leave this field blank, a `postman/collections` directory is created in the root of the repository.
8. Click **Connect Repository**.

The root definition file you selected is added to your API. For OpenAPI 2.0 and 3.0 APIs, Postman scans for any dependent files referenced in the root definition file and automatically adds them to your API. You can also [manually add more definition files](/docs/design-apis/api-builder/develop-apis/defining-an-api/#add-files-from-a-connected-repository) from your repository as needed.

Postman stores your authorized accounts so you can use them to connect to other repositories and services. Learn more about [managing connected accounts for remote repositories](#managing-connected-accounts-for-remote-repositories).

![Image 5: Connecting to a cloud-hosted repo](https://assets.postman.com/postman-docs/v10/api-builder-remote-repo-v10-18a.jpg)

## Managing connected accounts for remote repositories

After you connect an API to a remote repository, other editors of the API must authenticate to be able to contribute to the API. Postman will prompt editors to authenticate the next time they open the API.

Postman stores the accounts you’ve authorized with. After connecting to one repository, you can connect to other repositories that use the same Git provider without having to reauthenticate.

To manage services you’ve authorized with, click ![Image 6: Setting icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-setting-stroke.svg#icon) **Settings** in the header, click **Settings**, and select the **Connected accounts** tab. Learn more about [managing connected accounts](/docs/getting-started/installation/settings/#connected-accounts).

## Disconnecting a cloud-hosted repository

After you disconnect a remote repository, you can no longer sync changes between Postman and the repository.

1. Click **APIs** in the sidebar and select an API.
2. Click ![Image 7: Branch icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-branch-stroke.svg#icon) **Source Control** in the right sidebar.
3. In the **Source Control** pane, click ![Image 8: Options icon](https://assets.postman.com/postman-docs/aether-icons/action-options-stroke.svg#icon) and select **Disconnect repository**.
4. Enter the name of the API to confirm, then click **Disconnect**.

## Next steps

After you’ve connected a remote repository to your API, you can:

* Work with branches, push and pull changes, and resolve conflicts. Learn more about [managing changes using Git](/docs/design-apis/api-builder/versioning-an-api/managing-git-changes/).
* Publish an API version to a workspace or your team’s Private API Network. Learn more about [publishing an API version](/docs/design-apis/api-builder/versioning-an-api/api-versions/).