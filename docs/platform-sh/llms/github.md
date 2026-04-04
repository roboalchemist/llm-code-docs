# Source: https://docs.upsun.com/integrations/source/github.md

# Integrate with GitHub


If you have code in a GitHub repository, you might want to connect it to a Upsun project.
This means you can keep your GitHub workflows
and treat the GitHub repository as the source of truth for your code.

Your Upsun project becomes a mirror of your GitHub repository.
This means you shouldn't push code directly to Upsun.
Any changes you push directly get overwritten by the integration when changes happen in the GitHub repository.

When you set up an integration with GitHub,
it automates the following processes for you:

- Creating a new environment when a branch is created or a pull request is opened.
- Rebuilding the environment when new code is pushed to GitHub.
- Deleting the environment when a pull request is merged.

## Before you begin

To manage source integrations, you need to be a [project admin](https://docs.upsun.com../../administration/users.md).

You also need a GitHub repository with working code.

## 1. Generate a token

To integrate your Upsun project with an existing GitHub repository,
you need to [generate a new token](https://github.com/settings/tokens/new).
You can generate a classic personal access token,
or a [fine-grained personal access token](https://github.blog/changelog/2022-10-18-introducing-fine-grained-personal-access-tokens/)
for even greater control over the permissions you grant.

For the integration to work,
your GitHub user needs to have permission to push code to the repository.

When you set up or update an integration, it also needs permission to manage its webhooks.
This means your user needs to be a repository admin to create the integration.
You can remove this permission after setup.

Make sure you give your token a description.

If you're generating a classic personal access token,
ensure the token has the appropriate scopes based on what you want to do:

| Scope                 | Purpose                                                                |
| --------------------- | ---------------------------------------------------------------------- |
| `admin:repo_hook`     | To create webhooks for events in repositories. Always needed.          |
| `public_repo`         | To integrate with public repositories.                                 |
| `repo`                | To integrate with your private repositories.                           |
| `repo` and `read:org` | To integrate with private repositories in organizations you belong to. |

If you're generating a fine-grained personal access token,
ensure the token has the right [repository permissions](https://docs.github.com/en/rest/overview/permissions-required-for-fine-grained-personal-access-tokens?apiVersion=2022-11-28)
for the integration to work:

| Permission        | Access level    |
| ------------------| ----------------|
| `Commit statuses` | Read and write  |
| `Contents`        | Read and write  |
| `Metadata`        | Read-only       |
| `Pull request`    | Read and write  |
| `Webhooks`        | Read and write  |

After you've set the needed scopes or permissions,
generate and copy your token.

## 2. Enable the integration

To enable the integration, use either the [CLI](https://docs.upsun.com/administration/cli.md) or the [Console](https://docs.upsun.com/administration/web.md).

 - ``PROJECT_ID`` is the ID of your Upsun project.
 - ``OWNER/REPOSITORY`` is the name of your repository in GitHub.
 - ``GITHUB_ACCESS_TOKEN`` is the [token you generated](#1-generate-a-token).
 - ``GITHUB_URL`` is the base URL for your GitHub server if you self-host.
If you use the public ``https://github.com``, omit the ``--base-url`` flag when running the command.

For example, if your repository is located at ``https://github.com/platformsh/platformsh-docs``,
the command is similar to the following:

```bash {}
upsun integration:add \
  --project abcdefgh1234567 \
  --type github \
  --repository platformsh/platformsh-docs \
  --token abc123
```

 - Select the project where you want to enable the integration.
 - Click **Settings Settings**.
 - Under **Project settings**, click **Integrations**.
 - Click **+ Add integration**.
 - Under **GitHub**, click **+ Add**.
 - Add the [token you generated](#1-generate-a-token).
 - Optional: If your GitHub project isn’t hosted at ``github.com``, enter your GitHub custom domain.
 - Click **Continue**.
 - Choose the repository to use for the project.
 - Check that the other options match what you want.
 - Click **Add integration**.

In both the CLI and Console, you can choose from the following options:

| CLI flag         | Default | Description                                                               |
| ---------------- | ------- | ------------------------------------------------------------------------- |
| `fetch-branches` | `true`  | Whether to mirror and update branches on Upsun and create inactive environments from them. When enabled, merging on an Upsun environment isn't possible. That is, merging environments must be done on the source repository rather than on the Upsun project. See note below for details related to this flag and synchronizing code from a parent environment. |
| `prune-branches` | `true`  | Whether to delete branches from Upsun that don’t exist in the GitHub repository. When enabled, branching (creating environments) must be done on the source repository rather than on the Upsun project. Branches created on Upsun that are not on the source repository will not persist and will be quickly pruned. Automatically disabled when fetching branches is disabled. |
| `build-pull-requests` | `true` | Whether to track all pull requests and create active environments from them, which builds the pull request. |
| `build-draft-pull-requests` | `true` | Whether to also track and build draft pull requests. Automatically disabled when pull requests aren’t built. |
| `pull-requests-clone-parent-data` | `true` | 	Whether to clone data from the parent environment when creating a pull request environment. |
| `build-pull-requests-post-merge`| `false` | Whether to build what would be the result of merging each pull request. Turning it on forces rebuilds any time something is merged to the target branch. |
| `resources-init` | `false` | To [specify a resource initialization strategy](https://docs.upsun.com/manage-resources/resource-init.md#first-deployment) for new containers. Once set, the strategy applies to **all** the deployments you launch through your source integration. See more information on [available resource initialization strategies](https://docs.upsun.com/manage-resources/resource-init.md#specify-a-resource-initialization-strategy). |

To [keep your repository clean](https://docs.upsun.com/learn/bestpractices/clean-repository.md) and avoid performance issues, make sure you enable both the `fetch-branches` and `prune-branches` options.

## 3. Validate the integration

Verify that your integration is functioning properly [using the CLI](https://docs.upsun.com../overview.md#validate-integrations):

```bash
upsun integration:validate
```

### Add the webhook manually

If the integration was added with the correct permissions, the necessary webhook is added automatically.
If you see a message that the webhook wasn't added, add one manually.

To configure a webhook on a GitHub repository,
you need to have Admin [user permissions](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/repository-roles-for-an-organization#permissions-for-each-role).

1. Get the webhook URL by running this command: `upsun
 integration:get --property hook_url`.
1. Copy the returned URL.

1. In your GitHub repository, click **Settings** > **Webhooks** > **Add webhook**.
1. In the **Payload URL** field, paste the URL you copied.
1. For the content type, select **application/json**.
1. Select **Send me everything**.
1. Click **Add webhook**.

You can now start pushing code, creating new branches,
and opening pull requests
directly in your GitHub repository.
Your Upsun environments are automatically created and updated.

## Environment parent and status

When a **branch** is created in GitHub,
an environment is created in Upsun with the default branch as its parent.
It starts as an [inactive environment](https://docs.upsun.com/glossary.md#inactive-environment) with no data or services.

When a **pull request** is opened in GitHub,
an environment is created in Upsun with the pull request's target branch as its parent.
It starts as an [active environment](https://docs.upsun.com/glossary.md#active-environment) with a copy of its parent's data.

## Source of truth

When you add an integration, your GitHub repository is considered to be the source of truth for the project.
Your Upsun project is only a mirror of that repository and you can only push commits to GitHub.

To clone your code, follow these steps:

 - In the Console, open the project you want to clone.
 - Click **Code**.
 - Click **Git**.
 - Run the command you find using Git.

When you do this, you're cloning from your integrated GitHub repository,
if you have the [appropriate access to do so](https://docs.upsun.com/integrations/source/troubleshoot.md).

### Sync, fetch, and prune

An integration from GitHub to Upsun establishes that:

- GitHub is the source of truth, where Git operations occur
- Upsun is a mirror of that repository - provisioning infrastructure according to configuration, and orchestrating environments according to the branch structure of the GitHub repository

Actions that take place on Upsun don't affect commits on GitHub.
Because of this, the GitHub integration enables both `fetch-branches` (track branches on GitHub) and `prune-branches` (delete branches that don't exist on GitHub) by default.
You can change these settings but it is recommend to keep them.

When enabled by default, you are limited by design as to what actions can be performed within the context of a Upsun project with a GitHub integration:

| Action         | Observation         | Recommendation |
| :---------------- | :---------------- | :------- |
| Branch from parent | Running [`environment:branch`](https://docs.upsun.com/administration/cli/reference#environmentbranch) with the CLI, or selecting **Branch** in Console produces a new child environment, but it's deleted shortly after automatically. | Contribute to the GitHub repository itself by creating a branch and pull request. When the PR has been opened, a new environment will be provisioned for it.  |
| Merge in parent | Running [`environment:merge`](https://docs.upsun.com/administration/cli/reference#environmentmerge) with the CLI fails locally, and the **Merge** option in Console is not clickable. | Review and merge pull requests and/or branches on the GitHub repository. |
| Merge into child (sync code) | Running [`environment:synchronize`](https://docs.upsun.com/administration/cli/reference#environmentsynchronize) with the CLI fails locally, and the **Sync** option in Console won't allow me to include `code` in that sync. | Perform the merge locally from a matching branch on GitHub. For example, clone the most recent parent (`git pull origin parent-branch`), switch to the pull request branch (`git checkout ga-staging`), and then merge the parent into the current branch (`git merge main`). |

## Pull request URLs

When a pull request is deployed, the integration reports the primary URL for the deployed environment.
So you get a link to the deployed environment right in the pull request.

If you have multiple routes,
ensure the correct one is reported by [specifying the primary route](https://docs.upsun.com/define-routes.md#route-configuration-reference).


