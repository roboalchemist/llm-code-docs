# Source: https://www.courier.com/docs/external-integrations/email/sendgrid.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# SendGrid

> Send email notifications through Courier using SendGrid by configuring an API key, sender address, optional template imports, and advanced overrides for full control over message delivery.

## Setup

You will need both a [Courier](https://app.courier.com/signup) and a [SendGrid](https://signup.sendgrid.com/) account.

<Steps>
  <Step title="Navigate to Integrations">
    In Courier, navigate to the [**Integrations**](https://app.courier.com/integrations) page and click on the SendGrid Integration to configure it.
  </Step>

  <Step title="Configure API Key">
    Create a [SendGrid API key](https://app.sendgrid.com/settings/api_keys) in your SendGrid account with "Mail Send" permissions. Copy the API key and paste it into the "API Key" field in the Courier SendGrid configuration.

    <Warning>
      Make sure your SendGrid API key has the correct permissions. Without proper permissions, you may encounter authentication errors.
    </Warning>

    <Note>
      To receive `delivered` events from SendGrid, your [SendGrid API key permissions](https://sendgrid.com/en-us/blog/introducing-api-key-permissions) need to include `email activity` and `inbound parse` so that `delivered` events can be counted in your message metrics.
    </Note>
  </Step>

  <Step title="Set From Address">
    Add an email address to the "From Address" field (e.g., [noreply@example.com](mailto:noreply@example.com)). Click "Add Integration" and then "Save" to complete the setup.
  </Step>
</Steps>

## Profile Requirements

To deliver a message to a recipient over SendGrid, Courier must be provided the recipient's email address. This value should be included in the recipient profile as `email`.

```json icon="code" lines highlight={3} theme={null}
{
  "message": {
    "to": {
      "email": "user@example.com"
    }
    // ... rest of message definition
  }
}
```

## Overrides

Overrides can be used to change the request body that Courier uses to send an email. Overrides are useful when a field is not yet supported by Courier or you would like to override the value that Courier generates. You can override any of the fields supported by SendGrid's `/mail/send` endpoint ([see all v3 mail send request body fields in SendGrid's API documentation](https://docs.sendgrid.com/api-reference/mail-send/mail-send)). Below is an example of overriding the subject and adding an attachment:

```json icon="code" lines highlight={8-15} focus={1-20} theme={null}
{
  "message": {
    "template": "appointment-reminder",
    "to": {
      "email": "user@example.com"
    },
    "data": {
      "name": "Nomen Nescio"
    },
    "providers": {
      "sendgrid": {
        "override": {
          "body": {
            "subject": "Your appointment reminder",
            "attachments": [
              {
                "content": "eyJmb28iOiJiYXIifQ==",
                "type": "application/json",
                "filename": "appointment-details.json"
              }
            ]
          }
        }
      }
    }
  }
}
```

## Email Activity Tracking

For the SendGrid configuration, the toggle, *Enable Email Activity Tracking via Polling*, will allow Courier to use SendGrid's Email Activity API to periodically check on the delivery status of sent emails. The API Key must have Read Access to the Email Activity, and the SendGrid account must have the additional email history add-on enabled. See the documentation for [SendGrid API Keys](https://app.sendgrid.com/settings/api_keys) and [SendGrid Email Activity](https://app.sendgrid.com/settings/billing/addons/email_activity) to ensure the SendGrid account is set up correctly.

<Frame caption="Enable read access to Email Activity on the API Key.">
  <img src="https://mintcdn.com/courier-4f1f25dc/I2m6dzuFRO2SDOem/assets/platform/channels/sendgrid-api-key-permissions.png?fit=max&auto=format&n=I2m6dzuFRO2SDOem&q=85&s=f0fe34e7c3375136f1a6a14f942e3741" width="1030" height="861" data-path="assets/platform/channels/sendgrid-api-key-permissions.png" />
</Frame>

<Frame caption="Upgrade the plan to include extended email activity history.">
  <img src="https://mintcdn.com/courier-4f1f25dc/I2m6dzuFRO2SDOem/assets/platform/channels/sendgrid-addons.png?fit=max&auto=format&n=I2m6dzuFRO2SDOem&q=85&s=2a440ccca4d9b1aecf2abd04b44d3d5b" width="569" height="571" data-path="assets/platform/channels/sendgrid-addons.png" />
</Frame>

## Template Import

You can import your SendGrid templates to use with Courier from the [Courier SendGrid configuration page](https://app.courier.com/channels/sendgrid).

<Note>
  Before you can successfully import SendGrid Dynamic Templates, you will need to make sure of the following:

  * SendGrid templates must be saved as [SendGrid Dynamic Templates](https://docs.sendgrid.com/ui/sending-email/how-to-send-an-email-with-dynamic-templates).
  * Your SendGrid API key must have [full access permissions](https://docs.sendgrid.com/ui/account-and-settings/api-keys) for `Template Engine`.
  * You will need to provide your SendGrid credentials in the configuration page to retrieve your saved templates from SendGrid.
</Note>

### Import Process

Once your SendGrid API key has the appropriate permissions, you will be able to see your templates ready for import from the template import tool. Templates ready for import will appear as selectable checkboxes that you can choose to import.

<Frame caption="Template Import Page">
  <img src="https://mintcdn.com/courier-4f1f25dc/I2m6dzuFRO2SDOem/assets/platform/channels/template-import.png?fit=max&auto=format&n=I2m6dzuFRO2SDOem&q=85&s=2981edaa7da4f72da1848d0c783433a1" width="1010" height="700" data-path="assets/platform/channels/template-import.png" />
</Frame>

## Delivery Tracking

By default, after we send a message, Courier will poll SendGrid periodically to find out if the message was delivered successfully or not.
To get faster status updates, you can setup a webhook so SendGrid can report delivery status directly to Courier.

<Steps>
  <Step title="Get Webhook URL">
    In Courier, visit the [Courier SendGrid provider configuration screen](https://app.courier.com/channels/sendgrid) (from the Channels menu on the left side). There, you will find a Webhook URL.

    <Frame>
      <img src="https://mintcdn.com/courier-4f1f25dc/Okgc82MLlENV5nIi/assets/external-integrations/email/courier-ui.png?fit=max&auto=format&n=Okgc82MLlENV5nIi&q=85&s=6df5ad8d16a599d7f8f9cdb962760631" width="659" height="926" data-path="assets/external-integrations/email/courier-ui.png" />
    </Frame>
  </Step>

  <Step title="Configure SendGrid Webhook">
    Copy the webhook URL, then login to SendGrid. On the left side, choose Settings, then Mail Settings. Next, click on the Event Webhooks link.

    On the next page, click the Create new webhook button. Then fill out the form:

    * **Friendly Name** - Whatever you like
    * **Post URL** - Paste the URL you copied earlier from Courier's website.
    * **Deliverability Data** - Check all 5 boxes.
    * **Security features** - You can leave these disabled. The HTTPS URL you pasted includes a cryptographic token that Courier can use to verify incoming events belong only to you.

    <Frame>
      <img src="https://mintcdn.com/courier-4f1f25dc/gOrhLCtuaRi0MQwP/assets/external-integrations/email/webhook-form.png?fit=max&auto=format&n=gOrhLCtuaRi0MQwP&q=85&s=06718626def7d53ad78680dcdbf76196" width="2562" height="1610" data-path="assets/external-integrations/email/webhook-form.png" />
    </Frame>

    Hit the Save button.
  </Step>

  <Step title="Disable Polling">
    Now that the webhook is configured, you will no longer need Courier to poll for status updates. Wait about an hour before disabling polling to make sure there is no gap in status reporting of any messages already in-flight.

    When you are ready, return to the [Courier SendGrid configuration screen](https://app.courier.com/channels/sendgrid). Flip the toggle switch labeled "Enable polling for status updates" into the off position. Then, press the Save button at the bottom of the screen.
  </Step>
</Steps>

## Troubleshooting

If you encounter issues while using SendGrid with Courier, the troubleshooting guide below can help you resolve common problems. You can also check the [Courier Logs page](https://app.courier.com/logs) to help debug any provider errors you may encounter. For anything else, you may contact [Courier Support](mailto:support@courier.com).

<AccordionGroup>
  <Accordion title="SendGrid API Key Access Forbidden">
    This issue occurs when the request you are trying to perform is not listed under [SendGrid's allowed API key actions](https://docs.sendgrid.com/api-reference/api-key-permissions/api-key-permissions) of the SendGrid API key that you are using.

    #### Solution

    You can do one of the following.

    1. You can perform actions allowed by the API key you generated.
    2. Create a new SendGrid API key that allows the actions you wish to execute.

    **Creating the new SendGrid API key with desired permissions**

    When creating the SendGrid API key, you can [select the permissions in SendGrid's API key settings](https://docs.sendgrid.com/ui/account-and-settings/api-keys) that you need in the setup guide. To do so, visit the SendGrid API keys console and select "Create API Key." It displays the figure shown below.

    <Frame caption="Creating a new SendGrid API key">
      <img src="https://mintcdn.com/courier-4f1f25dc/gOrhLCtuaRi0MQwP/assets/external-integrations/email/sendgrid-create-api-key.png?fit=max&auto=format&n=gOrhLCtuaRi0MQwP&q=85&s=c890f306eb72d0dcf3444f0efce0b704" width="2872" height="1548" data-path="assets/external-integrations/email/sendgrid-create-api-key.png" />
    </Frame>

    As illustrated above, SendGrid allows you to select three permission scopes:

    * Full Access
    * Restricted Access
    * Billing Access.

    In addition, you can select the access levels that you require for your API Key based on your requirements.
  </Accordion>

  <Accordion title="Error: sendgrid invalid email">
    Whenever you try to send an email to an address that does not comply with internet email formatting standards, or if the email does not present on the recipient's mail server, you will get an invalid email error. This response might originate from either your server or the receiver's mail server.

    SendGrid checks the email address format before sending it to ensure that it is legitimate. If the receiver server cannot locate the address, it will return a 550 bounce, indicating that the email address is invalid.

    Inactive recipients who don't connect with your content have invalid email addresses. In addition, for a variety of reasons, unengaged email addresses may be invalid:

    * Invalid emails may contain typos or misformatting, preventing them from reaching a legitimate inbox.

    * An email can become invalid if the user's email address changes, leaving the prior email address empty. The biggest cause of emails being invalid is inactivity or lack of engagement.

    * When an inbox provider, such as Earthlink, goes out of business or a server goes down for good, all email domains under that provider become "dead." The emails linked to this defunct domain are similarly invalid.

    #### Solution

    * Email verification for cleaning or "scrubbing" email lists to increase email deliverability and engagement rates using a variety of digital email verification tools.

    * Sort your email list by why each address signed up for your newsletter. You can use this method to see if your emails are relevant to your readers. If your email communications are irrelevant or out-of-date, it can affect your total engagement rate by lowering open and click-through rates.

    * Contacts can be divided into groups based on their level of interaction. Double-check that it is still legitimate if you come across an email that appears to be graymail. If not, add the address to the unsubscribe or opt-out list.

    * Create a sunset policy. A sunset policy's purpose is to discover disengaged contacts regularly and remove or re-engage them from your email lists.
  </Accordion>

  <Accordion title="Maximum Credits Exceeded SendGrid">
    SendGrid credits denote the number of emails that you can send. SendGrid uses one credit per email, and these credits get renewed at the start of every month. Therefore, [you may encounter this issue in SendGrid's SMTP troubleshooting guide](https://docs.sendgrid.com/for-developers/sending-email/smtp-errors-and-troubleshooting) if you exceed the maximum number of emails your SendGrid account can send.

    #### Solution

    You will have to wait until your quota gets renewed to resolve this error. If this is not an option for you, you can upgrade your SendGrid plan and get more credits based on your requirements.
  </Accordion>

  <Accordion title="SendGrid 535 Authentication Failed Bad Username Password">
    This issue can occur due to the following reasons:

    * Username and password are incorrect. Error 535 occurs when the username and password entered in the Email client are incorrect. Using the incorrect mail server can potentially result in authentication difficulties.

    * The account has been disabled. Accounts might be disabled for a variety of reasons, including past-due payments or spamming difficulties.

    * SMTP Authentication error can occur if your email client does not have SMTP authentication enabled.

    #### Solution

    * Check your username and password, billing plans, and account status.

    * Check whether you have confirmed your email address.

    * Configure SMTP Authentication.

    * Your API Keys should be saved as environment variables. This is a far safer technique, with the additional benefit of only having to change them once rather than searching for them every time they're used.

    * Set up sender authentication for domains so that SPF and DKIM can be set up. This functionality enables you to use industry-standard email authentication protocols to authenticate your domains with the Twilio SendGrid account.
  </Accordion>

  <Accordion title="Sendgrid From Field Not Working">
    This indicates that the `from` address does not correspond to a verified Sender Identity. This issue prevents an email from being sent until it is resolved.

    #### Solution

    Customers are asked to [authenticate their sender identities in SendGrid's sender authentication guide](https://docs.sendgrid.com/glossary/sender-authentication) to sustain the highest attainable sender reputations and to maintain legal sending behavior. The address your receivers will view as the sender of your emails is represented by a sender identity. You can use Domain Authentication or Single Sender Verification to authenticate one or more Sender Identities.
  </Accordion>
</AccordionGroup>
