# Source: https://docs.frigade.com/integrations/hubspot.md

# Hubspot

Frigade supports writing data to Hubspot. When users take action in Flows, Frigade will send the data and any corresponding metadata to Hubspot.
For instance, when a User completes a Survey or a step in a Checklist, Frigade will send this data to Hubspot to the matching contact.

<Info>
  Frigade will only send data to Hubspot if the User has an email associated with them. To associate an email with a User, see the [useUser hook](/sdk/hooks/user) or the [User API](/api-reference/users).
</Info>

# Sending Frigade data to Hubspot

<Steps>
  <Step title="Create a Hubspot API Token">
    To get started, you will need to create a Hubspot API token by setting up a Private App in your Hubspot account.
    You can do this by navigating to the **Settings** > **Integrations** > **Private Apps** page as seen below:
    ![Hubspot Integrations](https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/integrations/hubspot/settings.png)
  </Step>

  <Step title="Create a new App">
    Click on the **Create a private app** button to create a new app. Type in "Frigade" as the app name. Leave description and logo blank.
    ![Create App](https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/integrations/hubspot/create-app.png)
  </Step>

  <Step title="Set App Scopes">
    Click on the **Scopes** tab and select the scopes which you would like Frigade to have access to. As a minimum, `contact.objects.contacts` is required for reading and writing.
    ![Set Permissions](https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/integrations/hubspot/app-permissions.png)
    Once you have set the permissions, click on the **Create app** button.
  </Step>

  <Step title="Get API Key">
    Once the app is created, you will be presented with the API token. Copy this token.
    ![Get API Key](https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/integrations/hubspot/app-key.png)
  </Step>

  <Step title="Add Token to Frigade">
    In the Frigade dashboard, navigate to the **Integrations** page and click on the **Hubspot** integration. Paste the API token into the input field and click **Save**.
    ![Add token to Frigade](https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/integrations/hubspot/frigade-connect.png)

    <Info>
      As soon as you save the token, Frigade will start sending data to Hubspot.
    </Info>
  </Step>

  <Step title="Verify Data in Hubspot">
    That's it! Data from Frigade will now start streaming to Hubspot in real time.

    You can test the integration by completing a Flow and checking the data in Hubspot for the corresponding contact.
    All data is added as Notes to the contact in Hubspot as seen below:
    ![Hubspot Data](https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/integrations/hubspot/frigade-hubspot.png)
  </Step>
</Steps>
