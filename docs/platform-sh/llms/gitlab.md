# Source: https://docs.upsun.com/integrations/source/gitlab.md

# Integrate with GitLab


If you have code in a GitLab repository, you might want to connect it to a Upsun project.
This means you can keep your GitLab workflows
and treat the GitLab repository as the source of truth for your code.

Your Upsun project becomes a mirror of your GitLab repository.
This means you shouldn't push code directly to Upsun.
Any changes you push directly get overwritten by the integration when changes happen in the GitLab repository.

When you set up an integration with GitLab,
it automates the following processes for you:

- Creating a new environment when a branch is created or a merge request is opened.
- Rebuilding the environment when new code is pushed to GitLab.
- Deleting the environment when a merge request is merged.

## Before you begin

To manage source integrations, you need to be a [project admin](https://docs.upsun.com../../administration/users.md).

You also need a GitLab repository with working code.

**Note**: 

If your GitLab instance is not accessible from the public internet, configure a [GitLab CI/CD pipeline](#optional-use-a-gitlab-cicd-pipeline) that pushes code to Upsun and manages environments via the Upsun API. This method provides full deployment control while keeping your GitLab instance isolated.

## 1. Generate a token

To integrate your Upsun project with an existing GitLab repository,
generate a [project access token](https://docs.gitlab.com/ee/user/project/settings/project_access_tokens.md#create-a-project-access-token).
Ensure the token has the following scopes:

- `api` to access your API
- `read_repository` to read the repository

For the integration to work, your GitLab user needs push access to the repository and to configure a webhook on a GitLab repository, you need to have Maintainer or Owner user permissions.

Copy the token.

**Note**: 

To create a project access token, you need to have a [sufficient GitLab license tier](https://docs.gitlab.com/ee/user/project/settings/project_access_tokens.md).
If you don’t see **Access Tokens** under **Settings**, upgrade your GitLab tier.
Alternatively, you can create a [personal access token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.md),
but that’s attached to a specific user rather than the project as a whole
and grants more permissions.

## 2. Enable the integration

To enable the integration, use either the [CLI](https://docs.upsun.com/administration/cli.md) or the [Console](https://docs.upsun.com/administration/web.md).

 - ``PROJECT_ID`` is the ID of your Upsun project.
 - ``PROJECT/SUBPROJECT`` is the name of your repository in GitLab.
 - ``GITLAB_ACCESS_TOKEN`` is the [token you generated](#1-generate-a-token).
 - ``GITLAB_URL`` is the base URL for your GitLab server if you self-host.
If you use the public ``https://gitlab.com``, omit the ``--base-url`` flag when running the command.

For example, if your repository is located at ``https://gitlab.com/platformsh/platformsh-docs``,
the command is similar to the following:

```bash {}
upsun integration:add \
  --project abcdefgh1234567 \
  --type gitlab \
  --server-project platformsh/platformsh-docs \
  --token abc123
```

 - Select the project where you want to enable the integration.
 - Click **Settings Settings**.
 - Under **Project settings**, click **Integrations**.
 - Click **+ Add integration**.
 - Under **GitLab**, click **+ Add**.
 - Add the [token you generated](#1-generate-a-token).
 - Optional: If your GitLab project isn’t hosted at ``gitlab.com``, enter your GitLab custom domain.
 - Click **Continue**.
 - Choose the repository to use for the project.
 - Check that the other options match what you want.
 - Click **Add integration**.

In both the CLI and Console, you can choose from the following options:

| CLI flag         | Default | Description                                                               |
| ---------------- | ------- | ------------------------------------------------------------------------- |
| `fetch-branches` | `true`  | Whether to mirror and update branches on Upsun and create inactive environments from them. When enabled, merging on an Upsun environment isn't possible. That is, merging environments must be done on the source repository rather than on the Upsun project. See note below for details related to this flag and synchronizing code from a parent environment. |
| `prune-branches` | `true`  | Whether to delete branches from Upsun that don’t exist in the GitLab repository. When enabled, branching (creating environments) must be done on the source repository rather than on the Upsun project. Branches created on Upsun that are not on the source repository will not persist and will be quickly pruned. Automatically disabled when fetching branches is disabled. |
| `build-merge-requests` | `true` | Whether to track all merge requests and create active environments from them, which builds the merge request. |
| `build-wip-merge-requests` | `true` | Whether to also track and build draft merge requests. Automatically disabled when merge requests aren’t built. |
| `merge-requests-clone-parent-data` | `true` | Whether to clone data from the parent environment when creating a merge request environment. |
| `resources-init` | `false` | To [specify a resource initialization strategy](https://docs.upsun.com/manage-resources/resource-init.md#first-deployment) for new containers. Once set, the strategy applies to **all** the deployments you launch through your source integration. See more information on [available resource initialization strategies](https://docs.upsun.com/manage-resources/resource-init.md#specify-a-resource-initialization-strategy).

To [keep your repository clean](https://docs.upsun.com/learn/bestpractices/clean-repository.md) and avoid performance issues, make sure you enable both the `fetch-branches` and `prune-branches` options.

## 3. Validate the integration

Verify that your integration is functioning properly [using the CLI](https://docs.upsun.com../overview.md#validate-integrations):

```bash
upsun integration:validate
```

### Add the webhook manually

If the integration was added with the correct permissions, the necessary webhook is added automatically.
If you see a message that the webhook wasn't added, add one manually.

To configure a webhook on a GitLab repository,
you need to have Maintainer or Owner [user permissions](https://docs.gitlab.com/ee/user/permissions.md).

1. Get the webhook URL by running this command: `upsun
 integration:get --property hook_url`.
1. Copy the returned URL.

1. In your GitLab repository, click **Settings** > **Webhooks**.
1. In the **URL** field, paste the URL you copied.
1. Under **Trigger**, select **Push events** and **Merge request events**.
1. Click **Add webhook**.

You can now start pushing code, creating new branches,
and opening merge requests
directly in your GitLab repository.
Your Upsun environments are automatically created and updated.

## Environment parent and status

When a **branch** is created in GitLab,
an environment is created in Upsun with the default branch as its parent.
It starts as an [inactive environment](https://docs.upsun.com/glossary.md#inactive-environment) with no data or services.

When a **merge request** is opened in GitLab,
an environment is created in Upsun with the merge request's target branch as its parent.
It starts as an [active environment](https://docs.upsun.com/glossary.md#active-environment) with a copy of its parent's data.

## Source of truth

When you add an integration, your GitLab repository is considered to be the source of truth for the project.
Your Upsun project is only a mirror of that repository and you can only push commits to GitLab.

To clone your code, follow these steps:

 - In the Console, open the project you want to clone.
 - Click **Code**.
 - Click **Git**.
 - Run the command you find using Git.

When you do this, you're cloning from your integrated GitLab repository,
if you have the [appropriate access to do so](https://docs.upsun.com/integrations/source/troubleshoot.md).

### Sync, fetch, and prune

An integration from GitLab to Upsun establishes that:

- GitLab is the source of truth, where Git operations occur
- Upsun is a mirror of that repository - provisioning infrastructure according to configuration, and orchestrating environments according to the branch structure of the GitLab repository

Actions that take place on Upsun don't affect commits on GitLab.
Because of this, the GitLab integration enables both `fetch-branches` (track branches on GitLab) and `prune-branches` (delete branches that don't exist on GitLab) by default.
You can change these settings but it is recommend to keep them.

When enabled by default, you are limited by design as to what actions can be performed within the context of a Upsun project with a GitLab integration:

| Action         | Observation         | Recommendation |
| :---------------- | :---------------- | :------- |
| Branch from parent | Running [`environment:branch`](https://docs.upsun.com/administration/cli/reference#environmentbranch) with the CLI, or selecting **Branch** in Console produces a new child environment, but it's deleted shortly after automatically. | Contribute to the GitLab repository itself by creating a branch and pull request. When the PR has been opened, a new environment will be provisioned for it.  |
| Merge in parent | Running [`environment:merge`](https://docs.upsun.com/administration/cli/reference#environmentmerge) with the CLI fails locally, and the **Merge** option in Console is not clickable. | Review and merge pull requests and/or branches on the GitLab repository. |
| Merge into child (sync code) | Running [`environment:synchronize`](https://docs.upsun.com/administration/cli/reference#environmentsynchronize) with the CLI fails locally, and the **Sync** option in Console won't allow me to include `code` in that sync. | Perform the merge locally from a matching branch on GitLab. For example, clone the most recent parent (`git pull origin parent-branch`), switch to the pull request branch (`git checkout ga-staging`), and then merge the parent into the current branch (`git merge main`). |

## Merge request URLs

When a merge request is deployed, the integration reports the primary URL for the deployed environment.
So you get a link to the deployed environment right in the merge request.

If you have multiple routes,
ensure the correct one is reported by [specifying the primary route](https://docs.upsun.com/define-routes.md#route-configuration-reference).

## Optional: use a GitLab CI/CD pipeline

If your GitLab instance is not accessible from the internet (e.g. air-gapped or behind a firewall), the GitLab integration process outlined above, based on incoming webhooks, might not be the best option to use.

Instead, [set up a push-based GitLab CI/CD pipeline](https://devcenter.upsun.com/posts/gitlab-push-solution/) that pushes code to Upsun and manages environments using the Upsun API. This setup allows you to:

- Deploy to production on `main` branch updates
- Create preview environments for Merge Requests
- Clean up environments when branches or MRs are removed
- Keep your GitLab instance fully private

**Detailed walkthrough**: 

For a detailed tutorial of how this works, with code samples and rationale, see this blog post: [Synchronize your air-gapped GitLab](https://devcenter.upsun.com/posts/gitlab-push-solution/).

You can also find a complete working example of how this works in the Upsun [GitHub snippets repository](https://github.com/upsun/snippets/tree/main/examples/gitlab-ci).


