# Source: https://northflank.com/docs/v1/application/release/continuous-integration-and-delivery-on-northflank.md

# Continuous integration and delivery on Northflank

Northflank enables you to manage your application delivery from development, through testing, to production.

You can automate builds and deployments using CI/CD in individual services, or use pipelines to configure workflows with complex tasks covering many resources.

You can also learn more in the guide on [releasing for production](https://northflank.com/docs/v1/application/production-workloads/release-for-production).

## Continuous integration and delivery

Continuous integration (CI) allows you to automatically build code when a commit is pushed to your Git repository. Continuous delivery (CD) automatically deploys new builds, in any environment.

You can configure rules in services and jobs to manage your development workflows and releases.

CI/CD on Northflank can be used to set up simple but powerful release flows. You can enable CI/CD in a single combined service in order to automatically build and deploy from one repository. You could also use CI/CD with a build service to build development, release, and production branches and deploy to different deployment services.

- [Manage CI/CD: Configure continuous integration and continuous delivery on your Northflank services.](/v1/application/release/manage-ci-cd)

## Release with pipelines

You can use pipelines to manage your release process through multiple environments. Add resources to different pipeline stages for visibility, and define your release workflow for each stage in a template to run releases with a single click.

### Release flows

Release flows are [templates](https://northflank.com/docs/v1/application/infrastructure-as-code/infrastructure-as-code) for specific pipeline stages that can automate release tasks, such as backing up databases, triggering builds, running jobs, and promoting images from one stage to another.

You can make each step in a release flow conditional so that if a step fails, the rest of the release will not continue. You can also quickly roll back to a previous release.

### Triggering releases

Releases can be run manually, or you can configure a Git or webhook trigger to start a release flow run.

- [Set up a pipeline and release flow: Manage your deployments and release your updates in an intuitive pipeline with release flows.](/v1/application/release/create-a-pipeline-and-release-flow)
- [Configure a release flow: Learn how to use the visual editor or code to configure a release flow.](/v1/application/release/configure-a-release-flow)
- [Release flows and preview environments within templates: Create and manage pipelines with release flow and preview environment templates within Northflank templates.](/v1/application/infrastructure-as-code/write-a-template#include-release-flows-and-preview-environment-templates)
- [Run a release flow: Run a release flow and manage releases for your different environments.](/v1/application/release/run-and-manage-releases)
- [Roll back a release: Roll back a release to a previous version.](/v1/application/release/run-and-manage-releases#roll-back-a-release)

## Run database migrations

You can run database migrations manually, or automate the process as part of a release flow.

- [Run migrations: Run database migrations and update your deployments simultaneously when you update your schema.](/v1/application/release/run-migrations)

## Ephemeral preview environments

You can define a [template](https://northflank.com/docs/v1/application/infrastructure-as-code/infrastructure-as-code) to create ephemeral environments to preview Git branches or pull requests.

Preview environments can be created automatically using Git or webhook triggers, and torn down in one action.

- [Set up a preview environment: Create templates in your pipelines to automatically generate temporary preview environments to view pull requests and branches.](/v1/application/release/set-up-a-preview-environment)
- [Create and manage previews: Manage your preview environments, pause triggers, and generate previews manually.](/v1/application/release/create-and-manage-previews)
- [Release flows and preview environments within templates: Create and manage pipelines with release flow and preview environment templates within Northflank templates.](/v1/application/infrastructure-as-code/write-a-template#include-release-flows-and-preview-environment-templates)

## Release using Git

You can store release flows as JSON in a Git repository with bidirectional sync, so that when you commit changes to your release flow template it will update in Northflank, and vice versa.

You can also trigger a release using a webhook in a GitHub action.

- [GitOps on Northflank: Use templates and release flows in a Git repository to trigger changes to your config and resources.](/v1/application/infrastructure-as-code/gitops-on-northflank)
- [Use Git Actions on Northflank: Create workflows and publish GitHub Actions that interact with Northflank.](/v1/application/infrastructure-as-code/use-github-actions-with-northflank)
