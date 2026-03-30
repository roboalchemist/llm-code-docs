# Source: https://docs.envzero.com/guides/admin-guide/templates/helm.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Helm Integration

> Deploy Helm charts with env zero from Git repos, Helm repos, or S3 with diff and upgrade support

Helm is a popular package manager for Kubernetes, an open-source container orchestration platform. It simplifies the deployment and management of applications in Kubernetes clusters by providing a templating system and a standardized way to package, distribute, and deploy software. With Helm, developers can define their application's configuration and dependencies using "charts," which are essentially packages that contain all the necessary files, templates, and metadata. These charts can be versioned and shared, allowing for easy collaboration and reuse across different projects.

## Helm Chart Source

env zero supports using Helm with different chart sources:

1. `git`/`local` - Use charts that are defined in your code and are not hosted in a Helm Repo.
2. `Helm Repo` - both [regular chart repositories](https://helm.sh/docs/topics/chart_repository/) and [OCI-based registries](https://helm.sh/docs/topics/registries/). If the repository requires authentication you can provide the username and password in `ENV0_HELM_REPO_USERNAME` and `ENV0_HELM_REPO_PASSWORD` environment variables.
3. `S3` - Hosted directly on S3, similar to `Helm Repo` these charts are hosted remotely but they follow a different protocol.

In order to use a chart that is defined directly in your `git` select the appropriate VCS provider and provide the path to your Helm chart code:

<img src="https://mintcdn.com/envzero-b61043c8/NFoAIaj_CGEzw-yg/images/guides/admin-guide/templates/fe72ec5-image.png?fit=max&auto=format&n=NFoAIaj_CGEzw-yg&q=85&s=5d0bc70cec255f6db57631f1139e4b4b" alt="" width="1439" height="687" data-path="images/guides/admin-guide/templates/fe72ec5-image.png" />

In order to use a chart hosted in a `Helm Repo` / `S3` select the Helm Repo option in your template:

<img src="https://mintcdn.com/envzero-b61043c8/NFoAIaj_CGEzw-yg/images/guides/admin-guide/templates/2e0ed11-image.png?fit=max&auto=format&n=NFoAIaj_CGEzw-yg&q=85&s=75eeacb369b0c8fcf07409e0b3391af7" alt="" width="1424" height="717" data-path="images/guides/admin-guide/templates/2e0ed11-image.png" />

<Note>
  **Custom Flow For Helm Repo Deployments**

  Helm Repo deployments do not require git clone since the chart is not stored in git, therefore there is no custom flow for a Helm Repo template.

  In order to use custom flows (for cluster authentication or other usages) in Helm Repo you must configure a [Project-level Custom Flow](/guides/admin-guide/custom-flows/project-level-custom-flow).
</Note>

## Environment Deployment

1. Create a Helm [Template](/guides/admin-guide/templates).
2. Follow our guide to [Connect Your Kubernetes Cluster](/guides/getting-started/getting-started/connect-your-cloud-account/#kubernetes).
3. Create an [Environment](/guides/admin-guide/environments/env-zero-setting-up-a-new-environment)
   1. The provided namespace is automatically injected with [HELM\_NAMESPACE](https://helm.sh/docs/helm/helm/#helm) env var
   2. If the provided namespace does not exist, make sure to add `--create-namespace` flag in the `upgrade` step. (See the section below for the instructions)

<Info>
  **Cluster Authentication**

  Cluster authentication varies from one provider to another. Please refer to the [Connect Your Kubernetes Cluster](/guides/getting-started/getting-started/connect-your-cloud-account/#kubernetes) guide to learn more.
</Info>

## Environment Variables For Enhanced Customization

env zero supports a more customized usage by providing unique environment variables which will be passed to Helm:

1. `ENV0_HELM_SET_<YOUR_VARIABLE_NAME>` - set  an environment variable with the `ENV0_HELM_SET` prefix and the variable name as the suffix will be passed to Helm using the `--set` flag. E.g. `ENV0_HELM_SET_servers[0].port=80` will pass `--set server[0].port=80` to helm command. (see below for additional examples for inputting more complex types)
2. `ENV0_HELM_VALUES_FILES` - set this environment variable in order to provide Helm with your configuration which is stored in a values file(s), and will be passed to Helm using the `--values (-f)` flag.
3. `ENV0_HELM_CLI_ARGS` - this variable's value will be added to every Helm command execution, it can be used to pass additional custom arguments to Helm. For example it can be set to `--create-namespace --no-hooks`.  `ENV0_HELM_CLI_ARGS_diff`, `ENV0_HELM_CLI_ARGS_upgrade`, and `ENV0_HELM_CLI_ARGS_uninstall` are similar, but only added to corresponding helm commands.

## Execution Steps

Beyond the common steps such as Clone, Loading variables, etc. Deploy/Destroy Helm deployments contain the following steps:

1. Helm Diff - `helm diff upgrade <release-name> <chart-name/path> --install --allow-unreleased --color --detailed-exitcode`

2. Helm Upgrade - `helm upgrade <release-name> . --install --atomic --timeout 4h`

3. Helm Uninstall - `helm uninstall <release-name> --wait --timeout 4h`

<img src="https://mintcdn.com/envzero-b61043c8/NFoAIaj_CGEzw-yg/images/guides/admin-guide/templates/df7413d-image.png?fit=max&auto=format&n=NFoAIaj_CGEzw-yg&q=85&s=383affb5975c224f2b6f93127f89de09" alt="" width="1431" height="881" data-path="images/guides/admin-guide/templates/df7413d-image.png" />

<Info>
  **What Counts as a "diff"**

  env zero calculates diff between deployments using `helm` and the [helm diff plugin](https://github.com/databus23/helm-diff).

  The Helm diff plugin finds the exact difference between Helm executions, changes to your Kubernetes resources that were not done by Helm are left unnoticed.

  For example, A Drift Detection run would result as successful (meaning no drift was found) if a change was done manually inside the cluster without using Helm (such as increasing the `replicas` from 1 to 2).
</Info>

## Complex Input Value Examples

| Desired Helm Value | env zero HELM SET Input                                                                                                                 | Examples                                                                                                                                                                            |
| :----------------- | :-------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **annotations**    | **general rule:**<br />- use quotes to encapsulate the "key" of annotation.<br />- escape . (period) and / (slashes) with a (backslash) | `ENV0_HELM_SET_annotations ."nginx\.ingress\.kubernets\.io\/backend-protocol"=HTTPS`<br />`ENV0_HELM_SET_server.ingress.annotations."cert-manager\.io\/cluster-issuer"=letsencrypt` |
| **labels**         | **general rule:**<br />- use quotes to encapsulate the "key" of label.<br />- escape . (period) and / (slashes) with a (backslash)      | `ENV0_HELM_SET_labels."app\.kubernetes\.io\/name"=my-deployment`                                                                                                                    |
| **complex values** | **general rule:**<br />- escape spaces with a (backslash)                                                                               | `ENV0_HELM_SET_map={"foo:\ bar"}`                                                                                                                                                   |

Built with [Mintlify](https://mintlify.com).
