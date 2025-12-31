# Source: https://firebase.google.com/docs/projects/billing/firebase-pricing-plans.md.txt

This page describes the Firebase pricing plans, including how billing works for Firebase and how it connects with other Google services.

Firebase offers two different pricing plans, the[no-cost Spark plan](https://firebase.google.com/docs/projects/billing/firebase-pricing-plans#spark-pricing-plan)and the[pay-as-you-go Blaze plan](https://firebase.google.com/docs/projects/billing/firebase-pricing-plans#blaze-pricing-plan). Here's a brief overview of each plan, but for detailed information, visit the sections later on this page.

| Spark pricing plan *No payment information needed to get started or to use only the no-cost Firebase products* | Blaze pricing plan *Link a billing account to access more services and usage levels beyond the no-cost usage quota* |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Full usage of no-cost Firebase products and features**\***                                                     | Full usage of no-cost Firebase products and features**\***                                                          |
| No-cost usage quota for paid Firebase products**\*\***                                                         | No-cost usage quota for paid Firebase products**\*\***                                                              |
|                                                                                                                | Pay-as-you-go pricing for any additional usage of paid Firebase products                                            |
|                                                                                                                | Access toCloud Functions (no-cost usage quota, then pay-as-you-go pricing for additional usage)                     |
|                                                                                                                | Access to paidGoogle Cloudproducts and features                                                                     |

Which Firebase products are considered "no-cost" vs "paid"?
> **Firebase products that are no-cost**   
> No matter which Firebase pricing plan your project uses, you get full usage of the following Firebase products at no charge --- even in your production apps and*even if you have several million users!*
>
> |---------------------------------------------------------------------|----------------------------------------------------------------|-------------------------------------------------------|
> | A/B Testing App Check App Distribution Authentication(most options) | Cloud Messaging(FCM) Crashlytics Firebase ML(model deployment) | In-App Messaging Performance Monitoring Remote Config |
>
> **Firebase products with a paid-tier of usage**   
> No matter which Firebase pricing plan your project uses, you get no-cost usage quota for the following Firebase products. If your project is on the Blaze plan, you also get pay-as-you-go pricing for additional usage.
>
> |---------------------------------------------------------------------------------------------|----------------------------------------------------------|----------------------------------------------|
> | App HostingandHosting Authentication(phone) Firebase Phone Number Verification Data Connect | Extensions Cloud Firestore Cloud Storage Cloud Functions | Realtime Database Test Lab Firebase AI Logic |
>
> For full details about the Firebase pricing plans (especially about[Cloud Functions](https://firebase.google.com/support/faq#storage-charge)andGoogle Cloudproducts), check out the[Firebase pricing page](https://firebase.google.com/pricing).

### Learn product-specific information

- **Product-by-product breakdown for each pricing plan** : Check out the[Firebase pricing page](https://firebase.google.com/pricing). On that page, you can learn about the no-cost Firebase products, no-cost usage quotas, and pay-as-you-go pricing for Firebase products.

- **Product-specific information about usage, quotas, and pricing** : Check out the product-specific documentation. These pages often provide usage-to-billing examples for the product and any limitations for specific features (for example,Crashlyticslimits custom logging to 64kB). Visit each product's section in the Firebase documentation to find this type of information.

### Relationship between projects, apps, and billing

| [All Firebase projects are actuallyGoogle Cloudprojects](https://firebase.google.com/docs/projects/learn-more#firebase-cloud-relationship)behind the scenes, which means billing is shared across Firebase andGoogle Cloudand you can view the same project in both theFirebaseconsole and theGoogle Cloudconsole.
| **Important:** **Firebase pricing plans apply to the entire project, not just to individual apps registered in the project.** When you're determining which pricing plan is right for you, consider the usage from*all the apps* registered in the same project. Learn more about[best practices](https://firebase.google.com/docs/projects/dev-workflows/general-best-practices)for when to add multiple apps to the same Firebase project.

The following illustration shows how pricing plans (and billing accounts) are associated with projects and apps.

![Relationship between pricing plans and projects and apps](https://firebase.google.com/docs/projects/images/billing_billingAcct-projects-apps-pricingPlan.png)

<br />

*** ** * ** ***

## **Spark pricing plan**

When you're in the initial stages of developing your app, start out with the no-cost Spark pricing plan. You don't need to provide any payment information to get started using most Firebase features right away!

And if you're*only* using no-cost Firebase products, likeRemote ConfigandCrashlytics, you can use the Spark plan in production apps.  
Which Firebase products are considered "no-cost" vs "paid"?
> **Firebase products that are no-cost**   
> No matter which Firebase pricing plan your project uses, you get full usage of the following Firebase products at no charge --- even in your production apps and*even if you have several million users!*
>
> |---------------------------------------------------------------------|----------------------------------------------------------------|-------------------------------------------------------|
> | A/B Testing App Check App Distribution Authentication(most options) | Cloud Messaging(FCM) Crashlytics Firebase ML(model deployment) | In-App Messaging Performance Monitoring Remote Config |
>
> **Firebase products with a paid-tier of usage**   
> No matter which Firebase pricing plan your project uses, you get no-cost usage quota for the following Firebase products. If your project is on the Blaze plan, you also get pay-as-you-go pricing for additional usage.
>
> |---------------------------------------------------------------------------------------------|----------------------------------------------------------|----------------------------------------------|
> | App HostingandHosting Authentication(phone) Firebase Phone Number Verification Data Connect | Extensions Cloud Firestore Cloud Storage Cloud Functions | Realtime Database Test Lab Firebase AI Logic |
>
> For full details about the Firebase pricing plans (especially about[Cloud Functions](https://firebase.google.com/support/faq#storage-charge)andGoogle Cloudproducts), check out the[Firebase pricing page](https://firebase.google.com/pricing).

### What's included with the Spark plan?

The Spark plan includes the following access to services:

- Full usage of the no-cost Firebase products and features**\*** (like social sign-in methods,Remote Config, andCrashlytics)
- No-cost usage quotas for paid Firebase products (likeCloud Firestore,Cloud Storage, andHosting)

^\**No-cost products still have limitations associated with specific features (for example,Crashlyticslimits custom logging to 64kB). Visit each product's section in the Firebase documentation to find this type of information.*^

### Example scenarios

Here are some examples of usage and billing on the Spark plan:

- Example 1: Your app uses social sign-in methods,Remote Config, andCrashlytics. You get access to all of the features in these three products --- at no cost ---*even if your app has several million users*.

- Example 2: Your app uses customAuthentication,Crashlytics, andCloud Firestore. You get access to all the features for customAuthenticationandCrashlytics(no matter how many users you have), plus you get 20,000Cloud Firestoredocument writes and 50,000 document reads every day --- at no cost.

### Important facts to remember about the Spark plan

Note the following about the Spark pricing plan:

- If you exceed the no-cost quota limit in a calendar month for any product,*your project's usage of that specific product will be shut off for the remainder of that month*.

  - This applies to*all apps*registered with that Firebase project.

  - To use that specific product again, you'll need to wait until the next billing cycle or[upgrade to the Blaze pricing plan](https://console.firebase.google.com/project/_/overview?purchaseBillingPlan=metered).

- No-cost products still have limitations associated with specific features (for example,Crashlyticslimits custom logging to 64kB). Visit each product's section in the Firebase documentation to find this type of information. Depending on the product or feature, these limitations may be due to factors like infrastructure, fair access, and other service protections.

- PaidGoogle Cloudproducts and features (likePub/Sub,Cloud Run, orBigQuerystreaming forAnalytics) are not available for projects on the Spark plan.

| **Important:** Review the sections at the bottom of this page about[switching between pricing plans](https://firebase.google.com/docs/projects/billing/firebase-pricing-plans#switch-between-pricing-plans). Some actions and scenarios may*automatically* switch the pricing plan for your project. For example,**linking aCloud Billingaccount to your project will auto-upgrade your project to the Blaze pricing plan**.

<br />

*** ** * ** ***

## **Blaze pricing plan**

You can upgrade to the pay-as-you-go Blaze pricing plan if your app requires the capabilities provided by the paid services and/or if you want increased quota (for the products that offer this on the Blaze plan).

A Firebase project on the Blaze plan has a[Cloud Billingaccount](https://firebase.google.com/docs/projects/billing/firebase-pricing-plans#cloud-billing-accounts)linked to it, which enables your project and apps to access more services and often higher usage levels.
| When your project is on the Blaze pricing plan,[**set up budget alerts**](https://firebase.google.com/docs/projects/billing/avoid-surprise-bills#set-up-budget-alert-emails)using the console. You can use the[Blaze plan calculator](https://firebase.google.com/pricing#blaze-calculator)to estimate your monthly costs.
|
| Be aware that**budget alerts do*not*cap your usage or charges** --- they are*alerts* about your costs so that you can take action, if needed. For example, you might consider[using budget notifications to programmatically disableCloud Billingon a project](https://cloud.google.com/billing/docs/how-to/disable-billing-with-notifications).
| **Important:** If you're usingGoogle Cloudcredits that are provided in aCloud Billingaccount (for example, the["Google Cloud$300 Free Trial"](https://firebase.google.com/support/faq#pricing-free-trial)) and you link that billing account to your project, then your project is automatically upgraded to the Blaze pricing plan. Note that any usage or costs beyond those credits is determined by the credits program that you're using.

### What's included with the Blaze plan?

The Blaze plan includes the following access to services:

- Full usage of the no-cost Firebase products and features**\*** (like social sign-in methods,Remote Config, andCrashlytics)

- No-cost usage quotas for paid Firebase products (likeCloud Firestore,Cloud Storage, andHosting)

- Pay-as-you-go pricing for any additional usage of paid Firebase products

- No-cost usage quota forCloud Functions for Firebase, then pay-as-you-go pricing

- Access to paidGoogle Cloudproducts and features (likePub/Sub,Cloud Run, orBigQuerystreaming forAnalytics)

^\**No-cost products still have limitations associated with specific features (for example,Crashlyticslimits custom logging to 64kB). Visit each product's section in the Firebase documentation to find this type of information.*^

If your project stays within the Blaze plan's no-cost usage quotas for paid products, then you won't see any charges for those products (with the[exception ofCloud Functions](https://firebase.google.com/support/faq#storage-charge)). But if you do happen to exceed the no-cost usage quota, you only pay for the resources that you consume --- this is why the Blaze plan is called the "pay-as-you-go" plan.

### Example scenarios

Here are some examples of usage and billing on the Blaze plan:

- Example 1: Your app uses social sign-in methods,Remote Config, andCrashlytics. You get access to all of the features in these three products --- at no cost ---*even if your app has several million users*.

- Example 2: Your app uses customAuthentication,Crashlytics, andCloud Firestore. You get access to all the features for customAuthenticationandCrashlytics(no matter how many users you have), plus you get 50,000Cloud Firestoredocument reads and 20,000 document writes every day --- at no cost.

  However, if your project's usage ofCloud Firestoreis*higher* than those daily quotas, you're charged for the reads and writes that day which*exceed*the 50K or 20K count.

### Important facts to remember about the Blaze plan

Note the following about the Blaze pricing plan:

- Depending on the product, the amount of no-cost usage quota available for the Spark vs Blaze plan may be different. Read more in this[FAQ](https://firebase.google.com/support/faq#pricing-blaze-no-cost).

- No-cost products still have limitations associated with specific features (for example,Crashlyticslimits custom logging to 64kB). Visit each product's section in the Firebase documentation to find this type of information. Depending on the product or feature, these limitations may be due to factors like infrastructure, fair access, and other service protections.

- Most Firebase products and features have quotas and pricing based on a daily usage, but some are based on monthly or hourly usage.Cloud Functions, for example, has a no-cost usage tier that resets every month, butCloud FirestoreandCloud Storagehave no-cost tiers that reset every day. Read more in this[FAQ](https://firebase.google.com/support/faq#pricing-blaze-no-cost).

| **Important:** Review the sections at the bottom of this page about[switching between pricing plans](https://firebase.google.com/docs/projects/billing/firebase-pricing-plans#switch-between-pricing-plans). Some actions and scenarios may*automatically* switch the pricing plan for your project. For example,**linking aCloud Billingaccount to your project will auto-upgrade your project to the Blaze pricing plan**.

## **GoogleCloud Billingaccounts**

When your project is on the Blaze pricing plan, your project is linked to a[GoogleCloud Billingaccount](https://cloud.google.com/billing/docs). Here are some quick facts aboutCloud Billingaccounts:

- Cloud Billingaccounts require a payment method. This includes most major credit cards as well as other payment methods. For detailed information, see the[Cloud Billingdocumentation](https://cloud.google.com/billing/docs/how-to/payment-methods#available_payment_methods).

- You can link multiple Firebase projects to a singleCloud Billingaccount. All these projects will be on the Blaze pricing plan.

- Check if you're eligible for credits. For example, if you're new to Firebase andGoogle Cloud, you might be eligible for the["Google Cloud$300 Free Trial"](https://firebase.google.com/support/faq#pricing-free-trial)to try out our services. Note that any usage or costs beyond those credits is determined by the credits program that you're using.

<br />

*** ** * ** ***

## **Switching between pricing plans**

| Some actions and situations may***automatically***switch your pricing plan between Spark and Blaze. Learn more in the following sections.

### Upgrading from Spark to Blaze

You can[upgrade to the Blaze pricing plan](https://console.firebase.google.com/project/_/overview?purchaseBillingPlan=metered)in theFirebaseconsole.

For all intents and purposes, upgrading a Firebase project to the Blaze pricing plan means that you're linking aCloud Billingaccount to the underlyingGoogle Cloudproject.

#### The following actions and situations will*automatically upgrade*your pricing plan from Spark to Blaze:

- Linking aCloud Billingaccount to your project from within theGoogle Cloudconsole

- UsingGoogle Cloudservices (likePub/SuborCloud Run) or Google Maps APIs in the same project

  For example, if you start using aGoogle Cloudservice from within theGoogle Cloudconsole, you'll be required to link aCloud Billingaccount --- this automatically upgrades your Firebase pricing plan to the Blaze plan.

#### If your project upgrades from Spark to Blaze, be aware of what will happen:

- Depending on the product, the amount of no-cost usage quota available for the Spark vs Blaze plan may be different. Read more in this[FAQ](https://firebase.google.com/support/faq#pricing-blaze-no-cost).

### Downgrading from Blaze to Spark plan

You can[downgrade to the Spark pricing plan](https://console.firebase.google.com/project/_/overview?purchaseBillingPlan=metered)in theFirebaseconsole.

#### The following actions and situations will*automatically downgrade*your pricing plan from Blaze to Spark:

- Unlinking aCloud Billingaccount from your project from within theGoogle Cloudconsole

- Closing theCloud Billingaccount linked to your project  
  Note thatCloud Billingcan close accounts based on the payment status or history. Learn how to[resolveCloud Billingissues](https://cloud.google.com/billing/docs/how-to/resolve-issues).

#### If your project downgrades from Blaze to Spark, be aware of what will happen:

- Your project loses access to any paidGoogle Cloudservices, likePub/Sub,Cloud Run, orBigQuerystreaming forAnalytics.

- Your project loses access to any non-defaultRealtime Databaseinstances or non-defaultCloud Storagebuckets.

  - *The data in these instances and buckets doesn't get deleted*, but you won't have access to the data (meaning no read/write access from your app, no console access, and no REST API access).

  - To re-enable access,[upgrade to the Blaze pricing plan](https://console.firebase.google.com/project/_/overview?purchaseBillingPlan=metered).

  - If you need to delete the data from these non-default instances and buckets, but remain on the Spark plan,[contact Firebase Support](https://firebase.google.com/support/troubleshooter/contact).

- You cannot do*new* deploys of any new or any existingCloud Functions.

- Depending on the product, the amount of no-cost usage quota available for the Spark vs Blaze plan may be different. Read more in this[FAQ](https://firebase.google.com/support/faq#pricing-blaze-no-cost).

<br />

*** ** * ** ***

## **Next steps**

- Check out the Firebase[pricing FAQs](https://firebase.google.com/support/faq#pricing)for answers to several specific situations, especially for billing related to[Cloud Functions for Firebase](https://firebase.google.com/support/faq#functions-pricing).

- Learn how to[avoid surprise bills](https://firebase.google.com/docs/projects/billing/avoid-surprise-bills)by testing your code, monitoring your usage and spend levels, and setting up budget alert emails.