# Source: https://docs.rootly.com/integrations/microsoft-teams.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Microsoft Teams

> Create dedicated channels and tabs for incidents in Microsoft Teams to centralize communication and collaboration.

## Prerequisites

Before setting up the Microsoft Teams integration, ensure you have:

1. **Service Account in Azure AD**
   * Create a dedicated service account (e.g., `incident.management@yourcompany.com`)
   * **Required:** Assign a Microsoft Teams license to this account
   * This account should not be tied to a specific employee to prevent integration breakage when staff changes occur

2. **Azure AD Enterprise Application Assignment**
   * The service account must be assigned to the Rootly Enterprise Application in Azure Portal
   * Navigate to **Azure Portal > Enterprise Applications > Rootly > Users and groups**
   * Add the service account to the application
   * This step is critical to avoid authentication errors (AADSTS650052, AADSTS50105)

3. **Rootly Admin Access**
   * A separate Rootly administrator account to initiate the integration setup
   * This admin needs permissions to manage integrations in Rootly
   * Note: The Rootly admin does NOT need to be the same person as the service account

4. **Permissions**
   * The service account needs the OAuth permissions listed below
   * The service account must exist as a Rootly user (can be assigned "No access" role)

## Installation in Rootly (required)

### Understanding the Two-User Setup

The integration setup involves **two different accounts**:

* **Rootly Admin** (e.g., your personal account): Initiates the setup within Rootly's web interface
* **Service Account** (e.g., [incident.management@yourcompany.com](mailto:incident.management@yourcompany.com)): Provides OAuth credentials and permissions

This separation ensures the integration remains active even if individual team members leave the company.

### Setup Steps

1. **Log into Rootly** as an admin user
2. Navigate to the **Integrations** page
3. Click **Connect** on the Microsoft Teams integration
4. You will be redirected to Microsoft's OAuth consent page
5. **Important:** At the Microsoft login screen, authenticate with your **service account credentials** (not your personal admin account)
6. Grant the requested permissions as the service account
7. You will be redirected back to Rootly with the integration configured

<Note>
  **Why use a service account?** The service account's OAuth tokens are stored securely in Rootly. Using a dedicated service account (rather than a personal account) ensures:

  * Integration continues working if employees leave
  * Delegated permissions scope is isolated to a controlled account
  * Audit trails are clearer
  * The service account email will be displayed as the integration name in Rootly
</Note>

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/EZBU89ISF00990Wy/images/integrations/microsoft-teams/images-1.webp?fit=max&auto=format&n=EZBU89ISF00990Wy&q=85&s=e319685afa51c7cf7eb9e1e7f962f4cb" width="709" height="583" data-path="images/integrations/microsoft-teams/images-1.webp" />
</Frame>

## Oauth Permissions

Your selected workspace needs the following oauth permissions:

* **offline\_access**
  * This permission is needed for to perform OAuth authentication.
* **User.Read**
  * Allows Rootly to have user information about who integrated the account. This permission is needed for our OAuth strategy.
* **Team.ReadBasic.All**
  * Read the names and descriptions of teams, on behalf of the signed-in user.
* **ChatMessage.Send**
  * Allows an app to send channel messages in Microsoft Teams, on behalf of the signed-in user.
* **Channel.Create**
  * Create channels in any team, on behalf of the signed-in user.
* **Channel.ReadBasic.All**
  * Read channel names and channel descriptions, on behalf of the signed-in user.
* **ChannelMessage.Send**
  * Allows an app to send channel messages in Microsoft Teams, on behalf of the signed-in user.
* **ChannelMessage.ReadWrite**
  * Allows the app to read and write channel messages, on behalf of the signed-in user.
* **ChannelSettings.ReadWrite.All**
  * Add and remove members from channels, on behalf of the signed-in user.
* **ChannelMember.ReadWrite.All**
  * Read and write the names, descriptions, and settings of all channels, on behalf of the signed-in user.
* **TeamsTab.ReadWriteSelfForChat**
  * Allows a Teams app to read, install, upgrade, and uninstall its own tabs in chats the signed-in user can access.
* **TeamsTab.ReadWriteSelfForTeam**
  * Allows a Teams app to read, install, upgrade, and uninstall its own tabs to teams the signed-in user can access.
* **TeamsAppInstallation.ReadWriteSelfForTeam**
  * Allows a Teams app to read, install, upgrade, and uninstall itself to teams the signed-in user can access.
* **TeamsAppInstallation.ReadWriteSelfForChat**
  * Allows the Rootly app to install itself into chats so that tabs and other features work in group chats and meeting chats.
* **Chat.Create**
  * Allows the app to create group chats and one-on-one chats on behalf of the signed-in user.
* **Chat.ReadWrite**
  * Allows the app to read and send messages in chats on behalf of the signed-in user.

## Installation in Microsoft Teams (required)

After completing the OAuth setup in Rootly, you need to add the Rootly app to Microsoft Teams.

<Warning>
  **Important:** Log into Microsoft Teams using the **same service account** that you used for the OAuth authorization in Rootly. Using a different account will result in authentication errors.
</Warning>

### Steps to Add Rootly App in Teams

1. **Log into Microsoft Teams** as your **service account** (e.g., [incident.management@yourcompany.com](mailto:incident.management@yourcompany.com))
2. On the left-hand side, click **"+ Apps"**
3. Search for **"Rootly"** in the Teams app store
4. Click on the Rootly app, then click the dropdown next to **"Add"**
5. Choose **"Add to a team"**
6. Select a team and a primary channel (we recommend the General channel)
7. Click **"Set Up"** to install both the bot and the Rootly tab

<Frame>
  <img alt="Document Image" src="https://mintcdn.com/rootly/EZBU89ISF00990Wy/images/integrations/microsoft-teams/images-2.webp?fit=max&auto=format&n=EZBU89ISF00990Wy&q=85&s=53c2f4eb8dec4f8cd43a62daac3da00b" width="1448" height="939" data-path="images/integrations/microsoft-teams/images-2.webp" />
</Frame>

8. A confirmation modal will appear - click **"Save"** to finalize the installation
9. Optionally, post a message to the channel announcing the new Rootly tab

<Note>
  You will need to install the Rootly app for each team that requires access to incident management features. The service account must be a member of each team where you want to install the app.
</Note>

## Troubleshooting Common Errors

### Error: AADSTS650052 - "The app doesn't exist in your tenant or has been disabled"

This error occurs when the service account hasn't been assigned to the Rootly Enterprise Application in Azure AD.

**Solution:**

1. Open **Azure Portal**
2. Navigate to **Enterprise Applications**
3. Find your **Rootly** application (e.g., "\[Production] Rootly Teams")
4. Go to **Users and groups**
5. Click **Add user/group**
6. Select your service account (e.g., [incident.management@yourcompany.com](mailto:incident.management@yourcompany.com))
7. Assign appropriate roles
8. Click **Assign**

After completing these steps, retry adding the Rootly app in Teams.

### Error: AADSTS50105 - "The signed in user is not assigned to a role for the application"

Similar to the above, this indicates the user account attempting to authenticate is not assigned to the Rootly Enterprise Application.

**Solution:** Follow the same steps as AADSTS650052 above.

### Error: "You don't appear to be a member of this organization"

This error appears when trying to add the Rootly app in Teams with an account that isn't a member of the required Teams workspace.

**Solution:**

1. Ensure the service account is a member of the Teams workspace
2. Verify the service account has an active Teams license
3. Add the service account to the specific team(s) where you want to install Rootly

### Integration Works in Rootly but Not in Teams

If the OAuth setup completes successfully in Rootly, but you can't add the app in Teams:

**Checklist:**

* [ ] Logged into Teams with the **same service account** used for OAuth
* [ ] Service account has a Teams license
* [ ] Service account is assigned to the Rootly Enterprise App in Azure
* [ ] Service account is a member of the team where you're trying to install the app
* [ ] Using the correct Rootly app from the Teams app store (production vs. sandbox)

### Need More Help?

If you continue experiencing issues after following these steps, please contact Rootly support with:

* Screenshots of any error messages
* The service account email being used
* Steps you've already tried
* Whether you're using Rootly production or sandbox environment

## Uninstall

1. Login to your **Microsoft Teams** account.
2. Click **Manage > Installed Apps** or search for the **Rootly** App.
3. Click the **Rootly** app.
4. Click **Uninstall**.


Built with [Mintlify](https://mintlify.com).