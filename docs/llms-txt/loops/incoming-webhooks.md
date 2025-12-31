# Source: https://loops.so/docs/integrations/incoming-webhooks.md

# Incoming webhooks

> Send data to Loops from supported platforms using webhooks.

<Info>
  Incoming webhooks allow you to:

  * Create and update contacts
  * Send events to trigger loops
</Info>

This feature lets external platforms send webhook events directly to Loops, making it straightforward to create or update contacts in Loops automatically when changes happen in other platforms.

You can also trigger events when webhooks arrive in Loops so you can send automated email after something happens in your other accounts.

## How it works

First, you create webhook endpoints in your Loops account. These allow other platforms to send data automatically and directly to Loops.

You then create webhooks in the external platforms, which send event data to your Loops endpoint URLs.

Note: we only process webhook events listed below for each provider (and which contain an email address).

We return helpful messages in responses if there is an issue processing a webhook event. Check the webhook logs in your external platforms.

<img src="https://mintcdn.com/loops/zNnVRjXA37FUc8Z0/images/webhook-event-configuration.png?fit=max&auto=format&n=zNnVRjXA37FUc8Z0&q=85&s=3429f5d0095e3c10220f48c1773d5c03" alt="Incoming webhook configuration" data-og-width="2280" width="2280" data-og-height="1541" height="1541" data-path="images/webhook-event-configuration.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/zNnVRjXA37FUc8Z0/images/webhook-event-configuration.png?w=280&fit=max&auto=format&n=zNnVRjXA37FUc8Z0&q=85&s=78bda7d204a6a232bc91f8afe8054267 280w, https://mintcdn.com/loops/zNnVRjXA37FUc8Z0/images/webhook-event-configuration.png?w=560&fit=max&auto=format&n=zNnVRjXA37FUc8Z0&q=85&s=6751d2e8fd127bcf70c633524960e819 560w, https://mintcdn.com/loops/zNnVRjXA37FUc8Z0/images/webhook-event-configuration.png?w=840&fit=max&auto=format&n=zNnVRjXA37FUc8Z0&q=85&s=2aca78ca1261640f30ff6a41323a9e35 840w, https://mintcdn.com/loops/zNnVRjXA37FUc8Z0/images/webhook-event-configuration.png?w=1100&fit=max&auto=format&n=zNnVRjXA37FUc8Z0&q=85&s=8da7e40f142f1196eff6ec26babaf38a 1100w, https://mintcdn.com/loops/zNnVRjXA37FUc8Z0/images/webhook-event-configuration.png?w=1650&fit=max&auto=format&n=zNnVRjXA37FUc8Z0&q=85&s=e86a9d68ff7d05f56fc6398fdd33a04c 1650w, https://mintcdn.com/loops/zNnVRjXA37FUc8Z0/images/webhook-event-configuration.png?w=2500&fit=max&auto=format&n=zNnVRjXA37FUc8Z0&q=85&s=29b055af202615627f7da2ae9c4f0fd3 2500w" />

### Syncing contacts

The primary use case for incoming webhooks is to create and update contacts in your Loops audience. When data arrives in Loops, we grab the email address to create and update contacts in your Loops audience. To this end, we only support incoming events that contain an email address.

You can assign a user group value to each new contact, which allows you to create segments from webhook-created contacts.

Any new contact created via a webhook will have a source like "Stripe webhook" so you know where it originated from.

For events that reference record deletion, like Stripe's `customer.deleted` event, you can choose to unsubscribe or delete contacts in Loops.

### Subscribing to mailing lists

You can subscribe contacts to [mailing lists](/contacts/mailing-lists) when they are created or updated via a webhook.

### Sending emails

Incoming webhooks can also trigger loops if you specify an event in the **Trigger an event** section. This can be useful to automatically send emails when something has happened in the external platform, for example a successful payment in Stripe or a new sign up in Clerk.

## Create webhook endpoints in Loops

To start sending webhook events to Loops, go to your chosen [integration's settings page](https://app.loops.so/settings) in Loops.

A webhook endpoint will be created for you. Copy the endpoint URL and paste it into your external platform.

<img src="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/create-endpoint.png?fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=be75ea5d3e49aaa75248d6d157d5780b" alt="Endpoint form" data-og-width="2280" width="2280" data-og-height="1556" height="1556" data-path="images/create-endpoint.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/create-endpoint.png?w=280&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=9e0e8289abc76ba6a6eb278ed097a779 280w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/create-endpoint.png?w=560&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=1f45e6a6c27d3847f4f37cbd47c3aab6 560w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/create-endpoint.png?w=840&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=b98f9ba7cac487f8e38da5f1fbb328b3 840w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/create-endpoint.png?w=1100&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=2e969b5ad5d478635aa17783cc3b363b 1100w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/create-endpoint.png?w=1650&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=2ec8f95dee66d9ddf4ca52460700d87c 1650w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/create-endpoint.png?w=2500&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=31ff8ef99563162302b0f8a62985cc2d 2500w" />

You may need to copy-paste signing secrets between the platform and Loops for extra security (we will prompt you when this is necessary and give you the steps to do it).

In the endpoint form, you can select the events you want Loops to process, assign a user group, and send a Loops event (which can [trigger email sending in loops](/loop-builder#triggers)).

## Supported platforms

For more information about the data we can sync from each platform, plus more detailed installation instructions, visit the integration pages below.

<CardGroup>
  <Card
    title="Clerk"
    icon={
    <svg viewBox="0 0 18 18" fill="none" aria-hidden="true"><ellipse cx="8.99999" cy="9" rx="2.81249" ry="2.8125" fill="#FF4A00"></ellipse><path fill="#FF4A00" d="M14.0674 15.6591C14.3067 15.8984 14.2827 16.2945 14.0015 16.4829C12.571 17.4411 10.8504 17.9999 8.9993 17.9999C7.14818 17.9999 5.42758 17.4411 3.99704 16.4829C3.71589 16.2945 3.69186 15.8984 3.93115 15.6591L5.98648 13.6037C6.17225 13.418 6.46042 13.3886 6.69424 13.5084C7.3856 13.8626 8.16911 14.0624 8.9993 14.0624C9.82948 14.0624 10.613 13.8626 11.3044 13.5084C11.5382 13.3886 11.8263 13.418 12.0121 13.6037L14.0674 15.6591Z"></path><path fill="#FF4A00" d="M14.0022 1.51706C14.2834 1.70539 14.3074 2.10155 14.0681 2.34084L12.0128 4.39619C11.827 4.58195 11.5388 4.61129 11.305 4.49151C10.6136 4.13733 9.83014 3.9375 8.99996 3.9375C6.20403 3.9375 3.93748 6.20406 3.93748 9C3.93748 9.83018 4.13731 10.6137 4.49149 11.3051C4.61127 11.5389 4.58193 11.827 4.39617 12.0128L2.34083 14.0682C2.10154 14.3074 1.70538 14.2834 1.51705 14.0023C0.558857 12.5717 0 10.8511 0 9C0 4.02944 4.02942 0 8.99996 0C10.8511 0 12.5717 0.55886 14.0022 1.51706Z" fillOpacity="0.5"></path></svg>
  }
    href="/integrations/clerk"
  />

  <Card title="Stripe" icon="stripe-s" href="/integrations/stripe" />

  <Card
    title="Supabase"
    icon={
    <svg
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      fill="none"
      viewBox="0 0 109 113"
    >
      <path
        fill="url(#a)"
        d="M63.708 110.284c-2.86 3.601-8.658 1.628-8.727-2.97l-1.007-67.251h45.22c8.19 0 12.758 9.46 7.665 15.874l-43.151 54.347Z"
      />
      <path
        fill="url(#b)"
        fillOpacity=".2"
        d="M63.708 110.284c-2.86 3.601-8.658 1.628-8.727-2.97l-1.007-67.251h45.22c8.19 0 12.758 9.46 7.665 15.874l-43.151 54.347Z"
      />
      <path
        fill="#ffbca6"
        d="M45.317 2.071c2.86-3.601 8.657-1.628 8.726 2.97l.442 67.251H9.83c-8.19 0-12.759-9.46-7.665-15.875L45.317 2.072Z"
      />
      <defs>
        <linearGradient
          id="a"
          x1="53.974"
          x2="94.163"
          y1="54.974"
          y2="71.829"
          gradientUnits="userSpaceOnUse"
        >
          <stop stopColor="#FF4A00" />
          <stop offset="1" stopColor="#ffbca6" />
        </linearGradient>
        <linearGradient
          id="b"
          x1="36.156"
          x2="54.484"
          y1="30.578"
          y2="65.081"
          gradientUnits="userSpaceOnUse"
        >
          <stop />
          <stop offset="1" stopOpacity="0" />
        </linearGradient>
      </defs>
    </svg>
  }
    href="/integrations/supabase"
  />
</CardGroup>
