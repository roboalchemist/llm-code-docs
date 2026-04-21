<!-- Source: https://namespace.so/docs/reference/github-actions/runner-configuration -->

# GitHub Actions Runner Configuration

## Runner Labels

As an alternative to using profiles, you can keep the entire runner configuration version-controlled within your workflow file.
This works by specifying one or more labels in the `runs-on` configuration of your workflow.

### Machine Label

The most important label is the one selecting architecture, operating system, and machine shape.

The label looks like `nscloud-{os}-{arch}-{shape}`

**Note:** only one `nscloud` label is allowed in the
`runs-on` field of your workflow file. Namespace will not schedule any
workflow job if `runs-on`
specifies more than one `nscloud` label or invalid ones.

Supported machine labels per OS

|  | Ubuntu | Windows | MacOS |
| --- | --- | --- | --- |
| OS | - `ubuntu-20.04` - `ubuntu-22.04` - `ubuntu-24.04` | - `windows-2022` | - `macos-sonoma` - `macos-sequoia-stable` - `macos-sequoia` - `macos-tahoe` - `macos-tahoe-latest` - `macos-tahoe-slim` - `macos-tahoe-slim-latest` |
| Arch | - `amd64` - `arm64` | - `amd64` | - `arm64` |
| **Shape** These are our standard shapes. Larger and odd-sized shapes are available, see [Machine Shapes](/docs/architecture/compute/machine-shapes) | - `2x4` - `4x8` - `8x16` - `16x32` - `32x64` | - `2x4` - `4x8` - `8x16` - `16x32` - `32x64` | - `6x14` - `12x28` - `12x56` |

Examples:

| Label | OS | Architecture | vCPU | Memory |
| --- | --- | --- | --- | --- |
| `nscloud-ubuntu-22.04` | Ubuntu 22.04 | AMD 64-bit | 4 vCPU | 16 GB |
| `nscloud-ubuntu-22.04-amd64` | Ubuntu 22.04 | AMD 64-bit | 4 vCPU | 16 GB |
| `nscloud-ubuntu-24.04-amd64-4x8` | Ubuntu 24.04 | AMD 64-bit | 4 vCPU | 8 GB |
| `nscloud-ubuntu-22.04-amd64-4x8` | Ubuntu 22.04 | AMD 64-bit | 4 vCPU | 8 GB |
| `nscloud-ubuntu-20.04-amd64-4x8` | Ubuntu 20.04 | AMD 64-bit | 4 vCPU | 8 GB |
|
| `nscloud-ubuntu-22.04-arm64` | Ubuntu 22.04 | ARM 64-bit | 4 vCPU | 8 GB |
| `nscloud-ubuntu-24.04-arm64-4x8` | Ubuntu 24.04 | ARM 64-bit | 4 vCPU | 8 GB |
| `nscloud-ubuntu-22.04-arm64-4x8` | Ubuntu 22.04 | ARM 64-bit | 4 vCPU | 8 GB |
| `nscloud-ubuntu-20.04-arm64-4x8` | Ubuntu 20.04 | ARM 64-bit | 4 vCPU | 8 GB |
|
| `nscloud-windows-2022-amd64-4x8` | Windows Server 2022 | AMD 64-bit | 4 vCPU | 8 GB |
| `nscloud-windows-2022-amd64-8x16` | Windows Server 2022 | AMD 64-bit | 8 vCPU | 16 GB |
|
| `nscloud-macos-sonoma-arm64-6x14` | MacOS Sonoma | ARM 64-bit | 6 vCPU | 14 GB |
| `nscloud-macos-sequoia-arm64-6x14` | MacOS Sequoia | ARM 64-bit | 6 vCPU | 14 GB |
| `nscloud-macos-tahoe-arm64-6x14` | MacOS Tahoe | ARM 64-bit | 6 vCPU | 14 GB |

## Cache Volumes using Runner Labels

### Using a Cache Volume

With runner profilesWith runner labels

If you configured a runner profile using the web UI and use `namespace-profile-name` runner label, enable caching by simply going to the [runner profile](https://cloud.namespace.so/workspace/actions/profiles) and enabling caching.

![runner profile cache configuration](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Frunnerprofilecaching.97a4825c.png&w=1080&q=75)

Cache volumes also enable caching for built-in software (Git, containerd, toolchain).

You can also force a custom cache tag. This allows sharing a cache from multiple profiles or repositories:  
`runs-on: namespace-profile-my-profile;overrides.cache-tag=new-tag-value`

#### Example: Caching NPM Packages

Use our [`nscloud-cache-action`](/docs/reference/github-actions/nscloud-cache-action) to mount the volume
under the paths you want to cache.

With runner profilesWith runner labels

```
jobs:
  tests:
    runs-on:
      - namespace-profile-node-tests
 
    steps:
      - name: Setup PNPM cache
        uses: namespacelabs/nscloud-cache-action@v1
        with:
          cache: pnpm
 
      - name: Install dependencies and run tests
        run: |
          pnpm install
          pnpm run test
```

If you run GitHub jobs in a container, you also need to mount the cache volume inside the
container. See [Running jobs in Containers](#jobs-in-containers)

### Caching Docker Images Across Invocations

Namespace also makes it trivial to cache container image pulls
(and unpacks, often the most expensive bit) across invocations.

With runner profilesWith runner labels

To enable this feature, just open the runner profile configuration, add a cache volume and enable `Container images`.

```
jobs:
  tests:
    runs-on:
      - namespace-profile-integration-tests
 
    steps:
      - name: Pull ubuntu image
        run: |
          time docker pull ubuntu
```

The second time the above example runs, the time to pull the ubuntu container image
should be close to 0, as every layer was already cached by the first run.

#### Known incompatibilities for Docker Image caching

Docker image caching relies on standard Docker APIs.
However, if you are using a tool that does not fully support Docker APIs, Docker Image caching can break your workflow.
Known issues are:

- Spring Boot [does not provide full image spec compatibility](https://github.com/spring-projects/spring-boot/issues/40100) in their Buildpacks plugin

### Caching GitHub Tools

Namespace volumes can cache GitHub tools across invocations.

For example, `actions/setup-go` and `actions/setup-python`
actions first look for their binaries in

`$RUNNER_TOOL_CACHE` directory, before fetching
from remote.

With runner profilesWith runner labels

To make GitHub tool cache use Namespace volumes, open the runner profile configuration, add a cache volume and check `Toolchain downloads`.

```
jobs:
  tests:
    runs-on:
      - namespace-profile-go-python-tests
 
    steps:
      - uses: actions/setup-go@v6
      - uses: actions/setup-python@v6
```

### Caching Git Repositories

With cache volumes, you can set your GitHub workflow to cache large git repositories to speed up the checkout phase.

After you enabled the Git caching (see below how), you'll need to change your workflows to call our optimized checkout action,
which will make use of the cache volume to store and retrieve the git mirrors. See the
[`nscloud-checkout-action`](/docs/reference/github-actions/nscloud-checkout-action)
page for more details.

With runner profilesWith runner labels

To enable this feature, just open the runner profile configuration, add a cache volume and check `Git repository checkouts`.

```
jobs:
  tests:
    runs-on:
      - namespace-profile-integration-tests
 
    steps:
      - uses: namespacelabs/nscloud-checkout-action@v8
        name: Checkout
        with:
          path: my-repo
      - run: |
          cd my-repo && git status
```

#### Expected Use Cases

Note that the `namespacelabs/nscloud-checkout-action` is optimized to speed up only specific use-cases.
If your workflows do not belong to these, you might not see the expected performance improvement.

- Very large repositories: when the workflow needs to check out a repository with many or big files.
- Checkout long commits history: when the workflow needs to check out many commits (the default is only 1).
- Repositories with a large set of submodules.
- Repositories with Git LFS objects.

### Custom Cache Identity

For scenarios requiring full control over the cache isolation boundary, you can specify custom cache tags.

With runner profilesWith runner labels

To specify a custom cache tag when using a profile, append `;overrides.cache-tag=new-tag-value` to the profile name:

`runs-on: namespace-profile-my-profile;overrides.cache-tag=new-tag-value`

### Advanced: Protect Caches from Updates

You can configure Cache Volumes to limit what git branches can perform updates to them.
This configuration allows you to use the same cache as the main branch from other branches (e.g. pull requests), but not commit changes to it.

With runner profilesWith runner labels

To specify which branches can update the cache volume, open the cache volume configuration, then check `Show Advanced features`, and finally type the branch names.

![branch cache configuration](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fbranch-cache-protection.1841ecf0.png&w=1080&q=75)

Any GitHub Actions job belonging to git branches that are not included in the allow-list,
will be able to access the Cache Volumes, but their changes to the caches' content will
not be persisted in the end.

#### Manage Cache Access per Job

Instead of protecting your cache per branch, you can also select which jobs may write to the cache.
This allows you to share a cache amongst multiple jobs while some are not allowed to update the cache contents.
Any job without commit rights can still access the cache and can also change contents locally.
But any edits that it makes to the cache will be ignored for future runs.

With runner labels

If using runner labels, you can add the label `nscloud-cache-exp-do-not-commit` to a job.

```
jobs:
  tests:
    runs-on:
        - nscloud-ubuntu-22.04-arm64-4x16-with-cache
        - nscloud-cache-tag-cache-npm
        - nscloud-cache-size-100gb
        - nscloud-cache-exp-do-not-commit
 
    steps:
      - uses: actions/setup-node@v6
```

## Controlling Job Order

By default, there is no queuing or ordering for jobs: as soon as a job is scheduled a runner is started for it.
This changes when your workspace is hitting [concurrency limits](https://namespace.so/docs/architecture/compute/resource-limits)
and jobs have to wait for resources to become available.

Namespace offers controls to influence the order of jobs to be picked up:

### Deterministic assignments

By default, a job can be assigned to any runner that matches that job's labels.
A runner will pick up the job that it's assigned by GitHub, which does not happen in order.
This means that while hitting concurrency limits, jobs with the same labels might not be executed in the expected order.

To control this behaviour, you can add the run id to the labels.
Then only that specific job can be picked up by the runner started for it, and jobs are executed in the order in which they are scheduled:

With runner profilesWith runner labels

```
runs-on:
  - namespace-profile-my-profile
  - namespace-features:github.run-id=${{github.run_id}}
```

### Job Priority

When some workflows should not be blocked by other less, time-sensitive ones, you can assign them a priority.
Priority only affects scheduling while running into concurrency limits.

Pending jobs with the lowest numbers will be started first. Jobs with any priority specified take precedence over those without.

To specify a priority, append `job.priority=<number>` to the runs-on label:

With runner profilesWith runner labels

```
runs-on: namespace-profile-my-profile;job.priority=1
```

## Namespace Remote Builders

### Building very large images

For most users, relying on Remote Builders is the preferred option.

When building very large images, data transfers to Remote Builders can add up.

Your Docker builds can benefit from local cross-invocation caching, instead of using Remote Builders.

With "Local caching" enabled, Namespace automatically configures your
instance to both upload build metadata to your workspace, so it's logged and
traced; and caching is configured using a previously attached cache volume.

Make sure to size your cache appropriately, to benefit from high cache hit ratio.

With runner profilesWith runner labels

To enable this feature, just open the [runner profile](https://cloud.namespace.so/workspace/actions/profiles) configuration and add a cache volume. Next, select `Locally cached` for your Docker builds.

![locally cached Docker build configuration](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fin-runner-builder.7d07d80c.png&w=1080&q=75)

#### Caveats

- Build caching using "local caching" is not shared with Remote Builders; each
  repository uses its own separate cache.
- Although multi-platform builds are supported, only builds of the same platform
  as the runner itself, will experience native performance.

### Large amounts of concurrent builds

Namespace Remote Builders are configured to offer great performance for many concurrent builds.
These defaults provide ideal performance for most customers.
If you run a very large amount of concurrent builds,
please reach out to [support@namespace.so](mailto:support@namespace.so) and we'll scale your Remote Builders to match your needs.

### Builds without output

When you want to test a build without pushing or loading it, use the `cacheonly` output type.
This runs the full build and populates the cache, but skips the export step:

```
- uses: docker/build-push-action@v6
  with:
    context: .
    outputs: type=cacheonly
```

### Disable Build Caching

If you prefer to skip build caching altogether, you have two options:

1. **Revert the Docker build context to the default**: Namespace configures Remote Builders
   as a separate `buildx` [context](https://docs.docker.com/engine/reference/commandline/context/). Before invoking a build that should not be cached, you can switch back to the
   default by calling `docker buildx use default`. E.g.

   ```
   jobs:
     build:
       steps:
         - name: Use default builder
           run: docker buildx use default
    
         - name: Build and push
           uses: docker/build-push-action@v5
           with:
             context: .
             platforms: linux/amd64,linux/arm64
   ```
2. **Disable Remote Builders**: You can request that runners created for a
   particular workflow job do not use Remote Builders.

With runner profilesWith runner labels

To disable remote builders, just open the [runner profile](https://cloud.namespace.so/workspace/actions/profiles) configuration and select `No caching` for your Docker builds.

![local Docker builder configuration](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fno-remote-builder.4b1383df.png&w=1080&q=75)

## Privileged workflows

Namespace Runner Instances run the runner software itself in a container.
This approach facilitates software packaging and enables [custom base images](/docs/solutions/github-actions/custom-base-images).

If your workflow requires deeper access to the host system, Namespace can run your workflow as privileged and in the host pid namespace.
Common cases that require this are modifying kernel settings using sysctl or enabling swap.

To do so, enable the corresponding features in your runner labels:

With runner profilesWith runner labels

To make the runner container privileged append the feature `container.privileged`. Similarly, you can select the host pid namespace with `container.host-pid-namespace`.

```
runs-on:
  - namespace-profile-e2e-large;container.privileged=true;container.host-pid-namespace=true
```

## Systemd

Namespace Runner images by default do NOT use Systemd.
For some users this might require small changes to their workflows, e.g. replacing
`sudo systemctl start ...`
with
`sudo service start ...`.

If your workflows rely on systemd, an image using systemd is available [upon request](mailto:support@namespace.so).

## Running Jobs in Containers

Namespace Runners support using [custom containers for GitHub Jobs](https://docs.github.com/en/actions/using-jobs/running-jobs-in-a-container).

### Accessing Namespace resources from Containers

To access Namespace resources from within a container, extra configuration is required.
In particular, the directory `/var/run/nsc/` must be mounted into the container, and [`namespacelabs/nscloud-setup`](/docs/reference/github-actions/nscloud-setup) needs to be run.

See the following snippet for a working example of accessing Bazel:

```
tests:
  runs-on: namespace-profile-my-profile-for-containers
 
  container:
    image: <my-image-ref>
    volumes:
      - /var/run/nsc/:/var/run/nsc/
 
    steps:
      - uses: actions/checkout@v4
      - uses: namespacelabs/nscloud-setup@v0
      - name: Setup Bazel cache
        run: |
          nsc cache bazel setup --bazelrc /etc/bazel.bazelrc
      - name: Bazel test
        run: |
          bazel --bazelrc=/etc/bazel.bazelrc test //..
```

### Accessing Cache Volumes from Containers

To access [Cache Volumes](/docs/solutions/github-actions/caching#cache-volumes) from within a container, additional configuration is required.

For example, when using an Ubuntu-based custom image, the following snippet provides a working, minimal example:

```
tests:
  runs-on: namespace-profile-my-profile-for-containers
 
  container:
    image: <my-image-ref>
    env:
      NSC_CACHE_PATH: ${{ env.NSC_CACHE_PATH }} # env.NSC_CACHE_PATH contains the path to Cache Volume directory, that is `/cache`.
    volumes:
      - /cache:/cache # Where the Cache Volume is mounted.
    options: --cap-add=SYS_ADMIN # Required to by nscloud-cache-action to call `mount`.
 
  steps:
    - uses: actions/checkout@v4
 
    - name: Install sudo
      run: |
        apt-get update -y && apt-get install -y sudo
 
    - name: Setup cache
      uses: namespacelabs/nscloud-cache-action@v1
      with:
        cache: rust
```

Please see our [nscloud-cache-action documentation](/docs/reference/github-actions/nscloud-cache-action#advanced-running-github-jobs-in-containers) for details.

### Accessing Git Mirrors from Containers

If your workflow runs in a container, additional configuration is required to use [cached Git Repositories](/docs/integrations/git-checkouts):

```
tests:
  runs-on: namespace-profile-my-profile-for-containers
 
  container:
    image: <my-image-ref>
    env:
      NSC_GIT_MIRROR: ${{ env.NSC_GIT_MIRROR }} # env.NSC_GIT_MIRROR contains the path to the git mirror directory.
    volumes:
      - /gitmirror:/gitmirror # Where the git mirror cache is mounted.
 
  steps:
    - name: Checkout with Namespace Git mirrors cache
      uses: namespacelabs/nscloud-checkout-action@v8
```

Please see our [nscloud-checkout-action documentation](/docs/reference/github-actions/nscloud-checkout-action#advanced-running-github-jobs-in-containers) for details.

### Using Local build caching from Containers

While Remote Builders provide the best performance for most scenarios, in-runner builders (locally cached) excel when building massive images (10GB+).
Keeping the build local skips network transfer time.

To access in-runner builders from within a container, additional configuration is required.

#### Enable local build caching

With runner profilesWith runner labels

To enable this feature, just open the [runner profile](https://cloud.namespace.so/workspace/actions/profiles) configuration and add a cache volume. Next, select `Locally cached` for your Docker builds.

![locally cached Docker build configuration](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fin-runner-builder.7d07d80c.png&w=1080&q=75)

#### Update your workflow

In the job step definition, you need to forward the buildkit socket and create a builder inside the container that uses the parent:

```
jobs:
  myjob:
    container:
      image: <my-image-ref>
      volumes:
        - /var/run/buildkit/buildkitd.sock:/var/run/buildkit/buildkitd.sock
  steps:
    - uses: actions/checkout@v4
    - ...
    - name: Configure builder
      run: |
        docker buildx create --driver remote --name parent --use unix:///var/run/buildkit/buildkitd.sock
    - ...
```

## macOS Features

### Bleeding-edge Images

Namespace team continuously makes changes to macOS runner images to keep the software up-to-date and
add new Xcode versions as soon as Apple releases them.
[More info on image updates](/docs/architecture/compute/macos#macos-image-updates).

To avoid regressions upcoming images go through multiple release stages before production release.
This means that new Xcode versions become available to most customers with a short delay.
However, it is possible to take advantage of new Xcode versions early. You can enroll your
runners into using bleeding-edge macOS images.

**Note**: Images in the bleeding-edge channel have not passed the full set of validation checks and may contain regressions.
We are happy to hear feedback from early users of these images via Namespace support channels.
But enrolling should be done without expectation of perfect stability.

With runner profilesWith runner labels

Visit the [runner profile editor](https://cloud.namespace.so/workspace/actions/profiles) and select the **Use bleeding-edge images** checkbox.

![runner profile macOS bleeding edge checkbox](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fmacos-bleeding-edge.e79e83f9.png&w=1080&q=75)

Last updated April 8, 2026
