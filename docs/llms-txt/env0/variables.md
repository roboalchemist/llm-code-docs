# Source: https://docs.envzero.com/guides/admin-guide/variables.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing Variables

> Configure Terraform variables and environment variables across scopes in env zero deployments

## Terraform Variables and Environment Variables

Using an infrastructure-as-code model, variables are used to customize certain aspects of a configuration for a specific deployment, without having to change the code. In this way, a single configuration can be used in different contexts to create different deployments.

Variables can be anything from ports and IPs to cloud credentials, availability zones, and images.

env zero supports two types of variables:

* Terraform Variables (also called Input Variables) - These are defined in the Terraform configuration files. Their values are set by env zero when running IaC commands.
* Environment Variables - These are set by env zero in the shell running IaC commands and [Custom Flows](/guides/admin-guide/custom-flows).

<Info>
  **Built-in Terraform/Terragrunt Environment Variables Support**

  Terraform and Terragrunt support various environment variables to alter the behavior of the deployment. You can add those as environment variables inside the env zero platform as well, under name and the appropriate value.

  See all the supported [Terraform environment variables](https://www.terraform.io/cli/config/environment-variables#environment-variables) and the relevant [Terragrunt environment variables](https://terragrunt.gruntwork.io/docs/reference/cli-options/#cli-options).

  For example:\
  If you wish to perform a state migration you can add the `TF_CLI_ARGS_init` environment variable and as a value by adding `-migrate-state`.\
  You can read more about `TF_CLI_ARGS` [here](https://www.terraform.io/cli/config/environment-variables#tf_cli_args-and-tf_cli_args_name).
</Info>

Terraform Variables and Environment Variables are both managed by the user in env zero.

## Variables and Scopes in env zero

env zero uses hierarchical scopes to manage variables (both Terraform Variables and Environment Variables). You can set variables for an Organization, a Template, a Project, or a specific Environment.

Each scope inherits the variables defined in the higher scopes. Hence, a template will have all the variables that are set for the organization. A project will have all the variables that are set for the organization, or any parent projects it has. And a new Environment will have all the variables that are set for the project, template, and organization.

You can change the value of a variable inherited from a higher scope, but not its name.

The different variable scopes reflect the fact that variables are used for different purposes and might be set by different people.

<Note>
  **Example**

* An administrator sets cloud credentials in the Organization scope to apply to all the environments managed in an organization.

* A DevOps engineer creates a new template. They want to have the option for the user to select from two different machine sizes. Therefore they use the same Terraform configuration, with the instance type set as a variable, and create two templates, each with a different value for the instance size variable.

* A developer creates a new environment. They don't need to know the credentials, or set the sizes of instances. They choose a template and let env zero use the variables defined in the higher scopes. They can, however, still make further customizations by overriding a Terraform Variable which specifies which port to use.
</Note>

## Variables Value Types

The env zero platform supports several value types of variables:

### Free Text

This is the most-common variable value type that holds a plain text value. To accommodate your variable with a value, simply type your desired text or leave it blank. This value type also supports setting it as [secrets](/guides/admin-guide/variables/#secrets).

### HCL Format

This type allows you to define complex terraform values, similar to what can you define in the `.tf` file\
We support all complex [terraform types](https://www.terraform.io/language/expressions/types#types-and-values).\
This format is only available under **Terraform Variables** section.

Examples for HCL values:

<CodeGroup>
  ```hcl Object theme={null}
  {
    name = "John"
    age  = 52
  }
  ```

  ```hcl Array theme={null}
  [
    "value1", 
    "value2"
  ]
  ```

  ```hcl Compound theme={null}
  {
    objects_list = [
      {
        first_field  = "value1"
        second_field = "value2"
      },
      {
        first_field  = "value1"
        second_field = "value2"
    }]
  }
  ```

</CodeGroup>

### JSON Format

This type allows you to define complex terraform values such as JSON format.\
We support all complex [terraform types](https://www.terraform.io/language/expressions/types#types-and-values).\
This format is only available under the Terraform Variables section.

Examples for JSON values:

```json  theme={null}
{
  "list_of_stuff": [
    { "some_field": "value", "other_field": "other value" },
    { "something": "value1", "something_else": "value2" }
  ]
}
```

### Dropdown List

This is a variable value that is configured with a predefined set of options that you can select as a value. This allows you to govern your specific variable with a dropdown of available options that any other organization or user can select from. Dropdown List variables can be re-selected in lesser scopes but can be configured (aka add/remove options) only in their original scope.

To add/remove options of a Dropdown List variable:

1. Add a new Dropdown List variable.
2. Click on its value input and a new select dropdown will be opened.
3. To add an option, type the desired option and click + Add Option button on the opened select's footer.
4. To remove an existing option,click the Trash icon next to the relevant option.
5. Don't forget to hit the save button to commit your changes.

<img src="https://mintcdn.com/envzero-b61043c8/pcx_nh6zT3at7dYL/images/guides/admin-guide/2709a2f-screen_shot_2020-11-05_at_17.png?fit=max&auto=format&n=pcx_nh6zT3at7dYL&q=85&s=c292819030947f7179f70d48a62e1203" alt="" width="588" height="241" data-path="images/guides/admin-guide/2709a2f-screen_shot_2020-11-05_at_17.png" />

## Variable Settings

You can configure advanced settings for every variable in our system by opening the advanced settings form -\
The rightmost icon in the variable line.

### Required Variable

This setting means that you can't start deployment without first setting a value for this variable.

In higher scopes (Organization, Template, Project), "Required" variables can be set without a value. The user will be required to enter a value before a deployment.

### Read Only Variable

This setting means you locked this variable for all lower scopes. When configured, none of the lower scopes can override it.

Here's a good example of using this setting: When the organization admin wants to enforce using the same stage and identifier for all environments in the organization, the admin can enable it and no one can override it or delete it.

### Regular Expression Validation (only for Free Text variables)

You can define a regular expression that value should match. If you set the regular expression in upper scope, you can keep the value empty - the validation will be enforced in lower scope.

### Variables Description

Variables have an optional description that is editable only at the scope in which they are created, and viewable in lower scopes. Unlike values, the description cannot be overridden.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/noVHY1C-wdNQ4iZn/images/guides/admin-guide/variables_description_interface.gif?s=b77c3efbb736a1c0c3d36f4635c758bb" alt="Variables description interface" width="1597" height="452" data-path="images/guides/admin-guide/variables_description_interface.gif" />
</Frame>

## Load Variables From Terraform Code

On a Terraform Variables scope, clicking on Load Variables From Code will load the variables from your Terraform code directory. All will be at default values.

Note that loaded variables will not be saved until the Save button is clicked, and only string-type variables will be loaded, as is generally done in Terraform Variables.

<Tip>
  **Complex value**

  All the default complex values will be loaded by env zero  JSON format. You will be able to edit them as JSON files.
</Tip>

<img src="https://mintcdn.com/envzero-b61043c8/pcx_nh6zT3at7dYL/images/guides/admin-guide/4a2ecce-screen_shot_2021-11-23_at_13.png?fit=max&auto=format&n=pcx_nh6zT3at7dYL&q=85&s=2f189e4d640b38819e4cb861c0d469ee" alt="" width="1376" height="358" data-path="images/guides/admin-guide/4a2ecce-screen_shot_2021-11-23_at_13.png" />

## Secrets

For security reasons, some variables needed for flow execution should not be exposed to user executing flows. This is known as Secrets Management. The most common use case for secrets management is cloud credentials.

In env zero, secrets are variables that are marked as sensitive. A sensitive variable has its value masked after you save it. If you'd like to change an existing sensitive variable, simply click on the masked value to clear it, type in the new secret value, and then click save.

Like other variables, secrets are inherited and can be defined in any scope.

<Info>
  **Secrets in a Self-Hosted Agent**

  If your organization manages self-hosted agents, you can control whether users are allowed to store sensitive data within env zero by the [policy](/guides/policies-governance/allow-env0-secrets).

  Additionally, you can reference a variable from an external secret manager in one of the following ways:

  1. [AWS Secret Manager](https://aws.amazon.com/secrets-manager/)
  2. [GCP Secret Manager](https://cloud.google.com/secret-manager)
  3. [Azure Key Vault](https://azure.microsoft.com/en-us/services/key-vault/)
  4. [HashiCorp Vault](https://www.vaultproject.io/)
  5. [OCI Vault](https://docs.oracle.com/en-us/iaas/Content/KeyManagement/home.htm)

  You can read more on how to configure it [here](/guides/admin-guide/self-hosted-kubernetes-agent/#sensitive-secrets)  <img src="https://mintcdn.com/envzero-b61043c8/BZYthPtvpSdQtcKJ/images/guides/admin-guide/0cf2d536fe81d6cfa0fdab855d5d24280ba6273b1fdfdc5c55e343a946aadd26-image.png?fit=max&auto=format&n=BZYthPtvpSdQtcKJ&q=85&s=858a79a3f453585ed888ee38422fb018" alt="" width="1386" height="77" data-path="images/guides/admin-guide/0cf2d536fe81d6cfa0fdab855d5d24280ba6273b1fdfdc5c55e343a946aadd26-image.png" />
</Info>

## Manage Variables

To manage variables at the organization scope, select the Variables tab on the main screen. This shows a list of the organization's Environment Variables and Terraform Variables. You can edit their names or values, and add new ones.

Don't forget to save any changes before leaving the page, or they will be lost.

To manage variables at the Template level, go to the Template tab and select the template you are interested in. Click Settings, then select the Variable tab. Here you can modify variables for the template.

At the environment level, you can set the variables just before deployment. When you create a new environment or redeploy, you’ll get a pop-up with environment details to fill in. Select the Variable section and modify the variables for that specific environment.

For an environment that already exists, you edit the variables settings by redeploying (or queuing) a new deployment or under the Variables section (the latter can only be done if the environment has no running deployment).

<Note>
  **Note**

* Changes to variables in a higher scope will change the variables in all inheriting scopes.

* Changes to variables in an existing environment will not take effect until the environment is redeployed.  When env zero runs a deployment, it stores the variable names to be used in undeploy so changes for an Active environment will not affect the destroy process.

* If a user does not have the RUN APPLY permission (like in the Planner project role), any variable changes they make when running a plan, will only be saved to the environment if the plan is approved. If the plan is canceled or the deployment fails, the proposed variable changes will not be saved. For a user with RUN APPLY permission, changes will be saved once the deployment is queued.
</Note>

## Variable Precedence

When using a combination of `TF_VAR_*` and `ENV0_TERRAFORM_CONFIG_FILE_PATH` option as described [here](/guides/admin-guide/additional-controls/#custom-terraform-variables-file), and with Terraform Variables in the UI, you might wonder which variable will actually be used.

env zero's Terraform Variables (created in the UI) are actually loaded into an `env0.auto.tfvars.json` file during run-time and `ENV0_TERRAFORM_CONFIG_FILE_PATH` uses the `-var-file` flag for plan and apply.

With this information, along with the [Variable Definition Precedence](https://opentofu.org/docs/language/values/variables/#variable-definition-precedence), essentially this will be the order of precedence, with later sources taking precedence over earlier ones:

* Environment Variables: `TF_VAR_*`
* env zero UI Terraform Variables: `env0.auto.tfvars.json`
* variable files specified through `ENV0_TERRAFORM_CONFIG_FILE_PATH`

If you also use Custom Flow to manage variables, then you could create your own `auto.tfvars` and make sure it is named **alphabetically** ahead or behind `env0.auto.tfvars.json` if you want your values to get overwritten by env zero or override env zero, respectively. For example, if you created a file `acme.auto.tfvars.json`, variables would get overwritten by env zero's UI tf vars.

## Ansible Variables

Currently, there's no way to set Ansible variables via the UI.\
However, you can set Ansible variables by setting any environment variable prefixed by `ANSIBLE_VAR_`.

Any variable added to that prefixed would be parsed and added to the `--extra-vars` flag.

More about it [here](/guides/admin-guide/templates/ansible/#setting-extra-variables).

<Info>
  📝 Additional Content

* [Managing Terraform variable hierarchy](https://www.env0.com/blog/managing-terraform-variable-hierarchy)
* [Why env zero is a Terraform Cloud alternative?](https://www.env0.com/alternatives/terraform-cloud-alternative)
</Info>

Built with [Mintlify](https://mintlify.com).
