# Source: https://docs.envzero.com/guides/admin-guide/remote-backend/state-migration.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Migrating State

> Migrate Terraform state to or from env zero remote backend, including from TFC, S3, and other backends

For State Migration to work, please make sure the following conditions are met:

* if you're migrating the state from another Remote Backend, make sure you are logged in to the previous Remote Backend
* Terraform is configured to run with the current backend - this can be done by running `terraform init` (this is needed for Terraform to detect the changes in the Backend configuration)
* You're [logged in](/guides/admin-guide/remote-backend/login/#login-to-env-zero-remote-backend) to the env zero Remote Backend
* You have your *Organization ID* and your *Project ID*

Migrating the state is fairly simple. All you have to do is:

1. Configure the Remote Backend in your Terraform code:

```hcl  theme={null}
terraform {
  cloud {
    hostname = "backend.api.env0.com"
    organization = "<YOUR_ORGANIZATION_ID>.<YOUR_PROJECT_ID>"

    workspaces {
      name = "<YOUR_WORKSPACE_NAME>"
    }
  }
}
```

1. Run:

```bash terraform theme={null}
terraform init -migrate-state -force-copy
```

```bash opentofu theme={null}
tofu init -migrate-state -force-copy
```

That's it!

The migration results with:

* A new Environment in the given Project, its name is as the given Workspace Name
* The Environment's current state will be exactly like the current state of your previous Backend

<Note>
  **Insert Missing Definitions Into Your Generated Environment**

  Since Terraform sends limited data for creating the Environment, there are a few things the generated Environment and its matching Template are missing.

  The Environment is missing [Continuous Deployment configuration](/guides/admin-guide/environments/continuous-deployment).

  The Template is missing VCS configuration (repository, branch, terraform folder).

  We recommend filling in those missing definitions so you can deploy your Environment remotely in env zero and fully leverage all of the env zero capabilities and features.
</Note>

## Migrating from env zero local to env zero remote state

**Note:** env zero local refers to Tofu/Terraform code which has been deployed in env zero without any backend configuration, and the env zero remote backend disabled.

* Find the environment in which you want to migrate
* Ensure your Terraform version is 1.x or above
* Navigate to Settings, enable Use env zero Remote Backend, and save
* Use the burger menu in the top right and select Run a task
* In the bash command section type `terraform init -migrate-state -force-copy` or `tofu init -migrate-state -force-copy`, depending on your infrastructure. Then, click Run task.
* Redeploy the Environment to ensure no changes are seen.

## Migrating from TFC/TFE to env zero remote state

### Option 1: Migrating the workspace using the env zero migration script

The env zero migration tool allows migrating states from TFC, as well as the workspaces themselves, and other configuration from your TFC account.

The tool is open source and can be found here: [env zero migration tool](https://github.com/env0/env0-migration-tool/tree/main/TFC), to see the exact instructions.

### Option 2: Migrating the workspace using env zero

1. Update your TFC/TFE workspace settings from Execution mode to Local mode, and Save settings. Note: Before you change this setting, make a quick note of your variable configurations in TFC/E.\
   <img src="https://mintcdn.com/envzero-b61043c8/pvGFjFxaiqGDTFG3/images/guides/admin-guide/remote-backend/3388e13-cleanshot_2023-03-31_at_15.png?fit=max&auto=format&n=pvGFjFxaiqGDTFG3&q=85&s=28c011e3bfb383691168936e99cdc73f" alt="" width="729" height="247" data-path="images/guides/admin-guide/remote-backend/3388e13-cleanshot_2023-03-31_at_15.png" />
2. In TFC/TFE, go to User Profile and head over to User Settings. Select Tokens, then Create an API token and hit Save to save the token for the next step.
3. Ensure the API token has the correct privileges.  This typically means a User or Team token needs to be created, not an Organization token.
4. In env zero, create a new **env zero environment** (from VCS Environment)
   1. IaC Type: Terraform
   2. Under Advanced, Select the same Terraform Version used with TFC. Select **NEXT**\
      <img src="https://mintcdn.com/envzero-b61043c8/pvGFjFxaiqGDTFG3/images/guides/admin-guide/remote-backend/af936bb-cleanshot_2023-04-04_at_11.png?fit=max&auto=format&n=pvGFjFxaiqGDTFG3&q=85&s=64797ce7c4db537d4e027183508ba4ab" alt="" width="415" height="91" data-path="images/guides/admin-guide/remote-backend/af936bb-cleanshot_2023-04-04_at_11.png" />
   3. Under **VCS**: Select the same Git Repo, Branch (aka Revision), and Folder as configured for TFC/E. Select **NEXT**
   4. Under **Variables**: Add any [variables](/guides/admin-guide/variables) used in your TFC/E workspace.
   5. Add an environment variable: `TF_TOKEN_app_terraform_io` (or `TF_TOKEN_your_tfe_host` if you are using a custom hostname) and add the token created in step 3. This variable can be saved at the Organization or Project level if you are planning on migrating more than one workspace manually.\
      Note: This configuration only works for TF v. 1.2+
   6. Add an environment variable:`ENV0_SKIP_WORKSPACE=true` This setting will avoid the error `workspaces not supported` - when using TFC/E remote backend.
   7. Copy the existing workspace name you're using in TFC/E. e.g. my-prod-resource to the Environment Details - Workspace Name. Note: this is not the ws- ID, but the name you provided.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/pvGFjFxaiqGDTFG3/images/guides/admin-guide/remote-backend/9c3e037-cleanshot_2023-05-18_at_21.jpg?fit=max&auto=format&n=pvGFjFxaiqGDTFG3&q=85&s=dd5787e4bf9d21aa0c4159f808de64f8" alt="Interface screenshot showing configuration options" width="478" height="154" data-path="images/guides/admin-guide/remote-backend/9c3e037-cleanshot_2023-05-18_at_21.jpg" />
</Frame>

1. Do NOT select Use env zero remote Backend – we will do this later.
2. **Run** the environment. You should expect to see no changes (assuming you've made no other changes to the code or variables); TFC/E
3. Update the Remote Backend to use env zero's remote backend and then push the code to Git.  This may start a new deployment.
4. Your Organization ID can be found under Organization Settings.\
   You may receive a Deploy Failed (Error: Backend configuration changed) error which is to be expected. We will fix this in the next step.

```hcl  theme={null}
  cloud {
    hostname = "backend.api.env0.com"
    organization = "<YOUR_ORGANIZATION_ID>.<YOUR_PROJECT_ID>"
    workspaces {
      name = "my-prod-resource"
    }
  }
```

1. Under **Environment > Settings**: **Check** "Use env zero remote Backend" and "**SAVE**"

<img src="https://mintcdn.com/envzero-b61043c8/pvGFjFxaiqGDTFG3/images/guides/admin-guide/remote-backend/1acafe0-cleanshot_2023-03-30_at_13.png?fit=max&auto=format&n=pvGFjFxaiqGDTFG3&q=85&s=cad7438c6b79de67ef848d2336649e16" alt="" width="761" height="223" data-path="images/guides/admin-guide/remote-backend/1acafe0-cleanshot_2023-03-30_at_13.png" />

1. **Re-deploy** with the following Environment Variables:

* Add `TF_CLI_ARGS_init=-migrate-state -force-copy`
* Delete `ENV0_SKIP_WORKSPACE=true`

1. Your deployment logs under Terraform Init should show this or a similar message:

<Info>
  **Backend configuration changed!**

  Terraform has detected that the configuration specified for the backend has changed. Terraform will now check for existing state in the backends.

  Successfully configured the backend "remote"! Terraform will automatically use this backend unless the backend configuration changes.
</Info>

1. **(Optional)** Redeploy and remove the `TF_TOKEN_app_terraform_io/TF_TOKEN_your_tfe_host` and `TF_CLI_ARGS_init` to clean up.
2. **(Optional)** The `backend remote` block can be removed if you are not using the remote plan feature.
3. **Your migration is now complete!** 🎉

### Option 2: Migrating the workspace using a local terminal/script

See the [env zero migration tool](https://github.com/env0/env0-migration-tool).

## Migrating from env zero remote backend to a third-party bucket

1. Add the remote backend code block to the environment you want to migrate.

```hcl  theme={null}
terraform {
  cloud {
    hostname = "backend.api.env0.com"
    organization = "<YOUR_ORGANIZATION_ID>.<YOUR_PROJECT_ID>"

    workspaces {
      name = "<YOUR_WORKSPACE_NAME>"
    }
  }
}
```

1. Remote login to env zero:
   1. Run `terraform login backend.api.env0.com`
   2. Enter `yes` when prompted
   3. Insert your `token` (See [Generating a Token](/guides/admin-guide/remote-backend/login/#generating-a-token))
2. Run `terraform plan` and ensure you are working in the correct environment.
   1. You should see this trigger a plan in env zero
3. (Optional) Run `terraform pull > backup.state` to pull the state to a local file.
4. Remove the remote backend code block from step 1.
5. Add a backend code block for the new remote backend of your choosing ([Terraform Backends](https://developer.hashicorp.com/terraform/language/settings/backends/configuration#backend-configuration)).
6. Run `terraform init -migrate-state`, respond to the prompt with `yes`
7. Run `terraform plan`. You should expect to see no or minimal changes.
8. (If necessary, in conjunction with step 4) Run `terraform state push backup.state` to push your state to your new remote backend.
9. The state has now been migrated to your configured backend.
    1. If you are moving away from env zero, the environment can be marked as inactive.
    2. If you are moving states between env zero, the old environment will need to be marked as inactive and a new environment will have to be created.

## Migrating from third-party bucket to env zero remote backend

1. (Optional) Run `terraform state pull > remote.state` to pull the state to a local file.
2. Swap the backend configuration with env zero's

```hcl  theme={null}
terraform {
  cloud {
    hostname = "backend.api.env0.com"
    organization = "<YOUR_ORGANIZATION_ID>.<YOUR_PROJECT_ID>"

    workspaces {
      name = "<YOUR_WORKSPACE_NAME>"
    }
  }
}
```

1. run `terraform init` and enter `yes`

```text  theme={null}
Initializing cloud backend...
Migrating from backend "s3" to cloud backend.
Do you wish to proceed?
  As part of migrating to cloud backend, Terraform can optionally copy your
  current workspace state to the configured cloud backend workspace.
  
  Answer "yes" to copy the latest state snapshot to the configured
  cloud backend workspace.
  
  Answer "no" to ignore the existing state and just activate the configured
  cloud backend workspace with its existing state, if any.
  
  Should Terraform migrate your existing state?

  Enter a value: yes
```

1. env zero will detect the new state and create an environment for you - the name will be your workspace name.
   1. Make sure to update the VCS details to point to your real VCS

## Troubleshooting

Error: Backend configuration changed – make sure that you add an Environment Variable with`TF_CLI_ARGS_init=-migrate-state -force-copy`

## Suggested Blog Content

[Terraform Modules Guide](https://www.env0.com/blog/terraform-modules)

[Terraform Plan Examples](https://www.env0.com/blog/terraform-plan)

[Managing Terraform Variable Hierarchy](https://www.env0.com/blog/managing-terraform-variable-hierarchy)

[Manage Terraform Remote State with a Remote Backend](https://www.env0.com/blog/terraform-remote-state-using-a-remote-backend)

Built with [Mintlify](https://mintlify.com).
