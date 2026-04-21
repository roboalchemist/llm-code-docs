<!-- Source: https://namespace.so/docs/architecture/storage/artifact-storage -->

# Artifact Storage

Namespace maintains high-performance artifact storage, ideal for workflow artifacts.
It is globally distributed, with transparent local caching.
Artifact storage offers highly-available, high throughput object storage that is seamlessly integrated with the rest of Namespace.
It is the backing technology behind our [Bazel cache](/docs/integrations/bazel) and [Turborepo](/docs/integrations/turborepo) integration.

## Uploading Artifacts

Artifact creation follows a two-phase commit model:

1. Call `CreateArtifact` to obtain a pre-signed upload URL and an `upload_id`.
2. Upload the artifact data to the signed URL using an HTTP PUT request.
3. Call `FinalizeArtifact` with the `upload_id` to commit the artifact and make it downloadable.

Artifacts can be versioned — if an artifact with the same path already exists, set
`create_new_version_if_exists` to create a new version rather than failing.

To download an artifact, use `ResolveArtifact` which returns a pre-signed download URL valid for 30 minutes.

You can interact with artifacts using the [CLI](/docs/reference/cli/artifact-upload) or the
[ArtifactsService API](https://buf.build/namespace/cloud/docs/main:namespace.cloud.storage.v1beta).

## Fine-grained Access Control

Artifacts are shared with your workspace by default, allowing for frictionless collaboration.
Namespace supports fine-grained access controls, allowing you to flexibly restrict or grant image access.
Learn more about RBAC support under [workspace access controls](/docs/workspaces/access).

## Expiration Policy

Artifacts can be associated with an expiration date at creation time.
Once expired, the artifact is automatically removed and no longer consumes storage.
Artifacts can also be manually expired using [`nsc artifact expire`](/docs/reference/cli/artifact-expire).

## Integrations

The artifact storage is a versatile building block that you can use to store large data close to your workloads.
To interact with artifacts manually, you can simply use the [CLI](/docs/reference/cli/artifact-upload).
Namespace maintains a selection of native integrations allowing a seamless adoption of artifacts.

### GitHub Actions

Namespace maintains API-compatible variants of `actions/upload-artifact` and `actions/download-artifact`.
Simply replace your current uses with [`namespace-actions/upload-artifact`](/docs/reference/github-actions/upload-artifact) and [`namespace-actions/download-artifact`](/docs/reference/github-actions/download-artifact).

### Pull through HTTP caching

You can use the in-network artifact storage for transparent caching of remote HTTP dependencies.
Check out [nsc artifact cache-url](/docs/reference/cli/artifact-cache-url) to get started.

Last updated March 20, 2026
