# Source: https://docs.ox.security/automate-with-ox-workflows/pipeline-workflows.md

# Pipeline Workflows

Pipeline workflows in OX Security automate how OX evaluates and handles issues during CI/CD runs. They build on the standard OX pipeline integration, which [connects your CI/CD system and enables pipeline scanning](https://docs.ox.security/scan-and-analyze-with-ox/scanning/scanning-ci-cd-pipelines).

You can use workflows to configure conditions, such as severity levels or issue types, and specify whether to block the pipeline or raise an alert.

OX Security provides the following configuration methods for pipeline workflows:

* [Customizing default pipeline workflows](#working-with-the-default-pipeline-workflow)
* [Creating custom pipeline workflows](#creating-a-new-pipeline-workflow)

After configuring a pipeline workflow, you need [to activate it](#activating-pipeline-workflows).

## Working with the default pipeline workflow

OX Security provides a built-in default pipeline workflow. This workflow applies to all applications unless a custom workflow is assigned. It is recommended to work with this workflow when you only need small adjustments.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-bcc2677ba3dba1aa6454accda4ce496a12fe4778%2FDefault_PW.png?alt=media" alt=""><figcaption></figcaption></figure>

The default pipeline workflow includes predefined conditions and actions for common use cases, and it includes the following elements:

* [**Trigger types:**](https://docs.ox.security/automate-with-ox-workflows/pipeline-workflows/pipeline-triggers) The default workflow includes triggers for all supported pipeline events.
* [**Conditions:**](https://docs.ox.security/automate-with-ox-workflows/pipeline-workflows/pipeline-conditions) All severities (low and above) are included by default.
* [**Actions:**](https://docs.ox.security/automate-with-ox-workflows/pipeline-workflows/pipeline-actions) The default action for all conditions is set to `alert`.

You can view the default workflow by opening any development environment. Even when the workflow is disabled, you can expand it and inspect the configuration without activating it.

You can use a default pipeline workflow or create custom workflows based on your use cases.

**To use the default workflow:**

1. Go to the **Pipeline Workflows** page.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-305cbe2714ea57ecc63d59491e431513a17ca4d2%2FDefaultPW1.png?alt=media" alt=""><figcaption></figcaption></figure>

1. Click the **Default** workflow to review its configuration.
2. Modify the workflow as needed:
   * Change alert to block.
   * Adjust severity levels.
   * Remove or add conditions and actions.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-2e9993d0e235e2e08d38b60f77f11d8530ff18b6%2FDefaultPW2.png?alt=media" alt=""><figcaption></figcaption></figure>

1. Enable the default pipeline workflow.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-101d459ee8ab7d079644dd74c8e1dee3a7268fb4%2FEnable%20def%20PW.png?alt=media" alt=""><figcaption></figcaption></figure>

1. [Activate the default pipeline workflow on the application](#activating-pipeline-workflows).

## Creating a new pipeline workflow

When you need many custom rules or want to separate workflows for different categories such as, secrets, specific branches, or apps, you can create a new workflow.

For example, to block critical secrets from entering the codebase, you can create a new workflow. When configured, this workflow ensures that any new secret of critical severity will block the pipeline and prevent the pull request from being merged.

**To create a new workflow:**

1. In the **Pipeline Workflows** page, select **Create New Workflow**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-dc6aa9222d33fc087c9dad0a854db5e546788add%2FCreate%20new%20workflow.png?alt=media" alt="" width="358"><figcaption></figcaption></figure>

1. Enter a name and a description for your new workflow.
2. Select the applications or repositories it should apply to and select **CREATE**. A new policy appears on the page.
3. Add [triggers](https://docs.ox.security/automate-with-ox-workflows/pipeline-workflows/pipeline-triggers), [conditions](https://docs.ox.security/automate-with-ox-workflows/pipeline-workflows/pipeline-conditions), and [actions](https://docs.ox.security/automate-with-ox-workflows/pipeline-workflows/pipeline-actions)to your new pipeline workflow.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-07c8e906b2b66ecbc7e4504616e241eb45f916a5%2FPipeline_Workflow.png?alt=media" alt="" width="212"><figcaption></figcaption></figure>

1. Enable the workflow and [activate it on the application](#activating-pipeline-workflows).

## Activating pipeline workflows

To run the workflow, make sure it is assigned to the application, enabled, and that pipeline integration has been completed for that application.

**To activate a workflow on an application:**

1. Go to the **Applications** page, select the relevant applications, and then select the **Pipeline Workflows** icon.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-410be629da7301cfdd5b0bbd08e1c5d532ec5033%2FApp_page%20(1).png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

1. In the **Pipelines** dialog box, verify that the relevant pipeline workflows are enabled.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-3da7f6de041b813c807c928c26b4132c7adf2e9b%2FPipeline_Settings_PW_enable.png?alt=media" alt=""><figcaption></figcaption></figure>

**Alternatively:**

1. On the **Pipeline Workflows** page, click the workflow gear icon.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-e30acdee6f8d3f14382ba93f3bccd269b2b70dc3%2FPW_gear_icon.png?alt=media" alt="" width="110"><figcaption></figcaption></figure>

1. In the **Pipelines** dialog box, select the applications in which you want to activate your pipeline workflow and select **SAVE**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-8057c169ca69a13a47094ed04069c849b58e77b5%2FPipelines_selectinf%20apps.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>
