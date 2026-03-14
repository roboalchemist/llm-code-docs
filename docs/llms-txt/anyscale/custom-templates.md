# Source: https://docs.anyscale.com/platform/workspaces/custom-templates.md

# Share workspaces with custom templates

[View Markdown](/platform/workspaces/custom-templates.md)

# Share workspaces with custom templates

This page provides an overview of creating and using custom templates for Anyscale workspaces.

important

Custom templates are in beta release.

## What are custom templates?[​](#what-are-custom-templates "Direct link to What are custom templates?")

Custom templates allow cloud owners to save the contents and configurations of an Anyscale workspace and publish them so users can create a new workspace from the template. Templates allow code owners to define development environments, share boilerplate code, or publish experiments and models.

Custom templates save the following assets from your Anyscale workspace:

* Workspace files
* Container images and customized containerfiles
* Runtime dependencies
* Compute configurations

Anyscale scopes custom templates at the cloud level. When a cloud owner publishes a custom template, it becomes available to all collaborators in an Anyscale cloud for all projects in that cloud. See [Create a workspace from a custom template](#use).

Anyscale versions templates and allows cloud owners to revert to previous versions or return a previously published template to a draft state. Only one version of a template is available to users in a published state. See [Manage custom templates](#manage).

## View available templates[​](#view "Direct link to View available templates")

Anyscale shows a selection of recommended templates when you log in to the [Anyscale console](https://console.anyscale.com). Click **View all templates** to see more templates. The **Templates** page contains the following tabs:

* **All templates**: Templates authored by Anyscale and your custom templates.
* **Anyscale templates**: Templates authored by Anyscale with example workloads.
* **My organization**: Published custom templates you can access.
* **Drafts**: Cloud owners can view custom templates they haven't published. You can convert previously published templates back to draft state and find them here. See [Manage custom templates](#manage).

note

You can also access the templates page from the **Workspaces** page by clicking **Create > Create from template > View all templates**.

## Create a workspace from a custom template[​](#use "Direct link to Create a workspace from a custom template")

To create a new workspace from a template, select a template from the **Templates** page. Click **Launch** to create a workspace with the template.

When you create a workspace from a template, your workspace launches with the configurations and workspace files saved in the template. Changes you make to contents and configurations in your workspace don't impact the template.

note

Cloud owners can export any workspace and publish it as a new version for an existing template. Updates to a template don't impact previously created workspaces.

## Create a custom template[​](#create "Direct link to Create a custom template")

Cloud owners create a custom template from an existing workspace in the Anyscale console. To create a new custom template or version an existing template, complete the following steps:

1. Log in to the [Anyscale console](https://console.anyscale.com).

2. In the left navigation bar, select **Workspaces**.

3. Click the name of an existing workspace or create a new workspace. See [Tutorial: Create a workspace](/get-started/create-workspace.md).

4. Customize your workspace. Templates track the following configurations:

   <!-- -->

   * Workspace files: Add files to your workspace by uploading them, creating new files, or cloning a Git repository.
   * Container images: Configure a container image for your workspace, or use containerfiles to define a custom workspace image. See [Iterate on workspace container images](/dependency-management/containerfiles.md).
   * Runtime dependencies: Python packages and environment variables set in the **Dependencies** tab.
   * Compute configurations: The compute configuration for your workspace. Anyscale recommends using named compute configs and versions to manage your compute configurations.

5. Click the ellipsis (**...**) and select **Export to template**.

6. A dialog displays prompting you to build a container image and save your compute config. Click **Continue**.

7. You can either publish a new version of a template or create a new template. Only one version of a template is available to users at a time.

   <!-- -->

   * To publish a new version of a template, select **Push changes to an existing template** and select the name of your template from the dropdown.
   * For a new template, select **Create a new template**.

8. Click **Export**.

9. For new templates, enter details in the **Name** and **Description** fields. You can't edit these fields if publishing a new template version.
   <!-- -->
   * Optionally, edit the container image and compute configuration.

10. Click **Create**.

The template displays in the **Draft** state.

## Working with draft templates[​](#draft "Direct link to Working with draft templates")

A *draft* template is a template that isn't published. Only cloud owners can interact with draft templates. You encounter draft templates in the following scenarios:

* When you create a new template.
* You create a new version of an existing template.
* You view previous versions of a template as drafts.
* You revert a published template back to the draft state.

Draft templates remain in a draft state unless you publish them. Most configurations in a draft template are read-only. To update things such as workspace files, compute configurations, or the container image, you can either create a new version or create a new template.

To publish your draft template for use by cloud collaborators, click **Publish template**. When you publish a template, all other versions of the template revert to draft state.

To create a workspace from the template, click **Test in a workspace**.

You have access to most template management options in the draft state. See [Manage custom templates](#manage).

## Manage custom templates[​](#manage "Direct link to Manage custom templates")

Only cloud owners can manage templates. Cloud collaborators interact with all templates as read-only.

Access the following management options by navigating to a template and clicking the ellipsis (**...**):

| Option                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Edit template details**       | Update the name, description, and icon associated with a template.Changes apply to all existing template versions.                                                                                                                                                                                                                                                                                                                            |
| **View versions**               | See all versions of a template.Click on a template version to view it as a draft.                                                                                                                                                                                                                                                                                                                                                             |
| **Create a new version**        | Create a new template version with the same workspace files and runtime dependencies.You can customize your container image and compute config through this flow. For most comprehensive updates including workspace files and runtime dependencies, start by creating a workspace from a desired version of your template and then follow instructions to **Push changes to an existing template**. See [Create a custom template](#create). |
| **Duplicate as a new template** | Clone the selected template version as a new template.                                                                                                                                                                                                                                                                                                                                                                                        |
| **Revert to a draft**           | Depublish the template so that cloud collaborators can't view or use it.                                                                                                                                                                                                                                                                                                                                                                      |
| **Delete**                      | Permanently remove all versions of a template.                                                                                                                                                                                                                                                                                                                                                                                                |
