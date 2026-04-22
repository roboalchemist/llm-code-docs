<!-- Source: https://namespace.so/docs/solutions/github-actions/migration -->

# Migrating to Namespace runners

You'd like to try out Namespace runners?
This guide explains how to incrementally adopt Namespace features to speed up your GitHub workflows.

## Prerequisites

Namespace needs access to your GitHub organization to be able to register runners on your behalf.  
If your company already uses Namespace, this access has probably already been established.

#### Link your GitHub organization to your Namespace workspace

Start from the [Namespace dashboard](https://cloud.namespace.so/workspace/ghrunners), and click on **Connect Organization**.

#### Complete the setup flow with GitHub

In the pop-up window, select which organization to connect to Namespace.
Also, choose if you want to install the app to all repositories or just a selection.

#### Optional: GitHub admin approvals

If you are not an administrator in the GitHub organization, you need to wait for an admin to approve the installation.
You will be able to connect Namespace to your GitHub organization after the installation has been approved.
[View pending installations](https://github.com/login/oauth/authorize?response_type=code&client_id=Iv1.91c4841cb44b841f&redirect_uri=https://cloud.namespace.so/workspace/actions/installations)

## Move to Namespace runners

To run your workflow on Namespace, you simply need to update the `runs-on` field in your workflow definition.

#### Create a profile

Open the [profile editor](https://cloud.namespace.so/workspace/actions/profiles) to see existing profiles for your workspace.
You can select from the existing profiles, or create a new profile:

1. Specify a name. The name will be part of the `runs-on` label in your workflow file.
2. Select if you want to run on Linux AMD64, Linux ARM64, Windows or macOS.
3. Pick a resource shape. You can change the shape later to find the best fit.
   ![edit profile dialog](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Frunnerprofileapple.bec52470.png&w=1200&q=75)
4. Confirm by pressing "Create Profile".

#### Select the Profile

Update the `runs-on` label in your workflow file to select the runner profile:

```
jobs:

myjob:

runs-on: macos-latest-xlarge

runs-on: namespace-profile-big-apple
```

#### That's it!

Your GitHub workflow will now run on Namespace!

## Next steps

When moving your workflow to Namespace, you should see immediate performance benefits.
You can speed up your workflows further by adopting more Namespace features.

### Faster Docker builds

*No configuration changes required*

The fastest way to speed up your Docker builds is to simply switch to Namespace runners.
[Remote Builders](/docs/solutions/github-actions/docker-builds) are enabled by default and will immediately accelerate your builds.

If your workflow includes `docker/setup-buildx-action`, you need to remove it to prevent overriding Namespaces configuration:

```
jobs:

build:

runs-on: ubuntu-latest

runs-on: namespace-profile-large-builder

steps:

- uses: actions/checkout@v4

- uses: docker/setup-qemu-action@v3

- uses: docker/setup-buildx-action@v3

- uses: docker/build-push-action@v5

with:

context: .

push: true

tags: my-registry/my-app:latest
```

That's it! Your builds are now running on high-performance Remote Builders with advanced caching.

To learn how Namespace speeds up your Docker builds, how to benefit from Namespaces Container registry, or how to gain comprehensive build performance insights, check out our [Docker build guide](/docs/solutions/github-actions/docker-builds).

### Adopt Cache Volumes

[Cache Volumes](/docs/architecture/storage/cache-volumes) are Namespace's high-performance caching solution that persists data across GitHub Actions runs.
For a deep dive into using Cache Volumes in GitHub actions, check out our [caching guide](/docs/solutions/github-actions/caching).

#### Enable caching

Go to the desired [Runner Profile](https://cloud.namespace.so/workspace/actions/profiles) and enable caching.
For most workflows, enabling all caching options leads to the best performance.

![profile cache dialog](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fcachingalloptions.0ae9ab8d.png&w=1200&q=75)

The caching options **Container images**, **Toolchain downloads** and **Action downloads** are fully transparent.
After enabling these options no additional steps are required.

#### Faster git checkouts

After enabling **Git repository checkouts** in your cache configuration, replace mentions of
`actions/checkout`
with
[`nscloud-checkout-action`](/docs/reference/github-actions/nscloud-checkout-action):

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

The main difference of `nscloud-checkout-action` over `actions/checkout` is builtin git mirror support, enabling the automatic caching.
Check out the [action reference](/docs/reference/github-actions/nscloud-checkout-action) for all supported options.

#### Adopt framework caching

The action [`nscloud-cache-action`](/docs/reference/github-actions/nscloud-cache-action) supports many popular frameworks natively.

Add the action to your workflow and select which framework you use. You can enable caching for multiple frameworks simultaneously:

```
- name: Configure Go and Rust cache

uses: namespacelabs/nscloud-cache-action@v1

with:

cache: |

go

rust
```

For a full list of supported frameworks, check out the [action reference](/docs/reference/github-actions/nscloud-cache-action).

#### Migrating from actions/cache

The action [`nscloud-cache-action`](/docs/reference/github-actions/nscloud-cache-action) can also be used to cache arbitrary files or directories.
If you are using `actions/cache` today, typically replacing it with `nscloud-cache-action` provides strictly better performance by skipping remote file transfers.

```
- name: Cache node modules

-   uses: actions/cache@v4

+   uses: namespacelabs/nscloud-cache-action@v1

with:

# npm cache files are stored in `~/.npm` on Linux/macOS

path: ~/.npm
```

Cache Volumes perform well when used frequently.
While onboarding to cache volumes, you may see a higher than usual amount of [cache misses](/docs/architecture/storage/cache-volumes#cache-hits-and-misses) before merging your change to main.

**Note:** `nscloud-cache-action` does not support manual partitioning (e.g. via cache keys); cache uses are shared across all users of a particular profile, including main and branch runs.
However, you can [protect caches](https://namespace.so/docs/solutions/github-actions/caching#protect-caches-from-updates) to only be writable by certain branches (e.g. by the main branch).

### Enable Build System Integrations

Namespace runners accelerate your [Docker builds](#faster-docker-builds) out of the box.
If you are using [Bazel](/docs/integrations/bazel), [Turborepo](/docs/integrations/turborepo), [Pants](/docs/integrations/pants), or [Moonrepo (Moon)](/docs/integrations/moonrepo) you can enable native caching integrations for your build system.

Don't see your build system? Reach out to our [integrations team](mailto:support@namespace.so) to learn about upcoming releases and join the early access.

Last updated November 14, 2025
