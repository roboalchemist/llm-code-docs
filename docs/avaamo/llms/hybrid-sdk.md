# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/integrate-with-api-1/hybrid-sdk.md

# Hybrid SDK

Avaamo Platform is offered as a SaaS service that runs on AWS (Amazon Web Services) in multiple regions. All the conversations is through a secure, reliable, and scalable messaging infrastructure where each message is encrypted.&#x20;

Typically, in business involving sensitive data such as banking and insurance or in-cases where the business has strict security measures that require the integration logic and access credentials to stay within the company network. Hence, it is required for the **Avaamo agent** to access on-premise applications and perform bi-directional interactions for providing value-added services to the user.

You can integrate with Avaamo Platform using **Hybrid SDK** that combines the performance, scale, and cost benefits of the cloud with the access control and permission limitations of enterprise data access.

{% hint style="success" %}
**Key Point**: You can clone and use this repository <https://github.com/avaamo/hybrid_sdk>, to get started on Hybrid SDK integration.
{% endhint %}

### Pre-requisites

Ensure that the customer machine must be allowed to connect to the Avaamo servers via HTTPS

### How does it work?

Avaamo agents access company data. The accuracy and security of data is critical to provide a good user experience. Hence, when you are developing an agent, it is important to understand how agents can access company data.

Conventionally, the enterprise application exposes REST API/SOAP Web Services to the internet that can be consumed by the agen&#x74;**.** This approach has the following limitations:

* It opens up the service/data for all kinds of internet hacking.
* Involves full IT services to open ports and set up security.
* Requires exposing unrestricted security credentials with a third party.

Avaamo’s **Hybrid SDK** eliminates these problems by providing native integration SDKs to connect your data/services to the agent. It is easy and secure, where the integration logic and access credentials stay within the company network. The following illustration depicts the overall data flow in the Hybrid SDK:

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-LyZlty5N9ksbx7ciKhe%2F-LyZoHN7QSlPqBCGZma5%2Fhowto-hybrid-sdk.png?alt=media&#x26;token=8bb56102-a83b-4545-bd6a-3f7d51e9ee85" alt=""></div>

1. Avaamo SDK initiates and automatically connects to the Avaamo servers over the HTTPS connection. In this step, Avaamo agent credentials are used. You may initialize your custom logic and connect to your data/services in this step or wait for the agent requests to appear. The SDK handles the connectivity with the Avaamo Conversation engine and acts as the secure pipe to carry messages back and forth from the users.
2. The user sends a message to the agent.
3. Avaamo conversation engine that is driving the conversation with the user determines it needs to access data/service.
4. A request is passed into your integration code via the SDK. Your code connects to your enterprise's systems to fetch necessary data or trigger further actions and a response is sent back to the Conversation engine.
5. The conversation engine processes the service response and replies to the user.

This approach does not require any ports to be opened in the firewall or require you to set up a VPN. The only requirement is the machine must be allowed to connect to the Avaamo servers via HTTPS protocol. It is not even required to enable full internet access to that machine.
