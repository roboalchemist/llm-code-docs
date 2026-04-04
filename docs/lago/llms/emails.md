# Source: https://getlago.com/docs/guide/emails.md

> ## Documentation Index
> Fetch the complete documentation index at: https://getlago.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Emails

> Send automatic emails when issuing an invoice or any billing documents.

<Info>
  **PREMIUM FEATURE** ✨

  Only users with a premium license can automatically send emails from Lago to their customers. Please **[contact us](mailto:hello@getlago.com)** to get access to Lago Cloud and Lago Self-Hosted Premium.
</Info>

With Lago, sending invoices and credit notes to your customers is simple - you can automatically email them as soon as they are created.

<Warning>
  Lago will never ask for payment details or personal information.
</Warning>

## SMTP setup on Lago Cloud

By default, you don't have to worry about SMTP settings with Lago, we take care of it, so you can sit back and relax. However, we also offer custom SMTP for Enterprise customers.

## SMTP setup on Lago Self-hosted Premium

In order to use the email feature, please configure your environment variables [as described here](/guide/lago-self-hosted/docker#smtp-configuration).

## Prerequisites for sending emails

To send emails to your customers, you will need to:

1. Define an organization email in Settings > \[Your billing entity] > General > Informations;
2. Optionally, add your organization’s logo;
3. Turn on the relevant email scenarios in  Settings > \[Your billing entity] > Email scenarios;
4. Define the customer’s email address during customer creation/edition;
5. To send invoices to multiple recipients, define multiple email addresses at the customer level, separated by commas.
   (e.g. `billing@acme.com`,`accounting@acme.com`,`finance@acme.com`)

## Email scenarios

Lago automatically sends email notifications to your customers in three key scenarios:

1. When an invoice is finalized (including subscription invoices, one-off invoices, or credit purchase invoices);
2. When a payment receipt is generated for a successful payment; and
3. When a credit note is issued to adjust or refund an invoice.

By default, all scenarios are switched off. To turn these scenarios on/off:

1. Go to Settings;
2. Open the Emails tab;
3. Toggle each scenario on/off; or
4. Click on a scenario to see the corresponding email; and
5. Use the toggle in the upper-right corner to switch this scenario on/off.

<Info>
  To avoid sending too many notifications to customers, we have deactivated emails for invoices without fees.

  Although invoices with `"fees_amount_cents": 0` are not sent to customers by email, they are available in the database and user interface.
</Info>

## Email locale

The content of the email will be based on the organization or customer's document locale. This means that the email will have the same locale as the invoice sent.

## Email sending address

For the cloud version, Lago uses [no-reply@getlago.com](mailto:no-reply@getlago.com) as the sending email address. Any responses from your customers will be directed to the email address you have established for your organization in the organization settings.

## Email template

<Frame caption="Email template">
  <img src="https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/email-template.png?fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=7825b52239e4e8c61e7124514c9c519f" data-og-width="2000" width="2000" data-og-height="1025" height="1025" data-path="guide/images/email-template.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/email-template.png?w=280&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=90f0da7814334fa75e6ad108a75e2fce 280w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/email-template.png?w=560&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=30de622b405a8093c0f7c9cbbd0bcfb3 560w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/email-template.png?w=840&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=f71c6a0fb0862ed0baad920fdc046a62 840w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/email-template.png?w=1100&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=6de167b14e562b413376c673a71a4062 1100w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/email-template.png?w=1650&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=a8c284b36446af9cd1fe3d59064d45a2 1650w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/email-template.png?w=2500&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=862a608e87fb3999f7a7cfa6b5c1e44d 2500w" />
</Frame>

As mentioned above, some information in the email template can be customized based on the settings of your account, including:

1. The logo of your organization;
2. The name of your organization; and
3. The email address of your organization.
