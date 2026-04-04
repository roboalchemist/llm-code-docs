# Source: https://developers.cash.app/cash-app-afterpay/guides/afterpay-messaging/migration.mdx

***

## stoplight-id: 8zu51ufbv5euc

# Migration

We support two messaging products:

* On-Site Messaging is our latest messaging product
* JavaScript Library V1 is our legacy messaging product

We recommend that you update to the On-Site Messaging product. Follow this guide to learn how.

## Migrate from the JavaScript Library V1 to On-Site Messaging

You have two migration choices:

* Self-migration: Your IT team does the migration

* Assisted migration: Afterpay helps you do some parts of the migration

## Self-migration

Depending on how customized your implementation is, follow one of these two paths.

### Light customizations

If you've made minor customizations to the Afterpay JavaScript attributes, do the following:

1. Find the `<afterpay-placement>` element you currently have. Copy it and paste it somewhere you can refer back to. This gives you a list of configuration changes you've made.

   <Note>
     For example, in:
     `<afterpay-placement data-is-eligible="true" data-locale="en_US" data-currency="USD" data-amount="59" data-show-upper-limit="false" data-size="xs" data-logo-type="lockup" data-lockup-theme="black"></afterpay-placement>`

     The configuration changes could include:

     * `data-show-upper-limit="false"`
     * `data-size="xs"`
     * `data-logo-type="lockup"`
     * `data-lockup-theme="black"`
   </Note>

2. Delete the old script: `<script src="https://js.afterpay.com/afterpay-1.x.js" async></script>`

3. Find and remove all instances of the elements below from the code:

   * `afterpay-placement`

   * `Afterpay.createPlacements`

   * `new Afterpay.AfterpayPlacement()`

   * `Afterpay.launchModal`

   * `afterpay-price-table`

4. Follow the instructions to [add On-Site Messaging to your website](/cash-app-afterpay/guides/afterpay-messaging/implementation#add-on-site-messaging-to-your-storefront).

5. Make attribute changes if needed. Click **Save all changes**.

### Major customizations

If you've made larger customizations to the custom Cascading Style Sheet (CSS) and the JavaScript, do the following:

1. Log in to the Business Hub to install On-Site Messaging.

2. Follow the steps in the [Implementation guide](/cash-app-afterpay/guides/afterpay-messaging/implementation).

3. Go to the Implementation Guide page and find the `<data-mpid>` and `<data-placement-id>` for each placement (both Product and Cart).

4. Go to your codebase, add your MPID to each placement as a `data-mpid` attribute.

5. Add your placement IDs to each placement as `data-placement-id` attributes.

6. Return to the messaging tool and make attribute changes if needed. Click **Save all changes**.

### Migrate from the dynamic widget to On-Site Messaging

The widget isn't actively supported by Afterpay; we strongly recommend migrating to On-Site Messaging. If you already have an agreement to use the widget, you can wait until this agreement expires.

To remove the widget:

1. Find the previous code and note the inline customisations that have been made.

2. Remove script from head section:

   `<script src="https://portal.afterpay.com/afterpay.js" async onload="createMessaging()"></script>`

3. Remove the previous code:

   `<div id="afterpay-messaging-widget"></div>`

4. Follow the On-Site Messaging implementation instructions.
