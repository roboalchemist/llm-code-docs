<!-- Source: https://namespace.so/docs/federation/github-actions -->

# Identity Federation with GitHub Actions

Namespace maintains a direct integration with GitHub, allowing any of your GitHub Action workflows to interact with Namespace resources.
Whether you run on Namespace runners, or any others, you're able to issue remote builds, create previews, or access your Bazel cache.

## From Namespace Runners

*No additional setup required*

If your GitHub Actions [run on Namespace](/docs/solutions/github-actions), your jobs can already access your workspace.
Each job contains a short-lived workload identity token which grants seamless access to your Namespace resources.
For example, you can download artifacts without additional setup steps:

```
download:
  runs-on: namespace-profile-default # runs on Namespace
  steps:
    # No setup needed. Runner can already access Namespace artifacts.
    - uses: namespace-actions/download-artifact@v2
      with:
        name: test-archive
        path: /tmp/destination
```

## From GitHub Runners

When running your jobs outside Namespace, you can still easily access your workspace.
Namespace federates with GitHub using [OpenID Connect](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-cloud-providers) to generate short-lived access tokens.
After a one-time setup, your workflows can access Namespace indefinitely, without relying on pre-shared keys which can be more easily compromised.

### Install the [Namespace GitHub application](https://github.com/apps/namespace-cloud/installations/new).

1. Open the [**Dashboard**](https://cloud.namespace.so/workspace/settings/federation).
2. On the **Federation** page, click on **Connect Organization** under **Associated GitHub organizations** section.
3. In the pop-up window, select which organization to connect to Namespace.
4. Finally, choose if you want to install the app to all repositories or just a selection.

### Grant federation permissions to your workflow

To allow GitHub Actions to authenticate with Namespace, you need to update your workflow definition.
In particular, you need to grant the permission `id-token: write` to federate with external cloud providers using OpenID Connect.

You can add the permission at the workflow level:

```
name: Example workflow
permissions:
  id-token: write # This is required for federation using OpenID Connect
  contents: read # This is required for actions/checkout
```

In this case, all the jobs within the workflow may use Namespace.

If you need to authorize only a single job, set the permission
within that job. For example:

```
name: Example workflow
jobs:
  example_job:
    permissions:
      id-token: write # This is required for federation using OpenID Connect
      contents: read # This is required for actions/checkout
```

### Initialize access to Namespace

After granting these permissions, simply use the [`namespacelabs/nscloud-setup`](/docs/reference/github-actions/nscloud-setup) action.
Subsequent steps can now access Namespace resources.

```
name: Example workflow
permissions:
  id-token: write # This is required for federation using OpenID Connect
  contents: read # This is required for actions/checkout
jobs:
  test:
    name: Preprod nodes test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Configure access to Namespace
        uses: namespacelabs/nscloud-setup@v0
      - run: |
          nsc cache bazel setup --bazelrc /etc/bazel.bazelrc
```

Last updated March 5, 2026
