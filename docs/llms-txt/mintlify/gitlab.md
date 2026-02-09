# Source: https://www.mintlify.com/docs/deploy/gitlab.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.mintlify.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

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
      <img src="https://mintcdn.com/mintlify/TMkAdDUtcJGNvRU5/images/gitlab/gitlab-config-light.png?fit=max&auto=format&n=TMkAdDUtcJGNvRU5&q=85&s=98809a957ecd59f3d2f2bd747086c5a2" alt="The GitLab configuration panel in the Git Settings page of the Mintlify dashboard." className="block dark:hidden" data-og-width="1096" width="1096" data-og-height="980" height="980" data-path="images/gitlab/gitlab-config-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/TMkAdDUtcJGNvRU5/images/gitlab/gitlab-config-light.png?w=280&fit=max&auto=format&n=TMkAdDUtcJGNvRU5&q=85&s=d126923362e8a1a04c5c363cc763d4c9 280w, https://mintcdn.com/mintlify/TMkAdDUtcJGNvRU5/images/gitlab/gitlab-config-light.png?w=560&fit=max&auto=format&n=TMkAdDUtcJGNvRU5&q=85&s=97f88b329f0ace8ab59777844583144a 560w, https://mintcdn.com/mintlify/TMkAdDUtcJGNvRU5/images/gitlab/gitlab-config-light.png?w=840&fit=max&auto=format&n=TMkAdDUtcJGNvRU5&q=85&s=07081ed0cb66ee2ce008d8b3dbecf462 840w, https://mintcdn.com/mintlify/TMkAdDUtcJGNvRU5/images/gitlab/gitlab-config-light.png?w=1100&fit=max&auto=format&n=TMkAdDUtcJGNvRU5&q=85&s=0c7d8715659c16920627eb0e57fb2605 1100w, https://mintcdn.com/mintlify/TMkAdDUtcJGNvRU5/images/gitlab/gitlab-config-light.png?w=1650&fit=max&auto=format&n=TMkAdDUtcJGNvRU5&q=85&s=1315b468f05d1a9036b979e3a975b885 1650w, https://mintcdn.com/mintlify/TMkAdDUtcJGNvRU5/images/gitlab/gitlab-config-light.png?w=2500&fit=max&auto=format&n=TMkAdDUtcJGNvRU5&q=85&s=c930bbb01934b367591f5f431040569b 2500w" />

      <img src="https://mintcdn.com/mintlify/TMkAdDUtcJGNvRU5/images/gitlab/gitlab-config-dark.png?fit=max&auto=format&n=TMkAdDUtcJGNvRU5&q=85&s=b4834ea4d6ebf771b7af095589a194ac" alt="The GitLab configuration panel in the Git Settings page of the Mintlify dashboard." className="hidden dark:block" data-og-width="1096" width="1096" data-og-height="980" height="980" data-path="images/gitlab/gitlab-config-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/TMkAdDUtcJGNvRU5/images/gitlab/gitlab-config-dark.png?w=280&fit=max&auto=format&n=TMkAdDUtcJGNvRU5&q=85&s=8d373c471a7f164d54366aa9e2945b70 280w, https://mintcdn.com/mintlify/TMkAdDUtcJGNvRU5/images/gitlab/gitlab-config-dark.png?w=560&fit=max&auto=format&n=TMkAdDUtcJGNvRU5&q=85&s=42b8beb83e53ee846ce1088b31711e2b 560w, https://mintcdn.com/mintlify/TMkAdDUtcJGNvRU5/images/gitlab/gitlab-config-dark.png?w=840&fit=max&auto=format&n=TMkAdDUtcJGNvRU5&q=85&s=1be52531d1bdd832f47a546f3add357d 840w, https://mintcdn.com/mintlify/TMkAdDUtcJGNvRU5/images/gitlab/gitlab-config-dark.png?w=1100&fit=max&auto=format&n=TMkAdDUtcJGNvRU5&q=85&s=bd77c60ab1d2829ea4f5be0f3b17c9ad 1100w, https://mintcdn.com/mintlify/TMkAdDUtcJGNvRU5/images/gitlab/gitlab-config-dark.png?w=1650&fit=max&auto=format&n=TMkAdDUtcJGNvRU5&q=85&s=32f2f35d16704fa661ccf963a7d47635 1650w, https://mintcdn.com/mintlify/TMkAdDUtcJGNvRU5/images/gitlab/gitlab-config-dark.png?w=2500&fit=max&auto=format&n=TMkAdDUtcJGNvRU5&q=85&s=d3428778d1c96107c42ebfa2f0e570dc 2500w" />
    </Frame>
  </Step>
</Steps>

## Create the webhook

Webhooks allow us to receive events when changes are made so that we can
automatically trigger deployments.

<Steps>
  <Step title="Add new webhook">
    1. In GitLab, navigate to **Settings** > **Webhooks**.
    2. Click **Add new webhook**.

    <Frame>
      <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-webhook.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=760e8faa2437ecf8ff2739c4dfa0bdc4" alt="Screenshot of the Webhooks page in the GitLab dashboard." data-og-width="3014" width="3014" data-og-height="1704" height="1704" data-path="images/gitlab/gitlab-webhook.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-webhook.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=08c3f527fcd75de5c88682d6fc08018e 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-webhook.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=c7579b9b8372dc9781dd1da38b1e404e 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-webhook.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=a0225726564aa9987b44bfb35f750c35 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-webhook.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=006a5aa0f321344da2d528c928f3bf4d 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-webhook.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=99c65eb0a83da2b793c1608ea3a47cbc 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-webhook.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=a8943cc826fc0bb2ab6db79ece619d8c 2500w" />
    </Frame>
  </Step>

  <Step title="Set up URL and webhook">
    Name the webhook **Mintlify**.

    In the **URL** field, enter the endpoint `https://leaves.mintlify.com/gitlab-webhook`.
  </Step>

  <Step title="Get webtoken">
    In your Mintlify dashboard, click **Show Webtoken**. Copy the webtoken.

    <Frame>
      <img src="https://mintcdn.com/mintlify/iZZGgKQ6swbDUuUa/images/gitlab/show-webtoken-light.png?fit=max&auto=format&n=iZZGgKQ6swbDUuUa&q=85&s=50d2acef9a5f88b607128f7c5292743c" alt="Screenshot of the GitLab connection in the Mintlify dashboard." className="block dark:hidden" data-og-width="1082" width="1082" data-og-height="980" height="980" data-path="images/gitlab/show-webtoken-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/iZZGgKQ6swbDUuUa/images/gitlab/show-webtoken-light.png?w=280&fit=max&auto=format&n=iZZGgKQ6swbDUuUa&q=85&s=75f9af453ff0b78c0405cf1c4c9553e2 280w, https://mintcdn.com/mintlify/iZZGgKQ6swbDUuUa/images/gitlab/show-webtoken-light.png?w=560&fit=max&auto=format&n=iZZGgKQ6swbDUuUa&q=85&s=e334492f35f31817572cdbee609bbb73 560w, https://mintcdn.com/mintlify/iZZGgKQ6swbDUuUa/images/gitlab/show-webtoken-light.png?w=840&fit=max&auto=format&n=iZZGgKQ6swbDUuUa&q=85&s=fa1f1e35ddf128b2c3ac11f1c0e07a03 840w, https://mintcdn.com/mintlify/iZZGgKQ6swbDUuUa/images/gitlab/show-webtoken-light.png?w=1100&fit=max&auto=format&n=iZZGgKQ6swbDUuUa&q=85&s=45c9ffca8d89232461ab659452ede15a 1100w, https://mintcdn.com/mintlify/iZZGgKQ6swbDUuUa/images/gitlab/show-webtoken-light.png?w=1650&fit=max&auto=format&n=iZZGgKQ6swbDUuUa&q=85&s=55bfb53452c1e4978ec8e553214a15c6 1650w, https://mintcdn.com/mintlify/iZZGgKQ6swbDUuUa/images/gitlab/show-webtoken-light.png?w=2500&fit=max&auto=format&n=iZZGgKQ6swbDUuUa&q=85&s=1ac1e1d5884482dcc2070aef8ea11ccc 2500w" />

      <img src="https://mintcdn.com/mintlify/iZZGgKQ6swbDUuUa/images/gitlab/show-webtoken-dark.png?fit=max&auto=format&n=iZZGgKQ6swbDUuUa&q=85&s=9fa9732011ac61c1250ebae004de87be" alt="Screenshot of the GitLab connection in the Mintlify dashboard." className="hidden dark:block" data-og-width="1082" width="1082" data-og-height="980" height="980" data-path="images/gitlab/show-webtoken-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/iZZGgKQ6swbDUuUa/images/gitlab/show-webtoken-dark.png?w=280&fit=max&auto=format&n=iZZGgKQ6swbDUuUa&q=85&s=2c31e6d34ed886094a1d1c8d65470ad3 280w, https://mintcdn.com/mintlify/iZZGgKQ6swbDUuUa/images/gitlab/show-webtoken-dark.png?w=560&fit=max&auto=format&n=iZZGgKQ6swbDUuUa&q=85&s=2fec0be80893185d3c7321f18d17b25d 560w, https://mintcdn.com/mintlify/iZZGgKQ6swbDUuUa/images/gitlab/show-webtoken-dark.png?w=840&fit=max&auto=format&n=iZZGgKQ6swbDUuUa&q=85&s=adab69cea59f22ef581e265c83f027e7 840w, https://mintcdn.com/mintlify/iZZGgKQ6swbDUuUa/images/gitlab/show-webtoken-dark.png?w=1100&fit=max&auto=format&n=iZZGgKQ6swbDUuUa&q=85&s=c5b46752749e9e3f76804499817387fe 1100w, https://mintcdn.com/mintlify/iZZGgKQ6swbDUuUa/images/gitlab/show-webtoken-dark.png?w=1650&fit=max&auto=format&n=iZZGgKQ6swbDUuUa&q=85&s=fe78cb48d5c090f0a931c477e425d678 1650w, https://mintcdn.com/mintlify/iZZGgKQ6swbDUuUa/images/gitlab/show-webtoken-dark.png?w=2500&fit=max&auto=format&n=iZZGgKQ6swbDUuUa&q=85&s=a29df1dda62856dc842ba1d3ee64becb 2500w" />
    </Frame>
  </Step>

  <Step title="Paste webtoken">
    In GitLab, paste the webtoken from your Mintlify dashboard in the **Secret token** field.
  </Step>

  <Step title="Select events">
    Select the following events to trigger the webhook:

    * **Push events** (All branches)
    * **Merge requests events**
  </Step>

  <Step title="Verify the webhook">
    You should see the following settings after configuring the webhook:

    * **Name**: Mintlify
    * **URL**: `https://leaves.mintlify.com/gitlab-webhook`
    * **Secret token**: The webtoken from your Mintlify dashboard
    * **Events**: **Push events** (All branches) and **Merge requests events**

    Add the webhook.

    <Frame>
      <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-webtoken.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=00c0ce70ce9e8dbc2712f71aaeef3362" alt="The Webhook page in the GitLab dashboard. The settings to configure for Mintlify are highlighted." data-og-width="1161" width="1161" data-og-height="1740" height="1740" data-path="images/gitlab/gitlab-project-webtoken.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-webtoken.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=d78ea01ef0a043783195c6d548d20eea 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-webtoken.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=b77667d112aa91a2db02ab5fb356f733 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-webtoken.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=7b2f55fe589a11b9e5ce5633b62c34ad 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-webtoken.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=531491f03816a11e44b651c921dc1789 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-webtoken.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=24770ed142d0cf9b7bfb0dc307c13449 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-webtoken.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=e8644419580dc23875105fb06f3f4433 2500w" />
    </Frame>
  </Step>

  <Step title="Test the webhook">
    After you create the webhook, click the **Test** dropdown. Click **Push events** to send a sample payload. If the test returns `Hook executed successfully: HTTP 200`, your webhook is configured correctly.

    <Frame>
      <img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-webtoken-test.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=3ad52f7ac39124a4c03944256d0b79d3" alt="Screenshot of the GitLab Webhooks page. The 'Push events' menu item is highlighted in the 'Test' menu." data-og-width="1161" width="1161" data-og-height="724" height="724" data-path="images/gitlab/gitlab-project-webtoken-test.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-webtoken-test.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=d174db5e7ba73d19a9431adca65ebe6c 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-webtoken-test.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=9dfb2d09246cb81c0074a2a429e940f7 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-webtoken-test.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=3db14fb7784c9380f627336622f73a8f 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-webtoken-test.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=68dc65bc33081a8a08c869f7f1ea8761 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-webtoken-test.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=ebd368461ffa4880d63a3ecbda59d84e 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/gitlab/gitlab-project-webtoken-test.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=1e510fe852d154bb8aca3dd2c20387aa 2500w" />
    </Frame>
  </Step>
</Steps>
