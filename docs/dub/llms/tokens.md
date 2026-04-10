# Source: https://dub.co/docs/api-reference/tokens.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dub.co/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# API keys

> Learn how API keys work on Dub.

API keys on Dub allow you to access your workspace programmatically. This is useful for integrating Dub into your application or with other tools and services.

Each API key is tied to a specific workspace – meaning you can use it to access that workspace's resources without having to worry about "leaking" access to other workspaces.

API keys on Dub follow the format:

```bash .env theme={null}
DUB_API_KEY=dub_xxxxxxxx
```

By default, you can use this key to perform any API request without restriction, so it must be stored securely in your app's server-side code (such as in an environment variable or credential management system). Don’t expose this key on a website.

## Create an API key

You can create an API key by following these steps:

<Steps>
  <Step title="Go to your workspace">
    Go to **Settings** > [**API Keys**](https://app.dub.co/settings/tokens) in your workspace.

    <Frame>
      <img src="https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/workspace-api-keys.png?fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=6493e58033c7a98e84664fafa2acb53d" alt="Workspace API keys on Dub" width="1468" height="249" data-og-width="1295" data-og-height="687" data-path="images/workspace-api-keys.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/workspace-api-keys.png?w=280&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=b86a609f47d24e8ff58964ece34864ef 280w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/workspace-api-keys.png?w=560&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=04acf462bf4dc0c99c78dbdd9a862484 560w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/workspace-api-keys.png?w=840&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=34d2ba2509f531f699c8a3af959bed5a 840w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/workspace-api-keys.png?w=1100&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=1a6273708e71a50c2c8e1eec4d8ee140 1100w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/workspace-api-keys.png?w=1650&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=0ca6a30b47ee4fadbe59658ac86ad78e 1650w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/workspace-api-keys.png?w=2500&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=5fe4492b33d785b20c68f559a143cff7 2500w" />
    </Frame>
  </Step>

  <Step title="Create an API Key">
    Click on the "Create" button and select permissions you want to grant to
    the API key.

    Select between "You" and "Machine" to associate the API key with your account or a [machine user](#machine-users).

    * **You**: This API key is tied to your user and can make requests against the selected workspace.
    * **Machine**: A machine user will be added to your workspace, and an API key associated with that machine user will be created.

    <Frame>
      <img src="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/add-new-api-key.png?fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=a0d7699b93f7ad32c8964ed1cedd65e7" alt="Add new API key on Dub" width="1468" height="249" data-og-width="902" data-og-height="828" data-path="images/add-new-api-key.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/add-new-api-key.png?w=280&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=15d4dd4759471d5ec7c43486fc0f7e66 280w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/add-new-api-key.png?w=560&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=8cc977fd0797ed4e7653033cdfd39389 560w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/add-new-api-key.png?w=840&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=8d549657d43d11b345bcaf48e70bfb20 840w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/add-new-api-key.png?w=1100&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=f8d58424c460ac03cc7759bb0e84e8ae 1100w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/add-new-api-key.png?w=1650&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=1aadf8911936e5eef509795f8f959112 1650w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/add-new-api-key.png?w=2500&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=3587feca5b4fae801315953d671ff714 2500w" />
    </Frame>

    Click on the **Create API Key** button to create the key. Make sure to copy your API key and store it in a safe place. You won't be able to see it again.

    <Frame>
      <img src="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/api-key-created.png?fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=c8a52da3ff2678850ce6569da5104a06" alt="API Key created on Dub" data-og-width="592" width="592" data-og-height="390" height="390" data-path="images/api-key-created.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/api-key-created.png?w=280&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=8b39311b149baad5489d138d77202f6b 280w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/api-key-created.png?w=560&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=94276f4c1701fec9cb4430c7be050290 560w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/api-key-created.png?w=840&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=9c7886cc478afabd3c056bd9136889ef 840w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/api-key-created.png?w=1100&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=c77bf640e550b38c81f54aea40994379 1100w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/api-key-created.png?w=1650&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=12e2d9e11e291252a300ccbd3549635d 1650w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/api-key-created.png?w=2500&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=6eb996917831616e541ca49e10808003 2500w" />
    </Frame>
  </Step>

  <Step title="Use your API Key">
    Now that you have your API key, you can use it to access your workspace's resources programmatically via SDKs or within any API request as a bearer token.

    ```
    Authorization: Bearer dub_xxxx
    ```
  </Step>
</Steps>

<Tip>
  We recommend creating API keys with the least privilege necessary to perform
  the required tasks. This helps to reduce the risk of unauthorized access to
  your workspace.
</Tip>

## API key permissions

When creating a secret key, you can select the permissions it has, which will give the key access to certain (or all) resources on Dub. Here are the different permission options:

| Permission          | Description                                                                                                                                                                                                                                      |
| :------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **All permissions** | This API key will have full access to all resources.                                                                                                                                                                                             |
| **Read only**       | This API key will have read-only access to all resources.                                                                                                                                                                                        |
| **Restricted**      | This API key will have restricted access to some resources: <ul><li>[Links](/data-model#links)</li><li>[Analytics](/api-reference/endpoint/retrieve-analytics)</li><li>[Domains](/data-model#domains)</li><li>[Tags](/data-model#tags)</li></ul> |

Depending on your use case, you might want to use one of these 3 options to limit the scope of the API key and improve security. When making API calls, if your API key has insufficient permissions, the error should tell you which permissions you need.

## Machine users

On Dub, you can create API keys that are associated with a "Machine user". This is particularly helpful when you don't want to associate the API key with a particular user in your workspace, to avoid security risks in involving turnover or changes in project ownership.

<Warning>
  Machine users share the same permissions as the [owner
  role](https://dub.co/help/article/workspace-roles#owner-role) in a workspace.
  Make sure to only create machine users for trusted applications.
</Warning>

<Frame>
  <img src="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/api-machine-users.png?fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=f085cda5b9d9cbe8a04ddba64d3293cc" alt="Creating an API key associated with a machine user on Dub" width="1528" height="974" data-og-width="794" data-og-height="563" data-path="images/api-machine-users.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/api-machine-users.png?w=280&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=6dde53d285800a892590df2f123a47e1 280w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/api-machine-users.png?w=560&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=10ca92f39b1a4252c9748a2116118b95 560w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/api-machine-users.png?w=840&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=b294692ba07616be6d0cc6f1d0cf8f7c 840w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/api-machine-users.png?w=1100&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=97bbe55faf7906a8ab695151f3afdc7d 1100w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/api-machine-users.png?w=1650&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=575d8dd29e60b3e25a237fbb147af7a4 1650w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/api-machine-users.png?w=2500&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=6726aa3bc87b0038fd26ba6c5de077a0 2500w" />
</Frame>

These machine users will show up on your workspace's **People** tab, but will not contribute to your workspace's user count.

<Frame>
  <img src="https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/machine-user.png?fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=823d1d725759cc1de777d41b8274a6e2" alt="Machine user on Dub" width="1468" height="249" data-og-width="712" data-og-height="188" data-path="images/machine-user.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/machine-user.png?w=280&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=7c1575a4c6ea752052111dd60aa10b28 280w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/machine-user.png?w=560&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=c20c5608d7bff74a8f82226337d2d066 560w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/machine-user.png?w=840&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=aa33850d0be3795865294ba046ee4ecf 840w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/machine-user.png?w=1100&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=2edacfacddaedacc375e4df4b92c3930 1100w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/machine-user.png?w=1650&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=b850576a537c2b3507e5fade5dd6c70b 1650w, https://mintcdn.com/dub/S5CJNHicyu5NWQ7r/images/machine-user.png?w=2500&fit=max&auto=format&n=S5CJNHicyu5NWQ7r&q=85&s=6a11511bd60862237d63bff4d3498bee 2500w" />
</Frame>

<Tip>
  If you delete an API key associated with a machine user, the machine user will
  be deleted. Vice versa, if you delete a machine user, their corresponding API
  key will be deleted as well.
</Tip>
