# Source: https://plivo.com/docs/voice/concepts/geo-permissions.md

# Source: https://plivo.com/docs/sip-trunking/concepts/geo-permissions.md

# Source: https://plivo.com/docs/messaging/concepts/geo-permissions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Messaging Geo Permissions

> Control which countries can receive your SMS traffic to prevent fraud

Plivo recommends that all customers set appropriate Geo Permissions to help curb the risk of SMS fraud, such as [SMS pumping](https://www.plivo.com/blog/sms-pumping/ "What is SMS Pumping") and account token takeover.

Geo Permissions allows you to control the countries to which your SMS traffic is sent. Once a country is enabled, you can set a threshold in MPH (Messages per Hour), which limits the number of messages that can be sent to that country per hour. Messages to countries not enabled on your destination list are blocked immediately at the API level, and you are not charged for them.

Note: Messaging Geo Permissions apply only to SMS and MMS traffic.

<Frame>
    <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/msg-geo-permission-image-1.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=d500e58fa74422bf25842c020ec72692" alt="Geo Permission" width="2868" height="1382" data-path="images/msg-geo-permission-image-1.png" />
</Frame>

Secure your account by disabling SMS permissions for countries in which you are not active. Set send thresholds to mitigate the risk of SMS pumping fraud. Learn more.

## Configuring Messaging Geo Permissions

You can manage Geo Permissions in the **Plivo Console > SMS > Settings > Geo Permissions**, where you can enable or disable countries based on your business needs. We strongly recommend disabling message sending to countries where you are not active to help protect you from SMS pumping attacks. Some countries are hard-disabled and cannot be enabled directly through the console. In such cases, you will need to contact Plivo Support to enable those countries.

<Frame>
    <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/msg-geo-permission-image-2.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=21d088e6de24cb8ddaec60b3d844c657" alt="How to configure Fraud Shield" width="2872" height="1382" data-path="images/msg-geo-permission-image-2.png" />
</Frame>

When a country is enabled, you can set an MPH threshold for it. We classify destination countries into risk levels (Low, Medium, High) based on fraud potential and historical abuse patterns, and we recommend setting MPH thresholds based on the risk levels of the countries you are messaging. You will also see recommendations for threshold values based on the last 15 days of activity from your account to the selected destination country.

You have three options for handling a threshold breach:

<Frame>
    <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/msg-geo-permission-image-3.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=cd687ecf050b1be221c8a6f6841e0146" alt="Thrreshold Breach Response" width="2244" height="726" data-path="images/msg-geo-permission-image-3.png" />
</Frame>

* **Block & Alert**: If the number of messages exceeds the set threshold, traffic will be blocked asynchronously with error code 451. You can configure the blocking period for up to 24 hours.
* **Alert Only**: No traffic will be blocked, but you will still receive an alert notifying you of the breach.
* **Ignore**: If this option is selected, the MPH threshold will have no effect, and the system will not enforce any messaging limits for that country.

Note: The MPH threshold only applies if the breach response setting is configured as Block and Alert or Alert Only.

Fraud Shield alerts can be delivered via email as well as via webhooks.

```json  theme={null}
{
  "auth_id": "MARERE12112",
  "destination_country": "US",
  "block": "no",
  "alert_type": "sms_threshold_breach",
  "message": "Take Action. The number of messages sent exceeded the hourly threshold set."
}
```

You can review these settings and make changes on this page.

## Overriding preferences for specific subaccounts

Geo Permissions and MPH thresholds can be managed at the **subaccount level**. By default, the settings for the master account apply to all subaccounts unless overridden.

If the master account has an MPH threshold of 50 for a country and a subaccount has an MPH threshold of 100 for the same country, the total threshold for that country will be 150 messages per hour — 50 from the master account and 100 from the subaccount.

<Frame>
    <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/msg-geo-permission-image-4.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=43a0a2596ec92206af7ba4f69cd8f4d4" alt="Manage Geo Permissions and messages per hour fraud thresholds" width="2880" height="1382" data-path="images/msg-geo-permission-image-4.png" />
</Frame>

To override Geo Permissions for a specific subaccount, select the subaccount from the Accounts dropdown, adjust the preferences, and click Save Changes. Subaccounts that have overridden preferences will show an "Overridden" tag next to them in the account list. To remove this override, go to Geo Permissions, select the subaccount, and click "Remove Override".

By managing your Geo Permissions and thresholds effectively, you can better secure your account and control the flow of SMS traffic to minimise the risk of fraud.
