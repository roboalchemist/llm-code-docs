# Source: https://docs.buildnatively.com/natively-platform/features/purchases.md

# In-app Purchases

### How to set up In-app Purchases?

Turn on the **In-app Purchases** feature and fill out the following information:

* Enter **iOS Api Key** (if you're planning to use it in iOS)
* Enter **Android Api Key** (if you're planning to use it in Android)

### Where to find Android or iOS API Keys?

{% content-ref url="../../guides/setup-revenuecat-app" %}
[setup-revenuecat-app](https://docs.buildnatively.com/guides/setup-revenuecat-app)
{% endcontent-ref %}

### I am already using Stripe for purchases on my website. Do I need to implement In-App Purchases in my app?

Yes, you generally need to implement In-App Purchases (IAP) in your app, particularly for in-app digital goods or services, as mandated by Apple and Google, which charge a 15% or 30% commission. However, there are exceptions where Stripe can be used, especially for transactions involving physical goods, real-world services, or person-to-person services. Stripe offers benefits like lower transaction fees and more flexibility but comes with challenges like potentially lower conversion rates and additional management complexities.&#x20;

For more details, refer to our partner's RevenueCat full article [here](https://www.revenuecat.com/blog/engineering/can-you-use-stripe-for-in-app-purchases/).
