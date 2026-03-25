# Source: https://docs.envzero.com/guides/getting-started/getting-started/create-your-first-template.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Building Your First Template

> Create your first env zero template by connecting your VCS and Terraform code

Templates are the way to add your Terraform code to env zero. You will need to tell env zero how to connect to your VCS, and where to find your Terraform code.

## Create Your Template

1. Open the **Organization Templates** page

<Frame caption="Link to Organization Templates">
  <img src="https://mintcdn.com/envzero-b61043c8/A22trGA9OCusm4S6/images/guides/getting-started/getting-started/organization_templates_page_link.png?fit=max&auto=format&n=A22trGA9OCusm4S6&q=85&s=a2a532c90f0a3ab59e0d76a0854a589d" alt="Organization templates page link" width="406" height="736" data-path="images/guides/getting-started/getting-started/organization_templates_page_link.png" />
</Frame>

1. Click on **Create new template**

<Frame caption="Create New Template">
  <img src="https://mintcdn.com/envzero-b61043c8/A22trGA9OCusm4S6/images/guides/getting-started/getting-started/create_new_template_button.png?fit=max&auto=format&n=A22trGA9OCusm4S6&q=85&s=c0c03f66e07edbc086cbf8ce0ee93ba2" alt="Create new template button" width="2240" height="436" data-path="images/guides/getting-started/getting-started/create_new_template_button.png" />
</Frame>

1. Choose your desired template type
2. Enter a name for your template in `Template Name`, and then click on **NEXT**

<img src="https://mintcdn.com/envzero-b61043c8/A22trGA9OCusm4S6/images/guides/getting-started/getting-started/c023fedf434d3406af005fa4412c9ffb691f5cf9e6342b86d9ecbcc56ec80f14-image.png?fit=max&auto=format&n=A22trGA9OCusm4S6&q=85&s=e40851de58f5186f5d6e4f7faf7dff11" alt="" width="1404" height="679" data-path="images/guides/getting-started/getting-started/c023fedf434d3406af005fa4412c9ffb691f5cf9e6342b86d9ecbcc56ec80f14-image.png" />

1. Please follow the next sections per your VCS integration:

* [GitHub](/guides/getting-started/getting-started/create-your-first-template/#github)
* [GitLab](/guides/getting-started/getting-started/create-your-first-template/#gitlab)
* [Bitbucket](/guides/getting-started/getting-started/create-your-first-template/#bitbucket)
* [AzureDevOps](/guides/getting-started/getting-started/create-your-first-template/#azure-devops)
* [Other VCS](/guides/getting-started/getting-started/create-your-first-template/#other-vcs)

## GitHub

1. After clicking on "GitHub.com" button for the first time, you will get a popup from GitHub asking you to install the `env zero` GitHub App on a GitHub organization. Pick the GitHub organization containing your Terraform repository.

<Frame caption="Pick GitHub Organization">
  <img src="https://mintcdn.com/envzero-b61043c8/A22trGA9OCusm4S6/images/guides/getting-started/getting-started/github_organization_selection_popup.png?fit=max&auto=format&n=A22trGA9OCusm4S6&q=85&s=5bf1518fbefd4311a0f3205c49a0156e" alt="GitHub organization selection popup" width="690" height="624" data-path="images/guides/getting-started/getting-started/github_organization_selection_popup.png" />
</Frame>

1. Pick the repositories you want env zero GitHub App to have access to, and install the GitHub App

<Frame caption="Pick GitHub Repositories">
  <img src="https://mintcdn.com/envzero-b61043c8/A22trGA9OCusm4S6/images/guides/getting-started/getting-started/github_repository_selection_interface.png?fit=max&auto=format&n=A22trGA9OCusm4S6&q=85&s=4a886841634a7f1b88d0ee1ef44f7519" alt="GitHub repository selection interface" width="675" height="811" data-path="images/guides/getting-started/getting-started/github_repository_selection_interface.png" />
</Frame>

1. The popup GitHub window will close.
2. Pick the GitHub repository that contains the code for this template
3. If you would like to pull the code from a specific revision or branch, enter that in the `Revision` field. Leaving this field empty will use your default branch, which is usually “master”/"main".
4. Enter the folder your IaC files are located in under `Terraform Folder` or `Terragrunt Folder`. If your IaC files are in the root of the repository, leave this empty.
5. Click on **NEXT** to go to the next step, [Variables](/guides/getting-started/getting-started/create-your-first-template/#variables)

<img src="https://mintcdn.com/envzero-b61043c8/A22trGA9OCusm4S6/images/guides/getting-started/getting-started/c7586a80eee514f4856d5b8478e5121275dae466a2ae77daef3c1c89d5742a26-image.png?fit=max&auto=format&n=A22trGA9OCusm4S6&q=85&s=280fa396cc9c7bc646644b4d1402bd86" alt="" width="1403" height="646" data-path="images/guides/getting-started/getting-started/c7586a80eee514f4856d5b8478e5121275dae466a2ae77daef3c1c89d5742a26-image.png" />

## GitLab

### OAuth

1. After clicking on the "GitLab.com" button for the first time, you will get a popup from GitLab asking you to authorize the `env zero` GitLab application access to your repositories using your account.

<img src="https://mintcdn.com/envzero-b61043c8/A22trGA9OCusm4S6/images/guides/getting-started/getting-started/54471f0-screen_shot_2021-01-21_at_18.png?fit=max&auto=format&n=A22trGA9OCusm4S6&q=85&s=9dfbe2c8c9779f42d53a67f6f63dacbf" alt="" width="518" height="432" data-path="images/guides/getting-started/getting-started/54471f0-screen_shot_2021-01-21_at_18.png" />

1. The GitLab popup will close.
2. Pick the GitLab repository that contains the code for this template
3. If you would like to pull the code from a specific revision or branch, enter that in the `Revision` field. Leaving this field empty will use your default branch, which is usually “master”/"main".
4. Enter the folder your IaC files are located in under `Terraform Folder` or `Terragrunt Folder`. If your IaC files are in the root of the repository, leave this empty.
5. Click on **NEXT** to go to the next step, [Variables](/guides/getting-started/getting-started/create-your-first-template/#variables)

### GitLab Access Token

1. After selecting "GitLab.com" a double-options radio button will be shown
2. Click on `Access Token` and either select an existing token or create a new one.
   1. Creating a token:
      1. The token can be either a [Personal Access Token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html) or a [Group Access Token](https://docs.gitlab.com/ee/user/group/settings/group_access_tokens.html).
      2. The token must have access to each repository you would like to be able to use with env zero. For each project, the user should have at least Maintainer/Owner permissions.
      3. The token must have the “read\_repository” and "api" scopes defined.
3. Follow the same steps from step 3, listed above in the `OAuth` section.

<img src="https://mintcdn.com/envzero-b61043c8/A22trGA9OCusm4S6/images/guides/getting-started/getting-started/b8353adf44b95bee031d103cb63f9f7f1562ca2bc3a897a5a816150103e00cba-image.png?fit=max&auto=format&n=A22trGA9OCusm4S6&q=85&s=30d77257f2befc223bdcb2bd8ca885cb" alt="" width="1402" height="826" data-path="images/guides/getting-started/getting-started/b8353adf44b95bee031d103cb63f9f7f1562ca2bc3a897a5a816150103e00cba-image.png" />

## Bitbucket

1. After clicking on the "Bitbucket.org" button for the first time, you will get a popup from Bitbucket asking you to authorize the `env zero` Bitbucket application access to your workspace using your account.

<img src="https://mintcdn.com/envzero-b61043c8/A22trGA9OCusm4S6/images/guides/getting-started/getting-started/47a575d-screen_shot_2021-04-08_at_14.png?fit=max&auto=format&n=A22trGA9OCusm4S6&q=85&s=c4acb9ebf93d18d60a76f066ae43e4fd" alt="" width="976" height="1260" data-path="images/guides/getting-started/getting-started/47a575d-screen_shot_2021-04-08_at_14.png" />

1. The Bitbucket popup will close.
2. Pick the Bitbucket repository that contains the code for this template.
3. If you would like to pull the code from a specific revision or branch, enter that in the `Revision` field. Leaving this field empty will use your default branch, which is usually “master”/"main".
4. Enter the repository sub-folder your IaC files are located in under `Terraform Folder` or `Terragrunt Folder`. If your IaC files are in the root of the repository, leave this empty.
5. Click on **NEXT** to go to the next step, [Variables](/guides/getting-started/getting-started/create-your-first-template/#variables)

## Azure DevOps

1. After clicking on "Azure DevOps" button for the first time, you will get a popup from Azure DevOps asking you to authorize the `env zero` Azure DevOps application access to your repositories using your account. Grant access for the app.

<img src="https://mintcdn.com/envzero-b61043c8/NFoAIaj_CGEzw-yg/images/guides/admin-guide/templates/be8b39b-ado_access_request.png?fit=max&auto=format&n=NFoAIaj_CGEzw-yg&q=85&s=86b900d735fde22d7a3a0a9d8a4309c7" alt="" width="966" height="669" data-path="images/guides/admin-guide/templates/be8b39b-ado_access_request.png" />

1. The Azure DevOps popup will close.
2. Pick the  Azure DevOps repository that contains the code for this template
3. If you would like to pull the code from a specific revision or branch, enter that in the `Branch` field. Leaving this field empty will use your default branch, which is usually “master”/"main".
4. Enter the folder your IaC files are located in under `<IaC> Folder`  (IaC being the template type you chose earlier). If your IaC files are in the root of the repository, leave this empty.
5. Click on **NEXT** to go to the next step, [Variables](/guides/getting-started/getting-started/create-your-first-template/#variables)

<Warning>
  Notice

  You must enable the `Third-party application access via OAuth` under `Organization Settings/Security/Policies` for any organization you wish to manage repositories for
</Warning>

## Other VCS

1. Enter the URL to your Terraform repository that contains the code for this template under "Repository URL" - The URL can either be an HTTP/S URL or an SSH URL
2. If you would like to pull the code from a specific revision or branch, enter that in the `Revision` field. Leaving this field empty will use your default branch, which is usually “master”/"main".
3. Enter the folder your Terraform files are located in under `Terraform Folder`. If your Terraform files are in the root of the repository, leave this empty.
4. If your repository is private - use the `SSH Keys` or `Git Token` dropdown, to select the keys/tokens you created in the Connecting your VCS stage.
5. Click on **NEXT** to go to the next step, [Variables](/guides/getting-started/getting-started/create-your-first-template/#variables)

<img src="https://mintcdn.com/envzero-b61043c8/A22trGA9OCusm4S6/images/guides/getting-started/getting-started/4534c4fb57676f845816c6ac4731a8bbbc4de3a0da9223b5a92758135173d427-image.png?fit=max&auto=format&n=A22trGA9OCusm4S6&q=85&s=24df2ea7c2fa5f7b9a1b19591bd40831" alt="" width="1403" height="736" data-path="images/guides/getting-started/getting-started/4534c4fb57676f845816c6ac4731a8bbbc4de3a0da9223b5a92758135173d427-image.png" />

## Variables

1. In the variables section, you can now enter environment variables and terraform variables that will be used when deploying this template. For more info **[Variables](/guides/admin-guide/variables)**
2. When you're done adding variables, click on **NEXT** to go to the final step, [Projects](/guides/getting-started/getting-started/create-your-first-template/#projects)

## Projects

1. Pick the projects that you'd like to allow to deploy this template.
2. Click on **DONE** when you're done to create the template.

<img src="https://mintcdn.com/envzero-b61043c8/A22trGA9OCusm4S6/images/guides/getting-started/getting-started/732ee4f-screen_shot_2021-01-21_at_18.png?fit=max&auto=format&n=A22trGA9OCusm4S6&q=85&s=28ca9194672a3ab4a99c896be3b9785f" alt="" width="1423" height="405" data-path="images/guides/getting-started/getting-started/732ee4f-screen_shot_2021-01-21_at_18.png" />

## Add Your Template To a Project

In order to run the template, you’ll need to add it to one of the organization's Projects. Your new organization will already have a Default Project.

1. Go to the **Default Organization Project**

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/A22trGA9OCusm4S6/images/guides/getting-started/getting-started/ff2459c-project_template_2_fix.png?fit=max&auto=format&n=A22trGA9OCusm4S6&q=85&s=593d3f8b1b396fc3fad994380f6820f1" alt="Project template creation interface showing template configuration options" width="470" height="572" data-path="images/guides/getting-started/getting-started/ff2459c-project_template_2_fix.png" />
</Frame>

1. Click the **Project Templates** page in the left menu.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/A22trGA9OCusm4S6/images/guides/getting-started/getting-started/project_templates_page_navigation.png?fit=max&auto=format&n=A22trGA9OCusm4S6&q=85&s=96ac6a6caa19b0d5ca426c6dfe794e7a" alt="Project templates page navigation" width="2240" height="1184" data-path="images/guides/getting-started/getting-started/project_templates_page_navigation.png" />
</Frame>

1. Click **Manage** and check the checkbox next to the template you've created.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/A22trGA9OCusm4S6/images/guides/getting-started/getting-started/ff2459c-project_template_2_fix.png?fit=max&auto=format&n=A22trGA9OCusm4S6&q=85&s=593d3f8b1b396fc3fad994380f6820f1" alt="Project template management interface" width="470" height="572" data-path="images/guides/getting-started/getting-started/ff2459c-project_template_2_fix.png" />
</Frame>

1. Click **Save**

<Info>
  Additional Content

* [Managing Terraform variable hierarchy](https://www.env0.com/blog/managing-terraform-variable-hierarchy)
* [Why env zero is a Terraform Cloud alternative?](https://www.env0.com/alternatives/terraform-cloud-alternative)
</Info>

Built with [Mintlify](https://mintlify.com).
