<!-- Source: https://namespace.so/docs/reference/github-actions/nscloud-checkout-action -->

# namespacelabs/nscloud-checkout-action

namespacelabs/nscloud-checkout-action@v8

Namespace platform provides [Cache Volumes](/docs/solutions/github-actions/caching)
feature that allows workflows to share data across invocations.

These caches can store Git repository mirrors for fast checkouts. This action uses the
Namespace cache volumes to store and retrieve the git mirrors.

## Prerequisites

The git mirrors cache volumes must be enabled in the Runner Profile, or set in runners' labels.
See [Caching Git Repositories](/docs/integrations/git-checkouts)

## Example

```
jobs:
  build:
    name: Build large Git repository
 
    # If you use Runner Profiles with Git mirror caching enabled
    runs-on:
      - namespace-profile-{profile name}
 
    # Or, if you use runners labels
    runs-on:
      - nscloud-ubuntu-22.04-amd64-2x4-with-cache
      - nscloud-git-mirror-5gb
 
    steps:
      - name: Checkout with Namespace Git mirrors cache
        uses: namespacelabs/nscloud-checkout-action@v8
        with:
          fetch-depth: 10
```

## Options

### repository

*`string`* Repository name with owner. For example, namespacelabs/foundation. Default: `${{ github.repository }}`.

### ref

*`string`* The branch, tag or SHA to checkout. When checking out the repository that triggered a workflow, this defaults to the reference or SHA for that event. Otherwise, uses the default branch.

### token

*`string`* Personal access token (PAT) used to fetch the repository. Default: `${{ github.token }}`.

### fetch-depth

*`string`* Number of commits to fetch. 0 indicates all history for all branches and tags. Default: 1.

### path

*`string`* Relative path under `$GITHUB_WORKSPACE` to place the repository.

### submodules

*`string`* Whether to checkout submodules: `true` to checkout submodules or `recursive` to recursively checkout submodules.
Only available since version `v1`.

Starting with `v4`, submodule checkouts are also cached.

### dissociate

*`string`* Dissociate the checkout (and optionally submodules, if any) from the mirror. Default: "false".

Use "true" to dissociate the main repository or "recursive" to dissociate the main repository and all submodules.

Dissociate instructs git to copy all git objects to a checkout directory. After this, the checkout has no link to the Namespace Git mirror.
This allows docker-based GitHub actions to perform git operations on the checkout, such as git status.

### persist-credentials

*`string`* Whether to configure the token or SSH key with the local git config. Default: "true".

### lfs

*`string`* Whether to download and cache Git-LFS files. Default: "false".

Supported from version `v6`.

### filter

*`string`* Partially clone against a given filter.

Optional.

### sparse-checkout

*`string`* Do a sparse checkout on given patterns. Each pattern should be separated with new lines.

Optional.

### sparse-checkout-cone-mode

*`boolean`* Specifies whether to use cone-mode when doing a sparse checkout.

Optional. Default is `true`.

### max-attempts

*`number`* Maximum number of attempts for git network operations. Set to `1` to disable retries.

Optional. Default is `3`.

### trace

*`boolean`* Enable git tracing (`GIT_TRACE`) for debugging.

Optional. Default is `false`.

---

## Advanced: Running GitHub Jobs in Containers

We recommend using a separate profile for your workflows that run in containers.  
GitHub Actions run as user runner by default, but running in a container can change the user. Sharing caches from different users may lead to permission errors.

[Details →](/docs/solutions/github-actions#configure-your-runners)

When using [containers to run GitHub Jobs](https://docs.github.com/en/actions/using-jobs/running-jobs-in-a-container), extra configuration is required to make
the checkout action work correctly.

1. The Git mirror path must be mounted into the container.
2. The env var `NSC_GIT_MIRROR` must be set.

This action relies on a few specific properties of the environment and may require tuning to work with images that significantly diverge from vanilla Ubuntu. Please reach out to us at [support@namespace.so](mailto:support@namespace.so) for assistance.

See the following snippet for a working example.

With runner profilesWith runner labels

```
jobs:
  tests:
    runs-on: namespace-profile-my-profile-for-containers
 
    container:
      image: mcr.microsoft.com/playwright:v1.39.0
      env:
        NSC_GIT_MIRROR: ${{ env.NSC_GIT_MIRROR }} # env.NSC_GIT_MIRROR contains the path to git mirror directory.
      volumes:
        - /gitmirror:/gitmirror # Where the Cache Volume containing the git mirror is mounted.
 
    steps:
      - name: Checkout code
        uses: namespacelabs/nscloud-checkout-action@v8
```

Last updated February 13, 2026
