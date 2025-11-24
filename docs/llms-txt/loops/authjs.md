# Source: https://loops.so/docs/integrations/authjs.md

# Auth.js

> Send Auth.js magic link emails with Loops.

Use Loops to send your [Auth.js Magic Link](https://authjs.dev/getting-started/authentication/email) emails.

<Info>
  You must configure a [database
  adaptor](https://authjs.dev/getting-started/database) to use Magic Link
  authentication in Auth.js.
</Info>

There are two big benefits to using Loops for sending your Auth.js emails:

<Steps>
  <Step title="More control over design">
    You can use [Loops' design editor](/creating-emails/editor) to create (and
    then easily edit) beautiful transactional emails instead of having to code
    them with HTML.
  </Step>

  <Step title="Better visibility of sent emails">
    You get full visibility on which emails are being sent, when, and to whom in
    your Loops account. Auth.js doesn't offer this out of the box.
  </Step>
</Steps>

## Create a transactional email

In Loops, create a new transactional email, which will be sent to your users when they attempt to log in.

Here is where you define your email's subject and sending details like From address and Reply to address. (Click the `>` button to reveal all the sending options.)

Then you can create your email in the editor. We recommend creating a stylish but basic email for magic links, to help with deliverability. Use the [style panel](/creating-emails/styles#style-panel) to customize the design.

To add the Auth.js magic link in your email, add a [data variable](/transactional#add-data-variables) named `url`. When the email is sent, each user's magic link will be inserted wherever you add the variable.

You can add data variables as URLs to text, buttons and images. In this example, we're adding the `url` data variable into the button's link field.

<Warning>
  Make sure that your variable is named `url`, which is the variable name
  Auth.js uses when sending authentication emails.
</Warning>

<img src="https://mintcdn.com/loops/sV62RmpVPftRQH5h/images/authjs-magic-link.png?fit=max&auto=format&n=sV62RmpVPftRQH5h&q=85&s=4b19466d5b17ad35ae3131beb597f643" alt="Magic link button" data-og-width="2280" width="2280" data-og-height="1518" height="1518" data-path="images/authjs-magic-link.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/sV62RmpVPftRQH5h/images/authjs-magic-link.png?w=280&fit=max&auto=format&n=sV62RmpVPftRQH5h&q=85&s=60728b41f8c449d259518edd3149d116 280w, https://mintcdn.com/loops/sV62RmpVPftRQH5h/images/authjs-magic-link.png?w=560&fit=max&auto=format&n=sV62RmpVPftRQH5h&q=85&s=e183825ef7239a57972a6688b46edbc6 560w, https://mintcdn.com/loops/sV62RmpVPftRQH5h/images/authjs-magic-link.png?w=840&fit=max&auto=format&n=sV62RmpVPftRQH5h&q=85&s=01f8f5ce5f7801b1c050a201ae58bd2d 840w, https://mintcdn.com/loops/sV62RmpVPftRQH5h/images/authjs-magic-link.png?w=1100&fit=max&auto=format&n=sV62RmpVPftRQH5h&q=85&s=2bd39cd6a93d265e2a60e1ad8110c8a7 1100w, https://mintcdn.com/loops/sV62RmpVPftRQH5h/images/authjs-magic-link.png?w=1650&fit=max&auto=format&n=sV62RmpVPftRQH5h&q=85&s=7cc5f6495cb9e7030a68d6ef0b93d812 1650w, https://mintcdn.com/loops/sV62RmpVPftRQH5h/images/authjs-magic-link.png?w=2500&fit=max&auto=format&n=sV62RmpVPftRQH5h&q=85&s=d31cfa44baa3b8e13f4c2e84e99c25ec 2500w" />

When you're done make sure to Save and Publish your email. Unpublished emails will not be sent.

## Set up Loops in your Auth.js Project

<Steps>
  <Step title="Environment variables">
    To use the Loops provider in Auth.js, you'll need to add two environment variables to your project.

    The first is an API key. You can generate or copy one from [Settings -> API](https://app.loops.so/settings?page=api).

    The second is the ID of your transactional email. Go to the email in Loops and click on to the **Publish** page. Here you will find the **Transactional ID**.

        <img src="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/next.png?fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=553cf454d657a3049b9566e2851d1b0b" alt="Publish page with details" data-og-width="2280" width="2280" data-og-height="1682" height="1682" data-path="images/next.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/next.png?w=280&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=60b1e92d098c794c93b8cfb01310586c 280w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/next.png?w=560&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=c8f8c7d1c2918340532861bb8bd52c4c 560w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/next.png?w=840&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=e9569fd50c07b058708c7447fcf4cacf 840w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/next.png?w=1100&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=695b04041f9dfe709a25a3ad36345426 1100w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/next.png?w=1650&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=ea4ba40f8634d64c2905b0cc375c0c43 1650w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/next.png?w=2500&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=2083f0ff2fc32596387a81dcf6e07f17 2500w" />

    Add both values to your environment, for example in an `.env` file:

    ```
    AUTH_LOOPS_API_KEY=<API_KEY>
    AUTH_LOOPS_TRANSACTIONAL_ID=<TRANSACTIONAL_ID>
    ```
  </Step>

  <Step title="Use the Loops provider">
    The final step is to configure your project to send emails with the built-in Loops provider.

    ```javascript auth.js theme={"dark"}
    import NextAuth from "next-auth"
    import Loops from "next-auth/providers/loops"

    export const { handlers, auth, signIn, signOut } = NextAuth({
      adapter: ..., // database adapter of your choosing
      providers: [
        Loops({
          apiKey: process.env.AUTH_LOOPS_API_KEY,
          transactionalId: process.env.AUTH_LOOPS_TRANSACTIONAL_ID,
        }),
      ],
    })
    ```
  </Step>
</Steps>

That's it!

Don't forget, your email details (subject, from address etc) and content can all be managed from Loops.

You also get access to [transactional email logs](/transactional#metrics) giving you an eye on your sending history.
