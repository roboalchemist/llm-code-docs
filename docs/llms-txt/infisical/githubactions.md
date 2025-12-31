# Source: https://infisical.com/docs/integrations/cicd/githubactions.md

# GitHub Actions

> How to sync secrets from Infisical to GitHub Actions

<Note>
  Alternatively, you can use Infisical's official GitHub Action
  [here](https://github.com/Infisical/secrets-action).
</Note>

Infisical lets you sync secrets to GitHub at the organization-level, repository-level, and repository environment-level.

## Connecting with GitHub App (Recommended)

<Tabs>
  <Tab title="Usage">
    <Steps>
      <Step title="Authorize GitHub Infisical App">
        Navigate to your project's integrations tab in Infisical and press on the GitHub tile.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/github/app/integration-overview.png" alt="integrations" />

        Select GitHub App as the authentication method and click **Connect to GitHub**.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/github/app/github-app-method-selection.png" alt="integrations github app auth selection" />

        You will then be redirected to the GitHub app installation page.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/github/app/github-app-installation.png" alt="integrations github app installation" />

        Install and authorize the GitHub application. This will redirect you back to the Infisical integration page.
      </Step>

      <Step title="Configure Infisical GitHub integration">
        Select which Infisical environment secrets you want to sync to which GitHub organization, repository, or repository environment.

        <Tabs>
          <Tab title="Repository">
                        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/github/integrations-github-scope-repo.png" alt="integrations github" />
          </Tab>

          <Tab title="Organization">
                        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/github/integrations-github-scope-org.png" alt="integrations github" />

            When using the organization scope, your secrets will be saved in the top-level of your GitHub Organization.

            You can choose the visibility, which defines which repositories can access the secrets. The options are:

            * **All public repositories**: All public repositories in the organization can access the secrets.
            * **All private repositories**: All private repositories in the organization can access the secrets.
            * **Selected repositories**: Only the selected repositories can access the secrets. This gives a more fine-grained control over which repositories can access the secrets. You can select *both* private and public repositories with this option.
          </Tab>

          <Tab title="Repository Environment">
                        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/github/integrations-github-scope-env.png" alt="integrations github" />
          </Tab>
        </Tabs>

        Finally, press create integration to start syncing secrets to GitHub.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/github/integrations-github.png" alt="integrations github" />
      </Step>
    </Steps>
  </Tab>

  <Tab title="Self-Hosted Setup">
    Using the GitHub integration with app authentication on a self-hosted instance of Infisical requires configuring an application on GitHub
    and registering your instance with it.

    <Steps>
      <Step title="Create an application on GitHub">
        Navigate to the GitHub app settings [here](https://github.com/settings/apps). Click **New GitHub App**.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/github/app/self-hosted-github-app-create.png" alt="integrations github app create" />

        Give the application a name, a homepage URL (your self-hosted domain i.e. `https://your-domain.com`), and a callback URL (i.e. `https://your-domain.com/integrations/github/oauth2/callback`).

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/github/app/self-hosted-github-app-basic-details.png" alt="integrations github app basic details" />

        Enable request user authorization during app installation.
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/github/app/self-hosted-github-app-enable-oauth.png" alt="integrations github app enable auth" />

        Disable webhook by unchecking the Active checkbox.
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/github/app/self-hosted-github-app-webhook.png" alt="integrations github app webhook" />

        Set the repository permissions as follows: Metadata: Read-only, Secrets: Read and write, Environments: Read and write, Actions: Read.
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/github/app/self-hosted-github-app-repository.png" alt="integrations github app repository" />

        Similarly, set the organization permissions as follows: Secrets: Read and write.
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/github/app/self-hosted-github-app-organization.png" alt="integrations github app organization" />

        Create the Github application.
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/github/app/self-hosted-github-app-create-confirm.png" alt="integrations github app create confirm" />

        <Note>
          If you have a GitHub organization, you can create an application under it
          in your organization Settings > Developer settings > GitHub Apps > New GitHub App.
        </Note>
      </Step>

      <Step title="Add your application credentials to Infisical">
        Generate a new **Client Secret** for your GitHub application.
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/github/app/self-hosted-github-app-secret.png" alt="integrations github app create secret" />

        Generate a new **Private Key** for your Github application.
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/github/app/self-hosted-github-app-private-key.png" alt="integrations github app create private key" />

        Obtain the necessary Github application credentials. This would be the application slug, client ID, app ID, client secret, and private key.
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/github/app/self-hosted-github-app-credentials.png" alt="integrations github app credentials" />

        Back in your Infisical instance, add the five new environment variables for the credentials of your GitHub application:

        * `CLIENT_ID_GITHUB_APP`: The **Client ID** of your GitHub application.
        * `CLIENT_SECRET_GITHUB_APP`: The **Client Secret** of your GitHub application.
        * `CLIENT_SLUG_GITHUB_APP`: The **Slug** of your GitHub application. This is the one found in the URL.
        * `CLIENT_APP_ID_GITHUB_APP`: The **App ID** of your GitHub application.
        * `CLIENT_PRIVATE_KEY_GITHUB_APP`: The **Private Key** of your GitHub application.

        Once added, restart your Infisical instance and use the GitHub integration via app authentication.
      </Step>
    </Steps>
  </Tab>
</Tabs>

## Connecting with GitHub OAuth

Prerequisites:

* Set up and add envars to [Infisical Cloud](https://app.infisical.com)
* Ensure that you have admin privileges to the repository you want to sync secrets to.

<Tabs>
  <Tab title="Usage">
    <Steps>
      <Step title="Authorize Infisical for GitHub">
        Navigate to your project's integrations tab in Infisical and press on the GitHub tile.
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/github/integration-overview.png" alt="integrations" />

        Select OAuth as the authentication method and click **Connect to GitHub**.
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/github/github-oauth-method-selection.png" alt="integrations github oauth auth selection" />

        Grant Infisical access to your GitHub account (organization and repo privileges).
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/github/integrations-github-auth.png" alt="integrations github authorization" />
      </Step>

      <Step title="Configure Infisical GitHub integration">
        Select which Infisical environment secrets you want to sync to which GitHub organization, repository, or repository environment.

        <Tabs>
          <Tab title="Repository">
                        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/github/integrations-github-scope-repo.png" alt="integrations github" />
          </Tab>

          <Tab title="Organization">
                        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/github/integrations-github-scope-org.png" alt="integrations github" />

            When using the organization scope, your secrets will be saved in the top-level of your GitHub Organization.

            You can choose the visibility, which defines which repositories can access the secrets. The options are:

            * **All public repositories**: All public repositories in the organization can access the secrets.
            * **All private repositories**: All private repositories in the organization can access the secrets.
            * **Selected repositories**: Only the selected repositories can access the secrets. This gives a more fine-grained control over which repositories can access the secrets. You can select *both* private and public repositories with this option.
          </Tab>

          <Tab title="Repository Environment">
                        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/github/integrations-github-scope-env.png" alt="integrations github" />
          </Tab>
        </Tabs>

        Finally, press create integration to start syncing secrets to GitHub.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/github/integrations-github.png" alt="integrations github" />
      </Step>
    </Steps>
  </Tab>

  <Tab title="Self-Hosted Setup">
    Using the GitHub integration on a self-hosted instance of Infisical requires configuring an OAuth application in GitHub
    and registering your instance with it.

    <Steps>
      <Step title="Create an OAuth application in GitHub">
        Navigate to your user Settings > Developer settings > OAuth Apps to create a new GitHub OAuth application.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/github/integrations-github-config-settings.png" alt="integrations github config" />
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/github/integrations-github-config-dev-settings.png" alt="integrations github config" />
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/github/integrations-github-config-new-app.png" alt="integrations github config" />

        Create the OAuth application. As part of the form, set the **Homepage URL** to your self-hosted domain `https://your-domain.com`
        and the **Authorization callback URL** to `https://your-domain.com/integrations/github/oauth2/callback`.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/github/integrations-github-config-new-app-form.png" alt="integrations github config" />

        <Note>
          If you have a GitHub organization, you can create an OAuth application under it
          in your organization Settings > Developer settings > OAuth Apps > New Org OAuth App.
        </Note>
      </Step>

      <Step title="Add your OAuth application credentials to Infisical">
        Obtain the **Client ID** and generate a new **Client Secret** for your GitHub OAuth application.

                <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/integrations/github/integrations-github-config-credentials.png" alt="integrations github config" />

        Back in your Infisical instance, add two new environment variables for the credentials of your GitHub OAuth application:

        * `CLIENT_ID_GITHUB`: The **Client ID** of your GitHub OAuth application.
        * `CLIENT_SECRET_GITHUB`: The **Client Secret** of your GitHub OAuth application.

        Once added, restart your Infisical instance and use the GitHub integration.
      </Step>
    </Steps>
  </Tab>
</Tabs>
