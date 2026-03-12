# Source: https://docs.port.io/solutions/resource-self-service/self-service-environments.md

# Self-service environments

Automating the creation of development environments is crucial for engineering teams. Manual setup is slow, error-prone, and often leads to inconsistencies that can delay development and cause integration headaches. By enabling self-service environment provisioning, teams can spin up the resources they needâon demand and with the right guardrailsâfreeing up developers to focus on building features instead of wrangling infrastructure.

[Self-Service Environments with Port](https://www.youtube.com/embed/1OLXdVAmee4?si=-Wtb-Y5KWkKRECrA)

## Get started with self-service environments[â](#get-started-with-self-service-environments "Direct link to Get started with self-service environments")

Explore these step-by-step guides to automate environment creation and management, which we've broken into the following categories

### Scaffolding new apps[â](#scaffolding-new-apps "Direct link to Scaffolding new apps")

* [Scaffold a New App and Deploy to Kubernetes](/guides/all/create-eks-cluster-and-deploy-app.md#scaffolding-a-nodejs-app)

### Ephemeral environments in the cloud[â](#ephemeral-environments-in-the-cloud "Direct link to Ephemeral environments in the cloud")

* [Manage a Developer Environment Lifecycle](/guides/all/create-dev-env.md) Create a Terraform based Development Environment and show its details in Port

* [Create a new AWS account with GitLab](/guides/all/create-new-aws-account-gitlab.md)<br /><!-- -->Instantly provision isolated AWS accounts for your teams using a GitLab-driven workflow.

* [Manage a Kubernetes namespace](/guides/all/manage-kubernetes-namespaces.md)<br /><!-- -->Empower developers to create, update, or delete Kubernetes namespaces on demandâno tickets required.

### Leverage 3rd party systems to manage IaC[â](#leverage-3rd-party-systems-to-manage-iac "Direct link to Leverage 3rd party systems to manage IaC")

* [Trigger Terraform Cloud via webhook](/actions-and-automations/setup-backend/webhook/terraform-cloud/.md)<br /><!-- -->Automate infrastructure changes by kicking off Terraform Cloud runs directly from Port.

* [Trigger a Spacelift stack](/guides/all/trigger-spacelift-stack.md)<br /><!-- -->Launch and manage Spacelift stacks with a single click for streamlined environment provisioning.
