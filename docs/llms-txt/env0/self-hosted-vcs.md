# Source: https://docs.envzero.com/guides/admin-guide/templates/self-hosted-vcs.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using Self-Hosted VCS

> Connect self-hosted VCS providers to env zero with agent proxy support for secure on-premises Git workflows

Easily connect your Self Hosted VCS to env zero. Once set up, you can effortlessly create self-hosted VCS [templates](/guides/admin-guide/templates) and [VCS environments](/guides/admin-guide/environments/#based-on-a-direct-vcs-integration) within the system. Manage all VCS connections in a centralized page, allowing you to apply changes across all templates and environments.

<Note>
  **This feature is available exclusively to customers using [self-hosted agents](/guides/admin-guide/self-hosted-kubernetes-agent)**
</Note>

<Info>
  **Supported VCS**

* [GitHub Enterprise Server](https://docs.github.com/en/enterprise-server)
* [Bitbucket Data Center](https://www.atlassian.com/software/bitbucket/enterprise/data-center) (Server)
* [Offline GitLab](https://docs.gitlab.com/ee/topics/offline/)
</Info>

**Using a self-hosted VCS provides you with all the features similar to a cloud-based VCS**. including:

* [Plan on Pull Request](/guides/admin-guide/environments/plan-on-pull-request)
* [Continuous Deployment](/guides/admin-guide/environments/continuous-deployment)
* [PR Comments Commands](/guides/admin-guide/environments/plan-and-apply-from-pr-comments)
* [Module Registry](/guides/admin-guide/private-registry)
* [Project-level Custom Flow](/guides/admin-guide/custom-flows/project-level-custom-flow)
* [Approval Policies](/guides/policies-governance/approval-policies)

## Add New VCS Connection

You can create a new connection in two ways; when creating a new template or through centralized management.

### Option 1 - Create VCS Connection from Template Creation

1. When configuring the VCS type, select one of the self-hosted supported VCS options.
2. Click the Repository dropdown and select "Add VCS Connection".

<img src="https://mintcdn.com/envzero-b61043c8/NFoAIaj_CGEzw-yg/images/guides/admin-guide/templates/77b5c437bbc65dc674deecf57e1f9beb230a842b448cd97562721d59c3e2e52d-image.png?fit=max&auto=format&n=NFoAIaj_CGEzw-yg&q=85&s=317c6569e976a3e73538aa9dc9102ccb" alt="" width="794" height="551" data-path="images/guides/admin-guide/templates/77b5c437bbc65dc674deecf57e1f9beb230a842b448cd97562721d59c3e2e52d-image.png" />

### Option 2 - Create VCS Connection from VCS Settings

1. Go to "Organization Settings," select the "VCS" tab, and scroll down.
2. Click "Create Connection"

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/NFoAIaj_CGEzw-yg/images/guides/admin-guide/templates/528a32db423ddd446f036f9c73787905af85a8180b0c44a174e7c4d8a2405fa1-image.png?fit=max&auto=format&n=NFoAIaj_CGEzw-yg&q=85&s=b072509d0f7f21043b1b85ab96822010" alt="Interface screenshot showing configuration options" width="582" height="389" data-path="images/guides/admin-guide/templates/528a32db423ddd446f036f9c73787905af85a8180b0c44a174e7c4d8a2405fa1-image.png" />
</Frame>

### Create VCS Connection

1. Choose Self-Hosted in the picker

2. Choose the VCS type and click **Add** for **Deployment** access.

   <Frame>
     <img src="https://mintcdn.com/envzero-b61043c8/NFoAIaj_CGEzw-yg/images/guides/admin-guide/templates/27fdbdf533706548ccabf057a710f0e49f871b106cfbf7a8fde98cd071af8b68-image.png?fit=max&auto=format&n=NFoAIaj_CGEzw-yg&q=85&s=046e6e56f77bba22d350a8d937bec213" alt="Interface screenshot showing configuration options" width="847" height="519" data-path="images/guides/admin-guide/templates/27fdbdf533706548ccabf057a710f0e49f871b106cfbf7a8fde98cd071af8b68-image.png" />
   </Frame>

3. Enter Self-Hosted VCS URL

4. Select the "Agent Key" to which all requests will be forwarded ([VCS Agent](/guides/admin-guide/templates/self-hosted-vcs/#configure-vcs-agent-proxy) - Running Proxy).

   1. To create a new agent key, please contact support.
   2. The dropdown is available only to users with the "[Edit Organization Settings](/guides/admin-guide/user-role-and-team-management/custom-roles/#custom-role-permissions)" permission.
   3. <Frame>
        <img src="https://mintcdn.com/envzero-b61043c8/NFoAIaj_CGEzw-yg/images/guides/admin-guide/templates/bfa206944f1c178c9de6e1365e1a5da27b6269cb1b76141772d14c8202a6834f-image.png?fit=max&auto=format&n=NFoAIaj_CGEzw-yg&q=85&s=c97a46159347517ff851ad7e6670943b" alt="Interface screenshot showing configuration options" width="598" height="592" data-path="images/guides/admin-guide/templates/bfa206944f1c178c9de6e1365e1a5da27b6269cb1b76141772d14c8202a6834f-image.png" />
      </Frame>

5. Click "Save Connection"

<Info>
  **Forward requests to this VCS Agent**

  The intention behind forwarding requests refers to all the requests the platform needs to support the features mentioned above. It does not refer to where the deployment actually runs; it will continue to run based on the project to which it is assigned.
</Info>

### Configure VCS agent (Proxy)

Running a proxy can be achieved in two ways; as part of the agent's Kubernetes helm chart deployment or as a standalone Docker instance.

#### Agent's Kubernetes Helm Chart

1. The [installation](/guides/admin-guide/self-hosted-kubernetes-agent/#installation) is included as part of the agent's Kubernetes Helm chart deployment.
2. By default, the proxy runs when the agent is installed without any special configuration.
3. Proxy Configuration: Configure it in the [values.yml](/guides/admin-guide/self-hosted-kubernetes-agent/#installation) file

   1. ```yaml  theme={null}
      agentProxy:
       install: true # default true
       replicas: 1 # how many replicas of the agent proxy to use. Default is 1
       maxConcurrentRequests: 500 # how many concurrent requests each pod should handle. Default is 500
       limits: # k8s (cpu and memory) limits. Default is 250m and 500Mi
        cpu: 250m
        memory: 500Mi
      bitbucketServerCredentialsEncoded: base64= # Base64 Bitbucket server credentials in the format `username:token (using a Personal Access token)
      gitlabEnterpriseCredentialsEncoded: base64= # Base64 Gitlab Enterprise credentials in the form of an Access token 
      githubEnterpriseAppId: 1 # For more details, check out /guides/admin-guide/templates/github-enterprise-integration
      githubEnterpriseAppInstallationId: 1
      githubEnterpriseAppPrivateKeyEncoded: "base64=="
      ```

      Refer to the Self Hosted Kubernetes Agent [specifications](/guides/admin-guide/self-hosted-kubernetes-agent/#customoptional-configuration) for additional configuration details.

#### Standalone VCS Agent Docker Instance

1. Run the VCS agent Docker image with the following command:

   ```shell  theme={null}
   docker run --env-file ~/path/to/env0.env ghcr.io/env0/vcs-agent:latest
   ```

2. For more details, see Standalone Docker Agent - [Running a VCS Agent](/guides/admin-guide/self-hosted-kubernetes-agent/standalone-docker-agent/#running-a-vcs-agent-for-on-prem--self-hosted-vcs).

<Info>
  **env zero communication with VCS Agent**

  The communication is one-way: the VCS agent connects to the env zero platform. This means that when the env zero platform forwards a request to the VCS agent, we cannot immediately determine if the communication was successful or if the proxy is alive until the timeout period (\~25s).

  If something isn't working as expected, check the VCS agent logs to see if the requests are being received
</Info>

### Configure Webhook Integration

This section outlines the steps required to configure webhook integration for your VCS. Follow the instructions to set up the webhook and ensure it works seamlessly with your system.

1. When you [Create VCS connection](/guides/admin-guide/templates/self-hosted-vcs/#create-vcs-connection) you will find the **Webhook Settings** button.

   1. <Frame>
        <img src="https://mintcdn.com/envzero-b61043c8/NFoAIaj_CGEzw-yg/images/guides/admin-guide/templates/03e5d6ced669a74341e747c24302c9b31661e75c918f5a94273842be86eb3271-image.png?fit=max&auto=format&n=NFoAIaj_CGEzw-yg&q=85&s=619d41b18978e90f516a0ebbe692dcaf" alt="Interface screenshot showing configuration options" width="407" height="329" data-path="images/guides/admin-guide/templates/03e5d6ced669a74341e747c24302c9b31661e75c918f5a94273842be86eb3271-image.png" />
      </Frame>
2. At the bottom of the window, you will see this section. From here, you need to obtain the **webhook URL** and **webhook secret**.
3. Configure Webhook Integration per Self-Hosted VCS:
   1. [Github Enterprise](/guides/admin-guide/templates/github-enterprise-integration)
   2. [Bitbucket Server](/guides/admin-guide/templates/bitbucket-server-integration)
   3. [Gitlab Enterprise](/guides/admin-guide/templates/gitlab-enterprise-integration)

<Warning>
  **Please ensure that only one entry is created for Webhook Integration. Creating multiple entries may result in duplicate events and cause multiple deployments for the same change.**
</Warning>

Built with [Mintlify](https://mintlify.com).
