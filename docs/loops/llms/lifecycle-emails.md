# Source: https://loops.so/docs/guides/lifecycle-emails.md

> ## Documentation Index
> Fetch the complete documentation index at: https://loops.so/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to set up customer lifecycle emails in Loops

> How to send onboarding, dunning and churn emails to your customers with Loops.

For SaaS companies, there are a few important events in a customer lifecycle that email can help with.

* **Acquisition emails** are emails sent after a user signs up for a waitlist, platform or newsletter.
* **Onboarding emails** help brand new users get familiar with—and get the most out of—your product.
* **Retention emails** keep your users engaged long-term.
* **Re-engagement emails** attempt to get users active again if they haven't used your platform recently.
* **Dunning emails** help reduce churn by prompting the user to re-activate a subscription or fix payment issues.
* **Re-activation emails** attempt to bring users back after a cancelation.

With Loops, you can easily set up "loops" (email workflows) plus our API (or an integration) to help with each of these use cases.

## How it works

To get this set up in Loops, the idea is to create a [loop](/loop-builder) for each of the types of email you want to send. So there would be a loop for activation emails and a loop for dunning emails and so on.

A loop is like an email sequence containing emails, time delays, audience filters and an initial trigger.

We will use a [custom contact property](/contacts/properties) called `subscriptionStatus` to enter users into each of the loops at different times in their subscriptions.

This property is used as the [loop trigger](/loop-builder/loop-triggers); if the property is ever changed—using [an integration](/integrations) or the [Loops API](/api-reference)—we trigger a loop, which will send emails to the contact.

## Add a contact property

First, let's add the contact property to the audience in Loops.

Go to your [Audience page](https://app.loops.so/audience). Click on a table header to show the dropdown then select **Add property**.

Enter "Subscription status" into the **Name** field and make sure **String** is selected in the "Type" field. (You'll notice that the "stored name" of your property is `subscriptionStatus`. This is the name we'll use in the API and integrations).

Click **Add Property** when you're done. Your new property was added to the far right of the Audience table.

## Update contacts

Now you can click on contacts and update the value manually one-by-one, or use the API or an integration to update contacts programmatically.

To update contacts in bulk you can download your Audience as a CSV, update values and [re-upload the file](/add-users/csv-upload).

## Create loops

The next step is to create the loops, one for each type of email. Repeat the following step for each of the different subscription statuses you want to send emails for.

Go to the [Loops page](https://app.loops.so/loops) in your account and click **New**.

Select the **Contact update** option, which will create a new loop using that trigger.

<img src="https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/triggers.png?fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=ba70751cfb0bbded010aa98d2e1d2661" alt="Select trigger" data-og-width="2280" width="2280" data-og-height="1409" height="1409" data-path="images/triggers.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/triggers.png?w=280&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=5368c3de6799c0594b57fa911cbbdcff 280w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/triggers.png?w=560&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=f0ab68aecfa3ece1267104f2991a11b8 560w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/triggers.png?w=840&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=f7461ac943339a6a86562ac48c428709 840w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/triggers.png?w=1100&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=79e61483ec59bfb9d5424ec6ff217fdd 1100w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/triggers.png?w=1650&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=f328b6128aa6debed2e39d789c5d0456 1650w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/triggers.png?w=2500&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=6acb4ae62a947e27d85396e443f82dad 2500w" />

You will enter the [loop builder](/loop-builder). Click on the **Contact updated** node to set up the loop trigger.

### Set up the trigger

1. Select the "Subscription Status" property from the **When** dropdown.
2. The **Changes from** dropdown should have "Any value" selected.
3. Next you need to specify what value Loops should look out for to enter users into the loop.
   For example, for onboarding emails, you can choose "is empty" from the **To** dropdown. For re-activation emails select "Equals" from the **To** dropdown and enter a relevant value like "Canceled".
4. **Trigger time** should be set to "Every time"; this will make sure users are entered into the loop every time that the Subscription Status value matches.

### Create emails

Now create the email(s) you want to send from each loop.

You can add as many emails as you like into each loop, separated with timers. If you want to send emails to certain groups of contacts, you can use Audience filters in your loop.

We have a range of [email templates](https://app.loops.so/templates) available, which you can use as a base for all of your subscription emails.

<img src="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/getting-started.png?fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=3ca8868a9bddc666b8293dc9ed17977f" alt="Templates" data-og-width="2280" width="2280" data-og-height="1284" height="1284" data-path="images/getting-started.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/getting-started.png?w=280&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=5a506352291ae9d058114929ca283502 280w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/getting-started.png?w=560&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=f2b5821b771981420f36232316f9cc18 560w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/getting-started.png?w=840&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=4a949d33a3098407f8344113d1ca5490 840w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/getting-started.png?w=1100&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=2adb957e405ce648e593a0414190c58f 1100w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/getting-started.png?w=1650&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=f2cd45877711b775b264c09ad18f9be2 1650w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/getting-started.png?w=2500&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=cde9e90bc02db67c684e5204272261d5 2500w" />

If you want to use cohesive branding in your emails, make use of [themes](/creating-emails/editor#themes) in the editor.

<img src="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/message-visual.png?fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=e2c7088ffd4d20ac66b5fee7a1756010" alt="Editor panel" data-og-width="2280" width="2280" data-og-height="1953" height="1953" data-path="images/message-visual.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/message-visual.png?w=280&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=1566d2f25ff94cd77ce02190627153c6 280w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/message-visual.png?w=560&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=b97a0e4251a474a7649518819d87364b 560w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/message-visual.png?w=840&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=a81c6e2c9f6ac29e31329ada927e038a 840w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/message-visual.png?w=1100&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=adb055873f4fd4c0e917faac0c927983 1100w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/message-visual.png?w=1650&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=5e6346334f27792ff4fab4450fe9c3a9 1650w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/message-visual.png?w=2500&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=738b8ddf5342b807bcfddc6fa07e61c7 2500w" />

## Update the Subscription status value

The final step is to make sure that your contacts have the correct "Subscription status" value assigned to them in Loops.

This will make sure they are in the correct loops at the correct moment within their subscription.

Using the API you can make a simple `PUT` call to the [Update contact endpoint](/api-reference/update-contact), with a request containing the contact's email address and subscription status.

(You can also add more contact properties in this call if you want to add more data to the contact in Loops.)

<Note>
  Using the Update contact endpoint will either create or update a contact in
  Loops using the provided email address.
</Note>

```json  theme={"dark"}
{
  "email": "canceleduser@gmail.com",
  "subscriptionStatus": "Canceled"
}
```

Many of [our integrations](/integrations) allow syncing of contact data. Just make sure you create or update contacts and include the current `subscriptionStatus` value.

Now you have set up different loops to trigger when the "Subscription status" value changes, your users will be automatically entered into each loop and receive the correct emails at the correct times during their subscription lifecycle.

## Example loops

Here are some example loops you can create along with a suggested trigger and loop contents.

### Onboarding

Sent to brand new users.

* **Trigger**: Contact added or Contact updated (e.g. `subscriptionStatus` is empty).
* **Audience filter**: Match the trigger (e.g. `subscriptionStatus` is empty).
* **Loop contents**: 1–5 welcome and onboarding emails over the first 30 days.

### New subscribers

Sent to users who just started paying.

* **Trigger**: Contact updated (e.g. `subscriptionStatus` changes to "Paying").
* **Audience filter**: Match the trigger (e.g. `subscriptionStatus` equals "Paying").
* **Loop contents**: 1–3 emails about paid-only features over the next 3 days.

### Dunning

Sent to customers who had a first failed payment.

* **Trigger**: Contact updated (e.g. `subscriptionStatus` changes to "Failed").
* **Audience filter**: Match the trigger (e.g. `subscriptionStatus` equals "Failed").
* **Loop contents**: 1–3 emails during your dunning period.

### Churn

Sent to customers who have just cancelled their payments.

* **Trigger**: Contact updated (e.g. `subscriptionStatus` changes to "Canceled")
* **Audience filter**: Match the trigger (e.g. `subscriptionStatus` equals "Canceled").
* **Loop contents**: 1 email saying goodbye and asking for feedback.
