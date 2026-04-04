# Source: https://polar.sh/docs/changelog/recent.md

> ## Documentation Index
> Fetch the complete documentation index at: https://polar.sh/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Product Updates

> Stay up to date with the latest changes and improvements to Polar.

<Update label="2025-10-17">
  ## Ability to update subscription to an updated price of the product

  Merchants can now [update existing subscriptions](https://polar.sh/docs/api-reference/subscriptions/update#subscriptionupdateproduct) from archived pricing schemes to current ones within the same product.

  * Enables migration from grandfathered pricing to current pricing schemes
  * Prorations calculated using active subscription prices
  * In the dashboard, a small badge **Upgrade pricing** will indicate that you can update to the same product, but with the new pricing scheme.

  <img class="rounded" src="https://mintcdn.com/polar/P14Bx1Nt4rA16sHk/assets/changelog/2025-10-17/update-subscription.png?fit=max&auto=format&n=P14Bx1Nt4rA16sHk&q=85&s=84b0f80f4c5d6c6ede3fb478d93febb9" data-og-width="1026" width="1026" data-og-height="1044" height="1044" data-path="assets/changelog/2025-10-17/update-subscription.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/polar/P14Bx1Nt4rA16sHk/assets/changelog/2025-10-17/update-subscription.png?w=280&fit=max&auto=format&n=P14Bx1Nt4rA16sHk&q=85&s=3883b6fb1705fb66a6bd711c1d465d29 280w, https://mintcdn.com/polar/P14Bx1Nt4rA16sHk/assets/changelog/2025-10-17/update-subscription.png?w=560&fit=max&auto=format&n=P14Bx1Nt4rA16sHk&q=85&s=7cba24c5d8795b7fb92361b32162075d 560w, https://mintcdn.com/polar/P14Bx1Nt4rA16sHk/assets/changelog/2025-10-17/update-subscription.png?w=840&fit=max&auto=format&n=P14Bx1Nt4rA16sHk&q=85&s=9771c2705febeda2b6bcbc5a48b9a36a 840w, https://mintcdn.com/polar/P14Bx1Nt4rA16sHk/assets/changelog/2025-10-17/update-subscription.png?w=1100&fit=max&auto=format&n=P14Bx1Nt4rA16sHk&q=85&s=775f2d95c6cb9a2c1312a8888f39d84c 1100w, https://mintcdn.com/polar/P14Bx1Nt4rA16sHk/assets/changelog/2025-10-17/update-subscription.png?w=1650&fit=max&auto=format&n=P14Bx1Nt4rA16sHk&q=85&s=8af4ce16db55fa74f8d65fa1ee55604d 1650w, https://mintcdn.com/polar/P14Bx1Nt4rA16sHk/assets/changelog/2025-10-17/update-subscription.png?w=2500&fit=max&auto=format&n=P14Bx1Nt4rA16sHk&q=85&s=7d06860644d6194437a0cf671a6af013 2500w" />

  ## New IP ranges

  From **October 27th, 2025**, [new IP ranges](https://polar.sh/docs/integrate/webhooks/delivery#ip-allowlist) will be added.

  ## Improved Subscription Cancellation Flow

  [Benefits](https://polar.sh/docs/features/benefits/introduction) attached to the subscription [are now automatically revoked](https://github.com/polarsource/polar/pull/7271) when the subscription is canceled.

  ## Ability to specify External ID

  [External ID can now be specified](https://github.com/polarsource/polar/pull/7275) during creation of a customer via the dashboard.

  <img class="border rounded" src="https://mintcdn.com/polar/P14Bx1Nt4rA16sHk/assets/changelog/2025-10-17/create-customer.png?fit=max&auto=format&n=P14Bx1Nt4rA16sHk&q=85&s=4f96d098affca55b7140c26196e16852" data-og-width="1034" width="1034" data-og-height="1030" height="1030" data-path="assets/changelog/2025-10-17/create-customer.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/polar/P14Bx1Nt4rA16sHk/assets/changelog/2025-10-17/create-customer.png?w=280&fit=max&auto=format&n=P14Bx1Nt4rA16sHk&q=85&s=c71ce04bc18bfe24a2076b8b3fa85fe7 280w, https://mintcdn.com/polar/P14Bx1Nt4rA16sHk/assets/changelog/2025-10-17/create-customer.png?w=560&fit=max&auto=format&n=P14Bx1Nt4rA16sHk&q=85&s=01efa2ee281c648d78f630578f5e0959 560w, https://mintcdn.com/polar/P14Bx1Nt4rA16sHk/assets/changelog/2025-10-17/create-customer.png?w=840&fit=max&auto=format&n=P14Bx1Nt4rA16sHk&q=85&s=d86240a390a690e1afa75a64de709274 840w, https://mintcdn.com/polar/P14Bx1Nt4rA16sHk/assets/changelog/2025-10-17/create-customer.png?w=1100&fit=max&auto=format&n=P14Bx1Nt4rA16sHk&q=85&s=0e2537c9c9912bcad0cbc7d3f1533656 1100w, https://mintcdn.com/polar/P14Bx1Nt4rA16sHk/assets/changelog/2025-10-17/create-customer.png?w=1650&fit=max&auto=format&n=P14Bx1Nt4rA16sHk&q=85&s=72db1acc1262b9d2092c80622b140131 1650w, https://mintcdn.com/polar/P14Bx1Nt4rA16sHk/assets/changelog/2025-10-17/create-customer.png?w=2500&fit=max&auto=format&n=P14Bx1Nt4rA16sHk&q=85&s=85fbba7f8319319a35a524599a780cac 2500w" />

  ## Ability to set Return URL for Checkouts and Customer Portal

  A Return URL can now be set while generating a [checkout session](https://polar.sh/docs/api-reference/checkouts/create-session#body-return-url-one-of-0) or a [customer portal session](https://polar.sh/docs/api-reference/customer-portal/sessions/create#body-one-of-0-return-url-one-of-0). This allows you to preserve the context for the end users who visit either if they wish to go back to the application.

  ## Ability to search Customers via their External ID

  The [List Customers API](https://polar.sh/docs/api-reference/customers/list) now accepts Customer's External ID [in the **query** parameter](https://polar.sh/docs/api-reference/customers/list#parameter-one-of-0).

  ## Ability to disable automatic customer emails

  Via the organization settings, you can now disable the emails we automatically send to customers on certain events. This gives you the ability to own the communications with the customers.

  <img class="border rounded" src="https://mintcdn.com/polar/P14Bx1Nt4rA16sHk/assets/changelog/2025-10-17/email-settings.png?fit=max&auto=format&n=P14Bx1Nt4rA16sHk&q=85&s=d64d9fd9fa62439c370ca5a39a62a47a" data-og-width="1660" width="1660" data-og-height="1522" height="1522" data-path="assets/changelog/2025-10-17/email-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/polar/P14Bx1Nt4rA16sHk/assets/changelog/2025-10-17/email-settings.png?w=280&fit=max&auto=format&n=P14Bx1Nt4rA16sHk&q=85&s=34406692e3c5ca7e20df5e2b462e9eae 280w, https://mintcdn.com/polar/P14Bx1Nt4rA16sHk/assets/changelog/2025-10-17/email-settings.png?w=560&fit=max&auto=format&n=P14Bx1Nt4rA16sHk&q=85&s=b8b8bb4d93d5091951214acb0bde2f3a 560w, https://mintcdn.com/polar/P14Bx1Nt4rA16sHk/assets/changelog/2025-10-17/email-settings.png?w=840&fit=max&auto=format&n=P14Bx1Nt4rA16sHk&q=85&s=39502fece8fb05eadc3a000f2a73ae61 840w, https://mintcdn.com/polar/P14Bx1Nt4rA16sHk/assets/changelog/2025-10-17/email-settings.png?w=1100&fit=max&auto=format&n=P14Bx1Nt4rA16sHk&q=85&s=103d7726ff4f901bf0d453e285555b5e 1100w, https://mintcdn.com/polar/P14Bx1Nt4rA16sHk/assets/changelog/2025-10-17/email-settings.png?w=1650&fit=max&auto=format&n=P14Bx1Nt4rA16sHk&q=85&s=7243575a6645fb7f11c95a80fc559c5e 1650w, https://mintcdn.com/polar/P14Bx1Nt4rA16sHk/assets/changelog/2025-10-17/email-settings.png?w=2500&fit=max&auto=format&n=P14Bx1Nt4rA16sHk&q=85&s=a81081e7c15f762563781a0b2556c9c2 2500w" />
</Update>

<Update label="2025-10-10">
  ## Launched In-Product Chat Support for Merchants

  <img src="https://mintcdn.com/polar/BSq8s4sf_HNjO0FK/assets/changelog/2025-10-10/launched-merchant-support.jpg?fit=max&auto=format&n=BSq8s4sf_HNjO0FK&q=85&s=8d424a428d041a57cd35ea2e3128071f" data-og-width="4291" width="4291" data-og-height="2632" height="2632" data-path="assets/changelog/2025-10-10/launched-merchant-support.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/polar/BSq8s4sf_HNjO0FK/assets/changelog/2025-10-10/launched-merchant-support.jpg?w=280&fit=max&auto=format&n=BSq8s4sf_HNjO0FK&q=85&s=c78c874694d6f94ad123370b637fd3c3 280w, https://mintcdn.com/polar/BSq8s4sf_HNjO0FK/assets/changelog/2025-10-10/launched-merchant-support.jpg?w=560&fit=max&auto=format&n=BSq8s4sf_HNjO0FK&q=85&s=b4fea1eb74ad72346c0096b6c7f21bac 560w, https://mintcdn.com/polar/BSq8s4sf_HNjO0FK/assets/changelog/2025-10-10/launched-merchant-support.jpg?w=840&fit=max&auto=format&n=BSq8s4sf_HNjO0FK&q=85&s=287b7597e37f6554ebc5a45894585b1e 840w, https://mintcdn.com/polar/BSq8s4sf_HNjO0FK/assets/changelog/2025-10-10/launched-merchant-support.jpg?w=1100&fit=max&auto=format&n=BSq8s4sf_HNjO0FK&q=85&s=65836546055f23909a482d19145813aa 1100w, https://mintcdn.com/polar/BSq8s4sf_HNjO0FK/assets/changelog/2025-10-10/launched-merchant-support.jpg?w=1650&fit=max&auto=format&n=BSq8s4sf_HNjO0FK&q=85&s=decd651383ea8e53a884211992c8c97a 1650w, https://mintcdn.com/polar/BSq8s4sf_HNjO0FK/assets/changelog/2025-10-10/launched-merchant-support.jpg?w=2500&fit=max&auto=format&n=BSq8s4sf_HNjO0FK&q=85&s=025c6d15aa49af9754f0d44dd61783e0 2500w" />

  We're excited to introduce a chat widget to the Polar dashboard, making it easier than ever for merchants to get help directly within the product.

  ## Improved Checkout Flow for Invalid Discount Code

  Previously, if you entered an invalid discount code during checkout, you couldn't continue even after removing the code. Now, clearing the discount input lets you proceed smoothly with the checkout process.

  ## Improved Customer Portal Rate Limits

  We've made several improvements to the Customer Portal to handle authentication rate limits more gracefully:

  * The portal now clearly shows 401 and 429 errors on the OTP (one-time password) page.
  * If you hit a 429 (too many requests), you'll be redirected to a clear `/too-many-requests` page.
</Update>

<Update label="2025-10-01">
  ## Launched Subscription Trials

  You can now offer [trial periods](/docs/features/trials) for new subscriptions! This highly requested feature allows you to let customers experience your product before their first payment is due. Trials can be configured in both the dashboard and API when creating or updating subscription products.

  ## Always display taxes line item in the checkout

  We've improved our checkout experience to always display taxes (vs lazy loading them on country selection), making charges more transparent for your customers regardless of whether taxes apply to their purchase.

  ## Do not calculate taxes on free or zero-amount orders

  Orders with a zero amount (such as promotional products) will no longer have taxes calculated, resulting in a clearer and more accurate order summary for your customers.

  ## Add confirmation modal for deleting discounts

  When deleting a discount, you'll now see a confirmation modal to help prevent accidental deletions and provide extra clarity on the impact of your actions.

  ## Fix infinite rendering loop with date picker

  Resolved a bug where selecting dates in the date picker could cause an infinite rendering loop, improving reliability for date-related forms.

  ## Require opt-in if you will be charged immediately

  Users must now explicitly confirm immediate charges or credits when switching subscription intervals, with the UI providing clearer, contextual explanations of invoicing outcomes.

  ## Check for `expires_at` when activating license keys

  License key activation now correctly checks the `expires_at` date, ensuring that only valid, non-expired license keys can be activated.

  ## Fix customer state for trialing subscriptions

  The [Customer State API](/docs/api-reference/customers/state) now properly handles customers with `trialing` subscriptions, so your integrations and dashboards always show an accurate subscription status.
</Update>

<Update label="2025-09-22">
  ## Improved preview of next invoice in Customer Portal

  We've enhanced the Customer Portal to provide a clearer and more accurate preview of your next invoice. The overview now updates automatically after subscription changes, and you can preview upcoming charges with all relevant taxes and discounts included.

  ## Cancellation metrics

  <img src="https://mintcdn.com/polar/KPDvrxuIefIR_xN_/assets/changelog/2025-09-22/cancellation-metrics-example.png?fit=max&auto=format&n=KPDvrxuIefIR_xN_&q=85&s=03281906e75a2f354a6636e54d226296" data-og-width="2490" width="2490" data-og-height="1186" height="1186" data-path="assets/changelog/2025-09-22/cancellation-metrics-example.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/polar/KPDvrxuIefIR_xN_/assets/changelog/2025-09-22/cancellation-metrics-example.png?w=280&fit=max&auto=format&n=KPDvrxuIefIR_xN_&q=85&s=6ae19ffbdaba4c7c0fe0d526ace61321 280w, https://mintcdn.com/polar/KPDvrxuIefIR_xN_/assets/changelog/2025-09-22/cancellation-metrics-example.png?w=560&fit=max&auto=format&n=KPDvrxuIefIR_xN_&q=85&s=42b4d9d3462985ebbe5caf58f19ecbe1 560w, https://mintcdn.com/polar/KPDvrxuIefIR_xN_/assets/changelog/2025-09-22/cancellation-metrics-example.png?w=840&fit=max&auto=format&n=KPDvrxuIefIR_xN_&q=85&s=fb4c1227797e8c4a7b87470f359b745e 840w, https://mintcdn.com/polar/KPDvrxuIefIR_xN_/assets/changelog/2025-09-22/cancellation-metrics-example.png?w=1100&fit=max&auto=format&n=KPDvrxuIefIR_xN_&q=85&s=8a7543565cb1ecfc64d1646cbc314f09 1100w, https://mintcdn.com/polar/KPDvrxuIefIR_xN_/assets/changelog/2025-09-22/cancellation-metrics-example.png?w=1650&fit=max&auto=format&n=KPDvrxuIefIR_xN_&q=85&s=364f0ea64944d70c3cf8d1dafb791c60 1650w, https://mintcdn.com/polar/KPDvrxuIefIR_xN_/assets/changelog/2025-09-22/cancellation-metrics-example.png?w=2500&fit=max&auto=format&n=KPDvrxuIefIR_xN_&q=85&s=db2266c6f032f8d0c503f06ea1de3ffa 2500w" />

  We've added detailed cancellation metrics, giving you clearer insights into subscription cancellations and their impact on your business performance.
</Update>

<Update label="2025-09-12">
  ## Webhooks payload now includes timestamp

  We've updated our webhooks server implementation to [include a timestamp in each payload](https://github.com/polarsource/polar/pull/6770), in line with the Standard Webhooks specification.

  This change ensures that every webhook payload contains precise event timing, making it easier to trace and debug webhook deliveries, and to meet integration requirements for external platforms.
</Update>

<Update label="2025-09-05">
  ## Meter management improvements

  We've made it easier to manage your meters with new UI functionality for archiving and unarchiving meters directly from the dashboard.

  You can now archive meters that are no longer needed, which helps keep your meter list organized. Archived meters can be unarchived if you need to use them again. Note that meters cannot be archived if they are still attached to active products or referenced by active benefits.

  ## Metrics accuracy improvements

  We've improved the accuracy of our metrics by excluding unpaid orders from all calculations. Previously, orders in pending status were included in metrics, which could lead to inflated numbers.

  Now, only successfully paid and refunded orders are included in metrics calculations, giving you a more accurate view of your actual business performance.

  ## Enhanced customer email branding

  We've improved the branding of emails sent to your customers by using organization-specific 'From' and 'Reply-to' addresses.

  Customer emails now appear to come from your organization (e.g., "YourOrg (via Polar)") with replies directed to your organization's email address, providing a more professional and branded experience for your customers.
</Update>

<Update label="2025-06-12">
  ## Update subscription discount

  We've added the ability to update the discount on a subscription. This allows you to add, remove, or change the discount applied to a subscription at any time.

  This feature is both available through the [API](/api-reference/subscriptions/update) and the dashboard.
</Update>

<Update label="2025-06-05">
  ## Payout Reverse Invoices

  We've added the ability to generate reverse invoices for payouts directly from the Payouts page. This feature allows you to easily create an invoice that details the sales made on your behalf, minus our fees.

  [Read more](/features/finance/payouts#reverse-invoices)
</Update>

<Update label="2025-05-22">
  ## Business Purchase Option on Checkout

  We've added a new "I'm purchasing as a business" checkbox to the Checkout flow. When selected, customers are required to provide their business billing name and complete billing address.
</Update>

<Update label="2025-05-19">
  ## Enhanced Attribution for Checkout Links

  We've added support for `reference_id` and UTM parameters (`utm_source`, `utm_medium`, `utm_campaign`, `utm_content`, `utm_term`) as query parameters for Checkout Links. These parameters are automatically stored in the Checkout metadata, allowing you to track the source of your traffic and conversions more effectively.

  [Read more](/features/checkout/links#store-attribution-and-reference-metadata)
</Update>

<Update label="2025-05-15">
  ## Checkouts and payments insights

  We've added a new **Checkouts** tab under the **Sales**, where you can review all the checkout sessions, successful or not. You can filter them by customer email, status, and product. You can also see the payment attempts for each checkout session, including the reason for any failed or declined payments.

  <img className="block dark:hidden" src="https://mintcdn.com/polar/fnujBPxaFvfkZfB0/assets/features/orders/checkout.light.png?fit=max&auto=format&n=fnujBPxaFvfkZfB0&q=85&s=4672cafc0b218d34a55c5cc006fdb153" data-og-width="3840" width="3840" data-og-height="2403" height="2403" data-path="assets/features/orders/checkout.light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/polar/fnujBPxaFvfkZfB0/assets/features/orders/checkout.light.png?w=280&fit=max&auto=format&n=fnujBPxaFvfkZfB0&q=85&s=bcf9dd8baf9fae7b84d2d046e9b4f811 280w, https://mintcdn.com/polar/fnujBPxaFvfkZfB0/assets/features/orders/checkout.light.png?w=560&fit=max&auto=format&n=fnujBPxaFvfkZfB0&q=85&s=1ac73955d12edfb9a605799d246d5237 560w, https://mintcdn.com/polar/fnujBPxaFvfkZfB0/assets/features/orders/checkout.light.png?w=840&fit=max&auto=format&n=fnujBPxaFvfkZfB0&q=85&s=4c931b7de4121f568d1ebefe90f42792 840w, https://mintcdn.com/polar/fnujBPxaFvfkZfB0/assets/features/orders/checkout.light.png?w=1100&fit=max&auto=format&n=fnujBPxaFvfkZfB0&q=85&s=87c8d57825f9c084f1b3664402629a23 1100w, https://mintcdn.com/polar/fnujBPxaFvfkZfB0/assets/features/orders/checkout.light.png?w=1650&fit=max&auto=format&n=fnujBPxaFvfkZfB0&q=85&s=21eb74aed158f9b11a2015bcfa763039 1650w, https://mintcdn.com/polar/fnujBPxaFvfkZfB0/assets/features/orders/checkout.light.png?w=2500&fit=max&auto=format&n=fnujBPxaFvfkZfB0&q=85&s=d51d0053a32db9f505742b4d4203854c 2500w" />

  <img className="hidden dark:block" src="https://mintcdn.com/polar/fnujBPxaFvfkZfB0/assets/features/orders/checkout.dark.png?fit=max&auto=format&n=fnujBPxaFvfkZfB0&q=85&s=d8ebc400902b1179700e7348745793e8" data-og-width="3840" width="3840" data-og-height="2403" height="2403" data-path="assets/features/orders/checkout.dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/polar/fnujBPxaFvfkZfB0/assets/features/orders/checkout.dark.png?w=280&fit=max&auto=format&n=fnujBPxaFvfkZfB0&q=85&s=5b1783d55724d4260dab83ba63b66a77 280w, https://mintcdn.com/polar/fnujBPxaFvfkZfB0/assets/features/orders/checkout.dark.png?w=560&fit=max&auto=format&n=fnujBPxaFvfkZfB0&q=85&s=a0cf5741f10810ab68d2dd1962511895 560w, https://mintcdn.com/polar/fnujBPxaFvfkZfB0/assets/features/orders/checkout.dark.png?w=840&fit=max&auto=format&n=fnujBPxaFvfkZfB0&q=85&s=189ed0cb4d1ec19a9daf370f778dfea1 840w, https://mintcdn.com/polar/fnujBPxaFvfkZfB0/assets/features/orders/checkout.dark.png?w=1100&fit=max&auto=format&n=fnujBPxaFvfkZfB0&q=85&s=115d82a958ab384611b9fa868566d104 1100w, https://mintcdn.com/polar/fnujBPxaFvfkZfB0/assets/features/orders/checkout.dark.png?w=1650&fit=max&auto=format&n=fnujBPxaFvfkZfB0&q=85&s=479d59cc8717b0f6330996e2f04915dd 1650w, https://mintcdn.com/polar/fnujBPxaFvfkZfB0/assets/features/orders/checkout.dark.png?w=2500&fit=max&auto=format&n=fnujBPxaFvfkZfB0&q=85&s=af86f31f76639dc114a243f54495601f 2500w" />

  The payment attempts information is also available on each order.

  Besides, we've also added new analytics around checkouts: total number of checkouts, successful checkouts, and conversion rate.
</Update>

<Update label="2025-03-11">
  ## Zapier integration officially launched

  We're excited to announce the official launch of our [Zapier integration](https://zapier.com/apps/polar/integrations)! Get started now and connect Polar to 2,000+ other web services.

  <Note>
    We've focused on **triggers** (webhooks) for now, so you can react to events in Polar and trigger actions in other apps.

    Need to perform actions in Polar? Tell us about your use case [here](https://github.com/orgs/polarsource/discussions/new?category=integrations\&labels=integrations%2Fzapier) and we'll consider adding more actions in the future.
  </Note>
</Update>

<Update label="2025-03-05">
  ## Customer State

  Maybe one of our neatest features to date! Customer State is a concept allowing you to query for the current state of a customer, including their **active subscriptions** and **granted [benefits](/features/benefits/introduction)**, in a single [API call](/api-reference/customers/state-external) or single [webhook event](/api-reference/webhooks/customer.state_changed).

  Combined with the [External ID](/features/customer-management#external-id) feature, you can get up-and-running in minutes.

  [Read more](/integrate/customer-state)
</Update>

<Update label="2025-03-04">
  ## Better Auth Plugin

  Integrating authentication and billing for your users has never been easier.

  <img src="https://mintcdn.com/polar/Ut0vPUvE1pIdMcH2/assets/changelog/2025-03-04/better_auth.jpeg?fit=max&auto=format&n=Ut0vPUvE1pIdMcH2&q=85&s=41206888e5c593cac95721d75ef3292c" data-og-width="3680" width="3680" data-og-height="3668" height="3668" data-path="assets/changelog/2025-03-04/better_auth.jpeg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/polar/Ut0vPUvE1pIdMcH2/assets/changelog/2025-03-04/better_auth.jpeg?w=280&fit=max&auto=format&n=Ut0vPUvE1pIdMcH2&q=85&s=a3a315f319b6e462a42d1a4815c806df 280w, https://mintcdn.com/polar/Ut0vPUvE1pIdMcH2/assets/changelog/2025-03-04/better_auth.jpeg?w=560&fit=max&auto=format&n=Ut0vPUvE1pIdMcH2&q=85&s=1c166f855f7dac6b29f212ed49793fa9 560w, https://mintcdn.com/polar/Ut0vPUvE1pIdMcH2/assets/changelog/2025-03-04/better_auth.jpeg?w=840&fit=max&auto=format&n=Ut0vPUvE1pIdMcH2&q=85&s=45446626b116d984c78c9d821396cca6 840w, https://mintcdn.com/polar/Ut0vPUvE1pIdMcH2/assets/changelog/2025-03-04/better_auth.jpeg?w=1100&fit=max&auto=format&n=Ut0vPUvE1pIdMcH2&q=85&s=06b67e75a228b7a33f5c1d60cafabedf 1100w, https://mintcdn.com/polar/Ut0vPUvE1pIdMcH2/assets/changelog/2025-03-04/better_auth.jpeg?w=1650&fit=max&auto=format&n=Ut0vPUvE1pIdMcH2&q=85&s=e7315932501dc71542d1ea1bea1d495e 1650w, https://mintcdn.com/polar/Ut0vPUvE1pIdMcH2/assets/changelog/2025-03-04/better_auth.jpeg?w=2500&fit=max&auto=format&n=Ut0vPUvE1pIdMcH2&q=85&s=6a2e2aacb09903b8be46f928e989d702 2500w" />

  [Better Auth](https://www.better-auth.com/) is an open source authentication framework for
  TypeScript that is quickly becoming a favorite amongst developers. Today, we're
  thrilled to have shipped a Polar plugin for Better Auth - in collaboration with them.

  Checkout our [integration guide](/integrate/sdk/adapters/better-auth).
</Update>

<Update label="2025-02-27">
  ## Customer External ID

  We've added support for an `external_id` field on Customers. We believe this will greatly simplify the reconciliation process between your system and Polar.

  Previously, the recommended way to reconcile with your users was to use `metadata`. However, this was not always the most convenient method, especially if you needed to fetch a Customer from our API.

  With `external_id`, you can now fetch a Customer directly by their external ID through dedicated `GET`, `PATCH`, and `DELETE` endpoints. You don't even need to store Polar's internal ID in your system anymore! [Read more](/features/customer-management#external-id)

  Of course, you can also directly preset `external_customer_id` when creating a Checkout Session, and it will automatically be set on the newly created Customer after a successful checkout. [Read more](/features/checkout/session#external-customer-id)
</Update>

<Update label="2025-02-19">
  ## Polar's take on Product variants

  We've released big changes to how we handle products and pricing, allowing us to support a unique approach to what the industry typically calls **variants** 🔥

  We believe having a single product with multiple pricing models and benefits adds unneccessary complexity to the user and to the API. Instead, we chose to treat everything as a product, giving you maximum flexibility about the pricing and benefits you want to offer.

  Thus, we introduce support for **multiple products** at checkout, allowing customers to switch between them before purchasing. Typically, you can offer a monthly and a yearly product, with specific pricing and benefits for each.

  {" "}

  <img className="block dark:hidden" src="https://mintcdn.com/polar/Ut0vPUvE1pIdMcH2/assets/features/checkout/session/checkout_multiple_products.light.png?fit=max&auto=format&n=Ut0vPUvE1pIdMcH2&q=85&s=36f88ae4e5e70735484c068f3605b713" data-og-width="3840" width="3840" data-og-height="2500" height="2500" data-path="assets/features/checkout/session/checkout_multiple_products.light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/polar/Ut0vPUvE1pIdMcH2/assets/features/checkout/session/checkout_multiple_products.light.png?w=280&fit=max&auto=format&n=Ut0vPUvE1pIdMcH2&q=85&s=04994e58aef6964bcbad83136d7a623b 280w, https://mintcdn.com/polar/Ut0vPUvE1pIdMcH2/assets/features/checkout/session/checkout_multiple_products.light.png?w=560&fit=max&auto=format&n=Ut0vPUvE1pIdMcH2&q=85&s=97436039cd7d08c4ca762d81dada1a73 560w, https://mintcdn.com/polar/Ut0vPUvE1pIdMcH2/assets/features/checkout/session/checkout_multiple_products.light.png?w=840&fit=max&auto=format&n=Ut0vPUvE1pIdMcH2&q=85&s=3bf82c3989003e71f22a230a25db119f 840w, https://mintcdn.com/polar/Ut0vPUvE1pIdMcH2/assets/features/checkout/session/checkout_multiple_products.light.png?w=1100&fit=max&auto=format&n=Ut0vPUvE1pIdMcH2&q=85&s=10505f70deec13a9097af4daa1d04b86 1100w, https://mintcdn.com/polar/Ut0vPUvE1pIdMcH2/assets/features/checkout/session/checkout_multiple_products.light.png?w=1650&fit=max&auto=format&n=Ut0vPUvE1pIdMcH2&q=85&s=47784df3a7278ec4df21c13c3ff81b5c 1650w, https://mintcdn.com/polar/Ut0vPUvE1pIdMcH2/assets/features/checkout/session/checkout_multiple_products.light.png?w=2500&fit=max&auto=format&n=Ut0vPUvE1pIdMcH2&q=85&s=f91a412a12601270ac3bfadd82832e7e 2500w" />

  <img className="hidden dark:block" src="https://mintcdn.com/polar/Ut0vPUvE1pIdMcH2/assets/features/checkout/session/checkout_multiple_products.dark.png?fit=max&auto=format&n=Ut0vPUvE1pIdMcH2&q=85&s=82f61a0c8e8108b64d214c223d9a0f67" data-og-width="3840" width="3840" data-og-height="2500" height="2500" data-path="assets/features/checkout/session/checkout_multiple_products.dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/polar/Ut0vPUvE1pIdMcH2/assets/features/checkout/session/checkout_multiple_products.dark.png?w=280&fit=max&auto=format&n=Ut0vPUvE1pIdMcH2&q=85&s=06d12edfe721f4ed1686a09110f935be 280w, https://mintcdn.com/polar/Ut0vPUvE1pIdMcH2/assets/features/checkout/session/checkout_multiple_products.dark.png?w=560&fit=max&auto=format&n=Ut0vPUvE1pIdMcH2&q=85&s=7bfedd743a9e5a2e2924f072218a6d73 560w, https://mintcdn.com/polar/Ut0vPUvE1pIdMcH2/assets/features/checkout/session/checkout_multiple_products.dark.png?w=840&fit=max&auto=format&n=Ut0vPUvE1pIdMcH2&q=85&s=d931de8df011738cedb1988f3c7adaee 840w, https://mintcdn.com/polar/Ut0vPUvE1pIdMcH2/assets/features/checkout/session/checkout_multiple_products.dark.png?w=1100&fit=max&auto=format&n=Ut0vPUvE1pIdMcH2&q=85&s=bd13134692851f71dd9228f52558b8a6 1100w, https://mintcdn.com/polar/Ut0vPUvE1pIdMcH2/assets/features/checkout/session/checkout_multiple_products.dark.png?w=1650&fit=max&auto=format&n=Ut0vPUvE1pIdMcH2&q=85&s=5396835651699c364b553bcc5ea9f34d 1650w, https://mintcdn.com/polar/Ut0vPUvE1pIdMcH2/assets/features/checkout/session/checkout_multiple_products.dark.png?w=2500&fit=max&auto=format&n=Ut0vPUvE1pIdMcH2&q=85&s=8b2984d955958ad755028e2760028fcd 2500w" />

  This is available right now using the [Checkout Session API](/features/checkout/session) and [Checkout Links](/features/checkout/links).

  ### Depreciations

  * Products can no longer have both a monthly and yearly pricing. Existing products still work, but you'll see a warning like this when trying to edit their pricing:

  {" "}

  <Frame>
    <img className="block dark:hidden h-[200px]" src="https://mintcdn.com/polar/Ut0vPUvE1pIdMcH2/assets/changelog/2025-02-19/deprecated_pricing.light.png?fit=max&auto=format&n=Ut0vPUvE1pIdMcH2&q=85&s=49934d3505bcdc38dbeafe43f9a72b58" data-og-width="636" width="636" data-og-height="840" height="840" data-path="assets/changelog/2025-02-19/deprecated_pricing.light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/polar/Ut0vPUvE1pIdMcH2/assets/changelog/2025-02-19/deprecated_pricing.light.png?w=280&fit=max&auto=format&n=Ut0vPUvE1pIdMcH2&q=85&s=e65d3de7ddfd5a6ab1769f4b6df49c86 280w, https://mintcdn.com/polar/Ut0vPUvE1pIdMcH2/assets/changelog/2025-02-19/deprecated_pricing.light.png?w=560&fit=max&auto=format&n=Ut0vPUvE1pIdMcH2&q=85&s=5cd2637aa8693c489f61689bf9608b2c 560w, https://mintcdn.com/polar/Ut0vPUvE1pIdMcH2/assets/changelog/2025-02-19/deprecated_pricing.light.png?w=840&fit=max&auto=format&n=Ut0vPUvE1pIdMcH2&q=85&s=f1848eed72e8996b801ca5ff2dd369a0 840w, https://mintcdn.com/polar/Ut0vPUvE1pIdMcH2/assets/changelog/2025-02-19/deprecated_pricing.light.png?w=1100&fit=max&auto=format&n=Ut0vPUvE1pIdMcH2&q=85&s=cff67ee9261a7fa66266b23054905ce9 1100w, https://mintcdn.com/polar/Ut0vPUvE1pIdMcH2/assets/changelog/2025-02-19/deprecated_pricing.light.png?w=1650&fit=max&auto=format&n=Ut0vPUvE1pIdMcH2&q=85&s=a41ef4b91020fd4ec3fcc1f52ba39e91 1650w, https://mintcdn.com/polar/Ut0vPUvE1pIdMcH2/assets/changelog/2025-02-19/deprecated_pricing.light.png?w=2500&fit=max&auto=format&n=Ut0vPUvE1pIdMcH2&q=85&s=b642f0b6bfcbcb10d76b5e10d75cafe0 2500w" />

    <img className="hidden dark:block h-[200px]" src="https://mintcdn.com/polar/Ut0vPUvE1pIdMcH2/assets/changelog/2025-02-19/deprecated_pricing.dark.png?fit=max&auto=format&n=Ut0vPUvE1pIdMcH2&q=85&s=26006e80ef284cc79eb4bf7a434e166f" data-og-width="636" width="636" data-og-height="840" height="840" data-path="assets/changelog/2025-02-19/deprecated_pricing.dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/polar/Ut0vPUvE1pIdMcH2/assets/changelog/2025-02-19/deprecated_pricing.dark.png?w=280&fit=max&auto=format&n=Ut0vPUvE1pIdMcH2&q=85&s=4525f8a4779925efaf53ad5a21118c47 280w, https://mintcdn.com/polar/Ut0vPUvE1pIdMcH2/assets/changelog/2025-02-19/deprecated_pricing.dark.png?w=560&fit=max&auto=format&n=Ut0vPUvE1pIdMcH2&q=85&s=7f79e8f8b5bdb4269b6bee2454466d45 560w, https://mintcdn.com/polar/Ut0vPUvE1pIdMcH2/assets/changelog/2025-02-19/deprecated_pricing.dark.png?w=840&fit=max&auto=format&n=Ut0vPUvE1pIdMcH2&q=85&s=e29745dbd4d5b72a54b350560f24af76 840w, https://mintcdn.com/polar/Ut0vPUvE1pIdMcH2/assets/changelog/2025-02-19/deprecated_pricing.dark.png?w=1100&fit=max&auto=format&n=Ut0vPUvE1pIdMcH2&q=85&s=30576f8854febabb8129d38f184b8361 1100w, https://mintcdn.com/polar/Ut0vPUvE1pIdMcH2/assets/changelog/2025-02-19/deprecated_pricing.dark.png?w=1650&fit=max&auto=format&n=Ut0vPUvE1pIdMcH2&q=85&s=ca196f3fc92085b830bdc6dbba0375cb 1650w, https://mintcdn.com/polar/Ut0vPUvE1pIdMcH2/assets/changelog/2025-02-19/deprecated_pricing.dark.png?w=2500&fit=max&auto=format&n=Ut0vPUvE1pIdMcH2&q=85&s=023941a6e7f1cf03e82c18376cd5c7b6 2500w" />
  </Frame>

  ### API changes

  * The `product_id` and `product_price_id` fields are deprecated in the [Checkout Session API](/api-reference/checkouts/create-session). You should now use the `products` field to specify the products you want to include in the checkout.
  * The `type` and `recurring_interval` fields on `ProductPrice` are deprecated. `recurring_interval` is now set directly on `Product`.
</Update>
