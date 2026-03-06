# Source: https://docs.salad.com/transcription/explanation/billing.md

# Source: https://docs.salad.com/container-engine/explanation/billing-pricing/billing.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Billing

*Last Updated: November 06, 2025*

# Prepaid Billing

SaladCloud used prepaid billing. In order to keep your organization's workloads active, you must maintain a positive
credit balance. There are two options to do this on SaladCloud: Auto Recharge and Manual Recharge.

## Auto Recharge

SaladCloud recommends enabling auto recharge for organizations serving production workloads to ensure uninterrupted
service. With auto recharge, you configure a threshold and recharge amount, allowing SaladCloud to automatically
replenish your organization’s credit balance when needed.

•	Recharge Threshold: The balance level that triggers an auto recharge ("when my balance falls below").

•	Recharge Amount: The predefined amount SaladCloud charges to your payment method when the threshold is reached ("bring credit balance back up to").

You can update these settings anytime through the Billing & Usage page in your organization’s portal. If you set the
recharge threshold to an amount higher than your current credit balance, an auto recharge will be triggered immediately
upon saving the updated settings.

<img src="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/auto-recharge.png?fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=15f1fb7907e25192795591124e270e0d" width="600" data-og-width="1300" data-og-height="1154" data-path="container-engine/images/auto-recharge.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/auto-recharge.png?w=280&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=b69005a26b926f10ee5a9e9002953faa 280w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/auto-recharge.png?w=560&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=fa3ccb3d2cf8e55062b5931c3aad3e37 560w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/auto-recharge.png?w=840&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=eb44815a0c3e461a239bc6ad90c36e05 840w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/auto-recharge.png?w=1100&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=dc469747360a4f7ec70bd6b08f9bf092 1100w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/auto-recharge.png?w=1650&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=4b9060aa1e2daea38236b774498c7306 1650w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/auto-recharge.png?w=2500&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=2a467a10e80c78bea498597be9e0c8ef 2500w" />

If an auto recharge encounters an error with the payment method, SaladCloud sends an email notification, and the
organization’s workloads are given a grace period to resolve the issue. If the issue is not resolved promptly,
SaladCloud reserves the right to stop all active workloads and API usage.

## Manual Recharge

Manual credit recharges provide an alternative way to maintain a positive credit balance for your organization. At any
time, you can add up to \$10,000 in credits to your account by clicking the “Add to Credit Balance” button on the Billing
& Usage page.

<img src="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/manual-recharge.png?fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=1de3d3d271181bdb31598dac7af26a2f" width="600" data-og-width="1282" data-og-height="922" data-path="container-engine/images/manual-recharge.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/manual-recharge.png?w=280&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=043b51bd49b743a5a85d8175b95d9adb 280w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/manual-recharge.png?w=560&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=54334369096022a0ac297e646e3f0412 560w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/manual-recharge.png?w=840&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=1bc284db7b33f224da5f34f68702a562 840w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/manual-recharge.png?w=1100&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=60b334ad74ed42ba1293d4a6cc148033 1100w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/manual-recharge.png?w=1650&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=579c3f1ccfa10bb1f592987b48d534e2 1650w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/manual-recharge.png?w=2500&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=84cc5337803f592d94351213fcae5911 2500w" />

For amounts exceeding \$10,000, please refer to our volume discount instructions below.

If your organization is not enrolled in auto recharge and the account balance reaches \$0.00, all active workloads and
API usage will stop immediately until a positive credit balance is restored. For organizations running production
workloads, SaladCloud strongly recommends enabling auto recharge to prevent service interruptions.

# How Are Charges Calculated?

SaladCloud only charges for the hardware resources that are dedicated to your application while your container is
Running on one of our machines. Our flexible billing model allows you to customize each machine to your exact hardware
requirements, no more selecting an instance type from an endlessly long pricing sheet.

## Hardware Resources

When creating a Container Group in SCE, you select the required hardware that will be dedicated to your application when
it runs on SaladCloud. The current rate for each type of hardware can be found on our
[pricing page](https://salad.com/pricing). For GPU container groups, there are no additional charges for RAM and vCPU.

### Example 1

You create a Container Group with 1 vCPU, 2 GB RAM, no GPU, and 10 replicas

Per Instance Cost = 1 vCPU x $0.004 per vCPU + 2 GB x $0.001 per GB = \$0.006/hr

**Total Cost** = $0.006/hr (per Instance) x 10 replicas = $0.06/hr

### Example 2

You create a Container Group with 4 vCPU, 6 GB RAM, RTX 3060 GPU at "Low" priority, and 5 replicas

Per Instance Cost = 1 RTX 3060 at "Low" Priority x $0.047 = $0.047/hr

**Total Cost** = $0.047/hr (per Instance) x 5 replicas = $0.235 /hr

## Running Time

SaladCloud bills for the time that the selected hardware resources are dedicated to your application, although it is
common to see hourly rates listed on Salad, usage is tracked per second.

> 🎉 Never Pay for Cold Boot Time Again
>
> You only pay for the time that the hardware is available to used by your application, you will never pay for Cold Boot
> time.

<img src="https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/deployment-map.png?fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=04e3d3853f227e1f2bc0439f75fb3447" data-og-width="1668" width="1668" data-og-height="354" height="354" data-path="container-engine/images/deployment-map.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/deployment-map.png?w=280&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=088e9c85f7e77a8f4007086997f60aa3 280w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/deployment-map.png?w=560&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=852ef734ab308e5d0f9908acb21c8b57 560w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/deployment-map.png?w=840&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=6920f62a52c1ea56c45fd35b3b2e16c1 840w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/deployment-map.png?w=1100&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=6cfc163789053959dedff8d7a7f651ee 1100w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/deployment-map.png?w=1650&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=9dd2e67e4a1c4e7bf290e72592972cc7 1650w, https://mintcdn.com/salad/4KO858akQWmRXuML/container-engine/images/deployment-map.png?w=2500&fit=max&auto=format&n=4KO858akQWmRXuML&q=85&s=2950bb44a772e5ac46f5695c82c50b6b 2500w" />

# Monitoring Usage

You can monitor the current month's usage and view previous invoices directly in the SaladCloud Portal.

<img src="https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/usage-monitoring.png?fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=6fb8a38f43da6ed134b6514921d33552" data-og-width="1290" width="1290" data-og-height="505" height="505" data-path="container-engine/images/usage-monitoring.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/usage-monitoring.png?w=280&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=ef677da603faac3c825f2419503c5955 280w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/usage-monitoring.png?w=560&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=0842322a3dec33959607aa41d7d74ddd 560w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/usage-monitoring.png?w=840&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=5a71d58591326fd04d6cd8831c00c8da 840w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/usage-monitoring.png?w=1100&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=c20efdb2aea7050ef8e57fd3c583b45f 1100w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/usage-monitoring.png?w=1650&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=9d6da8f4e75d25ef494de71657df38d9 1650w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/usage-monitoring.png?w=2500&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=1f4755db1e8c7dc1a4f8c552db447013 2500w" />

## Volume Discounts

SaladCloud offers volume pricing through prepaid credit purchases. You can bulk purchase SaladCloud usage credits at the
following discounted rates:

| Pre-Paid Amount     | Discount      |
| ------------------- | ------------- |
| $10,000 - $24,999   | 2%            |
| $25,000 - $49,999   | 4%            |
| $50,000 - $74,999   | 6%            |
| $75,000 - $99,999   | 8%            |
| $100,000 - $150,000 | 10%           |
| Above \$150,000     | Talk to Sales |

For purchases above \$150,000 or to complete a volume credit purchase, contact us at
[sales@salad.com](mailto:sales@salad.com).

# Preauthorization Requests

We may send a preauthorization request to the issuing bank to verify a bank will authorize charges. Some credit card
companies present these as real charges, which may surprise you.

A preauth is really just a hold on a credit card. We'll typically preauthorize a small amount (usually \$10) when a new
payment method is added to your Organization, then cancel the authorization immediately. Banks may show the preauth for
up to 7 days, even though we have not collected any money.

# Accepted Payment Types

SaladCloud only accepts valid credit and debit cards as a payment method through the SaladCloud portal. Prepaid cards
are not accepted. For additional payment methods, please reach out to [sales@salad.com](mailto:sales@salad.com).
