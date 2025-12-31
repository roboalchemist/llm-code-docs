# Source: https://loops.so/docs/guides/onboarding-emails.md

# Your first onboarding emails

> Some best practices for building your sender reputation with onboarding emails.

We covered the basics of a Sender Reputation in [this guide](/deliverability/sending-reputation) and this guide will cover some best practices for building your sender reputation with onboarding emails.

If you're new to Loops, we recommend taking some specific steps to help warm up your sending reputation and to ensure your emails land in inboxes.

We want to start with an onboarding Loop and transactional emails before we send larger campaigns to a large list. When we send those larger campaigns, we want to first start with a small list and then slowly increase volume while monitoring the results.

## Onboarding welcome loop

The first step is to set up a welcome email sent to users after they sign up to your application or subscribe to your list. Recipients of these emails are expecting the email and are most likely to engage with it.

For example, new users who sign up could expect a welcome email from you, welcoming them to your platform and explaining some initial steps to get them started.

Here is an example of the email we at Loops send out to new users:

<img src="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/loops-welcome-email.png?fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=d040d1fec19fee4f9d921a4848a571d5" alt="Loops' own welcome email" data-og-width="2280" width="2280" data-og-height="1613" height="1613" data-path="images/loops-welcome-email.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/loops-welcome-email.png?w=280&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=0c006a12ea631e4ae09fd2c0c1053417 280w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/loops-welcome-email.png?w=560&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=da8e983294ff96dbe01334acae86dc26 560w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/loops-welcome-email.png?w=840&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=3a28a60a8f74857465fe12f6cd70f038 840w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/loops-welcome-email.png?w=1100&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=0fc63d67ecb36d086390fd0292996a43 1100w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/loops-welcome-email.png?w=1650&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=efb019a4988b2460144d8e65c0f03b99 1650w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/loops-welcome-email.png?w=2500&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=46b25b5fe743e4665cb0cf94a76c3ca9 2500w" />

<CardGroup>
  <Card href="https://app.loops.so/templates?category=loops" title="Loop templates" icon="folder-closed">
    Check out our library of useful templates for creating welcome emails.
  </Card>
</CardGroup>

Users receive these emails because they expect them, so they are more likely to open and engage with them, building your sender reputation.

Get started by [creating loops](/loop-builder), which are email automations used to send emails after certain triggers, like a new contact joining your audience or after an event happens in your platform.

### Creating a welcome loop in Loops

<img src="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/onboarding-loop.png?fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=4d302090135bc255608bf93beb116507" alt="A simple welcome loop" data-og-width="2280" width="2280" data-og-height="1964" height="1964" data-path="images/onboarding-loop.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/onboarding-loop.png?w=280&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=2ad7953c65198241a9878b9a180518ab 280w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/onboarding-loop.png?w=560&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=f76d89aea68b1987be87f91440973633 560w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/onboarding-loop.png?w=840&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=08db4b38ffaafacd096cdae3c47b1003 840w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/onboarding-loop.png?w=1100&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=90c1d6b270cab2380eb55e10dca75bd3 1100w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/onboarding-loop.png?w=1650&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=0f7ed11f8a5e5b7dfef10344acb58e8c 1650w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/onboarding-loop.png?w=2500&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=a11c1fa9387da1fef330ee1843bf2994 2500w" />

<Steps>
  <Step title="Create a loop">
    Go to your [Loops page](https://app.loops.so/loops) and click **New**, or select from one of our [ready-made templates](https://app.loops.so/templates).
  </Step>

  <Step title="Set the trigger">
    Set your trigger to **Contact added** if you want the loop to fire for every new contact. You can also set a filter to only send to contacts with a specific tag or property, or specifically target it to a specific list.

    Select **Event received** if you want to trigger the loop based on something happening in an external platform.
  </Step>

  <Step title="Add an email">
    Next, write your email by clicking on the **Send email** node.\
    Make sure to make your loop active by clicking **Start**.
  </Step>
</Steps>

## Transactional emails

Transactional emails are by definition emails that are sent to users because of an action they took or need to take to use your platform. Since all emails from Loops send from a single domain and IP, we can also use these emails to build our sender reputation. We recommend starting with these essential transactional emails:

* Login verification emails
* Password reset emails
* Account confirmation emails

These types of emails have high engagement rates since users actively request them, which helps build your sender reputation.

<img src="https://mintcdn.com/loops/4h4NdelN1SeEp2xg/images/transactional-example.png?fit=max&auto=format&n=4h4NdelN1SeEp2xg&q=85&s=6d4f8855f2bb71dbf528ab8da2c4aacb" alt="Password reset email example" data-og-width="2280" width="2280" data-og-height="1355" height="1355" data-path="images/transactional-example.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/4h4NdelN1SeEp2xg/images/transactional-example.png?w=280&fit=max&auto=format&n=4h4NdelN1SeEp2xg&q=85&s=9e8df0d409a4bf917d37a08295dc8455 280w, https://mintcdn.com/loops/4h4NdelN1SeEp2xg/images/transactional-example.png?w=560&fit=max&auto=format&n=4h4NdelN1SeEp2xg&q=85&s=15b343e6210f4aa163570a8709f68152 560w, https://mintcdn.com/loops/4h4NdelN1SeEp2xg/images/transactional-example.png?w=840&fit=max&auto=format&n=4h4NdelN1SeEp2xg&q=85&s=5bdb62280bb095794d570da750a13c0e 840w, https://mintcdn.com/loops/4h4NdelN1SeEp2xg/images/transactional-example.png?w=1100&fit=max&auto=format&n=4h4NdelN1SeEp2xg&q=85&s=c7a97149078a5e2ac87cbd3c41d270a2 1100w, https://mintcdn.com/loops/4h4NdelN1SeEp2xg/images/transactional-example.png?w=1650&fit=max&auto=format&n=4h4NdelN1SeEp2xg&q=85&s=60cebc6a82938cb12f70af9f60ecbd21 1650w, https://mintcdn.com/loops/4h4NdelN1SeEp2xg/images/transactional-example.png?w=2500&fit=max&auto=format&n=4h4NdelN1SeEp2xg&q=85&s=fcb440735577b734aaf52a2a68f1a9f5 2500w" />

<CardGroup>
  <Card href="https://app.loops.so/templates?category=transactional" title="Transactional templates" icon="folder-closed">
    Check out our library of useful transactional email templates.
  </Card>
</CardGroup>

## Targeted campaign

Once your welcome loop has been active and sending for 2 or 3 days, you should see an open rate of around 40% on the first email after the welcome email.

Now you can start to send a campaign to a small list of engaged users. Here are two recommended approaches:

1. Target recent signups using the `createdAt` property to find users added in the last 3 days
2. Target active users by syncing login data to track your most engaged users

For your first campaign content, we recommend:
✅ Product updates or new feature announcements
❌ Avoid generic newsletters, giveaways or promotional content

Important metrics to monitor:

* Campaign open rate should be above 30%
* Welcome loop open rate should stay above 40%
* If either drops below these thresholds, pause sending and re-evaluate

Loops helps to mitigate deliverability issues by sending campaign emails in batches, waiting to check open rates and then sending further emails in your list depending on the results. We take great care to make sure your emails have the highest deliverability as possible from our side.

### Sending a campaign to active users in Loops

<Steps>
  <Step title="Define and label &#x22;active&#x22; users">
    You can use the default `createdAt` contact property, or you can create custom [contact properties](/contacts/properties#custom-contact-properties) and use the [API](/api-reference/update-contact) or an [integration](/integrations) to update contacts when an event happens in your account (e.g. a log in).

    For example, you could use the name `lastActive` and choose the "Date" field type. Then whenever the user does a major action in your application, update the contact with a new `lastActive` value:

    ```javascript  theme={"dark"}
    POST /v1/contacts/update
    {
      "userId": user.id,
      "lastActive": new Date().getTime() // timestamp in milliseconds
    }
    ```
  </Step>

  <Step title="Send the campaign to your segment">
    Once you have created your campaign in Loops, you need to specify the audience based on your chosen date field.

    In the "Audience" tab, choose "Last Active" (or "Created At"), then "After" and then pick the date three days ago from the date field.

        <img src="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/active-audience.png?fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=b515b1248a047295d16e6aaa23149160" alt="Selecting an active audience" data-og-width="2280" width="2280" data-og-height="1367" height="1367" data-path="images/active-audience.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/active-audience.png?w=280&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=ce0c69d202542a5afdd8bbf41316c276 280w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/active-audience.png?w=560&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=0aa20e6acf52611d5ff67a238a82c097 560w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/active-audience.png?w=840&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=45d0c28c404c1103662e9ef47864b2f1 840w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/active-audience.png?w=1100&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=ba5a10f6cbeb02a6a1165c80dad657ae 1100w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/active-audience.png?w=1650&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=99bafa2a560cfdc50267ed13067a90dd 1650w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/active-audience.png?w=2500&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=0aad9c4d362ffe8223b98e5f2774d335 2500w" />
  </Step>
</Steps>

## Larger campaigns

Now you have warmed up your account, you can start to send out larger campaigns to more contacts.

You may want to import users from another email platform of your application's user database.

We still recommend to not send to everyone on your list. Try to identify segments in your user list (especially if it's in the thousands) that are most likely to open emails from you.

## Read more

<CardGroup>
  <Card title="Improve your inbox placement" icon="inbox" href="/deliverability/improving-inbox-placement" />

  <Card title="Understand email open rates" icon="envelope-open-text" href="/deliverability/understanding-email-open-rates" />

  <Card title="Delivery optimization" icon="chart-line" href="/deliverability/optimization" />

  <Card title="Build your sender reputation" icon="shield" href="/deliverability/sending-reputation" />
</CardGroup>
