<!-- Source: https://namespace.so/docs/reference/github-actions/nscloud-setup -->

# namespacelabs/nscloud-setup

namespacelabs/nscloud-setup@v0

[namespacelabs/nscloud-setup](https://github.com/namespacelabs/nscloud-setup) is a GitHub action configuring access to Namespace.
After executing the action, other GitHub actions that access Namespace resources can be used.
`nscloud-setup` also installs and configures the Namespace CLI `nsc` in your GitHub Actions workflow, allowing you to manually interact with Namespace.

## Prerequisites

1. Install the [Namespace GitHub application](https://github.com/apps/namespace-cloud).

   1. Open the [**Dashboard**](https://cloud.namespace.so/workspace/select).
   2. On the **Federation** page, click on **Connect Organization** under the **Associated GitHub organizations** section.
   3. In the pop-up window, select the organization to which you want to install the Namespace app.
   4. Finally, choose if you want to install the app to all repositories or just a selection.
2. Grant `id-token: write` permissions to your workflow to allow GitHub Actions to
   [authenticate with Namespace](/docs/federation/github-actions).

**Note:** Workflows using Namespace-managed [GitHub Runners](/docs/solutions/github-actions) can typically skip `nscloud-setup`.
They are already authenticated with Namespace. On Namespace runners, the action may still be useful to obtain the address of your [private container registry](/docs/architecture/storage/container-registry).

## Example

```
jobs:
  deploy:
    name: Ephemeral cluster
    runs-on: ubuntu-latest
    # These permissions are needed to interact with GitHub's OIDC Token endpoint.
    permissions:
      id-token: write
      contents: read
    steps:
      - uses: actions/checkout@v4
      - uses: namespacelabs/nscloud-setup@v0
      - name: Create an ephemeral Kubernetes cluster
        run: |
          nsc cluster create
```

## Options

`nscloud-setup` has no parameters.

## Outputs

### registry-address

Endpoint address of your workspace's private [Namespace Container Registry](/docs/architecture/storage/container-registry).

Last updated September 1, 2025
