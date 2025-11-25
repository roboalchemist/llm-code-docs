# Source: https://resend.com/docs/knowledge-base/base44-integration.md

# Send emails with Base44 and Resend

> Learn how to add the Resend integration to your Base44 project.

[Base44](https://base44.com/) is a platform for building apps with AI. You can add Resend in a Base44 project by asking the chat to add email sending with Resend.

<Info>
  This integration requires backend functions, a feature available only on
  Builder tier and above. Learn more about [Base44
  pricing](https://base44.com/pricing).
</Info>

## 1. Add the Resend integration in Base44

**If starting a new app:**

1. Click **Integration** in the top nav.
2. Search for **Resend**, select it, and choose **Use This Integration**.

<img alt="Resend Integration page" src="https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/base44-integration.png?fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=f98f8dda5a22d0a0aa0aadc40c9324f3" data-og-width="1024" width="1024" data-og-height="475" height="475" data-path="images/base44-integration.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/base44-integration.png?w=280&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=7072436cdb22df727c491209aff6c628 280w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/base44-integration.png?w=560&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=d70832ba33dac909a6bdc75457ae1e1a 560w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/base44-integration.png?w=840&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=10b3566ba9fc7a0665fcd85c851070f1 840w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/base44-integration.png?w=1100&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=9e2f5b8962003810bbd1f850ad98049c 1100w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/base44-integration.png?w=1650&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=d135e408fbbd1b62d958d37812d24731 1650w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/base44-integration.png?w=2500&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=c5dc37bcc1838d2c444cc4cba1fdf9a3 2500w" />

**If adding Resend to an existing app:**

1. Enable backend functions.
2. Ask the chat: "Add the Resend email integration to my app. Prompt me to provide the API key and send a welcome email to new users."

<Note>
  See the [Base44
  documenation](https://docs.base44.com/Integrations/Resend-integration) for
  more information.
</Note>

## 2. Add your Resend API key

However you add Resend to your project, you'll need to add a Resend API key, which you can create in the [Resend Dashboard](https://resend.com/api-keys). Do not share your API key with others or expose it in the browser or other client-side code.

Copy the API key and paste it into the **RESEND\_API\_KEY** field in Base44.

<img src="https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/base44-integration-1.png?fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=e10a7a52b06dde106b7a2db585bb7b30" alt="Adding your Resend API key to Base44" data-og-width="1024" width="1024" data-og-height="476" height="476" data-path="images/base44-integration-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/base44-integration-1.png?w=280&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=91015dee5675e094d2c5863a42855bd3 280w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/base44-integration-1.png?w=560&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=b14a35c5976c953232577a85464112fc 560w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/base44-integration-1.png?w=840&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=e6ac3163ea0ad7d15d98d7b9ad6cf273 840w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/base44-integration-1.png?w=1100&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=f68c16fbcaa8a18b42151991775bbbb7 1100w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/base44-integration-1.png?w=1650&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=1e1f07d7c7269438f8e16946b8a15135 1650w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/base44-integration-1.png?w=2500&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=8ad66acfc04074bec5c6c4dfc39c4cb0 2500w" />

## 3. Add a custom domain to your Resend account

By default, you can only send emails to your own email address.

To send emails to other email addresses:

1. Add a [custom domain to your Resend account](https://resend.com/domains).
2. Add the custom domain to the `from` field in the `resend` function in the Base44 backend function (or ask the chat to update these fields).

Get more help adding a custom domain in [Resend's documentation](/dashboard/domains/introduction).
