# Source: https://docs.axonius.com/docs/connecting-the-slack-adapter-in-axonius.md

# Connecting the Slack Adapter in Axonius

**To add a new Slack Connection in Axonius:**

1. Navigate to the Adapters page, search for `Slack`, and click on the adapter tile.

   ![Slack tile](https://files.readme.io/dd999e61df073e32adad6efe55de4f82a4e952e5cb5bb19649dc65b0d0a3f7bf-image.png)

   <br />
2. On the top right side, click **Add Connection**. The **Add Connection** drawer opens.

## Required Parameters

1. **Host Name or IP Address** *(default: `https://slack.com`)* - The hostname or IP address of the Slack server.
2. **Authentication Token** - An Authentication Token associated with a user account that has the [required permissions](https://docs.axonius.com/axonius-help-docs/docs/slack-permissions) to fetch assets. For instructions on generating the Authentication Token, see [admin.users.list](https://api.slack.com/methods/admin.users.list).
3. **Selecting the Token type** - Select either of the following options:

   <Tabs>
     <Tab title="Enterprise Grid Organization">
       Select this if you are using the Slack Enterprise Grid Organization solution. This allows Axonius to fetch data from all workspaces associated with the authentication token.
     </Tab>

     <Tab title="Not an Admin Token">
       Select this option if the Authentication Token you entered is **not** an admin token. In this case, the **Team IDs** field must be populated. All admin endpoints will be skipped in the fetch.

       * Copy the Team ID from the team's URL in the Slack web client. For example, if the team URL is `https://app.slack.com/client/T0123456789/A0123456789`, the team ID is `T0123456789`.
       * If you leave this field empty, the team IDs will be fetched automatically from the admin.teams.list API.
     </Tab>
   </Tabs>

![slack connection](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/slack%20connection.png)

## Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
2. **HTTPS Proxy** - A proxy to use when connecting to the value supplied in **Host Name or IP Address**.

### Fetching Application Settings

<Callout icon="🚧" theme="warn">
  **Attention**

  These parameters are required to fetch high-privilege settings that cannot be fetched with an API Token.
</Callout>

1. **Account Sub Domain** - The Slack account's sub domain (.slack.com).
2. **User Name** and **Password** - The credentials for a user account that has the required permissions to fetch assets.
3. **MFA Secret** - If you access Slack through an SSO solution that requires multi-factor authentication, you will need to  generate a secret key in that solution and paste it here. See [Set Up Google Authenticator for the Okta adapter](https://docs.axonius.com/docs/okta-deploying-the-adapter#setting-up-multi-factor-authentication), for an example.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).