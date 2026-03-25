# Source: https://docs.envzero.com/guides/admin-guide/environments/setting-up-a-new-environment.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Creating a New Environment

> Create a new env zero environment using a pre-defined template or direct VCS integration

env zero provides two approaches for creating a new environment:

1. Based on a pre-defined [Template](/guides/admin-guide/templates)
2. Based on a direct VCS integration

env zero Templates can be very useful as they allow reusability and RBAC, however in some cases you may want to simply connect to your VCS directly without using Templates to avoid unnecessary complexity.

Both approaches will result in a complete env zero environment with all of the available features so you can choose the approach that most fits your style and use case.

<Info>
  **Permissions**

  If you are a *project planner* - you must select a template for the new environment.

  If you are an *organization admin* - you will be prompted to select between **Template** / **VCS**.

  To enable Environment creation based on VCS integration for non organization admins, create an Organization Role with the **Create & Edit Templates** permission. Users may have to log out and log back in to deploy see the modal to deploy an Environment without a Template.
  Organization -> Settings -> Roles -> (Create or update an existing role with the permission)
</Info>

To create a new environment, all you have to do is choose a specific *Project* and click on the **CREATE NEW ENVIRONMENT** button (located in the top right corner).

<img src="https://mintcdn.com/envzero-b61043c8/T2JW_alZSK9mPIUs/images/guides/admin-guide/environments/3330de8-screen_shot_2022-04-20_at_16.png?fit=max&auto=format&n=T2JW_alZSK9mPIUs&q=85&s=3967a9d011472dd7dcaec15537f94eb5" alt="" width="701" height="483" data-path="images/guides/admin-guide/environments/3330de8-screen_shot_2022-04-20_at_16.png" />

## Based On a Pre-defined Template

This choice is great for you if you want to use env zero templates with all of their benefits.

To run an environment based on a pre-defined template, follow these short instructions:

1. Select your desired [Template](/guides/admin-guide/templates).
2. Set environment details: environment name, workspace name (optional - only for Terraform), [Time To Live (TTL)](/guides/policies-governance/policy-ttl) , [Variables](/guides/admin-guide/variables) and [Terragrunt Working Directory](/guides/admin-guide/environments/#terragrunt-working-directory) (only refers to Terragrunt Templates, optional).

## Based On a Direct VCS Integration

This choice is great for you if you don't want to overwhelm yourself with env zero templates - just connect to your VCS and deploy.

To run an environment based on a direct VCS integration, follow these short instructions:

Select one of the many supported IaC types.

<img src="https://mintcdn.com/envzero-b61043c8/T2JW_alZSK9mPIUs/images/guides/admin-guide/environments/7b5f5e3-image.png?fit=max&auto=format&n=T2JW_alZSK9mPIUs&q=85&s=11f604e20fbda2d5590083bbf7fb0d3d" alt="" width="1417" height="391" data-path="images/guides/admin-guide/environments/7b5f5e3-image.png" />

Select one of the many supported Git repositories.

<img src="https://mintcdn.com/envzero-b61043c8/T2JW_alZSK9mPIUs/images/guides/admin-guide/environments/0f48f43-2022.png?fit=max&auto=format&n=T2JW_alZSK9mPIUs&q=85&s=a4ae511e9ccd8e326ae6a01fb2a4be59" alt="" width="2740" height="568" data-path="images/guides/admin-guide/environments/0f48f43-2022.png" />

Once a Git repository has been selected a new window will load, asking you to authenticate to that git account.  This will install the Env0 application as a trusted source to read/write to your chosen repositories.

<img src="https://mintcdn.com/envzero-b61043c8/RwbdEslsc74czQBG/images/guides/admin-guide/environments/aec2cb5-2022.png?fit=max&auto=format&n=RwbdEslsc74czQBG&q=85&s=146280bcf2894777a15f4eb39039d996" alt="" width="497" height="370" data-path="images/guides/admin-guide/environments/aec2cb5-2022.png" />

Add any Terraform or environmental variables you may want on the next screen.

Set the environment details and options.

<img src="https://mintcdn.com/envzero-b61043c8/T2JW_alZSK9mPIUs/images/guides/admin-guide/environments/62d4666-2022.png?fit=max&auto=format&n=T2JW_alZSK9mPIUs&q=85&s=1bc214d731f465cb214e46222c86573f" alt="" width="2744" height="744" data-path="images/guides/admin-guide/environments/62d4666-2022.png" />

Click done to complete the environment creation and run your first deployment.

<Tip>
  **Import existing environment (for Terraform only)**

  You may import an existing Terraform environment by specifying the *Workspace Name*
</Tip>

<Info>
  **Auto deploying created Environment**

  The default behavior in env zero is to automatically deploy a created environment.

  In case you would like to create the environment without deploying, you can use the [create environment API](/api-reference/environments/create-environment) and set the `preventAutoDeploy` param to `true`.

  This is also supported in our [Terraform Provider](https://registry.terraform.io/providers/env0/env0/latest/docs/resources/environment)
</Info>

Built with [Mintlify](https://mintlify.com).
