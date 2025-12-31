# Source: https://docs.meshconnect.com/advanced/sub-client-branding.md

# Sub-Client Branding

### What are Sub-Clients, and why would you register them with Mesh?

If your product is used directly by end-users, this is likely not relevant to you. However, if your product is usually embedded in other products, then this is important. A sub-client is the product that yours is embedded in.

For example, if Mesh’s client is Retailer A, they might embed Mesh Pay directly into their checkout experience, and there is no sub-client involved. In this scenario, the Mesh Link modal would have Retailer A branding everywhere to create a seamlessly embedded experience. However, some of our clients are also embedded products. For example, if our client is Payment Processor A, they might have a whole portfolio of clients that they power payments for (eg. Retailer A, Retailer B, etc.). In this scenario, they may want the Mesh Link branding experience to be all about their sub-client (eg. Retailer A or Retailer B) so the end-user still feels embedded in their shopping experience.

Registering a sub-client with Mesh allows you to ensure that the branding in Mesh Link is consistent with that of the client whose product it is being rendered in.

> Important: this isn’t just about branding. This is also for compliance. Mesh needs to know where our product is being used. So even if the branding will show your company’s name & logo (not your client’s), **all resellers must register subclients**. You can add your own name for display name and your own icon for branding. But we must know the legal business name for your subclients, and we must know which subclient each transaction pertains to.

### How do you register a subClient?

* Notify your Mesh representative that you need this functionality and an Admin will turn it on for your account.
* In the Mesh Dashboard, [in Account —> Link configuration you will see a new “Clients” tab](https://dashboard.meshconnect.com/company/link/clients).
* Click “Add a client”
* Add the Business legal name, Display name, Callback URL(s), and icon relevant for that client.
* Click Save.

### How can you ensure the appropriate branding is used when you call Link?

* You will then see a Client ID for that client. You can pass this value in the `subClientId` field in a /api/v1/linktoken request. This will ensure that Link takes on the branding of that sub-client.
* You can also test this out in our interactive demos. For example in the [Mesh Portfolio demo](https://dashboard.meshconnect.com/demos/mesh-portfolio), you can select a registered client from the “Sub-client” drop-down before clicking on “Connect your account.”
