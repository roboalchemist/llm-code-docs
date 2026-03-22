# Source: https://docs.wandb.ai/platform/app/settings-page/user-settings.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

> Manage your profile information, account defaults, alerts, participation in beta products, GitHub integration, storage usage, account activation, and create teams in your user settings.

# Manage user settings

Navigate to your user profile page and select your user icon on the top right corner. From the dropdown, choose **Settings**.

## Profile

Within the **Profile** section you can manage and modify your account name and institution. You can optionally add a biography, location, link to a personal or your institution’s website, and upload a profile image.

## Edit your intro

To edit your intro, click **Edit** at the top of your profile. The WYSIWYG editor that opens supports Markdown.

1. To edit a line, click it. To save time, you can type `/` and choose Markdown from the list.
2. Use an item's drag handles to move it.
3. To delete a block, click the drag handle, then click **Delete**.
4. To save your changes, click **Save**.

### Add social badges

To add a follow badge for the `@weights_biases` account on X, you could add a Markdown-style link with an HTML `<img>` tag that points to the badge image:

```markdown  theme={null}
[![X: @weights_biases](https://img.shields.io/twitter/follow/weights_biases?style=social)](https://x.com/intent/follow?screen_name=weights_biases)
```

In an `<img>` tag, you can specify `width`, `height`, or both. If you specify only one of them, the image's proportions are maintained.

## Default team

If you are a member of more than one team, the **Default team** section allows you to configure the default team to use when a run or a Weave trace does not specify a team. If you are a member of only one team, that team is the default and this section does not appear.

Select a tab to continue.

<Tabs>
  <Tab title="Multi-tenant Cloud">
    Next to **Default location to create new projects in**, click the drop-down, then select your default team.
  </Tab>

  <Tab title="Dedicated Cloud / Self-Managed">
    1. Next to **Default location to create new projects in**, click the drop-down, then select your default team or your personal entity.
    2. (**Optional**) If an admin has turned on public projects in **Account** > **Settings** > **Privacy**, configure the default visibility for your new projects. Click the button next to **Default project privacy in your personal account**, then select **Private** (the default) or **Public**.
    3. (**Optional**) If an admin has turned on [default saving and diffing code](/models/app/features/panels/code/) in **Account** > **Settings** > **Privacy**, to turn it on for your runs, click **Enable code saving in your personal account**.
  </Tab>
</Tabs>

<Note>
  To specify the default team when you’re running a script in an automated environment, you can specify the default location using the `WANDB_ENTITY` [environment variable](https://docs.wandb.ai/models/track/environment-variables).
</Note>

## Teams

The **Teams** section lists all of your teams.

1. Click a team name to go to the team page.
2. If you have permission to join additional teams, click **View teams** next to **We found teams for you to join**.
3. Optionally, turn on **Hide teams in public profile**.

<Note>
  To create or manage a team, see [Manage teams](/platform/app/settings-page/teams/).
</Note>

## API keys

The **API Keys** section allows you to manage your personal API keys for authenticating with W\&B services.

### View your API keys

The API keys table displays:

* **Key ID**: The first part of each API key, used for identification
* **Name**: A descriptive name you provided when creating the key
* **Created**: When the key was created
* **Last used**: The most recent usage timestamp

<Note>
  The table shows only the key ID (first part of the key) for security. The full secret API key is only displayed once when you create it.
</Note>

Enter a partial key name or ID to search filter the list of API keys.

### Create a new API key

To create an API key, select the **Personal API key** or **Service Account API key** tab for details.

<Tabs>
  <Tab title="Personal API key">
    To create a personal API key owned by your user ID:

    1. Log in to W\&B, click your user profile icon, then click **User Settings**.
    2. Click **Create new API key**.
    3. Provide a descriptive name for your API key.
    4. Click **Create**.
    5. Copy the displayed API key immediately and store it securely.
  </Tab>

  <Tab title="Service account API key">
    To create an API key owned by a service account:

    1. Navigate to the **Service Accounts** tab in your team or organization settings.
    2. Find the service account in the list.
    3. Click the action menu (`...`), then click **Create API key**.
    4. Provide a name for the API key, then click **Create**.
    5. Copy the displayed API key immediately and store it securely.
    6. Click **Done**.

    You can create multiple API keys for a single service account to support different environments or workflows.
  </Tab>
</Tabs>

<Warning>
  The full API key is only shown once at creation time. After you close the dialog, you cannot view the full API key again. Only the key ID (first part of the key) is visible in your settings. If you lose the full API key, you must create a new API key.
</Warning>

For secure storage options, see [Store API keys securely](/platform/app/settings-page/user-settings/#store-and-handle-api-keys-securely).

### Delete an API key

To revoke access by deleting an API key:

1. Find the key you want to delete in the API keys table.
2. Click the delete button next to the key.
3. Confirm the deletion.

<Warning>
  Deleting an API key immediately revokes access for any scripts or services using that key. Ensure you have updated all systems to use a new key before deleting the old one.
</Warning>

## Store and handle API keys securely

API keys provide access to your W\&B account and should be protected like passwords. Follow these best practices:

### Recommended storage methods

* **Secrets manager**: Use a dedicated secrets management system such as [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/), [HashiCorp Vault](https://developer.hashicorp.com/vault), [Azure Key Vault](https://azure.microsoft.com/en-us/products/key-vault), or [Google Secret Manager](https://cloud.google.com/security/products/secret-manager).
* **Password manager**: Use a reputable password manager application.
* **OS-level keychains**: Store keys in macOS Keychain, Windows Credential Manager, or Linux secret service. Not suggested for production.

### What to avoid

* Never commit API keys to version control systems such as Git.
* Do not store API keys in plain text configuration files.
* Do not pass API keys on the command line, because they will be visible in the output of OS commands like `ps`.
* Avoid sharing API keys through email, chat, or other unencrypted channels.
* Do not hard-code API keys in your source code.

If an API key is exposed, delete the API key from your W\&B account immediately and contact [support](mailto:support@wandb.ai) or your AISE.

### Environment variables

When using API keys in your code, pass them through environment variables:

```bash  theme={null}
export WANDB_API_KEY="your-api-key-here"
```

This approach keeps keys out of your source code and makes it easier to rotate them when needed.

<Warning>
  Avoid setting the environment variable in line with the command, because it will be visible in the output of OS commands like `ps`:

  ```bash  theme={null}
  # Avoid this pattern, which can expose the API key in process managers
  export WANDB_API_KEY="your-api-key-here" ./my-script.sh
  ```
</Warning>

### SDK version compatibility

New API keys are longer than legacy keys. When authenticating with older versions of the `wandb` or `weave` SDKs, you may encounter an API key length error.

**Solution**: Update to a newer SDK version:

* `wandb` SDK v0.22.3+

  ```bash  theme={null}
  pip install --upgrade wandb==0.22.3
  ```
* `weave` SDK v0.52.17+
  ```bash  theme={null}
  pip install --upgrade weave==0.52.17
  ```

If you cannot upgrade the SDK immediately, set the API key using the `WANDB_API_KEY` environment variable as a workaround.

## Beta features

Within the **Beta Features** section you can optionally enable fun add-ons and sneak previews of new products in development. Select the toggle switch next to the beta feature you want to enable.

## Alerts

Get notified when your runs crash, finish, or set custom alerts with [wandb.Run.alert()](/models/runs/alert/). Receive notifications either through Email or Slack. Toggle the switch next to the event type you want to receive alerts from.

* **Runs finished**: whether a Weights and Biases run successfully finished.
* **Run crashed**: notification if a run has failed to finish.

For more information about how to set up and manage alerts, see [Send alerts with wandb.Run.alert()](/models/runs/alert/).

## Personal GitHub integration

Connect a personal Github account. To connect a Github account:

1. Select the **Connect Github** button. This will redirect you to an open authorization (OAuth) page.
2. Select the organization to grant access in the **Organization access** section.
3. Select **Authorize** **wandb**.

## Delete your account

Select the **Delete Account** button to delete your account.

<Warning>
  Account deletion can not be reversed.
</Warning>

## Storage

The **Storage** section describes the total memory usage the your account has consumed on the Weights and Biases servers. The default storage plan is 100GB. For more information about storage and pricing, see the [Pricing](https://wandb.ai/site/pricing) page.
