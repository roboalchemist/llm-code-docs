# Source: https://firebase.google.com/docs/tutorials/payments-stripe.md.txt

Using a few different Firebase features and Stripe, you can process payments in your web app without building your own server infrastructure. This guide walks you through customizing and deploying your own version of the open-source[cloud-functions-stripe-sample.web.app](https://cloud-functions-stripe-sample.web.app/)example app.

Before you start, create a project in the[Firebase console](https://console.firebase.google.com)and set up a[Stripe](https://stripe.com/)account.
| **Note:** Our partners at Stripe have introduced two new extensions,[Run Subscription Payments with Stripe](https://firebase.google.com/products/extensions/firestore-stripe-subscriptions)and[Send Invoices using Stripe](https://firebase.google.com/products/extensions/firestore-stripe-invoices), to make it possible to process payments with even less code!

## Implementation overview

1. Set up a[Stripe](https://stripe.com/)account.
2. Create a project in the[Firebase console](https://console.firebase.google.com).
3. Upgrade your project to the[pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing).
4. Configure theFirebaseCLI to use your project with`firebase use --add`.
5. Get the[source code](https://github.com/firebase/functions-samples/tree/main/Node-1st-gen/stripe)for the sample Firestripe app. Configure it with the right information for your project and customize the code to fit your app.
6. Once you've deployed your app, look for a list of users and transactions in the Firebase console.

## Set up and deploy the sample app

1. Get the[source code](https://github.com/firebase/functions-samples/tree/main/Node-1st-gen/stripe).
2. Enable Google \& Email sign-in in your[authentication provider settings](https://console.firebase.google.com/project/_/authentication/providers).
3. Enable[Cloud Firestore](https://console.firebase.google.com/project/_/firestore).
4. Install the[FirebaseCLI](https://github.com/firebase/firebase-tools)if you haven't already, and log in with`firebase login`.
5. Configure this sample to use your project with`firebase use --add`.
6. Install dependencies locally by running`cd functions; npm install; cd -`
7. Add your[Stripe API Secret Key](https://dashboard.stripe.com/account/apikeys)to yourCloud Functionsenvironment configuration:

   `firebase functions:config:set stripe.secret=<YOUR STRIPE SECRET KEY>`
8. Set your[Stripe publishable key](https://dashboard.stripe.com/account/apikeys)in[`/public/javascript/app.js`](https://github.com/firebase/functions-samples/tree/main/Node-1st-gen/stripe/public/javascript/app.js#L16):

   `const STRIPE_PUBLISHABLE_KEY=<YOUR STRIPE PUBLISHABLE KEY>;`
9. Deploy your project using`firebase deploy`. This command:

   1. Sends all the files in the`public`directory toHostingso that your website is available.
   2. Sends the code in the`functions`directory toCloud Functions for Firebase.
   3. Sets security rules on yourCloud Firestoredatabase as configured in`firestore.rules`. The provided rules only allow a user to read and write their own payments and payment methods.

## Test the sample app

Visit your payments app's URL at`your-firebase-project-id.web.app`and verify that the following features work:

- You can sign in via Google or Email.
- You can add a new[Stripe test card](https://stripe.com/docs/testing)and view it in the card select element.
- You can select one of your cards and charge it.
- You can sign out.

For comparison, see[cloud-functions-stripe-sample.web.app](https://cloud-functions-stripe-sample.web.app/).

To provide a streamlined experience for your users, you can further customize your payment page's appearance, or plug it into your existing app.

## View processed payments

Once you've set up and deployed your payments page, you can check the Firebase console and see a list of users along with their payment methods and payments.

1. Go to[Cloud Firestore](https://console.firebase.google.com/project/_/firestore/data).
2. Check for a list of your users and, if they added any credit cards or made any transactions, a list of those under each user.

## Accept live payments

Once you're ready to go live, you'll need to exchange your test keys for your live keys. See the[Stripe docs](https://stripe.com/docs/keys)to learn more about these keys.

1. Update your Stripe secret config:

   `firebase functions:config:set stripe.secret=<YOUR STRIPE LIVE SECRET KEY>`
2. Set your[live publishable key](https://dashboard.stripe.com/account/apikeys)in[`/public/javascript/app.js`](https://github.com/thorsten-stripe/functions-samples/blob/thorsten-stripe/update-stripe-template/stripe/public/javascript/app.js#L16).

3. Redeploy bothCloud FunctionsandHostingfor the changes to take effect:`firebase deploy`.