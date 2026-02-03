# Source: https://docs.frigade.com/integrations/salesforce.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.frigade.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Salesforce

Frigade supports syncing data with Salesforce. For instance, when a User completes a Survey or a step in a Checklist, Frigade will send this data to Salesforce to the matching contact.

<Info>
  Frigade will only send data to Salesforce if the User has an email associated with them. To associate an email with a User, see the [useUser hook](/sdk/hooks/user) or the [User API](/api-reference/users).
</Info>

# Sending Frigade data to Salesforce

<Steps>
  <Step title="Connect Salesforce to Frigade">
    To get started, open teh Frigade Dashboard and navigate to the **Integrations**. Click **Connect** on the Salesforce integration.
    This will prompt you to connect your Salesforce account to Frigade using OAuth.
    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/salesforce/connect.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=64c4a27586506203b6660272f7d5bc02" alt="Salesforce Connect" data-og-width="1541" width="1541" data-og-height="1111" height="1111" data-path="images/integrations/salesforce/connect.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/salesforce/connect.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=a9e1a7907b65616a490cb950366cbd97 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/salesforce/connect.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=e8c031b93a3e23a4b93fdebbfe4c2c7e 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/salesforce/connect.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=ac705328a2ad529d2bbc47ee51b17a02 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/salesforce/connect.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=73232bf2e64e514fb5186b2d565615a8 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/salesforce/connect.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=9acdfde30d0ac9b4ba7ee3b347b7eb07 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/salesforce/connect.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=e0c1e6629aaeb1a3fef86fb072174eed 2500w" />
  </Step>

  <Step title="Specify data to sync">
    After connecting Salesforce, you will have the option to specify which data you would like to sync to Salesforce.
    By default, Frigade will only send Step and Flow completion events to Salesforce along with the associated metadata. For example, when a User completes a Survey or a step in a Checklist, Frigade will send this data to Salesforce for the corresponding contact.
  </Step>

  <Step title="Test the integration">
    You can test the integration by completing a Flow or a Step in a Flow. Once the Flow is completed, you can check Salesforce to see if the data has been synced.
    In the example below, a contact completed and NPS Survey and the data was synced to Salesforce:
    <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/salesforce/data.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=0169375f028c93cbe83de9dfc869f5c8" alt="Salesforce Data" data-og-width="1541" width="1541" data-og-height="1111" height="1111" data-path="images/integrations/salesforce/data.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/salesforce/data.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=b60ba677bd6e37eb6762fd6689fb8085 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/salesforce/data.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=6530779f7c9c6748b33272203e4e58a5 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/salesforce/data.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=7ad5e26ccad567ec298854a3ae997f49 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/salesforce/data.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=eb8dac2c8bfe83b4d26b22bdb58f3f60 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/salesforce/data.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=28cfdd7dd882fa0db300bf14e99d72b1 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/integrations/salesforce/data.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=5d852e6570bace6a27dfac1bd6a0a8ca 2500w" />
  </Step>
</Steps>
