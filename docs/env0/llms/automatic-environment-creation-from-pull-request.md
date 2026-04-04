# Source: https://docs.envzero.com/guides/admin-guide/environment-discovery/automatic-environment-creation-from-pull-request.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Auto-Creating Environments from Pull Requests

> Automatically create and destroy environments from pull requests using directory-based discovery in env zero

Manual environment creation and deployment can become tedious and error-prone at scale. env zero enables you to automatically create and destroy environments from pull requests. This leverages a preconfigured directory structure to streamline your workflow, save time, and reduce errors.

In order to enable this capability, follow the steps below:

### Get started

In this example, we will create a `Terragrunt` configuration based on [Terragrunt Infrastructure Example](https://github.com/env0/terragrunt-infrastructure-example) repository.

First things first, you will need to create a one time configuration of your discovery settings. This is a per Project configuration.

Under `Project Settings` select `Environment Discovery` tab. To continue, click `Get Started`.

<img src="https://mintcdn.com/envzero-b61043c8/T2JW_alZSK9mPIUs/images/guides/admin-guide/environment-discovery/c5f4b7ffb0f9255c67f22ba290f3a1f40a03160ab84f4430ec05f408b2a3d8d3-image.png?fit=max&auto=format&n=T2JW_alZSK9mPIUs&q=85&s=5be1954db2e4e50e21c58b750cc6b0ac" alt="" width="1914" height="922" data-path="images/guides/admin-guide/environment-discovery/c5f4b7ffb0f9255c67f22ba290f3a1f40a03160ab84f4430ec05f408b2a3d8d3-image.png" />

### Choose The Infrastructure

As with setting up a [Template](/guides/admin-guide/templates), choose the type of infrastructure you are using, then click `Next`.

<img src="https://mintcdn.com/envzero-b61043c8/pcx_nh6zT3at7dYL/images/guides/admin-guide/environment-discovery/63c5faff53a352405c0d8d6710070ed5f92274c8d5d60fa58a0bdde73e2dc287-image.png?fit=max&auto=format&n=pcx_nh6zT3at7dYL&q=85&s=b5de6bc9bb866faa1aada1cdae2d0f7d" alt="" width="1913" height="924" data-path="images/guides/admin-guide/environment-discovery/63c5faff53a352405c0d8d6710070ed5f92274c8d5d60fa58a0bdde73e2dc287-image.png" />

### Configure Your Repository

Next, choose the desired Git provider, and configure the repository you would like to discover from and click `Next`

<img src="https://mintcdn.com/envzero-b61043c8/pcx_nh6zT3at7dYL/images/guides/admin-guide/environment-discovery/471ed7af0a1083d6e74ef19e4d955314a4b2a528eff86b4cb55ec1e5cc4773db-image.png?fit=max&auto=format&n=pcx_nh6zT3at7dYL&q=85&s=f916b0b95ebbec236747fc8f5a215e64" alt="" width="1908" height="925" data-path="images/guides/admin-guide/environment-discovery/471ed7af0a1083d6e74ef19e4d955314a4b2a528eff86b4cb55ec1e5cc4773db-image.png" />

### Configure the Environment Mapping

The final step is crucial as it defines the structure of your project. In this section, you will specify the layout of your project, including which Environments will be created, how they will be named, and where they will be located within env zero

<img src="https://mintcdn.com/envzero-b61043c8/T2JW_alZSK9mPIUs/images/guides/admin-guide/environment-discovery/97ecd06fce39e75c60b12605eb2ed07599baed14c96c1712d07fc925ccbb3742-image.png?fit=max&auto=format&n=T2JW_alZSK9mPIUs&q=85&s=ca6b6b4208a6f91bf923d7db4a37661c" alt="" width="1906" height="927" data-path="images/guides/admin-guide/environment-discovery/97ecd06fce39e75c60b12605eb2ed07599baed14c96c1712d07fc925ccbb3742-image.png" />

Let's break it down step by step:

#### Match Environments Glob

You will need to define your project structure using a multi-glob pattern. Any match to this pattern will trigger the creation and planning of an environment in env zero. In this example, we aim to create an env zero Environment for any `terragrunt.hcl` file that is not located under the `_envcommon` folder

<img src="https://mintcdn.com/envzero-b61043c8/T2JW_alZSK9mPIUs/images/guides/admin-guide/environment-discovery/7536e4f-image.png?fit=max&auto=format&n=T2JW_alZSK9mPIUs&q=85&s=794d03a227d7ea0a7d6c16045a3018bc" alt="" width="654" height="65" data-path="images/guides/admin-guide/environment-discovery/7536e4f-image.png" />

<Info>
  **[Glob pattern](https://en.wikipedia.org/wiki/Glob_\(programming\))**

  Glob patterns specify sets of filenames with wildcard characters. For example, `\*.tf` or `prod/\*\*`

  For example, you can configure pattern like `src/prod/**/*.tf`\
  In this case, we will create new env zero Environments only if the new `main.tf` is located under `src/prod/...`

  We also support extglob patterns with that you can write pattern which ignores files or use a list of folders.\
  Note that for extglob, when using OR/AND statements, make sure to wrap each option with parentheses, for example:

* `!(prod/us-east-1/\*\*)+(dev/us-east-1/**|dev/us-west-2/main.tf)`\
    This means we will listen to any change in `dev/us-east-1` and `dev/us-west-2/main.tf`, and ignore changes under `prod/us-east-1`. (Recommend including exclusions first.)
* `+(Terraform/!(prod)**|Terragrunt/dev/**)`\
    Listen for any changes in `Terraform` or `Terragrunt/dev` but ignore any changes in `Terraform/prod`
</Info>

#### Root Path

The root path configuration defines the starting point from which env zero will generate environments. For instance, if the glob pattern is set to `src/prod/storage/*_/_.tf`, and the discovered file is `src/prod/storage/environment0/main.tf`, with the root path configured as `src/prod`, env zero will exclude the root path from the full path of the discovered `main.tf` file. Therefore, it will be treated as `storage/environment0/main.tf` when determining where to place the environment.

#### Environment Placement

This section will let you choose the Environment placement strategy within your project.

<img src="https://mintcdn.com/envzero-b61043c8/pcx_nh6zT3at7dYL/images/guides/admin-guide/environment-discovery/31c796d-image.png?fit=max&auto=format&n=pcx_nh6zT3at7dYL&q=85&s=2e037777d91d0dc572b647d8f0bc68b0" alt="" width="1269" height="205" data-path="images/guides/admin-guide/environment-discovery/31c796d-image.png" />

Let's consider a env zero Project hierarchy of

```
- environment-discovery
- - prod
- - non-prod
```

**Create Environments in this project** - Will not consider Sub-Projects when creating the environments. In our case, a PR to change `prod/us-east-1/prod/mysql` will create an Environment called `us-east-1/prod/mysql`

**Create Environments in the closest matching Sub-Project path, matching the directory path** - Will consider the closest Sub-Project to match the path, for example a PR to change `prod/us-east-1/prod/mysql` will create an Environment called `us-east-1/prod/mysql` on `prod` Sub-Project

Click `Done` and you should be greeted with the success screen if all went well. The discovery process will be started automatically but automatic Pull Request creation should be enabled in the settings section.

### Enabling Automatic Pull Request Creation

<img src="https://mintcdn.com/envzero-b61043c8/pcx_nh6zT3at7dYL/images/guides/admin-guide/environment-discovery/3be798b033f7d00daf5e341f06b8bfd2b62f014a39a90a10ff57f8f13b6bb84f-image.png?fit=max&auto=format&n=pcx_nh6zT3at7dYL&q=85&s=c08aef18afb2dbf3f3f90bb63f11f7a9" alt="" width="1908" height="930" data-path="images/guides/admin-guide/environment-discovery/3be798b033f7d00daf5e341f06b8bfd2b62f014a39a90a10ff57f8f13b6bb84f-image.png" />

#### Workspace Naming

Here we can choose to either use `default` as the workspace names or derive it from the Environment's name

#### Deploy Discovered Environments on

In the next section, you'll be able to set the [Continuous Deployment](/guides/admin-guide/environments/continuous-deployment) and [PR Plan](/guides/admin-guide/environments/plan-on-pull-request) settings which your Environments will be created with.

<img src="https://mintcdn.com/envzero-b61043c8/T2JW_alZSK9mPIUs/images/guides/admin-guide/environment-discovery/8f07d17-image.png?fit=max&auto=format&n=T2JW_alZSK9mPIUs&q=85&s=61c48d03a983a669583c24cccc9e4f8d" alt="" width="743" height="178" data-path="images/guides/admin-guide/environment-discovery/8f07d17-image.png" />

**Changes on Template Directory files** - The Environment will only plan / deploy on changes to the directory matched by the main glob pattern

**Changes by file filter pattern** - The Environment will plan / deploy on changes matching the given multi glob pattern.

<Tip>
  Custom Glob Variables

  We also support using custom string templates that are set during runtime -

* `env0_template_dir_path` - The entire template path.
* `env0_template_dir_name` - The **name** of the directory of the template files.
* `env0_template_dir_ancestors` - Will be interpolated with each ancestor directory up the template path, and is meant to be used in an extended glob expression. It is most useful for picking up configuration files up the path, like in a Terragrunt style repository. *\*\* NOTE: this should NOT be used with a file extension\
    e.g: If the template directory is `non-prod/us-east-1/dev/postgres`, then it will be interpolated as \`non-prod/*|non-prod/us-east-1/*|non-prod/us-east-1/dev/*|non-prod/us-east-1/dev/postgres/\*\`.

  example usage:\
  `+((_envcommon/${env0_template_dir_name}/**)|(${env0_template_dir_path}/**)|${env0_template_dir_ancestors})` which means match everything under the path defined in the environment's template and match any changes under `_envcommon` matching the template dir name, and any files changes in the ancestors (or parent) folders.
</Tip>

<Warning>
  Heads Up

  In case the even that the environment creation glob and the environment CD / PR plan glob do not match, it is possible that the changes that trigger the Environment creation won't trigger the initial PR Plan (see section below for more info)
</Warning>

In our example, we would like other changes to trigger a plan, and not only those under the Template Directory.

**That's it, you're all set.**

## Using Environment Discovery

After configured, using environment discovery is easy as opening and merging a pull request.

1. Create a branch with desired changes and open a PR.

<Frame caption="a PR Plan has started on env0">
  <img src="https://mintcdn.com/envzero-b61043c8/T2JW_alZSK9mPIUs/images/guides/admin-guide/environment-discovery/a_pr_plan_has_started_on_env0.png?fit=max&auto=format&n=T2JW_alZSK9mPIUs&q=85&s=dbcb152a3e5a7dbbec1044c11ed1d2ad" alt="a PR Plan has started on env0" width="1384" height="935" data-path="images/guides/admin-guide/environment-discovery/a_pr_plan_has_started_on_env0.png" />
</Frame>

1. Navigate to the relevant Project or Sub-Project in env zero or click the env zero bot comment (Remember: multiple environments can be created via a single PR)

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/pcx_nh6zT3at7dYL/images/guides/admin-guide/environment-discovery/4171ddd-proj_desc_1_fix.png?fit=max&auto=format&n=pcx_nh6zT3at7dYL&q=85&s=17687e246abfba690e0097a3bdbb381e" alt="Interface screenshot showing configuration options" width="1346" height="499" data-path="images/guides/admin-guide/environment-discovery/4171ddd-proj_desc_1_fix.png" />
</Frame>

1. In the `Deployments` tab, you'll be able to see the initial PR Plan env zero ran on your code.

<Frame caption="A real world example of multiple iteration on a failed PR">
  <img src="https://mintcdn.com/envzero-b61043c8/T2JW_alZSK9mPIUs/images/guides/admin-guide/environment-discovery/a_real_world_example_of_multiple_iteration_on_a_failed_pr.png?fit=max&auto=format&n=T2JW_alZSK9mPIUs&q=85&s=0be356f3dd0593477f78d906c7581fe1" alt="A real world example of multiple iteration on a failed PR" width="1320" height="787" data-path="images/guides/admin-guide/environment-discovery/a_real_world_example_of_multiple_iteration_on_a_failed_pr.png" />
</Frame>

<Warning>
  Closing a PR

  Closing a PR will archive the `Never Deployed` Environment. Note, that for Bitbucket Cloud and Bitbucket Server automatic archival is not supported, and you will have to do so manually.
</Warning>

1. After the plan has been reviewed and merged, env zero will trigger a deployment for that Environment.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/T2JW_alZSK9mPIUs/images/guides/admin-guide/environment-discovery/d2d8971-proj_desc_3_fix.png?fit=max&auto=format&n=T2JW_alZSK9mPIUs&q=85&s=f043c73e3231a2f3d275c83f1e8e745b" alt="Interface screenshot showing configuration options" width="1336" height="772" data-path="images/guides/admin-guide/environment-discovery/d2d8971-proj_desc_3_fix.png" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/T2JW_alZSK9mPIUs/images/guides/admin-guide/environment-discovery/d2d8971-proj_desc_3_fix.png?fit=max&auto=format&n=T2JW_alZSK9mPIUs&q=85&s=f043c73e3231a2f3d275c83f1e8e745b" alt="Interface screenshot showing configuration options" width="1336" height="772" data-path="images/guides/admin-guide/environment-discovery/d2d8971-proj_desc_3_fix.png" />
</Frame>

Built with [Mintlify](https://mintlify.com).
