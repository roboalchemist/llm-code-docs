# Source: https://loops.so/docs/types-of-emails.md

> ## Documentation Index
> Fetch the complete documentation index at: https://loops.so/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Types of emails

> Learn about the three types of emails that you can send with Loops: Campaigns, Loops, and Transactional.

<img src="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/create-first-email.png?fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=daa962aaa3dd795ed89021acc341a7a6" alt="" data-og-width="2280" width="2280" data-og-height="1134" height="1134" data-path="images/create-first-email.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/create-first-email.png?w=280&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=995db60712ac648e3d14e8fbb7e651e0 280w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/create-first-email.png?w=560&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=e8d3056be93980f525bb84acc8484820 560w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/create-first-email.png?w=840&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=44eb7ade0e2da35e08cd7c968cfe575c 840w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/create-first-email.png?w=1100&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=557b3af625d764ecfff8d3fa6cd6cb56 1100w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/create-first-email.png?w=1650&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=265f7518e2ac38d3ceb42fa3d4863fe5 1650w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/create-first-email.png?w=2500&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=e7546ba6f5bc0275d3c6444fb6878d3d 2500w" />

## Campaigns

A Campaign is the right type of email for a one-off send to your audience or a segment of your audience.

Marketing emails are a 1-to-many communication, meaning that the same exact email that you craft can (and probably will) be sent and read by a number of recipients or customers.

**Examples:**

* Newsletters
* Investor updates
* Product updates
* User feedback requests

**How to send a Campaign:**

1. Hit “Create” in the top right corner of your Loops dashboard.
2. Select “Campaign” in the popup module.
3. Enter the subject line, preview text, and content of the email.
4. Select your audience segment.
5. Schedule the email to send later or send it immediately.

## Loops

A Loop is an email that is triggered by an event, a contact being added to your audience, or a contact property update.

**Examples:**

* Welcome emails
* User onboarding sequences
* User check-ins

For more information on sending your first Loop, [visit this guide](/loop-builder).

## Transactional

A Transactional email is an automated message that is triggered by a specific contact action.

**Examples:**

* Password resets
* Purchase or upgrade confirmations
* Shipping information
* Account cancellation emails

For more information on sending your first Transactional messages, [read the transactional email guide](/transactional).

**Things to note:**

* Unlike campaigns and loops, transactional emails are not promotional in nature and as a result, they do not require unsubscribe information to be included in the email.
* Unlike campaigns and loops, we do not track opens or link clicks in transactional emails, to increase deliverability of your emails. This also means that `email.opened` and `email.clicked` [webhook events](/webhooks) are not available for transactional emails.
* Contacts behave slightly differently between transactional and marketing emails (campaigns and loops):
  * Your Audience only contains marketing contacts. If a new contact is sent a transactional email, they are not added to your Audience, unless you use the `addToAudience` flag when [sending the email](/api-reference/send-transactional-email).
  * Sending a transactional email to a new contact will not trigger the ["Contact added" loop trigger](/loop-builder#triggers).
  * The "Subscribed" [contact property](/contacts/properties#subscribed) does not affect transactional emails. Unsubscribed contacts will still receive all transactional emails they are sent.

<Tip>
  Are you stuck and wondering exactly how you should be setting up your email flows within Loops?

  Email [chris@loops.so](mailto:chris@loops.so) and we will help get you set up.
</Tip>
