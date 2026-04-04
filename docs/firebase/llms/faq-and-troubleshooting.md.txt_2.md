# Source: https://firebase.google.com/docs/functions/faq-and-troubleshooting.md.txt

<br />

This page provides answers to frequently asked questions (FAQs) about
Cloud Functions for Firebase.

## Cloud Functions runtime support

<br />

#### How do I upgrade to the latest supported version of Node.js?

<br />

1. Make sure you're on the
   [pay-as-you-go Blaze pricing plan](https://console.firebase.google.com/project/_/overview?purchaseBillingPlan=metered).

2. Make sure you are using the latest version of the Firebase CLI.

3. [Update the `engines` field](https://firebase.google.com/docs/functions/manage-functions#set_nodejs_version)
   in your functions' `package.json`.

4. Optionally, test your changes using the
   [Firebase Local Emulator Suite](https://firebase.google.com/docs/emulator-suite).

5. Redeploy all functions.

<br />

<br />

<br />

#### How can I make sure I deployed my functions to a specific Node.js runtime?

<br />

In the Firebase console, go to the
[functions dashboard](https://console.firebase.google.com/project/_/functions/list),
select a function, and check the function's language under
**Additional details**.

<br />

<br />

<br />

#### I use Firebase Extensions. Will I be affected by Cloud Functions runtime
updates?

<br />

Yes. Since
[extensions use Cloud Functions](https://firebase.google.com/docs/extensions#how_does_it_work),
the runtime of your extensions will need to be updated on the same timeline as
Cloud Functions.

We recommend that you periodically update to the latest version of each
extension installed in your project.
You can upgrade your projects' extensions via the
[Firebase console](https://firebase.google.com/docs/extensions/manage-installed-extensions?platform=console#update-version)
or
[Firebase CLI](https://firebase.google.com/docs/extensions/manage-installed-extensions?platform=cli#update-version).

<br />

<br />

## Cloud Functions pricing

> [!CAUTION]
> When your project is on the Blaze pricing plan, [**set up budget alerts**](https://firebase.google.com/docs/projects/billing/avoid-surprise-bills#set-up-budget-alert-emails) using the console. You can use the [Blaze plan calculator](https://firebase.google.com/pricing#blaze-calculator) to estimate your monthly costs.
>
> Be aware that **budget alerts do *not* cap your usage or
> charges** --- they are *alerts* about your costs so that you can
> take action, if needed. For example, you might consider
> [using
> budget notifications to programmatically disable Cloud Billing on a
> project](https://cloud.google.com/billing/docs/how-to/disable-billing-with-notifications).

<br />

#### Why do I need a billing account to use Cloud Functions for Firebase?

<br />

Cloud Functions for Firebase relies on some paid Google services. New
function deployments with Firebase CLI 11.2.0 and higher rely on
[Cloud Build](https://cloud.google.com/cloud-build) and
[Artifact Registry](https://cloud.google.com/artifact-registry/).
Deployments to earlier versions use Cloud Build in the same way, but rely
on
[Container Registry](https://cloud.google.com/container-registry/) and
[Cloud Storage](https://cloud.google.com/storage) for storage
instead of Artifact Registry. Usage of these services will be billed in addition to
existing pricing.

**Storage space for Firebase CLI 11.2.0 and newer versions**

[Artifact Registry](https://cloud.google.com/artifact-registry)
provides the containers in which functions run. Artifact Registry
provides the first 500MB at no cost, so your first function deployments may
not incur any fees. If you exceed that threshold, each additional GB of storage
is billed at $0.10 per month.

**Storage space for Firebase CLI 11.1.x and prior versions**

For functions deployed to earlier versions,
[Container Registry](https://cloud.google.com/container-registry/),
provides the containers in which functions run. You'll be
billed for each container required to deploy a function. You may notice small
charges for each container stored---for example, 1GB of storage is
[billed at $0.026 per month](https://cloud.google.com/container-registry/pricing#storage).

To understand more about how your bill might change, review the following

- [Cloud Functions pricing](https://cloud.google.com/functions/pricing): existing no-cost tier is unchanged.
- [Cloud Build pricing:](https://cloud.google.com/cloud-build/pricing) Cloud Build provides for a no-cost tier.
- [Artifact Registry pricing](https://cloud.google.com/artifact-registry/pricing).
- [Container Registry pricing](https://cloud.google.com/container-registry/pricing).

<br />

<br />

<br />

#### Does Cloud Functions for Firebase still have no-cost usage?

<br />

Yes. Even on the pay-as-you-go Blaze pricing plan, Cloud Functions provides a no-cost
tier for invocations, compute time, and internet traffic. The
first 2,000,000 invocations, 400,000 GB-sec, 200,000 CPU-sec, and 5 GB of
Internet egress traffic is provided at no cost each month. You'll be charged
only for usage that exceeds those thresholds.

After the first 500MB of no-cost storage, each deployment operation will incur
small-scale charges for the storage space used for the function's container. If
your development process depends on deploying functions for testing, you can
further minimize costs by using the
[Firebase Local Emulator Suite](https://firebase.google.com/docs/emulator-suite) during development.

See
[Firebase Pricing plans](https://firebase.google.com/pricing#cloud-functions) and the
[Cloud Functions Pricing](https://cloud.google.com/functions/pricing#pricing_examples)
example scenarios.

<br />

<br />

<br />

#### Is Firebase planning to raise the quotas and limits for
Cloud Functions for Firebase?

<br />

No. There are no plans to change the quotas except for the removal of a maximum
build time limit; instead of receiving errors or warnings when the daily build
quota of 120 minutes is reached, you'll be billed under the terms of the
pay-as-you-go Blaze pricing plan. See
[Quotas and limits](https://firebase.google.com/docs/functions/quotas#time_limits).

<br />

<br />

<br />

#### Can I get the Google Cloud $300 credit?

<br />

Yes, you can create a Cloud Billing account in the Google Cloud console to
get the $300 credit, then link that Cloud Billing account to a Firebase
project.

Learn more about the
[Google Cloud credit](https://cloud.google.com/free/docs/gcp-free-tier#free-trial).

Note that if you do this, you have to then
[set up](https://console.firebase.google.com/project/_/overview?purchaseBillingPlan=metered)
the Blaze pricing plan in the Firebase console in order
for your project to continue working after the $300 credit is exhausted.

<br />

<br />

<br />

#### I want to follow a codelab to learn about Firebase. Can you give me a
temporary billing account?

<br />

No, sorry. You can use the
[Firebase Local Emulator Suite](https://firebase.google.com/docs/emulator-suite) for development
without having a Cloud Billing account. Alternatively, try applying for a
[Google Cloud free trial](https://cloud.google.com/free/docs/gcp-free-tier#free-trial).
If you're still having trouble paying your bill because of this change, contact
Firebase Support.

<br />

<br />

<br />

#### I'm worried I'm going to rack up a huge bill.

<br />

You can
[set up budget alerts](https://firebase.google.com/docs/projects/billing/avoid-surprise-bills#set-up-budget-alert-emails)
in the Google Cloud console to help control costs. Also, you can
[set limits](https://firebase.google.com/docs/functions/manage-functions#min-max-instances) on
the number of billed instances created for each of your functions.
To get an idea of costing for typical scenarios, see the
[Cloud Functions Pricing](https://cloud.google.com/functions/pricing#pricing_examples)
examples.

<br />

<br />

<br />

#### How can I check my current billing charges?

<br />

View the [*Usage and billing*](https://console.firebase.google.com/project/_/usage)
dashboard in the Firebase console.

<br />

<br />

<br />

#### I use Firebase Extensions. Do I need a billing account?

<br />

Yes. Since
[extensions use Cloud Functions](https://firebase.google.com/docs/extensions#how_does_it_work),
extensions will be subject to the same charges as other functions.

To use extensions, you will need to upgrade to the
pay-as-you-go Blaze pricing plan. You will be charged a small amount (typically
[around $0.01 per month](https://firebase.google.com/pricing#cloud-functions))
for the Firebase resources required by each extension you install (even if they
are not used), in addition to any charges associated with your use of Firebase
services.

<br />

<br />