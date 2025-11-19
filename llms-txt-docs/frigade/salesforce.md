# Source: https://docs.frigade.com/integrations/salesforce.md

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
    ![Salesforce Connect](https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/integrations/salesforce/connect.png)
  </Step>

  <Step title="Specify data to sync">
    After connecting Salesforce, you will have the option to specify which data you would like to sync to Salesforce.
    By default, Frigade will only send Step and Flow completion events to Salesforce along with the associated metadata. For example, when a User completes a Survey or a step in a Checklist, Frigade will send this data to Salesforce for the corresponding contact.
  </Step>

  <Step title="Test the integration">
    You can test the integration by completing a Flow or a Step in a Flow. Once the Flow is completed, you can check Salesforce to see if the data has been synced.
    In the example below, a contact completed and NPS Survey and the data was synced to Salesforce:
    ![Salesforce Data](https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/integrations/salesforce/data.png)
  </Step>
</Steps>
