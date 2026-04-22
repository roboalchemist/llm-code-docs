<!-- Source: https://namespace.so/docs/architecture/storage/container-registry -->

# Container Registry

Namespace maintains nscr.io - a fully managed container image registry that is deeply integrated with the rest of the platform.
It is built atop the same technology as our high-performance [artifact storage](/docs/architecture/storage/artifact-storage).

[Learn how to use the container registry](/docs/solutions/docker-builders/registry)

## Fine-grained Access Control

Images pushed to nscr.io are shared with your workspace by default, allowing for frictionless collaboration.
Namespace supports fine-grained access controls, allowing you to flexibly restrict or grant image access.
Learn more about RBAC support under [workspace access controls](/docs/workspaces/access).

Images can be shared publicly using [`nsc registry share`](/docs/reference/cli/registry-share) or the [ContainerRegistryService API](https://buf.build/namespace/cloud/docs/main:namespace.cloud.registry.v1beta).
Shared images are accessible via a `public.nscr.io` URL and can optionally have an expiration date.

## Expiration policy

Container images stored in nscr.io can be associated with an expiration policy.
Once an image is expired, it is automatically removed and no longer consumes any storage.
This feature enables ephemeral container images, ideal for testing workflows.

Expiration policies can be configured at two levels: a default policy that applies to all repositories,
or a per-repository policy that overrides the default for a specific repository.
See [`nsc registry policy`](/docs/reference/cli/registry-policy) for details.

## Programmatic Access

You can access the Container Registry directly through HTTP calls.
To authorize incoming traffic, it employs [Basic access authentication](https://en.wikipedia.org/wiki/Basic_access_authentication).
The expected username is `token`, while the password is a workspace access token.
That is, the registry expects an `Authorization` header with the content `Basic base64(token:access_token)`.
You can generate an access token using our [CLI](/docs/reference/cli/installation):

```
$

```
nsc auth generate-dev-token
```
```

## Multi-cloud distribution

Namespace is highly invested in accelerating workflows that involve container images.
Enterprise customers can automatically have their container images distributed from nscr.io to other cloud providers.
[Reach out](mailto:support@namespace.so) to set up a registry sink.

Last updated March 20, 2026
