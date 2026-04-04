# Source: https://docs.upsun.com/environments/default-environment.md

# Rename the default environment

You can set the name of your default/production environment when creating a project.
To change it after project creation, follow the steps below.
For consistency, the steps are all given using the [CLI](https://docs.upsun.com../administration/cli.md).

The examples below are based off of changing the default environment from `old` to `main`.
Replace these names with what suits your situation.

If your site is already live,
remember that deactivating an environment is a destructive operation that can result in data loss.
To minimize potential issues, take the following steps:

- Switch the default environment during non-peak hours.
- Keep your data by taking a [backup of the `old` environment](https://docs.upsun.com../environments/backup.md)
- Reduce your DNS time-to-live (TTL) to a minimum.

## Requirements

If you have a domain set for your default environment, remove it before changing the default branch.
Otherwise you get an error that `default domain must be a valid project domain`.

To change the default branch, you need to be an [admin for the project](https://docs.upsun.com../administration/users.md)

## Note on source integrations

The following steps depend of whether your project has a [source integration](https://docs.upsun.com../integrations/source.md).

If it doesn't, Upsun is your primary remote repository for the project.
If it does, GitHub, GitLab, or BitBucket hosts your primary remote repository for the project.

## 1. Create a `main` environment

<div
>

            Without a source integration

            With a source integration

    In your local copy of your repository, create a new environment from ``old`` called ``main``:

```bash {}
upsun environment:branch main old
```

In your local copy of the external repository, make sure your default branch is up to date:

```bash {}
git checkout old && git pull origin old
```

Then create the ``main`` branch off of your default branch and push it to the remote repository:

```bash {}
git checkout -b main
git push origin main
```

Source integrations include all branches, but don’t activate the corresponding environments in Upsun.
Activate the ``main`` environment by running the following command:

```bash {}
upsun environment:activate main
```

## 2. Copy settings

If you have variables or other settings specific to your default environment, add those to the `main` environment.

For example, you may have variables for your production environment set to not be inheritable
(such as if you set them with `--inheritable=false` through the CLI).
These variables aren't added automatically to child environments and so you need to add them to the `main` environment manually.

If you want the `main` environment to send emails, [turn on outgoing email](https://docs.upsun.com../development/email.md).

## 3. Make `main` a top-level branch

To have `main` be your default, it needs to not be a child of `old`.
Use the following command to remove its parent and make it a top-level branch:

```bash
upsun environment:info -e main parent -
```

## 4. Make `main` the parent for other environments

<div
>

            Without a source integration

            With a source integration

    You probably have other environments that are children of ``old``.
For each environment, update its parent to ``main``:

```bash {}
upsun environment:info -e <ENVIRONMENT_NAME> parent main
```

To preserve your data on Upsun,
it’s best to switch your work in progress to be based off of ``main``.
Close any open pull/merge requests and resubmit them against ``main``.
If you want to continue working on branches after switching the default branch,
rebase them by running ``git rebase --onto main <BRANCH_NAME>``.
Once you resubmit a request, it appears under the ``main`` environment on Upsun.

## 5. Deactivate the `old` branch

To change your default branch, you first need to deactivate the existing default branch to remove protections.
Deactivate the `old` environment without deleting it by running the following CLI command:

```bash
upsun environment:delete --no-delete-branch old
```

## 6. Set `main` as the default branch

<div
>

            Without a source integration

            With a source integration

    Once ``old`` has been deactivated, set the project’s default branch to ``main``:

```bash {}
upsun project:info default_branch main
```

Set the project’s default branch in Upsun to ``main``:

```bash {}
upsun project:info default_branch main
```

Follow the instructions to change the default branch to ``main`` for your provider:

 - [GitHub](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-branches-in-your-repository/changing-the-default-branch)
 - [GitLab](https://docs.gitlab.com/ee/user/project/repository/branches/default.md#change-the-default-branch-name-for-a-project)
 - [BitBucket](https://community.atlassian.com/t5/Bitbucket-questions/How-to-change-MAIN-branch-in-BitBucket/qaq-p/977418)

## 7. Update DNS records

Whether or not you're using a CDN,
if your site is live you have probably added an Upsun address somewhere when configuring a [custom domain](https://docs.upsun.com../domains/steps.md).
If you have a CDN, it's with the CDN provider.
If you don't have a CDN, it's probably a `CNAME` record.

In either case, the setting probably has the old environment name as part of it.
Update the setting to use the new environment name.

Verify that the new URL is correct by comparing it to the result from this command:

```bash
upsun environment:info edge_hostname
```

## 8. Optional: Delete the `old` environment

If you no longer want the `old` environment, such as to stop accidental use, delete it completely:

```bash
upsun environment:delete --delete-branch old
```

