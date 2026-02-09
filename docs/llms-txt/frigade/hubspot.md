# Source: https://docs.frigade.com/integrations/hubspot.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.frigade.com/llms.txt
> Use this file to discover all available pages before exploring further.

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
    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/settings.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=07c6859475a52f65a4aaba50e3d524f6" alt="Hubspot Integrations" data-og-width="3680" width="3680" data-og-height="2196" height="2196" data-path="images/integrations/hubspot/settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/settings.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=a14c093d2560b7cca0f5981b2c6b6b4b 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/settings.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=f0a60c4dd4516841d083410c4f43f9ea 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/settings.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=59da4914ec4e6f23f589528470bfe357 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/settings.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=2ddae539a7fbdfa5c6bf03bb6278b3a2 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/settings.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=4991712290c491780866e8714d9d9edf 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/settings.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=bc21d89a19f90e1f3f30e69d51e23657 2500w" />
  </Step>

  <Step title="Create a new App">
    Click on the **Create a private app** button to create a new app. Type in "Frigade" as the app name. Leave description and logo blank.
    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/create-app.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=ac5b0ddfda5ac87eb0ac98101296a5f5" alt="Create App" data-og-width="3680" width="3680" data-og-height="2196" height="2196" data-path="images/integrations/hubspot/create-app.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/create-app.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=1e8ec611475a7bb4eb371fa5bd32766e 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/create-app.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=2099187dfb23755b91d7e9c1edfb9225 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/create-app.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=80e34c7758ae0938236807a07c853c4b 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/create-app.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=e9fb817d41d7d7020f931600f72677b9 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/create-app.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=9feb350d2f5beb0ae122f8f6a88dcd68 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/create-app.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=8180baf64102155196a8b7995d302ba6 2500w" />
  </Step>

  <Step title="Set App Scopes">
    Click on the **Scopes** tab and select the scopes which you would like Frigade to have access to. As a minimum, `contact.objects.contacts` is required for reading and writing.
    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/app-permissions.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=7b5069080bfdb2fd6e630a2ca16d4f52" alt="Set Permissions" data-og-width="3680" width="3680" data-og-height="2196" height="2196" data-path="images/integrations/hubspot/app-permissions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/app-permissions.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=49c79c73ec78f3139c19382e83cfda8f 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/app-permissions.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=a888c8b5a705e780899895fb6a665d65 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/app-permissions.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=4c5d7d8637a83041d757fe2892a534dd 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/app-permissions.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=90f16e1d83bc4da6298785badcb6672f 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/app-permissions.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=a7a5b2c007a0382a359c24f8e995f999 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/app-permissions.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=7ee293d9d0ca455163c3ded2fb472741 2500w" />
    Once you have set the permissions, click on the **Create app** button.
  </Step>

  <Step title="Get API Key">
    Once the app is created, you will be presented with the API token. Copy this token.
    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/app-key.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=26c876e442236acda0a2d166d7a338bf" alt="Get API Key" data-og-width="3680" width="3680" data-og-height="2196" height="2196" data-path="images/integrations/hubspot/app-key.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/app-key.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=5f58a306e11dce0456e12fd1dcaab0c3 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/app-key.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=e069bbafe0b693416224176b0db707ba 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/app-key.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=3e81835fdbbde6cae21cc6205b56974a 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/app-key.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=fc2f6b43733b1921e9421f800fe5367c 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/app-key.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=38834f97016fa8d68577e8746a2341cd 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/app-key.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=2ca6a90b674afeb501599fa3e044cb30 2500w" />
  </Step>

  <Step title="Add Token to Frigade">
    In the Frigade dashboard, navigate to the **Integrations** page and click on the **Hubspot** integration. Paste the API token into the input field and click **Save**.
    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/frigade-connect.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=e2d8b5be62e2d4165a7124594f7792e9" alt="Add token to Frigade" data-og-width="3680" width="3680" data-og-height="2196" height="2196" data-path="images/integrations/hubspot/frigade-connect.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/frigade-connect.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=f6cae782b6e2d3e4f23ecc09b1b6e692 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/frigade-connect.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=922147edc2a3e268954eceb54c762f0f 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/frigade-connect.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=69c745af7cf68921665aa9d5341a65c7 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/frigade-connect.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=ac2b4f5ef314e7bb771d7da59b862ac6 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/frigade-connect.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=3b5858a379089e8a444bfe24a7658ec9 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/frigade-connect.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=61957cc28373f41479b708a3ff28241f 2500w" />

    <Info>
      As soon as you save the token, Frigade will start sending data to Hubspot.
    </Info>
  </Step>

  <Step title="Verify Data in Hubspot">
    That's it! Data from Frigade will now start streaming to Hubspot in real time.

    You can test the integration by completing a Flow and checking the data in Hubspot for the corresponding contact.
    All data is added as Notes to the contact in Hubspot as seen below:
    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/frigade-hubspot.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=791aacea8840297353cee31e88ee30dd" alt="Hubspot Data" data-og-width="3680" width="3680" data-og-height="2196" height="2196" data-path="images/integrations/hubspot/frigade-hubspot.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/frigade-hubspot.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=00c4a78f802cc61bf5ffd85188a5a458 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/frigade-hubspot.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=ff2053c258b9dcb14fb532572bd11ff0 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/frigade-hubspot.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=7e9b6893ebbc88c1bcc6125ed8b9f29f 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/frigade-hubspot.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=223089f75ea333e28691df278a7061ee 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/frigade-hubspot.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=5afcad78da5a9eb79a5897e934d2e6bc 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/hubspot/frigade-hubspot.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=64d7477b3eab0803105bcfb4dd577576 2500w" />
  </Step>
</Steps>
