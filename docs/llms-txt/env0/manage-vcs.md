# Source: https://docs.envzero.com/guides/admin-guide/manage-vcs.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing VCS

> Connect version control systems to env zero for GitOps workflows, PR plans, and continuous deployment

env zero makes it simple for teams to connect their code repositories. This connection simplifies how you manage your infrastructure code by automatically updating env zero whenever your repository changes. This means less manual work, consistent environments, better tracking of changes, and improved teamwork between developers and operations.

Integrating your VCS is a key enabler of a GitOps workflow. For example, env zero's Pull Request (PR) plans automatically trigger a plan for your infrastructure code whenever changes are committed. This allows teams to continue using their familiar tools while env zero enhances their Infrastructure as Code (IaC) processes with features like PR plan/apply via comments and Continuous Deployment.

These capabilities streamline GitOps adoption by automating PR plan triggers, generating pull requests for review, and seamlessly applying updates to your infrastructure. Continuous Deployment further simplifies workflows by automatically redeploying and executing the complete IaC lifecycle - initializing, planning, and applying - with each code commit. This results in faster iteration within testing environments and reduces the need for manual reviews.

**With VCS integration, you gain access to all these capabilities**:

* [Plan on Pull Request](/guides/admin-guide/environments/plan-on-pull-request)
* [Continuous Deployment](/guides/admin-guide/environments/continuous-deployment)
* [PR Comments Commands](/guides/admin-guide/environments/plan-and-apply-from-pr-comments)
* [Module Registry](/guides/admin-guide/private-registry)
* [Project-level Custom Flow](/guides/admin-guide/custom-flows/project-level-custom-flow)
* [Approval Policies](/guides/policies-governance/approval-policies)
* [Create a pull request (Code Generation)](/guides/policies-governance/drift-detection-policy)

env zero seamlessly integrates with several popular Version Control System (VCS) providers to bring you the benefits of GitOps for your Infrastructure as Code. Currently, env zero natively supports:

* [GitHub](/guides/admin-guide/templates/github-templates)
* [GitLab](/guides/admin-guide/templates/gitlab-integration)
* [Bitbucket](/guides/admin-guide/templates/bitbucket-integration)
* [Azure DevOps](/guides/admin-guide/templates/azure-devops-integration)
* [GitHub Enterprise Server](/guides/admin-guide/templates/github-enterprise-integration) (Self-Hosted)
* [Bitbucket Data Center (Server)](/guides/admin-guide/templates/bitbucket-server-integration) (Self-Hosted)
* [Offline GitLab](/guides/admin-guide/templates/gitlab-enterprise-integration) (Self-Hosted)
* [Git Server](/guides/admin-guide/templates/#manage-git-connectivity) (Self-Hosted) - This basic integration allows actions like git clone, but does not support advanced features such as automated PR plans or Continuous Deployment.

<Warning>
  VCS Self-hosted - Connecting to self-hosted version control systems requires deploying and running the [VCS Agent](/guides/admin-guide/self-hosted-kubernetes-agent/standalone-docker-agent/#running-a-vcs-agent-for-on-prem--self-hosted-vcs)
</Warning>

## Centralized Management

All your VCS integrations can be managed and configured under the Organization settings.

<Note>
  This section allows you to manage your Self-Hosted VCS and GitHub Code Write connections only.
</Note>

Go to your Organization Settings and select the VCS tab. From there, you can edit existing connections or create new ones.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/pcx_nh6zT3at7dYL/images/guides/admin-guide/63cf466a617518ea407f6eff7e2ea21e4b132264a525c4d59a212bb4fc30b184-image.png?fit=max&auto=format&n=pcx_nh6zT3at7dYL&q=85&s=9388bf379c3d6fdd2b78eccb5ec3ff74" alt="Interface screenshot showing configuration options" width="806" height="733" data-path="images/guides/admin-guide/63cf466a617518ea407f6eff7e2ea21e4b132264a525c4d59a212bb4fc30b184-image.png" />
</Frame>

1. In this modal, select the relevant VCS provider. Options are separated into Cloud and Self-Hosted categories.
2. Choose  **[env zero Access](/guides/admin-guide/manage-vcs/#connection-types)**
   1. If you see the label 'Not Configured,' it indicates that this connection has not yet been saved in env zero.
3. Choose **[Authentication Type](/guides/admin-guide/manage-vcs/#authentication-types)**
   1. Each VCS supports different Authentication Types. If only one option is available, it will be selected by default.
4. Provide the necessary authentication information.
5. Click 'Save Connection' to save these details to env zero.
   1. Remember to click 'Save' to apply any changes you make to the VCS connection.

### VCS Actions

Within this modal, please confirm that the appropriate connection type is chosen. Additionally, you can perform the following actions:

* Delete Connection
  * Deleting the connection here will remove all related details from env zero. To revoke access from the VCS itself, you'll need to do so within your VCS provider's settings.
* Display connection health
* Display Available Repositories
* [Display Webhook Settings](/guides/admin-guide/templates/self-hosted-vcs#configure-webhook-integration) - These are the settings you need to configure within your self-hosted VCS to enable automatic triggering of features.

### Connection Types

<Info>
  **Repositories Access**

  For any connection type, you can specify which repositories env zero can access. For example, you might grant env zero access to both `repoX` and `repoY` for deployments, but limit code writing access to only `repoX`.
</Info>

* **Deployment**
  * Using this connection, env zero can deploy resources for your organization and enable all the features offered by CI/CD and governance
* **Code Write**
  * This connection allows env zero to commit code changes and generate AI-driven pull requests on your behalf. This capability powers features such as automatically creating pull requests to synchronize cloud environment changes with your code repository.

### Authentication Types

* **OAuth**
  * When you click the 'Grant Access' button, a pop-up window will appear. You'll need to authorize env zero to access your resources. After the pop-up closes (if successful), click 'Save Connection'.
* **By VCS Agent**
  * You need to have an active [VCS Agent running](/guides/admin-guide/templates/self-hosted-vcs#configure-vcs-agent-proxy). Then, provide the VCS URL and select the specific VCS Agent that env zero should connect to.

Built with [Mintlify](https://mintlify.com).
