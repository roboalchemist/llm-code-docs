# Source: https://loops.so/docs/contacts/double-opt-in.md

> ## Documentation Index
> Fetch the complete documentation index at: https://loops.so/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Double opt-in

> Require and manage subscription confirmations for new contacts.

Double opt-in requires new contacts to confirm their subscription before you can send them marketing emails. This improves list quality and deliverability.

## Good to know

This feature only applies to [marketing sends](/types-of-emails) (campaigns and loops). Transactional emails are never restricted by double opt-in.

Double opt-in is currently only enabled on [Form endpoints](/forms/simple-form). API endpoints like [Create contact](/api-reference/create-contact) and [Update contact](/api-reference/update-contact) are not yet gated. Coverage will expand to these endpoints soon.

## The double opt-in flow

When double opt-in is enabled:

1. Contact submits a form and receives a confirmation email with a link to a branded confirmation page.
2. The confirmation page displays **Confirm subscription** and **No thanks** buttons.
3. Contacts appear in your audience as "Pending" in the **Double opt-in** column.
4. Contact confirms or rejects the subscription:
   1. If they click **Confirm subscription**, they're subscribed to your audience and any selected mailing lists. This also triggers any applicable loops.
   2. If they click **No thanks**, they remain in your audience but are marked as [unsubscribed](/contacts/properties#subscribed).\
      They can request a new confirmation email from the same page if they clicked **No thanks** by accident.
      <Tip>
        Unsubscribed contacts do not count towards [your plan's
        limits](https://loops.so/pricing).
      </Tip>
   3. If they don't respond, the contact continues to appear as "Pending". Pending contacts are not automatically removed. You can manually delete them if needed.

<img src="https://mintcdn.com/loops/GrzDLwrUithgQO_4/images/opt-in-confirmation.png?fit=max&auto=format&n=GrzDLwrUithgQO_4&q=85&s=54b94d444db42035aa13af3f5dbffc26" alt="Double opt-in confirmation page" data-og-width="2280" width="2280" data-og-height="1673" height="1673" data-path="images/opt-in-confirmation.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/GrzDLwrUithgQO_4/images/opt-in-confirmation.png?w=280&fit=max&auto=format&n=GrzDLwrUithgQO_4&q=85&s=d5b3f634405dc35cf19d6c47bc017883 280w, https://mintcdn.com/loops/GrzDLwrUithgQO_4/images/opt-in-confirmation.png?w=560&fit=max&auto=format&n=GrzDLwrUithgQO_4&q=85&s=c278937923511171c99d3083a50e6eb3 560w, https://mintcdn.com/loops/GrzDLwrUithgQO_4/images/opt-in-confirmation.png?w=840&fit=max&auto=format&n=GrzDLwrUithgQO_4&q=85&s=40c39b411993357bf604d4c85e1957bc 840w, https://mintcdn.com/loops/GrzDLwrUithgQO_4/images/opt-in-confirmation.png?w=1100&fit=max&auto=format&n=GrzDLwrUithgQO_4&q=85&s=72bb954eb750cf66bde3d96653a1af18 1100w, https://mintcdn.com/loops/GrzDLwrUithgQO_4/images/opt-in-confirmation.png?w=1650&fit=max&auto=format&n=GrzDLwrUithgQO_4&q=85&s=55bde662ab49e96796e20f85868fa5f2 1650w, https://mintcdn.com/loops/GrzDLwrUithgQO_4/images/opt-in-confirmation.png?w=2500&fit=max&auto=format&n=GrzDLwrUithgQO_4&q=85&s=c4e7eca538c4803064a0ac6cff24d49b 2500w" />

## Enable double opt-in

To enable double opt-in, go to [Settings -> Sending](https://app.loops.so/settings?page=sending) and scroll to the **Double opt-in** section. Turn the **Double opt-in** setting on.

This creates a special transactional email that is used to confirm the subscription, which you can customize in the [Transactional](https://app.loops.so/transactional) page in the Loops dashboard.

To disable double opt-in, turn the **Double opt-in** setting off.

<img src="https://mintcdn.com/loops/GrzDLwrUithgQO_4/images/opt-in-settings.png?fit=max&auto=format&n=GrzDLwrUithgQO_4&q=85&s=915d8296c59158f05e874177e205f9cc" alt="Double opt-in settings" data-og-width="2280" width="2280" data-og-height="1314" height="1314" data-path="images/opt-in-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/GrzDLwrUithgQO_4/images/opt-in-settings.png?w=280&fit=max&auto=format&n=GrzDLwrUithgQO_4&q=85&s=005f4479af826dd11e86417dbad5eb17 280w, https://mintcdn.com/loops/GrzDLwrUithgQO_4/images/opt-in-settings.png?w=560&fit=max&auto=format&n=GrzDLwrUithgQO_4&q=85&s=ba80895ab517c802d5e2dfa934c0999c 560w, https://mintcdn.com/loops/GrzDLwrUithgQO_4/images/opt-in-settings.png?w=840&fit=max&auto=format&n=GrzDLwrUithgQO_4&q=85&s=95c2d704145f1e60b3c6e0e0bcee2341 840w, https://mintcdn.com/loops/GrzDLwrUithgQO_4/images/opt-in-settings.png?w=1100&fit=max&auto=format&n=GrzDLwrUithgQO_4&q=85&s=1a36d125aca767d0b189f5c8d02b0721 1100w, https://mintcdn.com/loops/GrzDLwrUithgQO_4/images/opt-in-settings.png?w=1650&fit=max&auto=format&n=GrzDLwrUithgQO_4&q=85&s=ddfbeb0316e7f81e12ef6849db1975e2 1650w, https://mintcdn.com/loops/GrzDLwrUithgQO_4/images/opt-in-settings.png?w=2500&fit=max&auto=format&n=GrzDLwrUithgQO_4&q=85&s=6dbef22174220b1e160ad1e9d30fd3e3 2500w" />

## Customize the confirmation email

The opt-in email is a special [transactional email](/transactional) that is created automatically when you first turn on double opt-in in your account.

You are free to customize the email as you like but it has specific requirements:

* Keep the email short, clearly branded, and focused on the confirmation action.
* Include the required data variable `optInUrl` (added automatically when the email is created).
* Other data variables are not allowed.

Click **Edit Draft** to [edit the email](/transactional#editing-the-email). Make sure to click **Publish** after editing to make your changes live.

<CardGroup>
  <Card title="Transactional email guide" icon="code" href="/transactional">
    Learn how to create and send transactional email with Loops.
  </Card>
</CardGroup>

## Manually re-send a confirmation email

You can re-send a confirmation email to a contact from their profile page. This is only available for contacts who are currently "Pending".

On a contact's profile page, click the `•••` menu icon and choose **Request opt-in**.

<img src="https://mintcdn.com/loops/GrzDLwrUithgQO_4/images/request-opt-in.png?fit=max&auto=format&n=GrzDLwrUithgQO_4&q=85&s=156f52aa6ddaac9df182b2b55748570a" alt="Request opt-in" data-og-width="2280" width="2280" data-og-height="1248" height="1248" data-path="images/request-opt-in.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/GrzDLwrUithgQO_4/images/request-opt-in.png?w=280&fit=max&auto=format&n=GrzDLwrUithgQO_4&q=85&s=58884914d049f713307e5bda1b3117a2 280w, https://mintcdn.com/loops/GrzDLwrUithgQO_4/images/request-opt-in.png?w=560&fit=max&auto=format&n=GrzDLwrUithgQO_4&q=85&s=3cc3f60f2f559c9e58e2a435129cb015 560w, https://mintcdn.com/loops/GrzDLwrUithgQO_4/images/request-opt-in.png?w=840&fit=max&auto=format&n=GrzDLwrUithgQO_4&q=85&s=af7841901a49fb35b627f8dafdbc7c1f 840w, https://mintcdn.com/loops/GrzDLwrUithgQO_4/images/request-opt-in.png?w=1100&fit=max&auto=format&n=GrzDLwrUithgQO_4&q=85&s=c6e884344895ae916be20dd75f288aaf 1100w, https://mintcdn.com/loops/GrzDLwrUithgQO_4/images/request-opt-in.png?w=1650&fit=max&auto=format&n=GrzDLwrUithgQO_4&q=85&s=67040fc8a2017e4dcf735bcd55a18313 1650w, https://mintcdn.com/loops/GrzDLwrUithgQO_4/images/request-opt-in.png?w=2500&fit=max&auto=format&n=GrzDLwrUithgQO_4&q=85&s=7fc2c0d2f09cdfc42284838a819706a8 2500w" />

## Webhooks and the API

When double opt-in is enabled, contact webhooks don't fire until the contact is confirmed. Specifically:

* The [`contact.created` event](/webhooks#event-types) will only be sent for contacts created via forms once the contact has confirmed their subscription.
* Other contact-related webhooks (such as `contact.mailingList.subscribed`) will also only fire after confirmation.
* Contacts remain in a "Pending" state in your audience until they confirm, and no webhook events are triggered during this pending state.

You can read a contact's opt-in status from the API by looking at the `optInStatus` field in the [Find contact](/api-reference/find-contact) endpoint.
