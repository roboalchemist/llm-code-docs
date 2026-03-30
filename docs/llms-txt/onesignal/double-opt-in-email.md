# Source: https://documentation.onesignal.com/docs/en/double-opt-in-email.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Set up confirmed opt-in for email

> Learn how to implement a double opt-in (confirmed opt-in) process in OneSignal using Tags, Segments, and Journeys to improve engagement, compliance, and list quality.

## Overview

A **confirmed opt-in** (also called **double opt-in**) requires new email subscribers to verify their email address by clicking a confirmation link in a follow-up email. This extra step ensures your email subscribers genuinely want to hear from you.

<Info>
  This guide walks you through how to set up a confirmed opt-in workflow using a minimum of 1 Tag, Segment, and Journey. See our [Pricing page](https://onesignal.com/pricing) for details on plan limits.

  If you want to set up a confirmed opt-in flow via API directly, see [Example verification magic link OTP](./example-verification-magic-link-otp).
</Info>

### Single vs double opt-in

* **Single opt-in**: A user enters their email (e.g., signup form) and is immediately added to your mailing list.
* **Double opt-in (confirmed opt-in)**: After entering their email, the user must click a confirmation link in a verification email before they’re added.

#### Benefits of double opt-in

* Improves engagement and list quality
* Verifies compliance with **GDPR**, **CAN-SPAM**, and other regulations
* Filters out fake, spam-trap, or mistyped addresses
* Reduces bounce and complaint rates
* Protects against abuse and list bombing

<Note>
  Most professional senders use double opt-in to protect their domain reputation and maximize [deliverability](./email-deliverability).
</Note>

***

## How to create a confirmed opt-in journey

This setup will use a tag called `confirmed_opt_in` with a value of `true` or `false` to identify confirmed subscribers. If you already have a list of email subscribers that are confirmed, you can use the [CSV Importer](./import) to add the tag to these users.

**Prerequisites:**

Before getting started, set your email addresses as test Subscriptions in OneSignal. See [Test Subscriptions](./find-set-test-subscriptions) for more details.

### 1. Create a segment of users that did not confirm opt-in

Within the OneSignal dashboard, go to **Audience > Segments** and click **New Segment**.

Build a segment called **Did not confirm email opt-in** that uses the following filters with **AND** logic:

* **User Tag** with `confirmed_opt_in` **"is not"** `true`
* **Device Type** is **Email**
* **Test Users** is true (will remove before setting live in Production)

This segment will contain all test users with an email Subscription and tag `confirmed_opt_in` set to `false` or is not set.

<Frame caption="Did not confirm email opt-in segment">
  <img src="https://mintcdn.com/onesignal/P-72FyFfB9AgPzK3/images/tutorials/did-not-confirm-email-opt-in-segment.png?fit=max&auto=format&n=P-72FyFfB9AgPzK3&q=85&s=8192490399d038544ae86863fce50a8c" alt="Did not confirm email opt-in segment" width="1246" height="866" data-path="images/tutorials/did-not-confirm-email-opt-in-segment.png" />
</Frame>

### 2. Create a confirmed opt-in email template

Navigate to **Messages > Templates > New Email Template** and select **HTML Editor** or **Drag & Drop Editor**.

Design a simple confirmation email:

* Clear subject line (e.g., “Confirm your subscription”)
* A single, prominent **confirmation CTA** (“Confirm Subscription”)
* Do not include any other links like social media buttons or other CTAs that may distract the user from the confirmation process.

Here’s a starter template you can copy and paste into the HTML editor:

```html HTML theme={null}
<!DOCTYPE html>
<html>
  <body style="font-family: Arial, sans-serif; background-color: #f7f7f7; padding: 20px;">
    <table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="max-width: 600px; margin: auto; background: #ffffff; border-radius: 8px; overflow: hidden;">
      <tr>
        <td style="padding: 30px; text-align: center;">
          <h2 style="color: #333;">Please confirm your subscription</h2>
          <p style="color: #555;">We just need to verify your email address before adding you to our list.</p>
          <a href="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHgxZjNrcTRvM2FoZTNzNDVhN2c1ZmN3ajdwYjFlcjR6ZmU0MDVuNCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/fxI1G5PNC5esyNlIUs/giphy.gif" 
             style="display: inline-block; padding: 12px 20px; margin-top: 20px; background-color: #007bff; color: #ffffff; text-decoration: none; border-radius: 4px; font-weight: bold;">
             Confirm Subscription
          </a>
          <p style="font-size: 12px; color: #999; margin-top: 30px;">
            If you did not request this, you can safely ignore this email.
          </p>
        </td>
      </tr>
    </table>
  </body>
</html>
```

<Frame caption="Opt-in Email Template">
  <img src="https://mintcdn.com/onesignal/P-72FyFfB9AgPzK3/images/tutorials/html-opt-in-template.png?fit=max&auto=format&n=P-72FyFfB9AgPzK3&q=85&s=f466d82e6e3a9ab0d644bb5f84d82bdb" alt="Opt-in Template" width="2312" height="1496" data-path="images/tutorials/html-opt-in-template.png" />
</Frame>

<Warning>
  Notice the "Confirm Subscription" button links to a page `https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHgxZjNrcTRvM2FoZTNzNDVhN2c1ZmN3ajdwYjFlcjR6ZmU0MDVuNCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/fxI1G5PNC5esyNlIUs/giphy.gif`

  It is recommended to change this to your website page that thanks the user for confirming their subscription.
</Warning>

### 3. Build a confirmed opt-in Journey

Navigate to **Journeys > New Journey** and select **Start from scratch**.

#### Journey settings

1. Name the Journey: `Confirm Email Opt-in` or anything you like to recognize what this Journey does.
2. Entry Rules: Include Segment **Did not confirm email opt-in** segment.
3. Exit Rules: Check **They moved through the entire Journey**.
4. Re-entry Rules: Select **No, they can receive this only once**.
5. Schedule: Select **Start immediately** or schedule it for a later time and **Never stops**.

Click **Save**.

#### Email message step

Add an **Email** message step and select the **Confirm Email Opt-in** template.

Your Journey should so far look like this:

<Frame caption="Email message step & Journey Settings">
  <img src="https://mintcdn.com/onesignal/P-72FyFfB9AgPzK3/images/tutorials/confirm-email-opt-in-message-step-and-journey-settings.png?fit=max&auto=format&n=P-72FyFfB9AgPzK3&q=85&s=15d881b358d978ce55bfe2c162248744" alt="Email message step" width="1506" height="1728" data-path="images/tutorials/confirm-email-opt-in-message-step-and-journey-settings.png" />
</Frame>

#### Wait until step

Add a **Wait Until** step and set the Branch A condition to:

* **Previous Message**
* **Confirm email subscription** template name
* **Clicked**

Check the **Expiration Branch** option and set to "Wait a maximum of `1 Day` and **Continue Journey**".

<Frame caption="Wait until step">
  <img src="https://mintcdn.com/onesignal/P-72FyFfB9AgPzK3/images/tutorials/confirm-email-opt-in-wait-until-step.png?fit=max&auto=format&n=P-72FyFfB9AgPzK3&q=85&s=18cd9325a298fca5dc1a3d417469d02b" alt="Wait until step" width="754" height="746" data-path="images/tutorials/confirm-email-opt-in-wait-until-step.png" />
</Frame>

#### Tag users who confirm

Under the branch **A (Message Clicked)** add a **Tag User** action and set the tag to `confirmed_opt_in` and the value to `true`.

<Frame caption="Tag User action">
  <img src="https://mintcdn.com/onesignal/P-72FyFfB9AgPzK3/images/tutorials/confirm-email-opt-in-tag-user-action.png?fit=max&auto=format&n=P-72FyFfB9AgPzK3&q=85&s=001a1d48f7bba349de2b21c297b509e9" alt="Tag User action" width="900" height="472" data-path="images/tutorials/confirm-email-opt-in-tag-user-action.png" />
</Frame>

As users click the button to confirm their subscription, their `confirmed_opt_in` tag will change from `false` to `true`. This will allow you to track which users have confirmed their email subscription.

#### Follow up with non-confirmers

After 1 day, if the user did not click the button to confirm their subscription, they will go down the **Expire (1 Day)** branch. At this point you can create a new email template and repeat the process (Confirm email subscription 2 > Wait until clicked > Tag if clicked). It is recommended to repeat the process at least one more time to ensure the best opt-in rate.

<Frame caption="Full Confirm Email Opt-in Journey Example">
  <img src="https://mintcdn.com/onesignal/P-72FyFfB9AgPzK3/images/tutorials/confirm-email-opt-in-journey-example.png?fit=max&auto=format&n=P-72FyFfB9AgPzK3&q=85&s=4b3e76960f548462d2213c1ea388ceb0" alt="Full Confirm Email Opt-in Journey Example" width="862" height="1636" data-path="images/tutorials/confirm-email-opt-in-journey-example.png" />
</Frame>

### 4. Test

At this point the Journey should be ready to test. If you followed this tutorial, remember that we use the "Test Users" filter in the Segment, so this will only send to emails you marked as "testers" and fit the tag criteria. If you need to add more test emails, you can do so manually within the OneSignal dashboard following these instructions:

* [Import emails](./import)
* Set [Test Subscriptions](./find-set-test-subscriptions)

When ready to test:

1. Click **Set Live** in the Journey.
2. Wait a few minutes and you should receive the first email template.
3. Click the button in the email. Wait a few more minutes.
4. Your user should exit the Journey and have the updated `confirmed_opt_in=true` tag.

#### Troubleshooting

Once you set the Journey live, if you did not get the confirmation email after a few minutes:

1. Navigate back into the active Journey
2. Click the first Email Step
3. Select **Audience Activity** at the top left. See [Journey Analytics](./journeys-analytics) for more details on Audience Activity.
4. You should see your email in the "Delivered" column. If its not there, check if your email address is Subscribed and fits the Segment criteria.

If you received the email and clicked the button, but did not get the tag updated afer a few minutes:

1. Navigate to **Audience > Users**
2. Search for your email address
3. Check the "Tags" column. You should see `confirmed_opt_in=true` if the Journey worked correctly.

<Info>
  Still need help?

  Email us at `support@onesignal.com` with the following information:

* The email address that you are testing.
* A link to the Journey. You can copy-paste the URL from the browser address bar.
* Any additional information that you think may be helpful.

  We'll be happy to help!
</Info>

### 5. Set live in production

When ready to send this to actual users, you will need to do the following:

1. Navigate to the Journey and click **More Options > Stop + Archive**.
2. Navigate to the Segment and click **Options > Pause**, then **Options > Duplicate**.
3. Update the Segment to remove the "Test Users" filter.
4. Navigate back to the Journeys page and click **Options > Duplicate**.
5. Update the Journey to use the Segment without the "Test Users" filter and **Save**.
6. Click **Set Live** when ready to go live to all users.

<Check>
  Subscribers who confirm now carry the `confirmed_opt_in=true` tag, which you can use for segmentation and to ensure you only message verified users.
</Check>

***

## Important Considerations & Gotchas

<AccordionGroup>
  <Accordion title="Regulatory Compliance">
    * **GDPR** requires explicit consent, which double opt-in provides.
    * **CAN-SPAM** doesn’t require double opt-in, but it reduces complaints.
    * Always store proof of consent (timestamp + source).
  </Accordion>

  <Accordion title="Deliverability Best Practices">
    * Confirmation emails should be **plain and short** — avoid heavy images.
    * Don’t add marketing content to your confirmation email.
    * Set up proper [email authentication](./email-setup) (SPF, DKIM, DMARC) to avoid spam folders.
  </Accordion>

  <Accordion title="UX and Conversion Tips">
    * Show a **thank-you page** after signup that explains the confirmation step.
    * Use a clear subject line (e.g., “One last step: Confirm your subscription”).
    * Send reminders sparingly — 2–3 attempts max.
  </Accordion>

  <Accordion title="Common Issues">
    * **Links not tracking**: Make sure your button uses a tracked link from the OneSignal template editor.
    * **Users never confirm**: Some emails may land in spam. Encourage users to check spam or promotions folders.
    * **Duplicate opt-ins**: Only allow `confirmed_opt_in = true` users in your primary send segments.
  </Accordion>
</AccordionGroup>

***

## Next Steps

* Use the `confirmed_opt_in` tag to build **high-quality email segments**.
* Review [Email Setup & Compliance](./email-setup) to protect your domain reputation.
* Explore [Journeys actions and branches](./journeys-actions) for advanced retry strategies.

Built with [Mintlify](https://mintlify.com).
