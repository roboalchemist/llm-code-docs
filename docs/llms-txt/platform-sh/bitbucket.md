# Source: https://docs.upsun.com/integrations/source/bitbucket.md

# Integrate with Bitbucket


If you have code in a Bitbucket repository, you might want to connect it to a Upsun project.
This means you can keep your Bitbucket workflows
and treat the Bitbucket repository as the source of truth for your code.

Your Upsun project becomes a mirror of your Bitbucket repository.
This means you shouldn't push code directly to Upsun.
Any changes you push directly get overwritten by the integration when changes happen in the Bitbucket repository.

When you set up an integration with Bitbucket,
it automates the following processes for you:

- Creating a new environment when a branch is created or a pull request is opened.
- Rebuilding the environment when new code is pushed to Bitbucket.
- Deleting the environment when a pull request is merged.

You can set up an integration with either Bitbucket Cloud
or a self-hosted [Bitbucket Server](https://confluence.atlassian.com/bitbucketserver/).

## Before you begin

To manage source integrations, you need to be a [project admin](https://docs.upsun.com../../administration/users.md).

You also need a Bitbucket Cloud or Bitbucket Server repository with working code.

## Bitbucket Cloud

### 1. Create an OAuth consumer

To integrate your Upsun project with an existing Bitbucket Cloud repository,
[create an OAuth consumer](https://support.atlassian.com/bitbucket-cloud/docs/use-oauth-on-bitbucket-cloud/):

![A screenshot of how to setup the Bitbucket OAuth consumer](https://docs.upsun.com/images/integrations/bitbucket/bitbucket-oauth-consumer.svg "0.35")

**Note**: 

Be sure to define the above as a private consumer by checking the **This is a private consumer** box.

The **Callback URL** isn't important in this case.
You can set it to `http://localhost`.

Copy the **Key** and **Secret** for your consumer.

### 2. Enable the Cloud integration

To enable the integration, use either the [CLI](https://docs.upsun.com/administration/cli.md) or the [Console](https://docs.upsun.com/administration/web.md).

 - ``PROJECT_ID`` is the ID of your Upsun project.
 - ``OWNER/REPOSITORY`` is the name of your repository in Bitbucket.
 - ``CONSUMER_KEY`` is the key of the [OAuth consumer you created](#1-create-an-oauth-consumer).
 - ``CONSUMER_SECRET`` is the secret of the [OAuth consumer you created](#1-create-an-oauth-consumer).

For example, if your repository is located at ``https://bitbucket.org/platformsh/platformsh-docs``,
the command is similar to the following:

```bash {}
upsun integration:add \
  --project abcdefgh1234567 \
  --type bitbucket \
  --repository platformsh/platformsh-docs \
  --key abc123 \
  --secret abcd1234 \
```

 - Select the project where you want to enable the integration.
 - Click **Settings Settings**.
 - Under **Project settings**, click **Integrations**.
 - Click **+ Add integration**.
 - Under **Bitbucket**, click **+ Add**.
 - Complete the form with:

 - The repository in the form ``owner/repository``
 - The [key and secret you generated](#1-create-an-oauth-consumer)

 - Check that the other options match what you want.
 - Click **Add integration**.

In both the CLI and Console, you can choose from the following options:

| CLI flag         | Default | Description                                                               |
| ---------------- | ------- | ------------------------------------------------------------------------- |
| `fetch-branches` | `true`  | Whether to mirror and update branches on Upsun and create inactive environments from them. When enabled, merging on an Upsun environment isn't possible. That is, merging environments must be done on the source repository rather than on the Upsun project. See note below for details related to this flag and synchronizing code from a parent environment. |
| `prune-branches` | `true`  | Whether to delete branches from Upsun that don’t exist in the Bitbucket repository. When enabled, branching (creating environments) must be done on the source repository rather than on the Upsun project. Branches created on Upsun that are not on the source repository will not persist and will be quickly pruned. Automatically disabled when fetching branches is disabled. |
| `build-pull-requests` | `true` | Whether to track all pull requests and create active environments from them, which builds the pull request. |
| `resync-pull-requests` | `false` | Whether to sync data from the parent environment on every push to a pull request. |
| `resources-init` | `false` | To [specify a resource initialization strategy](https://docs.upsun.com/manage-resources/resource-init.md#first-deployment) for new containers. Once set, the strategy applies to **all** the deployments you launch through your source integration. See more information on [available resource initialization strategies](https://docs.upsun.com/manage-resources/resource-init.md#specify-a-resource-initialization-strategy). |

**Note**: 

To [keep your repository clean](https://docs.upsun.com/learn/bestpractices/clean-repository.md) and avoid performance issues, make sure you enable both the ``fetch-branches`` and ``prune-branches`` options.

### 3. Validate the integration

Verify that your integration is functioning properly [using the CLI](https://docs.upsun.com../overview.md#validate-integrations):

```bash
upsun integration:validate
```

#### Add the webhook manually

If the integration was added with the correct permissions, the necessary webhook is added automatically.
If you see a message that the webhook wasn't added, add one manually.

To configure a webhook on a Bitbucket repository,
you need to have Admin [user permissions](https://support.atlassian.com/bitbucket-cloud/docs/manage-webhooks/).

1. Get the webhook URL by running this command: `upsun
 integration:get --property hook_url`.
1. Copy the returned URL.

1. Follow the [Bitbucket instructions to create a webhook](https://support.atlassian.com/bitbucket-cloud/docs/manage-webhooks/#Create-webhooks)
   using the URL you copied.
   Make sure to update the triggers to include all pull request events except comments and approval.

You can now start pushing code, creating new branches,
and opening pull requests
directly in your Bitbucket repository.
Your Upsun environments are automatically created and updated.

## Bitbucket Server

### 1. Generate a token

To integrate your Upsun project with a repository on a Bitbucket Server instance,
you first need to create an access token associated with your account.

[Generate a token](https://confluence.atlassian.com/display/BitbucketServer/HTTP+access+tokens).
and give it at least read access to projects and admin access to repositories.
Copy the token.

### 2. Enable the Server integration

To enable the integration, use either the [CLI](https://docs.upsun.com/administration/cli.md) or the [Console](https://docs.upsun.com/administration/web.md).

 - ``PROJECT_ID`` is the ID of your Upsun project.
 - ``OWNER/REPOSITORY`` is the name of the repository in Bitbucket server.
 - ``BITBUCKET_SERVER_ACCESS_TOKEN`` is the [token you generated](#1-generate-a-token).
 - ``BITBUCKET_SERVER_URL`` is the URL for your Bitbucket server.

For example, if your repository is located at ``https://example.com/upsun/upsun-docs``,
the command is similar to the following:
```bash {}
upsun integration:add \
  --project abcdefgh1234567 \
  --type bitbucket_server \
  --repository upsun/upsun-docs \
  --username user@example.com \
  --token abc123
  --bitbucket-url https://example.com  

```

 - Select the project where you want to enable the integration.

 - Click Settings **Settings**.

 - Under **Project settings**, click **Integrations**.

 - Click **+ Add integration**.

 - Under **Bitbucket server**, click **+ Add**.

 - Complete the form with:

 - Your server URL
 - Your Bitbucket username
 - The [token you generated](#1-generate-a-token)
 - The Bitbucket server project name
 - The repository in the form ``owner/repository``

 - Check that the other options match what you want.

 - Click **Add integration**.

In both the CLI and Console, you can choose from the following options:

| CLI flag | Default | Description |
| ``fetch-branches`` | ``true`` | Whether to mirror and update branches on Upsun and create inactive environments from them. |
| ``prune-branches`` | ``true`` | Whether to delete branches from Upsun that don’t exist in the Bitbucket server repository. Automatically disabled when fetching branches is disabled. |
| ``build-pull-requests`` | ``true`` | Whether to track all pull requests and create active environments from them, which builds the pull request. |
| ``pull-requests-clone-parent-data`` | ``true`` | Whether to clone data from the parent environment when creating a pull request environment. |

To [keep your repository clean ](https://docs.upsun.com/learn/bestpractices/clean-repository.md) and avoid performance issues,
  make sure you enable both the ``fetch-branches`` and ``prune-branches`` options.

### 3. Validate the integration

Verify that your integration is functioning properly [using the CLI](https://docs.upsun.com../overview.md#validate-integrations):

```bash
upsun integration:validate
```

#### Add the webhook manually

If the integration was added with the correct permissions, the necessary webhook is added automatically.
If you see a message that the webhook wasn't added, add one manually.

To configure a webhook on a Bitbucket repository,
you need to have Admin [user permissions](https://support.atlassian.com/bitbucket-cloud/docs/manage-webhooks/).

1. Get the webhook URL by running this command: `upsun
 integration:get --property hook_url`.
1. Copy the returned URL.

1. Follow the [Bitbucket instructions to create a webhook](https://confluence.atlassian.com/bitbucketserver076/managing-webhooks-in-bitbucket-server-1026535073.md#ManagingwebhooksinBitbucketServer-creatingwebhooksCreatingwebhooks)
   using the URL you copied.
   Send all events except comments and approval.

You can now start pushing code, creating new branches,
and opening pull requests
directly in your Bitbucket repository.
Your Upsun environments are automatically created and updated.

## Environment parent and status

When a **branch** is created in Bitbucket,
an environment is created in Upsun with the default branch as its parent.
It starts as an [inactive environment](https://docs.upsun.com/glossary.md#inactive-environment) with no data or services.

When a **pull request** is opened in Bitbucket,
an environment is created in Upsun with the pull request's target branch as its parent.
It starts as an [active environment](https://docs.upsun.com/glossary.md#active-environment) with a copy of its parent's data.

## Source of truth

When you add an integration, your Bitbucket repository is considered to be the source of truth for the project.
Your Upsun project is only a mirror of that repository and you can only push commits to Bitbucket.

To clone your code, follow these steps:

 - In the Console, open the project you want to clone.
 - Click **Code**.
 - Click **Git**.
 - Run the command you find using Git.

When you do this, you're cloning from your integrated Bitbucket repository,
if you have the [appropriate access to do so](https://docs.upsun.com/integrations/source/troubleshoot.md).

### Sync, fetch, and prune

An integration from Bitbucket to Upsun establishes that:

- Bitbucket is the source of truth, where Git operations occur
- Upsun is a mirror of that repository - provisioning infrastructure according to configuration, and orchestrating environments according to the branch structure of the Bitbucket repository

Actions that take place on Upsun don't affect commits on Bitbucket.
Because of this, the Bitbucket integration enables both `fetch-branches` (track branches on Bitbucket) and `prune-branches` (delete branches that don't exist on Bitbucket) by default.
You can change these settings but it is recommend to keep them.

When enabled by default, you are limited by design as to what actions can be performed within the context of a Upsun project with a Bitbucket integration:

| Action         | Observation         | Recommendation |
| :---------------- | :---------------- | :------- |
| Branch from parent | Running [`environment:branch`](https://docs.upsun.com/administration/cli/reference#environmentbranch) with the CLI, or selecting **Branch** in Console produces a new child environment, but it's deleted shortly after automatically. | Contribute to the Bitbucket repository itself by creating a branch and pull request. When the PR has been opened, a new environment will be provisioned for it.  |
| Merge in parent | Running [`environment:merge`](https://docs.upsun.com/administration/cli/reference#environmentmerge) with the CLI fails locally, and the **Merge** option in Console is not clickable. | Review and merge pull requests and/or branches on the Bitbucket repository. |
| Merge into child (sync code) | Running [`environment:synchronize`](https://docs.upsun.com/administration/cli/reference#environmentsynchronize) with the CLI fails locally, and the **Sync** option in Console won't allow me to include `code` in that sync. | Perform the merge locally from a matching branch on Bitbucket. For example, clone the most recent parent (`git pull origin parent-branch`), switch to the pull request branch (`git checkout ga-staging`), and then merge the parent into the current branch (`git merge main`). |

## Pull request URLs

When a pull request is deployed, the integration reports the primary URL for the deployed environment.
So you get a link to the deployed environment right in the pull request.

If you have multiple routes,
ensure the correct one is reported by [specifying the primary route](https://docs.upsun.com/define-routes.md#route-configuration-reference).


