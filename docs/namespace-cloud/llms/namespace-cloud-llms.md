# Namespace Documentation

## Solutions
- [GitHub Actions](https://namespace.so/docs/solutions/github-actions): The GitHub Actions solution page explains how to speed up your GitHub Actions by adopting Namespace runners.
- [Caching in GitHub Actions](https://namespace.so/docs/solutions/github-actions/caching): This documentation page explains how to speed up your GitHub Action runs further through Namespaces's comprehensive caching solutions. Cache Volumes provide high-performance caching for any framework or toolchain. In addition, Namespace offers seamless caching solutions for container image pulls, git checkouts and GitHub Action toolchains downloads.
- [Optimizing Docker Build Performance](https://namespace.so/docs/solutions/github-actions/docker-builds): This guide explains how to optimize your Docker build performance when using Namespace runners for your GitHub Actions.
- [Custom Base Images for GitHub Actions](https://namespace.so/docs/solutions/github-actions/custom-base-images): This documentation page explains how to avoid installing dependencies during your CI workflows by using custom base images.
- [Debugging GitHub Actions](https://namespace.so/docs/solutions/github-actions/debugging): This guide explains how debugging GitHub Actions gets significantly simpler with Namespace. You can interactively debug your runs through SSH/VNC/RDP access, pause runs at any step, or you can use advanced logging and observability features to root cause any issue.
- [Migration Guide](https://namespace.so/docs/solutions/github-actions/migration): This guide explains how to migrate your GitHub Action workflows to Namespace and how to adopt each feature incrementally to unlock the unparalleled performance benefits.
- [Docker Builds](https://namespace.so/docs/solutions/docker-builders): This page explains how to speed up you Docker builds with Namespace. Namespace offers high-performance remote builders that can be used from CI, or for local development. The performance gains stem from best-in-class performance and builtin maximum caching.
- [Container Registry](https://namespace.so/docs/solutions/docker-builders/registry)
- [Docker Build Observability](https://namespace.so/docs/solutions/docker-builders/tracing-and-logs): This guide explains how Namespace simplifies analysing the performance of Docker builds and root causing build failures.
- [Container Previews](https://namespace.so/docs/solutions/previews)
- [Kubernetes Previews](https://namespace.so/docs/solutions/previews/kubernetes)
- [Optimizing Docker Build Performance in Circle CI](https://namespace.so/docs/solutions/circle-ci/docker-builds)

## Framework integrations
- [Bazel integration](https://namespace.so/docs/integrations/bazel): This guide explains how to accellerate your Bazel builds with Namespace.
- [Turborepo caching](https://namespace.so/docs/integrations/turborepo): This guide explains how to accellerate your Turborepo builds with Namespace.
- [Pants integration](https://namespace.so/docs/integrations/pants): This guide explains how to accellerate your Pants builds with Namespace.
- [Moonrepo support](https://namespace.so/docs/integrations/moonrepo): This guide explains how to accellerate your Moonrepo builds with Namespace.
- [Git Checkouts](https://namespace.so/docs/integrations/git-checkouts): This guide explains Namespace can accelerate git checkouts for large repositories.
- [Docker Images](https://namespace.so/docs/integrations/docker-images): This guide walks through various optimizations provided by Namespace for the full lifecycle of a Docker image.
- [Integrating any framework](https://namespace.so/docs/integrations/any-framework): This guide explains how Namespace's flexible caching solutions can support virtually any framework.

## Compute, Storage and Networking
- [Multiplatform Compute](https://namespace.so/docs/architecture/compute)
- [Observability](https://namespace.so/docs/architecture/compute/observability)
- [SSH / Remote Display with Namespace Compute](https://namespace.so/docs/architecture/compute/ssh-remote-display)
- [Machine Shapes](https://namespace.so/docs/architecture/compute/machine-shapes): This page explains which shapes are available with Namespace for each platform and which prices are associated with each shape.
- [Nested Virtualization](https://namespace.so/docs/architecture/compute/nestedvirt): This page explains where nested virtualization is currently available, including KVM support by platform and architecture.
- [Resource Limits](https://namespace.so/docs/architecture/compute/resource-limits): This documentation page explains how concurrency limits work, and what concurrency limits are included in the different plans.
- [Storage](https://namespace.so/docs/architecture/storage): This overview page lists which storage options are available with Namespace.
- [Cache Volumes](https://namespace.so/docs/architecture/storage/cache-volumes): This page explains how cache volumes provide high-performance storage, how to use them and what to expect.
- [Container Registry](https://namespace.so/docs/architecture/storage/container-registry)
- [Artifact Storage](https://namespace.so/docs/architecture/storage/artifact-storage)
- [Secrets](https://namespace.so/docs/architecture/storage/secrets)
- [Networking](https://namespace.so/docs/architecture/networking)
- [Ingress](https://namespace.so/docs/architecture/networking/ingress): This page explains how instances can be accessed, and how unauthorized access is prevented.
- [Network Performance](https://namespace.so/docs/architecture/networking/performance): This page explains network-specific performance optimizations embedded in the Namespace platform.
- [Network Security](https://namespace.so/docs/architecture/networking/security): This page explains network-specific security features embedded in the Namespace platform.

## Workspaces

- [Workspaces](https://namespace.so/docs/workspaces)
- [Workspace Access](https://namespace.so/docs/workspaces/access): This documentation page explains access control mechanisms, authentication methods and which permissions are available to which workspace member.
- [Billing & Included Amounts](https://namespace.so/docs/workspaces/billing-and-limits): This page explains what is included in each plan and how additional usage is billed.
- [Data Residency for Workspaces](https://namespace.so/docs/workspaces/data-residency)
- [Security & Compliance](https://namespace.so/docs/workspaces/security): In this page, Namespace summarizes its multifaceted approach to ensure security and isolation.

## Federation

- [Federation](https://namespace.so/docs/federation): This overview page lists which workload federation options are available with Namespace.
- [Workload Federation with AWS](https://namespace.so/docs/federation/aws)
- [Workload Federation with GCP](https://namespace.so/docs/federation/gcp)
- [Workload Federation with OpenID Connect](https://namespace.so/docs/federation/openid)
- [Identity Federation with GitHub Actions](https://namespace.so/docs/federation/github-actions)
- [Identity Federation with CircleCI](https://namespace.so/docs/federation/circleci)

## Dashboard

This section contains documentation pages that explain features in the Namespace dashboard.

- [GitHub Actions Overview](https://namespace.so/docs/dashboard/github-actions): This page highlights how Namespace complements GitHub's UI through unique features that allow you to understand failures and job performance in a historic context.
- [Builds UI](https://namespace.so/docs/dashboard/builds)
- [Registry UI](https://namespace.so/docs/dashboard/registry)
- [Usage Explorer](https://namespace.so/docs/dashboard/usage-explorer): This page explains how to use Namespace's UI to better understand your usage and which workflows consume the most of your budget.

## SDK & API
- [SDK & API](https://namespace.so/docs/reference/api-sdk): The public Namespace API documentation can be found at https://buf.build/namespace/cloud

## GitHub Action reference

This section contains reference pages for GitHub Actions maintained by Namespace.

- [Runner configuration](https://namespace.so/docs/reference/github-actions/runner-configuration): This page is a comprehensive summary on how you can configure your Namespace runners for GitHub Actions, including how to use runner labels instead of profiles, and explaining many advanced features.
- [namespacelabs/nscloud-setup](https://namespace.so/docs/reference/github-actions/nscloud-setup)
- [namespacelabs/nscloud-setup-buildx-action](https://namespace.so/docs/reference/github-actions/nscloud-setup-buildx-action)
- [namespacelabs/nscloud-cluster-action](https://namespace.so/docs/reference/github-actions/nscloud-cluster-action)
- [namespacelabs/nscloud-cache-action](https://namespace.so/docs/reference/github-actions/nscloud-cache-action)
- [namespacelabs/nscloud-checkout-action](https://namespace.so/docs/reference/github-actions/nscloud-checkout-action)
- [namespacelabs/nscloud-expose-kubernetes-action](https://namespace.so/docs/reference/github-actions/nscloud-expose-kubernetes-action)
- [namespace-actions/upload-artifact](https://namespace.so/docs/reference/github-actions/upload-artifact)
- [namespace-actions/download-artifact](https://namespace.so/docs/reference/github-actions/download-artifact)
- [namespacelabs/breakpoint-action](https://namespace.so/docs/reference/github-actions/breakpoint)
- [namespace-actions/setup-turbocache](https://namespace.so/docs/reference/github-actions/setup-turbocache)

## CLI reference

This section contains reference pages for the commands offered by the Namespace CLI `nsc`.

- [Installation](https://namespace.so/docs/reference/cli/installation): This page explains how to get started with `nsc`.
- [nsc login](https://namespace.so/docs/reference/cli/login)
- [nsc workspace describe](https://namespace.so/docs/reference/cli/workspace-describe)
- [nsc create](https://namespace.so/docs/reference/cli/create)
- [nsc destroy](https://namespace.so/docs/reference/cli/destroy)
- [nsc extend](https://namespace.so/docs/reference/cli/extend)
- [nsc list](https://namespace.so/docs/reference/cli/list)
- [nsc logs](https://namespace.so/docs/reference/cli/logs)
- [nsc ssh](https://namespace.so/docs/reference/cli/ssh)
- [nsc top](https://namespace.so/docs/reference/cli/top)
- [nsc kubeconfig write](https://namespace.so/docs/reference/cli/kubeconfig-write)
- [nsc kubectl](https://namespace.so/docs/reference/cli/kubectl)
- [nsc docker login](https://namespace.so/docs/reference/cli/docker-login)
- [nsc docker attach-context](https://namespace.so/docs/reference/cli/docker-attach)
- [nsc docker buildx setup](https://namespace.so/docs/reference/cli/docker-buildx-setup)
- [nsc docker buildx cleanup](https://namespace.so/docs/reference/cli/docker-buildx-cleanup)
- [nsc build](https://namespace.so/docs/reference/cli/build)
- [nsc run](https://namespace.so/docs/reference/cli/run)
- [nsc expose container](https://namespace.so/docs/reference/cli/expose)
- [nsc expose kubernetes](https://namespace.so/docs/reference/cli/expose-kubernetes)
- [nsc ingress list](https://namespace.so/docs/reference/cli/ingress-list)
- [nsc ingress generate-access-token](https://namespace.so/docs/reference/cli/ingress-generate-access-token)
- [nsc git-checkout update-submodules](https://namespace.so/docs/reference/cli/update-submodules)
- [nsc volume list](https://namespace.so/docs/reference/cli/volume-list)
- [nsc volume release](https://namespace.so/docs/reference/cli/volume-release)
- [nsc artifact upload](https://namespace.so/docs/reference/cli/artifact-upload)
- [nsc artifact download](https://namespace.so/docs/reference/cli/artifact-download)
- [nsc artifact expire](https://namespace.so/docs/reference/cli/artifact-expire)
- [nsc artifact cache-url](https://namespace.so/docs/reference/cli/artifact-cache-url)
- [nsc bazel cache setup](https://namespace.so/docs/reference/cli/bazel-cache-setup): This command configures a bazel workspace to use Namespace for remote caching.
- [nsc pants cache setup](https://namespace.so/docs/reference/cli/pants-cache-setup): This command configures a pants workspace to use Namespace for remote caching.
- [nsc auth check-login](https://namespace.so/docs/reference/cli/auth-check-login)
- [nsc auth generate-dev-token](https://namespace.so/docs/reference/cli/auth-generate-dev-token)
