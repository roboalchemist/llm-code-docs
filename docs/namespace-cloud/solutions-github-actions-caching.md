<!-- Source: https://namespace.so/docs/solutions/github-actions/caching -->

# Caching in GitHub Actions

Accelerate your GitHub Actions workflows with Namespace's comprehensive caching solutions.
Our caching capabilities dramatically reduce build times by persisting data across workflow runs, eliminating redundant downloads, builds, and computations.
Namespace supports many frameworks and build systems natively through seamless integrations.

## Cache Volumes

[Cache Volumes](/docs/architecture/storage/cache-volumes) are Namespace's high-performance caching solution that persists data across GitHub Actions runs.
Unlike traditional caching solutions that require time-consuming uploads and downloads, Cache Volumes provide **instant access to cached data** through guaranteed cache locality.
Cache Volumes support very high concurrency through automatic forking and scale up to hundreds of GB to match your project needs.

#### Enable caching

Go to the desired [Runner Profile](https://cloud.namespace.so/workspace/actions/profiles) and enable caching.

![profile cache dialog](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Frunnerprofilecaching.97a4825c.png&w=1200&q=75)

The minimum cache size is 20 GB.

#### Use the cache in your workflow

The simplest way to start using the cache is to adopt [`nscloud-cache-action`](/docs/reference/github-actions/nscloud-cache-action).
The action supports many popular frameworks natively, but can also be used to cache arbitrary files or directories.

1. Add the action to your workflow and select which framework you use. You can enable caching for multiple frameworks simultaneously:

   ```
   - name: Configure Go and Rust cache
     uses: namespacelabs/nscloud-cache-action@v1
     with:
       cache: |
         go
         rust
   ```

   For a full list of supported frameworks, check out the [action reference](/docs/reference/github-actions/nscloud-cache-action).
2. In case native support is not available yet, you can still make your framework work with Cache Volumes. Simply configure a list of paths to retain:

   ```
   - name: Configure custom cache
     uses: namespacelabs/nscloud-cache-action@v1
     with:
       path: |
         ~/.cache/custom-tool
         /opt/shared-libraries
   ```

   Our [support team](mailto:support@namespace.so) can help you identify the optimal cache configuration.

#### Optional: Skip GitHub's action cache

After enrolling Namespace's caching, you can disable GitHub's builtin action caching.
This ensures that you avoid any superfluous network transfers, reducing the setup time of your workflow further.

```
- name: Setup Go
  uses: actions/setup-go@v6
  with:
    go-version: "1.21"
    cache: false # Use Namespace caching instead
 
- name: Setup Node.js
  uses: actions/setup-node@v6
  with:
    node-version: "18"
    package-manager-cache: false # Use Namespace caching instead
    cache: ""
```

## Container Images

Container Image caching allows you to dramatically reduce container startup times.
When enabling this feature, both image layers and the often expensive unpacking are cached locally.

#### Faster pulls with one click

To enable container image caching, ensure the corresponding option is checked in your [runner profile configuration](https://cloud.namespace.so/workspace/actions/profiles).

![profile container image caching](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Frunnerprofilecontainerimages.8aef9878.png&w=1200&q=75)

That's it!
Repeated pulls of the same image will now complete in seconds rather than minutes.

## Git Checkouts

Namespace can speed up your git checkouts by caching a mirror of your git repository.
Checkout caching works best when cloning large repositories with many files.
If you are also checking out submodules or rely on Git LFS, these are automatically cached, too.

#### Enable Git Checkout caching

Open your runner profile in the [Dashboard](https://cloud.namespace.so/workspace/actions/profiles) and enable **Git repository checkouts** in the caching section.

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

## Toolchain Downloads

Cache downloads from most setup actions like `actions/setup-go`, `actions/setup-python`, and `actions/setup-node`.
GitHub's tool SDK [@actions/tool-cache](https://github.com/actions/toolkit/tree/main/packages/tool-cache) uses *RUNNER\_TOOL\_CACHE* to decide where to lookup and store artifacts.
Namespace configures the SDK to ensure any tool downloads are retained on the Cache Volume.

#### Enable toolchain download caching

To start caching toolchain downloads, ensure the corresponding option is checked in your [profile configuration](https://cloud.namespace.so/workspace/actions/profiles).

![profile toolchain download caching](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Frunnerprofiletoolchain.49366dc4.png&w=1200&q=75)

That's it!
After enabling this option, most setup actions will automatically use the faster Namespace cache.
You don't need to change your workflow.

## Action Downloads

When your job starts up, it needs to first download the actions to be executed.
Namespace can cache the downloaded action archives to avoid repeated work on subsequent runs.

#### Enable action download caching

To start caching action downloads, ensure the corresponding option is checked in your [profile configuration](https://cloud.namespace.so/workspace/actions/profiles).

![profile action download caching](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Frunnerprofileactiondownloads.69e114d4.png&w=1200&q=75)

## Advanced Cache Controls

Namespace cache volumes are separated at multiple levels to ensure security and prevent data leakage between different contexts.

### Isolation Levels

**Workspace Isolation**: Each workspace maintains completely separate cache volumes.
Caches from one workspace cannot be accessed by any other workspace, providing a strong security boundary between different organizational units or projects.

**Runner Profiles**: Different runner profiles use distinct cache volumes, even within the same workspace.
This ensures that builds running on different profiles don't interfere with each other's cached data by default.
Sharing the cache between two profiles is possible.

**Repository**: Each repository using a specific runner profile gets its own separate cache volume.
The cache volume will be shared between all jobs running for a Git repository, but remains distinct from other repositories, even when they share the same runner profile configuration.
Sharing the cache between two repositories is possible.

For scenarios requiring more control over the cache isolation boundary, [custom cache tags can be specified](/docs/reference/github-actions/runner-configuration#custom-cache-identity).

### Protect Caches from Updates

You can configure Cache Volumes to limit what git branches can perform updates to them.
Restricting the source of cache updates is useful to avoid cache poisoning.
When using this feature, all branches (including pull requests) can benefit from your cache, but only selected branches (e.g. `main`) may commit changes to it.

To specify which branches can update the cache volume, open the cache volume configuration, then
check **Show Advanced features**, and finally type the branch names.

![branch cache configuration](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fprotected-branches.50607dda.png&w=1200&q=75)

Any GitHub Actions job belonging to git branches that are not included in the allow-list, will be able to access the Cache Volumes, but their changes to the caches' content will not be persisted in the end.
You may also use an asterisk as a placeholder to match a branch name pattern.

## Build System Integrations

For advanced build systems, Namespace provides direct integrations that offer native, high-performance caching capabilities.

[Docker immediate performance benefits, advanced options available](/docs/solutions/github-actions/docker-builds)

[Bazel low-latency remote caching, available locally and in your CI](/docs/integrations/bazel)

[Turborepo distributed caching with automatic configuration](/docs/integrations/turborepo)

[Pants integrated caching with shared artifact storage](/docs/integrations/pants)

[Moonrepo (Moon) accelerated task orchestration and dependency management](/docs/integrations/moonrepo)

[Gradle high-performance build caching for JVM-based projects](/docs/integrations/gradle)

[sccache compiler caching for C, C++, Rust, and more](/docs/integrations/sccache)

Don't see your build system? Reach out to our [integrations team](mailto:support@namespace.so) to learn about upcoming releases and join the early access.

## Troubleshooting

Debugging issues that involve cached data is traditionally difficult as the environment of the workflow may change with each run.
Namespace provides multiple means to bridge this gap.

### Connecting to Cache Volumes

Namespace allows you to create one-off instances and connect them to a cache volume.

#### Create an instance

Using [nsc create --volume](/docs/reference/cli/create#--volume), you can create an instance and attach a cache volume.

```
$

```
nsc create --volume cache:<cache-tag>:/cache:<size>gb
```
```

The size and the tag should match what you see on [the dashboard](https://cloud.namespace.so/workspace/storage).

**Note**: this follows standard [cache volume semantics](/docs/architecture/storage/cache-volumes#cache-hits-and-misses). Namespace tries hard to provide you with the latest cache version, but you may rarely see a slightly stale cache instead.

#### Connect via SSH

```
$

```
nsc ssh sgm9ngfaqmsn2
```
```

Inside the instance, you can find the cache contents at the mount point:

```
$

```
ls -al /cache
```
```

### Setting Breakpoints

When you want to investigate a particular cache state, you can temporarily add a [breakpoint](/docs/solutions/github-actions/debugging#setting-breakpoints) to your workflow definition and jump into an interactive SSH session.

```
jobs:
  tests:
    runs-on: namespace-profile-with-caching
 
    steps:
      - uses: actions/checkout@v4
 
	  - uses: namespacelabs/nscloud-cache-action@v1
	    with: ...
 
      - name: Run tests
        shell: bash
        run: ...
 
      - name: Breakpoint if tests failed
        if: failure() # Remove this for an unconditional breakpoint
        uses: namespacelabs/breakpoint-action@v0
        with:
          duration: 15m
          authorized-users: <your-github-username>,<another-github-username>
```

The [`breakpoint-action`](/docs/reference/github-actions/breakpoint) will emit instructions how to access the paused runner.
The action is compatible with any runners and also available outside of Namespace.

```
▶ Run namespacelabs/breakpoint-action@v0
Connecting endpoint=rendezvous.namespace.so:5000
┌──────────────────────────────────────────────────────────────────────┐
│ Breakpoint! Running until Jun 26 09:58:26 UTC (14 minutes from now). │
└──────────────────────────────────────────────────────────────────────┘
Connect with:
ssh -p 44793 runner@rendezvous.namespace.so
```

Workflows with active breakpoint sessions are still "running" and continue to count towards your usage.

Got stuck? Need help with debugging one of your workflows? Our team is here to assist:

- **Technical Support**: Reach out to [support@namespace.so](mailto:support@namespace.so) to talk to one of our engineers.
- **Community**: Join our community [Discord](https://discord.gg/DqMzDFR6Hc) to learn about tips and best practices.

Last updated April 7, 2026
