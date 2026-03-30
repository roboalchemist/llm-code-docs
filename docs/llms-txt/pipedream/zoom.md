# Source: https://pipedream.com/docs/apps/integrated-apps/zoom.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Zoom

> Connect your Zoom account to Pipedream to automate meetings, webinars, and more.

Pipedream's Zoom integration lets you connect your Zoom account to automate workflows involving meetings, webinars, recordings, and users.

## Connecting your Zoom account

<Steps>
  <Step title="Open the Pipedream accounts page">
    Visit [Pipedream's accounts page](https://pipedream.com/accounts) and click **Connect an app**.
  </Step>

  <Step title="Search for Zoom">
    Search for **Zoom** and select it from the list.
  </Step>

  <Step title="Authorize Pipedream">
    A new window will open prompting you to sign in to your Zoom account. After signing in, authorize Pipedream to access your Zoom account.
  </Step>

  <Step title="Confirm connection">
    Once authorized, you'll be redirected back to Pipedream. Your Zoom account will now appear in your connected accounts list.
  </Step>
</Steps>

## Using Zoom with Pipedream

Once connected, you can use Zoom in your workflows to:

* **Triggers**: Start workflows when new meetings are created, recordings become available, or participants join/leave meetings
* **Actions**: Create meetings, list recordings, get meeting details, add registrants to webinars, and more

### Example: Create a meeting

Use the **Create Meeting** action to schedule a new Zoom meeting from your workflow:

1. Add a new step to your workflow
2. Search for **Zoom** and select the **Create Meeting** action
3. Select your connected Zoom account
4. Configure the meeting topic, start time, duration, and other settings
5. Test the step to create the meeting

### Example: Get meeting recordings

Use the **List Recordings** action to retrieve cloud recordings for a user:

1. Add a new step to your workflow
2. Search for **Zoom** and select the **List Recordings** action
3. Select your connected Zoom account
4. Specify the user ID and date range
5. Test the step to retrieve recordings

## Disconnecting your Zoom account

To disconnect your Zoom account from Pipedream:

<Steps>
  <Step title="Open the Pipedream accounts page">
    Visit [Pipedream's accounts page](https://pipedream.com/accounts).
  </Step>

  <Step title="Find your Zoom account">
    Search for your Zoom connected account in the list.
  </Step>

  <Step title="Delete the connection">
    Click the **...** menu next to your Zoom account and select **Delete**.
  </Step>
</Steps>

<Note>
  Deleting a connected account will break any workflows that use it. Make sure to update or disable affected workflows before disconnecting.
</Note>

## Troubleshooting

### Reconnecting your account

If you encounter authorization errors, you may need to reconnect your Zoom account:

1. Visit [Pipedream's accounts page](https://pipedream.com/accounts)
2. Find your Zoom account and click the **...** menu
3. Select **Reconnect** and follow the authorization flow

### Scopes and permissions

Pipedream requests the necessary OAuth scopes to access Zoom's API on your behalf. If you need additional permissions, you may need to reconnect your account or contact support.

Built with [Mintlify](https://mintlify.com).
