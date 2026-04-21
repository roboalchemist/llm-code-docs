<!-- Source: https://namespace.so/docs/security/permissions -->

# Permissions

Namespace uses a resource-based permission model. Each API action is associated with a resource type
and optionally scoped to a specific resource ID.

The following lists all public resources and their available actions.

# Public Resources

The following resources and actions are publicly available in the Namespace API.

## artifact

Objects stored in a workspace, identified by a path and namespace.

- `create`: Upload a new artifact to the workspace.
- `expire`: Mark an artifact for deletion.
- `list`: List artifacts in the workspace.
- `resolve`: Download or retrieve an artifact.

## bazel/cache

Managed Bazel remote cache for accelerating builds by storing and retrieving build artifacts.

- `ensure`: Provision cache instance and get endpoint credentials.

## builder

Remote BuildKit instances that perform container image builds on behalf of a workspace.

- `access`: Connect to a running builder instance.
- `ensure`: Provision or reuse a builder instance.

## cache/gradle

Managed Gradle build cache for storing and retrieving build outputs.

- `ensure`: Set up and get Gradle cache endpoint credentials.
- `read`: Retrieve artifacts from the Gradle cache.
- `write`: Store artifacts in the Gradle cache.

## cache/httpcache

Managed HTTP build cache, compatible with Bazel, sccache, and other HTTP-cache-compatible tools.

- `ensure`: Set up and get HTTP cache endpoint credentials.
- `read`: Retrieve artifacts from the HTTP cache.
- `write`: Store artifacts in the HTTP cache.

## cache/turborepo

Managed Turborepo remote cache for storing and retrieving task-level build artifacts.

- `delete`: Delete all cached artifacts for a team.
- `list`: List teams with cached artifacts.
- `read`: Retrieve cached artifacts or check cache status.
- `report`: Submit Turborepo analytics and build events.
- `write`: Store artifacts in the Turborepo cache.

## containerregistry

Registry-wide configuration, including default and per-repository image expiration policies.

- `configure`: Manage registry expiration policies.

## containerregistry/image

Individual container images within a repository, identified by digest.

- `delete`: Delete a container image by digest.
- `get`: Get container image details.
- `list`: List container images across repositories.
- `update`: Update an image's expiration lifetime.

## containerregistry/repository

Named image repositories within the container registry.

- `delete`: Delete a repository and its contents.
- `list`: List image repositories in the registry.
- `share`: Create a publicly accessible link to an image.
- `unshare`: Revoke public access to a shared image.

## containerregistry/tags

Tags and tag version history within a repository.

- `list`: List tags in a repository.

## devbox

- `activate`
- `create`
- `expire`
- `fetch`
- `list`
- `update`

## devbox/image

- `expire`
- `fetch`
- `list`
- `wire`

## github/runner-profile

Configuration profiles for ephemeral GitHub Actions runners, defining instance shape, OS, cache volumes, and custom runner images.

- `create`: Create a new runner profile.
- `delete`: Delete a runner profile.
- `get`: Retrieve a specific runner profile.
- `list`: List all runner profiles.
- `update`: Update a runner profile.

## ingress

Authenticated network access to an instance's exposed ports.

- `access`: Access an instance's exposed ports.

## instance

Ephemeral compute environments for running containers, with support for Docker, Kubernetes, suspend/resume, and remote access.

- `create`: Create a new instance.
- `destroy`: Permanently terminate an instance.
- `dial_host`: Connect to an instance's host services.
- `exec`: Execute a command inside an instance.
- `get`: Retrieve an instance's details.
- `list`: List all instances in the workspace.
- `refresh`: Extend an instance's lifetime deadline.
- `release`: Detach an instance from its unique tag.
- `resume`: Wake a suspended instance.
- `ssh`: Start an SSH session to an instance.
- `suspend`: Pause an instance, snapshotting its state.
- `wait`: Wait for an instance to become ready.

## instance/ingress

Public internet ingress endpoints exposed from an instance.

- `list`: List ingress endpoints for an instance.
- `register`: Expose a backend from an instance to the internet.

## instance/notification

Lifecycle events representing instance status changes, such as running, terminated, or failed.

- `list`: List recent lifecycle events for instances.

## instance/o11y/logs

Streaming and historical log access for instance workloads.

- `get`: Stream or fetch logs from an instance.

## instance/o11y/metrics

Time-series resource usage metrics for instances, including CPU, memory, I/O, and storage.

- `get`: Retrieve resource usage metrics for an instance.

## instance/o11y/oom

Out-of-memory (OOM) kill events detected within an instance.

- `list`: List OOM kill events for an instance.

## network/fabric/segment

Isolated network segments enabling private connectivity between instances.

- `attach`: Connect to a private network segment.

## tenant

Workspaces in the Namespace platform.

- `get`: Retrieve workspace details and configuration.

## tenant/policies

Policy configuration for a workspace, including compute quotas and feature flags.

- `get`: Retrieve workspace policy settings and quotas.

## tenant/usage

Compute and storage resource usage tracking for a workspace.

- `get`: Retrieve usage summary for a workspace.

## testing/test/logs

Streaming access to test execution logs for a specific test target.

- `stream`: Stream logs for a test target execution.

## testing/test/result

Individual test target results within a test run, including pass/fail status and duration.

- `list`: List test results within a run.
- `push`: Submit test results for a target.

## testing/test/run

Top-level test execution sessions that group individual test results.

- `complete`: Mark a test run as finished.
- `create`: Start a new test run.
- `get`: Retrieve details of a test run.
- `list`: List test runs.

## token/revokable

Long-lived, explicitly revokable access tokens scoped to a workspace, with a maximum lifetime of 1 year.

- `create`: Create a new revokable access token.
- `list`: List revokable tokens for a workspace.
- `refresh`: Ensure a token remains valid for at least a requested duration.
- `revoke`: Revoke a token to prevent further use.

## volume/persistent

- `describe`
- `destroy`
- `list`

Last updated February 22, 2026
