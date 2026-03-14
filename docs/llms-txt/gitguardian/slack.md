# Source: https://docs.gitguardian.com/platform/configure-alerting/notifiers-integrations/slack.md

# Source: https://docs.gitguardian.com/internal-monitoring/integrate-sources/messaging-integrations/slack.md

# Integrate Slack

> Monitor Slack workspaces for exposed secrets in channel messages and team discussions.

Monitor Slack workspaces for exposed secrets in channel messages, and team discussions.

## Why Monitor Slack?

Slack serves as the central hub for team collaboration where developers frequently share code snippets, configuration examples, and troubleshooting outputs in real-time discussions. These casual conversations often contain accidentally copied API keys, database credentials, and debug information with embedded secrets, creating immediate security risks that spread across channels and persist in chat history.

## Capabilities

| Feature                 | Support             | Details                                                                  |
| ----------------------- | ------------------- | ------------------------------------------------------------------------ |
| **Historical Scanning** | â (Manual Trigger) | Analyze existing messages and chat history                               |
| **Real-time Detection** | â (Supported)      | Instant detection via Slack Events API                                   |
| **Monitored Perimeter** | â (Supported)    | Select public channels to monitor - private channels require app invitation |
| **Team Perimeter**      | â³ (Coming Soon)    | Users must be in the "All-incidents" team to access incidents            |
| **Presence Check**      | â (Not Supported)  | All occurrences considered present                                       |
| **Direct Messages**     | â (Upon Consent)   | When explicitly authorized by user                                         |
| **File Attachments**    | â (Beta)           | File attachments dropped in channels/messages are supported              |
| **Interactive Message** | â (Beta)           | Users receive threaded interactive message when a secret is surfaced     |

**What we scan:**

- Public and private channel messages
- Direct messages (when explicitly authorized)
- Thread discussions and replies

<!--
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/O7bArrDyfI4" title="Add GitGuardian Secrets Detection To Slack" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
-->

## Setup GitGuardian for Slack Integration on GitGuardian SaaS

**Prerequisites:**

- **Owner** or **Manager** account on your GitGuardian Dashboard
- **Slack Workspace Owner** permissions (if app restrictions are enabled)

GitGuardian natively integrates with Slack via the [**GitGuardian**](https://slack.com/marketplace/A05PK62HTFH-gitguardian) or [**GitGuardian EU**](https://slack.com/marketplace/A07EQPEG9M1-gitguardian-eu) application on **Slack Marketplace**. The GitGuardian app for Slack has **read-only access** to your channels.

You can refer to the [Slack documentation](https://api.slack.com/start/apps) for more information on managing apps.

<Setup/>

## Integration with GitGuardian Self-Hosted

If you are using a self-hosted GitGuardian instance, you must first create and configure a dedicated App on your Slack workspace so that you own the entire data stream. GitGuardian handles it for you programmatically via the creation of your app with a manifest file. This will ensure that your app is appropriately created, with all the necessary permissions.

:::info Permissions requested
No action needed on your side, the app will automatically request the following Bot Token Scopes: `channels:history`, `channels:join`, `channels:read`, `groups:history`, `groups:read`, `team:read`, `users:read`, `users:read.email`, `files:read`, `chat:write`, `im:write`, `reactions:read`, `reactions:write`
:::

### 1. Create an app on your Slack workspace

#### If you are a GitGuardian Manager and you have the permissions to create an app on your Slack workspace

1. Navigate to the Slack integration page
2. Click **Configure app on Slack Marketplace** from your GitGuardian dashboard
   ![configure](/img/internal-monitoring/integrate-sources/messaging-integrations/slack/slack-app-configure.png)
3. Click **Create app on your Slack workspace** from the modal 
   This will automatically redirect you to your Slack workspace applications, with a dialog modal opened 
   
4. Select the Slack workspace you would like to monitor with GitGuardian
5. Click **Next**
6. You may review details, scopes and configurations set for the app on Slack Marketplace
   
7. Click **Create**
8. Go to **Settings > Basic Information > App Credentials** section
9. Get your App Credentials (`App ID`, `Client ID`, `Client Secret`, `Signing Secret`) that will be required for the pairing of the app with your GitGuardian workspace 
   ![App creation](/img/internal-monitoring/integrate-sources/messaging-integrations/slack/slack-app-creation.gif)

That's it! Your app on Slack Marketplace has been created and you can now [pair your app on Slack Marketplace with your GitGuardian Platform](#2-pair-the-app-on-your-slack-workspace-with-your-gitguardian-platform).

#### If you are a GitGuardian Manager but you don't have the permissions to create an app on Slack Marketplace

If you don't have the right to create an app on your Slack workspace, please ask your Slack administrator to do it for you.
You can easily forward a request with this procedure:

1. Navigate to the Slack integration page
2. Click **Configure app on your Slack workspace** 
   ![App configuration](/img/internal-monitoring/integrate-sources/messaging-integrations/slack/slack-app-configure.png)
3. Click the **Send a request to a Slack administrator** link to easily forward your request
4. They should in turn provide you with the credentials to proceed with the [pairing of the app on your Slack workspace with your GitGuardian Platform](#2-pair-the-app-on-your-slack-workspace-with-your-gitguardian-platform).

#### If you are not a GitGuardian Manager but you received a request to create an app on your Slack Workspace

You received a request to create a new app on your Slack Workspace so you can use GitGuardian to scan your Slack workspace for secrets.

1. Go to the [App creation](https://api.slack.com/apps?new_app=1&manifest_json=%7B%22display_information%22%3A%7B%22name%22%3A%22GitGuardian%22%7D%2C%22features%22%3A%7B%22bot_user%22%3A%7B%22display_name%22%3A%22GitGuardian%22%2C%22always_online%22%3Afalse%7D%7D%2C%22oauth_config%22%3A%7B%22redirect_urls%22%3A%5B%22https%3A//dashboard.gitguardian.com/api/v1/slack/app/install_callback/%22%5D%2C%22scopes%22%3A%7B%22user%22%3A%5B%5D%2C%22bot%22%3A%5B%22channels%3Ajoin%22%2C%22channels%3Aread%22%2C%22channels%3Ahistory%22%2C%22groups%3Ahistory%22%2C%22groups%3Aread%22%2C%22team%3Aread%22%2C%22users%3Aread%22%2C%22users%3Aread.email%22%5D%7D%7D%2C%22settings%22%3A%7B%22event_subscriptions%22%3A%7B%22request_url%22%3A%22https%3A//dashboard.gitguardian.com/api/v1/receiver/slack/%22%2C%22bot_events%22%3A%5B%22app_uninstalled%22%2C%22channel_archive%22%2C%22channel_created%22%2C%22channel_deleted%22%2C%22channel_history_changed%22%2C%22channel_id_changed%22%2C%22channel_left%22%2C%22channel_rename%22%2C%22channel_shared%22%2C%22channel_unarchive%22%2C%22channel_unshared%22%2C%22email_domain_changed%22%2C%22group_archive%22%2C%22group_deleted%22%2C%22group_history_changed%22%2C%22group_left%22%2C%22group_rename%22%2C%22group_unarchive%22%2C%22member_joined_channel%22%2C%22message.channels%22%2C%22message.groups%22%2C%22team_access_granted%22%2C%22team_access_revoked%22%2C%22team_domain_change%22%2C%22team_rename%22%5D%7D%2C%22org_deploy_enabled%22%3Afalse%2C%22socket_mode_enabled%22%3Afalse%2C%22token_rotation_enabled%22%3Afalse%7D%7D) page
2. Select the Slack workspace on which you will create a new app on your Slack Workspace
3. Click **Next**
4. Click **Edit Configurations**
5. Edit the **redirect_url** and **request_url** in the manifest to fit with the GitGuardian self-hosted instance URL:
   - **redirect_url**:
     - replace: `https://dashboard.gitguardian.com/api/v1/slack/app/install_callback/`
     - with: `https://<gitguardian.acme.com>/api/v1/slack/app/install_callback/`
   - **request_url**:
     - replace: `https://dashboard.gitguardian.com/api/v1/receiver/slack/`
     - with: `https://<gitguardian.acme.com>/api/v1/receiver/slack/`
       ![App manifest](/img/internal-monitoring/integrate-sources/messaging-integrations/slack/slack-app-manifest.png)
6. Click **Next**
7. Click **Create**
8. Go to **Settings > Basic Information > App Credentials** section
9. Return the App Credentials to your requester in the secure way of your choice (`App ID`, `Client ID`, `Client Secret`, `Signing Secret`) 
   ![App credentials source](/img/internal-monitoring/integrate-sources/messaging-integrations/slack/slack-app-credentials-source.png)

That's it! Your app has been created, and the requester will be able to declare its configuration in the GitGuardian platform.

:::info
The Historical Scan feature for Slack workspaces can be affected by [Slack API rate limits on `*:history` scopes](https://api.slack.com/changelog/2025-05-terms-rate-limit-update-and-faq).
Please contact your Slack Account Manager for more information.
:::

### 2. Pair the app on your Slack Workspace with your GitGuardian Platform

1. Fill-in the Slack configuration modal opened from your GitGuardian dashboard, with your app credentials (`App ID`, `Client ID`, `Client Secret`, `Signing Secret`) 
   ![App credentials](/img/internal-monitoring/integrate-sources/messaging-integrations/slack/slack-app-credentials.png)
2. Click **Save and close**

Your app is now paired, you now need to finish the installation to start covering your channels.

### 3. Finish the installation

<Setup/>

## Extend your coverage to private channels

:::info
By default, GitGuardian only scans public channels.
We do not access private channels without your consent.
:::

You can also monitor your private channels with the Slack integration.
To do so, simply invite our GitGuardian app into the desired private Slack channels:

1. Navigate to the private Slack channel of your choice
2. Go to the **Integrations** tab of your channel settings
3. Click **Add an App**
4. Click **Add** next to the **GitGuardian** app
   ![App addition](/img/internal-monitoring/integrate-sources/messaging-integrations/slack/slack-app-addition.gif)

That's it! Our GitGuardian app is now invited to your private channel and ready for monitoring.

To remove the GitGuardian app from a private Slack channel:

1. Navigate to the private Slack channel of your choice
2. Go to the **Integrations** tab of your channel settings
3. Click the **GitGuardian** app
4. Select **Remove this app from #channel**
5. Confirm by clicking **Remove**
   ![App removal](/img/internal-monitoring/integrate-sources/messaging-integrations/slack/slack-app-removal.gif)

That's it! Our GitGuardian app is now removed from your private channel and secret detection is disabled.

## Edit the GitGuardian app on your Slack workspace configuration

In case you need to edit the GitGuardian app on your Slack workspace configuration, due to an error when declaring your credentials or due to a secret rotation, you can do so as follows:

1. Click **Edit app**
2. Update your app credentials
3. Click **Save and close**  
   ![App configuration edit](/img/internal-monitoring/integrate-sources/messaging-integrations/slack/slack-app-configuration-edit.png)

## Delete your GitGuardian app on your Slack workspace configuration

In case you need to delete your GitGuardian app on your Slack workspace configuration, you can do so as follows:

1. Click **Edit app**
2. Click **Delete configuration**
3. Confirm by clicking **Delete configuration** in the confirmation modal

:::info
Deleting your GitGuardian app on your Slack workspace configuration will uninstall all your Slack integrations.
However, all your existing incidents detected on Slack will remain available on your dashboard.
Note that deleting the GitGuardian app on your Slack workspace configuration will only delete the configuration, not the app.
If you want to delete your GitGuardian app on your Slack workspace, you must do so from your Slack workspace.
:::

## Uninstall your Slack workspace from GitGuardian Platform

To uninstall a Slack workspace:

1. In the GitGuardian platform, navigate to the Sources integration page
2. Click **Edit** next to **Slack** in the **Messaging** section
3. Click the bin icon next to the Slack workspace to uninstall
4. Confirm by clicking **Uninstall** in the confirmation modal 
   ![Slack uninstall](/img/internal-monitoring/integrate-sources/messaging-integrations/slack/slack-uninstall.gif)

That's it! Your Slack workspace is now uninstalled from GitGuardian Platform.

## Slack Interactive Messages

When GitGuardian detects a secret in a Slack message, it automatically sends a threaded response to the original message with interactive actions. This allows users to quickly review and remediate incidents directly within Slack.

### How it works

When a secret is detected in a Slack message:

1. GitGuardian sends a **threaded response** in the original Slack thread, reducing channel noise and preserving context.
2. The message includes information about the detected secret and provides quick actions.
3. Users can **ignore the incident** directly from Slack using the interactive button.

:::info
GitGuardian only triggers **one message per incident per thread**. Subsequent occurrences of the same secret in the same thread will not generate additional messages.
:::

### User identification and permissions

GitGuardian uses the **email address** associated with the Slack user to find the corresponding user in the GitGuardian application. This matched user must have the appropriate permissions to perform actions on incidents.

- To ignore an incident from Slack, the user must have the **Ignore incidents** permission in GitGuardian.
- If a user does not have the necessary permissions, they will see an error message when attempting to ignore an incident.

### Interactive message types

#### Secret detected

When a secret is detected, GitGuardian posts a threaded message containing:

- **Detector Type**: The type of secret detected (e.g., AWS Access Key, GitHub Token)
- **Validity**: Whether the secret is valid or invalid (â Valid, â Invalid)
- **Location**: Link to the original message
- **Posted by**: The author who posted the secret

Available actions:

- **View Incident**: Opens the incident detail page in GitGuardian
- **Ignore**: Ignores the incident with the reason "This is a low risk secret"

![Secret detected message](/img/internal-monitoring/integrate-sources/messaging-integrations/slack/interactive-messages/slack_secret_detected.png)

#### Incident ignored

When an incident is ignored via the Slack interactive message, the original message is updated to reflect the new status:

- Shows the incident has been ignored
- Displays who resolved the incident
- Removes the action buttons

![Incident ignored message](/img/internal-monitoring/integrate-sources/messaging-integrations/slack/interactive-messages/slack_ignored.png)

### Synchronization with GitGuardian Dashboard

:::warning Important
The synchronization between Slack and GitGuardian dashboard is **one-way for actions performed in GitGuardian**:

- **Slack â GitGuardian**: When an incident is ignored through the Slack interactive message, it **will be reflected** in the GitGuardian dashboard.
- **GitGuardian â Slack**: When an incident is resolved or ignored from the GitGuardian dashboard, the Slack interactive message **will NOT be updated** and no new message will be sent.
  :::

### Error scenarios

#### App reinstallation required

If the installation was done before the 27th of January 2026, you will need reinstall Slack integration and accept the newly added scope `chat:write`.

#### Insufficient permissions

If a user attempts to ignore an incident but does not have the required permissions in GitGuardian, they will see an error message indicating they do not have permission to perform this action.

![Insufficient permissions error](/img/internal-monitoring/integrate-sources/messaging-integrations/slack/interactive-messages/slack_no_permission.png)

## Privacy and compliance

### App permissions

The specific permissions used by our applications are listed on the corresponding Slack Marketplace pages:

- [GitGuardian app for SaaS US](https://slack.com/marketplace/A05PK62HTFH-gitguardian?next_id=0&tab=settings)
- [GitGuardian EU app for SaaS EU](https://slack.com/marketplace/A07EQPEG9M1-gitguardian-eu?settings=1&tab=settings)

### User notification

Country-specific laws and regulations may require you to inform your Slack users that your channels are being scanned for secrets. Here is a suggestion for a message you may want to use:

> As part of our internal information security process, the company scans the Slack channels for potential secrets leaks using [GitGuardian](https://www.gitguardian.com/monitor-internal-repositories-for-secrets). All data collected will be processed for the purpose of detecting potential leaks. To find out more about how we manage your personal data and to exercise your rights, please refer to our employee/partner privacy notice.
>
> _Please note that only channels relating to the company's activity and business may be monitored and that users shall refrain from sharing personal or sensitive data not relevant to the channel's purpose._
