# Source: https://mintlify.com/docs/deploy/gitlab.md

# GitLab

> Connect to a GitLab repository for automated deployments and preview builds.

We use access tokens and webhooks to authenticate and sync changes between GitLab and Mintlify.

* Mintlify uses access tokens to pull information from GitLab.
* GitLab uses webhooks to notify Mintlify when changes are made, enabling preview deployments for merge requests.

## Set up the connection

<Note>
  **HTTPS cloning required**: Your GitLab project must have HTTPS cloning enabled for Mintlify to access your repository. You can verify this in GitLab by going to your project's **Settings** > **General** > **Visibility and access controls** section.
</Note>

<Steps>
  <Step title="Find your project ID">
    In your GitLab project, navigate to **Settings** > **General** and locate your **Project ID**.

    <Frame>
      <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-id.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=4aae3ff6adbb509b607a63a4998992d0" alt="The General Settings page in the GitLab dashboard. The Project ID is highlighted." data-og-width="950" width="950" data-og-height="775" height="775" data-path="images/gitlab/gitlab-project-id.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-id.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=88f0bf511026ec7ed08f681ec90daf60 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-id.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=e724501d42bcadf2afee5a3383864b8f 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-id.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=7292cf914432f5773b27d0f7a26f77e8 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-id.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=df4fc24c66567b6fa8aaf96ef84be3db 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-id.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=c18b327b668e3111c2c365bd28804d4f 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-id.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=6d58f398e6a9dd837c15ef62bd84eca6 2500w" />
    </Frame>
  </Step>

  <Step title="Generate an access token">
    Navigate to **Settings** > **Access Tokens** and select **Add new token**.

    Configure the token with these settings:

    * **Name**: Mintlify
    * **Role**: Maintainer (required for private repos)
    * **Scopes**: `api` and `read_api`

    Click **Create project access token** and copy the token.

    <Note>
      If Project Access Tokens are not available, you can use a Personal Access Token instead. Note that Personal Access Tokens expire and must be updated.
    </Note>

    <Frame>
      <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-access-token.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=59ef23c54d88cdd723632086bced658b" alt="The Access tokens page in the GitLab dashboard. The settings to configure for Mintlify are highlighted." data-og-width="1166" width="1166" data-og-height="904" height="904" data-path="images/gitlab/gitlab-project-access-token.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-access-token.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=ed79687a8c28122d877619f87c2f10f5 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-access-token.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=eee224427bd45c62f4b300ff35e18c20 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-access-token.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=c58082216f7abcdca53dae175bc50e05 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-access-token.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=4391e8f8149b4750ce5727e90434d4cc 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-access-token.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=0b593dfe4be4578274123931ec3fd9a8 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-access-token.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=072f13cde75508169457c8bec172183f 2500w" />
    </Frame>
  </Step>

  <Step title="Set up the connection">
    In the [Mintlify dashboard](https://dashboard.mintlify.com/settings/deployment/git-settings):

    1. Enter your project ID and access token.
    2. Complete any other required configurations.
    3. Click **Save Changes**.

    <Frame>
      <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-config.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=882adfd7c2a3349608bc6240aa5b467d" alt="The Git Settings page in the Mintlify dashboard. The GitLab configuration settings are highlighted." data-og-width="2994" width="2994" data-og-height="1704" height="1704" data-path="images/gitlab/gitlab-config.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-config.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=92f573381038c697fb061a9793cbea4d 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-config.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=634591e44b502650a859b04aba4f3f07 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-config.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=82eda65fcc9475daf4c9d20eb1f5ac77 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-config.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=cc48a4ac66d50a65dcc4913111b26943 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-config.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=7932ae6cf49e9ba69d8133ff9f17fa23 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-config.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=106cb2e8a7eb3bdaef7f994bfcd31da8 2500w" />
    </Frame>
  </Step>
</Steps>

## Create the webhook

Webhooks allow us to receive events when changes are made so that we can
automatically trigger deployments.

<Steps>
  <Step title="Navigate to Settings > Webhooks and click 'Add new Webhook'">
    <Frame>
      <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-webhook.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=760e8faa2437ecf8ff2739c4dfa0bdc4" alt="Screenshot of the Webhooks page in the GitLab dashboard." data-og-width="3014" width="3014" data-og-height="1704" height="1704" data-path="images/gitlab/gitlab-webhook.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-webhook.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=08c3f527fcd75de5c88682d6fc08018e 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-webhook.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=c7579b9b8372dc9781dd1da38b1e404e 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-webhook.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=a0225726564aa9987b44bfb35f750c35 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-webhook.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=006a5aa0f321344da2d528c928f3bf4d 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-webhook.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=99c65eb0a83da2b793c1608ea3a47cbc 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-webhook.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=a8943cc826fc0bb2ab6db79ece619d8c 2500w" />
    </Frame>
  </Step>

  <Step title="Set up URL and webhook">
    In the "URL" field, enter the endpoint `https://leaves.mintlify.com/gitlab-webhook` and name the webhook "Mintlify".
  </Step>

  <Step title="Paste token">
    Paste the Webhook token generated after setting up the connection.

    <Frame>
      <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-show-webtoken.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=60c68dd86fa476e90af8cec2e5ee7c81" alt="Screenshot of the GitLab connection in the Mintlify dashboard. The Show Webtoken button is highlighted." data-og-width="555" width="555" data-og-height="527" height="527" data-path="images/gitlab/gitlab-show-webtoken.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-show-webtoken.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=90210c502642ebd9e493440279b675b7 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-show-webtoken.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=6533a778a099d0c4fc65e04e64587444 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-show-webtoken.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=6f4e8533153ee8efa98864377656a377 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-show-webtoken.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=b29eaa2ea7df3ca4e21fba49835a8360 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-show-webtoken.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=c1e857545a40103103e5958f03faecc7 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-show-webtoken.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=74798e74cae86d02520e756f0d7cfb37 2500w" />
    </Frame>
  </Step>

  <Step title="Select events">
    Select these events to trigger the webhook:

    * **Push events** (All branches)
    * **Merge requests events**

    When you're done it should look like this:

    <Frame>
      <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-webtoken.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=00c0ce70ce9e8dbc2712f71aaeef3362" alt="The Webhook page in the GitLab dashboard. The settings to configure for Mintlify are highlighted." data-og-width="1161" width="1161" data-og-height="1740" height="1740" data-path="images/gitlab/gitlab-project-webtoken.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-webtoken.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=d78ea01ef0a043783195c6d548d20eea 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-webtoken.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=b77667d112aa91a2db02ab5fb356f733 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-webtoken.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=7b2f55fe589a11b9e5ce5633b62c34ad 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-webtoken.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=531491f03816a11e44b651c921dc1789 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-webtoken.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=24770ed142d0cf9b7bfb0dc307c13449 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-webtoken.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=e8644419580dc23875105fb06f3f4433 2500w" />
    </Frame>
  </Step>

  <Step title="Test the Webhook">
    After creating the Webhook, click the "Test" dropdown and select "Push events" to send a sample payload to ensure it's configured correctly. It'll say "Hook executed successfully: HTTP 200" if configured correctly.

    This will help you verify that everything is working correctly and that your documentation will sync properly with your GitLab repository.

    <Frame>
      <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-webtoken-test.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=3ad52f7ac39124a4c03944256d0b79d3" alt="Screenshot of the GitLab Webhooks page. The 'Push events' menu item is highlighted in the 'Test' menu." data-og-width="1161" width="1161" data-og-height="724" height="724" data-path="images/gitlab/gitlab-project-webtoken-test.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-webtoken-test.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=d174db5e7ba73d19a9431adca65ebe6c 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-webtoken-test.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=9dfb2d09246cb81c0074a2a429e940f7 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-webtoken-test.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=3db14fb7784c9380f627336622f73a8f 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-webtoken-test.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=68dc65bc33081a8a08c869f7f1ea8761 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-webtoken-test.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=ebd368461ffa4880d63a3ecbda59d84e 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-webtoken-test.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=1e510fe852d154bb8aca3dd2c20387aa 2500w" />
    </Frame>
  </Step>
</Steps>
