# Source: https://io.net/docs/guides/payment/card-payments-faqs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Card Payment FAQs

> This page answers common questions about using Stripe (Fiat payments) and Credits when purchasing compute or IO Credits.

This page answers common questions about using Card (Fiat) payments when purchasing compute or IO Credits.

## General Payment Logic

**Users can pay for compute in two ways:**

* **IO Credits** — internal platform credits.
* **Fiat via Stripe** — credit/debit cards payment methods.

**Minimum amounts:**

* Purchasing IO Credits — **\$1.00**
* Paying directly with Fiat — **\$0.50**

## FAQ

### Q. Can I use Fiat (Stripe) to pay for compute?

Yes. You can now pay for compute directly using Fiat through Stripe. Minimum amount: **\$0.50**

If the cluster cost is **lower than the \$0.50 minimum card payment**, Stripe will still charge \$0.50, and **the remaining balance is automatically added to your IO Credits**.

<img src="https://mintcdn.com/ionet-cca8037f/7MlFa1mqtDeSHeqe/images/docs/stripe-faq/stripe-1.jpg?fit=max&auto=format&n=7MlFa1mqtDeSHeqe&q=85&s=9cfc91ed79576b04188acbbce9e5487e" alt="Stripe 1 Jp" title="Stripe 1 Jp" className="mx-auto" style={{ width:"71%" }} data-og-width="1425" width="1425" data-og-height="1530" height="1530" data-path="images/docs/stripe-faq/stripe-1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/7MlFa1mqtDeSHeqe/images/docs/stripe-faq/stripe-1.jpg?w=280&fit=max&auto=format&n=7MlFa1mqtDeSHeqe&q=85&s=a73434848583820a1896daae23ca939b 280w, https://mintcdn.com/ionet-cca8037f/7MlFa1mqtDeSHeqe/images/docs/stripe-faq/stripe-1.jpg?w=560&fit=max&auto=format&n=7MlFa1mqtDeSHeqe&q=85&s=930d6ef744d5a9c3ea39c54ee7b46c5a 560w, https://mintcdn.com/ionet-cca8037f/7MlFa1mqtDeSHeqe/images/docs/stripe-faq/stripe-1.jpg?w=840&fit=max&auto=format&n=7MlFa1mqtDeSHeqe&q=85&s=9a6aef3a10939227b99239e8eb0ed741 840w, https://mintcdn.com/ionet-cca8037f/7MlFa1mqtDeSHeqe/images/docs/stripe-faq/stripe-1.jpg?w=1100&fit=max&auto=format&n=7MlFa1mqtDeSHeqe&q=85&s=809042b1b59bfb31d521cbccd5c814a8 1100w, https://mintcdn.com/ionet-cca8037f/7MlFa1mqtDeSHeqe/images/docs/stripe-faq/stripe-1.jpg?w=1650&fit=max&auto=format&n=7MlFa1mqtDeSHeqe&q=85&s=9bc90becd21606975700fbdc6ab7ab84 1650w, https://mintcdn.com/ionet-cca8037f/7MlFa1mqtDeSHeqe/images/docs/stripe-faq/stripe-1.jpg?w=2500&fit=max&auto=format&n=7MlFa1mqtDeSHeqe&q=85&s=13fe0e3a0f9f170cfe7df984c447db42 2500w" />

Stripe will show line items such as:

* `Cluster Cost`
* `Payment Provider Fee`

<img src="https://mintcdn.com/ionet-cca8037f/7MlFa1mqtDeSHeqe/images/docs/stripe-faq/stripe-1-2.jpg?fit=max&auto=format&n=7MlFa1mqtDeSHeqe&q=85&s=2e11730ef15f78c8513ae8872741df7e" alt="Stripe 1 2 Jp" title="Stripe 1 2 Jp" className="mx-auto" style={{ width:"50%" }} data-og-width="930" width="930" data-og-height="712" height="712" data-path="images/docs/stripe-faq/stripe-1-2.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/7MlFa1mqtDeSHeqe/images/docs/stripe-faq/stripe-1-2.jpg?w=280&fit=max&auto=format&n=7MlFa1mqtDeSHeqe&q=85&s=30e82dee385031dcf46faa67fc0920ee 280w, https://mintcdn.com/ionet-cca8037f/7MlFa1mqtDeSHeqe/images/docs/stripe-faq/stripe-1-2.jpg?w=560&fit=max&auto=format&n=7MlFa1mqtDeSHeqe&q=85&s=613cc13ab1210e2b6f39acb6fb55db0c 560w, https://mintcdn.com/ionet-cca8037f/7MlFa1mqtDeSHeqe/images/docs/stripe-faq/stripe-1-2.jpg?w=840&fit=max&auto=format&n=7MlFa1mqtDeSHeqe&q=85&s=1b8351f745c77901e9f496de269c934a 840w, https://mintcdn.com/ionet-cca8037f/7MlFa1mqtDeSHeqe/images/docs/stripe-faq/stripe-1-2.jpg?w=1100&fit=max&auto=format&n=7MlFa1mqtDeSHeqe&q=85&s=50fe053a00eab41b0c6548c57156b865 1100w, https://mintcdn.com/ionet-cca8037f/7MlFa1mqtDeSHeqe/images/docs/stripe-faq/stripe-1-2.jpg?w=1650&fit=max&auto=format&n=7MlFa1mqtDeSHeqe&q=85&s=33fccfc9cf3c4e6c275e088c8b371eb7 1650w, https://mintcdn.com/ionet-cca8037f/7MlFa1mqtDeSHeqe/images/docs/stripe-faq/stripe-1-2.jpg?w=2500&fit=max&auto=format&n=7MlFa1mqtDeSHeqe&q=85&s=474f47638d8c33d93b03ad7150b010ca 2500w" />

### Q. Can I use Fiat to purchase IO Credits?

Yes. You can purchase IO Credits using either Crypto (USDC) or Fiat (Stripe). The minimum amount is **\$1.00**.

Stripe payment page will show line items:

* `IO Credits Cost`
* `Payment Provider Fee`

<img src="https://mintcdn.com/ionet-cca8037f/7MlFa1mqtDeSHeqe/images/docs/stripe-faq/stripe-2-2.jpg?fit=max&auto=format&n=7MlFa1mqtDeSHeqe&q=85&s=80ef59ce64421af1a4814f0f9a0d13e3" alt="Stripe 2 2 Jp" title="Stripe 2 2 Jp" className="mx-auto" style={{ width:"55%" }} data-og-width="930" width="930" data-og-height="712" height="712" data-path="images/docs/stripe-faq/stripe-2-2.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/7MlFa1mqtDeSHeqe/images/docs/stripe-faq/stripe-2-2.jpg?w=280&fit=max&auto=format&n=7MlFa1mqtDeSHeqe&q=85&s=e0b8d529dee8469eace4ec68342ce04f 280w, https://mintcdn.com/ionet-cca8037f/7MlFa1mqtDeSHeqe/images/docs/stripe-faq/stripe-2-2.jpg?w=560&fit=max&auto=format&n=7MlFa1mqtDeSHeqe&q=85&s=3fb982923b25824b2c222e7288e5f728 560w, https://mintcdn.com/ionet-cca8037f/7MlFa1mqtDeSHeqe/images/docs/stripe-faq/stripe-2-2.jpg?w=840&fit=max&auto=format&n=7MlFa1mqtDeSHeqe&q=85&s=28ffb56985a336017f9ff57fd4b118fc 840w, https://mintcdn.com/ionet-cca8037f/7MlFa1mqtDeSHeqe/images/docs/stripe-faq/stripe-2-2.jpg?w=1100&fit=max&auto=format&n=7MlFa1mqtDeSHeqe&q=85&s=2005812ee98ad77633905949dc1430ca 1100w, https://mintcdn.com/ionet-cca8037f/7MlFa1mqtDeSHeqe/images/docs/stripe-faq/stripe-2-2.jpg?w=1650&fit=max&auto=format&n=7MlFa1mqtDeSHeqe&q=85&s=ca98685ac76416e7e2dba05c2d6cc7fb 1650w, https://mintcdn.com/ionet-cca8037f/7MlFa1mqtDeSHeqe/images/docs/stripe-faq/stripe-2-2.jpg?w=2500&fit=max&auto=format&n=7MlFa1mqtDeSHeqe&q=85&s=01184e422654de517aaaadff4309e2ab 2500w" />

After successful payment, credits are added to the user’s IO Credits balance.

### Q. What happens if I already have enough credits?

If your existing IO Credits balance is enough to cover the compute cost then **Fiat (card) payments are disabled**

The following message will appear: `You have sufficient credits to purchase compute. Please proceed to use them.` This ensures credits are used first before showing any Fiat options.

<img src="https://mintcdn.com/ionet-cca8037f/7MlFa1mqtDeSHeqe/images/docs/stripe-faq/stripe-3.jpg?fit=max&auto=format&n=7MlFa1mqtDeSHeqe&q=85&s=09e2c382a360df85945f03cf8b116096" alt="Stripe 3 Jp" title="Stripe 3 Jp" className="mx-auto" style={{ width:"73%" }} data-og-width="1587" width="1587" data-og-height="1383" height="1383" data-path="images/docs/stripe-faq/stripe-3.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/7MlFa1mqtDeSHeqe/images/docs/stripe-faq/stripe-3.jpg?w=280&fit=max&auto=format&n=7MlFa1mqtDeSHeqe&q=85&s=109a7e633d8753f464746a2cf1540e92 280w, https://mintcdn.com/ionet-cca8037f/7MlFa1mqtDeSHeqe/images/docs/stripe-faq/stripe-3.jpg?w=560&fit=max&auto=format&n=7MlFa1mqtDeSHeqe&q=85&s=6d6dd4511a15e69160b7196540633c1c 560w, https://mintcdn.com/ionet-cca8037f/7MlFa1mqtDeSHeqe/images/docs/stripe-faq/stripe-3.jpg?w=840&fit=max&auto=format&n=7MlFa1mqtDeSHeqe&q=85&s=ba26ab1663b63dade9d3e988f93a5b87 840w, https://mintcdn.com/ionet-cca8037f/7MlFa1mqtDeSHeqe/images/docs/stripe-faq/stripe-3.jpg?w=1100&fit=max&auto=format&n=7MlFa1mqtDeSHeqe&q=85&s=9d6af4349f9b6b8cb0328de104e271e9 1100w, https://mintcdn.com/ionet-cca8037f/7MlFa1mqtDeSHeqe/images/docs/stripe-faq/stripe-3.jpg?w=1650&fit=max&auto=format&n=7MlFa1mqtDeSHeqe&q=85&s=658d0af90c8b7a6c261ab40d90adaaec 1650w, https://mintcdn.com/ionet-cca8037f/7MlFa1mqtDeSHeqe/images/docs/stripe-faq/stripe-3.jpg?w=2500&fit=max&auto=format&n=7MlFa1mqtDeSHeqe&q=85&s=5946dc7596323cb26d0361f8da49283a 2500w" />

### Q. Can I extend my compute using Fiat?

Yes. You can extend your compute using Fiat (Stripe). It works the same as initial compute purchase. Minimum fiat amount: **\$0.50**

<img src="https://mintcdn.com/ionet-cca8037f/7MlFa1mqtDeSHeqe/images/docs/stripe-faq/stripe-4.jpg?fit=max&auto=format&n=7MlFa1mqtDeSHeqe&q=85&s=5caf417127a342247cbc1c991ad5344b" alt="Stripe 4 Jp" title="Stripe 4 Jp" className="mx-auto" style={{ width:"64%" }} data-og-width="902" width="902" data-og-height="1052" height="1052" data-path="images/docs/stripe-faq/stripe-4.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/7MlFa1mqtDeSHeqe/images/docs/stripe-faq/stripe-4.jpg?w=280&fit=max&auto=format&n=7MlFa1mqtDeSHeqe&q=85&s=da2b12b505e180b2b45dfac12e42223f 280w, https://mintcdn.com/ionet-cca8037f/7MlFa1mqtDeSHeqe/images/docs/stripe-faq/stripe-4.jpg?w=560&fit=max&auto=format&n=7MlFa1mqtDeSHeqe&q=85&s=9e51c23774b2c721bd513eb84bcc29ff 560w, https://mintcdn.com/ionet-cca8037f/7MlFa1mqtDeSHeqe/images/docs/stripe-faq/stripe-4.jpg?w=840&fit=max&auto=format&n=7MlFa1mqtDeSHeqe&q=85&s=394befc4e9276c33a741b58b8580d763 840w, https://mintcdn.com/ionet-cca8037f/7MlFa1mqtDeSHeqe/images/docs/stripe-faq/stripe-4.jpg?w=1100&fit=max&auto=format&n=7MlFa1mqtDeSHeqe&q=85&s=4a3752c1eca3df0bdf75453457e5068e 1100w, https://mintcdn.com/ionet-cca8037f/7MlFa1mqtDeSHeqe/images/docs/stripe-faq/stripe-4.jpg?w=1650&fit=max&auto=format&n=7MlFa1mqtDeSHeqe&q=85&s=21c4b3e4f5dff07fc98e7ac0da4c9b44 1650w, https://mintcdn.com/ionet-cca8037f/7MlFa1mqtDeSHeqe/images/docs/stripe-faq/stripe-4.jpg?w=2500&fit=max&auto=format&n=7MlFa1mqtDeSHeqe&q=85&s=3502bf8c81b64afb41262b8ad3490bd7 2500w" />

Any leftover amount (after cluster cost + provider fee) is **automatically added to IO Credits.**

<img src="https://mintcdn.com/ionet-cca8037f/7MlFa1mqtDeSHeqe/images/docs/stripe-faq/stripe-4-2.jpg?fit=max&auto=format&n=7MlFa1mqtDeSHeqe&q=85&s=26e72123752239405aed0002d8de39c0" alt="Stripe 4 2 Jp" title="Stripe 4 2 Jp" className="mx-auto" style={{ width:"53%" }} data-og-width="930" width="930" data-og-height="712" height="712" data-path="images/docs/stripe-faq/stripe-4-2.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/7MlFa1mqtDeSHeqe/images/docs/stripe-faq/stripe-4-2.jpg?w=280&fit=max&auto=format&n=7MlFa1mqtDeSHeqe&q=85&s=43c740b15dd5c62507c69034d9445d83 280w, https://mintcdn.com/ionet-cca8037f/7MlFa1mqtDeSHeqe/images/docs/stripe-faq/stripe-4-2.jpg?w=560&fit=max&auto=format&n=7MlFa1mqtDeSHeqe&q=85&s=aa81b7850b6fc29be48f07a04374bfd9 560w, https://mintcdn.com/ionet-cca8037f/7MlFa1mqtDeSHeqe/images/docs/stripe-faq/stripe-4-2.jpg?w=840&fit=max&auto=format&n=7MlFa1mqtDeSHeqe&q=85&s=59a590cb7c9c564cdd05cdac81fe924b 840w, https://mintcdn.com/ionet-cca8037f/7MlFa1mqtDeSHeqe/images/docs/stripe-faq/stripe-4-2.jpg?w=1100&fit=max&auto=format&n=7MlFa1mqtDeSHeqe&q=85&s=868354a1a6269d481ec14d30fb939567 1100w, https://mintcdn.com/ionet-cca8037f/7MlFa1mqtDeSHeqe/images/docs/stripe-faq/stripe-4-2.jpg?w=1650&fit=max&auto=format&n=7MlFa1mqtDeSHeqe&q=85&s=a4e5be35f3053145e109d33ba0dcbb8e 1650w, https://mintcdn.com/ionet-cca8037f/7MlFa1mqtDeSHeqe/images/docs/stripe-faq/stripe-4-2.jpg?w=2500&fit=max&auto=format&n=7MlFa1mqtDeSHeqe&q=85&s=94d632e5fd83f22c6c125764d9cebe7d 2500w" />

### Q. How are fees displayed during payment?

When paying through Stripe, you will see:

* **IO Credits Cost / Compute Cost**
* **Payment Provider Fee**
* **Total Amount**

This breakdown makes the payment fully transparent.

### Q. Can I pay with my local currency?

Yes. If your local currency is supported by Stripe, you should be able to pay using it.

Stripe will automatically handle currency conversion to USD during checkout.

The final amount charged may vary slightly based on exchange rates and your bank’s conversion fees.

### Q. Why am I purchasing credits when I pay by card?

Even when you pay directly by card (Fiat), the system works by first adding the equivalent amount as **IO Credits** to your account and then using those credits to pay for your compute clusters.

This happens automatically in the background, so you might see a small remaining balance added as credits if the cluster cost is less than the minimum card payment amount.
