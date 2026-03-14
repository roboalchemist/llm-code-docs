# Source: https://docs.envzero.com/guides/admin-guide/self-hosted-kubernetes-agent/standalone-docker-agent.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Running a Standalone Docker Agent

> Run the env zero self-hosted agent as a standalone Docker container without Kubernetes

Choosing the docker agent is the quickest way to start running the self-hosted agent.

## Running a deployment-agent

1. Download the *Docker Configuration*(`env0.env` file) from the **Agents** tab under **Organization** > **Settings**.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/NFoAIaj_CGEzw-yg/images/guides/admin-guide/self-hosted-kubernetes-agent/bfa6b08-image.png?fit=max&auto=format&n=NFoAIaj_CGEzw-yg&q=85&s=a545278dc9973f6a9379eb2ead334821" alt="Interface screenshot showing configuration options" width="1746" height="492" data-path="images/guides/admin-guide/self-hosted-kubernetes-agent/bfa6b08-image.png" />
</Frame>

1. Create your state encryption key with the format of **base64 encoding**. (base64 encoding of any string you choose) and add it in `env0.env` as a new environment variable:\
   `ENV0_STATE_ENCRYPTION_KEY=<your-base64-encryption-key>`\
   ℹ️ This value will be used to encrypt and decrypt the environment state and working directory\
   ℹ️ Read more about the state encryption key [here](/guides/admin-guide/self-hosted-kubernetes-agent/env0-hosted-encrypted-state)
2. Run agent:\
   `docker run --env-file ~/path/to/env0.env ghcr.io/env0/deployment-agent:latest`

And that's it!

The agent should be marked as `Active` and be ready to handle deployments.

<Info>
  **Enabling Multi-Concurrency**

  Do you have multiple deployments waiting to run and you don't want to them to wait?

  Each container is designed to handle a single deployment at a time.

  **To run multiple deployments in parallel, just create another deployment agent using the** `docker run command`.  You can run any number of containers to satisfy your deployment needs.
</Info>

## Cloud Credential Configurations

These are optional configurations, and typically role authentication will be handled by native container service mechanisms.  See note below regarding exposing Environment Variables for native authentication.

| Keys                                                     | Description                                                                                                                                        |
| -------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ASSUMER_ACCESS_KEY_ID`<br />`ASSUMER_SECRET_ACCESS_KEY` | plaintext, access key and secret key user role that is used to assume the deployment credentials specified in the env zero project configurations. |

For GCP, and Azure you can embed the Environment Variables for GCP and Azure and use ADDITIONAL\_ENV\_VARS to expose them to the runner environment.

## Secrets

These are optional configurations, and typically will be handled by native authentication mechanisms in AWS, GCP, Azure if you're using the managed container services like ECS.

| Keys                                                                                           |                                                                                                                                                                                     |
| ---------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CUSTOMER_AWS_ACCESS_KEY_ID`<br />`CUSTOMER_AWS_SECRET_ACCESS_KEY`<br />`AWS_SECRETS_REGION`   | plaintext, access key & secret key user role that has the following permission: `secretsmanager:GetSecretValue`<br />`AWS_SECRETS_REGION`(optional) - default region is `us-east-1` |
| `USE_OIDC_FOR_AWS_SSM`                                                                         | When enabled, the agent will authenticate to AWS SSM using env zero OIDC                                                                                                            |
| `CUSTOM_ROLE_FOR_OIDC_AWS_SSM`<br />`CUSTOM_DURATION_FOR_OIDC_AWS_SSM`                         | Custom role for AWS SSM secret fetching, Note: only used when `USE_OIDC_FOR_AWS_SSM=true`                                                                                           |
| `CUSTOMER_VAULT_TOKEN`<br />`CUSTOMER_VAULT_ADDRESS`                                           | plaintext, using HashiCorp Vault to store secrets<br />Token should be a long lived token.                                                                                          |
| `CUSTOMER_GOOGLE_PROJECT`<br />`CUSTOMER_GOOGLE_CREDENTIALS`                                   | plaintext, Google service account credentials to fetch GCP secrets requires `Secret Manager Secret Access role`                                                                     |
| `CUSTOMER_AZURE_CLIENT_ID`<br />`CUSTOMER_AZURE_CLIENT_SECRET`<br />`CUSTOMER_AZURE_TENANT_ID` | plaintext, using Azure Key Vault Secrets to store secrets for the agent                                                                                                             |

## Cost Estimation

| Key                 | Description                                                               |
| :------------------ | :------------------------------------------------------------------------ |
| `INFRACOST_API_KEY` | Infracost API Key, create a personal / organizational key at infracost.io |

## Running a vcs-agent (for on-prem / self-hosted VCS)

In the case that you are using a self-hosted version control such as Bitbucket Server, GitLab Enterprise, GitHub Enterprise, you will need to run the `vcs-agent`.

It has to run **in parallel** with the `deployment-agent` in order to interact with private VCS.

1. Add credentials to the relevant VCS in `env0.env` file (see variables table below) as plaintext
2. Run docker:\
   `docker run --env-file ~/path/to/env0.env ghcr.io/env0/vcs-agent:latest`\
   ℹ️ env zero has a public docker registry on GitHub which is maintained [here](https://github.com/env0/agent/pkgs/container/vcs-agent).

| Keys                                                                                                                                                                                               | Description                                                                                                                                                                                                                               | Required for feature                      |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------- |
| `BITBUCKET_SERVER_CREDENTIALS`                                                                                                                                                                     | Bitbucket server credentials in the format `username:token` ([using a Personal Access token](https://confluence.atlassian.com/bitbucketserver076/personal-access-tokens-1026534797.html#Personalaccesstokens-usingpersonalaccesstokens)). | On-premise Bitbucket Server installation. |
| `GITLAB_ENTERPRISE_CREDENTIALS`                                                                                                                                                                    | Gitlab Enterprise credentials in the form of a [Personal Access token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#create-a-personal-access-token).                                                               | On-premise Gitlab Enterprise installation |
| `GITLAB_ENTERPRISE_BASE_URL_SUFFIX`                                                                                                                                                                | In cases where your GitLab instance base url is not at the root of the url, and in a separate path, e.g `https://gitlab.acme.com/prod` you should define that added suffix to this value<br />`GITLAB_ENTERPRISE_BASE_URL_SUFFIX=prod`    | On-premise Gitlab Enterprise installation |
| `GITHUB_ENTERPRISE_APP_ID`<br />`GITHUB_ENTERPRISE_APP_CLIENT_ID`<br />`GITHUB_ENTERPRISE_APP_INSTALLATION_ID`<br />`GITHUB_ENTERPRISE_APP_CLIENT_SECRET`<br />`GITHUB_ENTERPRISE_APP_PRIVATE_KEY` | [Github Enterprise Integration](/guides/admin-guide/templates/github-enterprise-integration) (see step 3)                                                                                                                                 | On-premise GitHub Enterprise installation |

## Exposing Custom Environment Variables

By default, env zero's runner will not expose all the environment variables defined in the container. This is to help ensure some safety, and isolating the container environment from the runner's environment. However, in certain scenarios, you may still want to expose environment variables defined in the container. For example, if you're running in AWS ECS, and you want to use the cluster role for authorization purposes.

| Key                   | Description                                                                                                                                                                                                                                                    |
| :-------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ADDITIONAL_ENV_VARS` | `["ENV_VAR_A", "ENV_VAR_B","ENV_VAR_C"]`<br />This single-quoted array will allow the runner environment to see the three environment variables listed in the list. This assume those environment variables were defined with the docker configuration itself. |

### AWS ECS

When defining a role for the container, AWS sets an environment `AWS_CONTAINER_CREDENTIALS_RELATIVE_URI` this variable should be added to the `ADDITIONAL_ENV_VARS` in order to be exposed to the runner environment.

For example, `ADDITIONAL_ENV_VARS=["AWS_CONTAINER_CREDENTIALS_RELATIVE_URI"]`

Built with [Mintlify](https://mintlify.com).
