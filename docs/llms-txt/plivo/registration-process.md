# Source: https://plivo.com/docs/messaging/a2p-10dlc/registration-process.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 10DLC Registration Process for Plivo Customers

> Step-by-step 10DLC registration process — brand, campaign, and number linking

10-digit long code (10DLC) is a service offered by US mobile network operators (MNO) to explicitly allow A2P messaging over long code phone numbers. 10DLC numbers provide lower surcharges, higher throughput, and less content filtering than unregistered long codes.

<Note>
  <strong>Note:</strong> If you don’t send messages to US mobile numbers using long codes, you don’t need to register your phone numbers for 10DLC service.
</Note>

To register for 10DLC service, you must first register your brand, which involves providing information about the business that’s sending messages.

Once the brand is successfully registered, you must register campaigns, the 10DLC term for messaging use cases.

Finally, you must link the phone numbers that you’ll use to send messages with registered campaigns.

Plivo lets businesses perform these tasks on the [10DLC page](https://cx.plivo.com/home) of the Plivo console or by using our [API](/messaging/api/overview/).

## Registration for resellers

Two types of business may register for 10DLC.

* Direct customers are those who send messages for their own business — companies that send one-time passwords to their users for login, for instance.
* Resellers provide communication services to other businesses and use Plivo’s messaging APIs on behalf of their customers.

While registration is straightforward for direct businesses, which need to register just their own brands, it’s a little more complicated for resellers. Resellers must register each of their customers as a separate brand; they may not use their brand as a proxy for their customers’. A violation of this rule is likely to result in the suspension of the brand’s messaging campaigns.

Consider a hypothetical messaging provider, Ovilp Corp., that provides a messaging platform for organizations that send messages in the US. Its customers are hospitals and medical practitioners that might send messages such as

* appointment alerts for patients
* marketing announcements to opted-in customers
* two-factor authentication (2FA) codes for individuals to use to log in to patient portals

Ovilp also has a console for their customers’ tech teams that requires 2FA to log in. This diagram shows this flow in action.

<Frame>
    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/detailed-outline.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=10956c4ce34d0bea0547519bd863b46e" alt="img" width="1446" height="774" data-path="images/detailed-outline.png" />
</Frame>

Ovilp must register its business and each of its clients’ businesses as separate brands and specify their respective use cases (campaigns).

Note: Resellers that don’t have messaging requirements of their own can forgo registering their own business and proceed to register their customers.

To ensure its own messages are registered for 10DLC services, Ovilp must

* Register itself as a brand
* Create a campaign corresponding to its 2FA use case
* Link Plivo long codes to the campaign

Then, per the diagram above,

* For Client A, Ovilp must
  * Register A’s brand
  * Create a campaign for A’s marketing use case
  * Link numbers to this campaign
* For Client B, Ovilp must
  * Register B’s brand
  * Create campaigns for each of B’s use cases, or create a mixed campaign with correct subtypes
  * Link numbers to the campaigns. Note that any number may be linked to only one campaign.

<Frame>
    <img src="https://mintcdn.com/plivo/2TJ0wsMl3kmSwJSX/images/highlevel-outline.png?fit=max&auto=format&n=2TJ0wsMl3kmSwJSX&q=85&s=6d14c82a411cd2faa4cb5e49708a1d21" alt="img" width="1446" height="774" data-path="images/highlevel-outline.png" />
</Frame>

Resellers need to repeat the process for each of their customers.

## 10DLC registration support

Plivo customers can use the console or SDKs to complete registration for themselves and their customers.

On the Plivo console, you can [register brands and campaigns](https://support.plivo.com/hc/en-us/articles/4682352262809-How-to-Register-10DLC-Brands-and-Campaigns) and [link numbers to campaigns](https://support.plivo.com/hc/en-us/articles/4704476885017-How-to-Link-Phone-Numbers-with-Campaigns).

Plivo also offers SDKs ([now in public beta](/messaging/api/10dlc/)) for customers to use to automate the 10DLC registration process. Consider the example of the imaginary entity Ovilp again. To complete 10DLC registration, Ovilp needs to follow a four-step process:

1. **Create a profile:** Before registering a brand or campaign, Ovilp should identify each of its clients’ types of business — private, public, nonprofit, government, or individual. Plivo uses that information and the [Profile API](/messaging/api/10dlc/profile/) to create a profile for each client, providing the correct business information. A profile contains information about Plivo customers’ (and their clients’) businesses, such as legal name, authorized contact, and business registration details. Profiles help Plivo understand its customers and help us unlock multiple communication services like 10DLC and STIR/SHAKEN (coming soon).

2. **Register a brand:** Once each client has a profile, Ovilp can register a brand for each client using the [Brand API](/messaging/api/10dlc/brand/). Each profile can create only one brand. For optimal throughput for Standard brands, opt in to vetting.

   Check the registration\_status field in the Brand API response to check the status of brand registration. It will show up as COMPLETED when the brand has been successfully registered with The Campaign Registry (TCR), the company that handles 10DLC registrations on behalf of US carriers.

3. **Register campaigns:** Once the brand is registered, Ovilp can create campaigns to meet the messaging needs of each client either using the console or programmatically using Plivo’s [Campaign API](/messaging/api/10dlc/campaign/). After you create a campaign you can check the registration\_status field in the Campaign API response to get the status of the campaign registration. It will show up as ACTIVE when the campaign has been successfully registered.

4. **Linking numbers to campaigns:** Once campaigns have been registered, Ovilp can link its clients’ existing Plivo long code phone numbers with a campaign using the [Number API](/messaging/api/10dlc/number-linking). You can link no more than 49 numbers to a Standard campaign. Also, sending the same content across multiple source numbers specifically to evade content filters is called snowshoeing and violates all carriers’ acceptable use policies. A snowshoeing violation may result in the suspension of the campaign.

   You can track the status of your number registration using the Number API. Check the status field in the Number response. A value of COMPLETED indicates the number has been successfully linked to the campaign. To link more numbers, you can make more calls to the API.

Once all the brands and campaigns are registered and the numbers are linked, Ovilp and its clients can start using them to send messages to US customers on 10DLC registered routes.

If you no longer need a source number to be linked with a campaign, you can unlink it using the Number API. Unlinking a number is irreversible; if you do it mistakenly, you must link the number to the campaign again to use it for 10DLC.

If you unrent a number, Plivo automatically unlinks it from 10DLC campaigns.

## Things to keep in mind before using 10DLC APIs

To use 10DLC APIs you must have a standard Plivo account with sufficient credits to cover the costs associated with 10DLC registration.

10DLC processes depend on integration with some third-party providers. Requests remain in the PROCESSING stage until all of the processes are complete. You can get the latest status using Plivo’s GET APIs for Brand, Campaign, and Number endpoints.

See our [10DLC registration guidelines](/messaging/a2p-10dlc/registration-guidelines/) for advice on how to register brands and campaigns.
