# Source: https://northflank.com/docs/v1/application/infrastructure-as-code/infrastructure-as-code.md

# Infrastructure as code on Northflank

Northflank uses templates as its infrastructure as code (IaC) primitive. A template describes resources, services, databases, pipelines, and integrations, everything you would otherwise configure manually through the Northflank UI or API. You can build templates visually using a drag-and-drop node editor, or work directly in JSON. Both approaches produce the same output and can be used interchangeably. Templates are repeatable, versionable, and can be run on-demand or triggered automatically.

If you've used tools like Terraform or Pulumi, templates fill a similar role: they let you define your infrastructure in code, commit it to Git, and apply changes programmatically. The key difference is that templates are native to Northflank and can express the full range of Northflank-specific concepts including pipelines, release flows, and preview environments without needing a separate provider or plugin.

### Types of template

There are three types of templates in Northflank, each scoped to a different part of your workflow.

- Team templates are the most general type. They are created at the team level and can define anything: cloud provider integrations, projects, services, databases, pipelines, and more. Use a team template when you want to provision an entire stack from scratch, replicate an environment across regions, or give other users a one-click way to deploy your project with their own configuration.

- Release flow templates are defined within a pipeline stage and automate the steps needed to ship a release. A release flow can back up a database, trigger a build, run a migration job, promote an image from staging to production, and more, all in a defined sequence. Each stage in a pipeline can have its own release flow template.

- Preview environment templates are also defined within a pipeline. They specify the resources and secrets that should be created whenever a pull request is opened or a new commit is pushed to a branch. The environment is ephemeral and is torn down automatically when the PR is closed or merged

![An example of a successfully run template in the Northflank application](https://assets.northflank.com/documentation/v1/application/infrastructure-as-code/infrastructure-as-code-on-northflank/template-success.png)

## Writing templates

Templates are composed of nodes. Each node represents an action or resource, such as creating a service, deploying a database, or running a job. In the visual editor you drag nodes onto a canvas and connect them. In JSON, you define them as objects in a spec. Nodes can reference each other's outputs, allowing you to chain actions together. For example, you can create a database node and pass its connection string directly into a service node as an environment variable.

You can use templates to:

- Automate the process to deploy a single service, or multiple projects

- Manage your infrastructure and deployments using GitOps

- Add [integrations with cloud providers](https://northflank.com/docs/v1/application/bring-your-own-cloud/use-other-cloud-providers-with-northflank) and deploy clusters into your own cloud accounts

- Define pipelines with release flows and preview environments

- Create shareable one-click deployments for your project so users can get up and running immediately

Templates can be created using the visual editor in the Northflank application, or edited directly as JSON.

- [Create a template: Learn how to create and configure a Northflank template.](/v1/application/infrastructure-as-code/create-a-template)
- [Write a template: Learn how to structure a Northflank template, define workflows, create resources, and perform actions.](/v1/application/infrastructure-as-code/write-a-template)
- [Template nodes: Learn about different types of template nodes, their behaviour, and their specifications.](/v1/application/infrastructure-as-code/template-nodes)
- [Run a template: Run templates manually or automatically.](/v1/application/infrastructure-as-code/run-a-template)
- [Share a template: Share templates with your team or the public.](/v1/application/infrastructure-as-code/share-a-template)

## Write dynamic templates

You can write templates in a programmatic manner so that they can be easily run with different configurations, or use dynamic values based on variables. Hardcoded values can be replaced by template arguments, references to the output from a previous template node, and functions that are evaluated when the template is run.

This allows you to use a single generalised template to deploy the same project in different regions, as different staging environments, or share a template where team members or the public can enter their own arguments to configure a deployment.

- [Use values from a template node: Use the values output from a node executed in a template.](/v1/application/infrastructure-as-code/make-a-template-dynamic#get-node-outputs-from-references)
- [Use arguments in your template: Use variables to make your template dynamic, and override the values on individual template runs.](/v1/application/infrastructure-as-code/make-a-template-dynamic#add-arguments)
- [Use functions in templates: Use Northflank functions in your templates to change and evaluate values based on arguments and node outputs.](/v1/application/infrastructure-as-code/make-a-template-dynamic#use-northflank-functions)
- [Manage multiple templates with GitOps: Use a single source of truth for your infrastructure and projects across regions and cloud providers, or deploy the same project with different configuration values.](/v1/application/infrastructure-as-code/gitops-on-northflank#create-multiple-northflank-templates-from-one-source)

## Manage infrastructure with GitOps

Northflank's bidirectional GitOps helps you maintain a single source of truth for your infrastructure and resource configuration. Any changes to your template code committed to your repository will automatically update the template on Northflank, and any changes to your template in Northflank will be committed to your repository. You can use one source template to manage multiple Northflank templates. Combined with [arguments and overrides](#write-dynamic-templates) you can update multiple projects with separate configurations.

You can also set your template to run automatically when it is updated, meaning you can manage your infrastructure and configuration using Git.

- [GitOps on Northflank: Use templates and release flows in a Git repository to trigger changes to your config and resources.](/v1/application/infrastructure-as-code/gitops-on-northflank)
- [Use Git Actions on Northflank: Create workflows and publish GitHub Actions that interact with Northflank.](/v1/application/infrastructure-as-code/use-github-actions-with-northflank)

## Define release flows and preview environments

Release flows are templates for specific pipeline stages that can automate release tasks, such as backing up databases, triggering and deploying builds, running jobs, and promoting images from one stage to another.

You can create a release flow either in an existing project's pipeline, or by configuring it in a pipeline node in a Northflank template. You can add Git or webhook triggers to run a release automatically.

- [Release flows and preview environments within templates: Create and manage pipelines with release flow and preview environment templates within Northflank templates.](/v1/application/infrastructure-as-code/write-a-template#include-release-flows-and-preview-environment-templates)
- [Set up a pipeline and release flow: Manage your deployments and release your updates in an intuitive pipeline with release flows.](/v1/application/release/create-a-pipeline-and-release-flow)
- [Configure a release flow: Learn how to use the visual editor or code to configure a release flow.](/v1/application/release/configure-a-release-flow)
- [Set up a preview environment: Create templates in your pipelines to automatically generate temporary preview environments to view pull requests and branches.](/v1/application/release/set-up-a-preview-environment)

## Versioning and history for templates

You can use [GitOps](#manage-infrastructure-with-gitops) with your Northflank templates to track and manage changes in your Git repository.

All templates have a run history, detailing the status and output of each template run, which you can use to review and troubleshoot templates. Release flows allow you to roll back to a previous release with a single click.

Enterprise customers can use the template drafts feature to review proposed changes to a template directly in Northflank, and track template changes and runs using [audit logs](https://northflank.com/docs/v1/application/observe/audit-logs).

- [Manage template versions on Northflank: Use the template drafts system to review, accept, or reject proposed changes to your team's Northflank templates.](/v1/application/infrastructure-as-code/manage-template-versions)
- [Roll back a release: Roll back a release to a previous version.](/v1/application/release/run-and-manage-releases#roll-back-a-release)
