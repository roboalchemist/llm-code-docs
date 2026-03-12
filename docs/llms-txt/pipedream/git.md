# Source: https://pipedream.com/docs/workflows/git.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# GitHub Sync

export const PD_EGRESS_IP_RANGE = '44.223.89.56/29';

When GitHub Syncing is enabled on your project, Pipedream will serialize your workflows and synchronize changes to a GitHub repo.

Capabilities include:

* Bi-directional GitHub sync (push and pull changes)
* Edit in development branches
* Track commit and merge history
* Link users to commits
* Merge from Pipedream or create PRs and merge from GitHub
* Edit in Pipedream or use a local editor and synchronize via GitHub (e.g., edit code, find and replace across multiple steps or workflows)
* Organize workflows into projects with support for nested folders

## Getting Started

### Create a new project and enable GitHub Sync

A project may contain one or more workflows and may be further organized using nested folders. Each project may be synchronized to a single GitHub repo.

* Go to `https://pipedream.com/projects`

* Create a new project

* Enter a project name and check the box to **Configure GitHub Sync**

  * To use **OAuth**

    * Select a connected account, GitHub scope and repo name
    * Pipedream will automatically create a new, empty repo in GitHub
    * <Frame>
        <img src="https://mintcdn.com/pipedream/grEzwYhEB2vZSwGw/images/7839227e-w860.png?fit=max&auto=format&n=grEzwYhEB2vZSwGw&q=85&s=ec631d2c0d1eeb6f75e850e49fe05713" width="642" height="574" data-path="images/7839227e-w860.png" />
      </Frame>

  * To use **Deploy Keys**

    * Create a new repo in GitHub
    * Follow the instructions to configure the deploy key
    * Test your setup and create a new project
    * <Frame>
        <img src="https://mintcdn.com/pipedream/anb6FA0wpd8jtdUB/images/57332d25-w860.png?fit=max&auto=format&n=anb6FA0wpd8jtdUB&q=85&s=26dc0f06eaf7e4ad5b94b311f759e4b8" width="638" height="860" data-path="images/57332d25-w860.png" />
      </Frame>

### Create a branch to edit a project

<Note>
  Branches are required to make changes

  All changes to resources in a project must be made in a development branch.

  Examples of changes include creating, editing, deleting, enabling, disabling and renaming workflows. This also includes changing workflow settings like concurrency, VPC assignment and auto-retries.
</Note>

To edit a git-backed project you must create a development branch by clicking **Edit > Create Branch**

<Frame>
  <img src="https://mintcdn.com/pipedream/grEzwYhEB2vZSwGw/images/8cde2d1c-w2000.png?fit=max&auto=format&n=grEzwYhEB2vZSwGw&q=85&s=40eee3f58a3378970e06b9f26aba89c3" width="2048" height="1281" data-path="images/8cde2d1c-w2000.png" />
</Frame>

Next, name the branch and click **Create**:

<Frame>
  <img src="https://mintcdn.com/pipedream/h8oodpUDiyR1Ssvt/images/4b629354-w2000.png?fit=max&auto=format&n=h8oodpUDiyR1Ssvt&q=85&s=c24b93c08d14088a6ea834d15b564871" width="2048" height="1275" data-path="images/4b629354-w2000.png" />
</Frame>

To exit development mode without merging to production, click **Exit Development Mode**:

<Frame>
  <img src="https://mintcdn.com/pipedream/anb6FA0wpd8jtdUB/images/73383cab-w2000.png?fit=max&auto=format&n=anb6FA0wpd8jtdUB&q=85&s=d9537e732f2374970f2ab3de395c4a58" width="2048" height="749" data-path="images/73383cab-w2000.png" />
</Frame>

Your changes will be saved to the branch, if you choose to revisit them later.

### Merge changes to production

Once you’ve committed your changes, you can deploy your changes by merging them into the `production` branch through the Pipedream UI or GitHub.

When you merge a Git-backed project to production, all modified resources in the project will be deployed. Multiple workflows may be deployed, modified, or deleted in production through a single merge action.

#### Merge via the Pipedream UI

To merge changes to production, click on **Merge to production:**

<Frame>
  <img src="https://mintcdn.com/pipedream/nKh6d_6A4aXFb6xD/images/f7005e9a-w2000.png?fit=max&auto=format&n=nKh6d_6A4aXFb6xD&q=85&s=1326654b2e73b8dce9753b89b3746d11" width="2048" height="1284" data-path="images/f7005e9a-w2000.png" />
</Frame>

Pipedream will present a diff between the development branch and the `production`. Validate your changes and click **Merge to production** to complete the merge:

<Frame>
  <img src="https://mintcdn.com/pipedream/NF77kliJSewMqg65/images/2061ff03-w2000.png?fit=max&auto=format&n=NF77kliJSewMqg65&q=85&s=060412a3c2afe6ab2b10609edde84620" width="2048" height="1282" data-path="images/2061ff03-w2000.png" />
</Frame>

#### Create a Pull Request in GitHub

To create a pull request in GitHub, either choose Open GitHub pull request from the git-actions menu in Pipedream or in GitHub:

<Frame>
  <img src="https://mintcdn.com/pipedream/h8oodpUDiyR1Ssvt/images/2ca2feab-w2000.png?fit=max&auto=format&n=h8oodpUDiyR1Ssvt&q=85&s=357fb51eb61c1f22b1743be8ea2015b9" width="2048" height="568" data-path="images/2ca2feab-w2000.png" />
</Frame>

You can also review and merge changes directly from GitHub using the standard pull request process.

<Warning>
  Pull request reviews cannot be required

  PR reviews cannot be required. That feature is on the roadmap for the Business tier.
</Warning>

### Commit changes

To commit changes without merging to production, select **Commit Changes** from the Git Actions menu:

<Frame>
  <img src="https://mintcdn.com/pipedream/xnRKrRxEtt3vxd6I/images/dc0aadde-w2000.png?fit=max&auto=format&n=xnRKrRxEtt3vxd6I&q=85&s=1d19182c6f238f14f5bf256a32c9a4ef" width="2048" height="629" data-path="images/dc0aadde-w2000.png" />
</Frame>

You can review the diff and enter a commit message:

<Frame>
  <img src="https://mintcdn.com/pipedream/Acz4Z1ch6TM7-aI8/images/a7b35c13-w2000.png?fit=max&auto=format&n=Acz4Z1ch6TM7-aI8&q=85&s=aba5bd64e21e96aa259474fdb5f4bfbe" width="2048" height="1281" data-path="images/a7b35c13-w2000.png" />
</Frame>

### Pull changes and resolve conflicts

If remote changes are detected, you’ll be prompted to pull the changes:

<Frame>
  <img src="https://mintcdn.com/pipedream/xnRKrRxEtt3vxd6I/images/df924b2e-w2000.png?fit=max&auto=format&n=xnRKrRxEtt3vxd6I&q=85&s=3d819d5446656abfd7a03240ddb8969e" width="2048" height="345" data-path="images/df924b2e-w2000.png" />
</Frame>

Pipedream will attempt to automatically merge changes. If there are conflicts, you will be prompted to manually resolve it:

<Frame>
  <img src="https://mintcdn.com/pipedream/NF77kliJSewMqg65/images/2277af22-w2000.png?fit=max&auto=format&n=NF77kliJSewMqg65&q=85&s=d832729b7f9bfffd77f5d435abd7d9cc" width="2048" height="1278" data-path="images/2277af22-w2000.png" />
</Frame>

### Move existing workflows to projects

<Warning>
  Not available for v1 workflows

  Legacy (v1) workflows are not supported in projects.
</Warning>

First, select the workflow(s) you want to move from the [workflows listing page](https://pipedream.com/workflows) and click **Move** in the top action menu:

<Frame>
  <img src="https://mintcdn.com/pipedream/nKh6d_6A4aXFb6xD/images/edc801f1-w2000.png?fit=max&auto=format&n=nKh6d_6A4aXFb6xD&q=85&s=38688169ee65ea45c8e81c18e4fa1fa6" width="1347" height="217" data-path="images/edc801f1-w2000.png" />
</Frame>

Then, select the project to move the selected workflows to:

<Frame>
  <img src="https://mintcdn.com/pipedream/anb6FA0wpd8jtdUB/images/54e4232f-w2000.png?fit=max&auto=format&n=anb6FA0wpd8jtdUB&q=85&s=a3ccc2540ef305d8fd4ca8f4a7d0459c" width="1354" height="216" data-path="images/54e4232f-w2000.png" />
</Frame>

<Note>
  Undeployed changes are automatically assigned a development branch

  If any moved workflows have undeployed changes, those changes will staged in a branch prefixed with `undeployed-changes` (e.g., `undeployed-changes-27361`).
</Note>

### Use the changelog

The changelog tracks all git activity (for projects with GitHub sync enabled). If you encounter an error merging your project, go to the changelog and explore the log details to help you troubleshoot issues in your workflows:

<Frame>
  <img src="https://mintcdn.com/pipedream/xnRKrRxEtt3vxd6I/images/c8f82945-w2000.png?fit=max&auto=format&n=xnRKrRxEtt3vxd6I&q=85&s=68bc288e5f00f1112818d6bd5e45c2d9" width="2048" height="858" data-path="images/c8f82945-w2000.png" />
</Frame>

### Local development

Projects that use GitHub sync may be edited outside of Pipedream. You can edit and commit directly via GitHub’s UI or clone the repo locally and use your preferred editor (e.g., VSCode).

To test external edits in Pipedream:

1. Commit and push local changes to your development branch in GitHub
2. Open the project in Pipedream’s UI and load your development branch
3. Use the Git Actions menu to pull changes from GitHub

## Known Issues

Below are a list of known issues that do not currently have solutions, but are in progress:

* Project branches on Pipedream cannot be deleted.
* If a workflow uses an action that has been deprecated, merging to production will fail.
* Legacy (v1) workflows are not supported in projects.
* Self-hosted GitHub Server instances are not yet supported. [Please contact us for help](https://pipedream.com/support).
* Workflow attachments are not supported

## GitHub Enterprise Cloud

If your repository is hosted on an GitHub Enterprise account, you can allow Pipedream’s address range to sync your project changes.

[Follow the directions here](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization) and add the following IP range:

{PD_EGRESS_IP_RANGE}

<Warning>
  GitHub Sync is available on Business plan

  To use this public IP address and connect to GitHub Enterprise Cloud hosted repositories, you’ll need to have a Pipedream Business plan. [View our plans](https://pipedream.com/pricing).
</Warning>

## FAQ

### How are Pipedream workflows synchronized to GitHub?

Pipedream will serialize your project’s workflows and their configuration into a standard YAML format for storage in GitHub.

Then Pipedream will commit your changes to your connected GitHub account.

### Do you have a definition of this YAML?

Not yet, please stay tuned!

### Can I sync multiple workflows to a single GitHub repository?

Yes, *projects* are synced to a single GitHub repository which allows you to store multiple workflows into a single GitHub repository for easier organization and management.

### Can I use this feature to develop workflows locally?

Yes, you can use the GitHub Syncing feature to develop your workflows from YAML files checked into your Pipedream connected GitHub repository.

Then pushing changes to the `production` branch will trigger a deploy for your Pipedream workflows.

### Why am I seeing the error “could not resolve step\[index].uses: component-key\@version” when merging to production?

This error occurs when a workflow references a [private component](/components/contributing/#using-private-actions) without properly prefixing the component key with your workspace name in the `workflow.yaml` configuration file. Pipedream requires this prefix to correctly identify and resolve components specific to your workspace.

For example, if you modified a [registry action](/components/contributing/) and published it privately, the correct component key should be formatted as `@workspacename/component-key@version` (e.g., `@pipedream/github-update-issue@0.1.0`).

To resolve this error:

1. Clone your repository locally and create a development branch.
2. Locate the error in your `workflow.yaml` file where the component key is specified.
3. Add your workspace name prefix to the component key, ensuring it follows the format `@workspacename/component-key@version`.
4. Commit your changes and push them to your repository.
5. Open your project in the Pipedream UI and select your development branch.
6. Click on **Merge to Production** and verify the deployment success in the [Changelog](/workflows/git/#use-the-changelog).
7. If the issue persists, [reach out to Pipedream Support](https://pipedream.com/support) for further assistance.

### Why am I seeing an error about “private auth mismatch” when trying to merge a branch to production?

<Frame>
  <img src="https://mintcdn.com/pipedream/grEzwYhEB2vZSwGw/images/9527ea29-private_auth_mismatch_kzdd7e.png?fit=max&auto=format&n=grEzwYhEB2vZSwGw&q=85&s=8560e481bd54df0a7e93236eed5b99df" width="1788" height="780" data-path="images/9527ea29-private_auth_mismatch_kzdd7e.png" />
</Frame>

This error occurs when **both** of the below conditions are met:

1. The referenced workflow is using a connected account that’s not shared with the entire workspace
2. The change was merged from outside the Pipedream UI (via github.com or locally)

Since Pipedream can’t verify the person who merged that change should have access to use the connected account in a workflow in this case, we block these deploys.

To resolve this error:

1. Make sure all the connected accounts in the project’s workflows are [accessible to the entire workspace](/apps/connected-accounts/#access-control)
2. Re-trigger a sync with Pipedream by making a nominal change to the workflow **from outside the Pipedream UI** (via github.com or locally), then merge that change to production

### Can I sync an existing GitHub repository with workflows to a new Pipedream Project?

No, at this time it’s not possible because of how resources are connected during the bootstrapping process from the workflow YAML specification. However, this is on our roadmap, [please subscribe to this issue](https://github.com/PipedreamHQ/pipedream/issues/9255) for the latest details.

### Migrating GitHub Repositories

You can migrate Pipedream project’s GitHub repository to a new repository, while preserving history. You may want to do this when migrating a repository from a personal GitHub account to an organization account, without affecting the workflows within the Pipedream project.

#### Assumptions

* **Current GitHub repository**: `previous_github_repo`
* **New GitHub repository**: `new_github_repo`
* Basic familiarity with git and GitHub
* Access to a local terminal (e.g., Bash, Zsh, PowerShell)
* Necessary permissions to modify both the Pipedream project and associated GitHub repositories

#### Steps

1. **Access Project Settings in Pipedream:**

   * Navigate to your Pipedream project.
   * Use the dropdown menu on the “Edit” button in the top right corner to access `previous_github_repo` in GitHub.

   <Frame>
     <img src="https://mintcdn.com/pipedream/xnRKrRxEtt3vxd6I/images/ca572f33-Screenshot_2024-05-03_at_12.12.36_PM_sxkrng.png?fit=max&auto=format&n=xnRKrRxEtt3vxd6I&q=85&s=63b2b08e0cbacc97a863bb44eaccd7cc" width="466" height="340" data-path="images/ca572f33-Screenshot_2024-05-03_at_12.12.36_PM_sxkrng.png" />
   </Frame>

2. **Clone the Current Repository Locally:**

   ```php  theme={null}
   git clone previous_github_repo_clone_url
   ```

3. Reset GitHub Sync in Pipedream:

   * In Pipedream, go to your project settings.
   * Click on “Reset GitHub Connection”.

   <Frame>
     <img src="https://mintcdn.com/pipedream/xnRKrRxEtt3vxd6I/images/dbeee2f8-Screenshot_2024-05-03_at_12.15.03_PM_icdppb.png?fit=max&auto=format&n=xnRKrRxEtt3vxd6I&q=85&s=10ecc48f9f0cfea9f9d3e9b85ee31489" width="1164" height="442" data-path="images/dbeee2f8-Screenshot_2024-05-03_at_12.15.03_PM_icdppb.png" />
   </Frame>

4. Set Up New repository connection:

   * Configure the project’s GitHub repository to use `new_github_repo`.

5. Clone the new repository locally:

   ```bash  theme={null}
   git clone new_github_repo_clone_url
   cd new_github_repo
   ```

6. Link to the old repository:

   ```python  theme={null}
   git remote add old_github_repo previous_github_repo_clone_url
   git fetch --all
   ```

7. Prepare for migration:

   * Create and switch to a new branch for migration:

     ```
     git checkout -b migration
     ```

   * Merge the main branch of `old_github_repo` into migration, allowing for unrelated histories:

     ```swift  theme={null}
     git merge --allow-unrelated-histories old_github_repo/production
     # Resolve any conflicts, such as in README.md
     git commit
     ```

8. Finalize the migration:

   * Optionally push the `migration` branch to the remote:

     ```python  theme={null}
     git push --set-upstream origin migration
     ```

   * Switch to the `production` branch and merge:

     ```
     git checkout production
     git merge --no-ff migration
     git push
     ```

9. Cleanup:

   * Remove the connection to the old repository:

     ```csharp  theme={null}
        git remote remove old_github_repo
     ```

   * Optionally, you may now safely delete `previous_github_repo` from GitHub.

### How does the `production` branch work?

Anything merged to the `production` branch will be deployed to your production workflows on Pipedream.

From a design perspective, we want to let you manage any branching strategy on your end, since you may be making commits to the repo outside of Pipedream. Once we support managing Pipedream workflows in a monorepo, where you may have other changes, we wanted to use a branch that didn’t conflict with a conventional main branch (like `main` or `master`).

In the future, we also plan to support you changing the default branch name.

Built with [Mintlify](https://mintlify.com).
