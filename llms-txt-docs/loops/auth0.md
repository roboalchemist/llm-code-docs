# Source: https://loops.so/docs/integrations/auth0.md

# Auth0

> Send Auth0 authentication emails with Loops.

Set up an SMTP connection to send all of your Auth0 emails with Loops.

There are two big benefits to using Loops for sending your Auth0 emails:

<Steps>
  <Step title="More control over design">
    You can use [Loops' design editor](/creating-emails/editor) to create (and
    then easily edit) beautiful transactional emails instead of having to code
    them with HTML.
  </Step>

  <Step title="Better visibility of sent emails">
    You get full visibility on which emails are being sent, when, and to whom in
    your Loops account. Auth0 doesn't offer this view.
  </Step>
</Steps>

## Set up Loops SMTP in Auth0

Go to **Branding -> Email Provider** in your Auth0 dashboard.

Scroll down and click on **SMTP Provider**.

In the SMTP Provider Settings section below, enter a value into the "From" field. This value will *always be overwritten by the values set in your Loops templates* from the next step, so it can be anything.

In the **SMTP Provider Settings** section enter the following data:

| Field       | Value                                                                                      |
| ----------- | ------------------------------------------------------------------------------------------ |
| Host        | `smtp.loops.so`                                                                            |
| Port number | `587`                                                                                      |
| Username    | `loops`                                                                                    |
| Password    | An API key copied from your [API settings](http://app.loops.so/settings?page=api) in Loops |

<img src="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/auth0-smtp-settings.png?fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=0e9c4040abd71242d76193c93de5b0d9" alt="" data-og-width="2280" width="2280" data-og-height="1982" height="1982" data-path="images/auth0-smtp-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/auth0-smtp-settings.png?w=280&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=e71fadd067ef09ccb3bb07aede4578ea 280w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/auth0-smtp-settings.png?w=560&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=25558b44c1609da7c91dc0f331d14e23 560w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/auth0-smtp-settings.png?w=840&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=89abcc30c9f0309150f9de1dd86c5822 840w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/auth0-smtp-settings.png?w=1100&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=f72aee593f991e4ceb91bb46da01b275 1100w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/auth0-smtp-settings.png?w=1650&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=d4a837442cd8c6ca99f1a05820e73ab5 1650w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/auth0-smtp-settings.png?w=2500&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=d0d74f21bb3065806376108865abd16c 2500w" />

<Info>
  The **Send Test Email** button here will not work due to how the Loops SMTP
  system works. You can test your connection in a later step.
</Info>

## Create Transactional emails in Loops

Next, create new transactional emails for the emails you are sending from Auth0. Go to **Branding -> Email Templates** to view the full list.

In Loops, go to the [Transactional page](https://app.loops.so/transactional) and click **New**. Alternatively, you can select one of our many ready-made templates from the [Templates page](https://app.loops.so/templates).

<img src="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/auth0-template.png?fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=a9a8f86342faca1e1e856db175308419" alt="" data-og-width="2280" width="2280" data-og-height="1328" height="1328" data-path="images/auth0-template.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/auth0-template.png?w=280&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=9096514b285c31ccc0e07ba4b520445e 280w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/auth0-template.png?w=560&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=5b54782f56de12e259741a1731679b7a 560w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/auth0-template.png?w=840&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=0ec243c92b6ac95ec772674d57978fb4 840w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/auth0-template.png?w=1100&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=513decde06d290b3dae9536f491af5ef 1100w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/auth0-template.png?w=1650&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=da714792b13ed1a557252b9d54a2295a 1650w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/auth0-template.png?w=2500&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=d55b0723adaf7fef99d2bcf25c41ad10 2500w" />

You can then use [the Loops editor](/creating-emails/editor) to create nicely-designed templates or make them as simple as you like.

You can even create [themes](/creating-emails/styles#themes) to apply consistent design and branding to all of your emails.

For each Loops template you create, you need to [add data variables](/creating-emails/personalizing-emails#add-dynamic-content-to-emails), which allow data from Auth0 to be inserted into each email.

You can check the list of [Common variables](https://auth0.com/docs/customize/email/email-templates#common-variables) supported in each email from the Auth0 documentation.

Once you're done creating the email and adding the data variables, click **Next**. On the next page, click the **Show payload** button to view the API payload for your template. You will need this for the next step.

<img src="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/auth0-payload.png?fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=63c92241cd4776a87d320451d3099eef" alt="" data-og-width="2280" width="2280" data-og-height="1454" height="1454" data-path="images/auth0-payload.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/auth0-payload.png?w=280&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=d9afa972a55760d973ce1e62286a8ee9 280w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/auth0-payload.png?w=560&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=2f9cd94bfa8d0e9c1bcb5766b9516e56 560w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/auth0-payload.png?w=840&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=e3f0acef8a871c0932f1f1489a6a6755 840w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/auth0-payload.png?w=1100&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=e4a586a2503fe8264368a8f3448a0feb 1100w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/auth0-payload.png?w=1650&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=34c7b8870b03aacfdcc1a0b726d19571 1650w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/auth0-payload.png?w=2500&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=e779a2265456a050f24d3d875060e811 2500w" />

Make sure to also publish your email! It won't send unless it's published.

<CardGroup>
  <Card title="Transactional email guide" icon="code" href="/transactional">
    Read our detailed guide for sending transactional emails.
  </Card>
</CardGroup>

## Configure email templates in Auth0

The final step is to make sure your emails in Auth0 are configured to send the correct data to Loops.

<Warning>
  Make sure you set up at least the **Verification Email (using Link)** or
  **Verification Email (using code)** templates in Auth0. Enable other emails
  based on your user flows.
</Warning>

Loops SMTP integrations work a bit differently than most. Instead of sending a text or HTML email body, you set them up to send API-like data.

In Auth0, go to **Branding -> Email Templates**, then edit each template to contain the payload as shown in the previous step (you can click the clipboard icon in Loops to copy the full payload).

<Tip>
  Make sure that each template you want to use in Auth0 has the **Status** field
  enabled.
</Tip>

If you are using Passwordless authentication, add your Loops payload into the **Body** field at **Authentication -> Passwordless -> Email**.

Once pasted into the **Message** body, you need to add the Auth0 message variables into the payload. You can do this using double curly brackets like `{{ url }}`.

Here is an example "Verification Email (using Link)" email template. This payload was copied from the template's Publish page in Loops, then the `{{ user.email }}` and `{{ url }}` Auth0 variables were added.

```json  theme={"dark"}
{
  "transactionalId": "clvmzp39u035tl50pw7wrl0ri",
  "email": "{{ user.email }}",
  "dataVariables": {
    "productName": "{{ application.name }}",
    "url": "{{ url }}"
  }
}
```

If you want to add each Auth0 user to your Loops audience so you can send marketing email to them, add the `addToAudience` flag to your template as below. This will create a contact in Loops using the `{{ user.email }}` value.

```json {4} theme={"dark"}
{
  "transactionalId": "clvmzp39u035tl50pw7wrl0ri",
  "email": "{{ user.email }}",
  "addToAudience": true,
  "dataVariables": {
    "productName": "{{ application.name }}",
    "url": "{{ url }}"
  }
}
```

Here's how the template looks in the Auth0 editor:

<img src="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/auth0-email.png?fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=a8493d476ff113be14647e077db93c60" alt="" data-og-width="2280" width="2280" data-og-height="1407" height="1407" data-path="images/auth0-email.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/auth0-email.png?w=280&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=5d8d3ff219cd9dc72bd8d21e5ebb56f2 280w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/auth0-email.png?w=560&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=29f4d36b22c660868002d040ae624c7b 560w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/auth0-email.png?w=840&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=cd0fd028ef6fc23b6f71ed214d828f67 840w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/auth0-email.png?w=1100&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=d017395fb87350e0f63c5e752eb0f867 1100w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/auth0-email.png?w=1650&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=ede8afa9fd3fd7336a01abdc004d6544 1650w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/auth0-email.png?w=2500&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=b743650316fe100eef7201889be04263 2500w" />

To test that everything works, click the **Try** button beneath the editor. Insert your email address in the modal that appears, then click **Try** to send the email.

You will also be able to see activity for your email sends in **Monitoring -> Logs**.

The best way to view your Auth0 email history is in Loops. Go to your [Transactional](https://app.loops.so/transactional) page then click on one of your emails. Click on **Metrics** in the left menu to view a page containing a table showing all sends and some statistics.

## Important notes

* The subject in Auth0 templates is always overwritten by the subject added to the corresponding template in Loops.
* The sender email configured in your Auth0 SMTP settings is always overwritten by the "From" address added to your templates in Loops.
* Any enabled Auth0 template not set up with the correct API-like payload will fail to send.
