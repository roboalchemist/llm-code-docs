# Source: https://resend.com/docs/send-with-railway.md

> ## Documentation Index
> Fetch the complete documentation index at: https://resend.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Send emails with Railway

> Learn how to send your first email using Railway and the Resend Node.js SDK.

[Railway](https://railway.com/?referralCode=resend) enables you to focus on building product instead of managing infrastructure, automatically scaling to support your needs as you grow.

## Prerequisites

To get the most out of this guide, you'll need to:

* [Create an API key](https://resend.com/api-keys)
* [Verify your domain](https://resend.com/domains)

## 1. Install

We've created a [Resend template](https://railway.com/deploy/resend?referralCode=resend\&utm_medium=integration\&utm_source=template\&utm_campaign=generic) using the Resend Node.js SDK as an introduction to using Resend on Railway.

To get started, you deploy the template to Railway.

[![Deploy on Railway](https://railway.com/button.svg)](https://railway.com/deploy/resend?referralCode=resend\&utm_medium=integration\&utm_source=template\&utm_campaign=generic)

<img alt="Deploy button highlighted on Railway" src="https://mintcdn.com/resend/UGYfPeFBYurSSqVy/images/send-with-railway.png?fit=max&auto=format&n=UGYfPeFBYurSSqVy&q=85&s=a4b37d9be58e4df72a9eec8e89352e1c" data-og-width="1500" width="1500" data-og-height="937" height="937" data-path="images/send-with-railway.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/UGYfPeFBYurSSqVy/images/send-with-railway.png?w=280&fit=max&auto=format&n=UGYfPeFBYurSSqVy&q=85&s=bf271760ce40cd8079322427a39d77f1 280w, https://mintcdn.com/resend/UGYfPeFBYurSSqVy/images/send-with-railway.png?w=560&fit=max&auto=format&n=UGYfPeFBYurSSqVy&q=85&s=f7888d3ea6f8122a023f08663016c113 560w, https://mintcdn.com/resend/UGYfPeFBYurSSqVy/images/send-with-railway.png?w=840&fit=max&auto=format&n=UGYfPeFBYurSSqVy&q=85&s=1a7363728a7710783f182ba092442c63 840w, https://mintcdn.com/resend/UGYfPeFBYurSSqVy/images/send-with-railway.png?w=1100&fit=max&auto=format&n=UGYfPeFBYurSSqVy&q=85&s=e03bb8355ef18cec8cdc16bf5fd68bf8 1100w, https://mintcdn.com/resend/UGYfPeFBYurSSqVy/images/send-with-railway.png?w=1650&fit=max&auto=format&n=UGYfPeFBYurSSqVy&q=85&s=19f0d8afd95b1cc917a8acb7f803de19 1650w, https://mintcdn.com/resend/UGYfPeFBYurSSqVy/images/send-with-railway.png?w=2500&fit=max&auto=format&n=UGYfPeFBYurSSqVy&q=85&s=83ccd4dc9546a07bedd86b3fdfc2847d 2500w" />

## 2. Add your API key

[Add an API key](https://resend.com/api-keys) from Resend and click **Deploy**.

<img alt="Template modal with API key field highlighted" src="https://mintcdn.com/resend/UGYfPeFBYurSSqVy/images/send-with-railway-1.png?fit=max&auto=format&n=UGYfPeFBYurSSqVy&q=85&s=0efcfbf778a0193a8c9aa353a07635b6" data-og-width="1500" width="1500" data-og-height="897" height="897" data-path="images/send-with-railway-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/UGYfPeFBYurSSqVy/images/send-with-railway-1.png?w=280&fit=max&auto=format&n=UGYfPeFBYurSSqVy&q=85&s=b8b01d2ee24d3605784c5f2958a07bf6 280w, https://mintcdn.com/resend/UGYfPeFBYurSSqVy/images/send-with-railway-1.png?w=560&fit=max&auto=format&n=UGYfPeFBYurSSqVy&q=85&s=eacb93ee1c7a3035ab3bef8ddaab083c 560w, https://mintcdn.com/resend/UGYfPeFBYurSSqVy/images/send-with-railway-1.png?w=840&fit=max&auto=format&n=UGYfPeFBYurSSqVy&q=85&s=953c1f5c79c803e1dfe488ed21088167 840w, https://mintcdn.com/resend/UGYfPeFBYurSSqVy/images/send-with-railway-1.png?w=1100&fit=max&auto=format&n=UGYfPeFBYurSSqVy&q=85&s=4dc4a00683fe0469c6d7137aaafff1ed 1100w, https://mintcdn.com/resend/UGYfPeFBYurSSqVy/images/send-with-railway-1.png?w=1650&fit=max&auto=format&n=UGYfPeFBYurSSqVy&q=85&s=9c6d30b53278651cf05de5444adf69f0 1650w, https://mintcdn.com/resend/UGYfPeFBYurSSqVy/images/send-with-railway-1.png?w=2500&fit=max&auto=format&n=UGYfPeFBYurSSqVy&q=85&s=edd9d52789be4f1bdfd0c49629db92b4 2500w" />

## 3. Send your first email

Once your deployment finishes, click the deploy URL to open the app and send your first email.

<img alt="Deployment link highlighted" src="https://mintcdn.com/resend/UGYfPeFBYurSSqVy/images/send-with-railway-2.png?fit=max&auto=format&n=UGYfPeFBYurSSqVy&q=85&s=c4a9f0838a4efb406d349c4e815c1c80" data-og-width="3360" width="3360" data-og-height="2010" height="2010" data-path="images/send-with-railway-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/UGYfPeFBYurSSqVy/images/send-with-railway-2.png?w=280&fit=max&auto=format&n=UGYfPeFBYurSSqVy&q=85&s=adaf5b30745d7ded34847652613f3a40 280w, https://mintcdn.com/resend/UGYfPeFBYurSSqVy/images/send-with-railway-2.png?w=560&fit=max&auto=format&n=UGYfPeFBYurSSqVy&q=85&s=fd1f32f9e6076a58af9d23f8c3e4bd6b 560w, https://mintcdn.com/resend/UGYfPeFBYurSSqVy/images/send-with-railway-2.png?w=840&fit=max&auto=format&n=UGYfPeFBYurSSqVy&q=85&s=c9d3428c7b95ca3cdba47e96c04a6f34 840w, https://mintcdn.com/resend/UGYfPeFBYurSSqVy/images/send-with-railway-2.png?w=1100&fit=max&auto=format&n=UGYfPeFBYurSSqVy&q=85&s=f9f08fcd1ec4d3d11d9cfd31f491265d 1100w, https://mintcdn.com/resend/UGYfPeFBYurSSqVy/images/send-with-railway-2.png?w=1650&fit=max&auto=format&n=UGYfPeFBYurSSqVy&q=85&s=560865688642ba263c03d209ba73e86b 1650w, https://mintcdn.com/resend/UGYfPeFBYurSSqVy/images/send-with-railway-2.png?w=2500&fit=max&auto=format&n=UGYfPeFBYurSSqVy&q=85&s=ee4de56e61dc8b2b1e1321c7350f8eab 2500w" />

While this example uses the [Resend Node.js SDK](https://www.npmjs.com/package/@resend/node), you can add Resend using [any of our Official SDKs](https://resend.com/docs/sdks) that Railway supports.

<Info>
  Keep in mind that as a basic project, this template sends an email with your
  account each time someone visits your deployment URL, so share the link with
  discretion.
</Info>

You can also [set up the project locally](https://docs.railway.com/develop/cli) and make changes to the projectusing the Railway CLI.

## 4. Try it yourself

<Card title="Railway Template" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-node-railway-starter">
  See the full source code.
</Card>
