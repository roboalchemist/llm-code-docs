<!-- Source: https://namespace.so/docs/reference/cli/update-submodules -->

# nsc git-checkout update-submodules

Check out submodules in a git checkout on a Namespace runner.

`git-checkout update-submodules` checks out submodules of a git checkout on a Namespace runner, utilizing
Namespace Cache Volumes to speed up the operation on subsequent runs. It performs the equivalent of
`git submodule update --init` on each discovered submodule.

## Prerequisites

The operation must be executed on Namespace [GitHub Runners](/docs/solutions/github-actions) with caching
configured for [Git repository checkouts](/docs/integrations/git-checkouts).

The operation must be executed after a git checkout exists, e.g. after executing [`nscloud-checkout-action`](/docs/reference/github-actions/nscloud-checkout-action).

For the operation to be effective, submodules should not be checked out before running it. In the case of `nscloud-checkout-action`
this means that its `submodules` option of should be either absent or set to false.

## Usage

If the git checkout is on the default path, submodules can be checked out as follows:

```
nsc git-checkout update-submodules --mirror_base_path=${NSC_GIT_MIRROR} --repository_path=${GITHUB_WORKSPACE} --recurse
```

It is possible to customize the path of the main repository checkout by passing a different value in `--repository-path`.

If `--recurse` is given, `nsc git-checkout update-submodules` will recurse into submodules and check out their submodules, respectively.

Last updated July 7, 2025
