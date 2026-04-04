# Source: https://docs.zapier.com/platform/build/static-ip.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Enable static IP address connection for customers

> To enable customers to access your integration by static IP address, all outbound traffic from Zapier to your integration will need to be routed through a smaller set of consistent IP addresses. Any app owner/developer can request to enable the static IP address feature on a private or public app.

## Traffic from Zapier

Traffic from Zapier uses the following IP addresses:

* 44.214.195.64/28 (us-east-1)
* 18.246.81.208/28 (us-west-2)

Enabling this feature will increase the volume of requests to your server received from these IP addresses. This means this change would affect all users of your integration who are on a Zapier Teams, Company, or Enterprise plan.

Review our documentation on how the [static IP address functions within Zapier](https://help.zapier.com/hc/en-us/articles/15406083674509-Use-a-static-IP-address-to-connect-to-Zapier).

## How to enable static IP address connection

1. **Consult with your Security team:** They can confirm if a static IP address is permitted within your network security policies and advise on any potential conflicts with existing security measures.

2. **Enable the feature:**
   * **For private integrations:** Navigate to the **Settings** tab on the **Advanced** page in the Platform UI. You'll find a toggle to enable static IP addresses for your integration. As a [team member](/platform/manage/add-team), you can turn this on yourself without contacting support.

   * **For published integrations:** [Contact Zapier Support](https://developer.zapier.com/contact) to enable static IP addresses for your integration. The turnaround time is typically within 1 business day.

## Testing the Static IP in the Platform UI

Static IP addresses are only used for requests sent from paid Zapier accounts (Pro, Teams, or Enterprise plans). This applies to testing within the Platform UI as well.

When testing an authentication, trigger, or action from the Platform UI:

* If the integration team member running the test is part of a paid Zapier account, the request will be sent using Zapier’s static IP addresses.
* If the integration team member is on a free Zapier account and not part of a Team or Enterprise plan, the request will not use static IP addresses.

***

*Need help? [Tell us about your problem](https://developer.zapier.com/contact) and we'll connect you with the right resource or contact support.*
