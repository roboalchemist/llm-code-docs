# Source: https://docs.buildnatively.com/guides/integration/in-app-purchases.md

# In-App Purchases

Before reading this page, please make sure you've set up your RevenueCat account.

{% content-ref url="../setup-revenuecat-app" %}
[setup-revenuecat-app](https://docs.buildnatively.com/guides/setup-revenuecat-app)
{% endcontent-ref %}

* [Bubble.io Plugin](#bubble.io-plugin)
  * [Verify Subscription with Plugin](#how-to-verify-users-subscription)
* [JavaScript SDK](#javascript-sdk)
  * [Verify Subscription with JS](#how-to-verify-subscription-with-js)
* [How to link Stripe & RevenueCat?](#how-to-link-stripe-and-revenuecat)
* [Where to find Package ID?](#where-to-find-package-id)

{% hint style="info" %}
To offer a seamless purchasing experience across platforms, use In-app Purchases for your mobile app users and your preferred web payment processor for website users. The [Browser Info](https://docs.buildnatively.com/guides/integration/browser-info) feature helps you identify the user's platform to apply the correct payment method.
{% endhint %}

### 🧋 Bubble.io Plugin

#### \[Element] Natively - Purchases

**Events:**

* Purchase Success
* Purchase Failed
* Set Customer Success
* Set Customer Failed
* Purchase Cancelled
* Customer ID Received
* Get Price Success
* Get Price Failed
* Restore Purchase Success \[iOS]
* Restore Purchase Failed \[iOS]
* Paywall - purchase success
* Paywall was not presented <mark style="background-color:$info;">//Paywall was not presented.</mark>
* Paywall - cancelled <mark style="background-color:$info;">//Paywall was presented and the user cancelled without executing an action.</mark>
* Paywall - error <mark style="background-color:$info;">//Paywall was presented and an error occurred performing an operation.</mark>
* Paywall - Entitlement ID missing <mark style="background-color:$info;">//Only returned when using \[Action] Show Paywall if needed and Entitlement ID is not provided.</mark>
* Paywall - Offering ID was not found <mark style="background-color:$info;">//Only returned when provided Offering ID is not valid.</mark>&#x20;
* Paywall - restore purchase success \[iOS]

**States:**

* Latest Transaction Id - Transaction Id after **Purchase Package**
* Latest Customer Id - Customer Id after **Set Customer ID** or **Purchase Package**
* Latest Error - Empty if no error&#x20;
* Latest GetPrice price - 9.99
* Latest GetPrice price (Localized) - "$9.99" / "9.99 USD"
* Latest GetPrice currency - "USD", "UAH", etc.
* Latest PurchasePackage packageId

**Actions:**

* Purchase Package - Initiate purchase of product or subscription
  * [Package ID](#where-to-find-package-id)
  * Old Product ID (Android) - Required for upgrading or downgrading an active Android subscription. You can retrieve the current Product ID by using the RevenueCat - Verify Subscription action.
  * Proration (Android) - When a user upgrades or downgrades their subscription on Android, Google Play offers five distinct proration modes. These modes determine exactly when the user is charged and how their billing cycle is adjusted.

    \
    Choosing the right model is essential for managing your revenue and providing a fair experience for your users (e.g., charging them immediately for an upgrade vs. waiting until the next cycle).

    \
    For a detailed breakdown of each specific mode and its implementation logic, please refer to the official [RevenueCat Proration Documentation](https://www.revenuecat.com/blog/engineering/google-proration/).
* Set Customer ID - Link your user's id with RevenueCat customer
  * Customer Identifier - (We're recommending using a **Current User's unique id** to identify customers in the RevenueCat dashboard)
* Reset Customer ID - Unlink Customer ID from a device
* Get Package Price - Returns a price for specific product
* Get Customer ID - Returns a current customer id
* Show Paywall - displays the paywall
  * Offering ID - if not provided, will be shown the default offering.
* Show Paywall if needed - automatically displays the paywall only if the user doesn't have an active entitlement
  * Offering ID - if not provided, will be shown the default offering.
  * Entitlement ID - this field is required.
* Restore Purchase \[iOS] - Restores purchases (Handled by RevenueCat automatically)

**How to use?**

1. Make sure you've [set up your Revenue Cat](https://docs.buildnatively.com/guides/setup-revenuecat-app) for your app
2. Add **revenuecat\_apiKey** in plugin settings. To find **API Key**, go to **RevenueCat App > API keys > Secret API keys**.
3. Call **Set Customer ID**&#x20;
4. When the **Set Customer Success** event fires, call **Purchase Package** action

#### How to verify User's subscription?

{% hint style="info" %}
Make sure you've added revenuecat\_apiKey in plugin settings. To find **API Key**, go to **RevenueCat App > API keys > Secret API keys**. \
\
⚠️⚠️⚠️ MAKE SURE YOU'RE USING API KEY V1
{% endhint %}

**RevenueCat - Verify Subscription**

* Customer ID - Revenue cat user id that was used on RevenueCat Login.

{% hint style="warning" %}
A new customer will be created if the customer with such ID does not exist. More details [here](https://docs.revenuecat.com/reference/subscribers)
{% endhint %}

* Entitlements ID - your entitlements id, more details [here](https://docs.revenuecat.com/docs/entitlements).

Returns a result as:&#x20;

* Product ID - text
* Purchase Date - date
* Grace Period Expires Date - date
* Expiration Date - date
* Is Active - yes / no (**Expiration Date > Current Date**)
* Error - empty text if no error

&#x20;

#### Bubble Setup example:

1. On each User Login or first Signup you need to set the RevenueCat customer ID to your own user's unique id.<br>

   <figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FahoBpzPDkC1oQGSnsZTE%2Fimage.png?alt=media&#x26;token=e0c49acc-24a6-4456-a10b-05dde7d9732a" alt=""><figcaption></figcaption></figure>

2. Purchase a subscription (package) with action<br>

   <figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2F6LP5oSQeBkmdU2IfLJGG%2Fimage.png?alt=media&#x26;token=a4e3faa3-b2a4-4897-814d-da0c1bfc25d7" alt=""><figcaption></figcaption></figure>

3. Verify user's subscription whenever you need it<br>

   <figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FGwoLSV0xDO48hICddzG0%2FSCR-20230130-m80.png?alt=media&#x26;token=3f4cd2e4-ae3d-4bb1-b1d5-c4dead1cfbd7" alt=""><figcaption></figcaption></figure>

   <figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2Fvqo2ZPNwNyNpfUShLLkN%2FSCR-20230130-m86.png?alt=media&#x26;token=cac2ab59-0eca-47ec-af04-0858b10b189d" alt=""><figcaption></figcaption></figure>

4. If you have any issues and, for some reasons, purchases doesn't work. You can check Latest Error value from Natively Purchases element<br>

   <figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2F4oIShe2RAaZfQqSHYZsz%2Fimage.png?alt=media&#x26;token=5b15744f-5756-45ef-93c4-50a8e99852e4" alt=""><figcaption></figcaption></figure>

5. You can also use [RevenueCat API](https://www.revenuecat.com/reference/basic) for your purpose (for example, validation of purchases)<br>

### 🛠 JavaScript SDK

#### NativelyPurchases

{% code overflow="wrap" lineNumbers="true" %}

```javascript
const purchases = new NativelyPurchases();
const login_callback = function(resp) {
    console.log(resp.status); // SUCCESS or FAILED
    console.log(resp.customerId); // Customer Id
    
    // Empty if no error (should contain an error if status === "FAILED"
    console.log(resp.error); 
};

// Link your user with the customer on RevenueCat
const userId = "sdfdsr-2345-3rsd-fsd3432";
const userEmail = "email@example.com";
purchases.login(userId, userEmail, login_callback);

// Unlink your user with the customer on RevenueCat
const logout_callback = function(resp) {
    console.log("Logged out");
}
purchases.logout(logout_callback);

// Get the current user's customer id (Useful in case you're not linking the user with the RevenueCat customer)
const customer_id_callback = function(resp) {
    console.log(resp.customerId);
}
purchases.customerId(customer_id_callback);

// Make a purchase
const packageId = "$rc_monthly";
     // Old Product ID. Android only. Required for upgrading or downgrading a subscription. Enter the Product ID of the user's current active subscription as defined in your Google Play Console.
const oldProductID = "premium"; 
     // Proration Mode. Sets the Android-specific proration behavior for plan changes (upgrade/downgrade).
     // Supported modes: "immediateWithoutProration" (WITHOUT_PRORATION), "immediateWithoutProration" (WITH_TIME_PRORATION), "immediateAndChargeFullPrice" (CHARGE_FULL_PRICE), "immediateAndChargeProratedPrice" (CHARGE_PRORATED_PRICE), "deferred" (DEFERRED).
     // See RevenueCat docs for Android proration modes and their behaviors: https://www.revenuecat.com/blog/engineering/google-proration/
const prorationMode = "immediateWithoutProration";
const purchases_package_callback = function(resp) {
    console.log(resp.status);
    console.log(resp.transactionId); //Legacy. Will not have value in a recent build
    console.log(resp.error);
};
purchases.purchasePackage(packageId, purchases_package_callback, oldProductID, prorationMode);

// Get price
const packageId = "$rc_monthly";
const price_callback = function(resp) {
    console.log(resp.status); // SUCCESS / FAILED
    console.log(resp.price); // "9.99"
    console.log(resp.localized); // "$9.99" or "9.99 USD"
    console.log(resp.currency); // "USD"
    console.log(resp.error); // Empty if no error
};
purchases.packagePrice(packageId, price_callback);

// Restore a purchase
const restore_callback = function(resp) {
    console.log(resp.status); // SUCCESS / FAILED
    console.log(resp.customerId);
    console.log(resp.error);
};
purchases.restore(restore_callback);

// --- Paywalls ---

const show_paywall_callback = function(resp) {
    console.log(resp.status); // SUCCESS or FAILED
    
    // Contains a result message if status === "FAILED" (not_presented, cancelled, error) or status === "SUCCESS" (purchased, restored)
    console.log(resp.message); 
    
    // Empty if no error (should contain an error if status === "FAILED", e.g. entitlement_id_missing, offering_not_found)
    console.log(resp.error); 
};

// Show a paywall
const offeringId = "my_main_offering"; // Optional: specify which offering to show. If not specified, the default will be used
const showCloseButton = true; //This parameter will be overwritten by the paywall's template
purchases.showPaywall(showCloseButton, offeringId, show_paywall_callback);

// Show a paywall if the user doesn't have an active entitlement
const entitlementId = "pro_access"; // This parameter is required
const showCloseButton_ifNeeded = true; // This parameter will be overwritten by the paywall's template
const offeringId_ifNeeded = "my_main_offering"; // Optional: specify which offering to show. If not specified, the default will be used
purchases.showPaywallIfNeeded(entitlementId, showCloseButton_ifNeeded, offeringId_ifNeeded, show_paywall_callback);
```

{% endcode %}

#### How to verify subscription with JS?

You need to fetch a user from RevenueCat API and verify it's entitlements. More details can be found [here](https://docs.revenuecat.com/reference/subscribers#the-entitlement-object).

### Where to find Package ID?

#### You can find it in your RevenueCat App dashboard, more details [here](https://docs.revenuecat.com/docs/entitlements#adding-packages)

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FnvrJmZjA460WsS4nmZQj%2Frc_package_id.gif?alt=media&#x26;token=fda8479f-460b-424b-92bf-4a1f649e5dfa" alt=""><figcaption></figcaption></figure>

### How to link Stripe & RevenueCat (Bubble.io)?

{% hint style="info" %}
We recommend checking [this](https://www.revenuecat.com/docs/stripe/?utm_medium=referral\&utm_source=solp\&utm_campaign=natively\&utm_content=partner) guide if you plan to use a Stripe subscription through RevenueCat.
{% endhint %}

#### How to link Stripe purchases with RevenueCat?

Create a request in [API Connector](https://manual.bubble.io/core-resources/bubble-made-plugins/api-connector) (more details about the endpoint you can find [here](https://www.revenuecat.com/reference/receipts/?utm_medium=referral\&utm_source=solp\&utm_campaign=natively\&utm_content=partner))

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FK1qXM7pCwO2dHfu9Wok4%2FSCR-20220825-thb.png?alt=media&#x26;token=d8afcfd0-acfc-4307-ac2a-ff4a53fbf907" alt=""><figcaption></figcaption></figure>

Where **fetch\_token** & **app\_user\_id** is:

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2F8p82t6dCeS9oYHYBljOB%2Fimage.png?alt=media&#x26;token=a9b6b506-b961-41c6-847f-f1d31cad04ec" alt=""><figcaption></figcaption></figure>
