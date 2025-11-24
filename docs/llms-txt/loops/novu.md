# Source: https://loops.so/docs/integrations/novu.md

# Novu

> Send Novu email notifications with Loops SMTP.

Set up an SMTP connection to send Novu notification emails with Loops.

## Set up Loops SMTP in Novu

Go to the [Integration Store settings](https://dashboard-v2.novu.co/integrations) in Novu and create a new email provider.

Click **Connect Provider** and then **Custom SMTP**.

Give your provider a name like "Loops SMTP" in the **Name** field.

Then add the following details into each field:

| Field    | Value                                                                                      |
| -------- | ------------------------------------------------------------------------------------------ |
| User     | `loops`                                                                                    |
| Password | An API key copied from your [API settings](http://app.loops.so/settings?page=api) in Loops |
| Host     | `smtp.loops.so`                                                                            |
| Port     | `587`                                                                                      |

You also have to add values to the **From email address** and **Sender name** fields because Novu requires them. You can add any value here because Loops will overwrite these values when sending emails.

Click **Create Integration** to finish setup.

<img src="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/novu-setup.png?fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=1f623a8e2fc5ceae51a8000c59027940" alt="Setting up custom SMTP in Novu" data-og-width="2280" width="2280" data-og-height="3231" height="3231" data-path="images/novu-setup.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/novu-setup.png?w=280&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=28391e5c4567966a21d43977a447ddcd 280w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/novu-setup.png?w=560&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=61349160bfc4ad2868df1e081ef2c79e 560w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/novu-setup.png?w=840&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=07346563228677cd35215257a3fd5e40 840w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/novu-setup.png?w=1100&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=1b4a0f193385ebab921105fff71cc1ba 1100w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/novu-setup.png?w=1650&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=48a9e802fec0c8ef2a561142feddd096 1650w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/novu-setup.png?w=2500&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=b0925bff41e68e0208d7b23ab0f88163 2500w" />

## Create Transactional emails in Loops

Next, create new transactional emails for the emails you are sending from Novu.

In Loops, go to the [Transactional page](https://app.loops.so/transactional) and click **New**. Alternatively, you can select one of our many ready-made templates from the [Templates page](https://app.loops.so/templates).

<img src="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/novu-template.png?fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=9f7d2854940de43c02bf6720b9da6565" alt="" data-og-width="2280" width="2280" data-og-height="1214" height="1214" data-path="images/novu-template.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/novu-template.png?w=280&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=8d99a1f5006d9dba4c7128c7a41e099f 280w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/novu-template.png?w=560&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=f79abe3974dbde7d132bdec6abacb3a1 560w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/novu-template.png?w=840&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=12978dcbc68da1a057cf86d2dee92ab6 840w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/novu-template.png?w=1100&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=dcf181971fbc140e6479e1971d8bbddf 1100w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/novu-template.png?w=1650&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=6bc6feba8c6a5fa5a2fbbf58213d3ba2 1650w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/novu-template.png?w=2500&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=64021d2ce9f93935233f1318cdb0bcaf 2500w" />

You can then use [the Loops editor](/creating-emails/editor) to create nicely-designed templates or make them as simple as you like.

You can even create [themes](/creating-emails/styles#themes) to apply consistent design and branding to all of your emails.

For each Loops template you create, you can add [add data variables](/creating-emails/personalizing-emails#add-dynamic-content-to-emails), which allow data from Novu to be inserted into each email.

Once you're done creating the email and adding the data variables, click **Next**. On the next page, click the **Show payload** button to view the API payload for your template. You will need this for the next step.

<img src="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/novu-payload.png?fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=fb4f3cb4526e1f3fcdde5a4db51b00aa" alt="" data-og-width="2280" width="2280" data-og-height="1380" height="1380" data-path="images/novu-payload.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/novu-payload.png?w=280&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=8776b026bb3c8bd9d5a35b7e131d2e12 280w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/novu-payload.png?w=560&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=1a6f6574c3792c466415ee520cd23923 560w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/novu-payload.png?w=840&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=8c73cabc9ab05bac8d640da0f14dc594 840w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/novu-payload.png?w=1100&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=ca438f68e9a9fef4be3e79da36e36ebf 1100w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/novu-payload.png?w=1650&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=e9b6823ff06e5840b7f2bdd39ba1e722 1650w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/novu-payload.png?w=2500&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=f5450088c6f5590bffebd0e04ee954f9 2500w" />

Make sure to also publish your email! It won't send unless it's published.

<CardGroup>
  <Card title="Transactional email guide" icon="code" href="/transactional">
    Read our detailed guide for sending transactional emails.
  </Card>
</CardGroup>

## Configure email templates in Novu

The final setup step is to add email templates in Novu.

Loops SMTP integrations work a bit differently than most. Instead of sending a text or HTML email body, you set them up to send API-like data.

In Novu, go to **Workflows** and create a new workflow. Give it a descriptive name and click **Create workflow**.

You will enter the workflow UI. Add an **Email** node. In the email body paste the transactional payload from Loops from the previous step.

<img src="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/novu-email-1.png?fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=34cf1bd578528dbfcbc945ed6a1fd522" alt="Novu template editor" data-og-width="2280" width="2280" data-og-height="1448" height="1448" data-path="images/novu-email-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/novu-email-1.png?w=280&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=b0e1e6d91d5f942534d24aa3cdd3c75b 280w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/novu-email-1.png?w=560&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=af57809e49bdaa05b8625e380b40df98 560w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/novu-email-1.png?w=840&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=f47f885f8b96b63a261dba3b77f4ec7b 840w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/novu-email-1.png?w=1100&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=0b160f6f9b3a0f53e6dbb053e66345e7 1100w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/novu-email-1.png?w=1650&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=6bc4c149dcf0a569f8175becdb9f78e5 1650w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/novu-email-1.png?w=2500&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=5c48c6d83578af13fce4bf52ad3061fd 2500w" />

Add a subject, but note that this will be overwritten by the subject you added to your Loops transactional email.

Next you need to add some Novu data into the template, namely the recipient's email and any data variables you added in Loops.

Here is an example **Confirm signup** email template. This payload was copied from the template's Publish page in Loops, then the `{{ subscriber.email }}` and `{{ payload.loginUrl }}` variables from Novu were added.

You can add any custom data to the `payload` object when triggering emails from Novu. We need to pass those same values to your Loops transactional email via the `dataVariables` data.

```json Email template in Novu theme={"dark"}
{
  "transactionalId": "cm67vfcgs00pha22s3qevs7nr",
  "email": "{{ subscriber.email }}",
  "dataVariables": {
    "loginUrl": "{{ payload.loginUrl }}"
  }
}
```

If you want to add each Novu subscriber to your Loops audience so you can send marketing email to them, add the `addToAudience` flag to your template as below. This will create a contact in Loops using the `{{ subscriber.email }}` value.

```json Email template in Novu {4} theme={"dark"}
{
  "transactionalId": "cm67vfcgs00pha22s3qevs7nr",
  "email": "{{ subscriber.email }}",
  "addToAudience": true,
  "dataVariables": {
    "loginUrl": "{{ payload.loginUrl }}"
  }
}
```

If you want to include [Novu subscriber attributes](https://docs.novu.co/concepts/subscribers#subscriber-attributes) to personalise your Loops email, you can add them into your Novu template just like the following example.

Make sure to add fallbacks for all non-required values and add the corresponding data variables (e.g. `firstName` here) into your Loops transactional email.

```json Email template in Novu {6} theme={"dark"}
{
  "transactionalId": "cm67vfcgs00pha22s3qevs7nr",
  "email": "{{ subscriber.email }}",
  "dataVariables": {
    "loginUrl": "{{ payload.loginUrl }}",
    "firstName": "{{ subscriber.firstName | default: 'subscriber' }}"
  }
}
```

Here's how a template with variables added looks in the Novu editor:

<img src="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/novu-email-2.png?fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=f0144ef1dce4107a8beb6f3b7fedbc9c" alt="Novu template editor" data-og-width="2280" width="2280" data-og-height="1448" height="1448" data-path="images/novu-email-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/novu-email-2.png?w=280&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=05ecb233fa73d2b69bfb64058a2918a8 280w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/novu-email-2.png?w=560&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=c40b9e45a32b19e3ed384795a367d1b1 560w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/novu-email-2.png?w=840&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=45c7f83d28b6d92ee0ef8896c1308cfe 840w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/novu-email-2.png?w=1100&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=1b51476d3b70506b0a5d48f1ac429ad7 1100w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/novu-email-2.png?w=1650&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=5e010bd5a6e8c9089fcb4b3d9186f84e 1650w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/novu-email-2.png?w=2500&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=d1ea7943a92bccf86699c1219736f57a 2500w" />

Now you're all set up to start sending!

## Trigger emails with Novu

When it comes to triggering Novu notifications to subscribers, you can use the Novu [SDKs](https://docs.novu.co/sdks/overview) or [API](https://docs.novu.co/api-reference/events/trigger-event).

In each call, you need to specify your workflow by its ID, add recipient data and also pass in any data variables for your Loops transactional email into the payload.

Using the same example from above, here's the trigger using Novu's Node SDK.

<Info>
  You can add a `to.email` value to send notifications to a specific email
  address.
</Info>

```javascript  theme={"dark"}
import { Novu } from "@novu/node";

const novu = new Novu("<NOVU_SECRET_KEY>");

await novu.trigger("<WORKFLOW_TRIGGER_IDENTIFIER>", {
  to: {
    subscriberId: "67867a14722783d44d69fc5a",
  },
  payload: {
    loginUrl: "https://myapp.com/login/",
  },
});
```

Here's the same request using the API:

```json  theme={"dark"}
POST https://api.novu.co/v1/events/trigger

{
  "name": "<WORKFLOW_TRIGGER_IDENTIFIER>",
  "to": {
    "subscriberId": "67867a14722783d44d69fc5a"
  },
  "payload": {
    "loginUrl": "https://myapp.com/login/"
  }
}
```

<Tip>
  To view all sends of your transactional emails, click through to the email
  from the [Transactional](https://app.loops.so/transactional) page in Loops,
  where you'll find the Metrics page containing a table showing all sends and
  some statistics.
</Tip>

## Testing the integration

Novu offers a testing UI where you can try out your set up before going live.

Go to the **Workflows** page and click on your workflow, then select the **Trigger** tab.

Here you will be able to set different subscriber and payload data and send test email notifications. The SDK examples below also update, so you can easily create code for your application.

You can also see logs of all emails sent from the [Activity Feed](https://dashboard-v2.novu.co/env/_/activity-feed) page in Novu.

<img src="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/novu-testing.png?fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=c7d2dee69e9a3b34d688625babdab227" alt="Novu testing" data-og-width="2280" width="2280" data-og-height="1805" height="1805" data-path="images/novu-testing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/novu-testing.png?w=280&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=22a953367d8fa9e78d4e17cbecfab2e3 280w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/novu-testing.png?w=560&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=a7245ca53f8b77a22d074e9d881625fb 560w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/novu-testing.png?w=840&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=73c20890931a4c805d3d15953167cedd 840w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/novu-testing.png?w=1100&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=f992af019eef5fb51d505bd1517b5105 1100w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/novu-testing.png?w=1650&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=a1fc10b4917b8d1baa16ade7f50e448f 1650w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/novu-testing.png?w=2500&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=553e7cf260aa015f6af84f3972ac26e2 2500w" />

## Important notes

* The subject in Novu templates is always overwritten by the subject added to the corresponding template in Loops.
* The **From email address** and **Sender name** configured in your Novu SMTP settings are always overwritten by the sender details added to your templates in Loops.
