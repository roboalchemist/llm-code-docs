# Source: https://docs.upsun.com/learn/bestpractices/clean-repository.md

# Keep your Git repository clean

When a Git repository contains a high number of references and files, the performance of Git can decrease.
This is why most Git providers have repository size limits in place (for more information, see the [GitHub](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github), [GitLab](https://docs.gitlab.com/ee/user/gitlab_com/index.md#account-and-limit-settings)
and [Bitbucket](https://support.atlassian.com/bitbucket-cloud/docs/reduce-repository-size/) documentation).

The Upsun API and [Console](https://docs.upsun.com/administration/web.md) are closely tied to Git.
When the performance of Git decreases, Upsun API servers also become slower.
As a user, you can then experience significant latencies.
If your repository becomes too large, your Console may even become unresponsive,
leaving you unable to access your project.

To avoid such issues, make sure you keep your Git repository clean by following the instructions on this page.

If you're already facing performance issues and suspect they might be related to the size of your Git repository,
see how you can [troubleshoot a sizeable Git repository](#troubleshoot-a-sizeable-git-repository).

## Enable the automated pruning of old branches in your project

To keep your repository size to a minimum,
make sure that branches that don't exist anymore in your repository have also been deleted from Upsun.

To automate this process, when setting up a [source integration](https://docs.upsun.com/integrations.md),
enable the `prune-branches` option.

If you already have a source integration set up and want to enable the `prune-branches` option,
follow these steps:

 - Then, to enable the ``prune-branches`` option, run the following command:

```bash {}
upsun integration:update --project <PROJECT_ID> <SOURCE_INTEGRATION_ID> --prune-branches true
```

 - Navigate to your project.
 - Click Settings **Settings**.
 - Click **Project Settings**.
 - Click **Integrations** and select your source integration.
 - Click **Edit**.
 - Enter your access token and click **Continue**.
 - Select your repository and check the following boxes:

 - **Fetch branches from the remote repository to your project** (``fetch-branches`` option, mandatory to enable ``prune-branches``).
 - **Remove branches from your project that have disappeared remotely (requires the fetch branches option to be enabled)** (``prune-branches`` option).

 - Click **Save**.

## Upload your files through mounts

Keeping too many files, especially large binary files, in your Git repository can cause performance and stability issues.
Therefore, Upsun recommends that you only commit your source code in Git.

To upload any other files to your app, [create mounts](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#mounts)
and [transfer your files directly to them](https://docs.upsun.com/development/file-transfer.md#transfer-a-file-to-a-mount).

**Note**: 

Upsun does not currently support [Git Large File Storage](https://git-lfs.com/).

There is a **100MB default file size limit** for direct Git pushes to Upsun. Pushing files larger than the limit will result in rejecting the push, so please keep this in mind. If you’d like to request a custom limit, please [contact Support](https://docs.upsun.com/learn/overview/get-support.md).

## Troubleshoot a sizeable Git repository

If you're experiencing latencies or can't access your Console anymore,
your Git repository may have become too large and may need to be cleaned up.
To do so, follow these instructions:

1. Remove old, unwanted files from your repository (especially large files).
   You can do it manually, or use a tool such as [BFG Repo-Cleaner](https://rtyley.github.io/bfg-repo-cleaner/).
2. Remove stale branches from your repository and Upsun project.
3. Rebase and/or squash commits to clean up your history.
4. Make sure you [enable the automated pruning of old branches in your project](#enable-the-automated-pruning-of-old-branches-in-your-project)
   and [upload your files through mounts](#upload-your-files-through-mounts) to avoid facing the same situation in the future.

