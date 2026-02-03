# Source: https://loops.so/docs/guides/bubble-api-connector.md

> ## Documentation Index
> Fetch the complete documentation index at: https://loops.so/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Bubble API Connector

> Send data to Loops from Bubble using the API Connector plugin.

This guide helps you set up an API connection to Loops from your Bubble app.

In this example, we will create an integration that allows you to sync Bubble users to your Loops audience.

<Tip>
  We have created an [official plugin for Bubble](/integrations/bubble), which contains actions for all Loops API calls. However, it is limited to what it can do by how Bubble works.\
  THis tutorial helps if you need more control or flexibility over the data that is sent to Loops.
</Tip>

## Install the API Connector plugin

In Bubble, you need to first install the API Connector Plugin. This plugin is what makes the API calls to Loops.

Go to Plugins and click **+ Add plugins**.

Search for "API Connector" and click **Install**.

<img src="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/bubble-search-plugin.png?fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=d4a70a59229cbecae781e4f4823365db" alt="Search for API Connector" data-og-width="2280" width="2280" data-og-height="1221" height="1221" data-path="images/bubble-search-plugin.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/bubble-search-plugin.png?w=280&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=5635521df2ba8fd1a2b2e7cbbd939551 280w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/bubble-search-plugin.png?w=560&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=e685702562ee0ca4e892cc54c58b808e 560w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/bubble-search-plugin.png?w=840&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=0ba4de412ccf2b4d33f4bdc0edd39f91 840w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/bubble-search-plugin.png?w=1100&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=f9bcc274de5d55bcb70dc3a84c073b80 1100w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/bubble-search-plugin.png?w=1650&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=d7d414c9f1fbd75064ba49b36230943b 1650w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/bubble-search-plugin.png?w=2500&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=1d03d672644c86fad7bb265604ab486d 2500w" />

## Add a Loops API connection

Now you have the plugin installed, you can add an API connection.

Click **Add another API**. In the form that appears, enter "Loops" into the **API Name** field (Bubble uses this field to group API calls together in the interface).

Make sure the **Key name** value is "Authorization" (this is the default).

In the **Authentication** field, select "Private key in header".

In Loops, go to your [API Settings page](https://app.loops.so/settings?page=api) and copy an API key (you can create a new key if you like).

Back in Bubble, in the **Key value** field, write the word `Bearer`, then a space character, then paste your API key, so it looks something like `Bearer YourApiKey`.

<img src="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-connect-api.png?fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=7d872c2397207fd27d8930d3c3d1fbb8" alt="Add the Loops API" data-og-width="2280" width="2280" data-og-height="1145" height="1145" data-path="images/bubble-connect-api.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-connect-api.png?w=280&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=a2156b98838c89be6cd9a00fbb4d8a7a 280w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-connect-api.png?w=560&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=e7a8edb0e9b6f31d6e63478a0ca589e6 560w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-connect-api.png?w=840&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=dde81cf4a33178a77d6045e6c23cd114 840w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-connect-api.png?w=1100&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=ca01c07c55f51d86e73110c10fba293c 1100w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-connect-api.png?w=1650&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=653867ae2264995c1c2846b2986adafd 1650w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-connect-api.png?w=2500&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=6c55dc89992d3eed69664480ac4df182 2500w" />

## Add an API call to sync users to Loops

Now you can create an API call using the connection you just created. Click **Add another call** at the bottom of the gray box.

In the **Name** field, write something like "Sync users".

In the **Use as** field, select "Action". The **Data type** field should be "JSON" (this is the default).

In the dropdown where it says "GET", select "POST", and in the subsequent field, paste the following endpoint URL:

```
https://app.loops.so/api/v1/contacts/update
```

<img src="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-add-api-call.png?fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=895b5df6050341511c75b426647f3a66" alt="Add an API call" data-og-width="2280" width="2280" data-og-height="968" height="968" data-path="images/bubble-add-api-call.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-add-api-call.png?w=280&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=b7daf5c91e45b966e3c40bd532120de2 280w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-add-api-call.png?w=560&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=8a3d443aef16139f619bfdc1acc540ae 560w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-add-api-call.png?w=840&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=cd899cc25f36f22ce0db30ee13953011 840w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-add-api-call.png?w=1100&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=c1e94de4eaa14fc78b1633b8061f5916 1100w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-add-api-call.png?w=1650&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=859524296512238892c83ba765a7540d 1650w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-add-api-call.png?w=2500&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=2cc0e75aaa2cce0400a56bfd2e43f5fd 2500w" />

Now all that's left is to set up the request body, which is the data that's sent to Loops. This will depend on what kind of data points you want to send.

In this example, we will add a [custom contact property](/contacts/properties) called "Plan name" (which we [already added in Loops](/contacts/properties#add-a-property)).

<Warning>
  Due to how Bubble handles empty values, make sure to only add properties to this request body that will always contain a value. Otherwise, Bubble will send `"null"` as the value instead of an empty value, which will mean, for example, your contact's first name will become `null`.
</Warning>

To make the request, we have to include an email address (which is required to create new contacts in Loops). Then we'll also add a "User ID" value (which will maintain a distinct connection between a user in Bubble to their contact record in Loops) plus the "Plan name" property. Due to the data in my example application, I know all three of these fields will always have a value.

In the **Body** field, paste this:

```json  theme={"dark"}
{
  "email": "<Email>",
  "userId": "<User_ID>",
  "planName": "<Plan_name>"
}
```

If you then click anywhere outside the **Body** field, you'll see two sets of fields appear below it, one for each of the three custom variables (`Email`, `User_ID` and `Plan_name`) we added to the body data.

Uncheck the **Private** checkbox for each of these variables, otherwise they won't show up in the Bubble interface when you come to use this API call.

<img src="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-body-data.png?fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=96050c8fabd306618d83c812190dcd93" alt="Adding body data" data-og-width="2280" width="2280" data-og-height="968" height="968" data-path="images/bubble-body-data.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-body-data.png?w=280&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=3f4934b73a82e9cc78e72f8fb67a240b 280w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-body-data.png?w=560&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=11d27eff167c351f31c08b82adcbe2f6 560w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-body-data.png?w=840&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=355d2e46d892a492ee647bffdfd547b0 840w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-body-data.png?w=1100&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=f2f2705c5d41f57ed15eb41e4d79f20d 1100w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-body-data.png?w=1650&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=5a3cdded5df8f425dab38ca26658b454 1650w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-body-data.png?w=2500&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=dea5b33950edd396c4f36952418a8eab 2500w" />

The final step is to initialize the call, which will show Bubble that the API call works.

To do this, enter some example values in each of the **Value** fields, then click **Initialize call** (this will send real data to Loops).

If it works, you'll see a success message and a confirmation of the returned values from Loops. Click **Save** to complete setting up the API call.

<img src="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/bubble-success.png?fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=f8cf486dc60788377fc366d9c66e89a9" alt="Request success" data-og-width="2280" width="2280" data-og-height="1172" height="1172" data-path="images/bubble-success.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/bubble-success.png?w=280&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=66be6a4c98835257e267c0a1a5e6eb6a 280w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/bubble-success.png?w=560&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=d8987326ce78ccdac0bf942bfbd2dbcd 560w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/bubble-success.png?w=840&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=ddf0122d4b144c080c59f4127ca739b4 840w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/bubble-success.png?w=1100&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=2bdcc42a0e27e487bdb3f4f033a38e1b 1100w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/bubble-success.png?w=1650&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=e6bbafd36e2d2a503b56da9e235a412f 1650w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/bubble-success.png?w=2500&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=cb6676592ceb52f9a5db1a792d9a490e 2500w" />

If the request is not successful, you should see a message telling you what went wrong.

<Info>When you're done, remember to delete the test data you just added in the **Value** fields.</Info>

## Add the action to your Workflow

The final step is using your API call inside your application.

To do this, go to **Workflows** in your Bubble account and create a workflow for when you want to send a user to Loops.

In this example, I want to sync users to Loops whenever they log in (they could also be synced after other events, like if their email address changes).

To do this, click **Click here to add an event...** and select "General > User is logged in".

Click **Click here to add an action...**, hover over **Plugins** and select the action you created by the name you gave it (naming is organized by "API name - API call name").

<img src="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/bubble-select-call.png?fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=0ab801be6192fc3894da11b4aa869be4" alt="Select the API call" data-og-width="2280" width="2280" data-og-height="1893" height="1893" data-path="images/bubble-select-call.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/bubble-select-call.png?w=280&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=32ad12820de786adf4945203a0572b47 280w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/bubble-select-call.png?w=560&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=e2d02d587768e25b29e86d8ce3fbe116 560w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/bubble-select-call.png?w=840&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=d152aa58d381880d8f9d219fc63aec51 840w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/bubble-select-call.png?w=1100&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=511fb63293c6d6b16f81d6106a7835d2 1100w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/bubble-select-call.png?w=1650&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=4b8882ff049902a54ed726cc72463556 1650w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/bubble-select-call.png?w=2500&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=a981b35b2ca6f9a30eda3ff9eb4aaab2 2500w" />

This will show a popover containing the fields you added in the previous step, allowing you to insert your data in Bubble into the API call.

Click into a field and then **Insert dynamic data**, then select the data you want to send to Loops. (In my example I searched for "Current User" and then selected `'s email`, `'s unique ID` and `'s plan` to fill out the three fields.)

<img src="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-add-data.png?fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=ab4b16f5e7cd87335e7cffdfd19765de" alt="Add data to API call" data-og-width="2280" width="2280" data-og-height="1050" height="1050" data-path="images/bubble-add-data.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-add-data.png?w=280&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=1eee89cfe2e2d421a631fe617475956f 280w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-add-data.png?w=560&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=0f3a0888d615f57d1934e49a4c832aed 560w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-add-data.png?w=840&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=adad0a9c0afe1bcfd6577ed718f5c1ad 840w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-add-data.png?w=1100&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=663c02c37965f9d271c5e98f8fd8c68f 1100w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-add-data.png?w=1650&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=34d76132ada287de6db33e57bc47707e 1650w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/bubble-add-data.png?w=2500&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=f4b3e1e4e1a309656f84795b1f0c9737 2500w" />

Now when the selected event happens, Bubble will make an API call to Loops!

To verify everything is set up correctly, log in to your Bubble app (to trigger the event) and then check the [Audience page](https://app.loops.so/audience) in Loops to see if your user account appears.

## Other examples

There are lots of different ways you can use Bubble's API Connector to send data to Loops:

* Create a newsletter subscription form and send all submitted email addresses to Loops.
* Sync contacts whenever a user's email address is changed in Bubble.
* [Trigger an event](/events) in Loops for all new sign ups using the [Send event endpoint](/api-reference/send-event), to enter new users into a welcome email sequence.
* Periodically sync [contact properties](/contacts/properties) to Loops so you can send personalized emails.

## Learn more

<CardGroup columns="2">
  <Card
    title="Bubble plugin"
    icon={
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="17" viewBox="0 0 16 17"><g fill="none" fillRule="nonzero" transform="translate(.5 .111)"><path fill="#FF4A00" d="M9.361 4.277c-1.474 0-2.928.633-4.037 1.877V.016H3.128v10.336a6.077 6.077 0 0 0 12.151 0c0-3.354-2.563-6.075-5.918-6.075Zm-.157 9.81a3.735 3.735 0 1 1 0-7.47 3.735 3.735 0 0 1 0 7.47Z"/><circle cx="1.53" cy="14.925" r="1.503" fill="#FF4A00"/></g></svg>
  }
    href="/integrations/bubble"
  >
    Manage contacts and send emails with our Bubble plugin.
  </Card>

  <Card title="Loops API" icon="rectangle-terminal" href="/api-reference">
    View all of our API endpoints.
  </Card>

  <Card title="Contact properties" icon="address-book" href="/contacts/properties">
    Learn more about custom contact properties.
  </Card>
</CardGroup>
