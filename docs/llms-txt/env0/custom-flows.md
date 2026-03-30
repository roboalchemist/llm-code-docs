# Source: https://docs.envzero.com/guides/admin-guide/custom-flows.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Custom Flows Overview

> Run custom commands during deployment with env0.yml custom flows for init, plan, apply, and destroy steps

Custom Flows are a way to run your own commands during the deployment of your environment. These will run outside the IaC of your choice and allow you to perform supplemental actions. For example, injecting custom variables into your IaC code before you apply it or calling external APIs with the outputs of your deployment.

Custom Flows allow you to run whatever you want (bash, Python, Gcloud, Ansible, CloudFormation, etc.) at any point in the deployment process– before or after Terraform init/plan/apply, destroy/error and even [tasks](/guides/admin-guide/environments/ad-hoc-tasks).

To attach a custom flow to a single [template](/guides/admin-guide/templates):\
Create a file named *env0.yml* under the template folder. env zero will use this file if it's found in your git repository.

For sharing a custom flow between templates:\
Create a file named *env0.yml* under the root folder. env zero will use this file if it is defined, and an env0.yml file is not found in the template folder.

For sharing a custom flow for all environments under a particular project:\
Create a custom flow file in any repository and [configure](/guides/admin-guide/custom-flows/project-level-custom-flow) it as a project policy.

*We support the suffixes env0.yml and env0.yaml in the same way.*

<Info>
  **Working Directory for env0.yml**

  env zero will run Custom Flow commands with the working directory being the one containing the YAML file. Based on that, you can reference your commands to other scripts/commands by using `./script.sh.`
</Info>

<Info>
  **Project level Custom Flows**

  Only the env0.yaml is "cloned" for project level Custom Flows, this means that scripts and other files referenced by your Custom Flow will either need to be cloned into the working directory, or you must specify the repo path location of your scripts and files.
</Info>

Below is an example of a custom flow that creates a more "dynamic" Terraform file, based on an environment variable value, and uses Python and Jinja before the Terraform Init (the full example of this template git repo (including the `env0.yml` file) is [here](https://github.com/env0/blueprints/blob/demo/redash/v5.0.2/aws/)):

```yaml  theme={null}
version: 2

deploy:
  steps:
    terraformInit:
      before:
        - name: Hydrate Template
          run: |
            pip install --user jinjanator
      echo "Generating \"stage.auto.tfvars\" for \"$STAGE\""
      jinjanate stage.auto.tfvars.j2 > stage.auto.tfvars
      echo -e "Generated \"stage.auto.tfvars\":\n$(cat stage.auto.tfvars)"
      echo "Generating \"elb.tf\" for \"$STAGE\""
      jinjanate elb.tf.j2 > elb.tf
      echo -e "Generated \"elb.tf\":\n$(cat elb.tf)"

```

You can include the following possible hooks in an \_ env0.yml \_ file.

<Info>
  **OpenTofu backward-compatibility**

  Terraform's Custom Flow format is interchangeable with OpenTofu's.
</Info>

<Note>
  Task  hooks

  Task hook uses the stored working directory source code to run, it will not fetch an updated version from you VCS provider. If you need updated files on your working directory to run the task hooks you will need to first run a deployment to update the files.
</Note>

## Hook Stages

<CodeGroup>
  ```yaml Terraform theme={null}
  version:
    type: number
  shell: sh (default) or bash

  deploy:
    onCompletion:
      - type: string
    onSuccess:
      - type: string
    onFailure:
      - type: string

    steps:
      setupVariables:
        after:
          - type: string

      terraformInit:
        before:
          - type: string
        after:
          - type: string

      terraformPlan:
        before:
          - type: string
        after:
          - type: string

      terraformApply:
        before:
          - type: string
        after:
          - type: string

      storeState:
        before:
          - type: string
        after:
          - type: string

      terraformOutput:
        before:
          - type: string
        after:
          - type: string

  destroy:
    onCompletion:
      - type: string
    onSuccess:
      - type: string
    onFailure:
      - type: string

    steps:
      setupVariables:
        after:
          - type: string

      terraformInit:
        before:
          - type: string
        after:
          - type: string

      terraformPlan:
        before:
          - type: string
        after:
          - type: string

      terraformDestroy:
        before:
          - type: string
        after:
          - type: string

  ```

  ```yaml OpenTofu theme={null}
  version:
    type: number
  shell: sh (default) or bash

  deploy:
    onCompletion:
      - type: string
    onSuccess:
      - type: string
    onFailure:
      - type: string

    steps:
      setupVariables:
        after:
          - type: string

      opentofuInit:
        before:
          - type: string
        after:
          - type: string

      opentofuPlan:
        before:
          - type: string
        after:
          - type: string

      opentofuApply:
        before:
          - type: string
        after:
          - type: string

      storeState:
        before:
          - type: string
        after:
          - type: string

      opentofuOutput:
        before:
          - type: string
        after:
          - type: string

  destroy:
    onCompletion:
      - type: string
    onSuccess:
      - type: string
    onFailure:
      - type: string

    steps:
      setupVariables:
        after:
          - type: string

      opentofuInit:
        before:
          - type: string
        after:
          - type: string

      opentofuPlan:
        before:
          - type: string
        after:
          - type: string

      opentofuDestroy:
        before:
          - type: string
        after:
          - type: string
  ```

  ```yaml Pulumi theme={null}
  version:
    type: number
  shell: sh (default) or bash

  deploy:
    onCompletion:
      - type: string
    onSuccess:
      - type: string
    onFailure:
      - type: string

    steps:
      setupVariables:
        after:
          - type: string

      pulumiPreview:
        before:
          - type: string
        after:
          - type: string

      pulumiUp:
        before:
          - type: string
        after:
          - type: string

      storeState:
        before:
          - type: string
        after:
          - type: string

      pulumiOutput:
        before:
          - type: string
        after:
          - type: string

  destroy:
    onCompletion:
      - type: string
    onSuccess:
      - type: string
    onFailure:
      - type: string

    steps:
      setupVariables:
        after:
          - type: string

      pulumiPreview:
        before:
          - type: string
        after:
          - type: string

      pulumiDestroy:
        before:
          - type: string
        after:
          - type: string
  ```

  ```yaml CloudFormation theme={null}
  version:
    type: number
  shell: sh (default) or bash

  deploy:
    onCompletion:
      - type: string
    onSuccess:
      - type: string
    onFailure:
      - type: string

    steps:
      setupVariables:
        after:
          - type: string

      cfCreateChangeSet:
        before:
          - type: string
        after:
          - type: string

      cfDeploy:
        before:
          - type: string
        after:
          - type: string

      cfOutput:
        before:
          - type: string
        after:
          - type: string

      storeState:
        before:
          - type: string
        after:
          - type: string

  destroy:
    onCompletion:
      - type: string
    onSuccess:
      - type: string
    onFailure:
      - type: string

    steps:
      setupVariables:
        after:
          - type: string

      cfListStackResources:
        before:
          - type: string
        after:
          - type: string

      cfDeleteStack:
        before:
          - type: string
        after:
          - type: string
  ```

  ```yaml Kubernetes theme={null}
  version:
    type: number
  shell: sh (default) or bash

  deploy:
    onCompletion:
      - type: string
    onSuccess:
      - type: string
    onFailure:
      - type: string

    steps:
      setupVariables:
        after:
          - type: string
      
      k8sDiff:
        before:
          - type: string
        after:
          - type: string

      k8sApply:
        before:
          - type: string
        after:
          - type: string

      storeState:
        before:
          - type: string
        after:
          - type: string

  destroy:
    onCompletion:
      - type: string
    onSuccess:
      - type: string
    onFailure:
      - type: string

    steps:
      setupVariables:
        after:
          - type: string

      k8sDiff:
        before:
          - type: string
        after:
          - type: string

      k8sDelete:
        before:
          - type: string
        after:
          - type: string
  ```

  ```yaml Helm theme={null}
  version:
    type: number
  shell: sh (default) or bash

  deploy:
    onCompletion:
      - type: string
    onSuccess:
      - type: string
    onFailure:
      - type: string

    steps:
      setupVariables:
        after:
          - type: string
      
      helmDiff:
        before:
          - type: string
        after:
          - type: string

      helmUpgrade:
        before:
          - type: string
        after:
          - type: string

      storeState:
        before:
          - type: string
        after:
          - type: string

  destroy:
    onCompletion:
      - type: string
    onSuccess:
      - type: string
    onFailure:
      - type: string

    steps:
      setupVariables:
        after:
          - type: string

      helmDiff:
        before:
          - type: string
        after:
          - type: string

      helmUninstall:
        before:
          - type: string
        after:
          - type: string
  ```

  ```yaml Ansible theme={null}
  version:
    type: number
  shell: sh (default) or bash

  deploy:
    onCompletion:
      - type: string
    onSuccess:
      - type: string
    onFailure:
      - type: string

    steps:
      setupVariables:
        after:
          - type: string

      ansibleGalaxy:
        before:
          - type: string
        after:
          - type: string
      
      ansibleCheck:
        before:
          - type: string
        after:
          - type: string

      ansiblePlaybook:
        before:
          - type: string
        after:
          - type: string


  destroy:
    onCompletion:
      - type: string
    onSuccess:
      - type: string
    onFailure:
      - type: string

    steps:
      setupVariables:
        after:
          - type: string
  ```

  ```yaml Task theme={null}
  version:
    type: number
  shell: sh (default) or bash

  task:
    onCompletion:
      - type: string
    onSuccess:
      - type: string
    onFailure:
      - type: string

    steps:
      setupVariables:
        after:
          - type: string

      taskCommands:
        before:
          - type: string
        after:
          - type: string

      storeState:
        before:
          - type: string
  ```

</CodeGroup>

## Specifying the Shell

Currently, env zero's Custom Flow features allow you to select the shell: `sh` (default) or `bash`\
To use `bash`, add the following snippet into your\_ env0.yaml\_:

```yaml  theme={null}
shell: bash
```

## Handling Errors

If any command in your custom flow returns a non-zero exit code, the env zero deployment will stop on a 'Failed' status. You can leverage this to perform validation. For instance, asserting that a certain environment variable was supplied.

In such a case, env zero will display any output from `stderr` as the deployment error. If no output is found in `stderr`, it will be shown as an 'Unknown Error'.

<Info>
  **Error Message Handling**

  Use the `1>&2` notation to redirect stdout messages to `stderr`. This allows env zero to display the message in its UI (see [I/O Redirection](https://tldp.org/LDP/abs/html/io-redirection.html))
</Info>

Here is an example:

```yaml env0.yml theme={null}
version: 2
deploy:
  steps:
    setupVariables:
      after:
        - if [ -z "$MY_VAR" ]; then echo "MY_VAR must be supplied" 1>&2 && exit 1; fi
```

## Exposed env zero System Environment Variables

env zero exposes the following environment variables for you to use:

| Variable Name              | Value Description                                                                            |
| -------------------------- | -------------------------------------------------------------------------------------------- |
| `ENV0_ENVIRONMENT_ID`      | The deployed Environment ID                                                                  |
| `ENV0_PROJECT_ID`          | The Project ID of the deployed Environment                                                   |
| `ENV0_PROJECT_NAME`        | The Project Name of the deployed Environment                                                 |
| `ENV0_DEPLOYMENT_LOG_ID`   | The deployment ID                                                                            |
| `ENV0_DEPLOYMENT_TYPE`     | The deployment type.<br />One of `deploy` / `destroy` / `prPlan` / `driftDetection` / `task` |
| `ENV0_DEPLOYMENT_REVISION` | The revision<br />(available only when deployment revision is defined)                       |
| `ENV0_WORKSPACE_NAME`      | The Terraform Workspace name used in the Environment                                         |
| `ENV0_ROOT_DIR`            | The root repository path                                                                     |
| `ENV0_ORGANIZATION_ID`     | Your env zero organization ID                                                                |
| `ENV0_TEMPLATE_ID`         | The deployed Template ID                                                                     |

See [this example](https://github.com/env0/templates/tree/master/misc/environment-variables) for using these variables in our public templates repo.

<Note>
  **Note**

  You can use exposed env zero variables in the UI using the \$\{...} notation:

  <Frame>
    <img src="https://mintcdn.com/envzero-b61043c8/pcx_nh6zT3at7dYL/images/guides/admin-guide/env0_variables_ui_notation_example.png?fit=max&auto=format&n=pcx_nh6zT3at7dYL&q=85&s=671efc34e7810ec973184794bc1d4636" alt="env0 variables UI notation example" width="1393" height="283" data-path="images/guides/admin-guide/env0_variables_ui_notation_example.png" />
  </Frame>
</Note>

## env zero System Files

env zero generates a few files during runtime that can be used in a custom flow (and terraform) to help you programmatically access environment variables and Terraform variables.

### env0.system-env-vars.json

This file contains all the environment variables generated by env zero through metadata. See above for list of available environment variables and their respective descriptions.

### env0.auto.tfvars.json

This file contains all the variables defined through the UI in json format. For example, you can parse the file using jq.

```bash  theme={null}
cat env0.auto.tfvars.json | jq -r '.'
```

### env0.env-vars.json

This file is similar to the Terraform variables, and contains all the environment variables defined through the env zero UI. This can also be parsed using jq.

<Info>
  **Accessing Environment Variables in Terraform**

  You can use this file to access environment variables within your Terraform code. Simply read and jsondecode the env0.system-env-vars.json file to get access to the metadata. See example:

  ```hcl  theme={null}
  locals {
    env_vars = jsondecode(file("env0.system-env-vars.json"))
  }

  output "env0_environment_id" {
    value = local.env_vars.ENV0_ENVIRONMENT_ID
  }
  ```

</Info>

## Using Additional CLI Tools in Custom Flows

Custom flows execute your shell commands within a dedicated deployment container. This container comes pre-loaded with a standard set of utilities, including common OS tools and package managers.

However, if your custom flow hooks require specific command-line interface (CLI) tools, such as the `AWS` CLI or `kubectl`, you must explicitly configure the deployment to install them.

To add these tools, set the `ENV0_INSTALLED_TOOLS` environment variable with a comma-separated list of the tools you need.

For example, to make the AWS CLI and kubectl available in your deployment container, you would set the following variable:

```bash  theme={null}
ENV0_INSTALLED_TOOLS=aws,kubectl
```

You can set this variable at any level. For instance, if one project uses `kubectl` and another uses the `aws` CLI, it's best to set the variable at the project level to ensure each environment has only the tools it requires.

### Available tools

| Tool                     | Description                                                                                                                                                                                                                                      |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `kustomize`              | A Kubernetes native tool for customizing application configuration.                                                                                                                                                                              |
| `infracost`              | Shows cloud cost estimates for Terraform, helping to manage budgets.                                                                                                                                                                             |
| `kubelogin`              | A kubectl plugin for non-interactive authentication with OIDC providers.                                                                                                                                                                         |
| `opa`                    | Open Policy Agent, a general-purpose policy engine for cloud native environments.                                                                                                                                                                |
| `aws`                    | The official command-line tool for Amazon Web Services.                                                                                                                                                                                          |
| `gcloud`                 | The primary command-line tool for Google Cloud Platform.                                                                                                                                                                                         |
| `az`                     | The official command-line tool for Microsoft Azure.                                                                                                                                                                                              |
| `helm`                   | The package manager for Kubernetes, used to find, share, and use software.                                                                                                                                                                       |
| `dyff`                   | A diff tool for YAML files, especially useful for Kubernetes manifests.                                                                                                                                                                          |
| `kubectl`                | The command-line tool for controlling Kubernetes clusters.                                                                                                                                                                                       |
| `terratag`               | A CLI tool for managing tags across all resources in a Terraform project.                                                                                                                                                                        |
| `pwsh`                   | PowerShell, a cross-platform task automation and configuration management framework. (Not supported on the **arm64** architecture or when running in **strictSecurityContext** mode. If you need this functionality, you must extend the image.) |
| `gke-gcloud-auth-plugin` | A plugin to handle GKE authentication for kubectl and other clients.                                                                                                                                                                             |

<Warning>
  **Version Updates**

  env0 will periodically update tool versions to address security considerations or end-of-life (EoL) versions.
  Customers will be notified in advance whenever an update introduces breaking changes.

  You can always check the currently installed versions under the Init Packages step.
</Warning>

## Exporting your own environment variables

In order to export your own Environment Variable to use in any downstream custom flow you should write a shell command in the format: `echo KEY=VALUE >> $ENV0_ENV`.\
In later steps of the same deployment, you will be able to use `$KEY` to access the stored value.

<Note>
  **Note**

  For \_env0.yml \_ files that use schema version 2, when using multiple commands within a given step e.g., `terraform:plan-before`, all commands are executed inside the same shell. Exported Environment variables like these are only available for the steps that follow.
  For values within the same shell, using the usual `export key=value` still works.
</Note>

## Forcing Manual Approvals

Whenever `ENV0_REQUIRES_APPROVAL=true` occurs, env zero will force deployment to require approval, regardless of the Auto Approval setting in the Environment.

For example, instead of failing a deployment based on some policies, we can use this field to help ensure that others can still review and proceed with the deployment.

Usage:\
`- echo ENV0_REQUIRES_APPROVAL=true >> $ENV0_ENV`

## FAQ

**Q.** How can I use Custom Flows to add new Terraform variables?

**A.** The recommended approach to adding Terraform variables is to use variable definitions files, specifically the *.auto.tfvars* or *.auto.tfvars.json* files, to pass additional variables to your Terraform code.

Note: Please be aware of the Terraform Variable Definition Precedence order, defined [here](https://developer.hashicorp.com/terraform/language/values/variables#variable-definition-precedence).

Another way is to create new Environment Variables inside the custom flow in the form of `TF_VAR_key=value`. To do that, please follow our [guide for exporting your environment variables](https://www.terraform.io/cli/config/environment-variables#tf_var_name).

**Q.** I noticed that env zero runs `init` again after approval. How can I run my custom flow only once per deployment?

**A.** You can take advantage of the ENV0\_REVIEWER\_NAME field to see if the plan has already been approved.

For example:

```yaml  theme={null}
deploy:
  steps:
    terraformInit:
      before: # run ./myScript.sh only on pre-approval
        - if [[ -z $ENV0_REVIEWER_NAME ]]; then ./myScript.sh; fi  
```

**Q.** Do env zero SaaS runners use static IP addresses? I would like to whitelist env zero's runners to access my network.\
**A.** Yes, env zero uses those [IP addresses](/guides/overview/security-overview/ip-addresses) for all the outbound requests.

**Q.** How do I export a multi-line string into an environment variable?\
**A.** Utilize `\n` and `sed` for example: `"MY_PEM_FILE='$(cat ${PEM_FILE} | sed -e 's/\n/\\n/g')'" >> $ENV0_ENV`

<Warning>
  **GitHub API limits**

  When downloading resources from GitHub (e.g. tflint), make sure you use an authenticated call (e.g. `curl -u USER:TOKEN`). Otherwise, you will likely run into API limits, as unauthenticated calls are pooled with other SaaS users, with a much lower API limit.  See [GitHub Rate Limiting](https://docs.github.com/en/rest/overview/resources-in-the-rest-api#rate-limiting).
</Warning>

<Info>
  Additional Content

* [Managing Terraform variable hierarchy](https://www.env0.com/blog/managing-terraform-variable-hierarchy)
* [Why env zero is a Terraform Cloud alternative?](https://www.env0.com/alternatives/terraform-cloud-alternative)
</Info>

Built with [Mintlify](https://mintlify.com).
