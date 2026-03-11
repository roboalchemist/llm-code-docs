# Source: https://docs.envzero.com/guides/admin-guide/templates/gitlab-enterprise-integration.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Gitlab Enterprise Integration

> Integrate GitLab Enterprise with env zero using self-hosted agents for secure on-premises deployments

<Note>
  Note

  Gitlab Enterprise is only supported on env zero Organizations signed up for our [Self-Hosted Agent](/guides/overview/security-overview/#self-hosted-agents).
</Note>

## Initial GitLab Enterprise Setup

For env zero to be able to clone your code and post back commit statuses when running [Plan on Pull Request](/guides/admin-guide/environments/plan-on-pull-request) you need to provide it with an access token with write permissions.

This only needs to be done once for your Organization.

1. Create a [Personal access token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#create-a-personal-access-token) on your GitLab Enterprise.

* We recommend creating the token for a bot user - as that is the user that will post back commit statuses and comments.
* The user must have access to each repository you would like to be able to use with env zero. For each project, the user should have at least Maintainer/Owner permissions.
* The token must have the “read\_repository” and "api" scopes defined.

1. Encode the personal access token in base64, and use it in the K8S agent installation process as a helm value - `gitlabEnterpriseCredentialsEncoded`. Check out our [Self-Hosted K8S agent docs](/guides/admin-guide/self-hosted-kubernetes-agent/#customoptional-configuration) for more information.
2. Install/update the agent with the new value

## Webhooks Integration

Adding Webhooks is required in order to support [Continuous Deployment](/guides/admin-guide/environments/continuous-deployment) and our [Plan on Pull Request](/guides/admin-guide/environments/plan-on-pull-request) features on Gitlab Enterprise.

1. Open your repository page in GitLab Enterprise.
2. Click on the settings icon.
3. Enter the **Webhooks** page.
4. Copy and paste the URL and Secret values from the env0 Template creation page.
   1. Navigate to env zero > Organization Settings > VCS tab.
   2. Find your Gitlab Self-Hosted connection, and click the pencil icon.
   3. In the modal that pops up, click on '"Webhook Settings".
   4. A new modal will pop up that contains the Webhook URL and Webhook Secret.
5. Check the "Push events", "Merge request events" and "Comments" events.
6. Click on the "Add webhook" button.

<Frame caption="GitLab Enterprise webhook creation">
  <img src="https://mintcdn.com/envzero-b61043c8/NFoAIaj_CGEzw-yg/images/guides/admin-guide/templates/gitlab_enterprise_webhook_creation_interface.jpg?fit=max&auto=format&n=NFoAIaj_CGEzw-yg&q=85&s=2cde1af5e630f2be2c2202dd421397de" alt="GitLab Enterprise webhook creation interface" width="2807" height="1601" data-path="images/guides/admin-guide/templates/gitlab_enterprise_webhook_creation_interface.jpg" />
</Frame>

Built with [Mintlify](https://mintlify.com).
