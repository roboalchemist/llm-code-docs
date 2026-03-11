# Source: https://docs.envzero.com/guides/integrations/plugins/import-variable-plugin.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using the Import Variable Plugin

> Use the Import Variable plugin for code-driven output-to-variable mappings in env zero custom flows

<Info>
  **Consider using [Environment Outputs](/guides/admin-guide/variables/environment-outputs) instead**

  For most use cases, the native [Environment Outputs](/guides/admin-guide/variables/environment-outputs) feature is the recommended approach. It provides:

* Native UI integration with no API keys required
* Support for sensitive/secret outputs
* Built-in workflow support with [template-level configuration](/guides/admin-guide/variables/workflow-variables#passing-outputs-between-sub-environments)

  **Use this plugin** if you need a code-driven / GitOps approach where output-to-variable mappings are defined in `env0.yaml` custom flows and version-controlled alongside your IaC code, rather than configured through the UI.

  You can also define Environment Output variables programmatically using the [env0 Terraform Provider](https://registry.terraform.io/providers/env0/env0/latest).
</Info>

## Overview

This plugin fetches output values from another environment and inserts them as Terraform and/or environment variables. The `${env0:...}` and `${env0-workflow:...}` syntax documented below is specific to this plugin and is not part of the native Environment Outputs feature.

Similar to self hosted agent secrets, use this notation in the value of the terraform input value:

* `${env0:<environment id>:<output name>}`
* `${env0:<environment name>:<output name>}` (see note below about Environment Names restrictions)
* `${env0-workflow:<parent node name>:<output name>}`

For fetching output values that contain lists (like subnet ids) or maps (like tags), make sure you select JSON type for your input variable, and in the value use the following JSON schema.

* `{"ENV0_ENVIRONMENT_NAME":<environment name>, "output": <output name>}`
* `{"ENV0_WORKFLOW_PARENT":<parent name>, "output": <output name>}`

For more information, check out the [Import Variable Plugin git repository](https://github.com/env0/env0-import-variable-plugin).

## Requirements

To use this plugin, you need to setup the env zero API key and secret for the environment.  You can use an [Organization API Key](https://github.com/env0/env0-import-variable-plugin#:~:text=Organization%20API%20Keys) or a [Personal API Key](/api-reference/credentials/create-api-key).

1. `ENV0_API_KEY` (**Required**)
2. `ENV0_API_SECRET` (**Required**)

## Usage

Add the following `env0.yaml` custom flow file to your environment or project.

```yaml  theme={null}
version: 2  
deploy:  
  steps:  
    terraformPlan:  
      before:  
        - name: Import Variables
          use: https://github.com/env0/env0-import-variable-plugin@0.4.3
```

1. Configure the Custom Flow above with a new environment or an existing environment
2. Add a Terraform Variable
3. The Key is the name of your Terraform variable
4. The Value is a *reference* to another environment's output variable.  With the following format:  `${env0:<env0_environment_id>:<output_key>}`
5. Run the environment, and env zero will fetch the value

## Workflows

<Note>
  The workflow syntax below (`${env0-workflow:...}`) is specific to this plugin. If you are using the native Environment Outputs feature, you do not need this plugin or this syntax. See [Passing Outputs Between Sub-Environments](/guides/admin-guide/variables/workflow-variables#passing-outputs-between-sub-environments) for the UI-based approach.
</Note>

When using the plugin within a workflow you can use the following notation:

string types: `${env0-workflow:<parent name>:<output name>}`\
json types: `{"ENV0_WORKFLOW_PARENT":<parent name>, "output": <output name>}`

In this case, the parent name is the yaml parent, not the "environment name."\
For example, given the following env0.workflow\.yaml the variable structure to fetch the "vpc-id" from the "parent vpc" would be `${env0-workflow:vpc:vpc-id}` Similarly, to fetch the tags (in json) from the vpc: `{"ENV0_WORKFLOW_PARENT":vpc, "output": tags}`

```yaml env0.workflow.yaml theme={null}
environments:  
  vpc:  
    name: 'My VPC'  
    templateName: 'vpc-template'  
  subnet:  
    name: 'My Subnets'  
    templateName: 'subnet-template'  
    needs:  
      - vpc
```

## Environment Name Restrictions

* Environment Names must be unique, otherwise, the script just uses the "first" matching environment name.
* Environment Names must not include spaces " " or slashes `/`. Ideally, your environment only contains alphanumeric characters and dashes `-`. \*\*

## Inputs

N/A

## Example Usage

In this example we will run fetch the variable from a "Dev VPC" environment.

```yaml  theme={null}
version: 2
deploy:
  steps:
    terraformPlan:  
      before:
        - name: Import Variables # The name that will be presented in the UI for this step
          use: https://github.com/env0/env0-import-variable-plugin@0.4.3
          inputs: {}

```

1. Configure the Custom Flow above with a new environment or an existing environment
2. Add a Terraform Variable
3. The `Key` is the name of your Terraform variable
4. The `Value` is a *reference* to another environment's output variable.  For example, if I needed the VPC ID from my "Dev VPC" Environment:

* First I need to get the ENV0\_ENVIRONMENT\_ID from that environment.\
  note: the Environment ID can be found in the URL: `https://app.env0.com/p/7320dd7a-4822-426c-84b5-62ddd8be0799/environments/9cec1eb6-c17f-4cca-9cdf-606a23cdf6b5` where `9cec1eb6-c17f-4cca-9cdf-606a23cdf6b5` is the ENV0\_ENVIRONMENT\_ID.
* Find the output name in the environment Resources tab.  e.g. `vpc_id`
* The value you enter would be then: `${env0:9cec1eb6-c17f-4cca-9cdf-606a23cdf6b5:vpc_id}`

1. Run the environment, and env zero will fetch the value

## Further Reading

This plugin takes advantage of [Terraform variable precendence](https://developer.hashicorp.com/terraform/language/values/variables#variable-definition-precedence) and \*.auto.tfvars.

\*\* If you must know why, it's because this script is written in Bash, and I'm taking advantage of Bash arrays which doesn't process spaces well, and also I'm saving the outputs to the filesystem which gets confused with slashes.

Built with [Mintlify](https://mintlify.com).
