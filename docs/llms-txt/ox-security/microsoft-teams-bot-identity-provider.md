# Source: https://docs.ox.security/ticketing-and-messaging/messaging/microsoft-teams/microsoft-teams-bot-identity-provider.md

# OX Security Alerts for Microsoft Teams

You can use the Microsoft Teams Bot Identity Provider connector to send OX notifications from an organization app, verified in [Azure Marketplace](https://marketplace.microsoft.com/en-us/product/office/WA200008847?tab=Overview), instead of from individual user identities.

This gives consistent sender identity (“OX Security”), allows org-wide rollout through Teams policies, and works from issues and workflows with deep links back to OX.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-f2a675d877d90c64ceac5f287621912e60975cac%2Fbot_MS%20Teams1%20(1).png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

### Prerequisites

* Microsoft Teams admin with permission to manage apps and policies in the Teams Admin Center.

### Step 1: Publish the OX Security app to your Teams tenant

1. Go to the **Teams Admin Center**.
2. Go to **Teams apps** > **Manage apps**.\
   Search for **OX Security** and open the app from the Azure Marketplace.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-680f1d62483da6624f8c3996c52a462eaab45a27%2Fbot_MS%20Teams_MS_marketplace.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

1. Set the app to **Allowed** for your organization, if required by your app permission policies.
2. Go to **Teams apps** > **Setup policies**.
3. Create a new **App setup policy** or edit an existing one; for example, edit the default policy **Global (Org-wide default)**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-01f4c47b013d6a5273ff90195e04bdaee200ae7a%2FTeams_alerts3.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

1. In **Installed apps**, select the **OX Security Alerts** app.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-d598d230d84748c8d388d8eba7cdcf50e12bf70a%2FTeams_alerts2.png?alt=media" alt="" width="281"><figcaption></figcaption></figure>

1. Select **Add**. This installs the app for everyone covered by the policy, which means all the users within the organization assigned to the policy.

### Step 2: Connect OX to the Bot Identity Provider

1. In OX, go to **Settings** > **Connectors**.
2. Select **Microsoft Teams**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-994f513a559395469422d1eac52908b1b044a8f7%2FConfigure%20MS%20teams%20credentials%20in%20OX_bot_identity_provider.png?alt=media" alt=""><figcaption></figcaption></figure>

1. Choose **Bot Identity Provider** and select **Connect**.
2. Complete the Microsoft consent flow, then return to OX and confirm the connector shows **Connected**.

### Step 3: Send notifications from a workflow (optional)

1. In OX, go to **Settings** > [**Workflows**](https://docs.ox.security/automate-with-ox-workflows/creating-a-workflow).
2. Create or edit a workflow and with a **Send Teams notification** action.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-6ab956d48416004bb71503cfe1c7a1f74ab6a6c3%2Fbot_MS%20Teams_WF.png?alt=media" alt="" width="155"><figcaption></figcaption></figure>
