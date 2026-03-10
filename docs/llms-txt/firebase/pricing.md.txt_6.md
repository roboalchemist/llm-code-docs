# Source: https://firebase.google.com/docs/ai-logic/pricing.md.txt

|---|
| *Click your Gemini API provider to view provider-specific content and code on this page.* <button value="dev" default="">Gemini Developer API</button> <button value="vertex">Vertex AI Gemini API</button> |

<br />

<br />

Pricing and whether your Firebase project needs to be on the
[pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing) depends on your chosen Gemini API provider and the
features of Firebase AI Logic that you use.

**Using Firebase AI Logic is free-of-charge.**

However, if you're on the Blaze pricing plan, you might incur costs
when you use other products in conjunction with Firebase AI Logic.

- **Other Firebase products may incur costs.**
  For details, see the [Pricing page](https://firebase.google.com/pricing).

  - Using some of the attestation providers supported by Firebase App Check.

  <!-- -->

  - Using Firebase Authentication beyond the no-cost usage levels.

  - Using any of Firebase's database products beyond their no-cost usage levels.

- **AI monitoring in the Firebase console may incur costs.**   

  While AI monitoring in the Firebase console is free-of-charge itself, you
  may incur costs if you go beyond the no-cost usage levels of the underlying
  Google Cloud Observability Suite products. Learn more in the
  [Google Cloud Observability Suite pricing documentation](https://cloud.google.com/products/observability#pricing).

- **Your chosen Gemini API provider may incur costs.**
  For details, see [Gemini Developer API pricing](https://ai.google.dev/gemini-api/docs/pricing).

  - Pricing is largely based on the model and features that you use.

  - Using some models (especially preview models) might require billing.

> [!TIP]
> **Tip:** If you're new to Firebase and Google Cloud, check if you're eligible for [$300 of credits](https://firebase.google.com/support/faq#pricing-free-trial) and a Free Trial Cloud Billing account.

## Firebase pricing plan requirements for your chosen API provider

The Gemini Developer API offers different tiers for its pricing:

- **Gemini Developer API "free tier"** :
  This tier requires that your project is *not* linked to a
  Cloud Billing account. This means your Firebase project is on the
  no-cost Spark pricing plan.

- **Gemini Developer API "paid tiers"** :
  These tiers require that your project is linked to a
  Cloud Billing account. This means your Firebase project is on the
  pay-as-you-go Blaze pricing plan.

> [!IMPORTANT]
> **Important:** If your project is linked to a Cloud Billing account (which means it's on the Blaze plan), then the Gemini Developer API makes all usage of its API be pay-as-you-go pricing (including any usage through the Firebase AI Logic SDKs).

Learn about the
[Gemini Developer API pricing](https://ai.google.dev/gemini-api/docs/pricing)
in its documentation.

## Recommendations to manage costs

> [!CAUTION]
> When your project is on the Blaze pricing plan, [**set up budget alerts**](https://firebase.google.com/docs/projects/billing/avoid-surprise-bills#set-up-budget-alert-emails) using the console.
>
> Be aware that **budget alerts do *not* cap your usage or
> charges** --- they are *alerts* about your costs so that you can
> take action, if needed. For example, you might consider
> [using
> budget notifications to programmatically disable Cloud Billing on a
> project](https://cloud.google.com/billing/docs/how-to/disable-billing-with-notifications).

We recommend doing the following to help manage your costs:

- Avoid surprise bills by
  [monitoring your costs and usage](https://firebase.google.com/docs/ai-logic/monitoring) and
  [setting up budget alerts](https://firebase.google.com/docs/projects/billing/avoid-surprise-bills#set-up-budget-alert-emails).

- When using Gemini models (except Live API models), get an
  estimate of the [token size](https://firebase.google.com/docs/ai-logic/count-tokens)
  of your requests using the `countTokens` API before sending your requests and
  accessing the `usageMetadata` attribute in your responses.

- Set the [thinking budget](https://firebase.google.com/docs/ai-logic/thinking)
  (for Gemini 3 models and Gemini 2.5 models only) and the
  `maxOutputTokens` (all Gemini models) in
  the [model's configuration](https://firebase.google.com/docs/ai-logic/model-parameters#gemini).

- [Enable AI monitoring](https://firebase.google.com/docs/ai-logic/monitoring#ai-monitoring-in-console)
  to view dashboards in the Firebase console with
  information about your requests, including token counts.