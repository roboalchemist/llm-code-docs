# Source: https://loops.so/docs/transactional.md

# Transactional email

> How to send transactional email with Loops.

Transactional emails are automated, API-triggered emails that are sent to individual contacts based on a specific action they have taken.

Examples include **confirmation emails**, **password reset emails**, and **purchase confirmations**.

<CardGroup columns="2">
  <Card title="Loops API - Send transactional email" icon="envelope" href="/api-reference/send-transactional-email">
    Read how to send transactional email with our API.
  </Card>
</CardGroup>

## How it works

Sending transactional email with Loops has two steps.

<Steps>
  <Step title="Create transactional emails">
    First, create transactional emails in Loops using our [email
    editor](/creating-emails/editor). In your email you can add data variables,
    which let you insert custom data into each email you send.
  </Step>

  <Step title="Send with the API">
    To send transactional emails you need to use the Loops API. All it takes is
    a simple call to our [Send transactional email
    endpoint](/api-reference/send-transactional-email). Your request needs to
    include the ID of the transactional email you created, the recipient's email
    address and any data variables needed for the email.
  </Step>
</Steps>

## Compose your email

There are two ways to create emails in Loops: using our editor or import an MJML template.

### Use our editor

You can [create emails in the editor](/creating-emails/editor), letting you easily add formatting, images and buttons.

<img src="https://mintcdn.com/loops/4h4NdelN1SeEp2xg/images/transactional-example.png?fit=max&auto=format&n=4h4NdelN1SeEp2xg&q=85&s=6d4f8855f2bb71dbf528ab8da2c4aacb" alt="" data-og-width="2280" width="2280" data-og-height="1355" height="1355" data-path="images/transactional-example.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/4h4NdelN1SeEp2xg/images/transactional-example.png?w=280&fit=max&auto=format&n=4h4NdelN1SeEp2xg&q=85&s=9e8df0d409a4bf917d37a08295dc8455 280w, https://mintcdn.com/loops/4h4NdelN1SeEp2xg/images/transactional-example.png?w=560&fit=max&auto=format&n=4h4NdelN1SeEp2xg&q=85&s=15b343e6210f4aa163570a8709f68152 560w, https://mintcdn.com/loops/4h4NdelN1SeEp2xg/images/transactional-example.png?w=840&fit=max&auto=format&n=4h4NdelN1SeEp2xg&q=85&s=5bdb62280bb095794d570da750a13c0e 840w, https://mintcdn.com/loops/4h4NdelN1SeEp2xg/images/transactional-example.png?w=1100&fit=max&auto=format&n=4h4NdelN1SeEp2xg&q=85&s=c7a97149078a5e2ac87cbd3c41d270a2 1100w, https://mintcdn.com/loops/4h4NdelN1SeEp2xg/images/transactional-example.png?w=1650&fit=max&auto=format&n=4h4NdelN1SeEp2xg&q=85&s=60cebc6a82938cb12f70af9f60ecbd21 1650w, https://mintcdn.com/loops/4h4NdelN1SeEp2xg/images/transactional-example.png?w=2500&fit=max&auto=format&n=4h4NdelN1SeEp2xg&q=85&s=fcb440735577b734aaf52a2a68f1a9f5 2500w" />

You can add dynamic data into your emails by using data variables (like `name` in the example above). Read on for more information about data variables.

### Bring your own MJML

You can also [upload your own MJML code](/creating-emails/uploading-custom-email) to use in the email. This is useful if you have a pre-existing template you want to use.

Like emails created in our editor, you can add data variables to MJML templates. To add a data variable called `passwordResetLink`, you can use it in your MJML like this:

```html  theme={"dark"}
<mj-text>{DATA_VARIABLE:passwordResetLink}</mj-text>
```

<Tip>
  Note the uppercase “DATA\_VARIABLE” and the colon before the variable name.
</Tip>

## Add data variables

Data variables let you insert dynamic values into every transactional email, to personalize them to each recipient. When it comes to sending the email, you specify the value of each data variable in the API call.

Let's say you have a password reset email that is sent once a user clicks a "Reset Password" button in your application.

For this we need to add two data variables to the email: `name` and `resetUrl`.

You can insert data variables into the text of the email in three ways:

* click the `{}` dynamic content button above the editor (see below)
* type variables directly into the editor, like `{planName}`
* use the `/` slash menu (select "Data variable" from the menu).

<img src="https://mintcdn.com/loops/SqldyWKxvGS7UNL4/images/terminal.png?fit=max&auto=format&n=SqldyWKxvGS7UNL4&q=85&s=d124653cd87536765f40e4de3102c15a" alt="" data-og-width="2280" width="2280" data-og-height="1079" height="1079" data-path="images/terminal.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/SqldyWKxvGS7UNL4/images/terminal.png?w=280&fit=max&auto=format&n=SqldyWKxvGS7UNL4&q=85&s=1c1834773261e5a0c8be7a0e1b4191a5 280w, https://mintcdn.com/loops/SqldyWKxvGS7UNL4/images/terminal.png?w=560&fit=max&auto=format&n=SqldyWKxvGS7UNL4&q=85&s=5e9e0bae89a5aded6a9d7448926ff5a8 560w, https://mintcdn.com/loops/SqldyWKxvGS7UNL4/images/terminal.png?w=840&fit=max&auto=format&n=SqldyWKxvGS7UNL4&q=85&s=40030ce29b5df99adb0c950877a84baa 840w, https://mintcdn.com/loops/SqldyWKxvGS7UNL4/images/terminal.png?w=1100&fit=max&auto=format&n=SqldyWKxvGS7UNL4&q=85&s=7712e06a02cfeedd04e43aef5024c6eb 1100w, https://mintcdn.com/loops/SqldyWKxvGS7UNL4/images/terminal.png?w=1650&fit=max&auto=format&n=SqldyWKxvGS7UNL4&q=85&s=cbcbd72414a41dc5717a61b867789fbe 1650w, https://mintcdn.com/loops/SqldyWKxvGS7UNL4/images/terminal.png?w=2500&fit=max&auto=format&n=SqldyWKxvGS7UNL4&q=85&s=3a8450a5d3357e016e9b562574bd68fe 2500w" />

You can also add data variables as links (on text, images and buttons). To add the `resetUrl` as the button's link, click on the data variable icon (1), click the data variable (2) and then enter your data variable name into the **Variable name** field (3).

<img src="https://mintcdn.com/loops/pXWwePlas8rhYOD8/images/passwordresetlink.png?fit=max&auto=format&n=pXWwePlas8rhYOD8&q=85&s=d16b1fcc5dbad1b0253b46e975c045c4" alt="" data-og-width="2280" width="2280" data-og-height="1049" height="1049" data-path="images/passwordresetlink.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/pXWwePlas8rhYOD8/images/passwordresetlink.png?w=280&fit=max&auto=format&n=pXWwePlas8rhYOD8&q=85&s=6be0ac1dc4fefc6122be98beebec72f7 280w, https://mintcdn.com/loops/pXWwePlas8rhYOD8/images/passwordresetlink.png?w=560&fit=max&auto=format&n=pXWwePlas8rhYOD8&q=85&s=db23368453e456524c620643793f920c 560w, https://mintcdn.com/loops/pXWwePlas8rhYOD8/images/passwordresetlink.png?w=840&fit=max&auto=format&n=pXWwePlas8rhYOD8&q=85&s=9391b1b06bf416f0e1d404b288c7bf51 840w, https://mintcdn.com/loops/pXWwePlas8rhYOD8/images/passwordresetlink.png?w=1100&fit=max&auto=format&n=pXWwePlas8rhYOD8&q=85&s=74385eae46b5a8f23764dcc0979e1184 1100w, https://mintcdn.com/loops/pXWwePlas8rhYOD8/images/passwordresetlink.png?w=1650&fit=max&auto=format&n=pXWwePlas8rhYOD8&q=85&s=1bde5d992c1d97db42a60200ee867338 1650w, https://mintcdn.com/loops/pXWwePlas8rhYOD8/images/passwordresetlink.png?w=2500&fit=max&auto=format&n=pXWwePlas8rhYOD8&q=85&s=698c31f35cbc4bfd90fe7eac851a419a 2500w" />

If you want to write the tags manually in your content or [in HTML emails](/creating-emails/uploading-custom-email), you can use our [dynamic tag syntax](/creating-emails/personalizing-emails#dynamic-tag-syntax). To add a reset URL you can write a tag like this:

```
{DATA_VARIABLE:resetUrl}
```

### Data variables in email headers

Data variables are also available in the email sending settings fields, like **From**, **Reply**, **CC**, **BCC** and **Subject**.

Click the `>` button to view all fields and then click the data variable icon. Use sensible names for your data variables, like `bccAddress` or `replyToAddress` so they are clear in your API call.

To send data to these fields, simply include the data variables in your API call as normal ([see below](#send-your-email)).

<img src="https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/data-variables-in-settings.png?fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=7226f894ff9b3663974fa1383b4e3a01" alt="Adding a data variable in the Subject field" data-og-width="2280" width="2280" data-og-height="1140" height="1140" data-path="images/data-variables-in-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/data-variables-in-settings.png?w=280&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=c699a0363ab7f8382b5e10394ec1be3f 280w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/data-variables-in-settings.png?w=560&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=7e79a5d62e16b21dfc53b134bf9733ea 560w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/data-variables-in-settings.png?w=840&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=ff9b2ae162d8fe95921210740a7d22dd 840w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/data-variables-in-settings.png?w=1100&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=2c836c5b413c8094180a51e09ed39697 1100w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/data-variables-in-settings.png?w=1650&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=a6d2afbaed9d450fcbbf61038f23cf1c 1650w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/data-variables-in-settings.png?w=2500&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=1d3f7818970bf466e718cc1bb06a3a10 2500w" />

### Optional data variables

Data variables can be optional, by selecting "Optional" from the selector just below the data variable name.

If a data variable is optional, you can omit the key from the API request entirely, or include the key and send an empty string `""` (sending `null` will not work).

<img src="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/optional-data-variables.png?fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=4f5d86b975c522904fdede6a43ed626f" alt="Optional data variables" data-og-width="2280" width="2280" data-og-height="1140" height="1140" data-path="images/optional-data-variables.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/optional-data-variables.png?w=280&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=dc0fb78face7b11d1c59326b49f61926 280w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/optional-data-variables.png?w=560&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=e949e5592781010fc3ceb3b2f05d5b8f 560w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/optional-data-variables.png?w=840&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=c4401a31741aa12b4bed575138d4b66c 840w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/optional-data-variables.png?w=1100&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=60b45b85d3af38564e3a3db17c98a478 1100w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/optional-data-variables.png?w=1650&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=7a7d3ef4aec37ef57dd9ea81c8d5b342 1650w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/optional-data-variables.png?w=2500&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=0bbd0fbbc057dee460689ee96cc51684 2500w" />

<CardGroup columns="2">
  <Card title="Personalizing emails" icon="crystal-ball" href="/creating-emails/personalizing-emails">
    Read more about adding dynamic content into your emails.
  </Card>

  <Card title="Send transactional email" icon="envelope" href="/api-reference/send-transactional-email">
    Read how to send transactional email with the API.
  </Card>
</CardGroup>

### Important information about data variables

* Make sure that when you [send a transactional email using the API](/api-reference/send-transactional-email) that you include *all non-optional data variables* in your request. If you do not include the correct set of data variables in your API call, the send will fail.
* Data variable names are case-sensitive (meaning `LastLoggedIn` and `lastLoggedIn` are different variables).
* Data variable names can only contain:
  * letters
  * numbers
  * underscores
  * dashes
* Data variable values sent over the API can be `string` or `number`.

## Review your email

On the next page, after clicking **Next**, you'll see the API Details section. This contains the data variables used in the email as well as a sample payload for reference. The “Transactional ID” lets you distinguish between different transactional emails when calling the API and is required.

<img src="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/next.png?fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=553cf454d657a3049b9566e2851d1b0b" alt="" data-og-width="2280" width="2280" data-og-height="1682" height="1682" data-path="images/next.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/next.png?w=280&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=60b1e92d098c794c93b8cfb01310586c 280w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/next.png?w=560&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=c8f8c7d1c2918340532861bb8bd52c4c 560w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/next.png?w=840&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=e9569fd50c07b058708c7447fcf4cacf 840w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/next.png?w=1100&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=695b04041f9dfe709a25a3ad36345426 1100w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/next.png?w=1650&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=ea4ba40f8634d64c2905b0cc375c0c43 1650w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/next.png?w=2500&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=2083f0ff2fc32596387a81dcf6e07f17 2500w" />

## Publish the email

To enable sending the email, it needs to be published by clicking **Publish**.

## Send your email

In the example above, two Data Variables were used in the email and there is a transactional ID needed as part of our API call. Any data variables created in the email are required when making the API request.

Here's an example of the request for sending this email:

**Send a POST to this endpoint (make sure to authenticate)**

```
https://app.loops.so/api/v1/transactional
```

**Payload**

You can copy an email's example payload from its Publish page in Loops by clicking the **Show payload** button.

```json  theme={"dark"}
{
  "transactionalId": "clfq6dinn000yl70fgwwyp82l",
  "email": "favorite@example.com",
  "dataVariables": {
    "name": "Chris",
    "passwordResetLink": "https://example.com/reset-password",
    "bccAddress": "me@company.com"
  }
}
```

You can add contacts to your audience from this call by adding `"addToAudience": true` to your payload.

<CardGroup columns="2">
  <Card title="Loops API - Send transactional email" icon="envelope" href="/api-reference/send-transactional-email">
    Read how to send transactional email with our API.
  </Card>

  <Card title="JavaScript/TypeScript SDK" icon="js" href="/sdks/javascript">
    Integrate our SDK into your JS or TS application.
  </Card>
</CardGroup>

## Editing the email

To edit the email, click **Edit Draft** on the Compose page.

<img src="https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/duplicate.png?fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=d0722987bdb55333b7a630f32df19a6f" alt="" data-og-width="2280" width="2280" data-og-height="1058" height="1058" data-path="images/duplicate.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/duplicate.png?w=280&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=23829ad96cfe8eece509bf2c058c9112 280w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/duplicate.png?w=560&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=e99b9584aadc2380cd7b44858c14f4b3 560w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/duplicate.png?w=840&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=8056e89a2e06b4eaf89880193d99533f 840w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/duplicate.png?w=1100&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=87794cfed2796331f07d42e62f5fe06f 1100w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/duplicate.png?w=1650&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=3d41f03a085fcdd28992ab63e05b19cf 1650w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/duplicate.png?w=2500&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=c044b70bfde0253163ac1c2c774621a8 2500w" />

The previous published version of the email will remain, and will continue sending until you republish the email. This means you can make changes to transactional emails without disrupting ongoing email sending.

When you have a draft, we retain both versions and you can switch between your draft and the published version using the toggles in the top right.

<img src="https://mintcdn.com/loops/SqldyWKxvGS7UNL4/images/view-draft.png?fit=max&auto=format&n=SqldyWKxvGS7UNL4&q=85&s=82ae4a335444a0a469056a501ba39aae" alt="" data-og-width="2280" width="2280" data-og-height="1058" height="1058" data-path="images/view-draft.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/SqldyWKxvGS7UNL4/images/view-draft.png?w=280&fit=max&auto=format&n=SqldyWKxvGS7UNL4&q=85&s=6d80ed67511413636bc22be7bacb7b68 280w, https://mintcdn.com/loops/SqldyWKxvGS7UNL4/images/view-draft.png?w=560&fit=max&auto=format&n=SqldyWKxvGS7UNL4&q=85&s=9f625a110f267a2d56df898baacb6a2e 560w, https://mintcdn.com/loops/SqldyWKxvGS7UNL4/images/view-draft.png?w=840&fit=max&auto=format&n=SqldyWKxvGS7UNL4&q=85&s=5d3e788d9786d738cb418aa2bdd90fd1 840w, https://mintcdn.com/loops/SqldyWKxvGS7UNL4/images/view-draft.png?w=1100&fit=max&auto=format&n=SqldyWKxvGS7UNL4&q=85&s=cf8a29535f024fea6911fb6bc60bb424 1100w, https://mintcdn.com/loops/SqldyWKxvGS7UNL4/images/view-draft.png?w=1650&fit=max&auto=format&n=SqldyWKxvGS7UNL4&q=85&s=9d37d949adcd2d894672c90803c1f73f 1650w, https://mintcdn.com/loops/SqldyWKxvGS7UNL4/images/view-draft.png?w=2500&fit=max&auto=format&n=SqldyWKxvGS7UNL4&q=85&s=ab6a8b24582e7d7fbf84d664fc1f97f7 2500w" />

To publish your changes, simply click **Republish** and click the confirmation. Your draft will seamlessly become the published version.

## Metrics

After emails are sent, details are shown in the email's Metrics page.

These include send time and if messages experienced any issues with delivery (bounces or spam complaints).

<Tip>
  Note that open and click tracking is disabled for transactional messages to
  improve deliverability for infrastructure-level communications.
</Tip>

## Testing transactional emails

You can test your transactional email integration by sending to email addresses with `@example.com` and `@test.com` domains (for example `user1@example.com` and `user2@example.com`).

Everything will work as normal (e.g. you will receive success responses from the API), but no emails will be sent to `@example.com` or `@test.com` email addresses, making this a good way to test transactional emails without affecting your sending domain’s reputation.

## Errors

### Links look like `x-webdoc://....`

This is a known issue with Apple Mail. Make sure that your links start with `https://` or `http://` and they should work fine.

### API (400-level error)

The first place to start is to check the body of the response. It will contain a JSON object with a `message` property that will give you more information about the error. Here are common reasons that the API might return with a 400-level error:

* Using the API without a [verified domain](/sending-domain).
* Trying to use the API for a transactional email without a published email message.
* Missing a required parameter: `transactionalId`, `email`, or `dataVariables`.
* Missing a data variable that is required by the email message.
