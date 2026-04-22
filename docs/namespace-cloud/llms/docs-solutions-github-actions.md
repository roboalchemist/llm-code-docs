<!-- Source: https://namespace.so/docs/solutions/github-actions -->

# Accelerate Your GitHub Actions with Namespace

Transform your CI/CD pipeline with high-performance runners.
Namespace offers unique capabilities for Linux, Windows and macOS to speed up your GitHub workflows.

## Why Namespace Runners?

[Reliable, consistent performance on best-in-class AMD EPYC and Apple M4 CPUs](/docs/architecture/compute)

[High-throughput NVMe caching directly integrated with your tooling](/docs/solutions/github-actions/caching)

[Easy to debug via breakpoints, VNC, container logs, metrics, and OOM detection](/docs/solutions/github-actions/debugging)

[Scales with you from 1 vCPU and 2GB RAM, up to 32 vCPUs and 512GB RAM](/docs/architecture/compute/machine-shapes)

[Flexible, competitive pricing custom plans available for larger customers](/docs/workspaces/billing-and-limits)

[Enterprise ready SAML SSO, SCIM, SLAs, audit logs, external log & metric sinks](/docs/workspaces/access)

## Getting Started

To speed up your workflows with Namespace, you need to connect Namespace with
your GitHub organization and do a one-line change to your workflow definition:

1

#### Connect your GitHub organization to Namespace

Open the Dashboard

2

#### Update your workflows

Change the `runs-on` field in a workflow file to a Namespace profile or label.

```
jobs:

build:

-     runs-on: ubuntu-latest

+     runs-on: namespace-profile-default

steps:

- name: Checkout

uses: actions/checkout@v4

...
```

To read more about the available configuration options, including machine sizes, see [Configure your Runners](/docs/solutions/github-actions#configure-your-runners).

3

#### Done!

Your GitHub workflow will now run on Namespace!

## Configure your Runners

Namespace runners offer a high degree of customization and unique capabilities.
Start off by selecting your target OS / architecture and picking an optimal shape.
Subsequent guides will explore how to benefit from each of the available solutions.

### Create a Profile

1. Open the [Dashboard](https://cloud.namespace.so/workspace/actions/profiles) and press "New Profile".
2. Specify a name. The name will be part of the `runs-on` label in your workflow file.
3. Select if you want to run on Linux AMD64, Linux ARM64, Windows or macOS.
4. Pick a resource shape. You can change the shape later to find the best fit.
   ![edit profile dialog](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Frunnerprofileapple.bec52470.png&w=1200&q=75)
5. Confirm by pressing "Create Profile".

### Select the Profile

Update the `runs-on` label in your workflow file to select the runner profile:

```
jobs:

myjob:

runs-on: namespace-profile-big-apple
```

Namespace Runners are powered by Namespace Compute which uses best-in-class hardware for every platform:

- **Linux AMD64** runs on high-performance AMD EPYC CPUs.
- **Linux ARM64** supported by AmpereOne (high memory configurations), and Apple M4 Pro.
- **Windows AMD64** runs on high-performance AMD EPYC CPUs.
- **macOS ARM64** Apple M4 Pro (or M2 Pro on some configurations).

Selecting an optimal resource shape can optimize your performance and cost.
Larger shapes may be faster if your workflows can make use of the additional resources.
Smaller shapes may be cheaper if your runner is oversized.
We recommend observing a few runs first before adjusting the resource shape.

## Next Steps: Optimize Your Workflows

Now that you have Namespace Runners configured, enhance your CI/CD pipeline with these advanced features:

**[Caching Solutions →](/docs/solutions/github-actions/caching)**
Learn how to implement cross-invocation caching for dependencies, tools, and build artifacts to dramatically reduce workflow execution time.

**[High-Performance Docker Builds →](/docs/solutions/github-actions/docker-builds)**
Discover how to leverage Remote Builders and local caching strategies for optimal Docker build performance.

**[Custom Base Images →](/docs/solutions/github-actions/custom-base-images)**
Speed up workflows by pre-installing your dependencies and tools in custom runner images.

**[Debugging Made Simple →](/docs/solutions/github-actions/debugging)**
Access advanced debugging tools and techniques that make troubleshooting GitHub Actions workflows effortless.

**[Analytics & Insights →](/docs/solutions/github-actions/job-analytics)**
Monitor workflow performance, track resource usage, and identify optimization opportunities with detailed analytics.

**[Optimizing Usage →](/docs/solutions/github-actions/optimizing-usage)**
Learn how to use insights data to optimize resource usage, reduce costs, and improve workflow performance.

**[Advanced Configuration →](/docs/reference/github-actions/runner-configuration)**
Specific configuration options for privileged workflows, container jobs, advanced caching, and more.

## Enterprise Support

Need custom machine shapes, dedicated capacity, or specialized support?
Our [support team](mailto:support@namespace.so) can unlock runners with up to 512GB RAM and provide dedicated consultation for complex CI/CD requirements.

Last updated September 11, 2025
