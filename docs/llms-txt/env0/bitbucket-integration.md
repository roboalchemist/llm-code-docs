# Source: https://docs.envzero.com/guides/admin-guide/templates/bitbucket-integration.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Standard Bitbucket Integration

> Connect Bitbucket Cloud repositories to env zero to create templates and manage deployments

<Info>
  **Note**

  In order to integrate with Bitbucket, you need to have permission to install a Bitbucket App on your Bitbucket workspace/repository. If you do not have those permissions, please ask an admin or a different user with those permissions to create the template
</Info>

## New Template

If you would like to create your first Bitbucket Integrated Template in this env zero organization, please see **[Create Your First Template](/guides/getting-started/getting-started/create-your-first-template)** instead.

1. Click **ADD A NEW TEMPLATE** on the top left in the *Templates* screen.
2. Pick your template type, pick a name for the template, and then click on **NEXT**
3. Click on the **Bitbucket.org** button. Since you have already created a Bitbucket template in this env zero organization, no such popup will appear, you are now able to pick from repositories known to env zero in your organization
4. Pick the repository containing your IaC configuration.
5. If you would like to pull the code from a specific revision or branch, enter that in the `Revision` field. Leaving this field empty will use your default branch, which is usually "master"/"main".
6. Enter the folder your IaC files are located in under `Terraform Folder` or `Terragrunt Folder`. If your IaC files are in the root of the repository, leave this empty.
7. Click on **NEXT** to proceed to the variables section
8. Add environment and IaC variables that you'd like to be used during deployment, and then click on **NEXT** to go to the final "Projects" section
9. Pick the projects that you'd like to have access to deploy this template, and then click on **DONE** to create the template.
10. Pick the projects that you'd like to have access to deploy this template, and then click on DONE to create the template.

<img src="https://mintcdn.com/envzero-b61043c8/NFoAIaj_CGEzw-yg/images/guides/admin-guide/templates/e6d3da9-screen_shot_2021-04-08_at_13.png?fit=max&auto=format&n=NFoAIaj_CGEzw-yg&q=85&s=c2b390ca1fd2ddf5c533834f83e33bcc" alt="" width="2784" height="1034" data-path="images/guides/admin-guide/templates/e6d3da9-screen_shot_2021-04-08_at_13.png" />

<Warning>
  Troubleshooting

* Can't find your repository? Check if your Bitbucket workspace has the env zero Bitbucket App installed, and if the App is allowed access to your repository
  * Bitbucket App is not installed - Simply click on the "authorize another Bitbucket workspace" link underneath the "Bitbucket Repository" field. You will get a popup allowing you to install the env zero Bitbucket app on another Bitbucket workspace.
</Warning>

## Existing Template

If you would like to integrate an existing template with Bitbucket via a Bitbucket App:

1. Go to the **Templates** screen, and click on **Settings** for the template you would like to integrate with Bitbucket.
2. Click on the **VCS** step. From there you can click on the **Bitbucket.org** button, and integrate with Bitbucket as you would for a new template.

Built with [Mintlify](https://mintlify.com).
