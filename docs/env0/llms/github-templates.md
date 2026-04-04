# Source: https://docs.envzero.com/guides/admin-guide/templates/github-templates.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Standard GitHub Integration

> Connect GitHub repositories to env zero using the GitHub App for template creation and deployments

<Info>
  **Note**

  In order to integrate with GitHub, you need to have permission to install the GitHub App on your GitHub organization/repository. If you do not have these permissions, please ask an admin or an authorized user to create the template
</Info>

## New Template

If you would like to create your first GitHub Integrated Template, please see **[Create Your First Template](/guides/getting-started/getting-started/create-your-first-template)** instead.

1. In the top right corner of the Templates screen, click ‘ADD A NEW TEMPLATE’
2. Pick your template type, name it, and then click ‘NEXT’
3. Click on the GitHub.com button
4. Pick the repository containing your IaC configuration
5. If you would like to pull the code from a specific revision or branch, enter it in the Revision field. Leaving this field empty will use your default branch, which is usually master/main
6. Under Terraform Folder, enter the folder your Terraform files are located in. If your Terraform files are in the repository’s root, leave this field empty
7. Click on ‘NEXT’ to proceed to the Variables section
8. Add the Environment and Terraform variables that you'd like to be used during deployment, then click ‘NEXT’ to go to the final Projects section
9. Pick the projects that you'd like to have access to deploy this template, then click on 'DONE' to create the template

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/NFoAIaj_CGEzw-yg/images/guides/admin-guide/templates/github_template_creation_interface.png?fit=max&auto=format&n=NFoAIaj_CGEzw-yg&q=85&s=7f9a4c95232b1e6953c005f35cedeae8" alt="GitHub template creation interface" width="1441" height="573" data-path="images/guides/admin-guide/templates/github_template_creation_interface.png" />
</Frame>

<Warning>
  Troubleshooting

* Can't find your repository? Check if your GitHub organization has the env zero GitHub App installed and that the App is allowed access to your repository.
  * GitHub App is not installed: Simply click on the 'add another organization' link in the GitHub Repository field. You will get a popup allowing you to install the env zero GitHub app on another GitHub organization.
  * GitHub App is installed and has access to the repository, but you still can't find your repository: Click on the 'add another organization' link and pick your GitHub organization, even though it already has the GitHub App installed. You will now see the env zero GitHub App settings page in GitHub. Edit the repositories that env zero App should have access to (you may also remove and re-pick a repository), then save your changes. Note: You can only do this if you are an organization admin for your GitHub organization.

* Got the following error: "GitHub App was not installed because you do not have permissions to install our GitHub App on your organization"? This means that you do not have permissions to install the GitHub App, and instead have sent a request to another user to install the App. Please cancel that request in GitHub and ask a different user with permissions to install the GitHub App and create the template for you.
  * A user already accepted your request to install the GitHub App? If so, follow the instructions in the GitHub App is installed and has access to the repository, but you still can't find your repository section above.
</Warning>

<Frame caption="Edit GitHub App Settings">
  <img src="https://mintcdn.com/envzero-b61043c8/NFoAIaj_CGEzw-yg/images/guides/admin-guide/templates/github_app_settings_page.png?fit=max&auto=format&n=NFoAIaj_CGEzw-yg&q=85&s=ea03082189fd2f82b21b9a77004a0a42" alt="GitHub App settings page" width="1214" height="778" data-path="images/guides/admin-guide/templates/github_app_settings_page.png" />
</Frame>

## Existing Template

If you would like to integrate an existing template with GitHub via a GitHub App:

1. Go to the Templates screen, and click on ‘Settings’ for the template you would like to integrate with GitHub
2. Click on ‘VCS’. From there you can click on the ‘GitHub.com’ button, and integrate with GitHub as you would for a new template

## Multi-Org Configuration

1. Click on ‘GitHub.com’ to create a new template
2. You will get a GitHub popup. Login if you're not already logged in
3. In the popup, pick the organization you would like to authorize

<img src="https://mintcdn.com/envzero-b61043c8/NFoAIaj_CGEzw-yg/images/guides/admin-guide/templates/395b45f-image_3.png?fit=max&auto=format&n=NFoAIaj_CGEzw-yg&q=85&s=51ca6e2794e6ed560ec8c843ee3512ff" alt="" width="557" height="343" data-path="images/guides/admin-guide/templates/395b45f-image_3.png" />.png")

1. After selecting the GitHub organization, you will be transferred to the GitHub App settings page for that organization

<img src="https://mintcdn.com/envzero-b61043c8/NFoAIaj_CGEzw-yg/images/guides/admin-guide/templates/11a1a2c-image_4.png?fit=max&auto=format&n=NFoAIaj_CGEzw-yg&q=85&s=981e6c8a1bdaef913cb70cecdb63865b" alt="" width="702" height="756" data-path="images/guides/admin-guide/templates/11a1a2c-image_4.png" />.png")

1. Here, you need to change something so that the GitHub dialogue will let you save. If ‘Only select repositories’ is already enabled, simply click on ‘All repositories’ and then re-click on ‘Only select repositories.’ You will then be able to save without changing any GitHub App permissions
2. Upon saving, env zero UI should be able to list the repositories. Once the template is saved, the env zero organization is integrated with GitHub

<Info>
  Additional Content

* [Managing Terraform variable hierarchy](https://www.env0.com/blog/managing-terraform-variable-hierarchy)
* [Why env zero is a Terraform Cloud alternative?](https://www.env0.com/alternatives/terraform-cloud-alternative)
</Info>

Built with [Mintlify](https://mintlify.com).
