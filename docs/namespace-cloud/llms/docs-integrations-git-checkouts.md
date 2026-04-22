<!-- Source: https://namespace.so/docs/integrations/git-checkouts -->

# Git Checkouts

Namespace can speed up your git checkouts by caching a mirror of your git repository.
Checkout caching works best when cloning large repositories with many files.
If you are also checking out submodules or rely on Git LFS, these are automatically cached, too.

## Getting started

When running your GitHub Actions on [Namespace runners](solutions/github-actions), cached git checkouts are available directly from the UI.

#### Enable Git Checkout caching

In your runner profile, enable **Git repository checkouts** in the caching section.

![profile cache dialog](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Frunnerprofilegitcheckouts.214811f4.png&w=1200&q=75)

#### Configure your workflow

To start using the newly enabled cache in your workflow, replace mentions of `actions/checkout` with [`nscloud-checkout-action`](/docs/reference/github-actions/nscloud-checkout-action):

```
jobs:

tests:

runs-on: namespace-profile-integration-tests

steps:

- name: Check out my repo

-       uses: actions/checkout@v4

+       uses: namespacelabs/nscloud-checkout-action@v8

with:

path: my-repo

- run: |

cd my-repo && git status
```

Check out the [action reference](/docs/reference/github-actions/nscloud-checkout-action) for a full
list of supported options.

## How it works

Namespace retains a mirror of your git repository on [Cache Volumes](/docs/architecture/storage/cache-volumes), making them available on subsequent runs.
Cache Volumes are Namespace's high-performance caching solution that persists data across GitHub Actions runs.
Unlike traditional caching solutions that require time-consuming uploads and downloads, Cache Volumes provide **instant access to cached data** through guaranteed cache locality.

Learn more about Namespace's comprehensive [caching solutions](/docs/solutions/github-actions/caching).

Last updated November 14, 2025
