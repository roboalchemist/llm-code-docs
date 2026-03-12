# Source: https://documentation.onesignal.com/docs/en/create-custom-unsubscribe-page.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a custom email unsubscribe page

> Learn how to replace OneSignal's default unsubscribe link with a branded, multi-language, and personalized email preferences page, while maintaining compliance and tracking.

## Overview

OneSignal provides a [default email-compliant unsubscribe experience](./unsubscribe-links-email-subscriptions) that injects a link into your email templates so users can unsubscribe with ease and their [subscription statuses](./subscriptions) are updated in real-time. If you want full control over branding, copy, and fields (such as category opt-outs), you can replace the default link with your own custom page and use the OneSignal API to unsubscribe or update user preferences.

This guide explains how to add your own custom unsubscribe page to emails (removing the default OneSignal link) and which of our APIs to use to unsubscribe the user's email Subscription.

If you want to add more functionality to your custom unsubscribe page (like opt out of specific email categories instead of all), this is detailed in our [Preference Center](./preference-center) tutorial.

***

## Remove OneSignal's default unsubscribe link

OneSignal automatically inserts a special link in the format `[unsubscribe_url]` to your email templates. This URL unsubscribes the user from all emails in OneSignal. See [Email Unsubscribe Links](./unsubscribe-links-email-subscriptions) for details.

To use your own page, **locate and remove the default link** in your template.

<Tabs>
  <Tab title="Drag-and-Drop Editor">
    In the drag-and-drop editor, the default link may appear nested like:

    <Frame caption="Drag-and-Drop editor unsubscribe link">
      <img src="https://mintcdn.com/onesignal/0qspEXXeJ8zJbkJ-/images/docs/82cc033-Default_Unsubscribe.png?fit=max&auto=format&n=0qspEXXeJ8zJbkJ-&q=85&s=3c507499bbc29854761df1136f8c0ff4" alt="Drag-and-Drop editor unsubscribe link" width="1598" height="1203" data-path="images/docs/82cc033-Default_Unsubscribe.png" />
    </Frame>
  </Tab>

  <Tab title="HTML Editor">
    ```html  theme={null}
    <a href="[unsubscribe_url]">Unsubscribe</a>
    ```
  </Tab>
</Tabs>

***

## Add your custom unsubscribe link

Now that you have removed our special link, you can replace it with your own URL.

Many times, these links require some additional data to be passed to your page. Use [Liquid variables](./message-personalization) to pass OneSignal data to your page.

Common parameters:

| Parameter                        | Description                           |
| -------------------------------- | ------------------------------------- |
| `subscription.email`             | Subscriber’s email address            |
| `subscription.external_id`       | User’s external ID                    |
| `app.id`                         | OneSignal App ID                      |
| `message.id`                     | ID of the email notification          |
| `subscription.language`          | Preferred language (for localization) |
| `subscription.unsubscribe_token` | Security token for API verification   |

**Example URL:**

```liquid  theme={null}
https://examplesite.com/unsubscribe?app_id={{app.id}}&notification_id={{message.id}}&email={{subscription.email}}&language={{subscription.language}}&token={{subscription.unsubscribe_token}}
```

```html HTML theme={null}
  <div style="text-align: center;">
    <a
      href="https://examplesite.com/unsubscribe?app_id={{app.id}}&notification_id={{message.id}}&email={{subscription.email}}&language={{subscription.language}}&token={{subscription.unsubscribe_token}}"
      data-disable-tracking="true"
      style="display: inline; text-decoration: none;"
    >
      Unsubscribe
    </a>
    <p style="display: inline;"> from our emails</p>
  </div>
```

<Frame caption="Add custom unsubscribe link">
  <img src="https://mintcdn.com/onesignal/6v_cVPknFpo5qSVB/images/docs/0c94ab0-HTML_unsubscribe_custom.png?fit=max&auto=format&n=6v_cVPknFpo5qSVB&q=85&s=e931f0e8649ea80d29194e0db2722942" alt="Add custom unsubscribe link" width="1606" height="1175" data-path="images/docs/0c94ab0-HTML_unsubscribe_custom.png" />
</Frame>

### Disable click tracking

Unsubscribe clicks are generally not used for engagement metrics. If you want to disable link tracking, you can add the `data-disable-tracking="true"` attribute to your link like this:

```html HTML theme={null}
  <a
    href="https://www.examplesite.com/unsubscribe?app_id={{app.id}}&notification_id={{message.id}}&email={{subscription.email}}&language={{subscription.language}}&token={{subscription.unsubscribe_token}}"
    data-disable-tracking="true"
  >
    Unsubscribe
  </a>
```

**Provider-specific attributes:**

| Provider  | Attribute                      |
| --------- | ------------------------------ |
| OneSignal | `data-disable-tracking="true"` |
| Mailgun   | `disable-tracking=true`        |
| SendGrid  | `clicktracking=off`            |
| Mandrill  | `mc:disable-tracking`          |

***

## Hosting your custom unsubscribe page

Deploy a web page that:

* Reads query parameters from the unsubscribe link.
* Displays user-friendly opt-out or preference options.
* Sends the unsubscribe or update request to OneSignal via API.

<Info> We provide a working [GitHub sample project](https://github.com/OneSignalDevelopers/custom-email-unsubscribe-page-sample) you can fork and deploy. </Info>

<Frame caption="Sample unsubscribe page UI">
  <img src="https://mintcdn.com/onesignal/jBdBk5XvQR5eKOks/images/docs/75a39d1-Github_page.png?fit=max&auto=format&n=jBdBk5XvQR5eKOks&q=85&s=4d1b004b41a3ad4bd3e7c4f76da7e9fc" alt="Sample unsubscribe page" width="1448" height="1438" data-path="images/docs/75a39d1-Github_page.png" />
</Frame>

***

## Calling the OneSignal API

Depending on your use case, you can use the following APIs to unsubscribe or update user preferences:

* [Update Subscription by Token](/reference/update-subscription-by-token)
* [Unsubscribe Email with Token](/reference/unsubscribe-with-token)
* [Update User](/reference/update-user)

<Tabs>
  <Tab title="Update Subscription by Token">
    This API is most commonly used when you have the user's email address and just want to subscribe or unsubscribe them from all emails.

    **Required query parameters:**

    * `app_id`
    * `token`

    **Authentication required**

    * Call this API from your server.
  </Tab>

  <Tab title="Unsubscribe Email with Token">
    Use this API if you want to track which specific email caused the unsubscribe. This uses the email message ID to track the unsubscribe. See [Unsubscribe Email with Token](/reference/unsubscribe-with-token) API for more details.

    **Required query parameters:**

    * `app_id`
    * `notification_id`
    * `token`

    **Optional parameters:**

    * `email`
    * `language`

    **Example JavaScript:**

    ```javascript JavaScript theme={null}
    const unsubscribeURL = (href) => {
      const unsubscribeURL = new URL(href)
      const appID = unsubscribeURL.searchParams.get("app_id")
      const notificationID = unsubscribeURL.searchParams.get("notification_id")
      const unsubscribeToken = unsubscribeURL.searchParams.get("token")
      const language = unsubscribeURL.searchParams.get("language")
      const email = unsubscribeURL.searchParams.get("email")
      return {
        unsubscribeURL: `https://api.onesignal.com/apps/${appID}/notifications/${notificationID}/unsubscribe?token=${unsubscribeToken}`,
        meta: { language, email },
      }
    }
    ```
  </Tab>

  <Tab title="Update User">
    Update the user's preferences using the [Update User](/reference/update-user) API.

    **Required query parameters:**

    * `app_id`
    * `alias_id` - The user's external ID is recommended.

    **Authentication required**

    * Call this API from your server.
  </Tab>
</Tabs>

***

<Check>
  You should now be equipped with everything you need to know about creating a custom unsubscribe page.
</Check>

***

Built with [Mintlify](https://mintlify.com).
